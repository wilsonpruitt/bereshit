#!/usr/bin/env python3
"""Build one crux's slice of the graph from its per-crux spec file cruxes/<id>.py.

Spec-file contract (see cruxes/ruach-hovering.py for the reference example):
  - imports helpers from `bench` (ROOT, RAW, latin, sef, DRAFT, thread)
  - WITNESSES: list of witness dicts, built by calling a local add(**kw)
  - THREADS: list of thread dicts, built with bench.thread(crux_id, ...)
  - FINDING: optional str, written into this crux's entry in data/cruxes.json
  - PERSONS, PLACES: optional dicts of new entries, merged into data/persons.json / data/places.json

Writes data/witnesses/*.json (this crux's witnesses only), merges this crux's threads into
data/threads.json (replacing any threads previously tagged with this crux id), updates this
crux's entry in data/cruxes.json (witnesses roster + status="built" + finding), and merges any
new persons/places. Does not touch data/scripture, data/licenses.json, or other cruxes' entries.

Usage: build-crux.py <crux-id>
"""
import json, pathlib, sys, importlib.util

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
W = ROOT / "data" / "witnesses"; W.mkdir(parents=True, exist_ok=True)

if len(sys.argv) < 2:
    sys.exit("usage: build-crux.py <crux-id>")
crux_id = sys.argv[1]
spec_path = ROOT / "cruxes" / f"{crux_id}.py"
if not spec_path.exists():
    sys.exit(f"no spec file: {spec_path}")

modspec = importlib.util.spec_from_file_location(f"cruxspec_{crux_id.replace('-', '_')}", spec_path)
mod = importlib.util.module_from_spec(modspec)
modspec.loader.exec_module(mod)

witnesses = getattr(mod, "WITNESSES", [])
threads_new = getattr(mod, "THREADS", [])
finding = getattr(mod, "FINDING", None)
persons_new = getattr(mod, "PERSONS", {})
places_new = getattr(mod, "PLACES", {})

if not witnesses:
    sys.exit(f"spec file {spec_path} defined no WITNESSES")

# ---------------------------------------------------------------- write witnesses
for w in witnesses:
    if crux_id not in w.get("cruxes", []):
        sys.exit(f"witness {w['id']!r} does not list crux {crux_id!r} in its own cruxes facet")
    fp = W / f"{w['id']}.json"
    if "answers" not in w and fp.exists():
        try: w["answers"] = json.load(open(fp)).get("answers", [])
        except Exception: w["answers"] = []
    fp.write_text(json.dumps(w, ensure_ascii=False, indent=1))
print(f"witnesses: {len(witnesses)}")

# ---------------------------------------------------------------- threads: replace this crux's own
threads_path = ROOT / "data" / "threads.json"
all_threads = json.load(open(threads_path)) if threads_path.exists() else []
all_threads = [t for t in all_threads if t["crux"] != crux_id]
for t in threads_new:
    t["crux"] = crux_id
all_threads.extend(threads_new)
threads_path.write_text(json.dumps(all_threads, ensure_ascii=False, indent=1))
print(f"threads: {len(threads_new)} for this crux (total {len(all_threads)})")

# ---------------------------------------------------------------- cruxes: update this crux's entry
cruxes_path = ROOT / "data" / "cruxes.json"
cruxes = json.load(open(cruxes_path))
idx = next((i for i, c in enumerate(cruxes) if c["id"] == crux_id), None)
if idx is None:
    sys.exit(f"crux {crux_id!r} not found in data/cruxes.json — add its entry there first")

own_ids = [w["id"] for w in witnesses if crux_id in w.get("cruxes", [])]
extra_ids = sorted(
    fp.stem for fp in W.glob("*.json")
    if fp.stem not in own_ids and crux_id in json.load(open(fp)).get("cruxes", [])
)
cruxes[idx]["witnesses"] = own_ids + extra_ids
cruxes[idx]["status"] = "built"
if finding:
    cruxes[idx]["finding"] = finding
cruxes_path.write_text(json.dumps(cruxes, ensure_ascii=False, indent=1))
print(f"crux {crux_id!r}: {len(own_ids) + len(extra_ids)} witnesses, status=built")

# ---------------------------------------------------------------- persons / places: merge new entries
for path, new in ((ROOT / "data" / "persons.json", persons_new), (ROOT / "data" / "places.json", places_new)):
    if not new: continue
    d = json.load(open(path)) if path.exists() else {}
    d.update(new)
    path.write_text(json.dumps(d, ensure_ascii=False, indent=1))
