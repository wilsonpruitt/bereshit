"""K1 — beginning-of-what (Gen 1:1). The beginning of what: time, a principle, or a person?
Built 2026-09-05 (Phase 2, crux 2 of 9). See PHASES.md for the spec-file contract.

Latin sliced from the local PL TEI by anchor phrase; rabbinic from raw/sefaria/*.json.
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, DRAFT, thread

CRUX_ID = "beginning-of-what"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

# ---------------------------------------------------------------- scripture-level witnesses
add(id="lxx-1-1", work="lxx", author="lxx-translators", tradition="greek-jewish",
    date=-250, date_precision="circa", place="alexandria",
    anchor={"verse": "gen.1.1"}, lemma={"el": "ἐν ἀρχῇ", "en": "in the beginning"},
    original={"lang": "el", "text": "ἐν ἀρχῇ ἐποίησεν ὁ θεὸς τὸν οὐρανὸν καὶ τὴν γῆν.", "source": "LXX Gen 1:1 (Rahlfs)", "license": "pd"},
    english={"text": "In the beginning God made the heaven and the earth.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["principio-temporis"],
    notes="ἐν ἀρχῇ without an article and without a governing noun: the Greek turns a Hebrew word that may be construct into an adverbial phrase, and in doing so closes off the reading Rashi and Ibn Ezra will call the plain sense. Note also ἐποίησεν, 'made', where the Vulgate will write creavit: the Latin bench's whole argument that creare means to make from nothing has no purchase on the Greek. Every Latin witness here quotes fecit or creavit according to which Latin text is in front of him, and the variation is evidence, not noise.")

add(id="vulgate-1-1", work="vulgate", author="jerome", tradition="latin",
    date=392, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In principio", "en": "In the beginning"},
    original=latin("7204", "In principio creavit Deus", "et terram.", 28),
    english={"text": "In the beginning God created the heaven and the earth.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["principio-temporis"],
    notes="Jerome translates in principio and not in Filio, and in the Hebrew Questions he says in so many words why: the reading 'in the Son' is false as a translation, however true as a sense. But he also writes creavit where the Old Latin his own contemporaries quote has fecit — Augustine, Ambrose, Bede and the Glossa all argue from fecit — so the Latin bench spends seven centuries reasoning about a verse in two versions at once.")

add(id="targ-onk-1-1", work="targ-onk", author="onkelos", tradition="rabbinic",
    date=200, date_precision="range-100-300", place="palestine",
    anchor={"verse": "gen.1.1"}, lemma={"arc": "בְּקַדְמִין", "en": "in former times"},
    original={"lang": "arc", "text": sef("targ-onk", "he", 0)[0], "source": "Sefaria, 'Onkelos Genesis'", "license": "pd"},
    english={"text": "In the beginning the LORD created the heavens and the earth.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["principio-temporis"],
    notes="be-qadmin, a plain adverb of time and nothing else: no construct, no wisdom, no first thing. Onkelos hears the verse as the Greek does. Etheridge's Onkelos did not return from Sefaria by version title (see notes/SOURCES-FINDINGS.md) and the Metsudah English is CC BY-NC, so the English is a fresh draft.")

add(id="targ-psj-1-1", work="targ-psj", author="targum-pseudo-jonathan", tradition="rabbinic",
    date=750, date_precision="range-600-800", place="palestine",
    anchor={"verse": "gen.1.1"}, lemma={"arc": "מִן אַוְולָא", "en": "from the first"},
    original={"lang": "arc", "text": sef("targ-psj", "he", 0)[0], "source": "Sefaria, 'Targum Jonathan on Genesis'", "license": "pd"},
    english={"text": "At the beginning the LORD created the heavens and the earth.", "translator": "J. W. Etheridge, 1862", "license": "etheridge"},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["principio-temporis"],
    notes="A third Aramaic word for the same Hebrew one: min avvela, 'from the first'. Etheridge prints the Aramaic in transliteration inside his English ('At the beginning (min avella)'), which is why his sentence carries a gloss no other version has; the parenthesis is his.")

_neof_he = sef("targ-neof", "he", 0)[0]
_neof_en = sef("targ-neof", "en", 0)[0]
add(id="targ-neof-1-1", work="targ-neof", author="targum-neofiti", tradition="rabbinic",
    date=300, date_precision="range-100-400", place="palestine",
    anchor={"verse": "gen.1.1"}, lemma={"arc": "מלקדמין בחכמה", "en": "from the first, in wisdom"},
    original={"lang": "arc", "text": _neof_he[:_neof_he.find("וית ארעא:") + len("וית ארעא:")], "source": "Targum Neofiti, Gen 1:1 (Vatican, Neofiti 1)", "license": "check", "version": "Sefaria, 'The Vatican Manuscript of the Targum Neofiti' (licence unknown)"},
    english={"text": _neof_en[:_neof_en.find(".") + 1], "translator": "Sefaria Community Translation", "license": "cc0"},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["beginning-is-wisdom"],
    notes="The single most consequential word on this crux: Neofiti does not translate bereshit, it interprets it — min qadmin be-ḥokhmah, 'from the first, in wisdom' — and then adds a second verb, shakhlel, 'and finished'. A Palestinian targumist and the Latin fathers reach the same gloss on the same word, 'in Wisdom', and then part company entirely over what Wisdom is: for Bereshit Rabbah it is the Torah, for Augustine and Bede it is the Son. Neither side knows the other is there. The CC0 English prints 'in great wisdom'; there is no word for 'great' in the Aramaic, and the reading בחוכמתא recorded in the manuscript's own margin is simply the emphatic state. Note that this witness and K7's targ-neof-1-2 are two slices of one Sefaria segment: the whole of Gen 1:1–5 comes back as a single block.")

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "cc-by", "attribution_required": True}

add(id="br-1-1", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "אָמוֹן — אֻמָּן", "en": "amon — artisan"},
    original={"lang": "he", "text": sef("br-1", "he", 0, he_file="br-1-he.json")[0], "source": "Bereshit Rabbah 1:1 (Vilna numbering; Theodor–Albeck differs)", **_BR_SRC},
    english={"text": sef("br-1", "en", 0)[0], **_BR_EN},
    tradents=["r-hoshaya"],
    cruxes=["beginning-of-what"], senses=["allegorical", "literal"],
    answers=["reshit-is-torah", "beginning-is-wisdom"],
    notes="The opening of the whole midrash, and the rabbinic answer to this crux in its classic form. R. Hoshaya reads Proverbs 8:30, 'I was with him as an amon', through four homonyms and then a fifth: amon is uman, artisan. The Torah speaks: I was the tool of the craft of the Holy One. A king does not build a palace out of his own head but from an architect's sheets and tablets; so the Holy One looked into the Torah and created the world. And then the philological hinge on which everything turns — 'reshit is nothing other than the Torah, as it says: The Lord made me reshit of his way' (Prov 8:22). Bereshit therefore means 'by means of the beginning', that is, by the Torah. On the Latin side Augustine, Bede, Bruno and Rupert prove that in principio means 'in Wisdom' from Ps 104:24 [Vg 103], 'you made all things in wisdom'; here the proof text is Prov 8:22 and the Wisdom is the Torah. The two benches share a chapter of Proverbs and a conclusion, and disagree about what the Wisdom is.")

add(id="br-1-4", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "שִׁשָּׁה דְבָרִים קָדְמוּ לִבְרִיאַת הָעוֹלָם", "en": "six things preceded the creation of the world"},
    original={"lang": "he", "text": sef("br-1", "he", 3, he_file="br-1-he.json")[0], "source": "Bereshit Rabbah 1:4 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-1", "en", 3)[0], **_BR_EN},
    tradents=["r-abba-b-kahana", "r-huna", "r-banai", "r-berekhya", "rav-matana"],
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["six-preceded", "reshit-is-torah", "reshit-is-israel", "beginning-is-wisdom"],
    notes="If the world has a reshit, what stands in it? Six things precede the creation: the Torah and the Throne of Glory were actually made, while the patriarchs, Israel, the Temple and the name of the Messiah were contemplated. Every one is proved from a verse containing reshit or a synonym, and the Torah's proof is again Prov 8:22. Then the question the section cannot leave alone — which came first, the Torah or the Throne — and R. Abba bar Kahana rules for the Torah. Two other answers close it out: R. Banai, that the world was created only for the merit of the Torah, quoting Prov 3:19, 'the Lord founded the earth be-ḥokhmah, with wisdom' — the very phrase Targum Neofiti puts into Genesis 1:1 itself; and Rav Huna in the name of Rav Matana, that reshit is ḥalla, tithes and first fruits, which turns the first word of Scripture into a warrant for the priestly dues.")

add(id="br-1-8", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "שֵׁשׁ לְשׁוֹנוֹת שֶׁל קְדִימָה", "en": "six expressions of precedence"},
    original={"lang": "he", "text": sef("br-1", "he", 7, he_file="br-1-he.json")[0], "source": "Bereshit Rabbah 1:8 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-1", "en", 7)[0], **_BR_EN},
    tradents=["r-yehoshua-b-levi", "r-levi"],
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["reshit-is-torah"],
    notes="A small section that shows the machinery. A builder needs six materials, down to the reed he measures with; so the Torah used six words of precedence in Proverbs 8:22–23 — of old, from earliest time, from ancient times, from the beginning, from before, counted as two. The point is that Prov 8 is not a proof text the midrash reaches for occasionally but the passage it treats as Genesis 1:1's own commentary. Ambrose, Augustine and Bede reach for the same chapter of Proverbs by way of the Septuagint's ἔκτισέν με, 'the Lord created me', and spend the fourth century arguing about whether it makes the Son a creature. Neither bench mentions the other's use.")

_rashi = json.load(open(RAW / "rashi-gen-1.json"))
_rashi_he = [v for v in _rashi["versions"] if v["language"] == "he"][0]["text"][0]
_rashi_en = [v for v in _rashi["versions"] if v["language"] == "en"][0]["text"][0]
add(id="rashi-1-1b", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1080-1105", place="troyes",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית בָּרָא", "en": "In the beginning God created"},
    original={"lang": "he", "text": _rashi_he[1], "source": "Rashi on Gen 1:1, s.v. בראשית ברא", "license": "pd"},
    english={"text": _rashi_en[1], "translator": "Rosenbaum–Silbermann 1929–34", "license": "silbermann"},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["reshit-is-torah", "reshit-is-israel", "reshit-construct"],
    notes="Rashi gives both answers and marks which is which. First the received one: the verse cries out to be expounded, and our rabbis expounded it — for the sake of the Torah, called reshit of his way (Prov 8:22), and for the sake of Israel, called reshit of his increase (Jer 2:3). Then, and this is the sentence that changes the history of the verse, 'if you wish to explain it in its plain sense' — reshit is everywhere in Scripture a construct, as in 'in the reshit of the reign of Jehoiakim', so read bereshit bara as though it were bereshit bero, at the beginning of God's creating; the verse is a subordinate clause and the main verb is 'God said, Let there be light.' The chapter is therefore not teaching the order of creation at all, and Rashi proves it from the water, which is already there in verse 2 and whose making is never narrated. Nothing on the Latin bench does this: the Vulgate's in principio is not a construct and cannot be read as one.")

_ie = json.load(open(RAW / "ibn-ezra-gen-1.json"))
add(id="ibn-ezra-1-1", work="ibn-ezra-gen", author="ibn-ezra", tradition="rabbinic",
    date=1155, date_precision="circa", place="lucca",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית — סָמוּךְ", "en": "bereshit — a construct"},
    original={"lang": "he", "text": [v for v in _ie["versions"] if v["language"] == "he"][0]["text"][0][0], "source": "Ibn Ezra on Gen 1:1, s.v. בראשית", "license": "pd", "edition": "Piotrkow, 1907–1911"},
    english={"text": [v for v in _ie["versions"] if v["language"] == "en"][0]["text"][0][0], "translator": "Sefaria Community Translation", "license": "cc0"},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["reshit-construct"],
    notes="The crux conducted purely as grammar, with the theology left out. Ibn Ezra sets down three opinions and refutes each from a counter-example: that the bet is otiose (then it would carry a long qamats); that bereshit is always construct and means 'at the beginning of the evening, or the night' (they forgot Deut 33:21, 'he saw a reshit for himself', where it is absolute); that the bet carries no sense at all and was written only so that no one should think heaven and earth had no beginning. His own view is Rashi's — a construct, like 'in the reshit of the reign of Jehoiakim' — and he answers in advance the objection that a construct cannot govern a finite verb by citing Hos 1:2 and Isa 29:1. Then he stops: 'the meaning will be explained for you at the second verse.' The Latin bench never argues at this level about in principio, because in Latin there is nothing to argue about.")

_ram = json.load(open(RAW / "ramban-gen-1.json"))
def _flat(x): return x if isinstance(x, str) else " ".join(_flat(i) for i in x)
_ram_he = _flat([v for v in _ram["versions"] if v["language"] == "he"][0]["text"][0])
_ram_en = _flat([v for v in _ram["versions"] if v["language"] == "en"][0]["text"][0])
_NIQQUD = re.compile(r"[\u0591-\u05c7]")
def _cut(t, a, b):
    """Slice t between two anchors, matching on the consonantal skeleton: Sefaria's vocalized
    Hebrew and any anchor retyped from a terminal differ in combining-mark order."""
    bare = _NIQQUD.sub("", t)
    back = [k for k, ch in enumerate(t) if not _NIQQUD.match(ch)]
    a, b = _NIQQUD.sub("", a), _NIQQUD.sub("", b)
    i = bare.find(a)
    if i < 0: raise SystemExit(f"K1: start anchor not found: {a!r}")
    j = bare.find(b, i)
    if j < 0: raise SystemExit(f"K1: end anchor not found: {b!r}")
    return t[back[i]:back[j + len(b) - 1] + 1].strip()
add(id="ramban-1-1", work="ramban-gen", author="ramban", tradition="rabbinic",
    date=1267, date_precision="range-1263-1270", place="girona",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית", "en": "In the beginning"},
    original={"lang": "he", "text": _cut(_ram_he, "בְּרֵאשִׁית כָּתַב רַשִׁ", "וְטָעַן בָּזֶה עוֹד טְעָנוֹת."), "source": "Ramban on Gen 1:1, s.v. בראשית", "license": "cc-by", "version": "Sefaria 'Vocalized Edition'"},
    english={"text": _cut(_ram_en, "IN THE BEGINNING. Rashi wrote", "And Rashi raised other objections."), "translator": "Charles B. Chavel, 1971–76", "license": "chavel-ramban"},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["reshit-construct", "world-has-a-beginning"],
    notes="Two centuries after Rashi, the plain-sense reading is refuted from inside the tradition that produced it. Ramban reports Rashi's construct-state argument and Ibn Ezra's version of it — with Ibn Ezra's refinement that the vav of ve-ha'aretz means 'when', so that only light was made on the first day — and then breaks the grammatical premise with two counter-examples: Isa 46:10, 'declaring the end mereshit', and Deut 33:21, 'and he chose reshit for himself', where reshit stands absolute. The Hebrew slice here begins at Ibn Ezra's name and is shorter than the English, which opens at Rashi; the two are aligned on the same argument, not sentence for sentence. Chavel's English shows on Sefaria as CC BY, which is surprising for a 1971 Shilo text: licence key chavel-ramban is marked for checking before publication. Ramban's own answer, that bara names creation from absolute nothing and that the primary matter is what the Greeks call hyle, belongs to K4 and is not sliced here.")

# ---------------------------------------------------------------- latin bench, patristic
add(id="jerome-hq-1-1", work="jerome-hq", author="jerome", tradition="latin",
    date=392, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In filio fecit Deus coelum et terram", "he": "בְּרֵאשִׁית", "en": "In the Son God made heaven and earth"},
    original=latin("7160", "In principio fecit Deus coelum et terram. Plerique", "nomina imponant.", 23),
    english={"text": "In the beginning God made heaven and earth. Very many suppose — as is written also in the Altercation of Jason and Papiscus, and as Tertullian argues in his book against Praxeas, and as Hilary too asserts in his exposition of a certain Psalm — that the Hebrew has: 'In the Son God made heaven and earth.' That this is false, the truth of the thing itself proves. For both the Seventy Translators and Symmachus and Theodotion rendered 'in the beginning'; and in the Hebrew it is written BRESITH, which Aquila translates 'in the head', and not BABEN, which is rendered 'in the son'. It can therefore be taken of Christ rather according to the sense than according to the translation of the word: he who, both at the very forehead of Genesis, which is the head of all the books, and also at the beginning of John the Evangelist, is shown to be the founder of heaven and earth. Whence also in the Psalter he says of himself: 'In the head of the book it is written of me' (Ps 40:8 [Vg 39:9]) — that is, in the beginning of Genesis. And in the Gospel: 'All things were made through him, and without him was made nothing' (John 1:3). But this too is to be known, that among the Hebrews this book is called BRESITH: they have the custom of giving volumes their names from their opening words.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation", "literal", "allegorical"],
    answers=["principio-in-filio", "bereshit-book-name"],
    notes="The pivot of the Latin side of this crux, and it goes against the Latin side. Jerome names three authorities who had said the Hebrew reads 'in the Son' — the lost Altercation of Jason and Papiscus, Tertullian, Hilary — and refutes them from the languages: the three Greek versions all have 'in the beginning', the Hebrew word is bresith, which Aquila renders ἐν κεφαλαίῳ, 'in the head', and the Hebrew for 'in the son' would be ba-ben, which is not what is written. Then the concession that is quoted for the next seven hundred years while the refutation is not: it may still be taken of Christ 'according to the sense rather than the translation of the word', because Genesis and John begin alike. Aquila's in capitulo is rendered 'in the head' here to keep Jerome's pun working — capitulum is what lets him bind bresith to caput librorum and to Ps 40:8's in capite libri. Wigbod reproduces this passage almost entire and drops the refutation.")

add(id="ambrose-hex-1-2", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "vel ipsum esse initium universorum", "en": "or that he himself is the beginning of all things"},
    original=latin("6958", "Unde divino spiritu praevidens sanctus Moyses", "quam indicium coeptae explicuisset.", 14),
    english={"text": "Whence holy Moses, foreseeing by the divine Spirit that these errors of men would come, and had perhaps already begun, speaks thus at the opening of his discourse: 'In the beginning God made heaven and earth' (Gen 1:1) — comprehending the beginning of things, the author of the world, and the creation of matter; so that you might know that God is before the beginning of the world, or that he himself is the beginning of all things, as in the Gospel the Son of God answered those who said to him 'Who are you?': 'The Beginning, who also speak to you' (John 8:25); and that he himself gave a beginning to the things to be brought forth, and that he himself is the creator of the world, not an imitator of matter with some idea for his guide, out of which he would shape his works, not at his own will, but to a form set before him. Beautifully too he says 'in the beginning he made', so as to express the incomprehensible speed of the work, since he set forth the effect of the operation completed before any sign of its being begun.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-in-filio", "principio-temporis", "world-has-a-beginning"],
    notes="Ambrose gets all three answers into one sentence and does not choose between them. 'In the beginning' comprehends at once the beginning of things, the author of the world and the creation of matter; God is before the beginning of the world, 'or he himself is the beginning of all things' — and that vel is doing the work, because it holds the temporal and the personal readings side by side without ranking them. The Son's self-naming at John 8:25 is quoted here for the first time in the Latin bench, and after Ambrose no witness on this crux argues without it: Augustine, Isidore, Bede, Rabanus, Bruno, Rupert and Isidore's ecclesial allegory all rest on the same verse. Ambrose's word throughout is initium, not principium; the Vulgate's word had not yet displaced the Old Latin he preached from.")

add(id="ambrose-hex-1-3", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "cognoscerent principium esse mundi", "en": "that they might know the world has a beginning"},
    original=latin("6958", "In principio, inquit. Quam bonus ordo", "sensum temporis praeveniret.", 14),
    english={"text": "'In the beginning,' he says. What a good order — that he should assert first the very thing they are accustomed to deny, and that they might know the world has a beginning, lest men should think the world is without a beginning. Whence David also, when he was speaking of heaven and earth and sea, said, 'You have made all things in wisdom' (Ps 104:24 [Vg 103:25]). He gave the world a beginning, then, and gave the creature weakness too, lest we should believe it uncaused, uncreated, and a partaker of the divine substance. And beautifully he added 'he made', lest it be supposed there was any delay in the making; that in this way at least men might understand how incomparable a workman he is, who completed so great a work in the brief and slender moment of his operating, so that the effect of his will outran the sense of time.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["world-has-a-beginning", "beginning-is-wisdom"],
    notes="The other Latin answer, and the polemical one: the beginning is the world's own, and the point of saying so is that the world is not eternal — anarchon, uncaused, a sharer in the divine substance. Remigius will make this the whole content of the verse and name Plato and Aristotle as the opponents; Ramban, from the other bench, says the same thing in the same place, that whoever thinks the world eternal 'denies the essential principle and has no Torah at all'. Note the proof text: Ps 104:24, 'you have made all things in wisdom' — the verse the Latin bench uses to get from in principio to in Sapientia, and so to the Son. The rabbinic bench gets to wisdom from Prov 8:22 and Prov 3:19 and arrives at the Torah.")

add(id="aug-gnm-1-2", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="circa", place="thagaste",
    anchor={"verse": "gen.1.1"}, lemma={"la": "non in principio temporis, sed in Christo", "en": "not in the beginning of time, but in Christ"},
    original=latin("7303", "Quod scriptum est, In principio fecit Deus coelum et terram, quaerunt", "non potest inveniri tempus quo Deus nondum fecerat coelum et terram.", 34),
    english={"text": "As to what is written, 'In the beginning God made heaven and earth', they ask, in what beginning; and they say: If God made heaven and earth in some beginning of time, what was he doing before he made heaven and earth? And why did it suddenly please him to make what he had never made before through eternal ages? To these we answer that God made heaven and earth in the beginning not in the beginning of time, but in Christ, since the Word was with the Father, through whom and in whom all things were made (John 1:1, 3). For our Lord Jesus Christ, when the Jews had asked him who he was, answered: 'The Beginning, because I also speak to you' (John 8:25). But even if we do believe that God made heaven and earth in the beginning of time, we ought certainly to understand that before the beginning of time there was no time. For God made the times too; and therefore before he made the times, there were no times. We cannot then say that there was some time when God had not yet made anything. For how was there a time that God had not made, since he himself is the fashioner of all times? And if time began together with heaven and earth, no time can be found in which God had not yet made heaven and earth.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-in-filio", "principio-temporis"],
    notes="Augustine's earliest answer, given under pressure. The Manichaean objection is not about grammar but about God's idleness — what was he doing before? — and Augustine takes the shortest road out: the beginning is not a time at all, it is Christ. Then, in the second half, he grants the temporal reading anyway and disarms the objection a second way, by making time itself a creature, so that there is no 'before'. Both moves survive him: the Christological one becomes the Latin commonplace, and the argument that time began with the world is what Rabanus compresses to 'time is from this world, not before the world', and Hugh of St Victor restates as 'in the first beginning of time, or rather with the beginning of time itself'.")

add(id="aug-gnl-1-1", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "utrum in principio temporis; an quia primo omnium facta sint; an in principio, quod est Verbum Dei", "en": "whether in the beginning of time; or because they were made first of all; or in the beginning which is the Word of God"},
    original=latin("7302", "Si ergo utroque modo illa Scriptura scrutanda est", "quod est Verbum Dei unigenitus Filius.", 34),
    english={"text": "If, then, that Scripture is to be searched in both ways, let us ask how it was said, apart from the allegorical signification, 'In the beginning God made heaven and earth': whether in the beginning of time; or because they were made first of all; or in the beginning which is the Word of God, the only-begotten Son.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["principio-temporis", "principio-first-of-all", "principio-in-filio"],
    notes="The crux stated as a crux, by the man who made it one. Three readings, set out in a single sentence at the head of the literal commentary and deliberately not decided: in the beginning of time, first of all things, or in the Word. Everything else on the Latin bench is an attempt at one of these three, and Peter Comestor's twelfth-century settlement — read the phrase twice, once for the Son and once for time — is a refusal to choose between the first and the third. The one possibility Augustine does not list is the one Rashi will make the plain sense: that bereshit is a construct and the sentence is subordinate. Latin cannot raise it.")

add(id="aug-gnl-imp-2-6", work="aug-gnl-imp", author="augustine", tradition="latin",
    date=393, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Est enim Principium sine principio, et est Principium cum alio principio", "en": "For there is a Beginning without a beginning, and a Beginning with another beginning"},
    original=latin("7310", "Hoc ergo quod scriptum est, In principio fecit Deus coelum et terram, quaeri potest", "ita Creatori creatura subnectitur.", 34),
    english={"text": "This, then, that is written, 'In the beginning God made heaven and earth', may be asked about: whether it is to be taken only according to history, or whether it also signifies something figuratively, and how it agrees with the Gospel, and for what cause this book was begun so. According to history it is asked what 'In the beginning' is — that is, whether in the beginning of time, or in the beginning which is the very Wisdom of God, since the Son of God also called himself the beginning, when it was said to him, 'Who are you?', and he said, 'The Beginning, who also speak to you' (John 8:25). For there is a Beginning without a beginning, and there is a Beginning with another beginning. The Beginning without a beginning is the Father alone, and therefore we believe all things to be from one beginning; but the Son is a Beginning in such a way as to be from the Father. The first intellectual creature itself can also be called a beginning to those things of which it is the head, which God made. For since a head may rightly be called a beginning, in that gradation the Apostle nevertheless did not call the woman the head of anything. For he called the man the head of the woman, and Christ the head of the man, and God the head of Christ (1 Cor 11:3): so is the creature bound beneath the Creator.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-in-filio", "principio-temporis", "principio-is-first-creature"],
    notes="The unfinished commentary is where Augustine works out what 'beginning' can mean before he decides what it means here, and the distinction he coins is exact: a Beginning without a beginning (the Father) and a Beginning that has another beginning (the Son, who is from the Father). Then a third possibility that no one else on this crux takes up: the first intellectual creature is a beginning to the things it heads, so 'in the beginning' might name the angelic creation. Bereshit Rabbah 1:4's list of six things that preceded the world is doing something formally similar — populating the beginning with a created thing — and reaches the Torah and the Throne of Glory instead.")

add(id="aug-conf-11-9", work="aug-conf", author="augustine", tradition="latin",
    date=398, date_precision="range-397-401", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In hoc Principio, Deus, fecisti coelum et terram", "en": "In this Beginning, God, you made heaven and earth"},
    original=latin("7270", "In hoc Principio, Deus, fecisti coelum et terram", "quis enarrabit?", 32),
    english={"text": "In this Beginning, God, you made heaven and earth: in your Word, in your Son, in your Strength, in your Wisdom, in your Truth, speaking in a wondrous way and in a wondrous way making. Who shall grasp it? who shall tell it?", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical", "spiritual"],
    answers=["principio-in-filio", "beginning-is-wisdom"],
    notes="Two sentences, and the crux's Latin answer at its highest pitch: the Beginning is named five times over — Word, Son, Strength, Wisdom, Truth — and the naming is prayer, not argument. This is also the clearest place to see how close the two benches come without touching. 'In your Wisdom you made heaven and earth' is, as a sentence, what Targum Neofiti prints as the text of Genesis 1:1, and what Prov 3:19 says in the mouth of R. Banai at Bereshit Rabbah 1:4. Augustine is confessing to the second person of the Trinity; Neofiti is translating a Hebrew word; R. Banai means the Torah.")

add(id="aug-civ-11-32", work="aug-civ", author="augustine", tradition="latin",
    date=417, date_precision="range-413-427", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "ut Pater fecisse intelligatur in Filio", "en": "so that the Father is understood to have made in the Son"},
    original=latin("21364", "Cum enim ita dicitur, In principio fecit Deus coelum et terram", "superferebatur super aquam (Gen. I, 1-3) .", 41),
    english={"text": "For when it is said thus, 'In the beginning God made heaven and earth', so that the Father is understood to have made in the Son — as the Psalm bears witness, where it reads, 'How magnified are your works, O Lord! you have made all things in wisdom' (Ps 104:24 [Vg 103:24]) — most fittingly a little after the Holy Spirit also is mentioned. For when it had been said what kind of earth God first made, or what mass and matter he had called by the name of heaven and earth for the construction of the world to come, by subjoining and adding, 'But the earth was invisible and unformed, and darkness was over the abyss', at once, that the mention of the Trinity might be completed, 'And the Spirit,' he says, 'of God was borne above the water' (Gen 1:1–3).", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical"],
    answers=["principio-in-filio", "beginning-is-wisdom"],
    notes="The mature statement of the same reading, and the one that shows the machinery: 'in the beginning' means 'in the Son' because Ps 104:24 says all things were made in wisdom, and Wisdom is the Son. That is an inference through a proof text, not a philological claim, and Jerome had already ruled out the philological claim. The witness is here rather than under K3 because the argument turns on what in principio names; the Trinitarian reading of the whole opening belongs with elohim-and-trinity.")

add(id="isidore-quaest-1-1", work="isidore-quaest", author="isidore", tradition="latin",
    date=630, date_precision="circa", place="seville",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Principium Christus est", "en": "The Beginning is Christ"},
    original=latin("21433", "In principio fecit Deus coelum et terram. Principium Christus est", "qui necdum terrenum hominem deposuerunt.", 83),
    english={"text": "'In the beginning God made heaven and earth.' The Beginning is Christ, as he himself answered in the Gospel to the Jews when they questioned him: 'I am the Beginning, who also speak to you' (John 8:25). In this beginning, therefore, God made heaven — that is, the spiritual, who meditate on and seek heavenly things; and in him he made the carnal also, who have not yet laid aside the earthly man.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical", "spiritual"],
    answers=["principio-in-filio"],
    notes="What the Christological reading becomes once it is settled: not an argument but a premise, and one that immediately turns ecclesial. Isidore states 'the Beginning is Christ' flatly, with John 8:25 and no discussion, and then reads heaven and earth as two kinds of Christian, the spiritual and the carnal. The Glossa's Mystice paragraph on this verse does the same thing in the same words four centuries later. Isidore's Quaestiones announce at the head that the historical sense has been read and the spiritual is what they are for, so the absence of argument is a genre, not a lapse.")

# ---------------------------------------------------------------- latin bench, insular and carolingian
add(id="bede-gen-1-1", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="range-717-725", place="jarrow",
    anchor={"verse": "gen.1.1"}, lemma={"la": "in principio temporum … in Unigenito Filio suo", "en": "in the beginning of times … in his Only-begotten Son"},
    original=latin("8466", "Creationem mundi insinuans Scriptura divina", "respondit: Principium quod et loquor vobis (Joan. VIII, 25) .", 91),
    english={"text": "Divine Scripture, in intimating the creation of the world, aptly shows in its very first word the eternity and omnipotence of God the creator. For him whom it declares to have created the world in the beginning of times, it thereby designates as having existed eternally before times. And him whom it relates to have created heaven and earth at the very outset of the founding, it declares to be omnipotent in so great a speed of operation, for whom to have willed is to have done. For when human frailty makes anything — when, for instance, we build a house — at the beginning of the work we prepare the material, and after that beginning we dig deep, then we lay stones in the foundation, then we set up the walls with courses of stone rising, and so little by little we come to the completion of the work proposed. But God, whose hand is omnipotent to accomplish his work, needed no delay of times, because it is written: 'Whatever he willed, he did' (Ps 115:3 [Vg 113B:3]). Whence it is well pleasing that in the beginning God created heaven and earth, so that it may be plainly understood that both were made by God at once, although both cannot be said at once by a man. And then the prophet says: 'In the beginning, Lord, you founded the earth' (Ps 102:25 [Vg 101:26]); but here the Lord is related to have created heaven and earth in the beginning; whence it is plainly gathered that the making of both elements was completed together, and this with such swiftness of divine power that not even the first moment of the world's birth had been passed. It can also be understood, not improbably, that God made heaven and earth in the beginning in his Only-begotten Son, who answered the Jews when they asked what they should believe him to be: 'The Beginning, who also speak to you' (John 8:25).", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-temporis", "principio-in-filio", "world-has-a-beginning"],
    notes="Bede takes Augustine's three readings and orders them: the temporal one first and at length, the Christological one last and hedged — 'not improbably'. In between comes the argument the whole Carolingian line will repeat, that in principio proves the two were made at once, since a man cannot say two words at once but God can do two things at once, and Ps 102:25's 'in the beginning you founded the earth' names the earth where Genesis names heaven first. This paragraph is the single most-copied piece of Latin on the crux: Rabanus reproduces it almost entire, the Glossa cuts it into three marginal glosses, and Remigius takes over its empyrean heaven word for word.")

add(id="alcuin-int-26", work="alcuin-int", author="alcuin", tradition="latin",
    date=800, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In Filio perfecit Deus coelum et terram", "en": "In the Son God completed heaven and earth"},
    original=latin("21416", "Inter. 26. Quid est: In principio creavit Deus coelum et terram?", "In Filio perfecit [ Ms., fecit] Deus coelum et terram?", 100),
    english={"text": "Question 26. What is: 'In the beginning God created heaven and earth'? — Answer. In the Son God completed [ms.: made] heaven and earth.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical"],
    answers=["principio-in-filio"],
    notes="The whole crux in eleven words, question and answer, with nothing left of the argument. Jerome had denied that the Hebrew says 'in the Son'; Augustine had offered it as one of three; Bede had called it not improbable. In the Carolingian schoolroom it is simply the answer, and it is the answer a boy memorises. The Glossa will later print exactly this — a single word, Filio — as its own gloss on in principio, under Alcuin's name. Migne prints perfecit with a manuscript variant fecit; the variant is kept in the English in brackets because the choice is not indifferent, perficere making the Son the completion of the work and facere merely its instrument.")

add(id="wigbod-gen-1-1", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="aachen",
    anchor={"verse": "gen.1.1"}, lemma={"la": "secundum sensum magis quam secundum verbi translationem, de Christo accipi potest", "en": "it can be taken of Christ according to the sense rather than the translation of the word"},
    original=latin("8606", "D. Genesis unde hoc nomen accepit?", "ex principibus eorum nomina imponant.", 96),
    english={"text": "D. Whence did Genesis take this name? — M. For the Seventy Translators, Symmachus and Theodotion rendered 'in the beginning', and in the Hebrew it is written Bresith, which Aquila translates 'in the head'. And therefore it can be taken of Christ according to the sense rather than according to the translation of the word: he who, both at the very forehead of Genesis, which is the head of all the books, and at the beginning of John the Evangelist, is shown to be the founder of heaven and earth. Whence also in the Psalter he says of himself: 'In the head of the book it is written of me' (Ps 40:8 [Vg 39:8]) — that is, in the beginning of Genesis. And in the Gospel, 'All things were made through him, and without him was made nothing' (John 1:3). Therefore it is to be known that this book is called Bresith among the Hebrews, they having the custom of giving volumes their names from their opening words.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation", "allegorical"],
    answers=["principio-in-filio", "bereshit-book-name"],
    notes="A Carolingian catena copying Jerome, and the copying is the finding. Wigbod reproduces the Hebrew Questions on this verse almost word for word — the three Greek versions, Bresith, Aquila's 'in the head', the forehead of Genesis, Ps 40:8, John 1:3, the Hebrew custom of naming books from their openings — and drops exactly two things: the list of authorities who said the Hebrew reads 'in the Son', and Jerome's refutation of them, including the decisive philological sentence that the Hebrew for 'in the son' is ba-ben and is not what is written. What survives is the concession without the correction, and Wigbod reaches it under a question about the book's title rather than about the verse. The K7 threads found him doing the same thing to Jerome on 1:2 under the label HIERONYMUS; here he does not name Jerome at all. Migne's ex principibus is a misprint for Jerome's ex principiis.")

add(id="rabanus-gen-1-1b", work="rabanus-gen", author="rabanus", tradition="latin",
    date=822, date_precision="range-819-822", place="fulda",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Tempus enim ab hoc mundo, non ante mundum", "en": "For time is from this world, not before the world"},
    original=latin("8885", "In principio itaque temporis, coelum et terram Deus fecit", "condita sunt omnia in coelis et terra (Coloss. I)", 107),
    english={"text": "In the beginning of time, therefore, God made heaven and earth. For time is from this world, not before the world; and a day is a portion of time, not its beginning. But God, whose hand is omnipotent, needed no delay of times to accomplish his work, because, as it is written, 'Whatever he willed, he did' (Ps 115:3 [Vg 113B:3]). Whence it is well said that in the beginning God created heaven and earth, so that it may be plainly understood that both were made by him at once, although both cannot be said at once by a man. And then the prophet says: 'In the beginning, Lord, you founded the earth' (Ps 102:25 [Vg 101:26]); but here the Lord is related to have created heaven and earth in the beginning. Whence it is plainly gathered that the making of both elements was completed together, and this with such swiftness of divine power that not even the first moment of the world's birth had been passed. It can also be understood, not improbably, that God made heaven and earth in the beginning in his Only-begotten Son, who answered the Jews when they asked what they should believe him to be: 'The Beginning, who also speak to you' (John 8:25); because in him, as the Apostle says, 'all things were created in the heavens and on the earth' (Col 1:16).", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-temporis", "principio-in-filio"],
    notes="Bede's paragraph again, taken over silently and unattributed, exactly as the K7 threads found at PL 107:447C and the K10 threads at 448D — but with a sentence in front of it that is not Bede's and that answers the crux more sharply than Bede does: 'in the beginning of time, therefore, God made heaven and earth. For time is from this world, not before the world; and a day is a portion of time, not its beginning.' Rabanus also drops Bede's long house-building simile and keeps everything after it. This is the Carolingian method visible in one paragraph: an inherited exposition, silently abridged, with the compiler's own thesis set at its head. On the id: K7 already holds a witness called rabanus-gen-1-1 which is in fact on Gen 1:2, so this one takes the b suffix (see notes/SOURCES-FINDINGS.md).")

add(id="angelom-gen-1-1", work="angelom-gen", author="angelomus", tradition="latin",
    date=845, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Unde Bresith Hebraice, Latine non immerito Genesis interpretatur", "en": "whence Bresith in Hebrew is not undeservedly rendered Genesis in Latin"},
    original=latin("9032", "libet inquirere quare volumen istud specialiter Genesis vocetur", "generatione hominum animantiumque narratur.", 115),
    english={"text": "It is worth asking why this volume is called Genesis in particular, since many things are recorded in it which are known not to pertain to generation — unless it be that the Hebrews have the custom of imposing the names of books from their openings, as Exodus and many others are named. Whence Bresith in Hebrew is not undeservedly rendered Genesis in Latin: because in its very opening the creation of heaven and earth, and the generation of men and living creatures, is narrated.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["translation"],
    answers=["bereshit-book-name"],
    notes="Jerome's last remark on the verse, promoted to the first question of a commentary. Angelomus keeps the Hebrew custom of naming books from their first words and draws from it a conclusion Jerome did not: that Bresith is properly rendered Genesis, because what stands at the opening is generation. The Latin bench thus ends by treating the crux word as the title of a book rather than as a word in a sentence. The rabbinic bench never loses the sentence, because for it the word governs what follows — either the Torah, by which God created, or, in Rashi's plain sense, the clause 'when God began to create'.")

add(id="remigius-gen-1-1", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In principio, et subauditur: temporis", "en": "'In the beginning' — and 'of time' is understood"},
    original=latin("9346", "In principio hujus voluminis philosophi confutantur", "tunc tempus coepisse quod antea minime erat.", 131),
    english={"text": "At the beginning of this volume the philosophers are refuted, who tried to argue about the creation of the world: Plato, for instance, who said there were three principles, namely God, the exemplar, and matter, and that God did not create all things from nothing as their author, but that matter furnished help to him as to a workman in the making of things. Aristotle said there were two principles, namely matter and form, and something third which he wished to call, I know not what, the operative. Opposing their errors, Moses, as chosen by God, is said to have shown the truth, showing that God formed all things at once out of nothing — not indeed in time, but at the beginning of time, saying 'In the beginning', with 'of time' understood; whence it is beyond doubt that time then began, which before was not at all.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["principio-temporis", "world-has-a-beginning"],
    notes="Remigius makes the temporal reading do the polemical work Ambrose gave it, and does the crux's grammar out loud: 'In principio, and of time is understood' — a supplied genitive, which is what every Latin reader is doing silently. The named opponents are Plato with his three principles and Aristotle with his two, and the distinction he needs is not in time but at the beginning of time. His neighbour on the rabbinic bench is Bereshit Rabbah 1:9, where a philosopher tells Rabban Gamliel that God is a great artisan who found good materials to hand and is told the list of them is a list of things created — the same refutation of the same philosophy, on the same verse, with the same absence of contact. That section is K4's.")

# ---------------------------------------------------------------- the Glossa and the twelfth century
add(id="glossa-1-1", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.1"}, lemma={"la": "« In principio. » Filio", "en": "'In the beginning.' In the Son"},
    original=latin("8950", "VERS. 1.-- « In principio creavit, »", "corda scilicet superborum.", 113),
    english={"text": "Verse 1. 'In the beginning he created,' etc. He does not say: In the beginning God says, Let heaven and earth be made. But he said, 'Let there be light, and light was made' — because under the name of heaven and earth was to be comprehended universally whatever God made, and then it was to be set out in parts how he made it. Whence there follows: 'God said, Let it be' — that is, he made it through his Word. Or, because when unformed matter, spiritual or bodily, was first coming to be, it was not to be said 'God said, Let it be'; for it was unfitting that 'let it be' should be said by God, since imperfection does not imitate the form of the Word except when a creature is perfected by the turning of its kind to the Creator; so that when it is said 'God said, Let it be', we may understand him to be calling the creature's imperfection back to himself. When therefore it is said 'In the beginning God made heaven and earth', mention is made of the Son, because he is the Beginning; but when it is said 'God said, Let it be', mention is made that he is the Word. By 'beginning' he notes the origin of the creature existing from him; by 'Word', the perfecting of the creature called back from him to himself, that it may be formed by imitating the unchangeable form of the Word. […] 'In the beginning,' etc. (BEDE, Hexaemeron I, vol. II, col. 13.) Scripture, in intimating the creation of the world, shows in its first word the eternity and omnipotence of God: for him whom it declares to have created the world in the beginning of times, it signifies to have existed eternally before times. […] 'In the beginning,' etc. Heaven — not the visible firmament, but the empyrean, that is, the fiery or intellectual heaven, so called not from burning but from splendour, which was at once filled with angels. […] (ALCUIN, on Genesis, vol. I.) 'In the beginning.' In the Son, by whose becoming man it became plain who were the heavenly and who the earthly. Heaven, the spiritual creature, perfect and blessed from its outset. Earth, bodily matter, still imperfect. […] Mystically. 'In the beginning God created heaven' — namely those who bore the image of the heavenly. 'And earth', that is, those who afterwards, by growing proud, bore the earth, that is, the image of the earthly man, and made themselves deformed. 'But the earth was empty', because it had laid aside its good form. 'And void', of the fruit of good work. 'And there were darknesses', namely the privation of the true light; 'over the face of the abyss', namely the hearts of the proud.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical", "spiritual"],
    answers=["principio-in-filio", "principio-temporis"],
    notes="The margin as a settlement rather than an argument. Five glosses stand on this verse: an unattributed Augustinian one distinguishing Beginning from Word (the Son is called the Beginning where origin is meant and the Word where perfecting is meant); three from Bede, on eternity, on the simultaneity of heaven and earth, and on the empyrean heaven; and then Alcuin's, which is one word — Filio. That is the whole apparatus a twelfth-century reader met: Jerome's refutation is nowhere on the page, and the reading he had called false stands unargued in the margin under a great name. Elisions marked […] are Bede's house-building simile, his Ps 102 argument, the seven heavens list with Jerome's three, and the Sapientia 11 gloss on unformed matter, all of which are on the making rather than on the word 'beginning'. Wilson's edition of the Glossa (migne.app/glossa) supersedes this draft when its English reaches Gen 1:1.")

add(id="bruno-gen-1-1", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1090, date_precision="range-1079-1123", place="segni",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In principio creaturarum omnium", "en": "In the beginning of all creatures"},
    original=latin("21403", "In principio, inquit, et ante omnem creaturam creavit Deus", "omniumque eorum materiam et matrem quae ex ea oriuntur.", 164),
    english={"text": "'In the beginning,' he says, and before every creature, God created heaven and earth. For this the Psalmist too testifies, saying: 'And you, God, in the beginning founded the earth, and the heavens are the works of your hands' (Ps 102:25 [Vg 101:26]). Not, therefore, heaven before earth, but God created heaven and earth together. Whence also this: 'He who lives for ever created all things at once' (Sir 18:1). For even if God is narrated in this same book to have made all things in six days, it is not to be doubted that he nevertheless created all things at once out of nothing. He created at once the very matter of all things, out of which he commanded the rest to be made at distinct times, as he willed. Let it be said, then: In the beginning of all creatures God created heaven — and those things, namely, which are contained in it, that is, the angels and the heavenly powers — and the earth, already as it were pregnant and in labour, and the matter and mother of all those things that arise from it.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["principio-first-of-all", "world-has-a-beginning"],
    notes="Bruno takes the second of Augustine's three readings, the one nobody else on the bench builds on: not in the beginning of time and not in the Son but 'in the beginning of all creatures', that is, before anything else — and he takes it in order to get simul out of the verse, so that Sir 18:1 and the six days can both stand. His pregnant earth, matter and mother of what rises from it, is the same instinct as Bereshit Rabbah 1:1's architect's plans: read the first verse as a statement about what was available to the maker. The Corpus Corporum text of Bruno is the dirtiest on the bench (K7 found Dei. vero, K10 found tuce for luce); nothing in this slice looks corrupt, but it is not collated.")

add(id="bruno-gen-1-1b", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1090, date_precision="range-1079-1123", place="segni",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In quo principio? In eo utique qui ait: Ego principium", "en": "In what beginning? In him, surely, who says: I am the Beginning"},
    original=latin("21403", "In quo principio? In eo utique qui ait", "ab exordio creavit Deus.", 164),
    english={"text": "In what beginning? In him, surely, who says: 'I am the Beginning, who also speak to you' (John 8:25) — 'for all things were made through him, and without him was made nothing' (John 1:3). In this beginning, therefore, God created from the outset the whole fabric of the world and the very orders of the angels.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical"],
    answers=["principio-in-filio"],
    notes="The same commentator, the same verse, the other answer — and the structure is the point. Bruno finishes the literal exposition of the whole first day, and only then turns back: 'having set these things out to the letter, let us see what they also signify allegorically. In what beginning? In him, surely, who says: I am the Beginning.' The two readings are not rivals for him but layers, taken in order, and he does not ask which is the sense of the word. This is how the Latin bench keeps three answers alive for seven centuries without ever having to lose two of them; Peter Comestor's 'the phrase is to be repeated' is the same manoeuvre, made explicit.")

add(id="rupert-gen-1-1", work="rupert-gen", author="rupert", tradition="latin",
    date=1117, date_precision="range-1112-1117", place="liege",
    anchor={"verse": "gen.1.1"}, lemma={"la": "vitium est in superfluitate dictionis", "en": "it is a vice of superfluity of expression"},
    original=latin("10873", "Cum ipsa creatio principium mundi sit", "sed de nihilo fecit coeli et terrae substantiam.", 167),
    english={"text": "Since the creation itself is the beginning of the world, why was it said thus: 'In the beginning he created'? For it is the same as if it were said: In the beginning he made the beginning; and if you take 'beginning' here in the ordinary way when it is said 'in the beginning he created', it is a vice of superfluity of expression. Well, therefore, is 'beginning' taken in this place as a kind of proper name of the Son, because he himself so willed it, who when he was asked by the Jews, 'Who are you?', said: 'The Beginning, who also speak to you' (John 8:25). For truly in this Beginning God created heaven and earth, because all things were made through him (John 1:3). Another Scripture confesses this too when it says: 'You have made all things in wisdom' (Ps 104:24 [Vg 103:24]) — which wisdom is none other than the Word of God, the Word God, who, as has been said, named himself the beginning. Not indeed that the native tongue of this Scripture, that is Hebrew, signifies son and beginning by one word: for son is ben in that language, and beginning is bresith. But we say this too, that though not in word, yet in sense the Son is the Beginning. He is Son, because born of God; Beginning, because he is shown to be the first and efficient cause of all creatures. And so in the beginning, that is, in the Son, in his Word, in his Wisdom, God created heaven and earth. Created, I say — that is, not, as the philosophers of the gentiles vainly supposed, that he had matter or hyle coeval with himself, but he made the substance of heaven and earth out of nothing.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["principio-in-filio", "world-has-a-beginning"],
    notes="The best argument the Latin bench produces on this crux, and the one that shows it had absorbed Jerome. Rupert does not begin from the proof texts; he begins from a defect in the sentence. If the creation is itself the world's beginning, then 'in the beginning he created' says 'in the beginning he made the beginning', which as ordinary Latin is a vitium, a redundancy. A word that would be superfluous in the common sense must be a proper name — so principium here names the Son. Then, having reached Jerome's conclusion by a route Jerome never took, he concedes Jerome's philology in Jerome's own terms and with the Hebrew words in his mouth: son is ben, beginning is bresith, they are not one word, and the identity is of sense and not of speech. That is the twelfth century answering the fourth on the fourth century's ground.")

add(id="abelard-hex-1-1", work="abelard-hex", author="abelard", tradition="latin",
    date=1133, date_precision="range-1130-1135", place="paraclete",
    anchor={"verse": "gen.1.1"}, lemma={"la": "ac si diceretur: In prima die", "en": "as if it were said: On the first day"},
    original=latin("11118", "Cum vero in sequentibus dicit diem secundum et tertium", "ante caetera quae sequuntur opera.", 178),
    english={"text": "But when in what follows he says a second day and a third and the rest, he means by the first day that on which heaven and earth were created, as it was said: 'In the beginning God created heaven and earth', on which also light was created or divided from the darkness. For to the works of the first day there belongs only the creation of heaven and earth, which is to be assigned to the first day, in respect of which first day the second or third day is so called; so that 'in the beginning he created' is as if it were said: On the first day — that is, before the other works that follow.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["principio-first-of-all", "principio-temporis"],
    notes="Abelard reads the word as a position in a series and nothing more: 'in the beginning' means 'on the first day', because a second and a third day are named afterwards and something must be first for them to be second to. Of everything on the Latin bench this is the closest to Rashi's plain sense — both make the phrase relative to what follows rather than absolute — and it is arrived at from the opposite end, Rashi from the construct state of a Hebrew noun and Abelard from the ordinals of the Latin chapter. Abelard is also the Latin witness that K7 found reporting the Hebrew against Jerome (volitabat at PL 178:735B): he is the one commentator on this bench who habitually asks what the words are doing rather than what they signify.")

add(id="hugh-sacr-1-1", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "in principio temporis, vel potius cum ipso tempore", "en": "in the beginning of time, or rather with time itself"},
    original=latin("11082", "Nam quod illa prima rerum omnium materia, in principio temporis", "nullam omnino dilationem intervenisse.", 176),
    english={"text": "For that that first matter of all things arose in the beginning of time, or rather with time itself, is clear from what was said: 'In the beginning God created heaven and earth.' But how long it remained in this unformedness or confusion, Scripture does not plainly show. To me, however, it seems, so far as I can conjecture, that between the creation and the disposing of things there was indeed an order of time but no delay interposed; so that it can truly be said that this was made after that, yet that between this making and that no postponement whatever came between.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal"],
    answers=["principio-temporis", "world-has-a-beginning"],
    notes="Hugh sharpens the temporal reading to the point where it stops being a place in time at all: not in the beginning of time but 'or rather with time itself', so that the verse dates nothing, it institutes the possibility of dating. From that he draws the conclusion the schools needed — that between creation and the ordering of things there was an order of time but no interval — which is how a literal six days can be held together with 'he created all things at once'. Compare b. Chagigah 12a, where the measure of the day and the measure of the night are themselves among the ten things made on the first day: both benches, asked what the beginning is the beginning of, answer that time is inside the creature and not outside it.")

add(id="honorius-hex-1-1", work="honorius-hex", author="honorius", tradition="latin",
    date=1120, date_precision="range-1110-1130", place="regensburg",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Moyses propheta Filium principium, Joannes autem Patrem principium", "en": "Moses the prophet has the Son as the beginning, but John the Father"},
    original=latin("10991", "Et notandum, quod Moyses propheta Filium principium", "visibilia et invisibilia.", 172),
    english={"text": "And it is to be noted that Moses the prophet records the Son as the beginning, and all things created in him; but John the apostle proclaims the Father as the beginning, and that the Son always remained in him, coequal to him, and that all things were made through him. For without doubt they announce to us in concord the one substance of both. It is said therefore (Gen 1): 'In the beginning God created heaven and earth' — that is, God the Father created in the Son, at once, the heavenly and the earthly, the visible and the invisible.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["allegorical"],
    answers=["principio-in-filio"],
    notes="The neatest thing said on this crux in the twelfth century, and the neatness is the problem. Honorius observes that Genesis and John begin with the same words and mean opposite persons by them: in Genesis 'the beginning' is the Son, in whom all is created; in John 'the beginning' is the Father, in whom the Son always was. The two openings had been read together since Jerome as evidence for one another; Honorius is the first on this bench to notice that reading them together requires the same phrase to name two different persons, and he resolves it not by choosing but by an appeal to the single substance. Honorius has already appeared on K7 (PL 172:254C) and K10 (255D) from the same columns of the same work.")

add(id="comestor-hs-1-1", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="range-1169-1173", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "iterandum est in principio", "en": "'in the beginning' is to be repeated"},
    original=latin("11575", "Moyses vero solum Deum aeternum prophetavit", "creaturas primordiales fecit, et simul.", 198),
    english={"text": "But Moses prophesied God alone to be eternal, and the world created without pre-existing matter. And it was created in the beginning, that is, in the Son; and 'in the beginning' is to be repeated thus: In the beginning God created heaven and earth, in the beginning, namely, of time. For the world and time are coeval. And as God alone is eternal, so the world is everlasting, that is, always eternal, eternal in a temporal way; the angels too are everlasting. Or: in the beginning of all creatures he created heaven and earth, that is, he made these primordial creatures, and made them at once.", **DRAFT},
    cruxes=["beginning-of-what"], senses=["literal", "allegorical"],
    answers=["read-it-twice", "principio-in-filio", "principio-temporis", "principio-first-of-all"],
    notes="The settlement, stated as a rule of reading: iterandum est in principio — say the phrase twice. Once it means in the Son, once it means at the beginning of time, and Comestor then adds Bruno's third sense as an alternative, in the beginning of all creatures. Augustine had listed the three as questions; the handbook that taught Europe the Bible for three hundred years prints all three as the answer and instructs the reader to take the words over again for each. Note the distinction Comestor needs and that the English must keep: God alone is aeternus, the world and the angels are sempiternus, everlasting — 'eternal in a temporal way'. The preceding columns, where he sets Plato, Aristotle and Epicurus against Moses, are not sliced here; that doxography is Remigius' material and belongs with K4.")

# ---------------------------------------------------------------- threads
THREADS = [
 # the versions
 E("t-k1-01", "jerome-hq-1-1", "lxx-1-1", "cites", "Jerome names the Seventy as his first witness against the reading 'in the Son': 'Nam et Septuaginta Interpretes, et Symmachus, et Theodotion, in principio, transtulerunt.' The Greek is what decides the Latin."),
 E("t-k1-02", "vulgate-1-1", "lxx-1-1", "transmits", "in principio renders ἐν ἀρχῇ and nothing else, and the translator says in the Hebrew Questions why he refused in Filio. Every Latin argument on this crux is conducted on a word Jerome chose against pressure to choose another."),
 E("t-k1-03", "targ-onk-1-1", "lxx-1-1", "parallel", "be-qadmin and ἐν ἀρχῇ make the same decision independently: turn the Hebrew word into a plain adverb of time, supply nothing, and let no construct be heard. Pseudo-Jonathan's min avvela does the same a third time."),
 E("t-k1-04", "targ-neof-1-1", "targ-onk-1-1", "contests", "Two Aramaic versions of one Hebrew word, and only one of them interprets: Onkelos writes be-qadmin, 'in former times'; Neofiti writes min qadmin be-ḥokhmah, 'from the first, in wisdom', and adds a second verb, 'and finished'. What Onkelos leaves as a time, Neofiti makes an instrument."),
 E("t-k1-05", "targ-psj-1-1", "targ-onk-1-1", "parallel", "min avvela beside be-qadmin: the same refusal to interpret, in a different word. Three targums on one verse give three renderings of bereshit and only Neofiti's carries a doctrine."),
 # the rabbinic bench
 E("t-k1-06", "br-1-4", "br-1-1", "echoes", "The same proof text put to the same use two sections later: 'The Lord made me reshit of his way' (Prov 8:22) makes the Torah the reshit in 1:1, and in 1:4 makes the Torah the first of the six things that preceded the world and settles its precedence over the Throne of Glory."),
 E("t-k1-07", "br-1-8", "br-1-1", "echoes", "1:1 reads Prov 8:30's amon as uman, artisan; 1:8 counts the builder's six materials against Prov 8:22–23's six words of precedence. Both treat Proverbs 8 not as a proof text reached for but as the chapter that comments on Genesis 1:1."),
 E("t-k1-08", "rashi-1-1b", "br-1-1", "cites", "Rashi reproduces the midrashic answer with its two proof texts — the Torah called reshit darko (Prov 8:22) and Israel called reshit tevu'ato (Jer 2:3) — and marks it as what 'our rabbis expounded', before setting his own plain sense against it."),
 E("t-k1-09", "rashi-1-1b", "br-1-4", "echoes", "Bereshit Rabbah 1:4 derives a series of referents for reshit from a series of verses — Torah, ḥalla, tithes, first fruits; Rashi keeps the method and reduces the list to two, Torah and Israel, which are the two that make the verse a claim about election."),
 E("t-k1-10", "ibn-ezra-1-1", "rashi-1-1b", "parallel", "The same conclusion from the same evidence with no acknowledgement: bereshit is a construct, like 'in the reshit of the reign of Jehoiakim' (Jer 26:1), and the objection that a construct cannot govern a finite verb is answered from Hos 1:2 by both. Ramban, reading them side by side, says Ibn Ezra 'explained it in an identical way'."),
 E("t-k1-11", "ramban-1-1", "rashi-1-1b", "contests", "Ramban quotes Rashi's plain sense verbatim and then breaks its premise: reshit is not everywhere construct — 'declaring the end mereshit' (Isa 46:10) and 'he chose reshit for himself' (Deut 33:21) stand absolute. The grammatical argument that made the modern translations is refuted inside the tradition that made it, two centuries on."),
 E("t-k1-12", "ramban-1-1", "ibn-ezra-1-1", "cites", "Ramban names R. Abraham and reports the refinement that is Ibn Ezra's own and not Rashi's — that the vav of ve-ha'aretz serves as 'when' — and draws its consequence, that on Ibn Ezra's reading only light was created on the first day."),
 # the two benches on wisdom
 E("t-k1-13", "targ-neof-1-1", "br-1-4", "parallel", "R. Banai proves that the world was created for the merit of the Torah from Prov 3:19, 'the Lord founded the earth be-ḥokhmah, with wisdom'; Neofiti puts that same be-ḥokhmah inside Genesis 1:1 as the translation of bereshit. A proof text in one place is the text itself in the other."),
 E("t-k1-14", "aug-civ-11-32", "br-1-1", "parallel", "The identical inference on both benches. Augustine: in principio means in the Son, because Ps 104:24 says 'you have made all things in wisdom' and Wisdom is the Son. Bereshit Rabbah: bereshit means by the Torah, because Prov 8:22 says 'the Lord made me reshit of his way' and that speaker is the Torah. One move, one kind of proof text, two Wisdoms, and no contact in either direction."),
 E("t-k1-15", "aug-conf-11-9", "targ-neof-1-1", "parallel", "'In this Beginning, God, you made heaven and earth: in your Word, in your Son, in your Wisdom' is, as a sentence, what Neofiti prints as the text of Genesis 1:1. A Latin bishop's prayer and a Palestinian targumist's translation arrive at the same clause, and mean by Wisdom the second person of the Trinity and the Torah respectively."),
 E("t-k1-16", "abelard-hex-1-1", "rashi-1-1b", "parallel", "Both make the first word relative to what follows rather than absolute — Abelard because a second and third day are named and something must be first for them to be second to, Rashi because reshit is a construct and the clause is subordinate. The closest the two benches come on this crux, reached from opposite ends of two grammars."),
 E("t-k1-17", "remigius-gen-1-1", "ramban-1-1", "parallel", "The same doctrinal stake stated on both benches at the same place in the commentary: for Remigius the verse exists to refute Plato and Aristotle and prove that time began; for Ramban whoever thinks the world eternal 'denies the essential principle and has no Torah at all'."),
 # Ambrose, Augustine and the Latin line
 E("t-k1-18", "aug-gnm-1-2", "ambrose-hex-1-2", "echoes", "The John 8:25 answer, taken over from the man Augustine had been hearing preach at Milan a year or two before: 'or he himself is the beginning of all things … the Son of God answered, The Beginning, who also speak to you.' After Ambrose no Latin witness on this crux argues without that verse."),
 E("t-k1-19", "aug-gnl-imp-2-6", "aug-gnm-1-2", "echoes", "The same author returning to the same question with the terms sharpened: what had been 'not in the beginning of time but in Christ' becomes a distinction — a Beginning without a beginning, who is the Father, and a Beginning with another beginning, who is the Son."),
 E("t-k1-20", "aug-gnl-1-1", "aug-gnl-imp-2-6", "echoes", "The unfinished commentary asks whether 'in the beginning' means time or the Wisdom of God; the finished one opens by listing three possibilities instead of two, adding 'or because they were made first of all', and declining to choose among them."),
 E("t-k1-21", "aug-conf-11-9", "aug-gnm-1-2", "echoes", "The argument of the anti-Manichaean book turned into prayer: 'in Christ, since the Word was with the Father' becomes 'in your Word, in your Son, in your Strength, in your Wisdom, in your Truth' — five names where the treatise had one, and no opponent in view."),
 E("t-k1-22", "aug-civ-11-32", "aug-conf-11-9", "echoes", "The same identification with its proof supplied: the Confessions name the Beginning as Wisdom without arguing, and the City of God adds the psalm that licenses it, 'omnia in sapientia fecisti' (Ps 104:24)."),
 E("t-k1-23", "aug-civ-11-32", "ambrose-hex-1-3", "echoes", "Ps 104:24 is Ambrose's proof text on this verse before it is Augustine's, and it does different work for each: Ambrose cites it to show that the world was given a beginning at all, Augustine to show that the beginning is the Son."),
 E("t-k1-24", "isidore-quaest-1-1", "ambrose-hex-1-2", "echoes", "'Principium Christus est', with John 8:25 attached and no argument at all. What Ambrose offered as one limb of a vel and Augustine as one of three readings has become a premise from which the allegory starts."),
 # the Carolingian transmission
 E("t-k1-25", "bede-gen-1-1", "aug-gnl-1-1", "echoes", "Bede takes Augustine's three undecided readings and ranks them: the beginning of times at length and first, the Only-begotten Son last and qualified as 'not improbable'. The hierarchy, not the list, is what the Carolingians inherit."),
 E("t-k1-26", "rabanus-gen-1-1b", "bede-gen-1-1", "cites", "Bede's exposition reproduced almost entire and unattributed — the simultaneity argument, Ps 115:3, Ps 102:25, the 'not improbably … in his Only-begotten Son' — with the house-building simile cut and Rabanus' own thesis set at its head. The same silent copying the K7 and K10 threads trace at PL 107:447C and 448D."),
 E("t-k1-27", "rabanus-gen-1-1b", "aug-gnm-1-2", "echoes", "The sentence Rabanus adds in front of Bede is Augustine's answer to the Manichees compressed to an axiom: 'time is from this world, not before the world; and a day is a portion of time, not its beginning.'"),
 E("t-k1-28", "wigbod-gen-1-1", "jerome-hq-1-1", "cites", "Verbatim Jerome, minus the argument: the three Greek versions, Bresith, Aquila's in capitulo, the forehead of Genesis, Ps 40:8, John 1:3 and the Hebrew custom of naming books are all kept, while the authorities who read 'in the Son' and Jerome's refutation of them — including the decisive point that the Hebrew for 'in the son' would be ba-ben — are dropped. The concession survives; the correction does not."),
 E("t-k1-29", "angelom-gen-1-1", "jerome-hq-1-1", "echoes", "Jerome's closing remark, that the Hebrews name volumes from their opening words, becomes the first question of Angelomus' commentary and acquires a conclusion Jerome did not draw: that Bresith is therefore rightly rendered Genesis."),
 E("t-k1-30", "alcuin-int-26", "jerome-hq-1-1", "contests", "The reading Jerome had declared false, printed as the answer to the question and in four words: 'In Filio perfecit Deus coelum et terram.' No Hebrew, no versions, no 'according to the sense rather than the word'."),
 E("t-k1-31", "remigius-gen-1-1", "bede-gen-1-1", "echoes", "Remigius takes over Bede's empyrean heaven — fiery or intellectual, so called not from burning but from splendour, filled at once with angels, proved from Job 38:7 — and puts it after a doxography of Plato and Aristotle that Bede does not have."),
 E("t-k1-32", "remigius-gen-1-1", "ambrose-hex-1-3", "echoes", "Ambrose's polemical use of the verse, given names: what Ambrose argued against those who would make the world anarchon, Remigius argues against Plato's three principles and Aristotle's two, and supplies the missing word out loud — 'In principio, and of time is understood'."),
 # the Glossa
 E("t-k1-33", "glossa-1-1", "bede-gen-1-1", "cites", "Three of the five glosses on this verse are Bede, the first of them cited by book and Migne column ('BEDA, Hexaem. lib. I, tom. II, col. 13'), and the margin keeps his eternity argument, his simultaneity argument and his empyrean heaven while dropping the house-building simile that carried them."),
 E("t-k1-34", "glossa-1-1", "alcuin-int-26", "cites", "The Glossa prints Alcuin's answer as a gloss of one word — '(ALCUIN. in Gen. tom. I.) « In principio. » Filio' — so that the twelfth-century reader meets the reading Jerome refuted as a bare equation under a great name, with nothing on the page to argue with."),
 E("t-k1-35", "glossa-1-1", "isidore-quaest-1-1", "parallel", "The Glossa's Mystice paragraph reads heaven and earth as those who bore the image of the heavenly and those who grew proud and bore the earthly; Isidore's Quaestiones read the same two words as the spiritual and the carnal in the Church. Same allegory, same verse, five centuries apart, and the Glossa does not name him."),
 # the twelfth century
 E("t-k1-36", "bruno-gen-1-1b", "bruno-gen-1-1", "parallel", "One commentator giving both answers in order and treating them as layers rather than rivals: the literal exposition takes in principio as 'in the beginning of all creatures', and then, the letter disposed of, 'in what beginning? in him, surely, who says: I am the Beginning.' Neither reading is asked to yield to the other."),
 E("t-k1-37", "bruno-gen-1-1", "aug-gnl-1-1", "echoes", "Augustine's second reading — 'or because they were made first of all' — is the one Bruno builds on, and he builds on it to get simul out of the verse, so that Sir 18:1's 'he created all things at once' and the six days can both stand."),
 E("t-k1-38", "rupert-gen-1-1", "jerome-hq-1-1", "echoes", "Rupert concedes Jerome's philology in Jerome's own terms and with the Hebrew words in his mouth — 'son is ben in that language, and beginning is bresith' — and then holds the Christological reading anyway, on the ground that the identity is of sense and not of speech. He reaches Jerome's conclusion about the word and refuses Jerome's conclusion about the sense."),
 E("t-k1-39", "rupert-gen-1-1", "aug-civ-11-32", "echoes", "The Ps 104:24 chain taken over entire — 'you have made all things in wisdom, which wisdom is none other than the Word of God' — but reached only after an argument Augustine never makes, that principium in the common sense would be a superfluity of expression and so must be a proper name."),
 E("t-k1-40", "honorius-hex-1-1", "jerome-hq-1-1", "echoes", "Jerome had read Genesis and John together as evidence for one another; Honorius notices what that costs — in Genesis the beginning is the Son, in John the beginning is the Father — and resolves it by the unity of substance rather than by choosing."),
 E("t-k1-41", "hugh-sacr-1-1", "aug-gnm-1-2", "echoes", "Augustine's 'time began together with heaven and earth' becomes Hugh's 'in the beginning of time, or rather with time itself', and Hugh draws the school's conclusion from it: between creation and the disposing of things there was an order of time but no delay interposed."),
 E("t-k1-42", "abelard-hex-1-1", "bruno-gen-1-1", "parallel", "Both read the phrase as a place in a series — Bruno 'in the beginning of all creatures', Abelard 'as if it were said, on the first day' — and both do it to keep the six days without losing the simultaneity of the first making."),
 E("t-k1-43", "comestor-hs-1-1", "aug-gnl-1-1", "echoes", "Augustine's three questions, printed as three answers with an instruction: 'in the beginning' is to be repeated, once for the Son and once for time, with 'in the beginning of all creatures' offered as a third. The handbook that taught Europe the Bible resolves the crux by refusing to resolve it."),
 E("t-k1-44", "comestor-hs-1-1", "bruno-gen-1-1", "echoes", "Comestor's third sense, 'in the beginning of all creatures he created heaven and earth, that is, he made these primordial creatures, and made them at once', is Bruno's opening sentence and Bruno's simul, carried into the schools' handbook."),
]

FINDING = "Both benches gloss the first word of Scripture as 'in wisdom', prove it from a wisdom text, and mean opposite things by it. Targum Neofiti does not translate bereshit but interprets it — min qadmin be-ḥokhmah — and Bereshit Rabbah reaches the same gloss by proof text, R. Banai from Prov 3:19 ('the Lord founded the earth with wisdom') and R. Hoshaya from Prov 8:22 ('the Lord made me reshit of his way'), where the Wisdom that speaks is the Torah, the architect's plan the King builds from. Augustine, Ambrose, Bede, Bruno and Rupert reach it from Ps 104:24 ('you have made all things in wisdom'), where the Wisdom is the Son. Neither side knows the other is there, and the shared conclusion is the least noticed thing about the crux. What separates them is not the gloss but what happened to the philology. Jerome, the one Latin who read the Hebrew, refuted the Christological reading outright — the three Greek versions all say 'in the beginning', the Hebrew is bresith, and the Hebrew for 'in the son' would be ba-ben — and then conceded that Christ might be understood 'according to the sense rather than the translation of the word'. Wigbod copies the passage almost entire and drops precisely the refutation, keeping the concession; Alcuin's schoolbook reduces the whole question to four words, In Filio perfecit Deus; and the Glossa prints Alcuin's answer in the margin as a single word, Filio, so that the twelfth century met a reading its best philologist had disproved with nothing on the page to argue against. Rupert of Deutz is the one who repairs it, four hundred years later, by stating the Hebrew evidence himself — 'son is ben in that language, and beginning is bresith' — and then holding the reading anyway on the ground that the identity is of sense and not of speech. Meanwhile the modern translations settle the crux by removing it, as they did at K10: the JPS Tanakh prints 'When God began to create heaven and earth', which is Rashi's plain sense and Ibn Ezra's construct, adopted as the text — the one reading no Latin witness on this bench could have raised, and the one Ramban had already refuted from Isa 46:10 and Deut 33:21."

# ---------------------------------------------------------------- persons / places new to this crux
PERSONS = {
 "r-hoshaya": {"name": "R. Hoshaya Rabbah", "dates": "fl. c. 230", "tradition": "rabbinic", "role": "tradent"},
 "r-abba-b-kahana": {"name": "R. Abba bar Kahana", "dates": "fl. c. 300", "tradition": "rabbinic", "role": "tradent"},
 "r-huna": {"name": "R. Huna", "dates": "d. 297", "tradition": "rabbinic", "role": "tradent"},
 "r-banai": {"name": "R. Banai", "tradition": "rabbinic", "role": "tradent"},
 "r-berekhya": {"name": "R. Berekhya", "dates": "fl. c. 350", "tradition": "rabbinic", "role": "tradent"},
 "rav-matana": {"name": "Rav Matana", "tradition": "rabbinic", "role": "tradent"},
 "r-yehoshua-b-levi": {"name": "R. Yehoshua ben Levi", "dates": "fl. c. 230", "tradition": "rabbinic", "role": "tradent"},
 "r-levi": {"name": "R. Levi", "dates": "fl. c. 300", "tradition": "rabbinic", "role": "tradent"},
 "ibn-ezra": {"name": "Abraham ibn Ezra", "he": "אַבְרָהָם אִבְּן עֶזְרָא", "dates": "1089–1167", "tradition": "rabbinic"},
 "ramban": {"name": "Moses ben Naḥman (Naḥmanides)", "he": "מֹשֶׁה בֶּן נַחְמָן", "dates": "1194–1270", "tradition": "rabbinic"},
}
PLACES = {
 "lucca": {"name": "Lucca", "lat": 43.84, "lon": 10.50},
 "girona": {"name": "Girona", "lat": 41.98, "lon": 2.82},
}

# ---------------------------------------------------------------- answer families new to this crux
ANSWERS = {
 "principio-temporis": {"label": "In the beginning of time", "gloss": "The word dates the making: time began with the world, and there was no before (Onkelos, Bede, Rabanus, Remigius, Hugh)."},
 "principio-in-filio": {"label": "In the Son", "gloss": "Principium is a proper name of the Word, on the strength of John 8:25 and Ps 104:24 (Ambrose, Augustine, Isidore, Alcuin, the Glossa, Rupert, Honorius)."},
 "principio-first-of-all": {"label": "First of all things", "gloss": "'In the beginning' means before everything else that follows — in the beginning of the creatures, or on the first day (Augustine's second reading; Bruno, Abelard)."},
 "principio-is-first-creature": {"label": "The first creature is a beginning", "gloss": "The first intellectual creature may be called a beginning to the things it heads (Augustine, De Genesi imperfectus)."},
 "beginning-is-wisdom": {"label": "In Wisdom", "gloss": "The beginning is Wisdom — which is the Torah on one bench (Prov 8:22, Prov 3:19, Neofiti) and the Son on the other (Ps 104:24)."},
 "reshit-is-torah": {"label": "The beginning is the Torah", "gloss": "Reshit is the Torah, called reshit darko: God looked into it as an architect into his plans and created the world (Bereshit Rabbah, Rashi)."},
 "reshit-is-israel": {"label": "For the sake of Israel", "gloss": "Reshit is Israel, called reshit tevu'ato (Jer 2:3); the world was made for their sake."},
 "reshit-construct": {"label": "'When God began to create'", "gloss": "Bereshit is a construct and the verse a subordinate clause: at the beginning of God's creating (Rashi's plain sense, Ibn Ezra; contested by Ramban)."},
 "world-has-a-beginning": {"label": "The world is not eternal", "gloss": "The point of saying 'in the beginning' at all is that the world had one, against the philosophers (Ambrose, Remigius, Hugh, Ramban)."},
 "bereshit-book-name": {"label": "It is the book's name", "gloss": "The Hebrews name volumes from their opening words, so bresith is the title of Genesis (Jerome, Wigbod, Angelomus)."},
 "six-preceded": {"label": "Six things preceded the world", "gloss": "Torah and the Throne of Glory were made before it; the patriarchs, Israel, the Temple and the Messiah's name were contemplated (Bereshit Rabbah 1:4)."},
 "read-it-twice": {"label": "Say the phrase twice", "gloss": "In principio is to be repeated — once in the Son, once at the beginning of time — rather than decided (Comestor)."},
}

LICENSES = {
 "chavel-ramban": {"label": "Charles B. Chavel's English of Ramban (Shilo, 1971–76), shown as CC BY on Sefaria. [CHECK: surprising for a 1971 text; verify the version page before publication, or replace with a fresh draft]"},
}
SHORT = "Bereshit / in principio"
