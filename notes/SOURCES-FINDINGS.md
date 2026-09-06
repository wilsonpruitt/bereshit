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

---

# K8 (first-light) — 2026-09-05, fourth session

27 witnesses, 35 threads. `notes/cross-crux.md` was right that most of the rabbinic material was
already on disk and read; the Latin side was larger than the plan expected.

## What the plan listed vs. what the sources are

- **The Latin bench splits three ways, not two, and the third is Abelard's alone.** Beside the
  angelic light (Augustine, Angelomus, Rupert) and the bodily one (Basil, Ambrose, Bede, Hugh,
  Honorius, Comestor, Bonaventure), Abelard makes the light **the distinction of the works
  themselves** (PL 178:738B): *"Lucem vero istam quae praedictas tenebras removit, ipsam sequentium
  operum distinctionem accipimus."* Not a body and not an angel — the confused heap becoming
  distinct and knowable. It is the only reading on the crux for which the fourth day raises no
  difficulty at all.
- **Abelard reports the Hebrew again** (PL 178:739D), exactly as K7 found him doing with *volitabat*:
  *"pro eo quod dicimus: Fiat lux, et facta est lux, in Hebraeo haberi: Sit lux, et fuit lux."* The
  observation is correct — *yehi or va-yehi or* is one verb twice, as the Greek's γενηθήτω / ἐγένετο
  is — and his conclusion, that no delay is interposed, is what the rest of the bench reaches by
  other routes. **Source still unknown** [CHECK], as at K7.
- **Bede does not refute the angelic light; he steps round it in one sentence** (PL 91:16C) by
  naming three lights instead of two — God the true light, the inaccessible light the angels were
  *already* enjoying in the heaven of heavens, and *primam materialis gratiam lucis* given to this
  world. The angels are on the page, already made, and are not the light. Alcuin, Rabanus and the
  Glossa's Bede gloss all inherit the step without noticing it is one.
- **Alcuin adds two words to Bede that are a doctrine** (PL 100:520A, Int. 33): *a luce aeterna lux
  temporalis*. Bede set the eternal light beside the material one; Alcuin derives the second from
  the first.
- **Bede's divers are an argument and the Glossa keeps only half of it.** PL 91:17A defends light in
  the waters by sailors who let oil out of their mouths to see under water, and closes with the pun
  that carries it: if a man can do it *per oleum sui oris*, what can God do *per Spiritum oris sui*?
  The Glossa (113:71A) keeps the divers and cuts the pun.
- **The twelfth century builds a physics, and three writers of one generation agree on it without
  citing each other**: Hugh, *Adnot.* (175:34C), the element of fire carried round *quasi quaedam
  lucida nubes, sicut modo sol*; Honorius (172:255C), *hanc corporalem lucem de elemento ignis*, a
  brightness like the sky before sunrise, twelve hours above and twelve below; Comestor (198:1057B),
  *quamdam nubem lucidam … claritate tamen tenui, ut fieri solet diluculo*. All three are Remigius'
  twilight (131:55B) given a body and an orbit.
- **Rupert's counter-argument is the best thing on the crux and it is his own** (167:207A): the
  physical light would make the first day *omnium dierum pauperrimus* — every other day makes a
  substance that abides, this one an unstable accident snuffed out after three days by a God who
  changed his counsel. Would the majesty that laid on sun and moon *praeceptum quod non praeteribit*
  do that? He also insists in the next chapter that the angelic light is meant *non pro similitudine,
  sed pro re vera*: the visible stars were made in the likeness of that light, not the reverse.
- **Bruno declines the question** (164:149B). He asks it in the bench's own words — *quae est ista
  lux, quae prior sole, luna, et stellis esse perhibetur?* — and answers that the verse settles it
  two clauses later: *Lux igitur pro die ponitur.*
- **Bonaventure closes it, and closes it on the weight of expositors** (II Sent. d.13 a.1 q.1,
  Quaracchi II.312–313), which is the same move as K10's d.12 a.1 q.2. He grants Augustine's
  position is probable and reasonable and declines it because *istam positionem magis insinuat textus
  Scripturae, et magis sequuntur expositores*. His report of Augustine also preserves an argument
  Augustine makes obliquely: that of bodily things Scripture says *fiat*, *fecit* and *factum est*,
  and of the light it does not.
- **The Glossa refuses to decide this verse**, unlike Gen 1:1. Four glosses: Augustine stating the
  disjunction, Bede giving the bodily light with its place and its divers, and two more Augustine
  glosses giving the angelic reading in full (*et facta est lux, id est angelica et coelestis
  substantia*). No verdict on the page.
- **Bereshit Rabbah 3:4 asks the question the Latin bench never asks** — not what the light was but
  what it was made *from* — and gives two answers: the garment of Ps 104:2 (said in a whisper, and
  the exchange about why it is whispered is part of the witness), and, from R. Berekhya in the name
  of R. Yitzḥak, **the site of the Temple**.
- **PdRE 3 turns the garment into cosmogony**: the heavens were made *out of* the light of the
  garment, stretched until God said *Dai* — whence El Shaddai. Nothing on the Latin bench makes the
  first light the stuff of anything, except the unnamed opinion Augustine reports.
- **Not built, and deliberately**: BR 3:2 (*vayhi* and not *vehaya*, the light came about at once)
  and BR 3:5 (light named five times for the five books). Both are about the wording rather than
  about what the light is. BR 3:2 belongs with the *fiat-is-instantaneous* answer family if a later
  session wants it.

## Text and licence problems found

- **b. Chagigah 12a: the Hebrew and English segment arrays align, but the crux material is at
  indices 7–11, not 6–10.** Index 6 is the *tohu* green-line baraita. Both versions on disk
  (Wikisource Aramaic CC BY-SA; Sefaria Community Translation CC0) segment identically — checked
  segment by segment before slicing.
- **Wilson's Bonaventure markdown needed a hyphenation repair.** The Quaracchi page break falls
  inside a word (*appro-* / p.313 / *baverunt*), so joining the paragraphs across the page marker
  produces *appro- baverunt*. The K8 slicer strips `-\n\n`. It also strips **all** asterisks rather
  than trying to pair them: an odd asterisk left by an unpaired `**bold**` marker leaked one into
  the text on the first build (*per lucem\* illam*). **K10's `cruxes/one-day-evening-first.py` uses
  the pairing regex and may carry the same latent defect** — not touched, per the one-crux rule.

## A note for Phase 4

`aug-gnl-4-22` and `alcuin-int-34`, both built for K10, carry `first-light` in their own facets and
so appear on this crux's daf without any K8-tagged thread attached to them. That is the design
working, not a fault; but Phase 4 should decide whether a witness that appears on a crux ought to be
threaded into it, or whether unthreaded cross-crux carriers are acceptable on the page.

---

# K6 (tohu-vabohu) — 2026-09-05, fifth session

## The crux is a text-critical fact before it is an exegetical one

`PLAN.md` §5 said the Vulgate's *inanis et vacua* is "a witness in its own right: Latin readers
inherited an interpretation, not a transliteration." That is true and it is only half of it. **The
Latin bench holds two texts of Gen 1:2 at once**, and the split runs straight down the middle of
the roster:

- *terra invisibilis et incomposita* — the Old Latin of the LXX's ἀόρατος καὶ ἀκατασκεύαστος — is
  the lemma of **Augustine everywhere** (Gnm, Gnl, Gnl imp., Conf. XII, Civ.), of **Ambrose**, of
  **Eustathius' Basil**, and of **Alcuin**, who flags it: *(Ibid. ex vers. LXX)*.
- *inanis et vacua* is the lemma of **Isidore, Bede, Wigbod (in one half of his book), Rabanus,
  Remigius, the Glossa, Bruno, Rupert, Abelard, both Hughs, Honorius and Comestor**.

The two lemmas ask different questions. "Invisible and unordered" invites answers about light and
form; "empty and void" invites a list of what was missing. The second question is the one the
schools inherit, and by the twelfth century the seeds-and-shoots answer is standard property
(Rupert, Abelard, Hugh *Adnot.*, each with the two privations distributed differently, none citing
another).

- **Wigbod has both and does not notice.** PL 96:1111B prints Augustine's Manichaean paragraph
  under *invisibilis et incomposita*; PL 96:1116B asks *"Cur inanis et vacua?"* and answers about
  coastlines. Five columns, one book, no seam.
- **Angelomus splices them in one paragraph** (PL 115:114D): the Vulgate question, Augustine's
  unformed matter, then *"Unde alia translatio dicit: Invisa et incomposita"* — glossed with
  **Alcuin's Interrogatio 30 word for word**, unattributed.
- **Hugh of St Victor is the first to tell a reader plainly** that the clause exists in two Latin
  forms: *"sive, ut alia translatio habet, incomposita"* (PL 176:190D).

## Jerome does not gloss the pair he made — `PLAN.md`'s [CHECK] resolved

`grep-bench.py "inanis|vacua|incomposit" jerome-hq` returns **0 hits**. The *Hebrew Questions* run
straight from *In principio fecit Deus coelum et terram* (PL 23:937C) to *(Vers. 2.) Et Spiritus
Dei ferebatur super aquas* (939A). The translator who put *inanis et vacua* into the Latin Bible
left no note on it, and the note he did leave on this verse — *merefeth / incubabat* — is K7's.

## What the plan listed vs. what the sources are

- **Bereshit Rabbah 2 is four readings of the pair, not one.** 2:1 (R. Berekhya, Prov 20:11 →
  Jer 4:23), 2:2 (R. Abahu and R. Yehuda bar Simon: the two slaves, the two maidservants — the
  earth sits *toheh u-voheh* with a grievance), 2:3 (the generations: Adam, Cain, Enosh, the Flood,
  Abraham), 2:5 (the deeds of the wicked; the Temple built, destroyed, rebuilt). **2:4, the four
  kingdoms, is already built as a K7 witness** for the Messiah's spirit and its first half belongs
  here too — left for Phase 4, per the frozen rule.
- **The whole rabbinic side reads the pair through Jer 4:23**, "I have seen the land, and behold it
  is *tohu va-vohu*" — a prophet using the phrase of a land under judgement. **No Latin witness on
  this crux cites Jer 4:23 at all.** That single intertext is why one bench can read the clause as
  history and the other cannot.
- **b. Chagigah 12a segment 6 was not in the plan and is the sharpest answer on either bench** to
  "state or thing": *tohu* is a green line encircling the world, *bohu* are slimy stones sunk in
  the deep, proved from Isa 34:11. It sits inside the ten-things-made-on-day-one list (segments
  4–5, which are **K5's** text), so both are creatures with a date.
- **Ramban's *bohu* paragraph is a K6 witness, not only a K4 one.** `notes/cross-crux.md` had
  filed the whole *hyle* passage under K4. The first half (creation from absolute nothing, the
  hyle as the only created thing) is K4's; the second half — *tohu* = the hyle, from *betohe*
  "he bethinks himself", because matter can hold no name; *bohu* = *bo hu*, "in it there is", the
  form; Isa 34:11 as a craftsman's measuring cord and the stones as forms — is the only place on
  either bench where the pair is a matched technical vocabulary. Sliced here from
  `וְהַחֹמֶר הַזֶּה, שֶׁקָּרְאוּ הִיּוּלִי`; the K4 half is untouched.
- **Ibn Ezra and Ramban divide on this verse.** Ibn Ezra names Sefer Yetzirah's green line and
  slimy stones and sets them aside for Onkelos (*tohu* = without substance); Ramban keeps Sefer
  Yetzirah, cites it approvingly, and makes *tohu* a substance. The two commentators Ramban reads
  side by side on 1:1 split here on whether the word names anything at all.
- **Rashi's *bohu* gloss is Onkelos.** He renders it *reikut ve-tzadu* — the two Aramaic words
  Onkelos uses for the whole pair, *tzadya ve-reikanya*, in the other order.
- **Isidore founds a lineage nobody else on the Latin bench starts.** PL 83:209B, *terra carnis
  nostrae … priusquam doctrinae acciperet formam*, is copied verbatim by Wigbod (96:1116B) and
  Rabanus (107:467A), stands at Remigius 131:55D, and is turned on the Church by **Bruno of Segni**
  (164:150B), whose reading of the clause as a periodization ending at Rom 11:25 has the same shape
  as Bereshit Rabbah 2:3's and 2:4's and the opposite contents.
- **The Glossa's second gloss on this lemma is Remigius verbatim.** Migne prints it under
  *(STRAB.)* at 113:69D — *"Inutilis scilicet, et infructuosa, et incomposita. Omnia enim elementa
  commixta, confusa…"* — and it is PL 131:55A to the last clause about the waters above the
  heavens. It is already on the site inside K7's `glossa-1-2-ruach` (Wilson's edition appended it),
  so only the *first* gloss on the lemma, Bede's, is sliced here as `glossa-1-2-terra`.
- **Comestor carries the Glossa's formula minus one adjective**, applied to the *machina mundialis*
  rather than to the earth, and identifies the deep with *chaos* flatly where Abelard had kept his
  distance.
- **Honorius (PL 172:260C) was read and not built.** *"corporalis creatura adhuc informata, sed in
  verbo Dei causaliter posita"* is one sentence and repeats Augustine's answer with nothing added;
  the *creavit omnia simul* argument around it is K10's and K4's.
- **Rabanus (PL 107:445A) copies Bede verbatim** on the angels-in-heaven argument, as at K7, and is
  not built; the transmission is already carried by the Glossa's gloss.

## Text problems found

- **Bede, PL 91:13C** reads *"divinae gloria praescientiae manet semper quietum"* where **both**
  Angelomus (115:114D) and the Glossa (113:69C) have *divinae praesentiae*. The Corpus Corporum
  reading is probably corrupt; the English brackets the phrase. **[CHECK the PL plate.]**
- **Bruno, PL 164:150C** carries a stray *3* before *ad Ecclesiam confugerent* (a signature or
  line mark pulled into the text). Dropped from the English. Bruno's digitisation continues to be
  the dirtiest on the bench (cf. *tuce* for *luce* at K10, *Dei. vero* at K7).
- **Abelard, PL 178:734C** prints *"ne forte,,"* with a doubled comma.

## Pipeline

- **`hcut` is now in `scripts/bench.py`.** PHASES.md said to lift the vocalized-Hebrew skeleton
  slicer out of `cruxes/beginning-of-what.py` at the third crux that needed it; K6 needed it for
  Ramban, so it moved. `beginning-of-what.py` still carries its own private copy and is untouched,
  since rebuilding K1 is not this session's business.

---

# K5 (heaven-earth-order) — 2026-09-05, sixth session

## The two benches refuse the same question with the same psalm

`PLAN.md` §5 predicted one `parallel` — Chagigah 12a's ten-things list beside Augustine's "what is
contained in *caelum et terra*" — and that thread is real (`t-k5-08`: an enumeration and a
generalisation of the same clause, at the same date, with no contact). But the sharper one was not
in the plan:

**Ps 102:26 [Vg 101:26] is on both benches, doing opposite work with the same logic.** The verse
names the earth before the heavens. R. Yehuda bar Ilai brings it as Beit Hillel's proof that the
earth was created first (BR 1:15). Ambrose brings the same reversal (from Ps 148:5, with 101:26
quoted whole immediately before) to prove that **the order of naming decides nothing**, since both
were made together — *"nihil interest quid prius exprimas, cum simul utrumque sit factum"* — and
then gives the reason: *lest heaven be reckoned the better by the privilege of being the firstborn
creature* (PL 14:135C). That is R. Shimon ben Yoḥai's stewpot and its lid, and it is exactly the
rule Bereshit Rabbah 1:15 closes with — where Scripture reverses an order in one place, it teaches
that the two are equal in honour (turtledoves and pigeons, father and mother, heaven and earth).
Milan, c. 387; Galilee, c. 450; no contact.

## Where they really divide: what "heaven" is

- **The Bavli reads the substance out of the noun.** *Mai shamayim?* — *sham mayim*, "there is
  water"; or, in the mishnaic tradition, fire and water mingled into the firmament (b. Chag 12a,
  segment 18). The Hebrew word can be made to spell what heaven is made of.
- **Latin's word will not spell anything**, so the bench imports a substance, and what it imports
  is **the empyrean**: not the visible firmament but a heaven *igneum … non ab ardore sed a
  splendore*, filled with angels the moment it was made (Job 38:7). **Remigius PL 131:54D is where
  it enters the gloss tradition**; the Glossa prints it almost verbatim at 113:68C (inside the
  VERS. 1 block K1 sliced whole); Comestor has it as *coelum empyreum et angelica natura* — and
  admits in passing that *philosophus empyreum non cognovit*.
- **Abelard throws it out** (PL 178:733C–734A): heaven is fire and air, earth is earth and water,
  and *"the angels, being of an incorporeal nature, are not included among the creatures of the
  world at all."* **Ibn Ezra makes the same objection from the other bench**, and it is a symmetry
  argument: those who say the heavens of v. 1 are the heavens of the heavens — *what will they then
  do with the earth?* Neither could have known the other.

## What the plan listed vs. what the sources are

- **Bereshit Rabbah 1:15 has five answers, not two.** Beit Shammai (throne then footstool, Isa
  66:1), Beit Hillel (palace from the ground up; Gen 2:4; Ps 102:26), R. Ḥanin turning Beit
  Shammai's own proof against them (*"the earth WAS"* — it already was), R. Yoḥanan in the sages'
  name splitting creation from completion, and R. Shimon ben Yoḥai's stewpot and lid. The section
  then generalises into a rule about Scripture's word order.
- **b. Chagigah 12a argues where Bereshit Rabbah illustrates**, and adds a resolution the
  Palestinian version does not have: **Resh Lakish** — created in one order, stretched out in the
  other (segment 17). That is Hugh of St Victor's *non ordinis sed dignitatis* six hundred years
  early, arrived at from the world's side rather than the writer's.
- **The R. Yishmael / R. Akiva encounter is on both rabbinic texts with different answers.** BR
  1:14: without the two *ets* "we might have said the heavens and the earth are deities" — and
  Akiva is rebuked for the answer (Deut 32:47) before giving the real one. b. Chag 12a segment 19:
  without them *shamayim* would be a name of the Holy One — and the answer stands unchallenged.
  Neither version ever considers that the *et* might include the angels; the Latin bench can think
  of little else.
- **Ramban gives the schools' answer and the midrash's in one paragraph and does not notice they
  are two.** *"The word ha'aretz includes these four elements"* is Abelard to the letter; then the
  particle *et*, with Bereshit Rabbah 1:14 named and quoted. The sentence joining them is "these
  include all created things which are corporeal."
- **Hugh of St Victor entertains the absurd answer before refusing it** (PL 176:191B): if heaven is
  named first, was heaven created *underneath*, as a foundation, and only set above at the
  forming? His second reason for the word order is better than his first and is purely
  compositional — the discourse that follows is about the earth, so the earth is named last.
- **PdRE 3 was not built.** Its cosmogony is the garment and the stretching-out (K8's material,
  already built as `pdre-3-6`); it has no dispute about which of the two came first.
- **Bruno of Segni PL 164:147B is the best Latin match to BR 1:15 and could not be built**, because
  K1 sliced exactly that passage as `bruno-gen-1-1`. He quotes Ps 101:26, concludes *"non igitur
  prius coelum, quam terram, sed simul et coelum Deus creavit et terram"*, and proves it from
  Sir 18:1. Phase 4 item — see `notes/cross-crux.md`.

## A structural gap this crux exposes

The daf rendered with **no `versiones` and no `glossa` column** (rab 9, patres 4, scholae 6). Every
version witness on Gen 1:1 — LXX, Vulgate, the three targums — and the Glossa's VERS. 1 block
belong to K1 and carry only that crux. **On a crux whose whole subject is the order of two words,
the witnesses that actually preserve that order are absent from the page.** Phase 4 should add
`heaven-earth-order` to the facets of `lxx-1-1`, `vulgate-1-1`, `targ-onk-1-1`, `targ-neof-1-1`,
`targ-psj-1-1` and `glossa-1-1` — the versions are relevant precisely because none of them reverses
the Hebrew order, while Gen 2:4, which every one of them also renders, does.

## Text problems found

- **Comestor, PL 198:1055A** prints *quaudoque* for *quandoque* (third occurrence only) and
  *hemines* for *homines* at 734A in Abelard — both plainly typographic, both left in the Latin and
  silently right in the English.
- **Abelard, PL 178:734A**: *natureae* for *naturae*.

## Method note

Because Gen 1:1 already carried 34 witnesses from K1, **every Latin slice was checked against K1's
slice boundaries before it was written** (`python3 -c` dump of each K1 witness's source column and
first/last 110 characters). Three of the eleven candidates turned out to be inside a K1 slice —
Bruno 147B, the Glossa's VERS. 1 block, and Rabanus 444B (which copies Ambrose Hex I.6.20 verbatim,
the passage this crux builds from Ambrose himself). **Do this check first on any remaining crux
anchored to a verse another crux has already built** — K2 (`why-begin-here`) and K3
(`elohim-and-trinity`) are both on 1:1–1:2 and will hit it harder than K5 did.

---

# K4 (ex-nihilo-or-matter) — 2026-09-05, seventh session

## One analogy, three benches, three kinds of answer

`PLAN.md` §5 predicted that both benches would reach for 2 Macc 7:28 and Wis 11:17 and find them
pulling opposite ways. **Half of that is wrong and the other half is bigger than the plan thought.**
2 Macc 7:28 is not quoted by a single witness on either bench in this crux. Wis 11:17 is quoted by
five Latin witnesses (Augustine, Bede, Rabanus, Angelomus, and the Glossa through Bede) and by no
rabbinic one, and it does not pull two ways — it pulls one way, *against* the doctrine, which is
why every Latin witness who quotes it immediately restricts it.

What is actually shared is **the craftsman**:

- **BR 1:9**: "Your God was a great artist, however he found many excellent raw materials that
  helped him: emptiness, disorder, darkness, wind, water, and depths."
- **Augustine, *Gnm* I.6.10 (PL 34:178)**: "we ought not to be like those who do not believe that
  almighty God could make anything out of nothing, *cum considerant fabros et quoslibet opifices
  non posse aliquid fabricare, nisi habuerint unde fabricent*" — wood helps the carpenter, silver
  the silversmith, gold the goldsmith, earth the potter.
- **Basil/Eustathius, PL 53:880C–881B**: "with us each art is exercised upon some matter brought to
  it, *sicut fabrilitas circa ferrum, carpentaria circa lignum* … so they suppose it is with the
  divine working too."

Thagaste 389, Caesarea via Eustathius c. 400, Galilee c. 450. The same inference from the same
analogy, and even the same verb — the materials *help*. **The answers are three different kinds of
thing.** Basil argues from the dignity of the unbegotten (call matter unbegotten and you have made
it God's equal). Augustine argues from omnipotence (if anything he had not made helped him, he was
not almighty). Rabban Gamliel answers with a concordance: of every one of the six, creation is
written — Isa 45:7 for tohu, bohu and darkness, Ps 148:4–5 for the water, Amos 4:13 for the wind,
Prov 8:24 for the deeps. Neither method would have satisfied the other, and that is the finding.

## The philological objection, three times in forty years

Not in the plan at all. Scripture uses the creation verb of things made out of something —
**Gen 1:21** (the sea-creatures) and **Gen 1:27** (man, three times in one verse):

| | date | move |
|---|---|---|
| **Rupert**, PL 167:202C | c. 1115, Liège | puts the objection to himself from both verses, in that order, and answers that *creavit* is right there **because the matter had already been created** |
| **Abelard**, PL 178:734B | c. 1130, Paraclete | separates two Latin verbs — *creare* of what has no *praejacens materia*, *formare* of what is shaped from matter, proved from *formavit* at Gen 2:7 and 2:19 |
| **Ibn Ezra** on 1:1, s.v. ברא | c. 1155, Lucca | brings the identical two verses in the identical order and concludes the commentators are wrong: **bara does not mean bringing forth something from nothing** |

⭐ **The Latin distinction exists only because the translation supplies two verbs where the Hebrew
has one at the decisive places.** *Creavit / formavit* is a fact about the Vulgate, not about
Genesis; Abelard builds a definition on it and never sees the seam. And **Ramban closes the
question by asserting the exclusive Ibn Ezra had denied** — "there is no expression in the sacred
language for bringing forth something from nothing other than the word *bara*" — a few lines after
naming R. Abraham. That is the one direct `contests` edge on the crux where both parties are on the
same bench and one has read the other.

## The position everyone refutes is held by the rabbinic bench, twice

- **BR 1:5, second half.** The parable of the palace built over the sewers, and then Rav Huna in the
  name of bar Kappara with the formula for saying the unsayable: *ilulei she-ha-davar katuv i
  efshar le-omro* — "In the beginning God created" — **from what?** — "the earth was tohu va-vohu."
  Four sections before BR 1:9, which refuses that inference to a philosopher's face. **Neither
  section acknowledges the other.**
- **PdRE 3:7.** "Whence was the earth created? He took of the snow beneath his Throne of Glory and
  threw it on the waters" (Job 37:6), with the heavens from the light of his garment in the
  preceding section (K8's `pdre-3-6`). No embarrassment at all. **The Latin bench has no answer of
  this shape and could not have**: once matter is what is at issue, a material that belongs to God
  is still a material, and Basil's objection falls on it as heavily as on Plato's hyle.

## What the plan listed vs. what the sources are

- **Hugh, *De sacramentis* I.1 CAP. I (PL 176:187A–B), not 247B.** PHASES pointed at 247B (the angels
  not made *de materia praejacente*, which is about angels, not the verse). 187A is the chapter
  headed *Unum esse principium a quo facta sunt omnia de nihilo*, opens with Gen 1:1, and is where
  the Latin bench begins its systematic theology. **When the Latin tradition organises itself into a
  summa, this crux is chapter one.**
- **Ambrose's doxography is at 14:123A, the first sentence of the Hexaemeron**, and is free: K1 had
  taken 124B (Moses against the philosophers) and K5/K6 the later columns. Every later Latin witness
  repeats one or both of its lists — Remigius 131:53D (inside K1's slice), Hugh (*opifex, materia,
  forma*), Comestor (Plato, Aristotle **and Epicurus**).
- **Alcuin *Inter*. 19–20 (PL 100:519A–B) is the Latin bench's only list.** "*Quae creaturae de
  nihilo factae sunt?* — Coelum, terra, angeli, lux, aer, aqua et anima hominis." Seven items,
  against b. Chagigah 12a's ten and PdRE 3:5's eight. **Identical form, and the contents diverge
  exactly where the doctrines do**: Alcuin's list has the angels and the human soul, which no
  rabbinic list has; the rabbinic lists have *tohu* and *bohu*, which Alcuin's question exists to
  exclude.
- **Wigbod copies Augustine entire here.** At K1 his signature was the omission — he takes over
  Jerome's discussion of *in principio* and drops precisely the refutation from the Hebrew. At
  PL 96:1113B he copies *Gnm* I.6.10 without losing a clause, to the closing *sacrilegum est
  credere*. **A fair index of what a Carolingian compiler thought load-bearing: philology about a
  Hebrew word is expendable, an argument securing omnipotence is not.**
- **Angelomus turns the objection back into a speech.** PL 115:114B: *Ista propterea dicunt, quia
  attendunt fabrum, et non Deum. Aiunt enim: Lignum adjuvat fabrum…* Augustine's "we ought not to be
  like those who…" has become reported speech with an (unnamed) speaker — the form the objection has
  at BR 1:9 and nowhere else on the Latin bench.
- **The Bede → Rabanus → Glossa chain loses the qualification.** Bede PL 91:15C opens *Ad haec
  tantum informis est illa materies* — formless only to this extent. Rabanus 107:446C copies the
  paragraph verbatim (not built; K6's precedent). The Glossa at 113:69D–70A keeps the last two
  sentences and drops the opening restriction with the sentence that carried it, so what a
  twelfth-century reader met in the margin is the flat statement that earth and water are called
  formless matter, with "or out of nothing" still attached and no longer doing any work.
- **Honorius PL 172:257A and Hugh *Adnot*. PL 175:33A were read and not built** — one clause each
  (*ad materiam ex nihilo creantur*; *In eo quod creavit, id est de nihilo*), adding nothing.
- **Rabanus PL 107:446C not built** (verbatim Bede, transmission already carried by the Glossa),
  and **Remigius 131:53D not available** (inside K1's `remigius-gen-1-1`).

## A structural gap, the same one K5 hit

The daf rendered **`versiones 0`** (rab 5, patres 7, scholae 9, glossa 1). On a crux where the whole
Latin argument turns on which verb the translation supplies — *creavit* against *formavit* — the
witnesses that actually supply it are absent, because `vulgate-1-1`, `lxx-1-1` and the three targums
belong to K1 and carry only that crux. **Phase 4 should add `ex-nihilo-or-matter` to their facets**;
this is now the second crux to hit it (see the K5 entry above) and the argument for it is stronger
here than there.

## Text problems found

- **Comestor, PL 198:1055B** prints *ile* for *hyle* ("Deum ideas, ile"). Left in the Latin, silently
  right in the English.
- **Wigbod, PL 96:1113B** reads *de nihilo facta est* where Augustine (PL 34:178) has *de omnino
  nihilo*; and *sic et caeteri omnes opifices* for Augustine's *sic et caeteri omnes hujusmodi
  opifices*. Both differences are in the English.
- **Angelomus, PL 115:114C** quotes Wis 11:17 as *Non enim erat manus tua, Domine, invalida, qua
  creasti mundum ex informi materia* — neither the Vulgate's wording nor Augustine's; rendered as he
  has it.

## Frozen-rendering conflict, resolved by usage

PHASES.md's K7 list froze *informis materia* = "formless matter"; the K1 addendum then wrote
*materia informis* = "unformed matter" **"as at K7"**, which K7 does not say, and the K6 addendum
propagated it citing K1. K4 followed usage, and **Wilson struck "unformed matter" on 2026-09-05**;
both PHASES lines are corrected.

⚠ **The correction is not cost-free, and the first count of it in this session was wrong.** The
built English is **23 occurrences of "formless matter" across 13 witnesses against 6 of "unformed
matter" across 4** — not, as first reported, none. Striking the line therefore leaves four
witnesses in drift, and Phase 3 owns them: `glossa-1-1` (K1), `angelom-gen-1-2-tohu` and
`glossa-1-2-terra` (K6) are all `claude-draft` and are a draft revision; **`bonaventure-sent-2-13-1-1`
is Wilson's own English** and is not to be changed mechanically. Note that Angelomus now reads
"unformed matter" at 1:2 and "formless matter" at 1:1 in K4's slice — one author, two renderings,
which is exactly the drift the frozen list exists to prevent.

## Method

The K1-overlap check was run first, as PHASES.md required, and mechanically rather than by column:
`scripts/overlap.py` (new, promoted out of the scratchpad this session) locates every existing
Latin witness's text inside its TEI by offset, builds a coverage map per idno, and reports each
candidate anchor as COVERED or FREE with the neighbouring slice boundaries. **Twenty candidates checked, three came back covered** — the Glossa's first gloss
on 1:2 (inside K1's `glossa-1-1`, which reaches from 67B to 69B), Comestor 1055B's *Empyreum autem*
(inside K5's `comestor-hs-1-1b`), and Ambrose 136A (inside K6's `ambrose-hex-1-7-25`). **Checking by
printed column would have missed all three**, because a single Migne column routinely holds two
witnesses from two different cruxes. K2 and K3 should use the same script.

## Pipeline

- **`scripts/overlap.py` added.** The K5 entry said to check every slice against the already-built
  ones on a crowded verse and did it with an ad-hoc `python3 -c` dump of columns and first/last
  characters. K4 needed it on two verses with 75 Latin witnesses already on them, so it is a script,
  and it works on offsets rather than columns. Run it as step 3.5 of the per-crux checklist.

## K9 `good-and-separated` (built 2026-09-05)

**What the plan got wrong or did not know.**

- The plan's Latin list for K9 was Augustine *Gnl* I.17, *Civ* XI.19–20, *Gnm* I.7, Bede, the
  Glossa, Rupert, Hugh, Lyra. Three of those are wrong loci. **Augustine's privation argument on
  this verse is at *Gnm* I.9 (PL 34:180), not I.7**, and PHASES.md's pointer to "*Gnm* I.4, PL
  34:176" is the earlier discussion of the darkness of v. 2, not the division of v. 4. **The richest
  Augustine text on the crux is not in the plan at all**: *De Genesi ad litteram imperfectus liber*
  §§23–25 (PL 34:228–230), where the privation doctrine acquires the term the whole tradition then
  uses — God does not *make* the darkness, he *orders* it — and the two analogies that carry it, the
  rests in a song and the shadows in a painting. `aug-gnl-imp` was on the bench and unqueried.
- **`grep-bench.py` on a five-alternative regex laid out the whole Latin bench in one call** (29
  hits across 7 twelfth-century works, 44 across the earlier ones), and the alternatives had to
  include *both* Latin texts of the verse — `inter lucem et tenebras` and `lucem a tenebris` — plus
  `lucem ac tenebras` and `separavit`. This is the K6 lesson holding: **a lemma with more than one
  Latin form is grepped for every form in one regex from the start.** Here it did more than save
  time; the split between the two forms turned out to be evidence (see below), and a single-form
  grep would have returned half the bench and hidden the fact.
- **Alcuin's *Interrogationes* have no question on *divisit*.** The divisit regex returned 0 hits
  for TEI 21416 and the crux nearly went without him; his contribution is Inter. 35, on *vidit Deus
  quod esset bonum*, found by reading the run of questions 31–35 directly. A work organised as
  questions will not answer a lemma grep if it did not ask about that lemma.
- **The two Latin texts of Gen 1:4 sort the bench almost perfectly, and this is a genuine finding
  rather than a curiosity.** The Greek keeps the Hebrew's doubled preposition (*ana meson … kai ana
  meson*) and the Old Latin follows it: *divisit inter lucem et tenebras*. Jerome writes *divisit
  lucem a tenebris*, an ablative of separation, which presupposes something to be separated from.
  Augustine, Angelomus and Alcuin quote the older form and hold that no darkness was made; Bede,
  Remigius, the Glossa and Comestor quote Jerome's and hold that both were made. Hugh and Rupert are
  the exceptions (Jerome's text, Augustine's doctrine), and Rupert quotes a third form with no
  preposition at all, *divisit lucem et tenebras*. Same shape as K1's *creavit* / *fecit*.
- **Sefaria's BR 3:6 is one segment carrying two arguments**, and K8 built it whole. See the K9
  entry in `notes/cross-crux.md`: `br-3-6b` was built rather than lose the crux's core text, and
  Phase 4 must trim K8's slice rather than delete the new one. **The general lesson for K3 and K2:
  before slicing a rabbinic passage, check whether an earlier crux took the whole segment for one
  clause of it** — `overlap.py` does this for Latin and nothing does it for the rabbinic bench.
  A `grep -l` of a distinctive phrase across `data/witnesses/*.json` is the cheap substitute and is
  what caught both of these.
- **The Glossa on this verse contradicts the Glossa on the previous verse**, and does not say so:
  113:69C prints the darkness of v. 2 as *veri luminis privatio*, and 113:71C prints *Lucem et
  tenebras fecit Deus* over Strabo's name for v. 4. The gloss's literal answer on K9 is Remigius'
  and is anti-Augustinian. Worth remembering when a later crux wants to know "what the schools
  taught": the standard book is not internally consistent verse to verse.
- **PdRE 3's Hebrew and English are differently indexed from what the section numbers suggest.**
  "Eight things were created on the first day" is index 5 in both versions (= PdRE 3:5); index 4 is
  the Torah's counsel. Check the segment content, not the section number.

**Burn, measured on K9 (Opus, 2026-09-05): ~110K tokens**, the cheapest of the seven, against K10
~170K, K1 ~200K, K8 ~170K, K6 ~135K, K5 ~125K, K4 ~unrecorded. Three reasons and only one of them
repeats. Every rabbinic locus was on disk and most had been read for K8 or K6 (BR 2, BR 3, Rashi,
PdRE, Ramban, Ibn Ezra), so the rabbinic side cost reading and no pulling. The Latin survey was two
`grep-bench.py` calls and one direct read of Alcuin. And the roster pruned itself: of 30 Latin
candidates, the ones that had to go were obvious (a second Rupert, a second Honorius, Hugh's cap.
XII, Bruno's one sentence), because K9's answers are few and sharply distinguished and a witness
either adds one or repeats one. **Contrast K10's note that deciding the roster was what took the
time**: on a crux with a small answer set it is not, and the answer set is knowable from the first
grep.

The roster ran to 32, well over the table's 12–15 — the fifth overrun in a row, and the table should
be read as a floor. 20 Latin witnesses is the real number for any verse the whole bench comments on.

## K3 `elohim-and-trinity` (built 2026-09-05)

**What the plan got wrong or did not know.**

- The plan's rabbinic list was "Megillah 9a; BR 1:7 [CHECK]; BR 1:12–13 [CHECK: heretics and
  *Elohim*]". **Both CHECKs resolve, and BR 1:7 is the crux's best rabbinic text** — R. Yitzḥak's
  three singular verbs against *shtei reshuyot*, two authorities. **BR 1:13 is not about heretics
  and Elohim**; it is R. Shimon ben Yoḥai on the wording of offerings and the Rabbis on the shape
  of a building, and it is not a K3 text. The heretic material the plan was reaching for is BR 8:8–9,
  on Gen 1:26, outside the scripture layer.
- **The plan did not know about Abelard, and Abelard is the crux.** *Hexaemeron* PL 178:739B–C is the
  only place on the Latin bench where the Hebrew word *Elohim* is brought to Gen 1:1: *El quippe
  singulare est … Eloim vero plurale est … Unde autem dictum est: Eloim creavit, non creaverunt?* It
  asks Bereshit Rabbah 1:7's question in Bereshit Rabbah's own terms and answers it for the Trinity.
  It was found by grepping abelard-hex alone for `Trinit|Spiritus sanct` after a bench-wide
  `Trinita(s|tis|tem|te)` grep had returned nothing for that work — **the bench-wide grep's work
  list is `latin-bench.json` order and it is easy to read a `— 0 hit(s)` line as a fact about the
  work when it is a fact about the regex.** Abelard's paragraph contains `Trinitatem` twice.
- **The anchor rule excludes most of this crux's Latin evidence, and that is itself the finding.**
  Nearly every Latin discussion of divine plurality is at Gen 1:26 (*Faciamus hominem*), and the only
  Latin note that *Elohim* is plural in number, outside Abelard, is Jerome's at **Gen 6:2** —
  copied verbatim by Rabanus at 107:511D. Both are outside the 1:1–5 layer. So the Latin bench had
  the philological fact for six hundred years, in its most-read commentary, and never carried it to
  the first verse. See notes/cross-crux.md for the register of what was excluded and why.
- **Three K3 passages had already been sliced whole by K7 and K1** — Augustine's *completa
  commemoratio Trinitatis* (*Gnl* I.6.12) inside `aug-gnl-1-5-11`, Ambrose's *operatio Trinitatis*
  inside `ambrose-hex-1-8-29`, Comestor's *in principio, id est in Filio* inside `comestor-hs-1-1`.
  All three were caught by `overlap.py` and none had to be rebuilt, because the first two were
  **pre-tagged with `elohim-and-trinity` by the K7 session**. That pre-tagging is the mechanism the
  project should use more: seven witnesses came onto this roster for free and three of them are
  load-bearing. **When a crux reads a passage that plainly belongs to an unbuilt crux, tag it then.**
- **The versiones column renders empty for the fourth crux running** (K5, K4, K9 partially, K3), and
  on K3 it costs real evidence: Megillah 9a is a claim about the Greek, and the targums replace
  *Elohim* with the Tetragrammaton. Phase 4 has the mechanical fix in cross-crux.md.
- **Sefaria's Ibn Ezra on Gen 1:1 is one long segment covering the whole verse**, so the *Elohim*
  paragraph is inside the same segment as the *bereshit* paragraph K1 sliced. `hcut` on the
  unvocalized Piotrkow text works with plain anchors — the skeleton match is only needed for
  vocalized texts — and the boundary was verified by reading K1's slice tail rather than by
  `overlap.py`, which covers Latin only.

**Burn, measured on K3 (Opus, 2026-09-05): ~85K tokens**, the cheapest of the eight, against K10
~170K, K1 ~200K, K8 ~170K, K6 ~135K, K5 ~125K, K9 ~110K. Two reasons, and both were predicted. The
seven pre-tagged witnesses meant a third of the roster needed no work at all. And the survey was
short *because the crux is small*: the anchor rule cut out Gen 1:26, which is where most of the
material is, so what remained was findable in three greps. **The roster came to 20 (13 new), the
first crux to land inside the table's estimate** (12–15 new), and it did so for a structural reason
rather than by pruning.

**A note for K2, the last one.** K2 `why-begin-here` is on Gen 1:1 with 34 K1 witnesses and now 13
K3 ones already on the verse, and its best single text — m. Chagigah 2:1, the ban on expounding what
is above, below, before and after — **is on disk, unbuilt, and is not a comment on the verse at
all**. K4's entry flagged this and it is still true: if the anchor rule is applied to K2 as strictly
as it was applied here, the crux loses its centre. That is a decision for Wilson, not for the
builder. The cheap options are (a) build it anyway with an explicit note, (b) leave it and say so in
the `finding`, (c) widen the anchor rule for texts that are *about* the act of expounding Genesis.
**Recommend (c), narrowly**: a witness may be anchored on a verse it does not quote if its subject
is whether that verse may be expounded — which is exactly what K2 is about, on both benches.

✅ **RULED 2026-09-05 (Wilson, Phase 6 session): (c), narrowly — adopted as written.** The rule is
now in `PHASES.md` under Frozen conventions. K2's four non-comment witnesses stand with their
`⚠ Anchor note`s; Gen 1:26 *Faciamus hominem* becomes admissible in K3. **The Gen 1:26 material has
not been built** — it was outside the scope Wilson set for this Phase 6 session and is the obvious
next addition to K3.

## K2 `why-begin-here` (built 2026-09-05 — Phase 2 complete)

**What the plan got wrong or did not know.**

- **The plan's PLAN.md §5 entry is the reason four witnesses on this daf are not comments on the
  verse.** It names "Glossa prothemata; Comestor prologue; Hugh Sacr. prologue", so prologues were
  contemplated for K2 before the anchor rule was frozen in PHASES.md, and the per-crux checklist's
  step 1 is to read that entry. K2 has built them and marked each with an `⚠ Anchor note`. **This is
  Wilson's ruling to confirm or reverse at Phase 3**, and the same licence would let Gen 1:26 into
  K3, where most of the Latin material on divine plurality actually is. If he reverses it the crux
  survives, because `br-1-10` carries m. Chagigah's four forbidden questions verbatim as an
  exegesis of the first *letter* of Gen 1:1.
- **PLAN.md's Tanchuma [CHECK] is unresolved**: `tanch-std-ber-1.json` and `tanch-buber-ber-1.json`
  are on disk and were not read for this crux. **The Glossa [CHECK] resolves negatively**: TEI 8950
  has no prefatory matter at all, opening straight at CAPUT PRIMUM, VERS. 1. If the Glossa's
  prothemata are wanted they are not in this transcription and are a Phase 6 job.
- **The plan did not name BR 1:2, which is Rashi's source.** R. Yehoshua of Sikhnin in the name of
  R. Levi has the whole of Rashi's answer — Ps 111:6, the charge of robbery, Deut 2:23, the earth is
  the Lord's — four hundred years earlier and without R. Isaac's objection. What Rashi contributes
  is the premise that makes it a question about the shape of Scripture rather than about the land.
- **Three slice defects, two of which fail silently.** `latin()` takes the FIRST match of its start
  anchor, and works with a printed table of contents print their chapter titles twice: the first
  build of `hugh-sacr-prologus` returned a 20,115-character witness spanning Hugh's whole table.
  **Use `occurrence=1` on any work with a table of contents** — this is a real defect in the helper
  and Phase 4 or 5 should make `latin()` warn when a slice exceeds, say, 5,000 characters. Second, a
  slice preceding the first `<pb>` in its TEI gets `col. ?`; Augustine's *De Genesi contra
  Manichaeos* CAPUT PRIMUM is one, and the column had to be supplied by hand. Third, Sefaria's
  English for m. Chagigah 2:1 is the **William Davidson Edition**, which is NC — the frozen data rule
  names Davidson/Steinsaltz for the Bavli and it applies to the Mishnah too, so the English there is
  a fresh draft from the Hebrew.

**Burn, measured on K2 (Opus, 2026-09-05): ~70K tokens.** Cheapest of the nine measured, and the
crux is also the smallest.

---

## Phase 2 closed — the whole run, measured

| crux | built | witnesses | threads | burn |
|---|---|---|---|---|
| K7 `ruach-hovering` | pilot | 30 | 33 | — (Fable pilot) |
| K10 `one-day-evening-first` | 1st | 28 | 34 | ~170K |
| K1 `beginning-of-what` | 2nd | 34 | 44 | ~200K |
| K8 `first-light` | 3rd | 27 | 35 | ~170K |
| K6 `tohu-vabohu` | 4th | 25 new / 32 on daf | 28 | ~135K |
| K5 `heaven-earth-order` | 5th | 17 new / 19 on daf | 20 | ~125K |
| K4 `ex-nihilo-or-matter` | 6th | 19 new / 22 on daf | 25 | — |
| K9 `good-and-separated` | 7th | 32 | 45 | ~110K |
| K3 `elohim-and-trinity` | 8th | 13 new / 20 on daf | 25 | ~85K |
| K2 `why-begin-here` | 9th | 10 | 15 | ~70K |
| **total** | | **235 witnesses** | **304 threads** | **~1.07M** |

**The cost curve is monotonic downward after K1 and the reasons are known**, so a future run of this
shape can be budgeted rather than guessed: (1) the rabbinic loci stop needing to be pulled and start
having been read — after K8 every locus any crux needed was on disk; (2) `grep-bench.py` turns
"which witnesses exist" from a reading problem into a search problem, provided the regex carries
**every Latin form of the lemma** (the K6 lesson) and provided a `— 0 hit(s)` line is read as a fact
about the regex and not about the work (the K3 lesson, which nearly cost the site its best witness);
(3) **pre-tagging** — seven witnesses arrived on K3's roster for free because the K7 session had put
`elohim-and-trinity` in their facets, and three were load-bearing. That last is the single most
transferable habit and it should be written into any comparable project's conventions from the
start: **when a crux reads a passage that plainly belongs to an unbuilt crux, add the facet then.**

**What did not get cheaper is the judgement**, and it moved rather than shrank. On the early cruxes
it went into pruning an over-large roster (K10's note: "what actually took the time was deciding the
roster"); on the late ones it went into boundary decisions — whether a passage another crux had
swallowed should be rebuilt (K9's `br-3-6b`: yes), whether a facet should be added to another crux's
witness (consistently: no, Phase 4), and whether the anchor rule should bend (K2: only on PLAN.md's
own authority, and flagged). **Those three questions are the whole of Phase 4's agenda** and they
are now itemised, by witness id, in `notes/cross-crux.md`.

## Phase 6 — second-tier sources (2026-09-05)

**What the plan got wrong or did not know.**

- **The plan's two "alternate fetch" jobs both fail on Sefaria, and for the same undocumented
  reason.** "Daat BR Hebrew" and "Etheridge Onkelos" are both listed on Sefaria's index for their
  works and both return **zero versions for the chapters this edition uses**. Daat Bereshit Rabbah
  has no text at Bereshit Rabbah 1, 2 or 3; Etheridge's Onkelos has none at Genesis 1 or Genesis 49
  but twenty segments at Genesis 12. **A version title appearing in `api/texts/versions/<work>` is
  a claim about the work, not about the passage** — always probe the actual ref. Etheridge was
  fetched instead from archive.org (`targumsonkelosa00ethegoog`, vol. 1, PD) into `raw/etheridge/`.
- **⚠ The BR Hebrew licence problem is NOT solved and is Wilson's to rule on.** Twenty-three
  witnesses carry `original.license: "check"` because the only Hebrew of Bereshit Rabbah 1–3 that
  Sefaria will serve is **"Midrash Rabbah -- TE"** (Torat Emet), licence *unknown*.

  ⛔ **"Unknown" is now worse than unknown.** The Torat Emet site itself
  (`toratemetfreeware.com`) prints **«כל הזכויות שמורות ©» — all rights reserved** — under a title
  that calls the project a free Torah database (מאגר תורני חופשי). A boilerplate reservation cannot
  create copyright in an 1878 Vilna text, but the *vocalization* is plausibly Torat Emet's own
  editorial work, and it is that vocalization which distinguishes their text from every free
  alternative. So the position is not "no licence stated" but "the source asserts rights".

  The free alternative is **"Wikisource Bereshit Rabbah", CC BY-SA** — same segment counts
  (15/5/9), same sections in the same order, and the same CC BY-SA family already pinned for the
  Bavli. It is unvocalized apart from scriptural quotations and prints the abbreviations
  (א"ר, רשב"י, הקב"ה) that Torat Emet expands.

  ⚠ **A first pass reported "only 4 of 23 slices survive a swap". That figure was wrong, and it was
  wrong in the way this project has been caught before — the matcher failed, not the text.** A
  consonantal-skeleton match still fails on abbreviation and on plene/defective spelling
  (מיחד/מייחד, ולחשך/ולחושך). Normalising the nine common abbreviations and dropping vav and yod as
  matres lectionis gives the real figure: **14 of 23 clean at both ends, 7 with one anchor holding,
  2 absent** (`br-1-2`, `br-3-4`). That is a few hours of re-cutting, not a rebuild.

  ⚠ **A second claim in that first pass was also wrong**: "BR 3:6 opens at תני אורה, without the
  וַיִּקְרָא lemma clause that is K9's evidence." What Wikisource lacks at the head of 3:6 is the
  question *לא הוא אור ולא הוא יום, אתמהא*, which is **not** K9's evidence. **K9's evidence is
  present**: R. Elazar's *לעולם אין הקדוש ברוך הוא מיחד שמו על הרעה אלא על הטובה*, with
  *ולחושך קרא אלהים לילה אין כתיב כאן*, is in the Wikisource segment, in different orthography.
  The genuine textual divergence found so far is **BR 3:5**, where Wikisource reads כנגד ספרי תורתו
  against Torat Emet's כנגד חמשה חומשי תורה. Any swap must diff every slice, not assume.
- **A `str.find` returning -1 had been used as a slice index since K10, and shipped.**
  `br-3-8`'s Hebrew was the single character `.` — the anchor failed on combining-mark order, the
  documented niqqud trap, and `text[-1:]` is the last character. It passed `check.py`, a daf read,
  and Phases 3, 4 and 5. Fixed; `bench.hcut` now takes `b=None` and `bench.ecut` is its non-Hebrew
  twin, both raising; `check.py` gained rule 7 (no original or English under 40 chars, no original
  under a quarter of its English). A sweep of all 235 witnesses at those thresholds returned br-3-8
  alone. ⭐ **The general lesson: every silent-truncation path in this repo is a `find` whose failure
  value is a legal index.** `_bon_slice` in the K10 spec has the same shape and degrades to the
  whole text rather than one character, which is why it was never noticed.
- **A CC BY compliance defect the colophon could not show.** Twenty-three Sefaria Midrash Rabbah
  passages and six Sefaria Vocalized Ramban passages were keyed to the generic `cc-by` — which is
  also the key on our own 177 fresh drafts and therefore carries no attribution line — while
  `colophon.astro` renders only `licenses[key].attribution`. CC BY requires attribution. Now keyed
  to `sefaria-midrash-rabbah` and a new `sefaria-vocalized`; `check.py` rule 8 enforces it.
  ⛔ **Put licence edits in the crux spec's `LICENSES`, not in `data/licenses.json`** — build-crux.py
  merges the spec over the file on every rebuild, and a first attempt at `chavel-ramban` was
  silently reverted that way. **`chavel-ramban` keeps its `[CHECK]`**: Phase 6 verified only that
  Sefaria's v3 API does assert CC-BY for that versionTitle, which was never the doubtful part.
- **Onkelos on Gen 1:5 was cited twice on the K10 daf and was not on it** — once by the
  Pseudo-Jonathan note and once by an answer gloss. Built as `targ-onk-1-5`. It reads *yoma chad*
  and then *yom tinyan* at 1:8, so it keeps the Greek's unevenness and adds one the Greek has not:
  the first is determined and the second is not. **And it corrects the K10 note on Etheridge**,
  which read as though his ordinal were a response to the expansive targum: his Onkelos prints "Day
  the First" for the same *yoma chad*, and "the Second Day" after it, so the ordinal is an even
  habit of the translator.
- ⛔ **The K10 bench greps missed the single most important patristic passage on the crux.**
  `basil-hex-2-8b` (PL 53:888A–B) gives both halves of "why evening first" — evening is named first
  *ut nativitatis diurnae privilegia reservaret*, because night accompanies the day and does not
  precede it, and before light was made there was no night in the world but only darkness — and then
  the argument from the choice of words, that Scripture said evening and morning and not day and
  night to give the dignity of the word to the better part. **Ambrose's answer on this daf is that
  sentence in other words**: "prerogative and birthright" is *privilegia* and *nativitas*, in that
  order, on the same clause. Ambrose is reading Basil's Greek, not this Latin — Eustathius
  translated a generation after the Hexaemeron of Milan — so the two are independent Latin
  renderings of one Greek sentence, and every later Latin answer descends from Ambrose's.
- **A variant that decides a doctrine, reported and not adjudicated.** Bonaventure (In II Sent.
  d.13 a.1 q.2) quotes that Basil sentence as *non **solaris** corporis motu*; the Patrologia column
  reads *non **solum** corporis motu*. The first has Basil deny that the first light moved as the
  sun does, which is the ground of Bonaventure's whole division of the question into Greeks and
  Latins; the second has him concede motion and merely add diffusion, and the division collapses.
  Basil's own context favours Quaracchi — the sentence has just distinguished what happens *after*
  the sun's creation from what happened *then*, when there was no solar body to move — and the same
  TEI column carries two plain OCR faults within six lines (*suipra* for *supra*, *et deo* for
  *ideo*). **Neither the Greek nor a second Latin witness was consulted, so this is left as a
  divergence.** Thread `t-k10-38` states it that way.
- **Bonaventure d.13 a.1 q.2 is the one witness that draws this site's own line from inside the
  tradition**: *duplex est hic modus dicendi, unus secundum doctores Graecos … alter secundum
  Latinos*, with both parties made to read the same two clauses — *Divisit Deus lucem a tenebris*
  and *factum est vespere et mane*, which are the whole of K9 and the whole of K10 — allotted
  between the schools sentence by sentence. Built as `bonaventure-sent-2-13-1-2`, on both dafs.
- ⚠ **`overlap.py` prints `!! could not locate glossa-1-2-ruach inside 8950` on every run.** That
  witness was filled from `raw/latin/glossa-8950-gen-1-2-*.md` rather than sliced from the TEI, so
  it is absent from the coverage map and the Glossa's 1:2 column is invisible to overlap checking.
  Not fixed here; it is a hole in a safety net, not a defect in the data.
- **`grep-bench.py` and `latin()` compute the PL column identically** — a disagreement between them
  on one passage turned out to be two different offsets in one passage, not two computations.
  The cited column is always the one containing the *start anchor*, so two witnesses sharing a
  column is expected, not a fault.

**Still unbuilt from Phase 6's list**: Nicholas of Lyra and Paul of Burgos (1492 Venice *Biblia cum
glossa*, vision OCR — its own session, ~150–200K), and Gen 1:26 *Faciamus hominem* into K3, which
the widened anchor rule now permits and which is where most of the Latin material on divine
plurality actually sits.

### Origen/Rufinus, Hom. in Gen. I.1 — built, and it raises a question about K1's finding

Built as `origen-hom-gen-1-1` (K1, pre-tagged for K6). Source **GCS 29, ed. Baehrens, Leipzig 1920,
p. 1** — PD in the US (1920) and in the EU (Baehrens d. 1929). ⛔ **This is the only Latin on the
site not sliced from the local TEI bench**, because Origen in Rufinus is PG 12 and the harvest is PL
only; `~/patrologia/sources/pg` holds 34 volumes and PG 12 is not among them. The archive.org item's
own djvu OCR of this page is badly degraded (*prineipium, feeit, dieit, ineomposita, aquase*) and was
**not** used; the Latin was transcribed from the page image (item `origenes-werke.-bd-6-1920`,
**leaf n37 = printed p. 1**, calibrated from `_scandata.xml`).

The paragraph is the head of the stream — *Non ergo hic temporale aliquod principium dicit, sed in
principio, id est in Salvatore* — and two things in it cut against how the later bench reads it.
Origen reaches the Son by **John 1:1–3 and Col 1:15**, with no Ps 104:24 and no *sapientia* anywhere
in the sentence; Ambrose reaches him by **John 8:25**, which makes *Principium* a name, and it is
Ambrose's route the Latin bench takes. And Origen runs straight on into 1:2, reading *invisibilis et
incomposita* as a statement of what was so *before* the light — a chronology, not a metaphysics.

**And Jerome, refuting the reading, names his opponents and Origen is not among them**: the
*Altercation of Jason and Papiscus*, Tertullian *Adv. Praxean*, Hilary on a Psalm. He could not have
been refuting *this text* — Rufinus's Latin is a decade later than the *Quaestiones*. More to the
point, **he refutes a claim Origen never made** (that the *Hebrew* has "in the Son") and then concedes
the claim Origen did make: *potest tamen de Christo intelligi secundum sensum magis quam secundum
verbi translationem*. That sentence is Rupert's "in sense, not in speech" of c. 1115, verbatim in
substance, six hundred years earlier — and K1's finding currently presents Rupert's formula as his
own recovery. Threads `t-k1-45` and `t-k1-46`.

⚠ **ESCALATED, NOT DECIDED — this may qualify K1's headline finding, and revising a finding is not a
builder's call.** K1 says the two benches gloss *bereshit* as "in wisdom" and mean opposite things,
"with no contact either way". Baehrens's apparatus to this very page carries two notices that bear on
the "no contact" half:

1. A **Catena notice under Akakios's name**: *ὁ δὲ Ὠριγένης τὸ »ἐν ἀρχῇ« βούλεται ἀντὶ τοῦ ἐν σοφίᾳ,
   τουτέστι τῷ υἱῷ* — Origen takes *en archē* as *en sophia*, that is, in the Son. So the Greek
   behind the Latin bench **did** put wisdom and the Son together at Gen 1:1, and the Latin homily
   as Rufinus gives it does not.
2. **Chalcidius, *Comm. in Tim.* 276**: *Origenes adseverat ita sibi **ab Hebraeis** esse persuasum
   … initium minime temporarium dici … est tamen unum … initium de quo **Salomon** … inquit …
   aperte indicans praeeunte divina sapientia caelum terramque facta.* A fourth-century Latin report
   that Origen got the non-temporal *initium* **from the Hebrews**, and grounded it on **Solomon** —
   Prov 8:22, which is the rabbinic bench's own verse for reaching wisdom.

**What this does and does not show.** It does not show the Latin bench receiving anything: Chalcidius
is a report about Origen, not a channel into Wigbod or the Glossa, and the Catena is Greek. What it
does show is that "no contact either way" is a claim about the *Latin* transmission and is false of
its head — a sharper finding than the one K1 printed, not a weaker one.

✅ **RESOLVED 2026-09-05 (Wilson: verify both, then amend). Chalcidius verified; the Catena is not,
and is not used.**

Chalcidius was read independently of Baehrens, in the 1617 Meursius edition
(`ita-bnc-mag-00000929-001`, printed p. 570), and the passage is **fuller than the apparatus's
ellipses suggested**. In full it runs: *Sed Origenes asseverat ita sibi ab Hebraeis esse persuasum…
Initium minime temporarium dici. Neque enim ullum tempus fuisse ante mundi exornationem… Est tamen
unum rerum omnium initium, de quo Salomo in proverbiis: «Creavit me (inquit) Deus progressionis suae
primitiam, cui nitens efficeret opera divina; constituitque ante mundi ortum…» Aperte indicans,
praeeunte divina sapientia caelum terramque factam, eandemque sapientiam divinam esse universitatis
primordium.* So Chalcidius does not merely allude to Solomon — **he quotes Prov 8:22 at length and
concludes to Wisdom, not to the Son.**

**The decisive check was run on the built bench, not asserted**: across all 240 witnesses,
**Prov 8:22 is cited by four and every one is rabbinic** (`br-1-1`, `br-1-4`, `br-1-8`,
`rashi-1-1b`); **Ps 104:24 by four and every one is Latin** (`ambrose-hex-1-3`, `aug-civ-11-32`,
`bruno-gen-1-1c`, `rupert-gen-1-1`); Prov 3:19 by two, both rabbinic. The disjunction is total.
K1's `finding` is amended accordingly: the contact existed at the head and the Latin transmission
lost it.

⛔ **Chalcidius is NOT built as a witness, and should be.** The only free text is uncorrected OCR of
a 1617 print whose page images carry a ProQuest copyright notice, and the volume's leaf-to-page
calibration does not hold, so the page could not be read the way Origen's was. This edition does not
embed Latin it cannot check against a clean page. He is a **fourth-century Latin witness on Gen
1:1–2 who is not in the PL and not on the bench** — he even preserves a Genesis 1:2 variant,
*terra autem stupida quadam erat admiratione* — and he wants Waszink's *Plato Latinus* (Corpus
Platonicum Medii Aevi). That is the single highest-value item left on the second-tier list.

⚠ **The Catena notice remains unverified** and is deliberately absent from the amended finding. If
it holds, it says something stronger still — that Origen himself glossed *ἐν ἀρχῇ* as *ἐν σοφίᾳ,
τουτέστι τῷ υἱῷ*, joining the two benches' words in one phrase — but it is a notice in catena
manuscripts under Akakios's name, reported at third hand here, and nothing is being built on it.

### The Bereshit Rabbah Hebrew swap — done 2026-09-05 (Wilson's ruling)

Moved off Torat Emet onto **"Wikisource Bereshit Rabbah", CC BY-SA**. All 23 BR witnesses now carry
a licence; `raw/sefaria/br-{1,2,3}-he.json` (the Torat Emet pulls) are deleted and
`pull-sefaria.py` is repinned with a warning at the top. The only witnesses still on `check` are the
two Neofiti ones, which are a separate question.

**What it actually cost, measured rather than estimated.** Every one of the 23 slices was diffed
against its Torat Emet text at word level, after normalising abbreviations and matres lectionis.
Similarity: **two identical** (`br-1-7`, `br-3-8-yanai`), **eighteen above 0.90**, and three below —
`br-3-4` (0.833), `br-3-6b` (0.869, and that one is the deliberate split described below),
`br-1-8` (0.875). No witness lost its argument. The differences fall into three kinds:

1. **Abbreviation style**, the largest share: Wikisource prints א"ר, א"ל, הה"ד, בהמ"ק where Torat
   Emet expands them.
2. **Scripture-citation format**, and this one is a genuine small loss to the reader: Torat Emet
   quotes proof texts more fully and supplies chapter-and-verse references that Wikisource
   abbreviates to וגו' or drops (Prov 8:21–22 at `br-1-8`, Deut 2:23 at `br-1-2`).
3. **A handful of real variants**: בזוזים / בזויים at `br-1-2`; לאמרה מקמי כן / ממרינה מקומיכן at
   `br-3-4`, where Wikisource also carries more of Ezek 43:2 and lacks Torat Emet's ברבים לא היה.

⛔ **The recension difference that forced an editorial change.** In Torat Emet, BR 3:6 runs: the
question *לא הוא אור ולא הוא יום*, then the stored light, then the va-yavdel block, and R. Elazar on
the withheld divine name **last**. Wikisource has no opening question at all, and puts **R. Elazar
second**, before the va-yavdel block. Two consequences, both handled:

- `br-3-6` (K8) is cut to what the two recensions share. Its English no longer opens at the lemma —
  Sefaria's English still translates the Torat Emet opening ("are 'light' and 'day' not the same
  thing? This is bewildering"), which the Wikisource Hebrew does not have, so the English is cut to
  match the Hebrew rather than left with an untranslated head. **The Hebrew and the English of this
  edition's BR witnesses now come from different recensions**, and where they disagree the pair is
  trimmed to the overlap. That is worth saying in the colophon.
- `br-3-6b` (K9) could not survive as one span, because its old cut runs from R. Ze'eira to
  R. Elazar and in Wikisource R. Elazar comes first. ⭐ **This forced a correction the frozen rule
  already required**: that card carried two arguments on two clauses. R. Elazar on the withheld
  divine name is now **`br-3-6c`**, and the two threads that were always about him — `t-k9-01`, the
  star thread of the crux, with Augustine's *Civ.* XI.20, and `t-k9-24` with Hugh on naming — point
  there. K9's headline finding is about that argument, and it now has a witness of its own instead
  of being the seventh tradent on somebody else's card.

**Tooling.** `bench.hcut` gained an orthography-tolerant fallback, used only when the exact
consonantal match fails and required to match **uniquely** or it refuses: abbreviations expanded,
vav and yod dropped as matres lectionis. ⚠ It equates רב and ר'/רבי, which are different titles —
harmless for locating an anchor, since the stored text is always the source text as it stands, but
not to be used for comparing readings. A first version expanded abbreviations character by
character and so expanded none of them; the offset map has to be built over the whole string.

**Every remaining silent-truncation path is closed.** `br-2-4` and `targ-neof-1-1` were still using
bare `find` results as slice indices, and `_bon_slice` in the K10 spec fell back to returning the
whole text on a failed anchor. All three raise now. Nothing in `cruxes/` uses an unguarded find.

---

# Phase 6 part three — Gen 1:26 *Faciamus hominem* into K3 (2026-09-05)

**26 witnesses added, 36 threads. Roster 240 → 266 witnesses, 329 → 366 threads, site 371 → 403
pages.** `check.py` clean, `npm run build` clean, `astro check` 0 errors, Pagefind indexed 403
pages. Every witness anchored on `gen.1.2` under the **second clause** of the anchor rule, each
with a visible ⚠ Anchor note; `data/scripture/gen-1.json` untouched, so the edition's scope is
still Gen 1:1–5 and there is no `/dialogue/gen-1-26/` page.

## ⚠ ESCALATED, NOT DECIDED: K3's finding is now false, and in both directions

K3's `finding` says three benches reach three incompatible conclusions from one grammatical fact,
"nobody is answering anybody", and that three of the four could not have read each other. On the
Gen 1:1 evidence that was right. On the Gen 1:26 evidence it is wrong, and the amendment is not a
builder's call. **The case, and a drafted replacement paragraph, are at the end of this section.**

## The roster, and what was pruned

`grep-bench.py "Faciamus hominem"` gave 107 hits across 23 works; `notes/k3-gen-1-26-survey.md`
narrowed that to 46 candidates; **15 Latin/Greek witnesses were built.** What was left out, and
why, because the pruning is the judgement and should be inspectable:

- **Rabanus** (PL 107:459C) and **Angelomus** (PL 115:145A) copy Bede verbatim and add nothing.
  Named in `bede-gen-1-26`'s notes instead of built.
- **Rupert's** other thirty hits are on the image and on predestination. The one that touches
  plurality, PL 167:315A on *unus ex nobis* at Gen 3:22, is material Bede, Alcuin and Rabanus all
  carry. The Rupert that was built is **PL 167:247B**, which the seeding list did not flag and
  which is the best Latin witness on the daf: see below.
- **Augustine, *Confessions* XIII** (PL 32:858) makes the plural/singular alternation an allegory
  of the renewed spiritual man, not an argument about God.
- The large majority of the 107 raw hits are on *ad imaginem*, a different question entirely.
- **Bruno** came back **COVERED** by `bruno-gen-1-1c`, built for this crux at Phase 2. So the
  Latin bench's Gen 1:26 material was already on this daf, inside a Gen 1:1 witness, unlabelled —
  which is itself a small argument that the anchor rule's second clause was describing something
  the data had already done.

**Rabbinic: 11 witnesses.** BR 8:3, 8:8, 8:9; b. Sanhedrin 38b twice; Rashi twice; Ibn Ezra;
Ramban; Onkelos; Pseudo-Jonathan. **BR 17 was not used** (secondary, and says nothing 8 does not).
**Targum Neofiti was not used**: its licence is the same open question as the two existing Neofiti
witnesses, and this was not the session to settle it.

## The seeding list missed the best Latin witness on the daf

`rupert-gen-1-26-consilium` (PL 167:247B) is **not in the 46**. The filter required two of
{plural, numer, persona, Trinit, Iudae, angel, singulari} within 700 characters, and Rupert's
sentence — *Mutavit vocem suam … non tam senatu quam soliloquio venerando* — contains **none of
them**. It was found by reading the context of a candidate that did match, three columns away.

That is the transferable lesson and it generalises past this crux: **a signal-word filter finds
the witnesses that argue in the vocabulary you already have, and misses the one that says the
thing in its own words.** The reason Rupert matters is exactly that he does not use the school's
terms — *senatus* and *soliloquium* are the two poles of Bereshit Rabbah 8:3's disagreement
(R. Yehoshua's king with two *sanqlitin*, Greek *synklētikoi*, against R. Ami's *be-libbo nimlakh*),
and no filter built out of Trinitarian vocabulary could have caught them.

## `overlap.py` had a silent gap, now fixed

`overlap.py` builds its coverage map by locating each Latin witness's first 60 characters in the
TEI. A witness whose `text` was **assembled** — several glosses concatenated, an editorial bracket
spliced in — has no 60-character verbatim prefix, so it was dropped from the map with a note on
**stderr**, and every candidate sitting inside it would then have been reported **FREE**.
`glossa-1-2-ruach` is such a witness and had been invisible to the guard since K4.

Fixed: shorter prefixes are tried (60, 40, 24), the failure notice moved to **stdout** where the
answer is being read and reworded to say the FREE verdicts in that work are not trustworthy, and a
witness matched only on a short prefix has its coverage claimed only as far as the prefix actually
matched, so coverage is never asserted beyond the evidence. No candidate in this session was
affected — all seven Glossa witnesses end by col. 72A and both candidates were at 80B and 114D —
but the class was live.

## What the plan and the brief got wrong

1. **Sanhedrin 38b has no free English.** "Sefaria Community Translation" is listed for the *work*
   and returns nothing for *this daf*; En Jacob (Glick 1916, PD) returns nothing either; Davidson
   is CC BY-NC and barred. Both Sanhedrin witnesses carry fresh drafts. This is the third time the
   rule has paid: **a version title in `api/texts/versions/<work>` is a claim about the work, not
   the passage.**
2. **Onkelos Gen 1:26 has no free English either** — only Metsudah, CC BY-NC. Fresh draft, as at
   `targ-onk-1-5`.
3. **The brief's BR 8 warning was right and is now permanent policy**: Wikisource does not cover
   BR ch. 8, Daat does; Daat is the version that returned nothing for chapters 1–3. The BR Hebrew
   on this site therefore comes from **two versions by chapter**, and that now has its own licence
   key, `daat-br`, so the colophon says so in its own entry rather than silently under `pd`.
4. **The brief's estimate was right for once.** ~60–100K was forecast; the survey being done in
   advance is what did it. The roster ran to 26 against no stated estimate; the pattern of
   overruns is unbroken but this time nobody had written a number to overrun.

## The evidence that K3's finding has to change

**K3's finding, as it stands, rests on Gen 1:1 alone, and Gen 1:1 is the verse where the two
benches happen not to touch.** Move one verse over and the same two benches are demonstrably in
contact — in three distinct ways, of which only the first is the obvious one.

**(a) Named, mutual contact.** Basil, in the Latin every western reader used, reports the rabbinic
answer accurately and by name: *ferunt enim, quod angelis dixerit: Faciamus hominem* — and it is
what Targum Pseudo-Jonathan actually prints in the biblical line. He then refutes it with
*Fecit Deus hominem: non fecerunt*, which is R. Simlai's own proof at BR 8:9 turned around. On the
other side, BR 8:8 has Moses stop while writing the verse — *why are you giving the minim an
opening?* — and BR 8:9 has the minim ask R. Simlai how many divinities created the world and cite
Gen 1:1 and Gen 1:26 in one breath. Both benches know what the other does with these verses and
say so.

**(b) A pairing neither bench could have got from the other.** R. Yoḥanan at b. Sanhedrin 38b
lists the plural verses with the singular refutations beside them, and the first two are Gen 1:26
answered by 1:27 and Gen 11:7 answered by 11:5. Augustine's *De civitate Dei* XVI.6, headed *de
locutione qua Deus Angelis loquitur*, takes up the same two verses in the same order and applies
the same test, refusing the angels at Gen 1:26 because of the image clause and granting them at
Gen 11:7 because nothing forbids it. The Glossa Ordinaria at PL 113:114D joins the same two verses
and answers both with their singulars. Three benches select the same pair out of the Pentateuch by
the same criterion and test it the same way, with no contact whatever. That is not influence; it
is the Hebrew text imposing the same structure on everyone who reads it carefully, which is a
stronger finding than "no contact" and a different one from "contact".

**(c) The same figures of speech, independently.** Rupert's *non tam senatu quam soliloquio* is
BR 8:3's two extremes, the king with his *sanqlitin* against *be-libbo nimlakh*, decided the other
way. Abelard's man who consults his own reason and so makes two of himself, with Boethius and the
*Soliloquies* named, is R. Ami's answer with a bibliography. Remigius's *quasi quodam concilio* is
*be-mi nimlakh* in one word. Hugh's moral — do not disdain to take counsel from equals and from
lesser people, since God himself so speaks to the angels — is BR 8:8's moral exactly, and he grants
the angels a possible ministry in forming the body, which is further than any rabbinic witness here
goes. Rashi's *pamalya shel ma'alah* is the Latin *familia*; the court is the same borrowed picture
on both benches.

**And one correction to the daf's own account of a witness.** K3 has Ibn Ezra as the man who takes
the plural noun to be an empty honorific. At Gen 1:26 Saadia Gaon offers him the identical
explanation for the plural verb and he destroys it — *ve-elleh ha-edim edei sheker hem*, these
witnesses are false witnesses — parses away every proof text, and puts a real hearer in their
place: God said **to the angels**, let us make a human. The two positions are compatible (a plural
of honour is a fact about nouns; *na'aseh* has a subject), but a reader with only the Gen 1:1 page
would have Ibn Ezra's answer to this crux exactly backwards. That is now `t-k3-54`.

## ⚠ Proposed amendment to K3's `finding` — for Wilson, not executed

The existing finding is unchanged in `data/cruxes.json`. What is proposed is to **keep both
existing paragraphs as they stand** — they are accurate about Gen 1:1 — and to **replace the third
and last paragraph**, the one that ends with Bruno of Segni refusing the plurality "in the rabbinic
bench's own words", with this:

> At Gen 1:1 nobody is answering anybody. One verse over, at *Faciamus hominem*, they are, and the
> daf now carries the evidence. Basil reports the rabbinic reading by name — *ferunt enim, quod
> angelis dixerit: Faciamus hominem* — and it is what Targum Pseudo-Jonathan prints in the
> biblical line itself; he refutes it with *Fecit Deus hominem: non fecerunt*, which is R. Simlai's
> own proof at Bereshit Rabbah 8:9 turned around. Bereshit Rabbah 8:8 has Moses stop while writing
> the verse to ask why God is giving the *minim* an opening, and is told to write it and let
> whoever wants to err, err. So on this verse each bench knows what the other does with the words
> and says so, which is not true of the first verse at all. The deeper contact is the one neither
> side could have arranged. R. Yoḥanan at b. Sanhedrin 38b lists the plural verses with their
> singular refutations beside them, and the first two are Gen 1:26 answered by Gen 1:27 and Gen
> 11:7 answered by Gen 11:5; Augustine's *De civitate Dei* XVI.6, in a chapter headed *de locutione
> qua Deus Angelis loquitur*, takes the same two verses in the same order and applies the same
> test, refusing the angels at the first because of the image clause and granting them at the
> second because nothing forbids it; and the Glossa Ordinaria joins the same pair at PL 113:114D.
> Three benches choose the same two verses out of the Pentateuch by the same criterion and test
> them the same way, and none of them has read another. The pairing is not borrowed. It is what
> the Hebrew does to anyone who reads it carefully, and the disagreement that remains is only
> about what the plural was doing there — a court of angels, a plurality of persons, the earth
> beside its maker, or nothing at all.

**Three smaller consequences follow if the amendment is taken, and none of them is executed
either.** (1) K1's finding says something similar about "no contact either way" and was already
queried at Phase 6 part one over Chalcidius; it should be looked at in the same sitting. (2) The
crux `summary` still frames the question as one about the word *Elohim*; on the present roster the
crux is about plural speech about God, of which the noun is one case and the verb another. (3)
The answer `elohim-is-honorific-plural` reads as Ibn Ezra's whole position and, after `t-k3-54`,
is only half of it.

## Ruling executed, 2026-09-05 — and the K1 review that came with it

**Wilson said go.** Three things done, one thing reviewed and found not to need doing, one small
thing newly escalated.

**Done.**
1. **K3's `finding` amended.** The drafted paragraph is in, as a fourth paragraph rather than as a
   replacement for the third. ⚠ **This is a deviation from what was approved and it is flagged
   here because the drafting error was mine.** The proposal said "replace the third and last
   paragraph"; what it did not say is that the third paragraph carries the Megillah 9a material —
   the seventy-two elders moving the divine name and turning *na'aseh* singular for Ptolemy —
   which nothing else on the daf states. Deleting it would have been a silent loss Wilson was not
   told he was approving. The three existing paragraphs are accurate about Gen 1:1 and stand; the
   new one opens by naming exactly what changes ("At Gen 1:1 nobody is answering anybody. One
   verse over, at *Faciamus hominem*, they are"). **Say the word and the third paragraph goes.**
2. **The crux `summary` replaced.** It had read "Megillah 9a is a Jewish witness to a Greek
   interpretive move that reaches the Latin bench through the Vetus Latina" — true, and no longer
   the headline. It now reads: "One question asked of two different plurals — the noun *Elohim* at
   Gen 1:1 and the verb *na'aseh* at Gen 1:26 — and the second is where the two benches turn out to
   be arguing with each other rather than past each other." ⚠ **Correction to what was escalated:**
   the item said the crux's `question` still framed this as being about the word *Elohim*. It does
   not — the `question` already read "what do grammar and word order say about plurality?" and was
   general enough. Only the `summary` needed the change.
3. **`elohim-is-honorific-plural` re-glossed** to say that the honorific plural is Ibn Ezra's
   account of the **noun**, and to point at `plural-of-majesty-refused` for what he does to the
   same reading of the **verb**.

**Reviewed, and it needs nothing.** K1's finding does not say "no contact either way" and has not
said it since Phase 6 part one: the Chalcidius amendment is already in it, and the sentence that
carries the claim is already hedged — "Neither side knows the other is there … which is what the
Latin bench looks like from the inside, **and is not the whole truth**" — before the amendment
corrects it outright. The phrase I remembered is from the PHASES.md escalation note, not from the
finding. Nothing in the Gen 1:26 block contradicts K1: its claim is about *bereshit / in principio*
specifically, that both benches reach "in wisdom" from different proof texts, and the Prov 8:22 /
Ps 104:24 split that proves it is untouched.

## ⚠ Newly escalated, one paragraph, not executed — an addition to K1

The Gen 1:26 block **strengthens** K1's finding by documenting its mechanism a second time, in a
different century and through a different text, and K1 does not know it yet. K1 says the contact
existed at the head of the tradition and the Latin transmission lost it: Chalcidius has Origen
persuaded *ab Hebraeis*, quoting the rabbinic bench's own verse, and nothing downstream carries it.
That is one channel. Basil is a second, and it fails the same way. Eustathius's Latin *Hexaemeron*
— which is how the entire Latin west read Basil — carries an **accurate report of the rabbinic
reading of Gen 1:26**, *ferunt enim, quod angelis dixerit: Faciamus hominem*, which is what Targum
Pseudo-Jonathan prints. Bede copies the passage at Jarrow, keeps the sentence about the preaching
of the Godhead lying hidden in the deep word for word, and **removes every Jew in it**, replacing
the polemic with a *ratio*; Rabanus copies Bede at Fulda and Angelomus at Luxeuil, and by the
Glossa the reading survives only at Gen 11:7, unattributed. So the same thing happens twice: a
fourth-century Latin text reports what the other bench actually says, and the copying tradition
keeps the argument and drops the knowledge that there was anyone to argue with.

**Proposed, as one added sentence at the end of K1's finding — yes or no:**

> The same loss happens a second time and in the other direction. Basil's Latin *Hexaemeron*
> carries an accurate report of the rabbinic reading of Gen 1:26 — *ferunt enim, quod angelis
> dixerit: Faciamus hominem*, which is what Targum Pseudo-Jonathan prints in the biblical line —
> and Bede copies the passage at Jarrow keeping every sentence of the argument and removing every
> Jew in it, Rabanus and Angelomus copy Bede, and by the twelfth century the reading survives in
> the Gloss only at Babel and with nobody's name on it. Twice, then, and by two unrelated routes,
> the Latin bench was handed the other bench's words and kept only the answer.

## Three rulings, 2026-09-06 — all executed

1. **K1's finding takes the Basil sentence.** ⚠ Placed **beside the Chalcidius loss-case, not at
   the literal end** as the proposal said. The finding closes on the JPS Tanakh removing the crux,
   which is the right last beat; a second loss-case buried after it would be wasted. It now sits
   immediately after "never met the text that had already got there from the other side", which is
   the sentence it doubles.
2. **Targum Neofiti ships as public domain**, with the reasoning on the page under a new licence
   key `neofiti-vatican`. **This clears the last `check` in the data** — the two Neofiti witnesses
   were the only ones left. The reasoning is the shop's own, applied to someone else's
   transcription rather than to ours: a faithful transcription of a public-domain text creates no
   new copyright, and Sefaria's "unknown" is a metadata gap, not an assertion. The note records the
   limit — it covers the text and not the Vatican's page images, which this edition does not
   reproduce — and says the two witnesses come down if anyone asserts a right.
3. **Push to a public GitHub repo — approved in principle, and the exact commands are surfaced for
   a per-action OK** before anything runs. Nothing has been pushed.

## Two stale things found while answering, both fixed

- **PHASES.md's Phase 7 still asked a question Wilson answered the same day.** It said to confirm
  whether the site takes the Wroot Press CC BY-NC licence. It does not, and the ruling was already
  recorded on the `cc-by` key in `data/licenses.json`: **the edition is CC BY 4.0, a deliberate
  departure from house policy**, because BY-NC cannot legally sit on top of the inbound CC BY-SA
  Hebrew (Wikisource Bavli, Miqra according to the Masorah). The Press rule is unchanged for every
  other corpus; this edition is the documented exception and the colophon must say so. That key's
  own passage count was stale too (177 → 197).
- **K1's finding was the only one in the edition carrying markdown markers**, and they rendered as
  literal asterisks on the live page — `*ab Hebraeis*`, `**The contact existed…**`. Seven of them,
  in one string. Stripped, keeping the words; every witness note and every other finding is plain
  prose, so K1 was the outlier and the renderer is not at fault. **Worth knowing as a class:** the
  `finding` and `notes` fields are plain text end to end, and nothing on the pipeline strips or
  interprets emphasis, so a marker written into either one ships to the reader as an asterisk.

---

# Phase 6 part four — Chalcidius on Genesis 1:1–2 (2026-09-06)

**Five witnesses, twenty-one threads, across four cruxes, from two leaves.** Roster 266 → 271
witnesses, 366 → 387 threads, site 403 → 413 pages. `check.py` clean, `npm run build` clean,
`astro check` 0 errors.

## The blocker was about the wrong book

Phase 6 part one recorded Chalcidius as "the single highest-value item left" and unbuildable
without **Waszink's *Plato Latinus***, on the ground that the only free text was uncorrected OCR of
a 1617 Meursius print whose page images carry a ProQuest notice, and that this edition does not
embed Latin it cannot check against a clean page. **Both halves of that were true and the
conclusion was wrong**, because only one free edition had been looked for.

**archive.org `bub_gb_LxGcsxR3tWgC`** — Josse Bade (Badius Ascensius), **Paris 1520**, 148 leaves,
Bayerische Staatsbibliothek via Google, **no rights notice of any kind**, roman type, printed folio
numbers on every recto. It was found with three `archive.org/advancedsearch` queries; the one that
worked was `creator:Chalcidius`, after title and editor searches returned nothing. The generalisable
part: **a "needs the critical edition" verdict should be re-tested against a creator search before
it is written down**, because an early print of a text with no manuscript problem is often good
enough for an edition that quotes rather than collates.

Calibration was confirmed by reading images, not estimated: `page/n115.jpg` = **fo. LVII verso**
(running head *Chalcidij Interpretatio*), `page/n116.jpg` = **fo. LVIII recto** (*In Timeū
Platonis. Fo. LVIII*, signature *h ii*). Leaf ≈ 2 × folio holds.

## ⭐ Two leaves, four cruxes, and most of it was not in the plan

The item was escalated for one sentence — Origen persuaded *ab Hebraeis* — which K1's finding
already used. What the leaves actually carry is much more:

| | crux |
|---|---|
| *Hebraei syluam generatam esse confitentur* — a fourth-century Latin reporting the rabbinic answer to this crux **and attributing it to the Hebrews** | **K4** |
| **Gen 1:1–2 printed four times**: LXX, Aquila, Symmachus, and the exemplar Origen credits to the Hebrews | **K1, K6** |
| Aquila's *caput rerum condidit Deus coelum et terram* — reshit as **head**, i.e. Ibn Ezra's construct reading, in Latin, in the fourth century | **K1** |
| Symmachus's *otiosum quid confusumque et inordinatum* — **the *alia translatio* the Carolingians cite without knowing whose it is**, here named and glossed word by word | **K6** |
| *terra autem stupida quadam erat admiratione* — tohu as astonishment, which is Bereshit Rabbah 2:2's *tohe u-bohe* and Rashi's word, **given a psychological gloss on the Latin page** | **K6** |
| Prov 8:22 at length; *sapientiam diuinam esse uniuersitatis primordium*; Wisdom made by God but not in time — **and he stops, without naming the Son** | **K1** |
| *initium minime temporarium dici*, plus a lexical survey of what *initium* can mean in ordinary scriptural Latin | **K1** |
| the heaven of v. 1 cannot be the firmament of day two nor the earth the dry of day three, so both are older and intelligible; **Philo by name**, who is nowhere else in this edition | **K5** |
| *sylua* as the plain sense of *inuisibilis et informis*; the receptacle argument stated flat — the receiver of all qualities has none of its own | **K6, K4** |

## What this does to the picture, and what it does not

**It does not overturn K1's finding; it is the finding's own evidence, now on the page.** K1 already
said the contact existed at the head of the tradition and the Latin transmission lost it. Three
things sharpen it.

1. **Chalcidius stops where every later Latin goes on.** He has the rabbinic bench's verse
   (Prov 8:22), reaches the rabbinic bench's word (*primordium*, which is *reshit*), and does not
   say the Son. Jerome, Ambrose, Augustine, Bede, Alcuin, the Gloss all take the step he declines.
   So the divergence is not a matter of which verse each bench happened to have — Chalcidius had
   the right verse and the right conclusion, in Latin, before any of them.
2. **The Latin bench's lost philology is quantifiable now.** Angelomus in the ninth century knows
   only that *another translation says: unseen and unordered*. Chalcidius in the fourth names
   Symmachus, quotes him, and explains both of his words. The apparatus does not develop across
   those five centuries; it is lost, and the same is true of Aquila.
3. **`chalcidius-hebraei-versiones` is the earliest accurate Latin report of a rabbinic position in
   the whole edition** — earlier than Jerome's *Hebrew Questions*, earlier than Basil's report of
   the angel reading, and unlike both of them it is not polemical. He states what the Hebrews hold
   about hyle in order to agree with it.

## Two stale claims corrected, both mine to have caught earlier

- **`origen-hom-gen-1-1`'s note said Chalcidius "is not built as a witness … He needs Waszink's
  Plato Latinus."** He is built and he does not. Rewritten to say what the blocker actually was.
- **K1's finding quoted Prov 8:22 as *creavit me Deus progressionis suae primitiam***, taken from
  Baehrens's apparatus to Origen. **The 1520 print the witness is built on reads *semitam*.** The
  finding now quotes its own witness and records the variant in parentheses. ⚠ **Worth generalising:
  a finding that quotes a text the edition does not yet hold as a witness is quoting a secondary
  apparatus, and will disagree with the witness the day it is built.**

## Still not verified, and still deliberately unused

The **Catena notice** — that Origen glossed ἐν ἀρχῇ as ἐν σοφίᾳ, τουτέστι τῷ υἱῷ — remains a
third-hand report in Baehrens under Akakios's name. Nothing is built on it. If it holds, it would
close the gap this section has just widened: it would put the Son and Wisdom together in Origen's
own words, and make Chalcidius's restraint the departure rather than the norm.

---

# Phase 6 part five — Philo of Alexandria, *De opificio mundi* (2026-09-06)

**282 witnesses, 427 threads, 424 pages, all checks clean.** Eleven witnesses across **nine of the
ten cruxes**, forty threads. The `greek-jewish` bench, which had held only the five LXX verses since
Phase 2, now has a voice: the LXX is a translation, and until today nothing in the edition defended
the equation of "the Jewish reading" with "the rabbinic reading". `chalcidius-caelum-et-terra`'s
note no longer has to say that Philo "does not appear anywhere else in this edition"; **t-k5-p1 is
the citation edge from Chalcidius to `philo-opif-29`, the one place in the project where a Latin
witness names a Jewish author and the passage he names is printed beside him.**

⚠ **Deviation from the brief, and it is upward.** The brief forecast five cruxes with K8 as a
possible sixth. The build landed on nine: K1, K2, K4, K5, K6, K7, K8, K9, K10 — everything but K3
(`elohim-and-trinity`), where Philo has nothing on the divine plurality of Gen 1:1. Three of the
four unforecast placements are as strong as the forecast ones and none is a stretch: §1–3 answers
K2's question outright and in its own terms; §30 asks K7's question as a question about privilege
(why is the breath alone called God's?) and answers it from what breath does; §33–34 answers K9's
question with a war and a demilitarised zone, and names the borders evening and morning, which is
also what it contributes to K10. §29 went to K5 rather than being folded into another witness
because it is the passage Chalcidius is reporting.

## ⛔ The finding of the session, and it is not about Philo

**The daf renderer had been dropping every witness that was not `latin` or `rabbinic`, silently.**
The columns in `site/src/pages/crux/[id].astro` are built by predicate, and the predicates covered
those two traditions, the Vulgate/LXX pair and the Glossa. Anything else was built, passed every
`check.py` rule, was listed on the crux roster, got its own `/witnesses/` page — and never appeared
on the daf. It survived there only inside the JavaScript thread data, so the wires pointed at notes
that were not on the page.

That hid **Philo's eleven witnesses the moment they were built**, and it had been hiding **Basil's
three Greek witnesses since Phase 5** — `basil-hex-2-6b`, `basil-hex-2-8`, `basil-hex-1-26-judaei`,
one of which is K9's Greek head. `check.py` cannot see this class: it checks the data, and the data
was correct. Fixed, and the fix is small because the design had anticipated the bench and only the
bucketing never landed — `--grk` and `.sn.greek-jewish` were already in `daf.css`. Basil goes with
the Fathers (his witnesses are tagged `greek` only because the slice is of his Greek rather than of
Eustathius's Latin); Philo gets his own block at the head of the left column.

⭐ **New standing check: `scripts/daf-coverage.py`**, run after `npm run build`. Every witness on a
built crux's roster must be a rendered note on that crux's daf and on its verse's dialogue page.
It was negative-tested by stripping the new block out of a copy of `dist` — it fails, naming the
three witnesses and their tradition, so its green light means something.

## The loader, and two things the survey did not know

`bench.greek()` slices Cohn's text by printed section number; `bench.yonge()` loads the aligned 1854
English for checking a draft and is never embedded. The trap the brief named is real and is fixed in
the loader rather than in a crux spec: **60 of the 172 sections carry the apparatus criticus inside
the section div as `<note type="footnote">`**, so a naive tag-strip welds manuscript sigla into the
middle of Philo's Greek in Greek script. Notes are dropped before any other flattening; verified
that no `<pb>` ever falls inside a `<note>`, so no page break is lost with them. Two further things:

- ⛔ **A single stray `|` survives in the whole file**, an OCR artifact left where a marginal Mangey
  page reference fell — and it falls inside §26, one of this session's slices. One occurrence in
  310 KB. Stripped in the loader.
- ⛔ **§24 is corrupt in the TEI**: `ἤδη [νοητὴν]ν [[νοητὴν]ητὴν]. πόλιν κτίζειν διανοουμένου`. It is
  the section that says outright that the intelligible world is nothing other than the Reason of God
  already creating, so it is the one a careless build would most want. It is **not sliced**; §20 says
  the same thing in words that are sound, and the corruption is recorded in
  `philo-opif-17-20`'s note.

## English

Drafted fresh from the Greek, **`DRAFT`**, not approved. Yonge is public domain and aligned and is
deliberately not embedded: he gives *νοητός* as "perceptible only by the intellect" and paraphrases.
Register additions, extending the frozen list rather than reopening it: *νοητὸς κόσμος* = "the
intelligible world", *αἰσθητὸς κόσμος* = "the perceptible world" (never "world of ideas");
*λόγος* = "Reason" where it is God's and "word" where it is speech; *ἀρχή* = "beginning", with
*κατὰ χρόνον* / *κατ’ ἀριθμόν* = "according to time" / "according to number"; *μόνωσις* =
"solitariness" and *μοναδικός* = "monadic", never "unity"; *δημιουργός* = "craftsman";
*στερέωμα* = "firmament"; *ἄποιος* = "without quality", *ἄτακτος* = "without order";
*ἰδέα* = "idea"; *παράδειγμα* = "model".

⚠ **One rendering is new and is flagged rather than assumed**: *τεχνίτης* = **"artificer"**. The
frozen list already spends "craftsman" on *artifex/faber* and *δημιουργός*, "workman" on *opifex*
and "worker" on *operator*, and §20 puts *τεχνίτης* and *δημιουργός* in the same paragraph about the
same man, so collapsing them would lose the distinction Philo is drawing. Overturnable on a word.

## ⚠ Three findings, written not executed — yes or no to each

Findings are Wilson's. Each of these is an addition, not a replacement, and each is reversible.

### 1. K1 (`beginning-of-what`) — a third loss, running the other way

K1's finding says the contact existed at the head of the tradition and the Latin transmission lost
it, and documents that twice: Chalcidius on Origen *ab Hebraeis*, and Basil's Latin *Hexaemeron*
copied by Bede with every Jew removed. Philo is a third case and it inverts the direction.

> A third loss, and it runs the other way. Philo of Alexandria read these verses in Greek four
> centuries before Bereshit Rabbah and told the same parable: a king founds a city, a trained
> architect draws the whole of it within himself first and carries an intelligible city in his
> soul, and only then builds in stone; so God conceived the types, made an intelligible world out
> of them, and used it as the model for this one. The midrash's amon, the craftsman's plan the King
> builds from, is that parable with the Torah put in the architect's hand. Nobody need have
> borrowed anything for that to matter; what matters is who kept him. The rabbinic bench does not
> cite Philo once and did not preserve him. He survives because the church copied him, and he was
> recovered for Judaism only in the sixteenth century, by Azariah dei Rossi. So the mechanism this
> finding has twice described in one direction runs in the other as well: the Latin bench lost the
> philology it had been handed, and the rabbinic bench lost the one Jewish reader of Genesis 1
> whose reading of this verse its own commentary most resembles. Nor did the Latins who preserved
> him know what they had. Chalcidius names him and was read by nobody; Ambrose's Hexaemeron follows
> his De opificio closely and rarely says so.

### 2. K10 (`one-day-evening-first`) — the head of both halves of the meeting

K10's finding says the two benches meet on the grammar (Bereshit Rabbah 3:9's objection to the
series, answered by Bruno's logic of relatives) and part on the calendar. Both halves have a head,
and the head supplies a third reading the finding does not currently name.

> Both halves of that meeting have a head, and it is the same man. Philo of Alexandria, writing in
> Greek before either bench existed, gives the grammatical argument first: Moses does not even call
> it first, so that it should not be counted in along with the others. That is Bruno's logic of
> relatives a thousand years early and Bereshit Rabbah 3:9's objection to the series eleven hundred
> years early. And he gives a reason neither bench states — day not first but one, because of the
> monosis of the intelligible world, its solitariness, which has a monadic nature. Monosis is not
> unity and it is not primacy; it is the condition of having nothing beside you, which is exactly
> what Rashi means by yachid be-olamo, that God was alone in his world that day because there was
> not yet a second anything to count with. Three benches read the cardinal as a claim about being
> alone rather than about position in a series, and the oldest of the three is the one neither of
> the others knew it had.

### 3. K2 (`why-begin-here`) — an older answer, Jewish, and on neither bench

K2's finding stages Rashi against Hugh: two traditions' reasons for having a commentary, the same
shape and opposite in content. Philo asks the same question from the same premise a thousand years
before Rashi and answers it in a third way.

> There is an older answer than either, and it belongs to neither bench. Philo opens De opificio
> with this crux's exact objection, that this is a book of laws and does not open like one, and
> answers that the opening is the law's credential: the cosmogony is there so that the world shall
> be shown to agree with the law and the law with the world, and so that the man who keeps the law
> shall be a citizen of the cosmos, directing his conduct by the nature that governs the world
> itself. Rashi's answer secures a title to a particular land and Hugh's concedes that the chapter
> is not what his own book is for. Philo's is jurisprudential, and it is the only answer on this
> daf that makes Genesis 1 do work for the legislation that follows it. His framing does survive on
> the Latin bench, with the philosophy taken out: other lawgivers wrote either bare statutes or
> myths, and Moses did neither, is Augustine's "not with ornate and polished speech but with plain
> facts".

**Not affected, checked:** K4's "three benches, one analogy, no contact" stands — Philo does not use
the craftsman-and-material analogy in §21–22, and his architect is at K1. K5, K6, K7, K8 and K9 are
strengthened by their new witnesses and contradicted by none of them.

## ⚠ Also for Wilson, and it is a framing question, not a finding

The index and the colophon describe this edition as **two benches**. It now prints sixteen
`greek-jewish` witnesses — the five LXX verses and Philo's eleven — and Philo argues, which the
Seventy do not. The daf shows him in his own block at the head of the left column, under his own
name, in the `--grk` colour the stylesheet already had. **Nothing has been changed in the index or
the colophon.** The question is whether the edition should stop calling itself two benches, and it
is worth answering now that there is a page to look at rather than in the abstract.

## Method, worth carrying

1. ⭐ **A green check is only worth what its negative test is worth.** `daf-coverage.py` was written
   against a bug that had already shipped once, so it was run against a doctored copy of `dist`
   before being trusted. A checker that has never been seen to fail is a claim, not a control.
2. ⛔ **A defect in the last stage of a pipeline is invisible to every check on the earlier ones.**
   Eleven witnesses were correct in the data, correct in the roster, correct on their own pages, and
   absent from the only page anyone reads. The class is not "the renderer is buggy"; it is "nothing
   was checking that the data reaches the ink".
3. **A brief's roster is a floor.** The survey found five cruxes because it filtered on the cruxes
   it expected; reading the sections in sequence found four more, and three of those four are
   witnesses the daf would be poorer without. The estimate held anyway (~95K against 90–130K),
   because the discovery was inside a text already identified.

---

# Phase 6 part six — Nicholas of Lyra and Paul of Burgos (2026-09-06)

**285 witnesses, 436 threads, 431 pages, all gates clean.** Three witnesses, nine threads, from two
leaves of the Koberger folio. Deliberately fewer than the brief's roster, and the reason is below.

⭐ **`burgos-add-3` is the text this edition exists to print.** Paul of Burgos — Solomon ha-Levi of
Burgos, a rabbi until he was forty, baptised in 1390, afterwards bishop of Burgos — arguing in a
printed Latin Bible about how much of the literal sense the Latin bench owes to Rashi, and arguing
that it owes less than Lyra says:

> tercio quia expositionis litteralis auctoritatem, quam nostri doctores primo invenerunt,
> **Ra. Sa. hebreo attribuit**

An early reader of this copy underlined *Ra. Sa. hebreo* in ink. Burgos then produces the Latin
doctors he says found it first — Rabanus, quoted at length on the unclean binary, and Peter Lombard
on the *sacramentum* of the number two — so the page carries the evidence for its own claim.
⚠ Anchored on `gen.1.4` under the **second clause** of the anchor rule, with a visible anchor note:
Burgos is arguing about the day-two absence of *Et vidit Deus quod esset bonum*, which is Gen 1:8
and outside scope, but the question he is arguing is the one Gen 1:4 raises and K9 is built on.

**The other two.** `lyra-gen-1-1` is the end of a line this crux has been tracing since Jerome: the
Glossa's first word on Gen 1:1 is *Filio*, and Lyra's *Postilla litteralis*, printed in the same
Bibles and often on the same opening, gives *in principio, scilicet temporis vel productionis
rerum* and never mentions the Son. `lyra-gen-1-2-tohu` gives *inanis* and *vacua* two different
physical causes and derives the darkness of v. 2 from an etymology, *a-byssus*, without whiteness.

## ⛔ The navigation traps, and they cost most of the session

**The brief's leaf calibration was wrong, and so was every method available for fixing it.**

1. **The brief's own leaves are off.** It has `n57` = Burgos's *Additiones* on Genesis 1 and `n61` ≈
   Gen 1:11–19. In fact **Gen 1:1–3 with the Postilla is on `n43`** (the rubric *Incipit liber
   Genesis qui dicitur hebraice Bresith* and the illuminated I are there), Gen 1:4–10 on `n44`,
   Burgos's Additio iij on `n57`, and `n61` is **Matthias Doering's *Correctorium corruptorii
   Burgensis***, which the brief does not mention is printed here at all.
2. ⛔ **`Lyra_djvu.txt` has no page separators**, so it cannot locate anything.
3. ⛔⛔ **`Lyra_hocr_pageindex.json.gz` locates text by leaf, and its leaves are offset from the
   image leaves by an amount that DRIFTS.** Calibrated at 3 near Genesis 1 and at 6 by folio 30. A
   single calibration therefore *validates* and then silently hands you the wrong leaf twenty pages
   later — which it did, twice, before the drift was caught. Note also that the same Additio is
   printed twice in this book, once in Burgos's block and again inside Doering's reply, so a
   duplicate hit is not evidence of a bad offset.
4. ⭐ **The fix, and it generalises past this book: archive.org's search-inside endpoint returns the
   leaf index in the same numbering `page/nN.jpg` uses, plus a pixel box and the page dimensions
   the OCR ran against.** One request gives both the leaf and where on it to crop.
   `https://ia600507.us.archive.org/fulltext/inside.php?item_id=<id>&doc=<doc>&path=<dir>&q=<query>`;
   `server`, `dir` and the file stem come from `https://archive.org/metadata/<id>`. Wrapped as
   `scratchpad/lyra/find.py`. This should be the first thing tried on any archive.org item in this
   shop, ahead of djvu text and ahead of hOCR offsets.

## ⛔ The trap that could have put fabricated Latin on the page

**A crop that straddles two columns reads as continuous prose.** This folio sets two columns with a
narrow gutter; a crop taken on a guessed x-range picked up the right half of column 1 and the left
half of column 2, and the result *scans* — Latin clauses running on plausibly across the splice.
Nothing about the image says the line is spliced. It was caught only because the sense went wrong
two lines later.

**How to not do it:** establish the column edges from a whole-page overview *before* cropping, keep
every crop inside one column, and treat any crop whose left or right edge cuts words as unreadable
rather than reconstructing the missing halves. Three slices in this session were shortened rather
than completed for exactly this reason — `lyra-gen-1-2-tohu` stops at *quia color candidus habet
plurimum de luce* because the next clause is cut, and what follows it is described in the notes
instead of quoted. That is the [[feedback_vision-ocr-discipline]] rule applied to geometry rather
than to letters: an unreadable half-word is not an invitation to supply the obvious word.

## What is still on the leaves, and it is a lot

Not built, all located, all worth a second session at ~60–80K now that navigation is solved:

| what | leaf | crux |
|---|---|---|
| Lyra's lemma **h**, *Et spiritus … aquas*, the will of the artificer over the matter | n43 | **K7** |
| Lyra's lemma **i** onward, *Dixitque Deus*, the beginning of the work of distinction | n43 | **K8** |
| Lyra on *vidit lucem quod esset bona*, *divisit*, *dies unus* | n44 | **K9, K10** |
| Burgos's **Additio i and ij** on the literal exposition of the chapter, *valde difficilis* | n48–n51 | **K1, K4** |
| ⭐ Burgos's **Additio ix** — *sicut inter christianos fuerunt aliqui heretici, ut Arriani, Nestoriani … sic inter iudeos fuerunt aliqui habentes erroneas opiniones que non approbantur a iudeis communiter*, written against Lyra's claim that the Jews fell into the error of the Saracens | n60 | ⚠ anchor unclear — it answers a passage of the Postilla on ch. 1 but not evidently on 1:1–5. **Check the Postilla passage it quotes before building.** |
| Doering's reply to Additio iij: *primam dicit truphaticam, secundam abicit tanquam non fundatam, terciam approbat a Ra. Sa. acceptam; in quo passu dicit eum in tribus deviare a rectitudine* | n61 | **K9** — completes the three-cornered quarrel |

⚠ **The substitution stands and is on the page.** PLAN.md named the 1492 Venice *Biblia cum glossa*;
this is Koberger, Nuremberg 1486–87, and every `source` and the licence key `lyra-koberger-1487`
say so. Someone should confirm the substitution before these ship.

## Phase 6 part six, second sitting — the quarrel gets its third corner (2026-09-06)

**289 witnesses, 446 threads, 435 pages, all gates clean.** Four more witnesses from the Koberger
folio, on the six targets the rewritten brief listed. Navigation cost nothing this time: the
search-inside locator and the recorded column edges did what they were meant to, and the whole
sitting went on reading rather than on finding.

⭐⭐ **K9 now carries all three corners of the only quarrel in this edition that is *about* the
rabbinic bench rather than merely parallel to it**, printed a hundred leaves apart in one book and
now on one daf:

1. **`lyra-gen-1-4-bonum`** (leaf n44) — the page Burgos indicts, and every charge checks out.
   Lyra calls the answer of Rabanus and Peter Lombard *truphatica* in that word; he refutes them
   from Luke 10 and Gregory on the pair; and he prefers Rashi: *Ideo aliter respondet Ra. Sa., et
   magis secundum intentionem littere ut videtur.* An early reader underlined *Ra. Sa.* in ink here
   too. ⚠ What Burgos does not mention: Lyra rejects **two** Latin answers, and the second — that
   the angels fell on the second day — he refutes on strictly Latin grounds, that it has no
   scriptural authority and leaves too long between the angels' creation and their fall.
2. **`burgos-add-3`** (n57, built in the first sitting) — the indictment.
3. **`doering-repl-3`** (n61) — and this is the one that says the quiet part. Matthias Doering,
   restating Burgos's third charge in order to answer it, does not write what Burgos wrote. Burgos
   wrote *Ra. Sa. hebreo*. Doering writes:

   > tercio quia **veram** responsionem attribuit **infideli**, que tamen in nostra glosa continetur,
   > cui potius debuit honorem exhibere

   *Verus* is Doering's own word: he does not dispute that the answer is true. He disputes whose it
   is, and what honour is owed. And his defence of Lyra on the first charge names the real subject
   — Lyra was not scoffing at the holy doctors *sed imperitis lectoribus, qui id pro sensu litterali
   eligunt quod sancti mystice … adducunt*, at unskilled readers who take for the literal sense what
   the saints adduced mystically. **The fight is about what the literal sense is for**, conducted by
   three Latins over the head of a Jew three hundred years dead whom all three have read.

All three are anchored on `gen.1.4` under the anchor rule's second clause with visible notes: the
passage argued about is the day-two absence of the formula, Gen 1:8, out of scope, but the question
is the one Gen 1:4 raises.

**Also built.** `lyra-gen-1-2-spiritus` (K7) — the craftsman's will at the end of its life, reduced
to a gloss, *spiritus Dei, id est voluntas*, with Augustine's *sicut voluntas artificis* reproduced
almost word for word and unattributed seven centuries on. `lyra-gen-1-5` (K10) — Bede's twenty-four
hours with the mechanism finally supplied: evening ends the artificial day, the next morning ends
the night, and the verse names the two joints of the natural day rather than reporting two events.

## ⚠ A fourth finding put to Wilson — K9, yes or no

K9's finding is about two benches reading the same silence with no contact, and about the
metaphysical question the Latin bench cannot get past and the rabbinic bench never asks. Nothing in
it is falsified. What the new witnesses add is an ending it does not have.

> There is one place where the silence stops being a coincidence, and it is four hundred years after
> the last witness above. Nicholas of Lyra, asking why the second day has no approval, calls the
> answer of Rabanus and of the Master a piece of trifling, refutes a second Latin answer from the
> Scriptures, and then takes the reading he wants from Rashi — more according to the intention of
> the letter, as it seems. Paul of Burgos, who had been a rabbi in that city until he was forty and
> was afterwards its bishop, replies that the postillator departs from rectitude in three ways, and
> the third is that he attributes to Ra. Sa. the Hebrew the authority of a literal exposition which
> our own doctors found first. Matthias Doering, defending Lyra, restates the charge and changes one
> word: he attributes the true answer to an unbeliever, though it is contained in our own gloss, to
> which he ought rather to have shown the honour. Nobody in that exchange denies that the answer is
> right. What they are arguing about is whose it is, what is owed for it, and whether the literal
> sense is the place where a Christian may be taught by a Jew. Every other page of this edition
> shows two traditions reading the same verses without knowing the other is in the room; this one
> shows what it sounds like when they do.

**Not affected, checked:** K7 and K10 are extended by their new witnesses and contradicted by none.

## Method

⭐ **The locator paid for itself in one sitting.** The first sitting spent most of its budget finding
leaves and built three witnesses; the second, with the same budget shape, built four and did no
searching at all. What made the difference was writing the leaf/box locator down
(`scripts/archive-find.py`) and writing the **column edges** down in the brief — n43 right column
x 0.655–1.00, n57 column 1 x 0.335–0.680, n44 columns 0.065–0.44 and 0.455–0.84, n61 column 2
x 0.660–1.00. A brief that records geometry is worth more than one that records page numbers.

⛔ **A continuous slice must actually be continuous.** `lyra-gen-1-4-bonum` was two legible crops
with a 0.09-of-a-page gap between them, and the two ends joined up plausibly. They were not spliced:
the gap was transcribed in two more crops before the witness was written. A join that reads well
across an untranscribed gap is the same failure as a join across a column gutter, and it is harder
to see because nothing is visibly cut.
