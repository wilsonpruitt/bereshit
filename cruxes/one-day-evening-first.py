"""K10 — one-day-evening-first (Gen 1:5). Why "one day" and not "first day," and why evening
before morning? Built 2026-09-05 (Phase 2, crux 1 of 9). See PHASES.md for the spec-file contract.

Latin sliced from the local PL TEI by anchor phrase; rabbinic from raw/sefaria/*.json;
Bonaventure from ~/bonaventure-sentences/vol2 (Wilson's edition, Latin + his English).
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, DRAFT, APPROVED, thread, hcut, ecut

CRUX_ID = "one-day-evening-first"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

BON = pathlib.Path.home() / "bonaventure-sentences" / "vol2"

# ---------------------------------------------------------------- scripture-level witnesses
add(id="lxx-1-5", work="lxx", author="lxx-translators", tradition="greek-jewish",
    date=-250, date_precision="circa", place="alexandria",
    anchor={"verse": "gen.1.5"}, lemma={"el": "ἡμέρα μία", "en": "day one"},
    original={"lang": "el", "text": "καὶ ἐκάλεσεν ὁ θεὸς τὸ φῶς ἡμέραν καὶ τὸ σκότος ἐκάλεσεν νύκτα. καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωί, ἡμέρα μία.", "source": "LXX Gen 1:5 (Rahlfs)", "license": "pd"},
    english={"text": "And God called the light Day, and the darkness he called Night. And there was evening and there was morning, one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["translation"],
    answers=["unus-cardinal"],
    notes="The Seventy render the cardinal exactly: ἡμέρα μία, 'day one', not ἡμέρα πρώτη. Every later day in the chapter is an ordinal (δευτέρα, τρίτη), so the Greek preserves the very unevenness the commentators argue about. Brenton's 1851 English prints 'the first day' and dissolves it; this is a fresh draft rather than Brenton for that reason.")

add(id="vulgate-1-5", work="vulgate", author="jerome", tradition="latin",
    date=392, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.5"}, lemma={"la": "dies unus", "en": "one day"},
    original=latin("7204", "Appellavitque lucem Diem", "dies unus.", 28),
    english={"text": "And he called the light Day, and the darkness Night. And there was made evening and morning, one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["translation"],
    answers=["unus-cardinal"],
    notes="Jerome keeps the cardinal against the Latin ear: dies unus, then dies secundus, tertius. Every Latin argument in this crux — Ambrose's, Bruno's, Rupert's — exists because he did not write dies primus. PL 28 prints the text with 'Factumque est vespere et mane, dies unus'.")

add(id="targ-onk-1-5", work="targ-onk", author="onkelos", tradition="rabbinic",
    date=200, date_precision="range-100-300", place="palestine",
    anchor={"verse": "gen.1.5"}, lemma={"arc": "יוֹמָא חָד", "en": "one day"},
    original={"lang": "arc", "text": sef("targ-onk", "he", 4)[0], "source": "Sefaria, 'Onkelos Genesis'", "license": "pd"},
    english={"text": "And the LORD called the light Day, and the darkness he called Night. And there was evening and there was morning, one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["translation"],
    answers=["unus-cardinal"],
    notes="Added at Phase 6. Onkelos was cited twice on this daf — by the Pseudo-Jonathan note and by the answer gloss — and was not on it: the plain targum renders the cardinal exactly, yoma chad, and then yom tinyan for the second day, so the Aramaic preserves the unevenness as the Greek and the Vulgate do — and preserves a second unevenness of its own that no other version has, since yoma chad is determined and yom tinyan is not. It interprets nothing here at all, which is the point: of the three targums only Neofiti ever adds a doctrine, and it does not add one to this verse either. Etheridge's 1862 English, fetched from archive.org for this phase, prints 'Day the First' and then 'the Second Day' — see the Pseudo-Jonathan note; the cardinal is restored here in a fresh draft for the same reason.")

add(id="targ-psj-1-5", work="targ-psj", author="targum-pseudo-jonathan", tradition="rabbinic",
    date=750, date_precision="range-600-800", place="palestine",
    anchor={"verse": "gen.1.5"}, lemma={"arc": "יוֹמָא חָד", "en": "one day"},
    original={"lang": "arc", "text": sef("targ-psj", "he", 4)[0], "source": "Sefaria, 'Targum Jonathan on Genesis'", "license": "pd"},
    english={"text": "And the LORD called the light Day, and made it that the inhabitants of the world might labour in it; and the darkness he called Night, and made it that in it the creatures might have rest. And it was evening, and it was morning, one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["translation", "literal"],
    answers=["unus-cardinal", "night-for-rest"],
    notes="Two things at once. The targum keeps the cardinal, yoma chad, as Onkelos does. And it supplies a reason for the pair that no Hebrew word demands: day is for labour, night for rest. Etheridge's 1862 English prints 'the First Day' — a translator taking the side of the ordinal, exactly as the WEB does — so the cardinal is restored here in a fresh draft. **Corrected at Phase 6**: this was written as though the ordinal were Etheridge's response to the expansive targum. It is not. His Onkelos, fetched from archive.org because Sefaria's Etheridge has no Genesis 1, prints 'Day the First' for the same Aramaic yoma chad, and 'the Second Day' after it — so the ordinal is a habit of the translator applied evenly, not a judgement about this text.")

# ---------------------------------------------------------------- rabbinic bench
br8_he, _, _ = sef("br-3", "he", 7, he_file="br-3-he.json")
br8_en, _, _ = sef("br-3", "en", 7)
# ⛔ These two were `br8_he.find(...)` and `br8_en.find(...)` used directly as slice indices. The
# Hebrew anchor failed on combining-mark order (the documented niqqud trap), find returned -1, and
# the witness shipped from K10 with an original of "." — one character — through Phases 3, 4 and 5
# without check.py or a daf read catching it. Fixed at Phase 6 with the guarded slicers, which raise.
cut8_he = hcut(br8_he, "וַיְהִי עֶרֶב, אֵלּוּ מַעֲשֵׂיהֶן שֶׁל רְשָׁעִים", label="br-3-8 he")
cut8_en = ecut(br8_en, "“It was evening” (Genesis 1:5)", label="br-3-8 en")
add(id="br-3-8", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.5"}, lemma={"he": "יוֹם אֶחָד", "en": "one day"},
    original={"lang": "he", "text": cut8_he, "source": "Bereshit Rabbah 3:8 (Vilna numbering; Theodor–Albeck differs)", "license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"},
    english={"text": cut8_en, "translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True},
    tradents=["r-yannai", "r-tanchum-b-yirmeya", "r-yudan", "r-yochanan", "r-hanina", "r-lulyana"],
    cruxes=["one-day-evening-first"], senses=["allegorical", "literal"],
    answers=["evening-moral", "unus-yom-kippur", "unus-alone"],
    notes="Three answers to 'one day' stacked in one section, and the last of them is the one Rashi will carry into Christendom's reading list. (1) Evening and morning are the deeds of the wicked and of the righteous — the moral reading. (2) 'One day' is the day God gave Israel: the Day of Atonement. (3) R. Yudan: it was the day on which the Holy One was alone (yachid) in his world. That third answer forces the angel question, and the section closes by ruling that on the first day nothing whatever was created besides God — lest anyone say Michael held the sky at the south and Gabriel at the north while God measured in the middle.")

br9_he, _, _ = sef("br-3", "he", 8, he_file="br-3-he.json")
br9_en, _, _ = sef("br-3", "en", 8)
add(id="br-3-9", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.5"}, lemma={"he": "אֶחָד, שֵׁנִי, שְׁלִישִׁי", "en": "one, second, third"},
    original={"lang": "he", "text": br9_he, "source": "Bereshit Rabbah 3:9 (Vilna numbering)", "license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown)"},
    english={"text": br9_en, "translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True},
    tradents=["r-shmuel-b-ami"],
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-grammatical"],
    notes="The grammatical objection in its sharpest rabbinic form: if the days were being tallied it should read 'one, two, three' or 'first, second, third' — is it proper to say 'one, second, third'? The midrash states the difficulty and then answers something else (the ten crowns of the Tabernacle's first day), leaving the grammar standing as a difficulty. Ambrose, Bruno and Rupert answer the identical objection on the Latin side, and nobody on either side cites anybody.")

rashi_he_all = json.load(open(RAW / "rashi-gen-1.json"))
_r_he = [v for v in rashi_he_all["versions"] if v["language"] == "he"][0]["text"][4]
_r_en = [v for v in rashi_he_all["versions"] if v["language"] == "en"][0]["text"][4]
add(id="rashi-1-5", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1080-1105", place="troyes",
    anchor={"verse": "gen.1.5"}, lemma={"he": "יוֹם אֶחָד", "en": "one day"},
    original={"lang": "he", "text": _r_he[0], "source": "Rashi on Gen 1:5, s.v. יום אחד", "license": "pd"},
    english={"text": _r_en[0], "translator": "Rosenbaum–Silbermann 1929–34", "license": "pd"},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-grammatical", "unus-alone"],
    notes="Rashi puts the question in the form the Latin bench uses — by the order of the chapter's own language it should have written 'first day,' as it writes second, third, fourth — and answers it from Bereshit Rabbah 3:8: because the Holy One was then alone (yachid) in his world, the angels not having been created until the second day. Ambrose asks the same question in Latin seven centuries earlier and answers it from the length of a circuit; Bruno of Segni answers it from the logic of relatives. Note that Silbermann's English renders the lemma 'THE FIRST DAY (literally, one day)' — the translator conceding the point the commentary exists to dispute.")

chag_he4, chag_ver, _ = sef("b-chag-12a", "he", 4)
chag_he5, _, _ = sef("b-chag-12a", "he", 5)
chag_en4, chag_enver, _ = sef("b-chag-12a", "en", 4)
chag_en5, _, _ = sef("b-chag-12a", "en", 5)
add(id="b-chag-12a", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.5"}, lemma={"he": "מִדַּת יוֹם וּמִדַּת לַיְלָה", "en": "the measure of the day and the measure of the night"},
    original={"lang": "arc", "text": chag_he4 + " " + chag_he5, "source": "b. Chagigah 12a (Vilna)", "license": "cc-by-sa", "version": chag_ver},
    english={"text": chag_en4 + " " + chag_en5, "translator": "Sefaria Community Translation", "license": "cc0"},
    tradents=["rav-yehuda", "rav"],
    cruxes=["one-day-evening-first", "heaven-earth-order"], senses=["literal"],
    answers=["day-is-a-measure"],
    notes="Rav Yehuda in Rav's name lists ten things made on the first day, and the tenth pair is proof-texted from our verse: the measure of the day and the measure of the night, 'and there was evening and there was morning, one day.' The day's own measure is itself a creature of day one — which is the rabbinic way of answering the question the Latin bench asks as 'what kind of day was it, with no sun?' Hugh of St Victor's dies naturalis is the same instinct in computistical dress.")

chull_he14, chull_ver, _ = sef("b-chull-83a", "he", 14)
chull_he15, _, _ = sef("b-chull-83a", "he", 15)
add(id="b-chull-83a", work="bavli-chullin", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.5"}, lemma={"he": "הַיּוֹם הוֹלֵךְ אַחַר הַלַּיְלָה", "en": "the day follows the night"},
    original={"lang": "arc", "text": chull_he14 + " " + chull_he15, "source": "b. Chullin 83a (Vilna; Mishnah Chullin 5:5 with its gemara)", "license": "cc-by-sa", "version": chull_ver},
    english={"text": "MISHNAH. The 'one day' stated with regard to an animal and its young (Lev 22:28) means that the day follows the night. This is what Ben Zoma expounded: it is said in the work of creation 'one day' (Gen 1:5), and it is said with regard to an animal and its young 'one day'; just as the 'one day' stated in the work of creation means that the day follows the night, so too the 'one day' stated with regard to an animal and its young means that the day follows the night. GEMARA. Our rabbis taught: this is what Ben Zoma expounded. Since the whole passage speaks of nothing but consecrated things, and with consecrated things the night follows the day, one might have thought it is so here too; therefore it is said here 'one day' and it is said in the work of creation 'one day' — just as the 'one day' stated in the work of creation means that the day follows the night, so too the 'one day' stated with regard to an animal and its young means that the day follows the night.", **APPROVED},
    tradents=["ben-zoma"],
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-follows-night"],
    notes="The halakhic weight of the verse, and the flat contradictory of the Latin bench. Ben Zoma — the same tradent who reads merahefet as a measured gap in K7 — ties 'one day' in Lev 22:28 to 'one day' in Genesis by verbal analogy and rules that the day follows the night: reckoning begins at evening. Augustine says in so many words that the days are counted a mane usque in mane; Ambrose says the day has the birthright over the night; Hugh says every dawn belongs to the preceding day. Same five words of Genesis, two calendars. Steinsaltz/Davidson English is CC BY-NC and is not embedded; this is a fresh draft against the Wikisource Aramaic.")

# ---------------------------------------------------------------- latin bench, patristic
add(id="ambrose-hex-1-10", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.5"}, lemma={"la": "Praeclare etiam unum non primum diem dixit", "en": "Excellently, too, he said one day and not first day"},
    original=latin("6958", "Quaerunt aliqui, cur prius vesperum, postea mane Scriptura memoraverit", "Sicut igitur circuitus unus, ita dies unus.", 14),
    english={"text": "Some ask why Scripture recorded evening first and morning afterward, lest it should seem to put night before day. They fail to notice, first, that it put the day first by saying, 'And God called the light Day, and the darkness he called Night'; and then that evening is the end of the day, and morning the end of the night. So, to give the day the prerogative and the birthright, it named the end of the day first, since night was to follow, and afterward added the end of the night. […] Excellently, too, he said one day and not first day. For with a second day and a third and the rest to follow he could have said 'first,' and that seemed to be the order; but he laid down a law, that twenty-four hours of day and night together be defined by the name of day only — as if he were saying: the measure of twenty-four hours is the time of one day. For as the generation of men is counted and the women are understood along with them, since the lesser are bound to the greater, so too the days are numbered and the nights reckoned as joined to them. Therefore as there is one circuit, so there is one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-precedes-night", "unus-24-hours"],
    notes="Ambrose's chapter heading states the crux exactly: 'That day is here set before night, against what seems so to some; why it is called one day rather than first; and that it is closed by a morning end.' His answers are three: evening comes first because evening is the end of the day and morning the end of the night, so naming evening first gives the day its birthright; 'one' rather than 'first' because a day is a single circuit of twenty-four hours; and the day names the night along with it as men name women. He also notes that many call a week 'one day' because it returns into itself. At PL 14:145C he adds a fourth: the day is set apart from the others as 'one,' not compared with them as 'first,' because on it the foundations of all things were laid. Elided in the English at […]: the proof from Scripture's custom of naming the greater term for the pair (Jacob's 'days of my life', Ps 89:10's 'days of our years', never 'and nights'), and the sentence 'Principium ergo diei, vox Dei est: fiat lux.'")

add(id="aug-gnm-1-10", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-389", place="thagaste",
    anchor={"verse": "gen.1.5"}, lemma={"la": "reliqui dies computantur a mane usque in mane", "en": "the remaining days are counted from morning to morning"},
    original=latin("7303", "Et hic calumniantur Manichaei", "sic deinceps reliqui dies computantur a mane usque in mane.", 34),
    english={"text": "Here too the Manichees carp, supposing it was said as though the day began from evening. They do not understand that the whole of that working — by which the light was made, and division was made between light and darkness, and the light was called Day and the darkness Night — that this whole working belongs to the day; and that after this working, the day being as it were finished, evening was made. But because the night also belongs to its own day, the one day is not said to have passed until, the night too being over, morning came: and so thereafter the remaining days are counted from morning to morning.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-precedes-night", "evening-is-completion"],
    notes="Augustine's earliest answer, and the one the Latin bench keeps: the day does not begin at evening. The whole work belongs to the day; evening is what follows a finished day; and the days are counted a mane usque in mane, morning to morning. The Manichees are the named opponents, but the reckoning he rejects is the one Ben Zoma rules for in b. Chullin 83a — the day that follows the night. Neither side knows it is contradicting the other.")

add(id="aug-gnl-1-17", work="aug-gnl", author="augustine", tradition="latin",
    date=401, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.5"}, lemma={"la": "ideoque non dictus est primus, sed unus dies", "en": "and that is why it was called not first but one day"},
    original=latin("7302", "An hic dies totius temporis nomen est", "renovatio ejus significata videatur.", 34),
    english={"text": "Or is this day the name of the whole of time, and does it include all the volumes of the ages under this one word — and is that why it was called not 'first' but 'one day'? For 'and there was evening,' he says, 'and there was morning, one day': so that by the evening's being made the sin of the rational creature may be signified, and by the morning's being made, its renewal.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["allegorical"],
    answers=["unus-all-time", "evening-moral"],
    notes="The one sentence in the Latin bench that puts the rabbis' question and answers it their way: not first but one, because the word holds all time. Augustine raises it and then sets it aside in the next paragraph — 'this is a matter of prophetic allegory, which is not what we undertook in this discourse' — and returns to the literal question. The reading he declines here is the one Abelard will take up as his own, and it is the shape of Bereshit Rabbah 3:8's 'one day' too, though what fills the word there is Yom Kippur and not the ages.")

add(id="aug-gnl-4-22", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.5"}, lemma={"la": "idem dies ubique repetitur", "en": "the same day is repeated throughout"},
    original=latin("7302", "Et quia caeterae creaturae, quae infra ipsam fiunt, sine cognitione ejus non fiunt", "percipiat de Verbo Dei cognitionem creaturae quae post ipsam fit, hoc est firmamenti", 34),
    english={"text": "And because the other creatures, which are made below it, are not made without its knowledge, therefore of course the same day is repeated throughout, so that by its repetition there come to be as many days as there are kinds of created things to be distinguished, to be brought to an end by the perfection of the number six: so that the evening of the first day is its knowledge of itself, that it is not what God is; and the morning after this evening, by which the one day is closed and the second begun, is its turning, by which it refers what it has been created to the praise of the Creator, and receives from the Word of God the knowledge of the creature that is made after it, that is, of the firmament.", **APPROVED},
    cruxes=["one-day-evening-first", "first-light"], senses=["spiritual", "literal"],
    answers=["unus-repeated", "evening-is-self-knowledge"],
    notes="Augustine's mature answer, and the one the Glossa puts in the margin of 1:5 by book, chapter and column. There is only one day: the angelic light itself. Its evening is its knowledge of itself as not-God; its morning is that knowledge referred back in praise; and the six days are that one day presented six times over, once for each kind of thing made. On this reading 'one day' is not a counting word at all, which is why the sixfold repetition does not make it 'first'. Two chapters on (I.25, PL 34:313) he draws the corollary the City of God will state more compactly: this is why no night is ever named.")

add(id="aug-gnl-5-18", work="aug-gnl", author="augustine", tradition="latin",
    date=412, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.5"}, lemma={"la": "illa velut matutina sive diurna cognitione, hac vero velut vespertina", "en": "by that as it were morning or daylight knowledge, and by this as it were evening knowledge"},
    original=latin("7302", "Jam nunc consideremus ea quae fecit Deus omnia simul", "hac vero velut vespertina.", 34),
    english={"text": "Now then let us consider those things which God made all at once, from which, when they were completed on the sixth day, he rested on the seventh — intending afterward to consider his works in which he works even now. […] Of this whole creation of God there is much we do not know: whether things in the heavens too high for our sense to reach them, or things in regions of the earth perhaps uninhabitable, or things hidden below, whether in the depth of the abyss or in the secret folds of the earth. Now these things, before they were made, certainly were not. How then were things known to God which were not? And again, how could he make things that were not known to him? For he made nothing in ignorance. He made them known, then; he did not come to know them once made. Accordingly, before they were made they both were and were not: they were in God's knowledge, they were not in their own nature. And therefore that day was made on which they should become known in both ways, both in God and in themselves: by that as it were morning or daylight knowledge, and by this as it were evening knowledge.", **APPROVED},
    cruxes=["one-day-evening-first", "ex-nihilo-or-matter"], senses=["spiritual"],
    answers=["simul", "evening-is-self-knowledge"],
    notes="The place where the two halves of Augustine's reading are joined and named. 'Creavit omnia simul' (Sir 18:1) makes the six days non-successive; the morning and evening knowledge explains what the day words are then doing. Migne's chapter heading supplies the technical term the schools will quote — cognitio matutina et vespertina. This is the passage Bonaventure will call 'very reasonable and very subtle' and then decline.")

add(id="aug-civ-11-7", work="aug-civ", author="augustine", tradition="latin",
    date=417, date_precision="range-413-427", place="hippo",
    anchor={"verse": "gen.1.5"}, lemma={"la": "nusquam interposuit vocabulum noctis", "en": "nowhere did it insert the word 'night'"},
    original=latin("21364", "Si tamen et vesperam diei hujus et mane aliquatenus congruenter intelligere valeamus", "in cognitione sui ipsius, dies unus est", 41),
    english={"text": "If, that is, we can understand the evening of this day and its morning with any fitness. For the knowledge of the creature, compared with the knowledge of the Creator, in a manner grows dusk; and again it grows light and becomes morning, when that knowledge too is referred to the praise and love of the Creator; nor does it fall away into night, where the Creator is not forsaken through love of the creature. In short, when Scripture numbered those days in order, it nowhere inserted the word 'night.' It nowhere says 'night was made,' but 'evening was made, and morning was made, one day' (Gen 1:5); and so a second day, and the rest. For the knowledge of a creature in itself is, so to speak, more faded than when it is known in the Wisdom of God, as in the art by which it was made. Therefore it can more fittingly be called evening than night; which nevertheless, as I said, when it is referred to the praise and love of the Creator, runs back into morning. And when it does this in the knowledge of itself, it is one day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["spiritual"],
    answers=["unus-repeated", "evening-is-self-knowledge"],
    notes="The City of God's compact restatement, and the one that travels. The observation that carries the argument is a plain fact about the text: through all six days Scripture never once writes 'and night was made.' Evening, yes; night, never. Augustine reads that as evidence that the vespera in question is a dimming of knowledge, not a darkness. Gregory the Great will make the same observation serve a moral reading, and the Glossa prints Gregory's version on 1:5.")

# ---------------------------------------------------------------- latin bench, Carolingian
add(id="bede-gen-1-5", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="circa", place="jarrow",
    anchor={"verse": "gen.1.5"}, lemma={"la": "dies expletus est unus, viginti scilicet et quatuor horarum", "en": "one day was completed, of twenty-four hours"},
    original=latin("8466", "Factumque est vespere et mane dies unus. Factumque est vespere occidente paulatim luce", "in vespera primi unum diceret esse diem perfectum", 91),
    english={"text": "'And there was evening and morning, one day.' There was evening, the light setting little by little after the space of a day's length was spent, and passing beneath the lower parts of the world — which is now done by the accustomed circuit of the sun in the nights; and there was morning, the same light returning little by little over the lands and beginning another day; and up to this point one day was completed, of twenty-four hours, that is. By the commendation of which word Scripture watchfully warns us to learn that the light which was made lit the lower parts of the world by its setting. For if it did not do this, but rather, evening having come, it wholly perished and again little by little revived at morning, it would have said the day was completed not at the morning of the following day but rather at the evening of the first.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-24-hours", "day-precedes-night"],
    notes="Bede reads the phrase as an argument about physics. If the created light had been snuffed out at evening and rekindled at morning, then the day would have been complete at its own evening and Scripture would have said so. That it waits for the morning proves the light went on shining round the underside of the world — the same body of light that later runs the sun's circuit. This is the one place in the crux where the wording of Genesis is treated as evidence for cosmology. Rabanus copies the paragraph verbatim.")

add(id="rabanus-gen-1-5", work="rabanus-gen", author="rabanus", tradition="latin",
    date=822, date_precision="circa", place="fulda",
    anchor={"verse": "gen.1.5"}, lemma={"la": "viginti scilicet et quatuor horarum", "en": "of twenty-four hours, that is"},
    original=latin("8885", "Factumque est vespere et mane dies unus. Factum est vespere, id est, occidente paulatim luce", "in vespera primi, unum diceret esse diem perfectum.", 107),
    english={"text": "'And there was evening and morning, one day.' There was evening, that is, the light setting little by little after the space of a day's length was spent, and passing beneath the lower parts of the world — which is now done by the accustomed circuit of the sun in the nights; and there was morning, the same light returning little by little above the lands and beginning another day; and up to this point one day was completed, of twenty-four hours, that is. By the commendation of which word Scripture watchfully warns us to say that the light which was made lit the lower parts of the world by its setting. For if it did not do this, but rather, evening having come, it wholly perished and again at morning rose up in the thing created, it would have said the day was completed not at the morning of the following day but rather at the evening of the first.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-24-hours", "day-precedes-night"],
    notes="Rabanus copies Bede on 1:5 as he copies Bede on 1:2 — the same silent transmission the K7 threads trace. The Corpus Corporum text differs from Bede's at two words ('dicamus' for 'discamus', 'in re creata resurgeret' for 'recreata resurgeret'); the second looks like a printer's separation of 'recreata' rather than a real variant, and the PL plate should be checked before either is treated as Rabanus' own.")

add(id="alcuin-int-34", work="alcuin-int", author="alcuin", tradition="latin",
    date=796, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.5"}, lemma={"la": "finis operis perfecti, et initium operis incoepti", "en": "the end of a work completed, and the beginning of a work begun"},
    original=latin("21416", "Inter. 33. Quare prima die lux creata legitur?", "et initium operis incoepti.", 100),
    english={"text": "Question 33. Why is the light read as created on the first day? — Answer: It suits the works of God that on the first day a temporal light should first be made from the eternal light, so that there might be something by which the rest he would create could appear. Question 34. What is 'there was evening and morning, one day'? — Answer: That is, the end of a work completed, and the beginning of a work begun.", **APPROVED},
    cruxes=["one-day-evening-first", "first-light"], senses=["literal"],
    answers=["evening-is-completion"],
    notes="Augustine's angelic evening and morning stripped of the angels and reduced to a schoolroom formula: evening is a finished work, morning is a work beginning. Everything that made the doctrine difficult is gone, and what is left will be copied by Wigbod and Angelomus and, through them, become the standard Carolingian gloss on the verse.")

add(id="wigbod-gen-1-5", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="aachen",
    anchor={"verse": "gen.1.5"}, lemma={"la": "ipsa creaturae cognitio in semetipsa vespera erat, in Deo autem mane", "en": "the creature's knowledge of itself was evening; in God, morning"},
    original=latin("8606", "D. Factumque est vespere et mane dies unus (Ibid.) . Quomodo hoc intelligendum est?", "quam in seipsa quae facta est.", 96),
    english={"text": "Disciple: 'And there was evening and morning, one day.' How is this to be understood? — Master: What is evening but the perfecting of each several work, and morning the beginning of those that follow? — AUGUSTINE. Disciple: You maintain that the first day is a spiritual creature; how then did it have evening and morning? — Master: Every creature, before it was made in its own time, was in the Word of God itself, to be known first by the angels and so to be made in its own time. Wherefore the creature's own knowledge of itself was evening; in God, however, morning — because the creature is seen more fully in the Lord than the creature is seen in itself; seen more fully, that is, in the art by which it was made than in itself which was made. For this reason the evangelist John says: 'What was made, in him was life' (John 1:3–4).", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal", "spiritual"],
    answers=["evening-is-completion", "evening-is-self-knowledge"],
    notes="The Carolingian catena doing on 1:5 what it does on 1:2 in K7: setting the two Latin lines side by side and labelling the second one. The schoolroom formula comes first unattributed; then the disciple presses the hard case — if the first day is a spiritual creature, what are its evening and morning? — and the answer is Augustine's angelic double knowledge, printed under his name. This is where a reader of the ninth century could see that the compressed gloss and the difficult doctrine were the same doctrine.")

add(id="angelom-gen-1-5", work="angelom-gen", author="angelomus", tradition="latin",
    date=850, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.5"}, lemma={"la": "propter unitatem angelicae dignitatis", "en": "on account of the unity of angelic dignity"},
    original=latin("9032", "VERS. 5.-- Factumque est vespere et mane dies unus. Quaerendum est cur dicatur", "ut nunquam intuitum amoveat a contemplatione.", 115),
    english={"text": "Verse 5. 'And there was evening and morning, one day.' It must be asked why 'evening and morning' is said, when the sun was not yet in the firmament, by whose setting evening and by whose rising morning would be made. Or did the first and second and third day perhaps have as much space as there is from the rising of the sun to its setting, and again, wheeling by the north, it returns to the east so as to drive off the world's darkness by its brightness — the space which those who are in caves and workhouses, though they lack the light, can feel by habit? Which might perhaps be understood so, were it not that 'evening and morning' is added. So it remains that by evening is understood the perfecting of the preceding work, and by morning the beginning of the one that follows. For Scripture speaks after our manner, so that the distinction of God's works may be understood. Further, what it says, 'evening and morning, one day,' can be referred to the angelic creature. For when it turned its gaze away from God and turned to beholding the creature, in a manner it was evening; but when it turned back to the Creator, so as to understand the creature more clearly in him, it was morning. And yet, if it had remained in the consideration of the creature, it would have been not evening only but night. 'One day' is well added, on account of the unity of angelic dignity, which so clings to contemplating the one God that it never moves its gaze from contemplation.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal", "spiritual"],
    answers=["evening-is-completion", "evening-is-self-knowledge", "unus-angelic-unity"],
    notes="Angelomus splices as he splices in K7: the schoolroom formula first, then Augustine's angelic reading, then a third answer that is his own. 'One day' is well said because of the unity of angelic dignity — the word 'one' is made a predicate of the angels' undivided attention rather than a number in a series. Note also that he keeps Augustine's guard rail: had the angelic mind stayed with the creature it would have been not evening but night, which is why Scripture never writes night.")

add(id="remigius-gen-1-5", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.5"}, lemma={"la": "Per mane initium fidei: per vesperam vero perfectio bonae operationis", "en": "By morning, the beginning of faith; by evening, the perfection of good work"},
    original=latin("9346", "Vers. 5. Factum est vespere et mane dies unus. Per mane initium fidei", "cum initium fidei completione bonae operationis perficitur.", 131),
    english={"text": "Verse 5. 'There was evening and morning, one day.' By morning is understood the beginning of faith; by evening, the perfection of good work. The morning of this day is drawn out into evening when the beginning of faith is perfected by the completion of good work.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["allegorical"],
    answers=["evening-moral"],
    notes="The shortest witness on the crux and the only one that quietly reverses the verse. Remigius reads morning as the beginning and evening as the perfection, so that his day runs from mane to vesperam — the opposite of the order Genesis prints and of the order every other Latin here defends. He is not arguing for a reckoning; the moral figure simply requires that a thing begin before it is completed, and the text is bent to it. Compare Bereshit Rabbah 3:8, where the same moral pairing (wicked and righteous) is fitted to the verse's own order instead.")

# ---------------------------------------------------------------- latin bench, twelfth century
add(id="bruno-gen-1-5", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1100, date_precision="circa", place="segni",
    anchor={"verse": "gen.1.5"}, lemma={"la": "primus et secundus relativa sunt", "en": "'first' and 'second' are relatives"},
    original=latin("21403", "Sequitur: « Factumque est vespere, et mane dies unus. » Vespere et mane noctem et diem quidam intelligunt.", "ipse tamen unus primus dici non poterat.", 164),
    english={"text": "There follows: 'And there was evening and morning, one day.' Some understand evening and morning as night and day. For since it enumerates all the days in order with the nights passed over, they want both day and night to be understood under the one name of day. But the order of speech is astonishing, in which evening is put before morning, as though he had begun to work not from morning but from evening. For if he had said, 'there was morning and evening, one day,' there would perhaps be no question; but because he put evening between two mornings, it can be doubted which of them it is referred to. For if evening is referred to the preceding morning, the whole night is undoubtedly left out; and if to the following, then the whole day is passed over and only the night's boundaries are set. Hence it was more fitting that there should be 'evening and morning, one day' — but it could have been called one night. But since divine providence created the night not for labour but for rest, there is nothing unfitting if in God's working, which was done not in the night but in the day, only the day's boundaries are set. For if in this place we understand the whole space of day and night, as they wish, to be one day, then God divided the two from each other in vain, and gave the divided things different names; for he called the light Day and the darkness Night. No day, therefore, consists of night and day. Since then it is not the dreams that are seen in the night, but the works that are done in it, that are described here, it was necessary to enumerate days and not nights. […] But as for its being said 'one day was made,' and not 'a first day was made,' this holds good because 'first' and 'second' are relatives, and neither can exist without the other. Since therefore there was not yet a second, it was indeed one day; yet that one could not be called first.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-grammatical", "day-precedes-night", "night-for-rest"],
    notes="The best-argued Latin answer on the crux, and the one that most nearly meets Bereshit Rabbah on its own ground. Bruno's is a logician's answer: primus and secundus are relative terms, and a relative cannot stand without its correlate; with no second day yet in existence there was nothing for a 'first' to be first of, so the day could only be called one. He also reaches, independently, the reason Pseudo-Jonathan gives for the night — that providence made it for rest and not for labour — and draws the hard conclusion the others avoid: nulla dies ex nocte constat ac die, no day is made of night and day, because God divided them and named them separately.")

add(id="rupert-gen-1-5", work="rupert-gen", author="rupert", tradition="latin",
    date=1114, date_precision="circa", place="liege",
    anchor={"verse": "gen.1.5"}, lemma={"la": "Quae enim Deus divisit, quomodo conjungi vel unum quid efficere possint?", "en": "For how can things God divided be joined or make one thing?"},
    original=latin("10873", "Notandum hic in primis est quod non dixit: Factaeque sunt tenebrae et lux dies unus.", "sociari vel unum quid efficere non possunt.", 167),
    english={"text": "It is to be noted here first of all that he did not say, 'And there were made darkness and light, one day.' This was well and prudently observed by the sacred writer. For how can the things God divided be joined together, or make some one thing? Now he divided light and darkness, and called the light Day — day, I say, whole and full, without partnership of darkness. […] For, as has been said already, things separated by God's dividing cannot be associated or make some one thing.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-precedes-night", "unus-eternal-day"],
    notes="Rupert's chapter heading is the crux in his own words: 'Why it was not said, there were made darkness and night, a first day, but there was made evening and morning, one day.' His first move is Bruno's conclusion arrived at differently — what God divided cannot be added back together into a single thing, so the 'one day' cannot be day-plus-night. Two columns later (PL 167:217D) he gives his own answer to the ordinal: the truly first day is not this one; and at PL 167:1807A, in the books on the Spirit's works, he states it flatly — the writer knowingly refused to write dies primus, because the day that is first by nature is eternal, and this one is first only by number and by the order of creation. Elided in the English at […]: the sentence the Corpus Corporum text prints as 'Bene ergo dictum est: Factae sunt tenebrae et lux dies unus', which contradicts the sentence it follows and should almost certainly read 'Bene ergo non dictum est'. [CHECK the PL plate before translating it either way.]")

add(id="abelard-hex-1-5", work="abelard-hex", author="abelard", tradition="latin",
    date=1130, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.5"}, lemma={"la": "Diem unum hic vocat totam illorum operum Dei consummationem", "en": "He here calls 'one day' the whole completion of those works of God"},
    original=latin("11118", "Et factum est vespere et mane dies unus. Diem unum hic vocat totam illorum operum Dei consummationem", "in sex diebus consummatum.", 178),
    english={"text": "'And there was evening and morning, one day.' He here calls 'one day' the whole completion of those works of God — held first in his mind, and afterward completed in the work on the sixth day. And the evening of this whole span of time which he here calls one day, he calls that whole working of God according as it first lay hid in his mind, before it came forth into the light through its effect. And again he names that same working morning, according as, being afterward completed in the work, it showed itself visible. Thus he calls the conception of the divine mind, in the disposing of the work to come, evening; and morning he calls the working out of that conception and the effect of the divine disposition, completed in six days.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["spiritual", "literal"],
    answers=["unus-all-time", "evening-is-completion"],
    notes="Abelard takes the reading Augustine raised and set aside: 'one day' names not the first of the days but the whole of them. His evening is the work as it lay hidden in God's mind, his morning the same work made visible — the pair describing the passage from conception to execution rather than any part of a night. He then allows, fairly, that a reader who prefers to refer the phrase to the first day's work alone may do so, 'nihil impedit'. As in K7 he is the Latin most willing to hold two readings and rank them rather than refute one.")

add(id="hugh-sacr-1-5", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.5"}, lemma={"la": "omnis aurora praecedentis diei est", "en": "every dawn belongs to the preceding day"},
    original=latin("11082", "Et propterea quia primus dies auroram praecedentem non habuit", "quod aurora semper ad praecedentem diem referenda sit.", 176),
    english={"text": "And therefore, because the first day had no dawn preceding it — since before the light was created there was full darkness, and as soon as the light appeared over the earth there was full day, and because God's work ought to have begun from what is perfect — therefore Scripture said: 'There was made evening and morning, one day.' For it did not say, 'There was made morning and evening,' but 'There was made,' it says, 'evening and morning, one day.' Because, as we have said, the first day had no morning preceding it, since it took its beginning from full and perfect light; and therefore every dawn belongs to the preceding day, and every day takes its beginning from sunrise. And the natural day is that space of time which, passing from sunrise to sunrise, encloses within itself both night and day; in which — since day naturally precedes night — we call the end of the day evening and the end of the night dawn; and it stands beyond doubt that dawn is always to be referred to the preceding day.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-precedes-night", "unus-24-hours"],
    notes="The computist's answer, stated with the technical vocabulary the schools had by then settled: the dies naturalis runs sunrise to sunrise and holds a night and a day inside it; evening is the end of the day and dawn the end of the night; therefore a dawn always belongs to the day before it. The reason evening is named first is not doctrinal at all but a fact about the first day: it had no dawn to be named, because it began in full light. Hugh's Adnotationes on Genesis (PL 175:35A) argue the same in brief and add a proof from the equinox.")

add(id="honorius-hex-1-5", work="honorius-hex", author="honorius", tradition="latin",
    date=1140, date_precision="circa", place="regensburg",
    anchor={"verse": "gen.1.5"}, lemma={"la": "non primus, sed unus dies dicitur, quia idem semper repetitur", "en": "it is called not first but one day, because the same day is always repeated"},
    original=latin("10991", "Factumque est vespere et mane, dies unus. Vespere est finis diei", "in eodem cuncta consummantur.", 172),
    english={"text": "'And there was evening and morning, one day.' Evening is the end of the day; morning, however, is the end of the night: which two joined together make twenty-four hours and complete one day. And it is called not first but one day, because the same day is always repeated, as it is written: 'By your ordinance the day continues' (Ps 119:91). During that first three days the night remained wholly dark, because neither moon nor stars lit it. It is to be noted, moreover, that the day begins from light and ends in light: because all the works of God are begun from Christ, who is the true light, and in him all are completed.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal", "allegorical"],
    answers=["unus-24-hours", "unus-repeated"],
    notes="By 1140 Augustine's angelic repetition has become a one-clause gloss with a proof text — 'not first but one, because the same day is always repeated' — sitting inside a paragraph of plain computistical arithmetic. The two answers that stand furthest apart in the tradition are here made to agree in a sentence apiece, which is what the twelfth-century handbook does with a contested question. Honorius returns to the verse later in the same work (PL 172:261D) with a wholly different answer: not first but one, because the angelic nature which is called day begins from the eternal day and has no end. [CHECK the work division at PL 172:261 before treating that as a second witness.]")

add(id="comestor-hs-1-5", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.5"}, lemma={"la": "completus est dies unus naturalis", "en": "one natural day was completed"},
    original=latin("11575", "Et factum est vespere, et post factum est mane. Et sic completus est dies unus naturalis.", "exstitit dies unus.", 198),
    english={"text": "'And there was evening, and after that there was morning.' And so one natural day was completed. For first, with heaven and earth, light was created; and as it set little by little, there was made the evening of the first usual day; and as the same light passed under the earth and came to the rising, there was made morning — that is, the night was ended and the second day began. And so, with the light of the day preceding and the night following being ended, one day came to be.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["unus-24-hours", "day-precedes-night"],
    notes="The textbook settles it: dies unus naturalis, light first and night following, on Bede's travelling light. Nothing of Augustine's day survives in the sentence, and the question 'why not first?' is not raised at all — it has been answered so often that the schools' handbook no longer needs to ask. Comestor does keep one older reading a few lines earlier: the division of light from darkness is also the division of the angels, the standing ones light and the fallen ones darkness.")

# ---------------------------------------------------------------- the Glossa and the schools' dissent
_gl_start = "VERS. 5.--"
add(id="glossa-1-5", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.5"}, lemma={"la": "non nox, sed vespera facta memoratur", "en": "not night, but evening is recorded as made"},
    original=latin("8950", "VERS. 5.--. . . . « Factumque est vespere, »", "usque ad ut illud scilicet ad diem pertineat, hoc ad vesperam.", 113),
    english={"text": "Verse 5. […] 'And there was evening,' etc. (GREGORY, Moralia VIII.6.) By no means in this life is sin so forsaken through the exercise of justice that one may remain in it unshaken: for if rectitude drives out the fault, the fault sits at the doors of our thought and knocks to be let in. Whence Moses says: 'Light was made'; and a little after: 'Evening was made.' For the Creator, foreknowing human guilt, then set forth in time what is now enacted in the mind. For the shadow of temptation follows the light of rectitude. But because the light of the elect is not put out by temptation, it is recorded that not night but evening was made: for temptation hides the light of justice, it does not destroy it. (AUGUSTINE, on Genesis to the letter, book IV, ch. 22, 23, vol. III, col. 311, 312.) Note that the other creatures, etc., down to: that the one may belong to the day, and this to the evening.", **APPROVED},
    cruxes=["one-day-evening-first"], senses=["allegorical", "spiritual"],
    answers=["evening-moral", "evening-is-self-knowledge", "unus-repeated"],
    notes="Two glosses only, and between them they carry both Latin answers onto the verse. Gregory the Great supplies the moral one, and he does it by seizing exactly the fact Augustine had seized in City of God XI.7 — that Scripture writes evening and never night — and reading it as consolation: temptation dims the light of justice, it does not extinguish it. Then Augustine's angelic reading is not quoted but cited, by book, chapter and Migne column, and abbreviated in the Glossa's usual way ('etc., usque ad'). A twelfth-century reader of the margin was told where to go and expected to have the book. The English here is a fresh draft; Wilson's edition of the Glossa (migne.app/glossa) supersedes it when it reaches 1:5.")

_bon = (BON / "bon-sent-II-d12-a1-q2.md").read_text().split("\n")
def _bon_slice(lines, cut):
    """Join the given lines of Wilson's edition, drop its page markers, and stop at `cut`
    (the last complete sentence before the paragraph runs on past a page break)."""
    t = re.sub(r"<!--.*?-->", "", "\n\n".join(lines)).strip()
    t = re.sub(r"\*([^*]+)\*", r"\1", t)   # Quaracchi's marginal labels, italic in Wilson's markdown
    t = re.sub(r"[ \t]+", " ", t)
    i = t.find(cut)
    return (t[:i + len(cut)] if i >= 0 else t).strip()
_bon_la = _bon_slice([_bon[68], _bon[70]], "esse distincta in forma.")
_bon_en = _bon_slice([_bon[139], _bon[141]], "were distinguished in form.")

# Phase 6: In II Sent. d.13 a.1 q.2, the Respondeo with both opinions. Footnote markers and the
# bold Respondeo banner are stripped here; _bon_slice's own regex does not remove them.
_bon13 = (BON / "bon-sent-II-d13-a1-q2.md").read_text().split("\n")
def _bon13_clean(lines):
    t = re.sub(r"<!--.*?-->", "", "\n\n".join(lines))
    t = re.sub(r"\[\^\d+\]", "", t).replace("**", "")
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    return re.sub(r"[ \t]+", " ", t).strip()
_bon13_la = _bon13_clean([_bon13[62], _bon13[64], _bon13[66]])
_bon13_en = _bon13_clean([_bon13[126], _bon13[128], _bon13[130]])
assert _bon13_la.startswith("Respondeo:") and _bon13_en.startswith("I respond:"), "d13 a1 q2 line offsets moved"
assert _bon13_la.endswith("quantum ad regressum.") and _bon13_en.endswith("and the return.")
# ---------------------------------------------------------------- Phase 6, second-tier sources
add(id="basil-hex-2-8b", work="basil-hex-lat", author="basil", tradition="latin",
    date=380, date_precision="range-370-380", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.5"}, lemma={"la": "dixit primo vesperam", "en": "he said evening first"},
    original=latin("7608", "Nunc quidem post solis creationem dies appellatur", "nullam facientes noctium mentionem", 53),
    english={"text": "Now indeed, after the creation of the sun, day is the name for air lit by the sun, when it stays in the hemisphere that is above the earth; and night is called the shadowing of the earth, which is produced when the sun is set at its going down. But then day was made, and night followed, not by the motion of the body but by the diffusion of the principal light, now withdrawing itself and now bringing itself back again, according to the divine command. And there was made evening, and there was made morning, one day. The naming of evening, therefore, is to be understood in the common way. For both when the day begins and when it inclines to its setting, night is next to it by its nearness; yet, so as to keep the privileges of the day's birth, he said evening first, saying that night accompanies the day. For before light was created there was no night in the world, but darkness. The shadowing of the earth, then, of which we spoke above, cutting off the day, was called night, and therefore was named with a new name after its coming to be: And so there was made evening, and there was made morning. He did not say day and night, but evening and morning, so as to give the dignity of the word to the better part. For a day touches evening and morning alike, and you will find that Scripture keeps this custom everywhere in numbering times. For we say that so many days have gone by, making no mention of the nights.", **DRAFT},
    cruxes=["one-day-evening-first"], senses=["literal"],
    answers=["day-precedes-night", "unus-cardinal"],
    notes="Added at Phase 6, and it should have been on the daf from the start: this is the passage every later Latin answer to 'why evening first' descends from, and K10's greps did not reach it. Basil, in the Latin of Eustathius, gives the crux its two halves at once. Evening is named first so as to keep the privileges of the day's birth — nativitatis diurnae privilegia — because night accompanies the day and does not precede it; and before light was made there was no night in the world at all, only darkness, so night is a new name for a new thing. Then the second argument, which is about the choice of words: he did not say day and night but evening and morning, to give the dignity of the word to the better part, and Scripture keeps that custom everywhere in counting times. ⚠ The TEI of this column carries at least two plain OCR faults in the space of six lines — suipra for supra, et deo for ideo — which is worth knowing before the variant in the next note is read as a textual fact.")

add(id="bonaventure-sent-2-13-1-2", work="bonaventure-sent", author="bonaventure", tradition="latin",
    date=1252, date_precision="range-1250-1252", place="paris",
    anchor={"verse": "gen.1.5"}, lemma={"la": "duplex est hic modus dicendi: unus secundum doctores Graecos, alter secundum Latinos", "en": "there is a twofold mode of speaking here: one according to the Greek doctors, the other according to the Latins"},
    original={"lang": "la", "text": _bon13_la, "source": "In II Sent., d. XIII, a. 1, q. 2 (Quaracchi 1885, II.315)", "license": "pd", "edition": "Opera Omnia, Tomus II, Quaracchi 1885; text re-set from the plates in ~/bonaventure-sentences"},
    english={"text": _bon13_en, "translator": "wilson-pruitt", "license": "wroot-bonaventure", "edition": "bonaventure.wrootpress.com, In II Sent. d.13 a.1 q.2"},
    cruxes=["one-day-evening-first", "good-and-separated"], senses=["literal"],
    answers=["day-precedes-night"],
    notes="Added at Phase 6. The one witness on either daf that draws the line this site draws, and draws it inside the Latin tradition rather than across it: there is a twofold mode of speaking here, one according to the Greek doctors — Basil, Gregory, Damascene — and the other according to the Latins. The Greeks have the first light make day and night by emitting and drawing back its rays, on the model of the three days' darkness in Egypt, and by divine command rather than by nature; on that reading the division of light from darkness is formal and not local, evening is the progress into privation and morning the regress into habit. The Latins have the light make day and night by its own motion, where the sun now is and out of which the sun was afterwards formed, so that the division is a real one between two hemispheres. Bonaventure prefers the Latins on the ground that it is more possible to natural power. What makes the passage worth its space is that both parties are made to read the same two clauses: Divisit Deus lucem a tenebris and factum est vespere et mane — which are the whole of K9 and the whole of this crux, allotted between the two schools sentence by sentence. ⚠ Anchor note: the argument is on Gen 1:4-5 throughout and quotes both clauses; it is anchored on 1:5 because that is where its conclusion lands.")

add(id="bonaventure-sent-2-12-1-2", work="bonaventure-sent", author="bonaventure", tradition="latin",
    date=1252, date_precision="range-1250-1252", place="paris",
    anchor={"verse": "gen.1.5"}, lemma={"la": "illi dies non fuerunt dies materiales, sed potius spirituales", "en": "those days were not material days but rather spiritual ones"},
    original={"lang": "la", "text": _bon_la, "source": "In II Sent., d. XII, a. 1, q. 2 (Quaracchi 1885, II.296–297)", "license": "pd", "edition": "Opera Omnia, Tomus II, Quaracchi 1885; text re-set from the plates in ~/bonaventure-sentences"},
    english={"text": _bon_en, "translator": "wilson-pruitt", "license": "wroot-bonaventure", "edition": "bonaventure.wrootpress.com, In II Sent. d.12 a.1 q.2"},
    cruxes=["one-day-evening-first", "ex-nihilo-or-matter"], senses=["literal", "spiritual"],
    answers=["simul", "six-days-literal"],
    notes="The moment the Latin tradition decides. Bonaventure sets out Augustine's position fairly and generously — the philosophical way, holding that all things were produced at once and that the days of Genesis were spiritual and could all be simultaneous — and calls it 'very reasonable and very subtle.' Then he declines it, on a ground that is not exegetical but moral: it is safer and more meritorious to submit our reason to Scripture than to twist Scripture to our reason. The common doctors, before Augustine and after, held that all bodies were created at once in matter but distinguished in form through the six days. Augustine's day, the one day repeated, does not survive this paragraph as the school's reading of Genesis 1.")

# ---------------------------------------------------------------- threads
THREADS = [
 # the versions
 E("t-k10-01", "vulgate-1-5", "lxx-1-5", "transmits", "Jerome's 'dies unus' renders the LXX's cardinal ἡμέρα μία, not an ordinal; the whole Latin quarrel over unus and primus rests on a word the Greek had already kept from the Hebrew."),
 E("t-k10-02", "targ-psj-1-5", "lxx-1-5", "parallel", "Aramaic 'yoma chad' and Greek ἡμέρα μία make the same decision independently: keep the cardinal, though every following day in the chapter is an ordinal. Onkelos does the same."),
 E("t-k10-35", "targ-psj-1-5", "targ-onk-1-5", "echoes", "Phase 6. Pseudo-Jonathan keeps Onkelos's yoma chad unaltered and then expands the clause it sits in, giving the day to labour and the night to rest — an expansion of the reason and not of the number. Where the targum that adds most adds nothing to a word, the word was not felt to need help."),
 E("t-k10-37", "ambrose-hex-1-10", "basil-hex-2-8b", "echoes", "Phase 6, and the strongest single edge on the daf. Basil: nox diem comitatur, and evening is named first ut nativitatis diurnae privilegia reservaret. Ambrose, five years later in Milan: evening is the end of the day and morning the end of the night, so 'to give the day the prerogative and the birthright, it named the end of the day first, since night was to follow'. Prerogative and birthright is privilegia and nativitas, in that order, on the same clause. Ambrose is reading Basil's Greek, not this Latin — Eustathius translated a generation after the Hexaemeron of Milan — so the two Latin texts here are independent renderings of one Greek sentence, and every later Latin answer to 'why evening first', Bede's and Bruno's included, comes down from Ambrose's."),
 E("t-k10-38", "bonaventure-sent-2-13-1-2", "basil-hex-2-8b", "cites", "Bonaventure quotes this sentence by name — 'Et Basilius in Hexaëmero' — as the Greek doctors' position, and quotes it with a variant that decides its sense. Quaracchi prints non solaris corporis motu, 'not by the motion of the solar body'; the Patrologia column reads non solum corporis motu, 'not only by the motion of the body'. The first makes Basil deny that the first light moved as the sun does, which is the whole ground of Bonaventure's division into Greeks and Latins; the second makes him concede motion and add diffusion to it, and so dissolves the division. Basil's own context favours Quaracchi — the sentence has just distinguished what happens after the sun's creation from what happened then, when there was no solar body to move — and the same TEI column carries two plain OCR faults within six lines. Reported as a divergence, not adjudicated: neither the Greek nor a second Latin witness was consulted."),
 E("t-k10-39", "bonaventure-sent-2-13-1-2", "bede-gen-1-5", "cites", "The Latin half of Bonaventure's division is Bede, named and quoted: 'Beda autem et alii expositores Latini dicunt, quod diem et noctem faciebat sua revolutione; et hoc habitum fuit in auctoritate prius posita, quae inducitur in littera: Occidente luce paulatim' — the opening words of the Bede witness on this daf. What Bede argued from the behaviour of light, the schools have by the thirteenth century filed as the position of the Latins."),
 E("t-k10-40", "bonaventure-sent-2-13-1-2", "bonaventure-sent-2-12-1-2", "parallel", "Phase 6. The same judgement twice, one distinction apart, and both times against the more spiritual reading on the same ground. At d.12 he grants Augustine's simultaneous days are 'multum rationabilis et valde subtilis' and declines them because Scripture would have to be twisted; at d.13 he grants the Greek doctors their emission and contraction of rays and declines it because the Latin account is 'rationabilior, quia virtuti naturali possibilior'. Reasonableness in the first case is fidelity to the letter, in the second what nature can do — and both times the literal, physical day wins."),
 E("t-k10-36", "targ-onk-1-5", "lxx-1-5", "parallel", "Phase 6. Onkelos's yoma chad and the Seventy's ἡμέρα μία, with yom tinyan and δευτέρα after each: two independent translators out of one Hebrew, and both let the unevenness stand rather than regularise the series. Every Latin argument in this crux descends from a Greek decision that an Aramaic translator had already made on his own."),
 # the rabbinic bench
 E("t-k10-03", "rashi-1-5", "br-3-8", "cites", "Rashi names his source — 'thus it is explained in Bereshit Rabbah' — and reproduces R. Yudan's answer, that God was alone (yachid) in his world, adding the datum that fixes it: the angels were not created until the second day."),
 E("t-k10-04", "br-3-9", "br-3-8", "parallel", "Two consecutive sections of one compilation asking the same thing from opposite ends: 3:8 asks what 'one day' is a name for, 3:9 asks why the series is 'one, second, third' at all. The second states the grammar as an unresolved difficulty."),
 E("t-k10-05", "b-chull-83a", "br-3-8", "parallel", "Both fix a meaning on the words yom echad and neither cites the other: the midrash makes it the day God was alone, the Talmud makes it the rule that reckoning follows the night. The halakhic use is the one that governs practice."),
 E("t-k10-06", "b-chag-12a", "br-3-8", "parallel", "Both list what was made on day one and both must decide whether anything besides God was there. Chagigah counts ten things and includes the measures of day and night from our verse; Bereshit Rabbah rules that nothing at all was created on the first day, so that no partner in creation can be alleged."),
 # Ambrose and the ordinal question
 E("t-k10-07", "ambrose-hex-1-10", "lxx-1-5", "echoes", "Ambrose reads a Latin text that keeps the Greek cardinal and builds his chapter on it: 'Praeclare etiam unum non primum diem dixit.' Without ἡμέρα μία behind the Latin there is no question to ask."),
 E("t-k10-08", "ambrose-hex-1-10", "rashi-1-5", "parallel", "The same question in two languages seven hundred years apart: he could have said 'first,' with a second and third to follow, and that seemed the order — so why 'one'? Ambrose answers from the twenty-four-hour circuit, Rashi from God's solitude. No contact is possible in either direction."),
 E("t-k10-09", "bruno-gen-1-5", "br-3-9", "parallel", "Bereshit Rabbah objects that 'one, second, third' is not a proper series; Bruno answers precisely that objection with the logic of relatives — first and second are correlative terms, and with no second yet in being nothing could be called first. The best-matched pair on the crux, and there is no channel between them."),
 # the Latin reckoning
 E("t-k10-10", "aug-gnm-1-10", "b-chull-83a", "contests", "Augustine: the day does not begin at evening, and 'reliqui dies computantur a mane usque in mane'. Ben Zoma: 'yom echad' in the work of creation means the day follows the night. The same five words of Genesis 1:5 are made to yield two calendars. Neither knows of the other; the contest is real and is in the text."),
 E("t-k10-11", "ambrose-hex-1-10", "aug-gnm-1-10", "parallel", "Both refuse the evening start and both do it by making vespera the end of a completed day rather than the opening of a new one. Ambrose adds the birthright argument, Augustine the Manichean opponent; Augustine was hearing Ambrose preach at Milan in the years before he wrote."),
 E("t-k10-12", "hugh-sacr-1-5", "aug-gnm-1-10", "echoes", "'Omnis dies ab ortu solis initium sumit' with the natural day running sunrise to sunrise is Augustine's 'a mane usque in mane' given the computists' vocabulary; Hugh adds the reason Augustine does not give, that the first day had no dawn to name."),
 E("t-k10-13", "bruno-gen-1-5", "aug-gnm-1-10", "echoes", "Bruno keeps Augustine's conclusion — the day's own boundaries are what Scripture sets, and the night is not counted in — and hardens it into a thesis Augustine never states: nulla dies ex nocte constat ac die."),
 E("t-k10-14", "bruno-gen-1-5", "targ-psj-1-5", "parallel", "'Divina providentia non ad laborem, sed ad quietem noctem creavit' is the reason Pseudo-Jonathan gives in Aramaic for the same pair — the light made that the world's inhabitants might labour, the darkness that the creatures might rest. Neither could have read the other."),
 # Augustine's own line
 E("t-k10-15", "aug-gnl-4-22", "aug-gnl-1-17", "echoes", "The same author's two answers, a decade apart in the same work: in book I 'one and not first' because the word holds all time, offered and set aside as allegory; in book IV 'one' because there is only one day, the angelic light, presented six times over."),
 E("t-k10-16", "aug-gnl-5-18", "aug-gnl-4-22", "echoes", "Book V supplies the name for what book IV describes: the two knowledges become cognitio matutina and vespertina, and the doctrine is tied to 'creavit omnia simul' (Sir 18:1), which is what makes the six days non-successive."),
 E("t-k10-17", "aug-civ-11-7", "aug-gnl-4-22", "echoes", "The City of God restates the Genesis commentary compactly and rests it on the textual observation that carries the argument — Scripture numbers six days and never once writes 'night was made.'"),
 # the Carolingian transmission
 E("t-k10-18", "rabanus-gen-1-5", "bede-gen-1-5", "cites", "Rabanus reproduces Bede's paragraph on the verse almost word for word, including the counterfactual about the light perishing at evening; the same silent copying the K7 threads trace at PL 107:447C."),
 E("t-k10-19", "alcuin-int-34", "aug-gnm-1-10", "echoes", "'Finis operis perfecti, et initium operis incoepti' compresses Augustine's account of evening as a finished work and morning as the next beginning into a single schoolroom answer."),
 E("t-k10-20", "wigbod-gen-1-5", "aug-gnl-4-22", "cites", "Wigbod puts the compressed formula first and then, under the label AUGUSTINUS, the doctrine it came from: the creature's knowledge of itself is evening, its knowledge in God is morning, 'plus videtur in arte qua facta est, quam in seipsa quae facta est.'"),
 E("t-k10-21", "wigbod-gen-1-5", "alcuin-int-34", "parallel", "The two Carolingian question-and-answer books give the same compressed gloss on the verse — evening a work perfected, morning a work begun — in almost the same words; the shared source is Augustine, and neither names him for that sentence."),
 E("t-k10-22", "angelom-gen-1-5", "alcuin-int-34", "echoes", "'In vespera intelligatur perfectio praecedentis operis, et mane inchoatio subsequentis' is the Carolingian formula verbatim, before Angelomus goes on to the angelic reading."),
 E("t-k10-23", "angelom-gen-1-5", "aug-gnl-4-22", "echoes", "The angelic mind turning from God to the creature is evening and turning back is morning; Angelomus keeps Augustine's guard rail — had it stayed with the creature it would have been night — and then adds 'one day' as a name for the unity of angelic dignity, which is his own."),
 E("t-k10-24", "remigius-gen-1-5", "aug-gnl-1-17", "echoes", "Remigius takes the moral reading Augustine had offered and set aside — evening as sin, morning as renewal — and turns it to the ordinary Christian's progress; but he reverses the terms, making morning the beginning and evening the perfection."),
 # the twelfth century and the Glossa
 E("t-k10-25", "glossa-1-5", "aug-gnl-4-22", "cites", "The margin cites 'AUG., de Gen. ad litt., l. IV, c. 22, 23, tom. III, col. 311, 312' and abbreviates the passage with the Glossa's usual 'etc., usque ad' — a pointer to a book the reader is assumed to own, not a quotation."),
 E("t-k10-26", "glossa-1-5", "aug-civ-11-7", "parallel", "Gregory's gloss and Augustine's City of God fasten on the identical textual fact — that Scripture writes evening and never night — and draw different conclusions from it: for Augustine the creature's knowledge dims but does not fall away; for Gregory temptation hides the light of justice but does not destroy it."),
 E("t-k10-27", "honorius-hex-1-5", "aug-gnl-4-22", "echoes", "'Non primus, sed unus dies dicitur, quia idem semper repetitur' is Augustine's repeated day reduced to a clause and given a proof text from Ps 119:91."),
 E("t-k10-28", "honorius-hex-1-5", "ambrose-hex-1-10", "echoes", "'Vespere est finis diei; mane autem finis noctis: quae duo juncta, viginti quatuor horae fiunt' is Ambrose's definition of evening and morning and his twenty-four hours, in the same order."),
 E("t-k10-29", "comestor-hs-1-5", "bede-gen-1-5", "echoes", "The light setting little by little, passing under the earth and coming to the rising, is Bede's travelling light; Comestor names the result dies unus naturalis and drops the argument Bede built it to support."),
 E("t-k10-30", "hugh-sacr-1-5", "ambrose-hex-1-10", "echoes", "Both make evening the end of the day and dawn the end of the night, and both conclude that day naturally precedes night; Hugh adds that the first day had no dawn of its own, which is why evening had to be named first."),
 E("t-k10-31", "abelard-hex-1-5", "aug-gnl-1-17", "echoes", "Abelard adopts as his own reading what Augustine raised and put aside: 'one day' names the whole span of the work, not the first of a series. His evening and morning are the work in God's mind and the work made visible."),
 E("t-k10-32", "rupert-gen-1-5", "bruno-gen-1-5", "parallel", "Two contemporaries reach the same conclusion by different routes: what God divided cannot be recombined into one thing (Rupert), and no day consists of night and day since God named them separately (Bruno). Neither cites the other."),
 # the dissent
 E("t-k10-33", "bonaventure-sent-2-12-1-2", "aug-gnl-5-18", "contests", "Bonaventure states Augustine's simul thesis with its Scriptural support and its account of the days as spiritual and simultaneous, grants that it is 'multum rationabilis et valde subtilis', and then declines it: to hold it, the sense of Scripture must be twisted, and it is safer to submit reason to Scripture than Scripture to reason."),
 E("t-k10-34", "bonaventure-sent-2-12-1-2", "comestor-hs-1-5", "parallel", "The schools' settled reading in its two registers within a century: Comestor simply narrates a natural day and never raises Augustine's question, and Bonaventure raises it in order to rule against it. The literal six days win by handbook and by disputation at once."),
]

FINDING = "The ancient versions all kept the cardinal — ἡμέρα μία, dies unus, yoma chad — and the modern English translations on both benches quietly convert it to the ordinal: the WEB prints 'the first day', Etheridge's targum prints 'the First Day', and Silbermann's Rashi glosses the lemma 'THE FIRST DAY (literally, one day)' in the very note that exists to ask why it is not 'first'. The question the whole crux is made of survives only in the languages nobody now reads it in. Where the two benches do meet, they meet on the grammar: Bereshit Rabbah 3:9 objects that 'one, second, third' is not a proper series, and Bruno of Segni answers exactly that objection with the logic of relatives — first and second are correlatives, and with no second yet in being nothing could be called first. And they part on the calendar: Ben Zoma derives from yom echad that the day follows the night, while Augustine states in so many words that the days are counted a mane usque in mane."

# ---------------------------------------------------------------- persons / places new to this crux
PERSONS = {
 "r-yannai": {"name": "R. Yannai", "dates": "fl. c. 220–250", "tradition": "rabbinic", "role": "tradent"},
 "r-yudan": {"name": "R. Yudan", "dates": "fl. c. 350", "tradition": "rabbinic", "role": "tradent"},
 "r-yochanan": {"name": "R. Yoḥanan bar Nappaḥa", "dates": "c. 180–279", "tradition": "rabbinic", "role": "tradent"},
 "r-hanina": {"name": "R. Ḥanina bar Ḥama", "dates": "d. c. 250", "tradition": "rabbinic", "role": "tradent"},
 "r-tanchum-b-yirmeya": {"name": "R. Tanḥum bar Yirmeya", "tradition": "rabbinic", "role": "tradent"},
 "r-shmuel-b-ami": {"name": "R. Shmuel bar Ami", "tradition": "rabbinic", "role": "tradent"},
 "r-lulyana": {"name": "R. Lulyana bar Tavrai", "tradition": "rabbinic", "role": "tradent"},
 "rav": {"name": "Rav (Abba Arikha)", "dates": "c. 175–247", "tradition": "rabbinic", "role": "tradent"},
 "rav-yehuda": {"name": "Rav Yehuda bar Yeḥezkel", "dates": "c. 220–299", "tradition": "rabbinic", "role": "tradent"},
 "gregory-the-great": {"name": "Gregory the Great", "la": "Gregorius Magnus", "dates": "c. 540–604", "tradition": "latin"},
 "bonaventure": {"name": "Bonaventure", "la": "Bonaventura de Balneoregio", "dates": "c. 1217–1274", "tradition": "latin"},
}
PLACES = {
 "rome": {"name": "Rome", "lat": 41.90, "lon": 12.50},
}

# ---------------------------------------------------------------- answer families new to this crux
ANSWERS = {
 "unus-cardinal": {"label": "The versions keep the cardinal", "gloss": "ἡμέρα μία, dies unus, yoma chad: 'one', not 'first', in every ancient version."},
 "unus-grammatical": {"label": "'First' needs a second", "gloss": "The series 'one, second, third' is improper (Bereshit Rabbah); or, first and second are relatives and there was no second yet (Bruno)."},
 "unus-alone": {"label": "God was alone that day", "gloss": "Yachid in his world: no angels were made on the first day, so there was no second anything (Bereshit Rabbah, Rashi)."},
 "unus-yom-kippur": {"label": "The one day given to Israel", "gloss": "'One day' is the Day of Atonement, the day the Holy One gave them."},
 "unus-24-hours": {"label": "One circuit, twenty-four hours", "gloss": "Day and night together make one revolution, and the whole is named from the day alone."},
 "unus-repeated": {"label": "The same day repeated", "gloss": "There is one day only — the angelic light — presented once for each kind of thing made (Augustine)."},
 "unus-all-time": {"label": "One day = all time", "gloss": "The word holds the whole span of the ages, or the whole work of the six days (Augustine's set-aside reading; Abelard's own)."},
 "unus-angelic-unity": {"label": "The unity of angelic dignity", "gloss": "'One' names the undivided attention of the angelic mind, not a place in a series (Angelomus)."},
 "unus-eternal-day": {"label": "The true first day is eternal", "gloss": "This day is first only by number and order of creation; the day that is first by nature is uncreated light (Rupert)."},
 "day-precedes-night": {"label": "Day before night", "gloss": "Evening is the end of a finished day, morning the end of the night; days are counted from morning to morning."},
 "day-follows-night": {"label": "Night before day", "gloss": "'One day' rules that reckoning begins at evening (Ben Zoma, b. Chullin 83a)."},
 "night-for-rest": {"label": "Night made for rest", "gloss": "Day is for labour and night for rest, so only the day's bounds are counted."},
 "day-is-a-measure": {"label": "The day's measure is a creature", "gloss": "The measure of day and of night was itself made on day one (b. Chagigah 12a)."},
 "evening-is-completion": {"label": "Evening completes a work", "gloss": "Vespera is a work perfected, mane the beginning of the next — the Carolingian formula."},
 "evening-is-self-knowledge": {"label": "Evening and morning knowledge", "gloss": "The creature known in itself is evening; known in the Word and referred back in praise, morning (Augustine)."},
 "evening-moral": {"label": "Evening as sin or temptation", "gloss": "Evening and morning are the deeds of the wicked and the righteous, or sin and renewal, or temptation and the light of justice."},
 "simul": {"label": "All things made at once", "gloss": "Creavit omnia simul (Sir 18:1): the days are not successive."},
 "six-days-literal": {"label": "Six real days", "gloss": "Created at once in matter, distinguished in form through six successive days (the common doctors, Bonaventure)."},
}

LICENSES = {
 "cc0": {"label": "CC0 1.0 (public domain dedication)"},
 "wroot-bonaventure": {
  "label": "Wilson Pruitt's English of Bonaventure, In II Sent. — CC BY 4.0",
  "attribution": "Bonaventure, Commentary on the Sentences, Book II, English by Wilson Pruitt, published at bonaventure.wrootpress.com (Wroot Press). Licensed CC BY 4.0.",
  "note": "Set 2026-09-05 by Wilson's ruling: his own Englishings carry the same licence as the edition, CC BY 4.0, with the colophon linking each back to its published home per the one-translation-one-home rule. Three witnesses: bonaventure-sent-2-12-1-2, bonaventure-sent-2-13-1-1, bonaventure-sent-2-13-1-2 — the third is fresh English of Phase 6 and is credited to the same edition.",
 },
}
SHORT = "Yom echad / dies unus"
