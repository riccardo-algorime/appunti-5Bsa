#!/usr/bin/env python3
"""Create optimized study transcriptions by removing non-study slides.

Removed page sections:
- Active Learning / Rispondi exercise slides.
- Green sidebar slides: SOSTENIBILITÀ, SALUTE, and Bosellini PER SAPERNE DI PIÙ.
"""

from __future__ import annotations

import re
from pathlib import Path

SRC = Path("trascrizioni_md")
DST = Path("trascrizioni_md_ottimizzate")

PAGE_RE = re.compile(r"(?m)^## Pagina/Slide (\d+)\s*\n")


def is_removed_page(body: str) -> tuple[bool, str]:
    low = body.lower()

    if "active learning" in low or re.search(r"\brispondi\b", low):
        return True, "Active Learning/Rispondi"

    # Green sidebar editorial slides. Avoid generic occurrences of "verde" used
    # only to describe diagrams, maps, molecules, or labels inside normal content.
    if "sostenibilità" in low:
        return True, "slide verde SOSTENIBILITÀ"
    if "salute" in low and re.search(r"barr[ae].{0,80}verde|verde.{0,80}barr[ae]|\bsalute\b", low, re.S):
        # In these PDFs SALUTE appears as green sidebar pages, not core chapter text.
        return True, "slide verde SALUTE"
    if "per saperne di più" in low and re.search(r"barra verde|titolo della sezione.*verde", low, re.S):
        return True, "slide verde PER SAPERNE DI PIÙ"

    return False, ""


def optimize_file(src: Path, dst: Path) -> tuple[int, int, list[tuple[int, str]]]:
    text = src.read_text(encoding="utf-8")
    matches = list(PAGE_RE.finditer(text))
    if not matches:
        dst.write_text(text, encoding="utf-8")
        return 0, 0, []

    prefix = text[: matches[0].start()].rstrip()
    kept: list[str] = [prefix]
    removed: list[tuple[int, str]] = []

    for idx, match in enumerate(matches):
        page_no = int(match.group(1))
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        section = text[start:end].strip()
        body = text[match.end():end]
        remove, reason = is_removed_page(body)
        if remove:
            removed.append((page_no, reason))
            continue
        kept.append("")
        kept.append(section)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(kept).rstrip() + "\n", encoding="utf-8")
    return len(matches), len(matches) - len(removed), removed


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing source directory: {SRC}")
    DST.mkdir(exist_ok=True)

    total_pages = 0
    total_kept = 0
    total_removed = 0
    for src in sorted(SRC.glob("*.md")):
        dst = DST / src.name
        pages, kept, removed = optimize_file(src, dst)
        total_pages += pages
        total_kept += kept
        total_removed += len(removed)
        removed_s = ", ".join(f"{n} ({reason})" for n, reason in removed) or "-"
        print(f"{src.name}: kept {kept}/{pages}; removed {len(removed)}: {removed_s}")

    print(f"TOTAL kept {total_kept}/{total_pages}; removed {total_removed}")
    print(f"BYTES src {sum(p.stat().st_size for p in SRC.glob('*.md'))}")
    print(f"BYTES dst {sum(p.stat().st_size for p in DST.glob('*.md'))}")


if __name__ == "__main__":
    main()
