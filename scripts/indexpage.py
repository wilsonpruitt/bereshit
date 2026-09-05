#!/usr/bin/env python3
"""Shared out/index.html writer, called by render-daf.py and render-map.py when run with no
crux-id (render-all mode). A placeholder nav page — Phase 5 replaces this with the Astro site."""
import json, html

def write_index(root):
    out = root / "out"; out.mkdir(exist_ok=True)
    cruxes = json.load(open(root / "data" / "cruxes.json"))
    built = [c for c in cruxes if c.get("status") == "built"]
    esc = lambda s: html.escape(str(s or ""), quote=True)
    rows = []
    for c in built:
        cid = c["id"]
        links = []
        if (out / f"C-daf-{cid}.html").exists(): links.append(f'<a href="C-daf-{cid}.html">daf</a>')
        if (out / f"B-map-{cid}.html").exists(): links.append(f'<a href="B-map-{cid}.html">map</a>')
        q = c.get("question", {}).get("en", "")
        rows.append(f"<li><b>{esc(cid)}</b> — {esc(q)} ({' · '.join(links) or 'not yet rendered'})</li>")
    page = f"""<!doctype html>
<meta charset="utf-8">
<title>Bereshit / In Principio — built cruxes</title>
<body style="font-family: Georgia, 'Times New Roman', serif; max-width: 640px; margin: 3rem auto; line-height: 1.5;">
<h1>Built cruxes</h1>
<ul>{''.join(rows) or '<li>none built yet</li>'}</ul>
</body>"""
    (out / "index.html").write_text(page)
    print(f"wrote out/index.html ({len(built)} built crux{'es' if len(built) != 1 else ''})")
