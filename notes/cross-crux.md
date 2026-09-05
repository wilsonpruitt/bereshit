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
