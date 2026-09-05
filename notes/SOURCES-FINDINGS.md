# Source findings — 2026-09-05 (first session)

What the plan assumed vs. what the sources actually are. Read before extraction.

## Latin bench (all local: `~/patrologia/sources/pl/tei/<idno>.xml`, index `~/patrologia/data/cc-pl-index.json`)

Resolved ids in `data/latin-bench.json`. Every PL work on the bench is on disk. Two are not in PL at all:

- **Origen, Hom. in Gen. (Rufinus)** — PG 12, not in the PL harvest. Source separately (Baehrens GCS is PD; archive.org) or defer.
- **Claudius of Turin on Genesis** — not in PL. Drop from pilot.

Aliases: Bede *In Genesim* = "Hexaemeron (Beda)" idno 8466 · Bruno of Segni = "Bruno Astensis, Expositio in Pentateuchum" 21403 · Wigbod = "Wicbodus" 8606 · Basil = "Eustathius, Metaphrasis Latina Hexaemeri" 7608 · Rupert *In Genesim* is inside *De Trinitate* 10873 (661K words; slice the first ~150K chars).

Column anchors: the TEI `<pb n="0939A"/>` marks resolve to PL columns; `scripts/build-k7.py` computes them. Sample-check against the Migne scan before trusting (per `~/patrologia/CLAUDE.md`: Corpus Corporum departs from Migne ~3 sites/page).

## Rabbinic bench (Sefaria v3 API; pulls in `raw/sefaria/`)

Licence surprises — the plan's "Aramaic is CC0" is wrong for the Bavli:

| Work | Original | English |
|---|---|---|
| Bavli (Chag 12a, 15a, Meg 9a, RH 10b–11a) | Davidson vocalized Aramaic is **CC BY-NC**. Use **"Wikisource Talmud Bavli" (CC BY-SA)**. | Davidson/Steinsaltz NC → never embed. "Sefaria Community Translation" is CC0 but patchy (RH: 1 segment). Translate fresh. |
| Bereshit Rabbah 1–3 | Default "Midrash Rabbah -- TE" licence *unknown*; a **"Daat Bereshit Rabbah" PD** version exists but did not return by title (try per-section). | **Sefaria Midrash Rabbah 2022, CC BY** — embed with attribution. |
| Rashi Gen 1 | Silbermann Hebrew, PD | Silbermann English, PD |
| Onkelos | "Onkelos Genesis" PD | Default English is Metsudah (**NC**). Etheridge (PD) is listed but didn't return by version title; fetch from archive.org. |
| Pseudo-Jonathan | PD | Etheridge 1862 PD — returned fine |
| Neofiti | Vatican MS transcription, licence *unknown* (whole of 1:1–5 as one segment) | Community translation CC0 |
| Yerushalmi Chag 2:1 | **Guggenheimer edition + translation both CC BY** on Sefaria → **resolves open decision §9.4: include, no fresh translation needed.** Verify the licence claim on Sefaria's version page. | |
| Mishnah Chag 2:1 | Torat Emet PD | default English is Davidson NC; use Kulp or translate |
| PdRE 3 | PD | Friedlander 1916 PD |
| Tanchuma Bereshit 1 | ref is `Midrash_Tanchuma,_Bereshit.1` (comma). Torat Emet PD | Berman **CC BY** (plan feared NC — it isn't) |
| Ibn Ezra Gen 1 | Piotrkow 1907 PD | Community CC0 (14 of 18 segs); Strickman–Silver is NC |
| Ramban Gen 1 | Vocalized ed. CC BY | **Chavel shows as CC BY on Sefaria** — surprising for a 1971 Shilo text; verify before embedding, else fresh. |
| Gen 1:1–5 Hebrew | Miqra according to the Masorah, CC BY-SA | JPS gender-sensitive is NC → use WEB (pulled, `raw/web-gen-1-1-5.json`). **WEB prints 1:5 as "the first day"** — a K10 datum. |

## K7 (ruach-hovering) — what extraction found that the plan didn't list

- **Rupert of Deutz** has the warmed egg (PL 167:205C) with no Syrian — image already naturalized.
- **Wigbod** quotes Jerome verbatim under the label HIERONYMUS (96:1116C) and Augustine Gnm (96:1112D): a Carolingian catena showing both Latin lines side by side.
- **Angelomus** splices Augustine's "non localiter sed potentialiter" onto Jerome's bird, unnamed, as "alia translatio" (115:116A).
- **Abelard** reports "Hebraicum habet volitabat" (178:735B) — against Jerome's incubabat and on the rabbinic side of the verb. Source unknown [CHECK].
- **Comestor** fuses Jerome's Hebrew + Basil's Syriac and turns the bird against Plato's world-soul (198:1057A).
- **Rashi's la'az acoveter** = Jerome's incubabat. Same vernacular sense, no contact.
- **Rashi's dove** is the Bavli's (yonah, Chag 15a), not BR 2:4's unspecified bird — settles the `cites` edge.
- **Bede has no bird** on 1:2; Trinitarian only (K3). Rabanus copies him verbatim (107:447C).
- Hugh *De sacramentis* and Rupert `fovebat` grep hits were false positives; Hugh's 1:2 is in the *Adnotationes* (175:36A).

## Still open

- Glossa on Gen 1:2 — Wilson's edition in progress; slot `glossa-1-2-ruach` reserved.
- Etheridge Onkelos, Daat BR Hebrew: fetch by alternate route.
- Sefaria attribution string for Midrash Rabbah: paste exact text into `data/licenses.json`.
- Bonaventure II Sent. d.12–13 files: `~/bonaventure-sentences/vol2/bon-sent-II-d12-*.md`, `-d13-*.md` (K4/K8/K10, not K7).

---

# K10 (one-day-evening-first) — 2026-09-05, second session

## What the plan listed vs. what the sources are

The plan's K10 list (`PLAN.md` §5) was accurate everywhere it named a locus, and thin in two places.

- **Ambrose Hex I.10 is the centre of the Latin side, not a supporting witness.** Migne's chapter
  heading is the crux itself: *"Diem nocti contra quam nonnullis videatur, hic anteponi. Cur dies
  unus potius dicatur quam primus; ac matutino fine concludatur."* Ambrose gives three answers in
  two paragraphs (day has the birthright; one circuit = one day of 24 hours; Scripture names the
  greater term for the pair) and a fourth at 145C (set apart as *one*, not compared as *first*).
- **Bruno of Segni (PL 164:150A) is the best-matched Latin answer to Bereshit Rabbah 3:9** and was
  not in the plan at all. *Primus et secundus relativa sunt, neque sine altero alter esse potest* —
  with no second day yet, nothing could be called first. He also states the hard thesis nobody else
  states: *nulla dies ex nocte constat ac die.*
- **b. Chullin 83a was not in the plan and is the crux's sharpest two-sided thread.** Ben Zoma —
  the same tradent as K7's hovering dove — derives from *yom echad* by verbal analogy with
  Lev 22:28 that **the day follows the night**. Augustine says in so many words that the days are
  counted *a mane usque in mane* (Gnm I.10). Pulled this session; added to `pull-sefaria.py`.
  Only the Wikisource Aramaic returned; no free English, so the English is a fresh draft.
- **RH 10b–11a (Tishrei vs Nisan) was dropped.** Its argument is on Gen 1:11–12, not 1:5, and a
  witness must be a continuous argument *on the verse*. The Hebrew is on disk (28 segments,
  nested per daf) if a later session wants it for a calendar crux; the English came back with one
  segment only.
- **Rupert has two loci, and the second is the explicit one.** PL 167:217 (In Gen., chapter heading
  *"Cur non dictum sit … dies primus, sed factum est vespere et mane dies unus"*) argues that what
  God divided cannot be recombined; PL 167:1807A (in the books on the Spirit's works, same TEI
  10873) states the answer flatly — the writer refused *dies primus* because the day first by
  nature is eternal and this one is first only by number. Only the first is built as a witness.
- **Honorius answers the question twice in TEI 10991.** At PL 172:255D, *non primus sed unus quia
  idem semper repetitur*; at PL 172:261D, *non primus sed unus quia angelica natura … nullo fine
  terminatur*. The TEI carries one `<title>` ("Hexaemeron") and both columns are inside the PL
  range for that work, but a work commenting on 1:5 twice is odd. **[CHECK the work division at
  PL 172:261 before promoting the second passage to a witness.]** Only the first is built.
- **The Glossa on 1:5 is two glosses and one of them is a pointer.** Gregory, *Moralia* VIII.6 on
  why *vespera* and not *nox*; then Augustine *de Gen. ad litt.* IV.22–23 cited by book, chapter
  and Migne column and abbreviated with the Glossa's *"etc., usque ad"*. Wilson's Glossa edition
  has not reached 1:5, so the English here is a `claude-draft` and is superseded when it does.
- **Bonaventure II Sent. d.12 a.1 q.2 is exactly the contested-Augustine witness the plan wanted.**
  Wilson's edition carries Latin and English in one file; both are sliced from it and the English
  is credited `wilson-pruitt` under a new licence key `wroot-bonaventure` **[CHECK: Wilson to set,
  as with `wroot-glossa`]**. Quaracchi's marginal labels are italic in the markdown; the asterisks
  are stripped on the way in.
- **Isidore has nothing on 1:5** in the *Quaestiones*; his hits are on Gen 2:4 and the six ages.
  Not built.
- **Hugh has two treatments.** *De sacramentis* (PL 176:194B) is the fuller one and is built;
  the *Adnotationes* (PL 175:35A) argue the same in brief and add a proof from the equinox.

## Text problems found

- **Rupert, PL 167:217A**: the Corpus Corporum text prints *"Bene ergo dictum est: Factae sunt
  tenebrae et lux dies unus"* immediately after saying that the writer did **not** say this. It
  should almost certainly read *"Bene ergo non dictum est"*. The sentence is elided in the English
  with `[…]`. **[CHECK the PL plate.]**
- **Rabanus, PL 107:448D** departs from Bede at two words: *dicamus* for *discamus*, and *in re
  creata resurgeret* for *recreata resurgeret*. The second looks like a printer's separation of
  *recreata*, not a variant. **[CHECK the plate before treating either as Rabanus' own.]**
- **Bruno, PL 164:149B** prints *tuce* for *luce* (as it printed *Dei. vero* in K7). The Corpus
  Corporum digitisation of Bruno is noticeably dirtier than the rest of the bench.

## A pipeline defect this crux surfaced

`check.py` grew a sixth check (answer ids and licence keys must resolve), and it immediately caught
a K7 bug: `targ-onk-1-2` wrote `original.license: "public-domain"` because the K7 build lowercased
Sefaria's "Public Domain" string, while `licenses.json` keys that licence `pd`. Fixed in
`cruxes/ruach-hovering.py` by normalising the one string; no argument, thread or English touched.

---

# K1 (beginning-of-what) — 2026-09-05, third session

34 witnesses, 44 threads. The plan's K1 list (`PLAN.md` §5) named eleven Latin loci and five rabbinic
ones and was right about all of them; what it did not have is below.

## What the plan listed vs. what the sources are

- **The Glossa's gloss on 1:1 is Alcuin's, and it is one word.** The plan asked for
  `Glossa marginal "in principio, id est in Filio" [CHECK exact gloss]`. Resolved: PL 113:69A prints
  **`(ALCUIN. in Gen. tom. I.) « In principio. » Filio`** — not a clause, a single word standing for
  an answer. The verse carries five glosses in all: an unattributed Augustinian one distinguishing
  *principium* (origin) from *Verbum* (perfecting), three from Bede cited by book and Migne column,
  Alcuin's one-word gloss, and a *Mystice* paragraph that is Isidore's allegory unattributed.
- **Alcuin's own book is where that word comes from, and it is four words long.** *Interrogationes
  et responsiones* 26 (PL 100:519C): *"Quid est: In principio creavit Deus coelum et terram? — Resp.
  In Filio perfecit Deus coelum et terram."* Migne records a manuscript variant *fecit* for
  *perfecit*; the two are not equivalent and the variant is kept in the English.
- **Wigbod drops exactly the refutation.** PL 96:1105C reproduces Jerome's *Quaestiones* on 1:1
  almost entire — the three Greek versions, *Bresith*, Aquila's *in capitulo*, the forehead of
  Genesis, Ps 40:8, John 1:3, the Hebrew custom of naming books — and omits the authorities who read
  *in filio* **and Jerome's disproof of them**, including *"et non BABEN, quod appellatur in filio"*.
  He also reaches the passage under a question about the book's *title*, not about the verse. This
  is the same silent-editing pattern K7 found in him at 96:1116C, but there it preserved the
  argument and here it reverses it.
- **Rupert of Deutz repairs the philology four hundred years later, and nobody asked him to.**
  PL 167:202A states the Hebrew evidence in his own mouth — *"filius quippe ben, principium vero
  bresith dicitur in illa lingua"* — concedes it, and holds the Christological reading anyway on the
  ground that the identity is *sensu* and not *voce*. He also gets there by an argument nobody else
  on the bench makes: *in principio creavit* would say *in principio principium fecit* and so be a
  **vitium in superfluitate dictionis** unless *principium* is a proper name.
- **Bruno of Segni answers the crux twice, in two places, and treats the answers as layers.**
  PL 164:147B is the literal exposition (*in principio creaturarum omnium*, with Sir 18:1 and
  *simul*); PL 164:150A, after the whole first day has been expounded *ad litteram*, turns back:
  *"In quo principio? In eo utique qui ait: Ego principium."* Built as two witnesses.
- **Comestor states the settlement as a rule of reading.** PL 198:1056A: *"Creatus autem est in
  principio, id est in Filio, et **iterandum est in principio** sic: In principio creavit Deus coelum
  et terram, in principio scilicet temporis."* Say the phrase twice. He then adds Bruno's third sense
  as an alternative. Note his *aeternus / sempiternus* distinction, which the English must keep.
- **Honorius sees the cost of reading Genesis and John together** (PL 172:254B): in Genesis the
  *principium* is the Son, in John it is the Father. He resolves it by the unity of substance.
- **Rabanus' own sentence stands in front of Bede's paragraph** (PL 107:444B): *"In principio itaque
  temporis, coelum et terram Deus fecit. Tempus enim ab hoc mundo, non ante mundum: dies autem
  temporis est portio, non principium."* Then Bede verbatim, with the house-building simile cut.
- **Remigius does the Latin grammar out loud** (PL 131:53D): *"In principio, et subauditur:
  temporis"* — a supplied genitive — after a doxography of Plato's three principles and Aristotle's
  two that Bede does not have.
- **Ambrose answers at two chapters, not one.** I.2 (PL 14:124B) holds the temporal and the personal
  readings together in a single *vel* and is the first Latin use of John 8:25 on this verse; I.3
  (PL 14:126A) is the polemical answer — the world has a beginning, *ne anarchon* — and quotes
  Ps 104:24, the verse the whole Latin bench will use to get from *in principio* to *in Sapientia*.
- **Augustine has four separate treatments and they are not the same argument.** *De Gen. c. Man.*
  I.2 (34:174, "not in the beginning of time but in Christ", then time as a creature); *De Gen. ad
  litt. imp.* II.6 (34:222, *Principium sine principio* / *cum alio principio*, plus a third reading
  nobody else takes up — the first intellectual creature as a beginning to what it heads); *De Gen.
  ad litt.* I.1 (34:247, the three readings listed and left open); *Civ.* XI.32 (41:345, the Ps 104:24
  inference). *Conf.* XI.9 (32:813) is built as a fifth. **Conf. XIII.5 (32:847) belongs to K3.**
- **Ibn Ezra and Ramban both belong here, not only to K4.** Ibn Ezra on 1:1 is the crux conducted
  purely as grammar (three opinions, each refuted from a counter-example, then his own: construct,
  like Jer 26:1). Ramban's *first* movement quotes Rashi's plain sense and **breaks its premise**
  with Isa 46:10 and Deut 33:21; his *hyle* paragraph, which follows immediately in the same segment,
  is K4's and is not sliced.
- **Three targums, three renderings, and only one interprets.** Onkelos *be-qadmin*; Pseudo-Jonathan
  *min avvela*; Neofiti *min qadmin be-ḥokhmah*, "from the first, in wisdom", plus a second verb
  *shakhlel*, "and finished".

## Text and licence problems found

- **Neofiti's licence is still unknown** (Sefaria's "Vatican Manuscript of the Targum Neofiti"); the
  original is marked `check`. The CC0 community English prints **"in great wisdom"**; there is no
  word for "great" in the Aramaic, and the marginal בחוכמתא is simply the emphatic state.
- **Chavel's Ramban shows as CC BY on Sefaria**, which remains surprising for a 1971 Shilo text.
  Embedded under a new licence key **`chavel-ramban`** carrying a `[CHECK]`, on the pattern of
  `wroot-bonaventure`. Verify the version page before publication or replace with a fresh draft.
- **Ramban's Hebrew and English anchors do not match by string**: Sefaria's vocalized Hebrew and any
  anchor retyped through a terminal differ in **combining-mark order**, so `t.find()` fails on a
  phrase that is visibly present. The spec file slices Hebrew by matching on the **consonantal
  skeleton** (strip U+0591–U+05C7, find, map offsets back). Any later crux slicing vocalized Hebrew
  by anchor needs the same helper — it is a trap that looks like a missing text.
- **Wigbod, PL 96:1105C** prints *ex principibus* where Jerome has *ex principiis*. A printer's
  error, not a variant; the English follows Jerome. **[CHECK the plate if it is ever quoted.]**
- **Migne page-numbers survive inside the sliced Latin** (e.g. `306` inside Jerome's sentence at
  PL 23:938C). The TEI marks them as text, not as `<pb>`; they are left in the Latin and dropped
  from the English, as in K10.

## A pipeline defect this crux surfaced

- **`scripts/render-daf.py` requires Python 3.12 or later** (it uses backslashes inside f-string
  expressions). `python3.11 scripts/render-daf.py` fails with a `SyntaxError` that reads like a bug
  in the file. The machine's `python3` is 3.14.6 and is the interpreter to use; `render-map.py`,
  `build-crux.py` and `check.py` all run under 3.11 as well, which makes the failure look selective.
- **Witness ids collide across cruxes and nothing catches it.** K7 built a witness called
  `rabanus-gen-1-1` whose anchor is **Gen 1:2**; K1's Rabanus on Gen 1:1 therefore had to be built as
  `rabanus-gen-1-1b`. `build-crux.py` writes `data/witnesses/<id>.json` unconditionally, so a
  colliding id in a later crux would silently overwrite an earlier crux's witness. Worth a seventh
  check in `check.py`, or a guard in the builder, at Phase 4.
