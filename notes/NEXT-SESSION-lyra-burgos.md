# Next session — the rest of Lyra, Burgos and Doering on Genesis 1

**Model: Opus. Estimated ~60–80K**, down from the original 150–200K: the source is now transcribed
from, the leaves are calibrated, and the locator is written. **Read Phase 6 part six in
`notes/SOURCES-FINDINGS.md` first** — it records what was built, and the four navigation traps that
ate most of the first session. Do not re-survey.

## Already built (2026-09-06)

`lyra-gen-1-1` (K1, K4, K5) · `lyra-gen-1-2-tohu` (K6) · `burgos-add-3` (K9, the Ra. Sa. passage).
Persons `nicholas-of-lyra`, `paul-of-burgos`, `matthias-doering`; place `burgos`; licence key
`lyra-koberger-1487`; shared metadata in `scripts/lyra.py`.

## The locator — use this, not the OCR files

⭐ **archive.org's search-inside endpoint returns the leaf index in the same numbering that
`page/nN.jpg` uses, plus a pixel box.** Wrapped as `find.py` in the session scratchpad; rebuild it
from this recipe:

    https://ia600507.us.archive.org/fulltext/inside.php
      ?item_id=biblia-sacra-lyra_202308&doc=Lyra&path=/3/items/biblia-sacra-lyra_202308&q=<phrase>

`server`, `dir` and the file stem come from `https://archive.org/metadata/<id>`. Each hit carries
`page` (= leaf n), `l/t/r/b` and `page_width/page_height`; divide to get fractions, because the
image is a different size again.

- ⛔ **Do NOT use `Lyra_hocr_pageindex.json.gz`.** Its leaves are offset from the image leaves and
  **the offset drifts** — 3 near Genesis 1, 6 by folio 30. One calibration validates and then lies.
- ⛔ **Do NOT use `Lyra_djvu.txt`.** No page separators at all.
- ⛔ The same Additio is printed **twice** (Burgos's block, then again inside Doering's reply), so a
  duplicate hit is not a calibration error.

## Calibrated leaves

| leaf | content |
|---|---|
| n42 | Lyra's introduction to Genesis: *Circa primum tria facit scriptura…* |
| **n43** | **Gen 1:1–3**, rubric *Incipit liber Genesis qui dicitur hebraice Bresith*, Postilla lemmas a–i in the right column |
| **n44** | **Gen 1:4–10**, Postilla |
| n45–n46 | Gen 1:11–21, and Lyra's second run through the chapter on Strabus's exposition |
| n48–n51 | Burgos's *Additiones* on ch. 1 begin (*Additio i: circa expositionem litteralem huius primi capituli, que valde difficilis est*) |
| n57 | **Additio iij**, the Ra. Sa. passage — built |
| n60 | **Additio ix**, Arriani/Nestoriani and the Jews |
| n61 | Doering's *Correctorium corruptorii Burgensis* begins |

⛔ **Column geometry before anything else.** Take a whole-page overview and fix the column edges
before cropping: a crop that straddles the gutter reads as continuous Latin and is spliced from two
columns. On n43 the right column is x 0.655–1.00; on n57 column 1 is x 0.335–0.680. An edge that
cuts words makes the crop unreadable — shorten the slice, never reconstruct the missing half.

## The roster, in priority order

1. **Lyra lemma h** (n43), *Et spiritus … aquas*, the will of the artificer over the matter → **K7**.
   It lands beside Rabanus's and Remigius's craftsman and Abelard's *volitabat*.
2. **Lyra on Gen 1:4–5** (n44) → **K9, K10**. *Vidit lucem quod esset bona*, *divisit*, *dies unus*.
3. **Doering's reply to Additio iij** (n61) → **K9**. This completes the quarrel: Lyra calls the
   fathers' answer trifling, Burgos calls that irreverence and says the credit is misattributed to
   Rashi, Doering answers Burgos. Three Latins, one rabbinic authority, on one page.
4. **Burgos's Additio i / ij** (n48–n51) → **K1, K4**.
5. **Lyra lemma i** (n43) → **K8**.
6. ⚠ **Additio ix** (n60) — the best text on the leaf and the anchor is not yet established. Burgos
   answers a passage of the Postilla on chapter 1 in which Lyra says the Jews fell into the error of
   the Saracens. **Find and read that Postilla passage first**: if it is on 1:1–5 it is a witness, and
   if it is not, it is out of scope and should be recorded here rather than forced. Do not anchor it
   on a guess.

## Standing rules

- ⛔ Fresh English is **`DRAFT`**. ⛔ Don't fetch `Lyra.pdf` (3.5 GB on an 8 GB machine).
- ⛔ `overlap.py` does not cover this text; `grep -l` against `data/witnesses/*.json` before reusing an id.
- ⛔ Run `check.py` after `build-crux.py`, and `daf-coverage.py` after `npm run build`.
- ⚠ The **substitution** (Koberger 1486–87 for PLAN.md's 1492 Venice) is unconfirmed by Wilson.
