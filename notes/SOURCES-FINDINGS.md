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
