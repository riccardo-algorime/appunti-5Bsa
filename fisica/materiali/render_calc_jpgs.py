#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parent
WIDTH = 384
VIEWPORT_HEIGHT = 16000


CSS = """
html, body {
  margin: 0;
  padding: 0;
  width: 384px;
  background: #ffffff;
  color: #111111;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  line-height: 1.22;
}
body {
  box-sizing: border-box;
  padding: 5px 6px 7px 6px;
  overflow-wrap: anywhere;
  word-break: normal;
}
h1 {
  font-size: 18px;
  line-height: 1.1;
  margin: 0 0 6px 0;
  padding: 0 0 4px 0;
  border-bottom: 1px solid #888;
}
h2 {
  font-size: 16px;
  line-height: 1.12;
  margin: 0 0 6px 0;
  padding: 0 0 3px 0;
  border-bottom: 1px solid #aaa;
}
h3 {
  font-size: 14px;
  margin: 7px 0 4px 0;
}
p {
  margin: 4px 0;
}
strong {
  font-weight: 700;
}
em {
  font-style: italic;
}
ul, ol {
  margin: 4px 0 4px 16px;
  padding: 0;
}
li {
  margin: 2px 0;
}
blockquote {
  margin: 5px 0;
  padding: 4px 6px;
  border-left: 3px solid #555;
  background: #f2f2f2;
}
blockquote p {
  margin: 2px 0;
}
hr {
  border: 0;
  border-top: 1px solid #bbb;
  margin: 7px 0;
}
code {
  font-family: "DejaVu Sans Mono", monospace;
  font-size: 11px;
  background: #eeeeee;
  padding: 0 2px;
  border-radius: 2px;
}
pre {
  margin: 4px 0;
  padding: 4px;
  background: #eeeeee;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}
.math.display {
  display: block;
  text-align: center;
  margin: 4px 0;
  overflow: hidden;
}
.MathJax {
  font-size: 92% !important;
}
mjx-container[jax="CHTML"][display="true"] {
  margin: 4px 0 !important;
  overflow-x: hidden !important;
  overflow-y: visible !important;
  max-width: 372px !important;
}
mjx-container {
  max-width: 372px !important;
}
"""


HTML_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=384, initial-scale=1">
<style>{css}</style>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
    processEscapes: true
  }},
  chtml: {{
    scale: 0.90,
    mtextInheritFont: true,
    matchFontHeight: false
  }},
  startup: {{
    pageReady: () => MathJax.startup.defaultPageReady().then(() => {{
      document.body.setAttribute('data-mathjax-ready', '1');
    }})
  }}
}};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
{body}
</body>
</html>
"""


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def pandoc_body(md_path: Path) -> str:
    result = subprocess.run(
        [
            "pandoc",
            "--from=markdown+tex_math_dollars+tex_math_single_backslash",
            "--to=html",
            str(md_path),
        ],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return result.stdout


def crop_and_convert(png_path: Path, jpg_path: Path) -> None:
    img = Image.open(png_path).convert("RGB")
    bg = Image.new("RGB", img.size, "white")
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        _, top, _, bottom = bbox
        top = max(0, top - 2)
        bottom = min(img.height, bottom + 6)
        img = img.crop((0, top, WIDTH, bottom))
    else:
        img = img.crop((0, 0, WIDTH, 216))
    img.save(jpg_path, "JPEG", quality=88, optimize=True, progressive=False)


def render_one(md_path: Path) -> None:
    body = pandoc_body(md_path)
    title = html.escape(md_path.name)
    html_path = md_path.with_name(md_path.name + "--Z.html")
    png_path = md_path.with_name(md_path.name + "--Z.png")
    jpg_path = md_path.with_name(md_path.name + "--Z.jpg")

    html_path.write_text(HTML_TEMPLATE.format(css=CSS, body=body), encoding="utf-8")

    run(
        [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            "--allow-file-access-from-files",
            "--virtual-time-budget=8000",
            f"--window-size={WIDTH},{VIEWPORT_HEIGHT}",
            f"--screenshot={png_path}",
            html_path.resolve().as_uri(),
        ],
        cwd=ROOT,
    )
    crop_and_convert(png_path, jpg_path)
    html_path.unlink(missing_ok=True)
    png_path.unlink(missing_ok=True)
    print(jpg_path.relative_to(ROOT))


def main() -> None:
    targets = sorted((ROOT / "calc").glob("*/*.md"))
    if not targets:
        raise SystemExit("No markdown files found under calc/*/*.md")
    for md_path in targets:
        render_one(md_path)


if __name__ == "__main__":
    main()
