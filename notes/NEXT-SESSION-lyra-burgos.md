# The Lyra leaves — closed 2026-09-06, reopenable

Three sittings on 2026-09-06 built **ten witnesses** from the Koberger folio (Nuremberg 1486-87,
archive.org `biblia-sacra-lyra_202308`). **This thread can be left closed without loss.** Read
Phase 6 part six in `notes/SOURCES-FINDINGS.md` (all three sittings) before reopening it.

## Built

| witness | crux |
|---|---|
| `lyra-gen-1-1` | K1, K4, K5 |
| `lyra-gen-1-2-tohu` | K6 |
| `lyra-gen-1-2-spiritus` | K7 |
| `lyra-gen-1-3` | K8 |
| `lyra-gen-1-4-divisio` | K9 |
| `lyra-gen-1-4-bonum` | K9 |
| `lyra-gen-1-5` | K10 |
| `burgos-add-1` | K4 |
| `burgos-add-3` | K9 |
| `doering-repl-3` | K9 |

Metadata `scripts/lyra.py` (`LYRA`, `BURGOS`, `DOERING`); licence key `lyra-koberger-1487`.
⚠ **A K9 finding amendment is written and NOT executed.** ⚠ The **substitution** (Koberger 1486-87
for PLAN.md's 1492 Venice) is still unconfirmed by Wilson.

## Rulings taken

⛔ **Additio ix is OUT OF SCOPE and is not to be built.** It answers a Postilla passage on **Gen
1:21** (the *cete grandia*, and Lyra's *ex quo patet iudeos cecidisse in errorem saracenorum*),
verified on leaf n47. Neither clause of the anchor rule reaches it: the question it argues is
whether the beatitude of the future life is bodily, which is not a question any of the ten cruxes
raises. Do not revisit this without a new argument.

## If reopened — what is left, and it is thin

**Lyra's lemma i** (n43), *Dixitque Deus. Hic incipit opus distinctionis* — structural, K8, low
value. **Burgos's Additio ij** (n48-51), unread. **Doering's replies** to the other Additiones,
unread. Estimate ~20K for all three.

## The locator and the geometry — do not rediscover these

`scripts/archive-find.py` returns leaf + pixel box from archive.org's search-inside endpoint.
⛔ Never `Lyra_djvu.txt` (no page separators) or `Lyra_hocr_pageindex.json.gz` (leaf offset
**drifts**: 3 near Genesis 1, 6 by folio 30).

| leaf | content | columns |
|---|---|---|
| n42 | Lyra's introduction to Genesis | — |
| n43 | **Gen 1:1-3**, Postilla lemmas a-i | right col x **0.655-1.00** |
| n44 | **Gen 1:4-10**, Postilla lemmas k-v | x **0.065-0.44**, **0.455-0.84** |
| n45-46 | Gen 1:11-21, and the second run on Strabus | — |
| n47 | Gen 1:21-27 (the Saracens passage) | x **0.45-0.84** (col 2) |
| n48-51 | Burgos's *Additiones* on ch. 1 begin | col 2 x **0.45-0.845** |
| n57 | Additio iij | col 1 x **0.335-0.680** |
| n60 | Additio ix (out of scope) | — |
| n61 | Doering's *Correctorium* begins | col 2 x **0.660-1.00** |

⛔ A crop across a gutter reads as continuous Latin and is spliced. ⛔ So does a join across an
untranscribed gap between two crops. ⛔ Fresh English is `DRAFT`. ⛔ Don't fetch `Lyra.pdf` (3.5 GB).
