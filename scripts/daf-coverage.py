#!/usr/bin/env python3
"""Every witness on a crux's roster must actually be rendered as a note on that crux's daf, and on
its verse's dialogue page. Run after `npm run build` in site/.

Why this exists. The daf's columns are built by predicate in site/src/pages/crux/[id].astro, and
until Phase 6 part five those predicates covered `latin` and `rabbinic` and nothing else. A witness
on any other bench was built, passed every check.py rule, was listed on the crux roster, got its own
/witnesses/ page, and was then dropped from the daf without a word -- it survived there only as a
thread endpoint inside the JavaScript, so the wires pointed at notes that were not on the page.
That silently hid Philo's eleven witnesses the day they were built, and had been hiding Basil's
three Greek ones since Phase 5. check.py cannot see this: it checks the data, and the data was fine.

Usage: daf-coverage.py [site/dist]
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "site" / "dist"
if not DIST.exists():
    sys.exit(f"no build at {DIST} -- run `npm run build` in site/ first")

cruxes = json.load(open(ROOT / "data" / "cruxes.json"))
W = {fp.stem: json.load(open(fp)) for fp in (ROOT / "data" / "witnesses").glob("*.json")}

def rendered(page):
    return set(re.findall(r'<div class="sn[^"]*"[^>]*id="([^"]+)"', page)) | \
           set(re.findall(r'id="([^"]+)" tabindex="0" role="button"', page))

missing, verses = [], {}
for c in cruxes:
    if c.get("status") != "built": continue
    fp = DIST / "crux" / c["id"] / "index.html"
    if not fp.exists():
        missing.append(f"crux {c['id']}: no page at {fp}"); continue
    on_page = rendered(fp.read_text())
    for wid in c["witnesses"]:
        if wid not in on_page:
            missing.append(f"crux {c['id']}: witness {wid!r} is on the roster but is not a note on the daf "
                           f"(tradition={W[wid]['tradition']!r}, work={W[wid]['work']!r})")
        verses.setdefault(W[wid]["anchor"]["verse"], set()).add(wid)

for ref, wids in verses.items():
    fp = DIST / "dialogue" / ref.replace("gen.", "gen-").replace(".", "-") / "index.html"
    if not fp.exists():
        missing.append(f"dialogue {ref}: no page at {fp}"); continue
    on_page = rendered(fp.read_text())
    for wid in sorted(wids - on_page):
        missing.append(f"dialogue {ref}: witness {wid!r} is anchored here but is not a note on the page "
                       f"(tradition={W[wid]['tradition']!r}, work={W[wid]['work']!r})")

if missing:
    print(f"daf-coverage.py: {len(missing)} witness(es) never reach the ink")
    for m in missing: print(f"  - {m}")
    sys.exit(1)
print(f"daf-coverage.py: clean ({sum(len(v) for v in verses.values())} witness placements checked)")
