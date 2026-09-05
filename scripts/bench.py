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

def thread(crux_id, tid, frm, to, ty, ev):
    return {"id": tid, "from": frm, "to": to, "type": ty, "evidence": ev, "crux": crux_id}
