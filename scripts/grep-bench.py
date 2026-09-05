#!/usr/bin/env python3
"""Search the Latin bench TEI for a crux's lemma words, printing each hit with its computed PL
column and surrounding context — the seeding step of the per-crux checklist in PHASES.md.

Usage: grep-bench.py <regex> [work-key ...]   (default: every work in data/latin-bench.json)
       grep-bench.py "dies unus" bede-gen aug-gnl
Options: -c N   context characters either side (default 240)
"""
import json, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bench import ROOT, TEI, tei_text

argv, ctx = sys.argv[1:], 240
if "-c" in argv:
    i = argv.index("-c"); ctx = int(argv[i + 1]); del argv[i:i + 2]
args = [a for a in argv if not a.startswith("-")]
if not args:
    sys.exit(__doc__)
pattern = args[0]
keys = args[1:]

bench = json.load(open(ROOT / "data" / "latin-bench.json"))
if not keys:
    keys = [k for k, v in bench.items() if v.get("idno")]

rx = re.compile(pattern, re.I)
total = 0
for k in keys:
    entry = bench.get(k)
    if not entry or not entry.get("idno"):
        print(f"## {k}: no idno on the bench ({entry.get('note', 'unknown key') if entry else 'unknown key'})")
        continue
    idno = entry["idno"]
    if not (TEI / f"{idno}.xml").exists():
        print(f"## {k} ({idno}): TEI file missing")
        continue
    clean, mp, cols = tei_text(idno)
    hits = list(rx.finditer(clean))
    print(f"## {k}  PL {entry.get('pl')}  idno {idno}  — {len(hits)} hit(s)")
    for m in hits:
        orig = mp[m.start()]
        col = [c for o, c in cols if o <= orig]
        col = (col[-1] if col else "?").lstrip("0")
        a, b = max(0, m.start() - ctx), min(len(clean), m.end() + ctx)
        print(f"  [PL {entry.get('pl')}:{col}] …{clean[a:b]}…")
        print()
    total += len(hits)
print(f"# {total} hit(s) across {len(keys)} work(s)")
