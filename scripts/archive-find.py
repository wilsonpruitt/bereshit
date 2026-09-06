"""Locate a phrase in biblia-sacra-lyra_202308 and crop the page image around it.

Kept in the repo because the recipe, not the phrase, is the reusable part -- see PHASES.md.

archive.org's search-inside endpoint returns, for every hit, the LEAF INDEX in the same numbering
that `page/n<N>.jpg` uses, plus a pixel box and the page dimensions the OCR was run against. That
is the only reliable locator for this item: the printed folio numbers are absent from scandata, and
the hOCR page index in Lyra_hocr_pageindex.json.gz is offset from the image leaves by an amount
that DRIFTS along the volume (3 near Genesis 1, 6 by folio 30), so it will silently hand you the
wrong leaf. Boxes are rescaled to the actual image, which is a different size again.

  find.py "phrase"                 -> list hits: leaf, fractional position, OCR context
  find.py "phrase" <k> <up> <down> -> also crop hit k, extending up/down by that fraction of page
"""
import json, subprocess, sys, urllib.parse, pathlib
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
ID = "biblia-sacra-lyra_202308"

q = urllib.parse.quote(sys.argv[1])
url = (f"https://ia600507.us.archive.org/fulltext/inside.php?item_id={ID}"
       f"&doc=Lyra&path=/3/items/{ID}&q={q}")
d = json.loads(subprocess.run(["curl", "-s", url], capture_output=True, text=True).stdout)
hits = []
for m in d.get("matches", []):
    p = m["par"][0]
    hits.append((p["page"], p["l"]/p["page_width"], p["t"]/p["page_height"],
                 p["r"]/p["page_width"], p["b"]/p["page_height"], m["text"]))
for i, h in enumerate(hits):
    print(f"[{i}] n{h[0]}  x {h[1]:.3f}-{h[3]:.3f}  y {h[2]:.3f}-{h[4]:.3f}  :: "
          + h[5].replace("<IA_FTS_MATCH>", "[").replace("</IA_FTS_MATCH>", "]")[:150].replace("\n", " "))
if len(sys.argv) > 2:
    k = int(sys.argv[2]); up = float(sys.argv[3]); down = float(sys.argv[4])
    n, l, t, r, b, _ = hits[k]
    fp = pathlib.Path(f"n{n}_full.jpg")
    if not fp.exists():
        subprocess.run(["curl", "-sL", "-o", str(fp),
                        f"https://archive.org/download/{ID}/page/n{n}.jpg"], check=True)
    im = Image.open(fp); im.draft("L", im.size); W, H = im.size
    # widen to the whole column: the boxes are word-level, the argument is a paragraph
    L = max(0.0, l - 0.14); R = min(1.0, r + 0.16)
    box = (int(L*W), int(max(0.0, t-up)*H), int(R*W), int(min(1.0, b+down)*H))
    o = im.convert("L").crop(box)
    if o.width > 2000: o = o.resize((2000, int(o.height*2000/o.width)), Image.LANCZOS)
    name = sys.argv[5] if len(sys.argv) > 5 else f"hit_n{n}"
    o.save(f"{name}.png"); print(f"-> {name}.png {o.size} leaf n{n} box {box}")
