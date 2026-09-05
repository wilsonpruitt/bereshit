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
