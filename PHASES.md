# PHASES.md — Bereshit / In Principio, from K7 to launch

Written 2026-09-05 at the end of the Fable pilot session. This is the score; cheaper sessions play it.
Rule of thumb from the model-prudence rubric: **no crux build, translation draft, or site page is Fable work.**
Fable returns only for the items in Phase 7, or when Opus has failed twice on one specific problem.

State when written: `~/bereshit` scaffolded (no git yet). K7 `ruach-hovering` built end to end: 30 witnesses,
33 threads, three prototypes, **C (daf) chosen**. Glossa on Genesis finished and wired in. Nine cruxes remain.

---

## Frozen conventions (do not re-decide in later sessions)

### Data
- Schema is `PLAN.md` §4 exactly, plus two facets added in the pilot: `answers` (ids from `data/answers.json`, one file per crux family set) and `senses` (`literal | allegorical | spiritual | translation`). Every witness carries both.
- One witness = one continuous argument on the verse from one work. A work may yield several witnesses (Augustine has five on 1:2). Never merge distinct arguments to save a card.
- Latin is **sliced from the local TEI by anchor phrase** (`~/patrologia/sources/pl/tei/<idno>.xml`; ids in `data/latin-bench.json`). Never retype Latin. PL column is computed from the last `<pb>` before the start anchor. If an anchor fails, fix the anchor; do not paste text.
- Rabbinic text comes from `raw/sefaria/*.json` pulled by `scripts/pull-sefaria.py`, using only the versions pinned there (Wikisource Bavli CC BY-SA; Sefaria Midrash Rabbah 2022 CC BY; Silbermann Rashi PD; Etheridge PD; Guggenheimer Yerushalmi CC BY; Berman Tanchuma CC BY). Davidson/Steinsaltz is never embedded.
- Edges need `evidence` quoting the words that prove the dependency. A shared image without a citation is `parallel`. Direction later → earlier except `transmits`. When a witness names its source (`HIERON.`, `AUG.`), that is `cites`; verbatim reuse without a name is `echoes`.
- Compilations carry a range and a precision flag (`compilation-1110-1130`, `redaction-500-600`), never a fake year.
- Every English passage has a non-empty `translator`; fresh drafts are `claude-draft` with `status: draft-awaiting-approval` until Wilson approves, then `wilson-pruitt` (revised) or `claude-draft-approved`.

### English register for fresh drafts (Latin bench)
- Plain, literal, unhurried; keep the Latin sentence order where English allows. No archaism, no "thee."
- Fixed renderings: *ferebatur / superferebatur* = "was borne over / above"; *fovebat* = "was warming"; *incubabat* = "was brooding"; *vivificare* = "quicken"; *artifex / faber* = "craftsman"; *voluntas artificis* = "the will of a craftsman"; *informis materia* = "formless matter"; *inanis et vacua* = "empty and void"; *per spatia locorum* = "across spaces of place".
- Quote the Vulgate lemma in single quotes as the witness quotes it; keep *Spiritus Domini* vs *Spiritus Dei* as the witness has it (it is evidence).
- Scripture references in parentheses, modern numbering; add Vulgate numbering only where it differs (Ps 104:30 [Vg 103]).
- Mark elisions in the English with `[…]` and say in `notes` what was elided; the Latin excerpt is always continuous.
- Added for K10 (extends the list, does not re-decide it): *dies unus* = "one day" and never "the first day"; *dies primus* = "first day"; *vespera / vespere* = "evening", *mane* = "morning", *aurora* = "dawn"; *dies naturalis / artificialis* = "natural / artificial day"; *circuitus* = "circuit"; *cognitio matutina et vespertina* = "morning and evening knowledge"; *creavit omnia simul* = "he created all things at once"; *relativa* = "relatives"; *senarius dierum* = "a senary of days".

### English register for fresh drafts (rabbinic bench)
- "Our rabbis taught" for *tanu rabbanan*; "as it is said" for *she-ne'emar*; "as it is written" for *di-khtiv*; "the Holy One, blessed be He"; in targums the Tetragrammaton is "the LORD"; *min qodam* = "from before".
- Transliteration: merahefet, tohu va-vohu, Bereshit, ruach; ḥ for ח, no other diacritics.
- Tradents named as in the text (Rav Aḥa bar Yaakov, Mar Zutra); add `tradents` to the witness.
- Added for K10: *yom echad* = "one day", *yom rishon* = "first day", *yachid be-olamo* = "alone in his world"; "the work of creation" for *ma'aseh bereshit*; "it is taught" for *tanya*; "our rabbis taught" for *tanu rabbanan* (as above).

### Crux files
- Questions in three languages (`en`, `la`, `he`) as in `data/cruxes.json`; the Latin and Hebrew forms are the medieval question, not a translation of the English.
- `summary` = why it is a crux; `finding` = what the built data showed that the plan did not know. Write `finding` only after the threads exist.

---

## Phase 1 — Generalize the pipeline · **Sonnet** · ~1 session — **DONE 2026-09-05**

Built as specified, plus four things the spec did not name: `scripts/bench.py` (the shared TEI
slicer / Sefaria loader, imported by every crux spec), `scripts/grep-bench.py` (seeds a crux by
searching the bench TEI for lemma words and printing hits with computed PL columns — the
checklist's step 3, now one command), `scripts/indexpage.py`, and two extra fields in the
spec-file contract added while building K10: **ANSWERS** and **LICENSES** (merged like
PERSONS/PLACES, so a crux spec is self-contained) and **SHORT** (the crux's display name, which
removed the last K7 hardcoding from the renderers). `check.py` has six checks, not three: the
sixth (answer ids and licence keys must resolve) caught a real K7 licence-key bug on its first run.

File paths and the pattern are given, so this is Tier-1 work.

1. Turn `scripts/build-k7.py` into `scripts/build-crux.py <crux-id>` reading a per-crux spec file `cruxes/<id>.py` (witness dicts + threads, same shape as K7). Keep the TEI slicer, the Sefaria loader, the answers-merge, and the column computation unchanged.
2. `scripts/render-daf.py` and `render-map.py` already take a crux id; make them iterate all built cruxes and write an `out/index.html` listing them.
3. Add `scripts/check.py`: every thread endpoint exists; every witness in a crux has that crux in its `cruxes`; no `claude-draft` without `status`; no licence `check` in a witness marked `ships: true`; anchors resolve.
4. `git init`, first commit (**ask Wilson before pushing anywhere**).

Done when: `python3 scripts/build-crux.py ruach-hovering` reproduces today's K7 byte-for-byte and `check.py` is clean.

## Phase 2 — Build the nine remaining cruxes · **Opus**, one crux per session

**State: K10 built (2026-09-05). Next up is K1 `beginning-of-what`, row 2 of the table.**
To start that session, paste: *"Build the crux `beginning-of-what` in ~/bereshit, following the
per-crux checklist in PHASES.md."* Everything the checklist needs is on disk: the bench TEI, the
Sefaria pulls (`br-1`, `targ-neof`, `ibn-ezra-gen-1`, `ramban-gen-1`, `rashi-gen-1`, `b-meg-9a`),
`cruxes/one-day-evening-first.py` as the worked example to copy the shape from, and
`notes/cross-crux.md`, which already lists what K1's neighbours turned up.

Order chosen by how much rabbinic material each has and how much it teaches the next one:

| # | crux | why this order | expected witnesses |
|---|---|---|---|
| ~~1~~ | ~~K10 `one-day-evening-first`~~ | **BUILT 2026-09-05** — 28 witnesses, 34 threads | 20–25 |
| 2 | K1 `beginning-of-what` | BR 1:1 + Neofiti "with wisdom" vs Jerome's *in Filio*; Prov 8 thread across benches | 25–30 |
| 3 | K8 `first-light` | hidden light (BR 3:6, Chag 12a, PdRE 3) vs angelic light (Augustine); Bonaventure d.13 | 20–25 |
| 4 | K6 `tohu-vabohu` | Glossa 69D gloss already sliced; Rashi's *estordison*; BR 2:2–3; Vulgate as witness | 15–20 |
| 5 | K5 `heaven-earth-order` | Shammai/Hillel (BR 1:15, Chag 12a) vs Augustine's *caelum* = spiritual creation | 15–20 |
| 6 | K4 `ex-nihilo-or-matter` | BR 1:9 philosopher; Conf XII; Abelard already sliced; Ramban Phase 2 | 15–20 |
| 7 | K9 `good-and-separated` | moral allegory both sides; test Bede for Hebrew mediation | 12–15 |
| 8 | K3 `elohim-and-trinity` | Megillah 9a; Rupert's whole design; much already tagged from K7 | 12–15 |
| 9 | K2 `why-begin-here` | Rashi's R. Yitzchak; Ambrose I.1; prologues; smallest | 8–12 |

Per-crux checklist (paste into the Opus prompt):
1. Read `PLAN.md` §5 entry, this file's conventions, and `notes/SOURCES-FINDINGS.md`.
2. Rabbinic: read the pulled JSON for the loci listed; add pulls to `pull-sefaria.py` only for refs not yet on disk.
3. Latin: grep the bench TEI for the crux's lemma words (as `build-k7.py` was seeded by grepping *incubabat / fovebat / superferebatur*); list hits with columns; keep only continuous arguments on the verse.
4. Write `cruxes/<id>.py`; run `build-crux.py`; run `check.py`; render the daf; read the daf once.
5. Fill `finding` last. Log anything the plan got wrong in `notes/SOURCES-FINDINGS.md`.
6. Do **not** revise K7 or another crux's threads while building this one; note cross-crux edges in `notes/cross-crux.md` for the Phase 4 pass.

Escalate to Fable only if: a crux needs a new edge type, a new facet, or a witness that does not fit "one continuous argument".

**Burn, measured on K10 (Opus, 2026-09-05): ~170K tokens of context for the whole crux** —
survey, extraction, 28 English drafts, 34 threads, the daf read, and the notes. That is inside the
150–250K estimate and at its low end, and K10 was chosen as the *richest* of the nine, so the
remaining eight should not exceed it. Two things held the number down and are worth repeating:
`grep-bench.py` replaced hand-reading TEI files, and every rabbinic locus K10 needed was already on
disk except one (Chullin 83a). A crux needing several new Sefaria pulls or vision work will cost more.

What actually took the time was not extraction but **deciding the roster** — the bench yielded far
more than 25 usable witnesses and the pruning is a judgement call each time. Budget for that.

## Phase 3 — English review · **Wilson**, with **Opus** as second reader

- Wilson revises every `claude-draft` passage or approves it as is; set `translator` and clear `status`.
- An Opus pass afterward checks each approved passage against the frozen renderings above and flags drift (does not rewrite).
- The Glossa English keeps `translator: wilson-pruitt`; Wilson sets its licence in `data/licenses.json` (`wroot-glossa`).

## Phase 4 — Cross-crux pass · **Opus** · 1 session

Merge `notes/cross-crux.md`: edges between witnesses in different cruxes, witnesses that belong to more cruxes than tagged, duplicated witnesses across crux files (one witness file, many `cruxes`). Re-run `check.py` over all ten.

## Phase 5 — Astro site · **Sonnet** (Opus on second failure)

Spec is the prototype: `out/C-daf-ruach-hovering.html` is the crux view, pixel for pixel; `out/B-map-*.html` is the secondary map view; the stream (A) is retired. Build order per `PLAN.md` §7.8: crux (daf) view → dialogue view (`/dialogue/gen-1-<verse>`; use the daf grid with all cruxes' notes, crux chip on each note) → `/witnesses/<id>`, `/persons/<id>`, `/places/<id>` → colophon from `licenses.json` → Pagefind. Static JSON in, no client fetches beyond Pagefind. EB Garamond / Inter / Frank Ruhl Libre. Both themes.

## Phase 6 — Second-tier sources · **Opus** (vision work needs care)

Only after Phases 2–4: Origen/Rufinus Hom. in Gen. I (GCS Baehrens, archive.org, PD) for K1/K3; Lyra Gen 1 from the 1492 Venice *Biblia cum glossa* (transcription = vision OCR, follow `feedback_vision-ocr-discipline`); Paul of Burgos; Bonaventure II Sent. d.12–13 slices from `~/bonaventure-sentences/vol2/`; Etheridge Onkelos and Daat BR Hebrew by alternate fetch; Sefaria attribution string.

## Phase 7 — Deploy · **Haiku**

`git` push to a new Labs repo (Wilson's OK per push), Vercel project on the Labs team, Cloudflare DNS-only record for the subdomain Wilson names (open decision §9.1), production deploy on Wilson's per-action OK.

## Phase 8 — Fable, once

One session, after everything above: read all ten daf pages; write the editorial introduction and the ten `finding` paragraphs into a single voice; decide whether any Phase-2 view (time scrubber, lemma view, invertible centre, authority map) is worth building; rule on the "one translation, one home" question for the Glossa and Bonaventure text this site re-hosts.
