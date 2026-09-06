# Cross-crux notes — for the Phase 4 pass

Edges and facets noticed while building one crux that belong to another. Nothing here has been
acted on; Phase 4 merges it. Do not revise another crux's threads to fit an entry in this file.

## From K10 (built 2026-09-05)

**Ben Zoma appears on both K7 and K10, and it is the same kind of move both times.** In K7
(b. Chagigah 15a) he reads *merahefet* as a measured physical fact — three fingerbreadths between
the upper and lower waters. In K10 (b. Chullin 83a) he reads *yom echad* as a rule about
reckoning — the day follows the night. Both times he takes a word the tradition reads figuratively
and makes it yield a measurement. Worth an edge between `b-chag-15a` and `b-chull-83a`, and
probably a line in the K7 *finding* as well as K10's.

**Witnesses now carrying a crux whose roster does not yet exist** (check.py exempts register-only
cruxes from the reverse-direction roster check, so these are silent until those cruxes are built):

| witness | also claims | note |
|---|---|---|
| `aug-gnl-1-5-11` (K7) | `elohim-and-trinity` | the elided middle chapter finds the Trinity in 1:2 |
| `glossa-1-2-ruach` (K7) | `elohim-and-trinity`, `tohu-vabohu` | four glosses, three cruxes |
| `b-chag-12a` (K10) | `heaven-earth-order` | segments 15–19 are Shammai/Hillel — that is K5's core text, already on disk |
| `aug-gnl-4-22` (K10) | `first-light` | the angelic light of day one is K8's subject |
| `aug-gnl-5-18` (K10) | `ex-nihilo-or-matter` | *creavit omnia simul* bears on K4 |
| `bonaventure-sent-2-12-1-2` (K10) | `ex-nihilo-or-matter` | d.12 q.2 is about matter's actuality; K4 will want the whole quaestio |

**K8 (`first-light`) already has most of its rabbinic material on disk and read.** BR 3:6 (the
hidden light stored for the righteous), b. Chagigah 12a segments 7–11 (R. Elazar's light; R. Yaakov
vs the sages on whether the lights were made day one and hung day four), and Rashi on 1:4 (which
cites Chagigah 12a by name and then gives a *peshat* alternative from BR 3:6). Building K8 should
be cheaper than the table assumes.

**K5 (`heaven-earth-order`) likewise**: b. Chagigah 12a segments 15–19 carry the whole
Shammai/Hillel dispute, the sages' *"this and that were created at once"*, Resh Lakish's
reconciliation, and R. Yishmael's question to R. Akiva about the particles *et*.

**Tanchuma Bereshit 1:7** (Resh Lakish on why *ha-shishi*, the sixth day, takes the definite
article) is the same grammatical question family as K10 but anchored at Gen 1:31, outside the
1:1–5 scripture layer. It cannot be a witness under the present anchor rule. If the scripture
layer is ever widened, it belongs with K10.

## From K1 (built 2026-09-05)

**Two Neofiti witnesses now sit on this crux.** K7 built `targ-neof-1-2` (the ruach clause) and gave
it the `beginning-of-what` facet, because Sefaria returns the whole of Gen 1:1–5 as one segment and
the "with wisdom" is in the same block. K1 has built `targ-neof-1-1`, sliced at the same verse it is
about. Phase 4 should drop `beginning-of-what` from `targ-neof-1-2`'s facets; K1 did not touch it.

**Witness-id collision, and it is a builder defect as much as a naming one.** `rabanus-gen-1-1`
(K7) is a witness on **Gen 1:2**; K1's Rabanus on 1:1 is therefore `rabanus-gen-1-1b`. See the
pipeline note in `SOURCES-FINDINGS.md`: `build-crux.py` would have overwritten the K7 file without
a word. Phase 4 should either rename K7's witness or add the guard.

**Material read for K1 that belongs to another crux, all of it already on disk:**

| locus | belongs to | note |
|---|---|---|
| Bereshit Rabbah 1:5–1:7 | K2 `why-begin-here` | "may they be silenced" — the ban on expounding what is before the world; and R. Yitzḥak on "the beginning of your word is truth" |
| Bereshit Rabbah 1:10 | K2 | why the world was created with a *bet*: closed on three sides, so do not ask what is before |
| Bereshit Rabbah 1:12 | K3 `elohim-and-trinity` | R. Yudan in the name of Akilas: the King acts first and names himself after — *bereshit bara*, and only then *Elohim* |
| Bereshit Rabbah 1:9 | K4 `ex-nihilo-or-matter` | the philosopher to Rabban Gamliel; the plan already lists it, and it is the exact counterpart of Remigius' Plato and Aristotle |
| Bereshit Rabbah 1:14 | K5 `heaven-earth-order` | R. Yishmael and R. Akiva on the two *et* particles |
| Bereshit Rabbah 1:15 | K5 | Beit Shammai and Beit Hillel in full, with R. Yehuda bar Ilai and R. Ḥanin |
| Ramban on 1:1, second movement | K4 | the *hyle* paragraph follows immediately in the same Sefaria segment; anchors `הקב"ה בָּרָא כָּל הַנִּבְרָאִים מֵאֲפִיסָה מֻחְלֶטֶת` → the *bohu* etymology |
| Rupert, PL 167:202B (continuation) | K4 | *"non, ut philosophi gentilium vane putaverunt, sibi coaevam habuit hylen"* — sliced into the K1 witness's tail already, but the argument runs on |
| Comestor, PL 198:1055D–1056A | K4 | Plato, Aristotle and Epicurus set against Moses, immediately before the sentence K1 slices |
| Hugh, *De sacramentis* PL 176:247B | K4 or K8 | the contradiction between "wisdom was made first of all" and "in the beginning God created heaven and earth", set up as a *quaestio* |
| Bruno, PL 164:157B | K3 | *"Habes ergo Deum, id est Patrem; habes et principium, id est Filium"*, on *Faciamus hominem* |
| Augustine, *Conf.* XIII.5 (PL 32:847) | K3 | the Trinity read out of the first words: *"in Principio sapientiae nostrae … id est in Filio tuo, fecisti coelum et terram"* |
| Glossa on 1:1, Bede's second and third glosses | K4, K5 | the empyrean heaven and the *materia informis* / Wis 11:17 gloss are in the same VERS. 1 block K1 slices whole |
| Isidore, PL 83:209B (continuation) | K7, K8 | the same ecclesial allegory runs straight on into 1:2 and 1:3 |
| Honorius, PL 172:260B | K10 | *"Quid vero beatus Augustinus sentiat de his diebus"* — a third treatment in TEI 10991, and further evidence for K10's open **[CHECK the work division at PL 172:261]** |

**A thread K1 could not draw.** `hugh-sacr-1-1` ("in the beginning of time, or rather with time
itself") and K10's `b-chag-12a` (the measure of the day and the measure of the night are among the
ten things made on day one) are the same answer on the two benches — time is inside the creature,
not outside it. The Bavli witness belongs to K10 and K5, so no K1-tagged thread was written to it.

**Both benches use a chapter of Proverbs as Genesis 1:1's commentary, and neither knows it.**
Proverbs 8 is the rabbinic bench's proof text throughout K1 (BR 1:1, 1:4, 1:8; Rashi). On the Latin
bench Prov 8:22's *ἔκτισέν με / Dominus creavit me* is the Arian battleground, and the Latin
witnesses on this crux therefore avoid it and reach for **Ps 104:24** instead. That avoidance is
worth stating in the Phase 8 introduction; it is not a single-witness observation and no thread
carries it.

## From K8 (built 2026-09-05)

**The strongest cross-crux fact on the site so far, and it cannot be a thread.** Augustine's answer
to K8 is that the first light is the angelic creation, made on day one. The rabbinic bench is
debarred from that answer by rulings it makes in two other places: **BR 1:3** (all agree that none
of the angels were created on the first day, lest anyone say Michael or Gabriel helped) and **BR 3:8**,
which is K10's built witness (nothing whatever was created on the first day besides God, so that no
partner in creation can be alleged). Neither of those is a witness on K8, and neither is about the
light. Phase 4 should decide whether the graph can carry an edge of this kind — a doctrine settled
at one crux that forecloses an answer at another — or whether it belongs only to the Phase 8 prose.
It is stated in K8's `finding` for now.

**Material read for K8 that belongs elsewhere, all on disk:**

| locus | belongs to | note |
|---|---|---|
| BR 3:2 | K8, unbuilt | *vayhi* and not *vehaya*: the light came about at once. Fits the `fiat-is-instantaneous` family but is about the verb, not the light |
| BR 3:5 | none yet | light named five times for the five books of the Torah — a structural derashah with no counterpart on the Latin bench |
| BR 3:6, second half | K9 `good-and-separated` | R. Ze'eira on the havdala blessing, derived from *va-yavdel*; and "he set it aside for himself" |
| Rashi on 1:4, peshat half | K9 | "not seemly that light and darkness should function in confusion" is K9's answer, in the same dibbur K8 slices |
| Augustine, *Gnm* I.4 (PL 34:176) | K9 | darkness is not a thing but the absence of light — silence, nakedness, emptiness |
| Augustine, *Gnl* I.9–10 (PL 34:254) | K10 | the circuit of that light and how it made evening, which is K10's question asked of K8's light |
| Rabanus (107:467A), Remigius (131:56A) | K9 or a moral layer | the same allegory on both: *fiat lux* = the light of faith, the first commandment, the division of the sons of light from sinners |
| Isidore (83:209B, continuation) | K7, K8 | *Dixit quoque Deus: Fiat lux, id est illuminatio credulitatis appareat* — the ecclesial allegory reaches this verse too; not built for K8, which took the literal question |
| Bonaventure II Sent. d.13 a.1 q.2, a.2 q.1–2 | K9, or a light-physics crux | "in what manner that light made day and night"; "whether light is a body or the form of a body"; "whether light is a substantial or an accidental form" — Rupert's substance/accident argument is exactly what a.2 q.2 disputes |
| PdRE 3, seg. 5 | K5 `heaven-earth-order` | eight things created on the first day, against Chagigah's ten |
| Hugh, *De sacr.* I.1 caps. X–XII | K9, K10 | "that visible and invisible light were made at once and alike divided from the darkness"; "that the light illumined three days, and why it was made before the sun" |

**Two K10 witnesses now appear on the K8 daf without K8 threads** — `aug-gnl-4-22` and
`alcuin-int-34` carry `first-light` in their own facets. See the Phase 4 note in
`SOURCES-FINDINGS.md`.

## From K6 (built 2026-09-05)

**`br-2-4` (K7) is half a K6 witness.** Resh Lakish reads the whole verse as the four kingdoms:
*tohu* is Babylon (Jer 4:23), *va-vohu* is Media, the darkness is Greece, the deep is Edom — and
only then does the spirit become the Messiah's, which is why K7 built it. The first half is the
same move as BR 2:3's generations and Bruno of Segni's Church, both of which are on K6's daf, and
the thread `bruno-gen-1-2-tohu → br-2-4` was not written because a crux's threads should join
witnesses on its own roster. Phase 4: add `tohu-vabohu` to `br-2-4`'s cruxes facet and write the
edge.

**`glossa-1-2-ruach` carries the Strabo gloss on *inanis et vacua* inside a witness whose lemma is
the Spirit clause.** Wilson's edition chunk appended it, K7 built it, and K6 threads to it
(`t-k6-10`, `t-k6-11`) rather than duplicating the text. Phase 4 should decide whether that gloss
becomes its own witness on the K6 lemma — and if it does, `glossa-1-2-terra` (the Bede gloss, built
here with a draft English) should be merged with it into one Glossa witness per lemma block.

**The third gloss on Gen 1:2 in the Glossa** — Bede again, on *tenebrae erant*, ending *"Ipsa autem
terra et aqua informis dicuntur materia, quia omnia quae videmus vel ex istis sumpserunt exordium,
vel ex nihilo"* (PL 113:69D–70A) — is **K4's**, and is the Glossa's only statement of *materia
informis* on this verse. Not sliced.

| left for | crux | note |
|---|---|---|
| Basil/Eustathius, PL 53:880C | K4 | the paragraph after K6's slice: against those who read *invisibilis et incomposita* as proof of an unbegotten matter coeval with God — the Greek bench's answer to BR 1:9's philosopher |
| b. Chagigah 12a, segments 4–5 | K5 | Rav Yehudah in Rav's name, the ten things created on day one, with *tohu va-vohu* among them; the list is K5's core text and is on disk, read |
| Ramban on 1:1, first movement | K4 | creation from absolute nothing and the hyle as the only created thing — the paragraph immediately before K6's slice, ending `וְאַחַר הַהִיּוּלִי לֹא בָּרָא דָּבָר` |
| BR 2:5 | K8 or K9 | R. Abahu: *tohu va-vohu* is the deeds of the wicked and *fiat lux* the deeds of the righteous, with God preferring the latter at 1:4 — the moral reading of the separation; R. Ḥiyya: the Temple built, destroyed, rebuilt |
| Honorius, PL 172:260C | K4 | *corporalis creatura adhuc informata, sed in verbo Dei causaliter posita*, with *creavit omnia simul* following |
| Abelard, PL 178:734D (continuation) | K4 or K5 | the confused heap of the elements named *chaos* by "certain of the philosophers or poets", immediately after K6's slice |
| Ibn Ezra on 1:2 (continuation) | K5 | the seven earths, and the refutation of those who take *heaven* in v. 1 as the heaven of heavens |
| Bruno, PL 164:148B | K5 | *"natura tamen prior terra non exstitit"* — the order of heaven and earth, immediately before K6's slice |

**Witnesses now on two benches with the same shape.** BR 2:3, BR 2:4 and Bruno of Segni all read
Gen 1:2 as a periodization of sacred history running to a final redemption; Isidore, Wigbod,
Rabanus and Remigius read it as the soul before doctrine. The K9 pass (`good-and-separated`) will
meet the same pairing again on *vayavdel*, where BR 3:8 and Augustine both make the division moral
— worth checking whether the two allegorical strands are one habit or two.

## From K5 (built 2026-09-05)

**Three passages that belong to K5 were already sliced whole by K1 and could not be built.** The
frozen rule is that a crux does not revise another crux's witnesses, so these are threads and
facets for Phase 4, not edits:

| witness (built for) | add crux | why |
|---|---|---|
| `bruno-gen-1-1` (K1) | `heaven-earth-order` | PL 164:147B is the closest Latin analogue to BR 1:15 anywhere on the bench: Ps 101:26 quoted, then *"non igitur prius coelum, quam terram, sed simul et coelum Deus creavit et terram"*, then Sir 18:1. Write the edge to `br-1-15` and to `ambrose-hex-1-6-24`. |
| `glossa-1-1` (K1) | `heaven-earth-order` | the VERS. 1 block carries **two** K5 glosses — Augustine's *universaliter … deinde per partes* at 113:67B (thread to `aug-gnl-1-9` and `angelom-gen-1-1b`) and the empyrean gloss at 68C, which is Remigius PL 131:54D almost verbatim (thread to `remigius-gen-1-1b`). |
| `rabanus-gen-1-1b` (K1) | `heaven-earth-order` | PL 107:444B copies Ambrose *Hex.* I.6.20 verbatim from *"In principio itaque temporis, coelum et terram Deus fecit"* — the passage K5 builds as `ambrose-hex-1-6-20`. A clean `cites` edge, invisible while the two sit in different cruxes. |

**The version witnesses on Gen 1:1 should carry K5.** `lxx-1-1`, `vulgate-1-1`, `targ-onk-1-1`,
`targ-neof-1-1`, `targ-psj-1-1` all render the word order the crux is about, and none of them
reverses it; Gen 2:4, which reverses it in Hebrew, is what both benches argue from. Without them
the K5 daf renders with an empty `versiones` column — see `notes/SOURCES-FINDINGS.md`.

**`b-chag-12a` (K10's ten-things witness) now carries three cruxes** and is threaded on K5 to
Augustine (`t-k5-08`). Its segments 7–11 are K8's light material, built separately as
`b-chag-12a-light`; segments 15–19 are K5's, built here as three witnesses. One Talmud page is now
divided among four cruxes and five witnesses — the largest single locus in the project, and worth a
line in the Phase 8 introduction.

| left for | crux | note |
|---|---|---|
| b. Chagigah 12a, segments 12–14 | K1 or K4 | R. Zutra bar Tuvya: with ten things the world was created (wisdom, understanding, knowledge…), Prov 3:19 for the first two — the same verse the Latin bench uses for *in principio = in Wisdom* (K1) |
| b. Chagigah 12a, segment 14 | K4 | the world expanding like warp and woof until God rebuked it and said *dai* — the El Shaddai etymology, which PdRE 3 (K8's `pdre-3-6`) also carries |
| Comestor, PL 198:1055A (continuation) | K4 | Plato, Aristotle and Epicurus set against Moses' *creavit* — noted at K1 too, still unbuilt |
| Ramban on 1:1 (continuation) | K9 | the four elements named again under the terms of v. 2: *fire* is what "darkness" means, *water* is "the deep" — a physical reading of the words K9 is built on |
| Abelard, PL 178:737B | K5 (second pass) | a second treatment of *nomine coeli et terrae* on the fourth day's works, restricting the pair to the earthy and fiery elements; not built, the first is fuller |

## From K4 (built 2026-09-05)

**The version witnesses on Gen 1:1 should carry K4, and the case is stronger than K5's.** The whole
Latin argument on this crux turns on *creavit* against *formavit* — Abelard builds his definition of
creation on the pair, Rupert has to explain *creavit* away at Gen 1:21 and 1:27, and Ibn Ezra takes
the same two verses to prove the Hebrew verb does not carry the sense. **That is a fact about the
translations**, and none of the witnesses that preserve them is on the daf: `vulgate-1-1`, `lxx-1-1`,
`targ-onk-1-1`, `targ-neof-1-1`, `targ-psj-1-1` all belong to K1 and carry only that crux. The daf
rendered with `versiones 0`. Second crux in a row to hit this — see the K5 entry above.

**A doctrine settled at one crux foreclosing an answer at another, for the second time.** K8's
finding was that BR 1:3 and BR 3:8 debar the rabbinic bench from Augustine's angelic first light.
The same shape appears here: **Alcuin's list of what was made out of nothing has the angels and the
human soul on it, and the rabbinic lists (b. Chag 12a's ten, PdRE 3:5's eight) have tohu and bohu on
theirs** — each list is the other's answer with the contested items swapped in and out. Phase 4
should decide whether the graph can carry an edge between two enumerations that are answering the
same question with incompatible inventories, or whether this too is Phase 8 prose. No thread was
written; `b-chag-12a` and `pdre-3-5` are on other cruxes' rosters.

**Witness-facet additions noticed while building, not acted on:**

| witness (built for) | add crux | why |
|---|---|---|
| `ramban-1-2-tohu` (K6) | `ex-nihilo-or-matter` | it is the sentence immediately after K4's slice and completes the argument: the hyle *is* what Scripture calls tohu. K4 threads to `br-1-5b` for the same point instead. |
| `br-2-2` / `br-2-3` (K6) | — | checked, not K4: they read *tohu va-vohu* as periodization, not as material. |
| `basil-hex-2-4` (K6) | — | its own note already says the following paragraph is K4's; K4 has now built it as `basil-hex-2-2-materia`. No facet change needed. |

**Material read for K4 that belongs elsewhere, all on disk:**

| locus | belongs to | note |
|---|---|---|
| Bereshit Rabbah 1:5, **first half** | K2 `why-begin-here` | "may they be silenced" and the ban on expounding the work of creation — already flagged from K1, still unbuilt. K4 took only the second half, from the palace parable. |
| m. Chagigah 2:1 (`m-chag-2-1`, on disk, unbuilt) | K2 | "whoever looks at four things: what is above, what is below, what is before, what is after" — **the rabbinic bench forbidding the question that is chapter one of Hugh's *De sacramentis***. It is not a comment on the verse, so the anchor rule keeps it out of K4; it is the best single text K2 has. |
| b. Chagigah 12a, segments 12–13 | K1 | R. Zutra bar Tuvya: with ten things the world was created, wisdom and understanding from Prov 3:19 — the verse the Latin bench uses for *in principio = in Wisdom*. |
| b. Chagigah 12a, segment 14 | K1 or a cosmology crux | the world expanding like warp and woof until God rebuked it and said *dai*; the El Shaddai etymology, which PdRE 3:6 (K8) also carries. Read, and not K4: it is about the world's extension, not its material. |
| b. Chagigah 12a, segment 6 | K6 | the baraita: *tohu* is a green line encompassing the world, *bohu* smooth stones sunk in the deep, from Isa 34:11 — **the same verse Ramban builds his hyle on**, four lines after K4's slice ends. |
| Honorius, PL 172:257A | K10 or a six-days crux | *In principio namque coelum et terra, ad materiam ex nihilo creantur* inside a summary of the six days; one clause, read and not built. |
| Hugh, *De sacr.* I.5 CAP. VII, PL 176:249C–D | an angels crux, if one is ever made | *Quod non sunt facti de materia praejacente sicut corporea* — the angels' creation, which is what PHASES.md's "247B" pointer was near. Not on the verse. |
| Ambrose, PL 14:130C | K2 | *Auctorem enim…* — the argument from the visible to the invisible; adjacent to K4's material, on K2's question. |

## From K9 (built 2026-09-05)

**Two rabbinic slices this crux had to work around, and one of them is a slice defect rather than a
crux boundary.** K8's `br-3-6` took the whole of Sefaria's BR 3:6 segment for its first half (the
light stored away for the righteous); the segment's *second* half is entirely on *va-yavdel* and is
K9's single richest rabbinic text — R. Ze'eira's havdala derivation, *hivdilo lo* / *hivdilo
la-tzaddikim*, R. Yoḥanan and Resh Lakish's *havdala mamash* with the two generals, R. Tanḥuma on
Isa 45:7, and R. Elazar on the missing divine name. Two distinct arguments on two clauses were
merged into one card, which the frozen rule forbids. K9 has built the second half as `br-3-6b` on
its own lemma rather than lose it. **Phase 4 must trim `br-3-6` to end at R. Neḥemya's seven days of
mourning**, not delete `br-3-6b`.

**`rashi-1-4` (K8) carries both cruxes' answers in one dibbur and was left alone.** Rashi gives the
aggadic answer (the wicked were unworthy of the light, so he set it apart for the righteous — K8,
citing Chagigah 12a) and then the *peshat* (it was not seemly that light and darkness should
function in confusion, citing BR 3:6 — K9's answer, and the closest thing on the rabbinic bench to
Ambrose's *nihil videatur intra se habere confusum*). It is genuinely one continuous argument, so
no duplicate was built. **Phase 4: add `good-and-separated` to its `cruxes` facet** and write the
edges to `ambrose-hex-1-9b` (parallel: the same purpose clause, Milan and Troyes) and to `br-3-6b`.

**Witness-facet additions noticed while building, not acted on:**

| witness (built for) | add crux | why |
|---|---|---|
| `br-3-6` (K8) | — | do not add K9; trim it instead, per the note above |
| `rashi-1-4` (K8) | `good-and-separated` | the *peshat* half is this crux's answer |
| `b-chag-12a-light` (K8) | `good-and-separated` | it is what Rashi cites for *va-yavdel* = he set it apart for the righteous, and `br-3-6b`'s Rabbis say the same thing |
| `aug-gnl-1-3` / `aug-gnl-1-11` (K8) | possibly | Augustine's *Gnl* I treats the division at I.9–10 (PL 34:254), which is neither built here nor there |

**Material read for K9 that belongs elsewhere, all on disk or in the local TEI:**

| locus | belongs to | note |
|---|---|---|
| Alcuin, *Int.* 94 (PL 100:530-ish) | an evil/privation crux, if one is ever made | *Quid est malum? — Malum vero nihil est per se, nisi privatio boni: sicut tenebrae nihil sunt, nisi absentia lucis.* The cleanest Carolingian statement of the privation doctrine, and it is **not on the verse** — it sits among the questions on the fall — so the anchor rule keeps it off this daf. It is what makes Wigbod's essence-of-darkness the more striking. |
| Hugh, *De sacr.* I.1 cap. XII (PL 176:195C–196C) | K9, second pass, or a moral layer | *Primum in corde peccatoris creatur lux* — the sinner dividing light from darkness in himself, virtues from vices, and only then daring to name them. Read and dropped: the moral reading is already carried by Isidore, Remigius, the Glossa, BR 2:5 and BR 3:8. It is the best Latin text for a moral layer if one is built. |
| Rabanus PL 107:467A, Remigius PL 131:55D | K7 or a moral layer | the *fiat lux* = light of faith allegory that PHASES.md flagged for K9. Both are anchored on **1:2** (*terra inanis*, *tenebrae super faciem abyssi*), not on 1:4, and both run the soul-before-doctrine reading K6 and K7 already have. Not built here. |
| Rupert, PL 167:214B and 215B | K9, second pass | two further treatments of the same clause in the same work — the potter of Rom 9 and the order *prius vidit … deinde dividens*. The first (210A–C) is fuller and is what K9 built. |
| Basil/Eustathius, PL 53:924B | a day-and-night crux | *sic obumbrato aere qui terrae proximus est, nox efficitur* — night as the shadowing of the air near the earth, on the fourth day's works. The physics behind Comestor's shadow. |
| Bonaventure II Sent. d.13 a.1 q.2, a.2 q.1–2 | Phase 6 | still unbuilt, still the right place for the substance/accident question Rupert raises at K8. |
| Honorius, PL 172:261C | K9, second pass | *formatam et intelligibilem creaturam ab informata discrevit* — a second treatment in TEI 10991, the *formatum ab informi* answer again; the 255D passage is fuller and is what K9 built. Note this is inside the same work-division problem K10 flagged at PL 172:261. |
| Bruno, PL 164:149A | — | checked and dropped: his only sentence on 1:4 is *bona ergo lux, quae a tenebris divisa rerum formas coloresque illuminat*, and the block is where `bruno-gen-1-3` begins. |

**A third instance of the shape K8 and K4 both hit — a doctrine settled elsewhere foreclosing an
answer here — and this time it runs the other way.** The Latin bench cannot say that God made the
darkness, because Augustine settled at Gen 1:2 that darkness is the privation of light; so when
Remigius, Wigbod's pupil and the Glossa say it anyway, they say it without argument from authority
and without noticing that they are contradicting the gloss printed three columns earlier on the
previous verse. The rabbinic bench, which never took up the question, says it four times over
without embarrassment. Phase 4 should decide whether this belongs in the graph; K9's `finding`
carries it for now.

**The two Latin texts of this verse sort the bench, and no witness on the site preserves the Old
Latin.** `vulgate-1-4` is Jerome's *divisit lucem a tenebris*; the Old Latin that Augustine, Alcuin
and Angelomus quote — *divisit inter lucem et tenebras*, from the Greek's doubled *ana meson* — is
attested on this daf only inside the witnesses that quote it. Phase 6 should decide whether a Vetus
Latina witness is worth adding, at this verse and at Gen 1:1 (*creavit* / *fecit*, K1) where the
same problem arose.

## From K3 (built 2026-09-05)

**The versiones column is empty for the fourth crux running, and on this crux it is not a cosmetic
loss.** Megillah 9a is a text *about* what the Greek Bible says; the targums replace *Elohim* with
the Tetragrammaton throughout and so erase the plural noun the whole crux turns on; and the
Vulgate's *Deus* for *Eloim* is the fact Abelard is working behind. None of it is on the daf,
because all five version witnesses on Gen 1:1 were built by K1 and carry only `beginning-of-what`.
**Phase 4, mechanical edit**: add facets to `lxx-1-1`, `vulgate-1-1`, `targ-onk-1-1`,
`targ-neof-1-1`, `targ-psj-1-1` — `heaven-earth-order` (flagged at K5), `ex-nihilo-or-matter`
(flagged at K4) and `elohim-and-trinity` (here) — and write the K3 edges: `b-meg-9a → lxx-1-1`
(*contests*: the baraita says the elders reversed the order, and the transmitted Greek has not
reversed it) and `targ-onk-1-1 → br-1-7` (*echoes*: the targum removes the plural noun the midrash
has to defend).

**Three Latin passages that belong to K3 were already sliced whole and could not be built.** All
three were caught by `overlap.py` and all three are threaded to instead:

| witness (built for) | why it is K3's | status |
|---|---|---|
| `aug-gnl-1-5-11` (K7) | contains *De Genesi ad litteram* I.6.12, the **completa commemoratio Trinitatis** — the fullest statement of the triad anywhere on the bench | already carries `elohim-and-trinity`; threaded (`t-k3-11`, `t-k3-19`, `t-k3-22`, `t-k3-23`) |
| `ambrose-hex-1-8-29` (K7) | contains PL 14:138D, *ut in constitutione mundi operatio Trinitatis eluceat … in Christo fecit Deus* | already carries the crux; threaded (`t-k3-13`) |
| `comestor-hs-1-1` (K1) | contains PL 198:1056A, *creatus autem est in principio, id est in Filio* | K1-only; **Phase 4 should add the facet.** No K3 thread was written |

**Material read for K3 that the anchor rule keeps off this daf, and it is the crux's own evidence.**
This is the sharpest case so far of the scripture layer excluding something the finding depends on:

| locus | why it matters | why it is not a witness |
|---|---|---|
| Jerome, *HQ in Gen.* PL 23 on **Gen 6:2** | *Verbum Hebraicum ELOIM communis est numeri, et Deus quippe et dii similiter appellantur; propter quod Aquila plurali numero filios deorum ausus est dicere.* The **only** Latin statement that *Elohim* is plural in number outside Abelard | Gen 6:2, outside the 1:1–5 layer |
| Rabanus, PL 107:511D–512A | copies Jerome's sentence verbatim, so the fact is in the Carolingian schools too — and still nobody carries it to Gen 1:1 | same |
| Bede PL 91:28C–29A; Rabanus 107:459C; Angelomus 115:122A; Alcuin *Int.* 37; Augustine *Gnl* III and *Gnl imp* 61; Abelard 178:761A | the whole Latin bench's discussion of divine plurality, all of it on **Gen 1:26** *Faciamus hominem* — *unitas sanctae Trinitatis aperte commendatur*, *trinus est Deus in personis et unus in deitatis natura* | Gen 1:26, outside the layer |
| BR 8:8–9; Rashi and Ibn Ezra on 1:26 | the rabbinic answers to *na'aseh* — the counterpart material — unread and unpulled | same |

⭐ **If the scripture layer is ever widened, Gen 1:26 is the first verse to add, and K3 is the crux
that would gain most.** Bruno of Segni's witness here reaches back to 1:1 *from* 1:26 and is the
only reason the refutation ("was it to the angels? God forbid") is on the daf at all. As it stands,
the daf carries the Latin bench's triad-of-names reading in full and its plural-noun reading only in
Abelard, which is accurate to the anchor rule and not to the tradition.

**Left for a second pass or another crux:**

| locus | belongs to | note |
|---|---|---|
| Honorius, PL 172:260B | K3 second pass, or K1 | *In Filio suo, scilicet in Sapientia sua, Deus Pater creavit omnia simul* — a second treatment of the same triad in TEI 10991; `honorius-hex-1` (254B) is fuller and is on the roster. Same work-division question K10 flagged at PL 172:261 |
| Hugh, *De sacr.* I.2–3 (PL 176:208D, 226B–234A) | a Trinity crux, if one is ever made | the full Victorine treatise, including the appropriation *potentia Patri, sapientia Filio, bonitas Spiritui sancto* that Honorius applies to Gen 1:1. Not on the verse, so not buildable here |
| Augustine, *Gnl* II (PL 34:267–268) | K3 second pass | *An ita Trinitas intelligitur: Et dixit Deus Fiat, Et fecit Deus, Et vidit Deus quia bonum est?* — the reading Rupert builds on, **considered and refused**, at Gen 1:6. Threaded from `rupert-gen-1-3-trinitas` to `aug-gnl-1-5-11` instead, which is not the same passage; Phase 4 should build the real one if the layer widens |
| Wigbod PL 96:1109D, 1115C | K1 | *omnia in se Trinitas Deus disposuit* and a second *in principio, id est in Filio*; the dialogue treats the verse three times |

## From K2 (built 2026-09-05 — Phase 2 complete)

**The anchor rule was set aside for four witnesses, on PLAN.md's authority and not the builder's.**
`m-chag-2-1`, `hugh-sacr-prologus` and `comestor-hs-prologus` are not comments on Gen 1:1, and
PLAN.md §5's K2 entry names prologues explicitly ("Glossa prothemata; Comestor prologue; Hugh Sacr.
prologue"), so the plan contemplated them for this crux before the rule was frozen in PHASES.md.
Each carries an `⚠ Anchor note` in its own `notes` field and the file docstring says so. **Wilson
should rule on this at Phase 3.** If he rules against, the three are removable and the crux survives:
`br-1-10` carries m. Chagigah's four forbidden questions verbatim as a comment on the first letter
of Gen 1:1, and `rashi-1-1` carries the crux's central objection. If he rules for, the same
licence would let **Gen 1:26 (*Faciamus hominem*) into K3**, which is where most of the Latin
material on divine plurality actually sits — see the K3 entry above.

**Two K2 passages were already sliced whole and are threaded to rather than rebuilt:** Ambrose's
Plato and the three principles (PL 14:123A) is inside K4's `ambrose-hex-1-1-hyle`, and Hugh's
*philosophi gentilium tria quaedam rerum principia* (PL 176:187A) is inside K4's
`hugh-sacr-1-1-nihilo`. Both belong to K2's *against the philosophers* answer as much as to K4's
matter question. **Phase 4: add `why-begin-here` to both.**

**`rashi-1-1b` (K1) and `rashi-1-1` (K2) are the two dibburim of one Sefaria segment**, correctly
split: K1 took *bereshit bara*, K2 took *bereshit*. No trimming needed — this is what K8's `br-3-6`
should have looked like.

**Left for a second pass:**

| locus | note |
|---|---|
| Hugh, *De sacr.* Prologue CAP. III (PL 176:183B) | *Quoniam divina Scriptura per opera conditionis descendat ad narranda opera restaurationis* — the chapter that repairs the difficulty CAP. II creates, and the literal answer to this crux's question. Not built; CAP. II is the one that states the position |
| Hugh, *De sacr.* I.1 CAP. XXVIII | *Quare opera conditionis prius commemorantur; deinde opera restaurationis* — the crux's question as a chapter heading, in Book I. Located in the table of contents at PL 176:175D; the chapter body was not tracked down |
| Glossa *prothemata* | PLAN.md §5 lists it; **TEI 8950 has no prefatory matter** — the file opens straight at CAPUT PRIMUM, VERS. 1. If the Glossa's prologues are wanted they are not in this transcription |
| Tanchuma Bereshit 1 | PLAN.md's [CHECK] for K2. `tanch-std-ber-1.json` and `tanch-buber-ber-1.json` are on disk and were not read for this crux |
| BR 1:1, 1:3, 1:4 | K1's material (Torah as *amon*, the architect's plans); adjacent to K2's question and not read again here |
