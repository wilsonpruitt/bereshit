# PLAN.md — Genesis 1:1–5 Crux & Dialogue Pilot

Working title: **Bereshit / In Principio** (Wroot Labs)
Scope: one pericope, two views, full corpus depth. Nothing beyond Genesis 1:5 in this pilot.

---

## 1. What this is

A digital edition of the interpretation of Genesis 1:1–5 in which the organizing unit is **not the verse and not the tradition** but:

1. **The crux** — a specific textual difficulty that interpreters in both the Latin and rabbinic traditions actually addressed. Each crux page shows every response from both traditions, undivided, ordered by date.
2. **The dialogue** — per verse, every witness interleaved chronologically across traditions, with documented dependencies (citations, echoes, contested readings) drawn as visible threads between them.

Two traditions, one text, ~1,300 years. The Glossa is one witness among many; the Patrologia Latina supplies the rest of the Latin bench, Sefaria supplies the rabbinic bench.

Both views are queries over a single graph. Build the graph first.

---

## 2. Locked decisions

- **Pericope:** Genesis 1:1–5 only. No 1:6 material even where a witness runs past it.
- **Views in pilot:** Crux view and Dialogue view. Time-scrubber, word-level lemma view, invertible center, authority map are Phase 2 views over the same data.
- **Crux register is authored by hand** for the pilot (see §5). No automatic crux detection.
- **Thread edges require evidence.** No edge without a `evidence` field quoting or citing the dependency. Structural similarity without citation is edge type `parallel`, never `cites`.
- **Latin text source:** Corpus Corporum (mlat.uzh.ch) TEI for passage *location and extraction*. Latin is republished from the public-domain PL text; do not republish Corpus Corporum's TEI files verbatim (see Traps).
- **Glossa text:** Wilson's own Englished Glossa (migne.app/glossa edition), not PL 113.
- **Rabbinic text source:** Sefaria API / Sefaria-Export (GitHub). Hebrew/Aramaic originals are CC0/PD.
- **English policy:** Use existing PD or CC BY English where it exists; everything else is freshly Englished. No CC BY-NC text is embedded, ever. NC texts are link-out only.
- **Stack:** Astro + Tailwind, static JSON, Pagefind. EB Garamond / Inter. Same architecture as the Wesley Timeline and Dictionary.
- **Scripture:** Hebrew (Sefaria, Miqra according to the Masorah), Vulgate (Corpus Corporum), English WEB. Vulgate is a *witness*, not just a base text — it makes interpretive choices (`inanis et vacua`, `ferebatur`, `dies unus`) that later Latin witnesses inherit.

---

## 3. Source manifest

### 3a. Latin bench (Patrologia Latina via Corpus Corporum)

Ordered by date. PL volume given for locating the passage; `[CHECK]` where the exact locus must be confirmed against the text.

| id | Author | Work | Locus for Gen 1:1–5 | Date | Place | PL |
|---|---|---|---|---|---|---|
| origen-hom-gen | Origen (Rufinus tr.) | Homiliae in Genesim I | Hom. 1.1 | c. 240 / tr. c. 403 | Caesarea / Aquileia | PG 12 [CHECK: present in Corpus Corporum?] |
| basil-hex-lat | Basil (Eustathius tr.) | Hexaemeron I–II | Hom. 1–2 | 378 / tr. c. 400 | Caesarea Capp. | PL 53 |
| ambrose-hex | Ambrose | Exameron I | I.1–10 | c. 387 | Milan | PL 14 |
| jerome-hq | Jerome | Hebraicae Quaestiones in Genesim | on 1:1, 1:2 | c. 391 | Bethlehem | PL 23 |
| aug-gnm | Augustine | De Genesi contra Manichaeos I | I.1–10 | 388–389 | Thagaste | PL 34 |
| aug-gnl-imp | Augustine | De Genesi ad litteram liber imperfectus | 1–6 | 393 | Hippo | PL 34 |
| aug-conf | Augustine | Confessiones XI–XIII | XI.3–9, XII.3–22, XIII.2–5 | c. 400 | Hippo | PL 32 |
| aug-gnl | Augustine | De Genesi ad litteram I, IV | I.1–19; IV.21–35 | 401–415 | Hippo | PL 34 |
| aug-civ | Augustine | De civitate Dei XI | XI.7–9, 19–20, 32–33 | c. 417 | Hippo | PL 41 |
| isidore-quaest | Isidore | Quaestiones in Vetus Testamentum, In Genesim | 1–2 | c. 620 | Seville | PL 83 |
| bede-gen | Bede | In Genesim I | on 1:1–5 | c. 720 | Jarrow | PL 91 |
| alcuin-int | Alcuin | Interrogationes et responsiones in Genesim | qq. 1–20 approx. | c. 796 | Tours | PL 100 |
| wigbod-gen | Wigbod | Quaestiones in Octateuchum, In Genesim | on 1:1–5 | c. 790 | Aachen | PL 96 |
| claudius-gen | Claudius of Turin | Commentarii in Genesim | on 1:1–5 [CHECK: extant portion] | c. 820 | Turin | PL 50 [CHECK] |
| rabanus-gen | Rabanus Maurus | Commentaria in Genesim I | I.1–2 | c. 822 | Fulda | PL 107 |
| angelom-gen | Angelomus of Luxeuil | Commentarius in Genesim | on 1:1–5 | c. 850 | Luxeuil | PL 115 |
| remigius-gen | Remigius of Auxerre | Expositio super Genesim | on 1:1–5 | c. 900 | Auxerre | PL 131 |
| bruno-gen | Bruno of Segni | Expositio in Genesim | on 1:1–5 | c. 1100 | Segni / Montecassino | PL 164 |
| glossa | Glossa ordinaria | Marginal and interlinear on Gen 1:1–5 | — | c. 1110–1130 | Laon | Wilson's edition |
| rupert-gen | Rupert of Deutz | De sancta Trinitate, In Genesim I | I.1–20 approx. | c. 1114 | Liège / Deutz | PL 167 |
| abelard-hex | Peter Abelard | Expositio in Hexaemeron | on 1:1–5 | c. 1130 | Paraclete | PL 178 |
| hugh-adnot | Hugh of St Victor | Adnotationes elucidatoriae in Pentateuchon | on Gen 1 | c. 1130 | Paris | PL 175 |
| hugh-sacr | Hugh of St Victor | De sacramentis I.1 | I.1.1–12 | c. 1134 | Paris | PL 176 |
| honorius-hex | Honorius Augustodunensis | Hexaemeron | 1–2 | c. 1140 | Regensburg | PL 172 |
| comestor-hs | Peter Comestor | Historia Scholastica, Genesis | cc. 1–5 | c. 1170 | Paris | PL 198 |
| bonaventure-sent | Bonaventure | In II Sent. d. 12–13 | d.12 (matter, simultaneity); d.13 (light) | c. 1252 | Paris | Not PL — Wilson's Bonaventure corpus (bonaventure.wrootpress.com) |
| lyra-post | Nicholas of Lyra | Postilla litteralis, Gen 1 | on 1:1–5 | c. 1322 | Paris | Not PL — [CHECK source; see Open Decisions §9.2] |
| burgos-add | Paul of Burgos | Additiones to Lyra, Gen 1 | on 1:1–5 | c. 1429 | Burgos | Not PL — [CHECK, same source as Lyra] |

Pilot minimum if the bench must be cut: Jerome HQ, Augustine (Gnl + Gnm + Civ XI), Ambrose, Bede, Glossa, Rupert, Hugh (Sacr.), Comestor, Lyra. The rest are depth.

### 3b. Rabbinic bench (Sefaria unless noted)

| id | Work | Locus for Gen 1:1–5 | Date | Place | Original | English & license |
|---|---|---|---|---|---|---|
| lxx | Septuagint Gen 1:1–5 | — | 3rd c. BCE | Alexandria | Greek (PD) | Brenton 1851 (PD) |
| philo-opif | Philo, De opificio mundi | 7–37 | c. 30 CE | Alexandria | Greek (PD) | Yonge 1854 (PD) |
| josephus-ant | Josephus, Antiquities | 1.27–29 | c. 94 | Rome | Greek (PD) | Whiston (PD) |
| targ-onk | Targum Onkelos | 1:1–5 | c. 2nd c. | Babylonia | Aramaic (CC0) | Etheridge 1862 (PD) |
| targ-neof | Targum Neofiti | 1:1–5 (esp. "with wisdom") | 1st–4th c. | Palestine | Aramaic (CC0) | [CHECK: no PD English; translate] |
| targ-psj | Targum Pseudo-Jonathan | 1:1–5 | 7th–8th c. (older strata) | Palestine | Aramaic (CC0) | Etheridge 1862 (PD) |
| m-chag | Mishnah Chagigah 2:1 | — | c. 200 | Galilee | Hebrew (CC0) | Kulp, Mishnah Yomit [CHECK license, believed CC BY] |
| br-1 | Bereshit Rabbah 1 | whole parashah (on 1:1) | c. 400–500 | Galilee | Hebrew/Aramaic (CC0) | Sefaria commissioned tr., CC BY |
| br-2 | Bereshit Rabbah 2 | whole parashah (on 1:2) | " | " | " | " |
| br-3 | Bereshit Rabbah 3 | whole parashah (on 1:3–5) | " | " | " | " |
| y-chag | Yerushalmi Chagigah 2:1 (77c) | ma'aseh bereshit | c. 400 | Tiberias | Aramaic (CC0) | None PD in English; Schwab French 1871–90 (PD). Translate or omit. |
| b-chag-12a | Bavli Chagigah 12a | ten things created on day one; heaven/earth order; primordial light hidden | c. 500 | Babylonia | Aramaic (CC0) | Steinsaltz CC BY-NC → **link only**; fresh translation |
| b-chag-15a | Bavli Chagigah 15a | Ben Zoma on the hovering spirit | " | " | " | " |
| b-meg-9a | Bavli Megillah 9a | the LXX elders' changes; "God created in the beginning" | " | " | " | " |
| b-rh-11a | Bavli Rosh Hashanah 10b–11a | world created in Tishrei / Nisan | " | " | " | " |
| pdre-3 | Pirkei de-Rabbi Eliezer 3 | creation day one; what preceded the world | 8th–9th c. | Palestine | Hebrew (CC0) | Friedlander 1916 (PD) |
| tanch-ber | Midrash Tanchuma, Bereshit 1 | on 1:1 | 8th–9th c. | Palestine | Hebrew (CC0) | [CHECK Sefaria English license; Berman 1996 is likely NC] |
| rashi | Rashi on Genesis 1:1–5 | all comments | c. 1080–1105 | Troyes | Hebrew (CC0) | Rosenbaum–Silbermann 1929–34 (PD, on Sefaria) |
| ibn-ezra | Ibn Ezra on Genesis 1:1–5 | esp. on *bereshit* grammar | c. 1155 | Rouen/Lucca | Hebrew (CC0) | No PD English; translate (Phase 2 candidate) |
| ramban | Ramban on Genesis 1:1–5 | esp. 1:1 on creation ex nihilo (*hyle*) | c. 1260 | Girona | Hebrew (CC0) | No PD English (Chavel copyrighted); translate (Phase 2 candidate) |

Rashi cites Bereshit Rabbah explicitly and repeatedly in 1:1–5; those citations are `cites` edges, not `parallel`.

### 3c. Where English already exists (embed) vs. must be made (translate)

- **Embed as-is:** Sefaria Midrash Rabbah (CC BY, attribution block required), Silbermann Rashi (PD), Etheridge Targums (PD), Yonge Philo (PD), Whiston Josephus (PD), Brenton LXX (PD), Friedlander PdRE (PD), Wilson's Glossa.
- **Translate fresh (from CC0 originals):** all Bavli passages, Yerushalmi if included, Neofiti, Tanchuma if NC, Ibn Ezra, Ramban.
- **Translate fresh (from PD Latin):** essentially the entire Latin bench. Existing English of Augustine *De Genesi ad litteram* (Taylor 1982), Ambrose *Hexameron* (Savage 1961), Bede *On Genesis* (Kendall 2008), Jerome *Hebrew Questions* (Hayward 1995) are all in copyright. NPNF (PD) covers *Confessions* and *City of God* only. Do not use NPNF Basil — it translates the Greek, not Eustathius' Latin, and the Latin bench should carry the Latin the medieval readers had.

---

## 4. Data model

Static JSON, monthly-chunk pattern adapted to pericope. All ids are slugs; all dates are integers (year CE, negative for BCE) with a `date_precision` field.

```
data/
  scripture/
    gen-1.json            # verses 1–5 in he / la / en(WEB), word-tokenized with stable token ids
  witnesses/
    <witness-id>.json     # one file per passage (a witness = one continuous passage from one work)
  cruxes.json
  threads.json
  persons.json            # authors + named rabbis (R. Hoshaya, Ben Zoma, etc.) — same schema as Wesley Timeline persons.json
  places.json             # gazetteer — same schema as Topographia Sacra places.json
  works.json              # bibliographic: author, title, date, place, PL vol / Sefaria ref, license
  licenses.json           # attribution strings, rendered in colophon
```

### witness

```json
{
  "id": "jerome-hq-1-2",
  "work": "jerome-hq",
  "author": "jerome",
  "tradition": "latin",
  "date": 391, "date_precision": "circa",
  "place": "bethlehem",
  "anchor": { "verse": "gen.1.2", "tokens": ["he.gen.1.2.7"] },
  "lemma": { "he": "מְרַחֶפֶת", "la": "ferebatur", "en": "was hovering" },
  "original": { "lang": "la", "text": "…", "source": "PL 23, col. 937", "license": "pd" },
  "english": { "text": "…", "translator": "wilson-pruitt", "license": "cc-by" },
  "cruxes": ["ruach-hovering"],
  "senses": ["literal"],
  "notes": "Jerome cites the Hebrew directly and gives the bird image."
}
```

`tokens` point into `scripture/gen-1.json` so the Phase 2 lemma view costs nothing later. Populate them now, even though the pilot views don't use them.

### crux

```json
{
  "id": "ruach-hovering",
  "verse": "gen.1.2",
  "question": "What is the ruach that moves over the waters, and what does merahefet mean?",
  "lemma": { "he": "וְרוּחַ אֱלֹהִים מְרַחֶפֶת", "la": "spiritus Dei ferebatur", "en": "the Spirit of God was hovering" },
  "summary": "…two or three sentences on why this is a crux…",
  "witnesses": ["br-2-4", "b-chag-15a", "jerome-hq-1-2", "aug-gnl-1-18", "rashi-1-2b", "glossa-1-2-m3", "…"]
}
```

### thread (edge)

```json
{
  "id": "t-017",
  "from": "rashi-1-2b",
  "to": "br-2-4",
  "type": "cites",
  "evidence": "Rashi names the source: 'as a dove hovering over the nest' follows BR 2:4 / Chagigah 15a.",
  "crux": "ruach-hovering"
}
```

`type` ∈ `cites` (explicit), `echoes` (verbal or image dependence, argued in `evidence`), `contests` (explicit disagreement), `parallel` (same move, no known contact), `transmits` (translation/mediation, e.g. Vulgate → Bede). Direction is always later → earlier except `transmits`.

---

## 5. Crux register — Genesis 1:1–5

Authored by hand. Ten cruxes. Witness lists are starting points; extraction will add and remove. `[CHECK]` marks loci to verify before extraction.

**K1 · `beginning-of-what`** (1:1, *bereshit / in principio*)
The beginning of what — time, or a principle, or a person? Rabbinic: BR 1:1 (R. Hoshaya, *amon* = Torah as architect's plan); BR 1:4 (six things preceded the world); Targum Neofiti "with wisdom"; Rashi 1:1 (construct state — "in the beginning of God's creating"; and *reshit* = Torah and Israel). Latin: Jerome HQ 1:1 (notes Aquila's *in capitulo*; the reading *in Filio*); Origen Hom. 1.1; Augustine Gnl I.1, Conf XI–XII, Gnm I.2; Ambrose Hex I.4; Bede; Glossa marginal *in principio, id est in Filio* [CHECK exact gloss]; Rupert; Hugh Sacr. I.1.1; Comestor c.1; Lyra (grammatical reading close to Rashi's).
Thread to watch: Neofiti's "with wisdom" and the Latin "in the Son/Wisdom" are the same move made from opposite ends of Prov 8:22–30.

**K2 · `why-begin-here`** (1:1)
Why does Scripture open with creation at all? Rashi 1:1 (R. Yitzchak: it should have begun at Exod 12:2 — answer: the nations and the land); BR 1:10 (why the letter *bet*); Tanchuma Bereshit 1 [CHECK]. Latin: Ambrose Hex I.1–2 (Moses against the philosophers); Augustine Gnm I.1–2 (against Manichaean mockery); Glossa prothemata; Comestor prologue; Hugh Sacr. prologue.
This is the crux where each tradition's *reason for having a commentary* is exposed.

**K3 · `elohim-and-trinity`** (1:1–2, *Elohim / Deus … spiritus*)
Who is the "God" who creates — and what do the grammar and word order say about plurality? Rabbinic: Megillah 9a (the elders wrote "God created in the beginning" so no one would read *Bereshit* as a deity); BR 1:7 [CHECK]; BR 1:12–13 [CHECK: heretics and *Elohim*]. Latin: Augustine Gnm I.2 (Father in *principio*, Son as *principium*, Spirit *super aquas*); Ambrose Hex I.8; Bede; Glossa; Rupert (whole work is structured on the Trinity in Genesis); Hugh Sacr. I.1.
Thread: Megillah 9a is a Jewish witness to a *Greek* interpretive move (the LXX order), which then reaches the Latin bench through the Vetus Latina. Edge type `transmits`.

**K4 · `ex-nihilo-or-matter`** (1:1–2)
Was anything there before? Rabbinic: BR 1:9 (the philosopher to Rabban Gamliel: "your God is a great craftsman, but he found good materials"); BR 1:5 [CHECK]; Ramban 1:1 (*hyle*, Phase 2). Latin: Augustine Conf XII.3–8 (*prope nihil*, formless matter), Gnm I.5–7, Gnl I.14–15; Bede; Glossa (*materia informis*); Hugh Sacr. I.1.4–6; Abelard; Comestor c.1; Bonaventure II Sent. d.12.
Both benches reach for 2 Macc 7:28 / Wis 11:17 and find them pulling in opposite directions.

**K5 · `heaven-earth-order`** (1:1, *hashamayim ve'et ha'aretz*)
Which was created first, and what is "heaven" here? Rabbinic: BR 1:15 (Shammai vs Hillel; R. Shimon b. Yochai: like a pot and its lid); Chagigah 12a (same dispute; the ten things created on day one); PdRE 3. Latin: Augustine Gnl I.1–3, I.9 (*caelum* = spiritual creation, *terra* = corporeal matter); Ambrose Hex I.6; Bede; Alcuin qq.; Glossa; Hugh Sacr. I.1.2–3; Comestor.
Chagigah 12a's ten-things list and Augustine's "what is contained in *caelum et terra*" are answering the same question — `parallel`.

**K6 · `tohu-vabohu`** (1:2, *tohu vabohu / inanis et vacua*)
What does the pair mean, and is it a state or a thing? Rabbinic: BR 2:2–3 (Bar Kappara; the four kingdoms reading [CHECK: BR 2:4]); Rashi 1:2 ("astonishment"); Targums. Latin: the Vulgate itself; Jerome HQ 1:2 [CHECK whether he glosses this pair]; Augustine Gnm I.5–7, Gnl I.15; Bede; Glossa (*inanis: ideo quia nihil erat in ea*); Rupert; Comestor.
The Vulgate's *inanis et vacua* is a witness in its own right: Latin readers inherited an interpretation, not a transliteration.

**K7 · `ruach-hovering`** (1:2, *ruach Elohim merahefet / spiritus Dei ferebatur*)
Wind, spirit, or Spirit — and what is *hovering*? Rabbinic: BR 2:4 (R. Shimon b. Lakish: the spirit of the King Messiah; Ben Zoma: "like a bird hovering, touching and not touching"); Chagigah 15a (Ben Zoma); Rashi 1:2 (throne of glory; "like a dove hovering over the nest"); Targums (*ruḥa min qodam YY*). Latin: Jerome HQ 1:2 (cites the Hebrew *merefeth*: *incubabat sive confovebat, in similitudinem volucris ova calore animantis* [CHECK exact wording]); Basil/Eustathius Hex II (the Syrian's bird-warming-eggs); Ambrose Hex I.8 (warming into life); Augustine Gnl I.18 (*superferebatur* — the Spirit's will above what it makes, not spatially above); Bede; Glossa; Rupert.
**This is the star thread of the pilot.** The bird image is in BR / Chagigah / Rashi and in Jerome, who says he got it from the Hebrew. Edge: `jerome-hq-1-2 → (Hebrew tradition)` type `cites`; `rashi-1-2b → br-2-4` type `cites`; `basil-hex-lat → syriac` type `cites`; `jerome ↔ ben-zoma` type `parallel` unless direct contact can be argued.

**K8 · `first-light`** (1:3, *yehi or / fiat lux*)
What was the light of day one, before sun and moon? Rabbinic: BR 3:4 (God wrapped in light like a garment, Ps 104:2); BR 3:6 (the light was hidden away for the righteous); Chagigah 12a (Adam saw from end to end by it; hidden); Rashi 1:4; PdRE 3. Latin: Augustine Gnl I.3–5, I.9–12, IV.22 (light = the angelic creation / angelic knowledge); Gnm I.6; Ambrose Hex I.9; Basil/Eustathius Hex II; Bede; Alcuin; Glossa; Rupert; Hugh Sacr. I.1.10; Comestor c.2; Bonaventure II Sent. d.13.
Both benches agree the light is not the sun's; they disagree on what it *is*.

**K9 · `good-and-separated`** (1:4, *vayavdel / divisit*)
Why does God separate light from darkness, and is darkness a creature, an evil, or the wicked? Rabbinic: BR 3:8 (the deeds of the righteous and the wicked; the separation is moral); Rashi 1:4 (not fitting that they be mixed); BR 3:6. Latin: Augustine Gnl I.17 (darkness is privation, not a thing); Civ XI.19–20 (the separation is the fall of the angels; *tenebrae* = the apostate angels); Gnm I.7; Bede; Glossa; Rupert; Hugh; Lyra.
Both traditions allegorize the same verse the same way (light/dark = righteous/wicked) — `parallel` on the surface; test whether Bede or the Glossa show any Hebrew mediation.

**K10 · `one-day-evening-first`** (1:5, *yom echad / dies unus; erev … boker*)
Why "one day" and not "first day," and why evening before morning? Rabbinic: BR 3:8–9 (God was alone in his world; "one day" = Yom Kippur [CHECK section]); Rashi 1:5 (unique, because the angels were not yet created); Chagigah 12a; RH 11a (Tishrei/Nisan). Latin: Vulgate *dies unus*; Augustine Gnl IV.22–31 (*cognitio matutina et vespertina* — angelic knowledge of things in the Word and in themselves), IV.33 (*creavit omnia simul*, Sir 18:1: the days are not successive); Ambrose Hex I.10; Bede (why *unus* not *primus*; the day begins at evening); Glossa; Rupert; Hugh; Comestor; Bonaventure II Sent. d.12–13 (Augustine vs the literal six days).
Augustine's morning/evening knowledge and Rashi's "alone in his world" both read *unus* as a claim about God's solitude, not about counting.

---

## 6. Views

### 6a. Crux view (`/crux/<id>`)
- Header: question, verse, trilingual lemma.
- One stream of witness cards ordered by date, each carrying a tradition badge (Latin / Rabbinic / Greek-Jewish), author, place, date, and the English with a toggle for the original. No columns, no grouping by tradition.
- Threads that stay inside this crux drawn as connectors between cards (SVG line in a gutter; hover highlights both ends and shows `evidence`).
- Right rail: persons and places appearing on this page, linked.

### 6b. Dialogue view (`/dialogue/gen-1-<verse>`)
- Every witness anchored to this verse, all cruxes, ordered by date. A crux chip on each card links out to the crux page.
- All threads drawn. `cites` solid, `echoes` dashed, `contests` red, `parallel` dotted-grey, `transmits` arrow with the mediating text labeled.
- Date axis as a faint scale on the left so the 1,300-year spread is visible. This axis is the hook for the Phase 2 scrubber.

### 6c. Shared
- `/witnesses/<id>` permalinks; `/persons/<id>`; `/places/<id>`; colophon with the license block rendered from `licenses.json`.
- Pagefind across English text, questions, and evidence strings.
- Fully static. No client fetches beyond Pagefind.

---

## 7. Build order

1. **Scripture layer.** `scripture/gen-1.json` with token ids in Hebrew, Latin, English. Everything else anchors here.
2. **Rabbinic pull.** Sefaria API: Bereshit Rabbah 1–3 (he + Sefaria CC BY en), Rashi Gen 1:1–5 (he + Silbermann en), Chagigah 12a & 15a, Megillah 9a, RH 10b–11a (Aramaic only), Targums Onkelos/PsJ/Neofiti (Aramaic), PdRE 3 (he). Etheridge, Friedlander, Yonge, Whiston, Brenton from Internet Archive / Wikisource / sacred-texts (PD).
3. **Latin pull.** Corpus Corporum: locate each work in §3a by browser path, fetch TEI, extract the loci listed. Record PL volume and column for every passage — that is the citation, not the Corpus Corporum URL.
4. **Witness files.** Cut passages into witness JSON. One witness = one continuous argument, not one PL column. Tag `cruxes` and `tokens`.
5. **Crux register** → `cruxes.json` from §5. Adjust witness lists to what extraction actually found.
6. **Threads** → `threads.json`. Start with the explicit citations (Rashi → BR; Jerome → Hebrew; Bede → Augustine; Glossa → everyone; Lyra → Rashi). Add `parallel` edges only where a crux page would be misleading without them.
7. **English gaps.** Produce a manifest of every witness lacking English. Wilson translates; Claude drafts and Wilson approves. Translator field is never blank.
8. **Astro build.** Crux view first, dialogue view second, permalinks and search last.
9. **Validate** against K7 (`ruach-hovering`) end-to-end before touching any other crux's rendering: if the Jerome / Ben Zoma / Rashi bird thread reads clearly on one page, the design works.

---

## 8. Known traps

- **Corpus Corporum licensing.** The site describes itself as non-commercial and the TEI files carry their conditions. The *Patrologia Latina text* is public domain (1844–1865); the *TEI markup and digitization* are theirs. Use the TEI to locate and extract; republish only the Latin text, cite PL by volume and column, and write your own English. Do not mirror their XML. If in doubt, email turicense@gmail.com and ask — the project is academic and friendly.
- **Steinsaltz Talmud is CC BY-NC.** Never embed. Link to the Sefaria daf; translate the Aramaic fresh.
- **Sefaria Midrash Rabbah is CC BY and requires attribution.** Render the exact attribution string Sefaria specifies, per passage, in the colophon.
- **Bereshit Rabbah numbering** differs between the Vilna edition (Sefaria) and Theodor–Albeck. Cite Vilna parashah:section; note the discrepancy once in the editorial intro.
- **PL 113 attributes the Glossa to Walafrid Strabo.** It is not by Strabo. Use Wilson's edition and attribute to the Laon school (Anselm and collaborators), c. 1110–1130.
- **PL column references** are the scholarly citation; Corpus Corporum sometimes drops or shifts them in TEI. Verify a sample against the Migne scan on Internet Archive before trusting them wholesale.
- **Basil in Latin.** The medieval Latin bench read Eustathius' translation (PL 53), not the Greek. NPNF English is of the Greek and will not match the Latin they quote.
- **Origen via Rufinus.** Rufinus edits freely. What the Latin West had is Rufinus' Origen; treat Rufinus as a `transmits` edge, not a transparent window.
- **Do not invent edges.** A shared image is `parallel` until someone shows a citation. The temptation is highest on K7 and K9.
- **Date fields for compiled works** need a range and a precision flag, not a fake year. BR: 400–500, "compilation"; Glossa: 1110–1130, "compilation"; Bavli: 500–600, "redaction". Do not sort a compilation by its earliest tradent.
- **Rashi's sources.** When Rashi says "as the midrash says" the edge target is BR, but the *wording* is often Tanchuma's. Check both before assigning the edge.

---

## 9. Open decisions (author)

1. **Name and imprint.** Working title *Bereshit / In Principio*. Wroot Labs subdomain to confirm.
2. **Lyra and Paul of Burgos.** Lyra is the historical hinge (he read Rashi, and the Glossa travels with him in the printed editions), but he is not in PL. Options: (a) transcribe Gen 1 from a scanned incunable (1492 Venice or 1498 Basel *Biblia cum glossa ordinaria*; Internet Archive / BSB Digital have copies) — a real but bounded job for five verses; (b) omit from pilot and mark as the first Phase 2 witness. Recommend (a): without Lyra the dialogue has no documented Latin reader of Rashi.
3. **Greek-Jewish witnesses.** Include Philo, Josephus, LXX as a third tradition badge, or restrict to Latin-mediated Greek only? Recommend including them: K1, K3, and K4 are half-unintelligible without the LXX and Philo, and all three are PD in English.
4. **Yerushalmi Chagigah 2:1.** No PD English. Translate from Aramaic or omit? Recommend omit from pilot; the Bavli parallel carries the material.
5. **Bavli English.** Fresh translation is the only NC-safe option. Rodkinson (1903) is PD but incomplete and unreliable — confirm whether he covers Chagigah at all before considering him even as a crib. [CHECK]
6. **Crux phrasing.** Questions are currently in a neutral reader's voice. Alternative: phrase each crux as the medieval interpreters would have posed it (*Quare dicitur "dies unus" et non "dies primus"?* / *למה נאמר "יום אחד" ולא "יום ראשון"?*) with the English question beneath. Recommend the bilingual form: it makes the point that the questions themselves were shared.
7. **Bonaventure.** In or out of the pilot? He is on hand (bonaventure.wrootpress.com), II Sent. d.12–13 is squarely on K4/K8/K10, and he is the clearest Latin witness that Augustine's reading was *contested* inside the tradition. Recommend in.
