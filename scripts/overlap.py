#!/usr/bin/env python3
"""Is a candidate Latin anchor already inside another crux's slice? Run this BEFORE writing any
slice on a verse another crux has already built (PHASES.md, Phase 2 checklist).

Checks by OFFSET, not by printed column: one Migne column routinely holds two witnesses from two
different cruxes, so a column comparison silently passes candidates that are inside an existing
slice. Written for K4, where three of twenty candidates came back covered and column-checking would
have missed all three.

Usage: overlap.py <idno>::<anchor phrase> [<idno>::<phrase> ...]
       overlap.py 7303::"Et ideo Deus rectissime creditur" 11082::"Unum esse principium"

Prints, for each candidate, either the witness(es) whose slice contains it, or FREE with the
columns at which the previous slice ends and the next slice begins in that work.
"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bench import ROOT, tei_text

def coverage():
    cov = {}
    for fp in sorted((ROOT / "data" / "witnesses").glob("*.json")):
        w = json.load(open(fp))
        o = w.get("original", {})
        if o.get("lang") != "la" or not o.get("cc_idno"):
            continue
        clean, mp, cols = tei_text(o["cc_idno"])
        # A witness whose `text` was ASSEMBLED — several glosses concatenated, an editorial
        # bracket spliced in — has no 60-character prefix that occurs verbatim in the TEI, and
        # the first version of this loop dropped it from the coverage map with a stderr note
        # nobody reads. It then reported FREE for a candidate sitting inside it. Try shorter
        # prefixes, and when none matches say so on STDOUT where the answer is being read.
        for n in (60, 40, 24):
            i = clean.find(o["text"][:n])
            if i >= 0: break
        if i < 0:
            print(f"!! UNCHECKED: {w['id']} ({o.get('source','')}) could not be located inside "
                  f"{o['cc_idno']} — a FREE verdict in that work is not trustworthy")
            continue
        # An assembled witness matched on a short prefix may not run to i+len(text); use the
        # longest run that is actually there, so coverage is never claimed beyond the evidence.
        end = i + (len(o["text"]) if n == 60 else n)
        cov.setdefault(o["cc_idno"], []).append((i, end, w["id"], o.get("source", "")))
    return cov

def col_at(idno, off):
    clean, mp, cols = tei_text(idno)
    c = [c for o, c in cols if o <= mp[off]]
    return (c[-1] if c else "?").lstrip("0")

def check(cov, idno, phrase, occ=0):
    clean, mp, cols = tei_text(idno)
    i = -1
    for _ in range(occ + 1):
        i = clean.find(phrase, i + 1)
        if i < 0:
            return print(f"  NOT FOUND in {idno}: {phrase!r}")
    hits = [r for r in cov.get(idno, []) if r[0] <= i < r[1]]
    if hits:
        print(f"  [{idno} col {col_at(idno, i)}] COVERED by " +
              ", ".join(f"{w} ({s})" for _, _, w, s in hits))
        return
    print(f"  [{idno} col {col_at(idno, i)}] FREE")
    near = sorted(cov.get(idno, []), key=lambda r: r[0])
    prev = [r for r in near if r[1] <= i]
    nxt = [r for r in near if r[0] > i]
    if prev: print(f"      prev slice ends col {col_at(idno, prev[-1][1] - 1)}: {prev[-1][2]}")
    if nxt:  print(f"      next slice starts col {col_at(idno, nxt[0][0])}: {nxt[0][2]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cov = coverage()
    for arg in sys.argv[1:]:
        idno, _, phrase = arg.partition("::")
        print(f"\n{phrase[:70]!r}")
        check(cov, idno, phrase)
