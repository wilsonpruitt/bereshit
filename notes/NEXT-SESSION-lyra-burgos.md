# Next session — what is left on the Lyra leaves

**Model: Opus. Estimated ~35–45K.** Small. Two sittings on 2026-09-06 built seven witnesses; this
is the tail. **Read Phase 6 part six in `notes/SOURCES-FINDINGS.md` first** (both sittings) and do
not re-survey.

## Built

`lyra-gen-1-1` (K1, K4, K5) · `lyra-gen-1-2-tohu` (K6) · `lyra-gen-1-2-spiritus` (K7) ·
`lyra-gen-1-4-bonum` (K9) · `lyra-gen-1-5` (K10) · `burgos-add-3` (K9) · `doering-repl-3` (K9).
Metadata in `scripts/lyra.py` (`LYRA`, `BURGOS`, `DOERING`); licence key `lyra-koberger-1487`.
⚠ **A K9 finding amendment is written and NOT executed** — see SOURCES-FINDINGS.

## The locator and the geometry — use both, don't rediscover them

`scripts/archive-find.py` gives leaf + pixel box from archive.org's search-inside endpoint. ⛔ Never
`Lyra_djvu.txt` (no page separators) or `Lyra_hocr_pageindex.json.gz` (leaf offset **drifts**: 3
near Genesis 1, 6 by folio 30).

**Column edges, measured** — crop inside one column, full column width:

| leaf | columns |
|---|---|
| n43 | right column x **0.655–1.00** |
| n44 | x **0.065–0.44** and **0.455–0.84** |
| n57 | column 1 x **0.335–0.680** |
| n61 | column 2 x **0.660–1.00** |

⛔ A crop across a gutter reads as continuous Latin and is spliced. ⛔ So does a join across an
untranscribed gap between two crops — transcribe the gap, don't assume the ends meet.

## What is left, in priority order

1. **Burgos's Additio i and ij** (n48–n51) → **K1, K4**. Additio i opens *circa expositionem
   litteralem huius primi capituli, que valde difficilis est*. These are his substantive additions
   on Gen 1:1 itself, as against Additio iij which is a quarrel about credit.
2. ⚠ **Additio ix** (n60) — the best untouched text on the leaves and **the anchor is still not
   established**. *Sicut inter christianos fuerunt aliqui heretici, ut Arriani, Nestoriani, et
   huiusmodi, quorum errores non sunt imponendi veris christianis, sic inter iudeos fuerunt aliqui
   habentes erroneas opiniones que non approbantur a iudeis communiter* — Burgos refusing to let a
   Jewish error be charged to Jews generally, against Lyra's claim that the Jews fell into the error
   of the Saracens. **Find and read the Postilla passage it answers before building.** If that
   passage is on Gen 1:1–5 it is a witness for K2 or K3; if it is not, it is out of scope and should
   be recorded here rather than forced onto an anchor. Do not guess.
3. **Lyra's lemma i** (n43), *Dixitque Deus. Hic incipit opus distinctionis* → **K8**. Structural
   rather than argumentative; low value, build only if the other two come in cheap.
4. **Lyra's lemmas k–o** (n44 left column), *Fiat lux · Et vidit Deus lucem quod esset bona · Et
   divisit lucem a tenebris · Appellavitque lucem diem* → **K8, K9**. The division is *per motum
   solis*, by the sun's motion over one hemisphere and the earth's opacity — a flatly astronomical
   answer to K9's question that no other witness on the daf gives.

## Standing rules

⛔ Fresh English is `DRAFT`. ⛔ Don't fetch `Lyra.pdf` (3.5 GB). ⛔ `overlap.py` does not cover this
text; `grep -l` before reusing an id. ⛔ `check.py` after `build-crux.py`; `daf-coverage.py` after
`npm run build`. ⚠ The **substitution** (Koberger 1486–87 for PLAN.md's 1492 Venice) is still
unconfirmed by Wilson.
