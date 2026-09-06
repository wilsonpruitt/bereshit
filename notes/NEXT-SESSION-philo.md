# Next session — Philo of Alexandria, *De opificio mundi*, on Genesis 1:1–5

**Model: Opus. Estimated ~90–130K.** Cheaper than it looks and cheaper than Lyra: the Greek is
**machine-readable and section-numbered**, so this is roster judgement, slicing and drafting, with
no discovery and no vision work. **Run it before Lyra.** Philo is the head of streams that five
existing cruxes are the tail of, so building him first means Lyra's Rashi material lands on a daf
whose findings are already settled; the other order means revisiting K10 and K1 twice.

---

## Why he belongs here, and it is not scope creep

**The edition already has this bench.** `tradition: greek-jewish` exists with five witnesses — the
LXX on Gen 1:1–5. No schema change is needed; Philo sits beside the Septuagint.

But **that bench has no voice**. The LXX is a translation, not an argument. So the daf has been
letting "the Jewish reading" mean "the rabbinic reading", and nothing in the edition defends that
equation. Philo is the correction.

It is also already a live hole: **`chalcidius-caelum-et-terra` names Philo on the daf as an
authority and the edition does not print him.** That witness's note says he "does not appear
anywhere else in this edition" as though it were a curiosity. It is a defect.

⭐ **And the transmission story is this edition's own thesis in mirror.** K1's finding says contact
existed at the head and the Latin transmission lost it. Philo is the harder case: **a Jewish
reading of these five verses that the Christian bench preserved and the rabbinic bench lost
entirely.** He is not cited in rabbinic literature at all and is recovered for Judaism only in the
sixteenth century by Azariah dei Rossi; meanwhile Ambrose's *Hexaemeron* is substantially Philo and
rarely says so. That is a third instance of the same mechanism, after Chalcidius and Basil→Bede,
and the sharpest of the three — Cohn's own prolegomena open by saying it outright: *Philonis
Alexandrini memoria a Iudaeis non minus quam a paganis fere neglecta tota pendet ab ecclesia
Christiana.*

## The text: machine-readable, critical, and section-aligned

**`OpenGreekAndLatin/First1KGreek`, `data/tlg0018/tlg001/`** — two TEI files, already downloaded
once to scratch during this survey:

| file | what it is |
|---|---|
| `tlg0018.tlg001.1st1K-grc1.xml` (310 KB) | **Cohn's Greek**, i.e. the Cohn–Wendland critical text of 1896, in TEI, **172 numbered sections** |
| `tlg0018.tlg001.1st1K-eng1.xml` (154 KB) | **Yonge's English**, 1854, same 172 sections, aligned |

Raw URLs: `https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/master/data/tlg0018/tlg001/<file>`

**This is the Greek equivalent of the PL TEI**, and it is better in two ways: the text is critical
(Migne is not), and the unit is a printed section number rather than an anchor phrase, so slicing
is exact and `overlap.py`-style collision risk does not arise.

⚠ **Licence: the First1KGreek repo is CC BY-SA 4.0.** Cohn's 1896 text is itself public domain and
the edition's own stated principle is that a faithful transcription of a PD text creates no new
copyright — but the file being used is theirs, including their correction and encoding, and the
site already carries CC BY-SA components (Wikisource Bavli, Miqra according to the Masorah) under
per-component licensing. **Do the same: a new licence key crediting First1KGreek under CC BY-SA,
and leave the reasoning short** — this is not the Neofiti situation and does not need re-arguing.

**Citation scheme is ready-made.** The Greek TEI carries `<pb n="v.1.p.11"/>` throughout — Cohn–
Wendland volume and page. Cite as **`Cohn–Wendland i. 11`** with the section number, the way the
Latin bench cites PL columns.

## ⛔ The one trap, and it fails silently

**The critical apparatus is inside the section divs, tagged `<note type="footnote">`.** Strip tags
naively and you get Philo's Greek with manuscript sigla welded into the middle of it:

> ἐπεὶ δὲ φῶς μὲν ἐγένετο, σκότος δ’ ὑπεξέστη **1 πλανῆτι Eus τε om. M Eus ἀρύτονται Ems cod. I…**

**60 of the 172 sections are affected**, including §35, which is this session's headline. It looks
like text, it is in Greek script, and nothing downstream would catch it — `check.py` rule 7 only
catches slices that are too *short*.

**Fix, verified during the survey: drop `<note>` elements before flattening**, i.e.
`re.sub(r'(?s)<note.*?</note>', '', div)` first, then strip remaining tags. With that, zero of 172
sections retain apparatus. **Write this into the loader in `scripts/bench.py` (a `greek()` helper
beside `latin()`), not into the crux spec**, so the class cannot recur, and consider a `check.py`
rule 11 matching manuscript-sigla runs in any `original.text`.

## ⭐ The roster — five cruxes, and he is the head of two findings

Section numbers are Cohn's and are what the TEI is keyed to.

| § | what he says | crux |
|---|---|---|
| **17–20** | **The city in the mind of the architect.** A king founds a city; a trained architect first stamps the plan in his own mind and builds from it; so the intelligible world has no place but the divine Reason. | **K1** ⭐⭐⭐ |
| **26** | *ἐν ἀρχῇ* is taken *οὐχ ὡς οἴονταί τινες τὴν κατὰ χρόνον* — not, as some think, the beginning according to time; there was no time before the world, since time is the interval of the world's motion | **K1** ⭐ |
| **27** | *εἰ δ’ ἀρχὴ μὴ παραλαμβάνεται … ἡ κατὰ χρόνον, εἰκὸς ἂν εἴη μηνύεσθαι τὴν κατ’ ἀριθμόν* — then it is the beginning **according to number**, so that "in the beginning he created" means "first of all he created the heaven" | **K1** ⭐ |
| **21–22, 26** | the substance was of itself *ἄτακτος, ἄποιος, ἄψυχος* — without order, quality or life, full of disorder | **K6, K4** |
| **35** | *καὶ ἡμέραν οὐχὶ πρώτην, ἀλλὰ μίαν, ἣ λέλεκται διὰ τὴν τοῦ νοητοῦ κόσμου **μόνωσιν** μοναδικὴν ἔχοντος φύσιν* | **K10** ⭐⭐⭐ |
| **36** | the incorporeal world was complete in the divine Reason; heaven is called *στερέωμα* precisely as corporeal, against the intelligible | **K5** ⭐ |
| **29–31** | the intelligible light, *νοητὸν φῶς*, before sun and moon | **K8 `first-light`** — check this one; it may add a sixth crux |

**Two of those are not additions to a crux, they are the head of the crux's own finding.**

1. **K1's finding turns on the architect's plan** — it says Bereshit Rabbah 1:1 makes the Torah the
   *amon*, "the architect's plan the King builds from". **Philo has the same parable, in Greek,
   four hundred years earlier**: the king, the architect, the plan stamped in his mind, the city
   that has no place but the mind that holds it. The rabbinic bench and the Hellenistic-Jewish
   bench are telling one story. Nobody has to have borrowed it for that to be the most interesting
   fact on the daf, and the finding cannot stay as it is once `br-1-1` and this sit side by side.
2. **K10's finding says Augustine's morning/evening knowledge and Rashi's *yachid be-olamo* both
   read *unus* as a claim about solitude rather than counting.** Philo says exactly that and gives
   the word: *μόνωσις*, the solitariness of the intelligible world, which has a *monadic* nature —
   and he states the contrast the crux is named for, *οὐχὶ πρώτην ἀλλὰ μίαν*, not first but one.
   He is the head of **both** streams the finding contrasts.

⚠ **So this session will almost certainly require amending K1's and K10's findings, and possibly
K5's. Findings are Wilson's.** Write the evidence, state the case in `notes/SOURCES-FINDINGS.md`,
put the amendment to him, and do not execute it — the pattern of Phase 6 parts one and three.

## English: draft fresh from the Greek

**Yonge (1854) is public domain and is in the same repo, aligned section by section**, so it is
embeddable. **Do not embed it.** Its register fights the frozen renderings badly — it gives
*νοητός* as "perceptible only by the intellect" (five words for "intelligible"), and it paraphrases
freely. **Draft fresh from the Greek, `DRAFT` not `APPROVED`, with Yonge cited in the witness notes
as the public-domain English available for checking** — the same call made for Onkelos at
`targ-onk-1-5` and for Sanhedrin 38b.

**Register additions this session must freeze** (extend the list, do not re-decide it):
*νοητὸς κόσμος* = "the intelligible world" and *αἰσθητὸς κόσμος* = "the perceptible world", never
"world of ideas"; *λόγος* = "Reason" where it is God's and "word" where it is speech, kept apart
and flagged in the notes wherever the choice is contestable; *ἀρχή* = "beginning" throughout, with
*κατὰ χρόνον* / *κατ’ ἀριθμόν* = "according to time" / "according to number"; *μόνωσις* =
"solitariness" and *μοναδικός* = "monadic", **not** "unity" — the whole K10 point is that the word
is about being alone; *δημιουργός* = "craftsman" (as *artifex/faber* already is at K7);
*στερέωμα* = "firmament"; *ἄποιος* = "without quality", *ἄτακτος* = "without order"; *ἰδέα* =
"idea" untranslated as a school term; *παράδειγμα* = "model".

## Persons, places, keys to add

`philo` **already exists** in `data/persons.json` — added at Phase 6 part four when Chalcidius
cited him. Check and extend the note rather than re-adding. Place: `alexandria`, which already
exists. New licence key for the First1KGreek text. `work` key: `philo-opif`.

## Traps

- ⛔ **Strip `<note>` before flattening.** See above. This is the whole of the risk in this session.
- ⛔ **Yonge's section alignment is the TEI's, not Yonge's own** — his printed chapters (I, II, III…)
  are coarser than Cohn's sections. Cite Cohn's §, and give the Cohn–Wendland page from `<pb>`.
- ⛔ Fresh English is **`DRAFT`**, not `APPROVED`.
- ⛔ `overlap.py` does not cover him — it maps the PL TEI only. No collision risk, but `grep -l`
  against `data/witnesses/*.json` before reusing an id.
- ⚠ **Do not let him become a third bench in the site's framing without asking.** He goes in as
  `greek-jewish` beside the LXX, which is structurally free. Whether the index and colophon should
  stop describing the edition as two benches is **Wilson's call and a separate one** — raise it
  when the witnesses are built and he can see what they look like on the daf.
