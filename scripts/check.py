#!/usr/bin/env python3
"""Consistency checks across data/*.json. Run after every build-crux.py call. Exits nonzero (and
prints every violation) if anything fails; prints "check.py: clean" and exits 0 otherwise.

Checks:
  1. Every thread's from/to id names a witness that exists on disk.
  2. Every witness listed in a crux's "witnesses" roster (data/cruxes.json) actually carries that
     crux in its own "cruxes" facet, and vice versa (no witness claims a crux that omits it).
  3. No witness has translator "claude-draft" without "status": "draft-awaiting-approval".
  4. No witness marked "ships": true has license "check" (a licence still to confirm).
  5. Every witness's anchor.verse resolves to a verse in data/scripture/gen-1.json.
  6. Every answer id on a witness exists in data/answers.json, and every licence key used by a
     witness exists in data/licenses.json.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
W = ROOT / "data" / "witnesses"

errors = []

witnesses = {}
for fp in sorted(W.glob("*.json")):
    w = json.load(open(fp))
    if w["id"] != fp.stem:
        errors.append(f"{fp.name}: id {w['id']!r} does not match filename")
    witnesses[w["id"]] = w

threads = json.load(open(ROOT / "data" / "threads.json"))
cruxes = json.load(open(ROOT / "data" / "cruxes.json"))
scripture = json.load(open(ROOT / "data" / "scripture" / "gen-1.json"))
verse_refs = {v["ref"] for v in scripture["verses"]}

# 1. thread endpoints exist
for t in threads:
    for end in ("from", "to"):
        if t[end] not in witnesses:
            errors.append(f"thread {t['id']}: {end}={t[end]!r} is not a witness on disk")

# 2. crux <-> witness roster agreement. Roster -> facet must hold for every crux. The reverse
# (facet -> roster) only holds for "built" cruxes — a "register-only" crux's roster is populated
# only when it is built (Phase 4 reconciles cross-crux facets left dangling until then).
for c in cruxes:
    cid = c["id"]
    roster = set(c.get("witnesses", []))
    for wid in roster:
        if wid not in witnesses:
            errors.append(f"crux {cid!r}: roster lists {wid!r}, no such witness on disk")
        elif cid not in witnesses[wid].get("cruxes", []):
            errors.append(f"crux {cid!r}: roster lists {wid!r}, but that witness's own cruxes facet omits {cid!r}")
    if c.get("status") != "built": continue
    for wid, w in witnesses.items():
        if cid in w.get("cruxes", []) and wid not in roster:
            errors.append(f"witness {wid!r} claims built crux {cid!r}, but that crux's roster omits it")

# 3. draft English carries its status
for wid, w in witnesses.items():
    eng = w.get("english", {})
    if eng.get("translator") == "claude-draft" and eng.get("status") != "draft-awaiting-approval":
        errors.append(f"witness {wid!r}: translator=claude-draft but status is {eng.get('status')!r}, not draft-awaiting-approval")

# 4. no unresolved licence on a witness marked to ship
for wid, w in witnesses.items():
    if not w.get("ships"): continue
    for facet in ("original", "english"):
        if w.get(facet, {}).get("license") == "check":
            errors.append(f"witness {wid!r}: ships=true but {facet}.license is still 'check'")

# 5. anchors resolve
for wid, w in witnesses.items():
    ref = w.get("anchor", {}).get("verse")
    if ref not in verse_refs:
        errors.append(f"witness {wid!r}: anchor.verse {ref!r} does not resolve in data/scripture/gen-1.json")

# 6. answer ids and licence keys resolve
answers = json.load(open(ROOT / "data" / "answers.json"))
licenses = json.load(open(ROOT / "data" / "licenses.json"))
for wid, w in witnesses.items():
    for a in w.get("answers", []):
        if a not in answers:
            errors.append(f"witness {wid!r}: answer {a!r} is not in data/answers.json")
    for facet in ("original", "english"):
        lic = w.get(facet, {}).get("license")
        if lic and lic not in licenses:
            errors.append(f"witness {wid!r}: {facet}.license {lic!r} is not in data/licenses.json")

if errors:
    print(f"check.py: {len(errors)} problem(s)")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"check.py: clean ({len(witnesses)} witnesses, {len(threads)} threads, {len(cruxes)} cruxes)")
