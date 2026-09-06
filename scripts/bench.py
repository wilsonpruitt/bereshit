#!/usr/bin/env python3
"""Shared helpers for per-crux spec files under cruxes/*.py. Extracted unchanged from the K7 pilot
(build-k7.py) so behavior is identical: TEI slicer, Sefaria loader, and the draft-English marker.

Latin is sliced from the local Corpus Corporum TEI (~/patrologia/sources/pl/tei) between two anchor
phrases, so no Latin is retyped. PL column = last <pb n=> before the start anchor.
"""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEI = pathlib.Path.home() / "patrologia" / "sources" / "pl" / "tei"
RAW = ROOT / "raw" / "sefaria"

DRAFT = {"translator": "claude-draft", "license": "cc-by", "status": "draft-awaiting-approval"}
# Phase 3, 2026-09-05: Wilson approved the whole body of fresh English as it stood. Passages he
# has not revised himself carry translator "claude-draft-approved" and no status, per the frozen
# convention. DRAFT stays for anything drafted after this point (Phase 6's second-tier sources).
APPROVED = {"translator": "claude-draft-approved", "license": "cc-by"}

_tei_cache = {}
def tei_text(idno):
    """Return (clean_text, list of (offset, column)) with tags stripped, whitespace collapsed."""
    if idno in _tei_cache: return _tei_cache[idno]
    raw = (TEI / f"{idno}.xml").read_text()
    out, cols, pos = [], [], 0
    for m in re.finditer(r"<pb n=\"([^\"]+)\"/?>|<[^>]+>|[^<]+", raw):
        s = m.group(0)
        if s.startswith("<pb"):
            cols.append((pos, m.group(1)))
        elif s.startswith("<"):
            out.append(" "); pos += 1
        else:
            out.append(s); pos += len(s)
    text = "".join(out)
    # collapse whitespace, keeping a map from new offsets to old ones
    clean, mp, i, last_space = [], [], 0, False
    for j, ch in enumerate(text):
        if ch.isspace():
            if not last_space: clean.append(" "); mp.append(j); last_space = True
        else:
            clean.append(ch); mp.append(j); last_space = False
    clean = "".join(clean)
    _tei_cache[idno] = (clean, mp, cols)
    return _tei_cache[idno]

def latin(idno, start, end, pl_vol, occurrence=0):
    clean, mp, cols = tei_text(idno)
    i = -1
    for _ in range(occurrence + 1):
        i = clean.find(start, i + 1)
        if i < 0: sys.exit(f"START anchor not found in {idno}: {start!r}")
    j = clean.find(end, i)
    if j < 0: sys.exit(f"END anchor not found in {idno}: {end!r}")
    j += len(end)
    orig = mp[i]
    col = [c for o, c in cols if o <= orig]
    col = col[-1] if col else "?"
    col = col.lstrip("0")
    return {"lang": "la", "text": clean[i:j].strip(), "source": f"PL {pl_vol}, col. {col}",
            "cc_idno": idno, "license": "pd"}

def sef(slug, lang, idx=None, he_file=None):
    d = json.load(open(RAW / (he_file or f"{slug}.json")))
    v = [v for v in d["versions"] if v["language"] == lang][0]
    t = v["text"]
    def flat(x): return x if isinstance(x, str) else " ".join(flat(i) for i in x)
    if idx is not None: t = t[idx]
    return flat(t), v["versionTitle"], v.get("license")

_NIQQUD = re.compile(r"[\u0591-\u05C7]")
def hcut(t, a, b=None, label="hcut"):
    """Slice vocalized Hebrew between two anchors, matching on the consonantal skeleton: Sefaria's
    pointed text and any anchor retyped through a terminal differ in combining-mark order, so a
    plain str.find fails on a phrase that is plainly there. Lifted out of cruxes/beginning-of-what.py
    at K6, the third crux to need it (PHASES.md, Phase 2).

    b=None slices from the start anchor to the end of t. Use this rather than
    `t[t.find(anchor):]` — a failed find returns -1 and silently yields the LAST CHARACTER of the
    text instead of raising. That is how br-3-8 shipped with an original of "." from K10 until
    Phase 6 found it."""
    bare = _NIQQUD.sub("", t)
    back = [k for k, ch in enumerate(t) if not _NIQQUD.match(ch)]
    a = _NIQQUD.sub("", a)
    i = bare.find(a)
    if i < 0: raise SystemExit(f"{label}: start anchor not found: {a!r}")
    if b is None: return t[back[i]:].strip()
    b = _NIQQUD.sub("", b)
    j = bare.find(b, i)
    if j < 0: raise SystemExit(f"{label}: end anchor not found: {b!r}")
    return t[back[i]:back[j + len(b) - 1] + 1].strip()

def ecut(t, a, b=None, label="ecut"):
    """The same guarded slice for a non-Hebrew (English/Latin) string: raises instead of returning
    the tail character when an anchor is absent."""
    i = t.find(a)
    if i < 0: raise SystemExit(f"{label}: start anchor not found: {a!r}")
    if b is None: return t[i:].strip()
    j = t.find(b, i)
    if j < 0: raise SystemExit(f"{label}: end anchor not found: {b!r}")
    return t[i:j + len(b)].strip()

def thread(crux_id, tid, frm, to, ty, ev):
    return {"id": tid, "from": frm, "to": to, "type": ty, "evidence": ev, "crux": crux_id}
