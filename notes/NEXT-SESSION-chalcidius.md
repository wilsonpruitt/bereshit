# Next session — Chalcidius on Genesis 1:1–2

**Model: Opus. Estimated ~60–90K** — one or two leaves of clean roman type, calibrated below, and
the judgement is which cruxes he goes on rather than where he is. **Run this before Lyra:** it is
smaller, it is calibrated, and it touches four cruxes instead of one.

---

## ⛔ The blocker in PHASES.md is gone. He does not need Waszink.

`notes/SOURCES-FINDINGS.md` says Chalcidius "wants Waszink's *Plato Latinus*" because the only free
text was uncorrected OCR of a 1617 print whose page images carry a ProQuest notice. **There is a
clean public-domain alternative and the passage has been read on it.**

**archive.org `bub_gb_LxGcsxR3tWgC`** — *Chalcidii viri clarissimi luculenta Timaei Platonis
traductio, et eiusdem argutissima explanatio*, **Josse Bade (Badius Ascensius), Paris 1520**,
148 leaves, Bavarian State Library via Google. **No rights notice of any kind.** A duplicate copy is
at `bub_gb_t-tyWOP6VRYC` (150 leaves) if a leaf is damaged in the first.

⚠ It is a 1520 print, not a critical edition, so **the colophon must cite the edition actually
used**, exactly as with Lyra. Where a reading matters, note the variant: this print has Prov 8:22 as
*Creavit me Deus progressionis suae **semitam***, where the text quoted in K1's finding (from
Baehrens's apparatus to Origen) has ***primitiam***. That difference should be recorded, not
silently harmonised.

## Calibration — verified by reading the image, not estimated

**`page/n116.jpg` = printed folio LVIII recto.** Running head *In Timeū Platonis. Fo. LVIII.*,
signature *h ii*, 1686×2500, clean impression. Fetch it as
`https://archive.org/download/bub_gb_LxGcsxR3tWgC/page/n116.jpg`.

**`page/n115.jpg` should be fo. LVII verso** and carries the Origen sentence — this is inferred from
the order of the item OCR (…*Origenes asseverat ita sibi ab Hebreis esse persuasum*… then the folio
LVIII running head, then *Salomo in prouerbiis*), **not yet confirmed against the image. Confirm it
first.** Leaf ≈ 2 × folio holds across the volume, so the arithmetic is self-consistent.

**Type is roman, not gothic.** This is much easier than Lyra: ordinary humanist abbreviations
(*-q̃*, *-ꝫ*, tildes for nasals, *q̄*), no rubrication, wide clean lines. The item OCR is poor and is
for **locating only** — it prints "Hebreis" for *Hebraeis* and mangles the marginalia.

⚠ The outer margin carries **printed keywords** — *Coelū & terra dicto loco*, *Terra*, *Arida*,
*Philo*, *Inanis cur sit terra*, *Symmachus*, *†desperandum* — which are the 1520 editor's finding
aids, **not Chalcidius**. Do not transcribe them into the witness text; they may be worth a note.

## ⭐ He is not a K1 witness. He is a K1 + K5 + K6 + K4 witness, on one page.

This is why the session is worth running ahead of Lyra. Folio LVIII recto alone carries, in order:

| what he says | crux |
|---|---|
| *Salomo in prouerbiis: Creauit me Deus progressionis suae semitam* … *praeeunte diuina sapientia coelum terramque factam: eandemque sapientiam diuinam esse vniuersitatis primordium* | **K1** — the rabbinic bench's verse, reaching "in wisdom" from Prov 8:22 and not from Ps 104:24 |
| *sapientiam factam quidem a Deo: sed non aliquo in tempore. Neque enim fuerit tempus vllum quo Deus fuerit sine sapientia* | **K1** — and the non-temporal beginning |
| *qui altius indagantur negant hoc coelum ab initio factum, sed secundo die* … *aliud verum coelum, et aliud quiddam esse soliditatem scriptura testatur* | **K5 `heaven-earth-order`** — whether *caelum et terra* names what we see |
| *Philo carentes corpore, atque intelligibiles essentias esse censet, ideas et exemplaria tam siccae istius terrae quam soliditatis* | **K5** — and Philo by name, on a Latin bench that otherwise never cites him |
| *Terra autem erat inuisibilis et informis, hoc est sylua corporea vetus mundi substantia, prius quam efficta Dei opificis sollertia sumeret formas, etiam tunc decolor et omni carens qualitate* | **K6 `tohu-vabohu`** and **K4 `ex-nihilo-or-matter`** — *sylua* is hyle, in Latin, in the fourth century |
| *Inanis porro et nihil propterea dicta: quia cum sit omnium qualitatum receptrix, propriam nullam habet ex natura* | **K6** — and it is the receptacle argument |
| *Otiosa vero et indigesta nuncupatur a Symmacho* | **K6** — a Greek-version variant of *tohu va-vohu* no other witness on the daf carries |
| *Stupide vero ex admiratione significatio animae vim quandam similitudinemque declarat* | the Gen 1:2 variant already noted in SOURCES-FINDINGS |

**The Origen sentence on n115 is the one K1's finding already quotes** and is the reason he was
escalated in the first place: *Origenes asseverat ita sibi ab Hebreis esse persuasum*, plus
*initium minime temporarium dici*.

## What to build

Slice by argument, not by page: probably **four or five witnesses** across K1, K5, K6 and K4, each
one continuous, under the frozen "one witness = one continuous argument" rule. He is a
**fourth-century Latin on Gen 1:1–2 outside the PL** — `data/latin-bench.json` has no idno for him
and `scripts/latin()` cannot slice him, so his `original` is transcribed from the image and carries
`cc_idno: null`. That is new: **every Latin witness in the edition so far came out of the TEI.**

## Traps

- ⛔ **`overlap.py` cannot see him** — it maps the PL TEI bench only. No collision risk, but
  `grep -l` against `data/witnesses/*.json` before reusing an id.
- ⛔ **Never transcribe from the item OCR.** Read the image. Follow `feedback_vision-ocr-discipline`.
- ⛔ Fresh English is **`DRAFT`**, not `APPROVED`.
- ⛔ New person `chalcidius` (fl. c. 320–350), new place (**Cordoba? unresolved — say "unknown" rather
  than guess**), new licence key for the 1520 Badius print.
- ⚠ He will very likely bear on **K4's and K6's findings** the way he bore on K1's. Findings are
  Wilson's; write the evidence and escalate.
