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

# Phase 6: the Bereshit Rabbah Hebrew moved from Torat Emet (vocalized, abbreviations expanded,
# licence asserted) to Wikisource (CC BY-SA, unvocalized, abbreviations printed). An anchor retyped
# from one will not match the other on the consonantal skeleton alone: א"ר stands for אמר רבי, and
# plene/defective spelling varies freely (מיחד/מייחד, ולחשך/ולחושך). _HFUZZ is the fallback used
# only when the exact skeleton match fails, and it must match UNIQUELY or hcut refuses it.
_ABBR = [('א"ר', "אמר רבי"), ("ר'", "רבי"), ('רשב"י', "רבי שמעון בן יוחאי"),
         ('הקב"ה', "הקדוש ברוך הוא"), ('ר"ש', "רבי שמעון"), ("שנא'", "שנאמר"),
         ('אר"י', "אמר רבי יהודה"), ('ב"ו', "בשר ודם"), ('ד"א', "דבר אחר")]
def _hfuzz_map(bare):
    """Fuzz a consonants-only Hebrew string and return (fuzzed, index) where index[k] is the offset
    in `bare` that produced fuzzed[k]. Abbreviations expand to several letters, so the map cannot be
    built character by character — that was the first attempt and it silently failed to expand any
    multi-letter abbreviation at all."""
    out, idx, i = [], [], 0
    while i < len(bare):
        for a, b in _ABBR:
            a_bare = re.sub(r"[^\u05d0-\u05ea\"']", "", a)
            if a_bare and bare.startswith(a_bare, i):
                for ch in b:
                    if "\u05d0" <= ch <= "\u05ea" and ch not in "\u05d5\u05d9":
                        out.append(ch); idx.append(i)
                i += len(a_bare); break
        else:
            ch = bare[i]
            if "\u05d0" <= ch <= "\u05ea" and ch not in "\u05d5\u05d9":
                out.append(ch); idx.append(i)
            i += 1
    return "".join(out), idx

def _hfuzz(s):
    """The same normalisation for a short anchor, where no offset map is needed."""
    bare = re.sub(r"[^\u05d0-\u05ea\"']", "", _NIQQUD.sub("", s))
    return _hfuzz_map(bare)[0]

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

    def locate(anchor, frm, which):
        i = bare.find(_NIQQUD.sub("", anchor), frm)
        if i >= 0: return i, len(_NIQQUD.sub("", anchor))
        # Fallback for a text in a different orthography (see _hfuzz_map above).
        fz, idx = _hfuzz_map(bare)
        fa = _hfuzz(anchor)
        if not fa: raise SystemExit(f"{label}: {which} anchor has no Hebrew letters: {anchor!r}")
        hits = [m.start() for m in re.finditer(re.escape(fa), fz)]
        hits = [h for h in hits if idx[h] >= frm]
        if not hits:
            raise SystemExit(f"{label}: {which} anchor not found, exactly or fuzzily: {anchor!r}")
        if len(hits) > 1:
            raise SystemExit(f"{label}: {which} anchor matches {len(hits)} places under orthographic "
                             f"normalisation and so is not safe to use — lengthen it: {anchor!r}")
        h = hits[0]
        end = idx[min(h + len(fa) - 1, len(idx) - 1)]
        return idx[h], end - idx[h] + 1

    i, alen = locate(a, 0, "start")
    if b is None: return t[back[i]:].strip()
    j, blen = locate(b, i + alen, "end")
    return t[back[i]:back[j + blen - 1] + 1].strip()

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
