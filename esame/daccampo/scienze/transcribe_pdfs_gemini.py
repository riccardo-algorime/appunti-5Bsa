#!/usr/bin/env python3
"""Transcribe local PDF slide decks to detailed Markdown with Gemini.

The script is resumable: each page-range chunk is saved under .gemini_pdf_chunks,
then assembled into one Markdown file per PDF under trascrizioni_md/.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "trascrizioni_md"
STATE_DIR = ROOT / ".gemini_pdf_chunks"
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")

SYSTEM_INSTRUCTION = """Sei un trascrittore tecnico-scientifico per materiali di studio liceali.
Il tuo compito è convertire slide/PDF in Markdown ricco, fedele e molto dettagliato.
Non riassumere, non semplificare, non saltare immagini o schemi.
Trascrivi ciò che è presente e descrivi in testo ciò che è visuale.
Se un dettaglio è illeggibile, scrivi [illeggibile] e il contesto.
Rispondi solo con Markdown, senza introduzioni o commenti esterni.
"""

PROMPT_TEMPLATE = """Trascrivi integralmente in Markdown ricco il PDF allegato.

Contesto:
- File originale: {pdf_name}
- Questo allegato contiene le pagine/slide globali {start}-{end} del file originale.
- La pagina 1 dell'allegato corrisponde alla Pagina/Slide {start} globale.

Requisiti obbligatori:
- NON riassumere.
- Mantieni massimo dettaglio e ordine originale.
- Crea una sezione esatta per ogni pagina globale: `## Pagina/Slide N`.
- Devi coprire tutte e sole queste pagine globali: da {start} a {end}.
- Trascrivi tutto il testo leggibile, inclusi titoli, sottotitoli, note, didascalie, etichette, legenda, formule, reazioni, simboli e numerazioni.
- Descrivi in testo immagini, grafici, diagrammi, tabelle, frecce, mappe concettuali, strutture chimiche, cicli metabolici, sezioni geologiche, fotografie, schermate e layout visuali.
- Per immagini scientifiche: spiega cosa mostrano, le parti etichettate, le relazioni/frecce e il concetto didattico.
- Per tabelle: ricostruisci una tabella Markdown quando possibile; altrimenti elenco strutturato.
- Per formule/reazioni: mantieni notazione chimica/scientifica più fedele possibile.
- Non inventare contenuti non visibili.
- Se qualcosa è illeggibile, scrivi `[illeggibile]` e spiega dove si trova.
- Output solo Markdown.
"""


def load_api_key() -> str:
    for env_path in [ROOT / ".env", *ROOT.parents, Path.home()]:
        candidate = env_path if env_path.name == ".env" else env_path / ".env"
        if candidate.exists():
            load_dotenv(candidate, override=False)
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise SystemExit("Missing GEMINI_API_KEY/GOOGLE_API_KEY in environment or .env files")
    return key


def page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", out, re.MULTILINE)
    if not match:
        raise RuntimeError(f"Cannot read page count for {pdf}")
    return int(match.group(1))


def slugify(name: str) -> str:
    value = Path(name).stem
    value = value.replace("’", "_").replace("'", "_")
    value = re.sub(r"[^\w\-.]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "documento"


def make_chunk_pdf(pdf: Path, start: int, end: int, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 0:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pdf_pages_") as tmp:
        tmpdir = Path(tmp)
        pattern = tmpdir / "page-%d.pdf"
        subprocess.check_call(["pdfseparate", "-f", str(start), "-l", str(end), str(pdf), str(pattern)])
        parts = [tmpdir / f"page-{i}.pdf" for i in range(start, end + 1)]
        subprocess.check_call(["pdfunite", *map(str, parts), str(dest)])


def wait_for_file(client: genai.Client, uploaded):
    name = getattr(uploaded, "name", None)
    if not name:
        return uploaded
    for _ in range(120):
        state = getattr(uploaded, "state", None)
        state_name = getattr(state, "name", str(state)) if state is not None else ""
        if "FAILED" in state_name:
            raise RuntimeError(f"Gemini file processing failed for {name}: {state_name}")
        if not state_name or "ACTIVE" in state_name:
            return uploaded
        time.sleep(2)
        uploaded = client.files.get(name=name)
    raise TimeoutError(f"Timed out waiting for Gemini file processing: {name}")


def generate_chunk(client: genai.Client, model: str, pdf: Path, chunk_pdf: Path, start: int, end: int, retries: int) -> str:
    prompt = PROMPT_TEMPLATE.format(pdf_name=pdf.name, start=start, end=end)
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        uploaded = None
        try:
            uploaded = client.files.upload(file=str(chunk_pdf))
            uploaded = wait_for_file(client, uploaded)
            response = client.models.generate_content(
                model=model,
                contents=[prompt, uploaded],
                config=types.GenerateContentConfig(
                    systemInstruction=SYSTEM_INSTRUCTION,
                    temperature=0.1,
                    maxOutputTokens=32768,
                    responseMimeType="text/plain",
                ),
            )
            text = (response.text or "").strip()
            if not text:
                raise RuntimeError("empty Gemini response")
            missing = [n for n in range(start, end + 1) if f"Pagina/Slide {n}" not in text]
            if missing:
                raise RuntimeError(f"response missing page headings: {missing}")
            return text + "\n"
        except Exception as exc:  # noqa: BLE001 - keep resumable CLI robust
            last_error = exc
            wait = min(90, 5 * attempt * attempt)
            print(f"Retry {attempt}/{retries} failed for {pdf.name} pages {start}-{end}: {exc}", file=sys.stderr)
            if attempt < retries:
                time.sleep(wait)
        finally:
            if uploaded is not None and getattr(uploaded, "name", None):
                try:
                    client.files.delete(name=uploaded.name)
                except Exception:
                    pass
    raise RuntimeError(f"Failed {pdf.name} pages {start}-{end}: {last_error}")


def assemble(pdf: Path, chunks: list[tuple[int, int, Path]], out_file: Path) -> None:
    total = page_count(pdf)
    body = [f"# {pdf.stem}\n", f"_Trascrizione dettagliata Markdown del PDF `{pdf.name}`._\n", f"_Pagine/slide totali: {total}._\n"]
    for start, end, chunk_md in chunks:
        text = chunk_md.read_text(encoding="utf-8").strip()
        body.append(f"\n<!-- chunk pages {start}-{end} -->\n")
        body.append(text)
        body.append("\n")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")


def transcribe_pdf(client: genai.Client, model: str, pdf: Path, pages_per_chunk: int, retries: int, force: bool) -> Path:
    total = page_count(pdf)
    slug = slugify(pdf.name)
    pdf_state = STATE_DIR / slug
    out_file = OUT_DIR / f"{slug}.md"
    if out_file.exists() and not force:
        print(f"SKIP complete: {out_file}")
        return out_file

    chunks: list[tuple[int, int, Path]] = []
    for start in range(1, total + 1, pages_per_chunk):
        end = min(total, start + pages_per_chunk - 1)
        chunk_pdf = pdf_state / f"pages_{start:03d}_{end:03d}.pdf"
        chunk_md = pdf_state / f"pages_{start:03d}_{end:03d}.md"
        chunks.append((start, end, chunk_md))
        if chunk_md.exists() and not force:
            print(f"  skip pages {start}-{end}")
            continue
        print(f"  build pages {start}-{end}")
        make_chunk_pdf(pdf, start, end, chunk_pdf)
        text = generate_chunk(client, model, pdf, chunk_pdf, start, end, retries)
        chunk_md.write_text(text, encoding="utf-8")

    assemble(pdf, chunks, out_file)
    print(f"WROTE {out_file}")
    return out_file


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdfs", nargs="*", help="Specific PDF files. Defaults to all *.pdf in this directory.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--pages-per-chunk", type=int, default=4)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not shutil.which("pdfinfo") or not shutil.which("pdfseparate") or not shutil.which("pdfunite"):
        raise SystemExit("Requires pdfinfo, pdfseparate and pdfunite")

    key = load_api_key()
    client = genai.Client(api_key=key)
    pdfs = [Path(p) for p in args.pdfs] if args.pdfs else sorted(ROOT.glob("*.pdf"), key=lambda p: p.name.lower())
    if not pdfs:
        raise SystemExit("No PDF files found")

    for pdf in pdfs:
        print(f"PDF {pdf.name} ({page_count(pdf)} pages)")
        transcribe_pdf(client, args.model, pdf, args.pages_per_chunk, args.retries, args.force)


if __name__ == "__main__":
    main()
