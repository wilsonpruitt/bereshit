# Next session — Nicholas of Lyra and Paul of Burgos on Genesis 1

**Model: Opus. Vision work; do not rush it.** Estimated ~150–200K, a crux-sized session of its own.
Run **after** the Gen 1:26 session. Follow `feedback_vision-ocr-discipline`.

---

## The source is identified, calibrated and quality-checked

**archive.org item `biblia-sacra-lyra_202308`** — *Biblia Sacra cum postillis Nicolai de Lyra*,
**Anton Koberger, Nuremberg 1486–87**, part 1 of four: **Genesis through 2 Chronicles**. 912 leaves.
Files: `Lyra.pdf` (3.5 GB — do not fetch), `Lyra_text.pdf` (367 MB), `Lyra_djvu.txt` (5.6 MB),
`Lyra_scandata.xml` (293 KB).

⚠ **This is a substitution.** PLAN.md names the **1492 Venice** *Biblia cum glossa*; that edition did
not surface on archive.org and this one did. Same textual tradition — Postilla + Burgos's
*Additiones* + Doering's *Replicae* — but **the colophon must cite the edition actually used**, and
someone should confirm the substitution is acceptable before the witnesses ship.

**Licence: public domain** (1486–87 print; the scans are the Internet Archive's, no ProQuest notice
on this item, unlike the Chalcidius item).

**Calibration, verified by reading the images, not estimated:**

- `page/n57.jpg` — **Paul of Burgos's *Additiones* on Genesis 1**, running *Additio ij* through
  *Additio vij* down the page. Running head "Genesis".
- `page/n61.jpg` — still Genesis, in the region of Gen 1:11–19 (herbs, the fourth day, the sun).
- The Postilla proper on Gen 1:1 is therefore **earlier than n57**; walk back from there.
- ⛔ **`Lyra_scandata.xml` carries no printed page numbers at all** (0 of 912 leaves), so leaf↔folio
  calibration must be done by reading images. Do not try to scale from `_djvu.txt` offsets: that
  method put Gen 1:1 at leaf 61, which is ~Gen 1:11–19.

**Scan quality: good.** 5980×7901, clean impression, rubricated, legible gothic with the usual
incunable abbreviations. Vision transcription is feasible. The item's own OCR is *partly*
abbreviation-aware (it renders ꝓ, qð, ᷣ) but is not trustworthy for text — use it only to locate.

---

## ⭐ Why this session is worth 200K — read this before pruning

Leaf n57 shows Burgos's third complaint against Lyra, and it is the best text in the whole project
for the question this edition exists to ask:

> *tercio quia expositiones lralis auctoritatem quam nostri doctores primo invenerunt **Ra. sa.
> hebreo** attribuit* — "third, because he attributes to **Rabbi Solomon the Hebrew** the authority
> of literal expositions which our own doctors found first"

and again, *Ra. Sa. invenit prius in glo. nostra*. **Paul of Burgos — a convert from Judaism, writing
in a printed Latin Bible — is arguing about how much the Latin bench owes Rashi, by name.** Every
other witness in this edition is two traditions that do not know they are in contact. This is the one
place where a Latin reads the rabbinic bench, credits it, and is attacked by another Latin for
crediting it too much. Whatever else gets pruned, **the Additiones that name Ra. Sa. are the roster.**

The apparatus is also structurally ideal: the *Additiones* are **printed as numbered discrete units**
(*Additio ij*, *iij*, *iiij*…), so one Additio maps cleanly onto one witness under the frozen
"one continuous argument" rule. No slicing judgement required.

---

## What to build

1. **Lyra's Postilla on Gen 1:1–5** — the literal exposition, especially wherever he cites Rashi.
2. **Burgos's *Additiones* on Gen 1** that touch the five verses, prioritising those that name
   *Ra. Sa.* or dispute Lyra's use of Hebrew authority.
3. **Doering's *Replicae*** only if they answer an Additio actually built — otherwise leave them.

Persons/places to add: `nicholas-of-lyra` (c. 1270–1349, Paris), `paul-of-burgos`
(c. 1351–1435, Burgos), possibly `matthias-doering`. New licence key for the Koberger edition.

## Traps

- ⛔ **Never read the gothic by eye from the OCR.** Transcribe from the page image, and expand
  abbreviations silently but consistently; record the expansion convention in PHASES.md the first
  time, as the frozen renderings were recorded.
- ⛔ **`overlap.py` does not cover this text** — it maps the PL TEI bench only. Lyra and Burgos are
  outside it, so nothing will warn you about a collision. There is no collision risk with the PL
  bench, but check `grep -l` against `data/witnesses/*.json` before reusing an id.
- ⛔ Fresh English is **`DRAFT`**, not `APPROVED`.
- ⛔ Don't fetch `Lyra.pdf`. 3.5 GB on an 8 GB machine.
