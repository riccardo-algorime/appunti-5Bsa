from pathlib import Path
import subprocess
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "_source"
PNG = ROOT / "png"
JPG = ROOT / "jpg"
PNG.mkdir(exist_ok=True)
JPG.mkdir(exist_ok=True)

CSS = r"""
<style>
html,body{margin:0;padding:0;background:white}
body{width:384px;box-sizing:border-box;padding:5px 7px 7px 7px;color:#050505;font-family:DejaVu Sans,Arial,sans-serif;font-size:14px;line-height:1.14;overflow:hidden}
h1{font-size:18px;line-height:1.05;margin:0 0 5px 0;font-weight:800;border-bottom:2px solid #111;padding-bottom:3px}
h2{font-size:15px;line-height:1.05;margin:7px 0 3px 0;font-weight:800;background:#eee;padding:2px 4px;border-left:4px solid #111}
p{margin:2px 0}
ul,ol{margin:2px 0 3px 17px;padding:0}
li{margin:1px 0}
code{font-family:DejaVu Sans Mono,monospace;font-size:12px;background:#f3f3f3;padding:1px 2px}
pre{margin:3px 0;padding:3px;background:#f5f5f5;border:1px solid #ddd;white-space:pre-wrap;font-family:DejaVu Sans Mono,monospace;font-size:12px;line-height:1.08}
.math.display{display:block;margin:3px 0;padding:2px 2px;background:#f7f7f7;border:1px solid #ddd;font-size:82%;overflow:visible!important}
.math.inline{font-size:93%}
mjx-container{max-width:100%!important;overflow:visible!important}
mjx-container[jax="CHTML"][display="true"]{margin:.05em 0!important;overflow:visible!important}
svg{max-width:100%;height:auto;margin:3px 0}
::-webkit-scrollbar{display:none;width:0!important;height:0!important}
</style>
<script>
window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']]},chtml:{scale:.82,linebreaks:{automatic:true,width:'container'}},startup:{typeset:true}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
"""


def crop_white(raw: Path, out: Path) -> None:
    im = Image.open(raw).convert("RGB")
    bg = Image.new("RGB", im.size, "white")
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        im = im.crop((0, 0, 384, min(im.height, bbox[3] + 7)))
    else:
        im = im.crop((0, 0, 384, 216))
    im.save(out, "PNG", optimize=True)


for md in sorted(SRC.glob("[0-9][0-9].md")):
    num = md.stem
    body = subprocess.check_output(["pandoc", str(md), "-t", "html", "--mathjax"], text=True)
    html = SRC / f"{num}.html"
    html.write_text(
        '<!doctype html><html><head><meta charset="utf-8">'
        + CSS
        + "</head><body>"
        + body
        + "</body></html>",
        encoding="utf-8",
    )
    raw = SRC / f"{num}.raw.png"
    png = PNG / f"{num}.png"
    jpg = JPG / f"{num}.jpg"
    subprocess.check_call(
        [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--allow-file-access-from-files",
            "--virtual-time-budget=5000",
            "--window-size=384,5000",
            f"--screenshot={raw}",
            f"file://{html}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    crop_white(raw, png)
    subprocess.check_call(
        [
            "magick",
            str(png),
            "-strip",
            "-colorspace",
            "sRGB",
            "-type",
            "TrueColor",
            "-interlace",
            "None",
            "-sampling-factor",
            "4:2:0",
            "-quality",
            "62",
            str(jpg),
        ]
    )
    print(f"{num}.jpg")
