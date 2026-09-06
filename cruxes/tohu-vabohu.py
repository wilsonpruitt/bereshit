"""K6 — tohu-vabohu (Gen 1:2). What does the pair mean, and is it a state or a thing?
Built 2026-09-05 (Phase 2, crux 4 of 9). See PHASES.md for the spec-file contract.

Latin sliced from the local PL TEI by anchor phrase; rabbinic from raw/sefaria/*.json.
The vocalized-Hebrew slicer `hcut` was lifted into scripts/bench.py in this session (PHASES.md
said to do so at the third crux that needed it; this is it).

Seven witnesses already carry this crux from K7 — the LXX, the Vulgate, the three targums,
Hugh's Adnotationes on the Spirit, and Wilson's Glossa chunk — and build-crux.py folds them into
the roster. They are not rebuilt here.
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, APPROVED, thread

CRUX_ID = "tohu-vabohu"
SHORT = "tohu va-vohu"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "cc-by-sa", "version": "Sefaria 'Wikisource Bereshit Rabbah' (CC BY-SA). Phase 6, 2026-09-05: moved off 'Midrash Rabbah -- TE', whose own site asserts all rights reserved"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True}

add(id="br-2-1", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.2"}, lemma={"he": "גַּם בְּמַעֲלָלָיו יִתְנַכֶּר נָעַר", "en": "even a boy is known by his deeds"},
    original={"lang": "he", "text": sef("br-2", "he", 0)[0], "source": "Bereshit Rabbah 2:1 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-2", "en", 0)[0], **_BR_EN},
    tradents=["r-berekhya"],
    cruxes=["tohu-vabohu"], senses=["allegorical"],
    answers=["pair-is-history"],
    notes="The opening of the section, and it settles in one move what the whole rabbinic side of this crux will do with the pair: it reads it through Jeremiah. R. Berekhya begins from Prov 20:11, 'even a boy is known by his deeds' — while the plant was still unripe it put out thorns — and lands on Jer 4:23, 'I have seen the land, and behold, it is tohu va-vohu.' The prophet used the phrase of a land under judgement; so the phrase in Gen 1:2 can be read as a verdict rather than a description, and the four readings that follow in 2:2–2:5 all take that licence. Nothing on the Latin bench cites Jer 4:23 at all.")

add(id="br-2-2", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.2"}, lemma={"he": "תּוֹהָה וּבוֹהָה", "en": "bewildered and astonished"},
    original={"lang": "he", "text": sef("br-2", "he", 1)[0], "source": "Bereshit Rabbah 2:2 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-2", "en", 1)[0], **_BR_EN},
    tradents=["r-abahu", "r-yehuda-b-simon"],
    cruxes=["tohu-vabohu"], senses=["allegorical"],
    answers=["pair-is-astonishment"],
    notes="The etymology Rashi will give as lexicography is here still a parable, and the parable is about grievance. A king buys two slaves with one bill of sale and one price and decrees that one shall be fed from the treasury and the other must work to eat; the second sits toheh u-voheh — bewildered and astonished — saying, we were bought together, why him and not me? So the earth sat toheh u-voheh: the celestials and the terrestrials were created together, the celestials are fed on the radiance of the Presence and we must toil. R. Yehuda bar Simon tells it again with two maidservants, one kept in the palace and one banished, and the earth's complaint becomes mortality: they live for ever and we die. The pair is not a state of matter here but a state of mind, and it belongs to the earth, who is a person with a case to make.")

add(id="br-2-3", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.2"}, lemma={"he": "פָּתַר קְרָיָא בַּדּוֹרוֹת", "en": "he interpreted the verse of the generations"},
    original={"lang": "he", "text": sef("br-2", "he", 2)[0], "source": "Bereshit Rabbah 2:3 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-2", "en", 2)[0], **_BR_EN},
    tradents=["r-yehuda-b-simon"],
    cruxes=["tohu-vabohu"], senses=["allegorical"],
    answers=["pair-is-history"],
    notes="The verse read straight through as a history of the generations: tohu is Adam, who came to nothing; va-vohu is Cain, who sought to return the world to tohu va-vohu; the darkness is the generation of Enosh; the face of the deep is the generation of the Flood; the spirit of God is the wind God made pass over the earth (Gen 8:1); and 'let there be light' is Abraham. Then day and night are Jacob and Esau. The move is exactly Bruno of Segni's in the twelfth century — the verse as a periodization running from the first man to the last redemption — and neither could have known the other; the difference is whose history it is. Note that Resh Lakish's reading of the same verse as the four kingdoms follows immediately in 2:4, which is built as a K7 witness for the Messiah's spirit; its first half belongs here too (see notes/cross-crux.md).")

_chag = json.load(open(RAW / "b-chag-12a.json"))
def _seg(lang, a, b):
    v = [x for x in _chag["versions"] if x["language"] == lang][0]["text"]
    def flat(x): return x if isinstance(x, str) else " ".join(flat(i) for i in x)
    return " ".join(flat(v[i]) for i in range(a, b))
add(id="b-chag-12a-tohu", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.2"}, lemma={"he": "תֹּהוּ קַו יָרוֹק שֶׁמַּקִּיף אֶת כָּל הָעוֹלָם", "en": "tohu is a green line encircling the whole world"},
    original={"lang": "arc", "text": _seg("he", 6, 7), "source": "b. Chagigah 12a (Vilna)", "license": "cc-by-sa", "version": [x for x in _chag["versions"] if x["language"] == "he"][0]["versionTitle"]},
    english={"text": _seg("en", 6, 7), "translator": "Sefaria Community Translation", "license": "cc0"},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-two-things"],
    notes="Two sentences, and they answer the crux's second question in the way no Latin does: the pair names two things, and you could point at them. Tohu is a green line that encircles the whole world and darkness comes out of it (Ps 18:12); bohu are the slimy stones sunk in the deep from which the waters come out — and the proof is Isa 34:11, 'he shall stretch over it the line of tohu and the stones of bohu', read as an inventory rather than as a curse. The baraita stands in the list of the ten things created on the first day (segments 4–5 here, which are K5's text), so tohu and bohu are creatures with a day of creation. Ibn Ezra knows this tradition from Sefer Yetzirah and sets it aside; Ramban knows it and keeps the proof-text while turning the line into a builder's measuring cord.")

_rashi = json.load(open(RAW / "rashi-gen-1.json"))
def _rashi_seg(lang, verse_idx, segs):
    v = [x for x in _rashi["versions"] if x["language"] == lang][0]["text"][verse_idx]
    return " ".join(v[i] for i in segs)
add(id="rashi-1-2a", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1080-1105", place="troyes",
    anchor={"verse": "gen.1.2"}, lemma={"he": "תֹּהוּ לְשׁוֹן תֵּמַהּ וְשִׁמָּמוֹן", "en": "tohu is a word for astonishment and desolation"},
    original={"lang": "he", "text": _rashi_seg("he", 1, [0, 1, 2]), "source": "Rashi on Gen 1:2, s.v. תהו ובהו", "license": "pd"},
    english={"text": _rashi_seg("en", 1, [0, 1, 2]), "translator": "Rosenbaum–Silbermann 1929–34", "license": "silbermann"},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-astonishment", "pair-is-unfurnished"],
    notes="Three lines that turn the parable of BR 2:2 into a lexicon. Tohu is a word for astonishment and desolation, because a person would be astonished and appalled at the bohu in it — the emptiness is the thing seen and the astonishment is what seeing it does. Then the la'az: tohu is estordison in Old French, from estordir, to stun or daze, the word for the swimming in the head after a blow; Rashi gives the reader the sensation rather than the definition. Bohu he glosses reikut ve-tzadu, emptiness and waste — which are the two Aramaic words Onkelos used for the whole pair, in the other order. The Latins who answer this crux describe what was missing from the earth; Rashi describes what looking at it would do to you.")

_ie = json.load(open(RAW / "ibn-ezra-gen-1.json"))
def _ie_text(lang, idx):
    v = [x for x in _ie["versions"] if x["language"] == lang][0]["text"][idx]
    return v if isinstance(v, str) else " ".join(v)
add(id="ibn-ezra-1-2", work="ibn-ezra-gen", author="ibn-ezra", tradition="rabbinic",
    date=1155, date_precision="circa", place="lucca",
    anchor={"verse": "gen.1.2"}, lemma={"he": "תֹהוּ", "en": "tohu"},
    original={"lang": "he", "text": hcut(_ie_text("he", 1), "תהו, אמר הגאון", "להיות למטה מהמים", "K6 ibn-ezra he"),
              "source": "Ibn Ezra on Gen 1:2, s.v. תהו", "license": "pd", "version": "Piotrkow, 1907–1911"},
    english={"text": hcut(_ie_text("en", 1), "“Void” (tohu) – The Ga’on", "to be beneath the water.", "K6 ibn-ezra en"),
             "translator": "Sefaria Community Translation", "license": "cc0"},
    tradents=[],
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-under-water", "pair-is-unfurnished"],
    notes="A grammarian clearing the ground. Saadia Gaon had derived tohu from tehom, the deep; Ibn Ezra refuses it, because the mem of tehom is a root letter, as in hadom. Then he names Sefer Yetzirah's green line and slimy stones — the baraita of b. Chagigah 12a in its other home — and sets it aside in four words: 'what is correct is as the Aramaic translator said', that is, Onkelos' tzadya ve-reikanya, waste and empty; and he proves it from 'the howling waste of tohu' (Deut 32:10) and 'after tohu' (1 Sam 12:21), where the word means without substance. Bohu is 'the brother of' tohu, its vav standing for a hey. His own answer is then physical and is Basil's: at the creation of the firmament and the dry land there was no settled place on the earth, because it was covered with water. The community translation embedded here leaves mefulamot untranslated and renders bohu as 'and confused'; it is CC0 and is kept as it stands.")

_ram = json.load(open(RAW / "ramban-gen-1.json"))
def _ram_text(lang):
    v = [x for x in _ram["versions"] if x["language"] == lang][0]["text"][0]
    return v if isinstance(v, str) else " ".join(v)
add(id="ramban-1-2-tohu", work="ramban-gen", author="ramban", tradition="rabbinic",
    date=1267, date_precision="range-1263-1270", place="girona",
    anchor={"verse": "gen.1.2"}, lemma={"he": "תֹּהוּ … בֹּהוּ", "en": "tohu … bohu"},
    original={"lang": "he", "text": hcut(_ram_text("he"), 'וְהַחֹמֶר הַזֶּה, שֶׁקָּרְאוּ הִיּוּלִי', 'דָּבָר שֶׁיֵּשׁ בּוֹ מַמָּשׁ, דִּכְתִיב "בּוֹ הוּא"', "K6 ramban he"),
              "source": "Ramban on Gen 1:1, s.v. בראשית (the tohu–bohu paragraph)", "license": "sefaria-vocalized", "version": "Sefaria 'Vocalized Edition'"},
    english={"text": hcut(_ram_text("en"), "This substance, which the Greeks called hyly", "‘bo hu’ (in it there is substance)", "K6 ramban en"),
             "translator": "Charles B. Chavel, 1971–76", "license": "chavel-ramban"},
    tradents=["r-berekhya"],
    cruxes=["tohu-vabohu", "ex-nihilo-or-matter"], senses=["literal"],
    answers=["pair-is-matter-and-form", "pair-is-astonishment"],
    notes="The one witness on either bench that makes the pair a matched technical vocabulary. The primary matter, which the Greeks call hyle, is called in the holy tongue tohu — the word derived from the rabbinic betohe, of a man who bethinks himself of what he has done, because if a man came to fix a name to this matter he would think again and call it something else, having no form to fasten a name on. The form that the matter puts on is called bohu, a compound word, bo hu, 'in it there is'. Then Isa 34:11 read as a workshop: the line of tohu is the cord by which the craftsman marks out the plan of his building, the stones of bohu are the forms in it — the same verse the Chagigah baraita read as a green line round the world and stones in the deep. He closes with Sefer Yetzirah and with the Bahir's R. Berekhya, who defines tohu as 'a thing which astonishes people' — Rashi's etymology, now describing a substance rather than a viewer. Chavel's English shows on Sefaria as CC BY, which is surprising for a 1971 Shilo text: licence key chavel-ramban is marked for checking before publication. The paragraph that precedes this one — creation from absolute nothing, and the hyle as the only thing created — belongs to K4 and is not sliced here.")

# ---------------------------------------------------------------- latin bench, patristic
add(id="basil-hex-2-4", work="basil-hex-lat", author="basil", tradition="latin",
    date=400, date_precision="circa", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Terra autem erat invisibilis et incomposita", "en": "But the earth was invisible and unordered"},
    original=latin("7608", "Terra autem, inquit, erat invisibilis et incomposita. Quomodo igitur", "cum aer ipse splendore carens esset obscurus.", 53),
    english={"text": "'But the earth,' he says, 'was invisible and unordered.' How then, when both elements, that is heaven and earth, were built with equal honour, was heaven complete while the ground was still unordered? Or what cause was there at all that it should be less than finished, and should not be visible? The full ordering of the earth is its own fruitfulness — that is, the sprouting of all plants, and the abundance of trees bearing fruit and bearing none, and the colours and scents of flowers, and the other things which, brought forth a little later at the divine command, adorned the ground. Since none of these yet existed, the word of Scripture rightly called it unordered. And we shall be right to say the same of heaven as unfinished, since it had not taken up its own adornment either, having not yet been lit by the brightness of the sun and the moon, nor crowned with the choirs of the stars. So you will not seem to turn aside from the truth if you call heaven too unordered. But he called the earth invisible for two reasons: either because man, the beholder of it, had not yet come forth, or because, lying hidden under the waters that then stood over it, it could in no way be seen. For the waters had not yet been gathered into their own basins, which the Lord afterwards, when they were collected into one, named seas. A thing is invisible either because it cannot be grasped by bodily eyes, as our mind cannot, or because it can indeed be seen by nature but is hidden by the covering of some body drawn over it, as iron is that lies in the deep. It is in this sense, then, that the earth is now to be thought called invisible, inasmuch as it was covered by the surface of the waters. And then, since light was not yet established, it is no wonder if it was held invisible, when the air itself, lacking brightness, was dark.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-under-water", "pair-is-unfurnished"],
    notes="The Greek pair expounded as a report on conditions, and every answer is a physical one. Unordered means not yet fruitful — and Basil is willing to say heaven was unordered too, since it had no sun or stars yet, which no Latin after him will say. Invisible means either that there was no one to see it, or that it was under water; and he adds a small definition of invisibility that a modern reader can use — invisible as a mind is invisible, or invisible as iron lying at the bottom of the sea. Ibn Ezra reaches the second of these in Lucca seven centuries later from the Aramaic rather than the Greek. The paragraph that follows in Eustathius (PL 53:880C), against those who take the pair to prove an unbegotten matter, is a different argument and belongs to K4.")

add(id="ambrose-hex-1-7-25", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Quid est, Erat", "en": "What does 'was' mean?"},
    original=latin("6958", "Terra autem erat invisibilis et incomposita (Gen. I, 2) . Bonus artifex", "Erat ergo, ex quo facta est.", 14),
    english={"text": "'But the earth was invisible and unordered' (Gen 1:2). A good craftsman lays the foundation first; afterwards, the foundation laid, he distinguishes the parts of the building and adds the adornment. So, the foundation of the earth having been laid and the substance of heaven made firm — for these two are as it were the hinges of things — he wove in below: 'But the earth was invisible and unordered.' What does 'was' mean, unless it is said lest they stretch their opinion out to infinity and without a beginning, and say: See, matter, that is hyle, as the philosophers say, had no beginning even according to divine Scripture. But to those who say this you will answer that it is written: 'And Cain was a worker of the earth' (Gen 4:2). And of the man called Jubal, Scripture has: 'He was the father who showed forth the psaltery and the lyre' (Gen 4:21). And, 'There was a man in the land of Uz, whose name was Job' (Job 1:1). Let them stop raising a question about the word, especially since Moses has said beforehand that God made the earth. It was, then, from the time it was made.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["world-has-a-beginning", "pair-is-unfurnished"],
    notes="Ambrose does not argue about the pair at all; he argues about the verb standing in front of it. If the earth 'was' invisible and unordered, someone will say that the matter it was made of has no beginning, which is what the philosophers say of hyle — and the answer is grammatical and slightly impatient: Scripture says Cain 'was' a worker of the earth and Job 'was' in the land of Uz, and nobody makes them eternal. It was, from the time it was made. The image before it is the builder's: foundation first, then the parts distinguished, then the adornment, which is the order of the six days and is Basil's answer to the same question turned into a plan of work.")

add(id="aug-gnm-1-3-5", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-389", place="thagaste",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Quomodo fecit Deus in principio coelum et terram, si jam et terra erat invisibilis?", "en": "How did God make heaven and earth in the beginning, if the earth was already invisible?"},
    original=latin("7303", "Quod autem sequitur in libro Geneseos, Terra autem erat invisibilis", "vel derideat quia superbi sunt.", 34),
    english={"text": "What follows in the book of Genesis, 'But the earth was invisible and unordered', the Manichaeans find fault with in this way, saying: How did God make heaven and earth in the beginning, if the earth was already invisible and unordered? So, wanting to blame the divine Scriptures before they know them, they fail to understand even the plainest things. For what could have been said more plainly than what is said here: 'In the beginning God made heaven and earth; but the earth was invisible and unordered' — that is, In the beginning God made heaven and earth; but that very earth which God made was invisible and unordered, before God set out the forms of all things in their places and seats by an ordered distinction: before he said, 'Let there be light', and 'Let there be a firmament', and 'Let the waters be gathered', and 'Let the dry land appear', and the rest, which are set forth in order in the same book in such a way that little ones can take them in? All of which hold mysteries so great that whoever has learned them either grieves over the emptiness of all the heretics, because they are men, or laughs at it, because they are proud.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-formless-matter"],
    notes="The crux in the sharpest form anyone puts it, and it is put by an opponent: if God made the earth in the beginning, how was it already invisible and unordered? The objection assumes the pair describes something God had not yet made, and Augustine's whole answer is a single word of grammar — 'that very earth which God made was invisible and unordered', before he distinguished the forms of things. Everything the Latin bench does with this verse for the next eight hundred years is a development of that reading of the sentence. Note the lemma: Augustine's text is the Old Latin invisibilis et incomposita, from the Greek, and not Jerome's inanis et vacua, which he never quotes.")

add(id="aug-conf-12-4", work="aug-conf", author="augustine", tradition="latin",
    date=400, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Quid ergo vocaretur … nisi usitato aliquo vocabulo?", "en": "What then was it to be called, if not by some familiar word?"},
    original=latin("7270", "Quid ergo vocaretur, quod etiam sensu tardioribus", "vel ignorare noscendo.", 32),
    english={"text": "What then was it to be called, so as to be conveyed even to those slower of understanding, if not by some familiar word? And what can be found in all the parts of the world nearer to complete formlessness than earth and the deep? For they are less comely, in their lowest degree, than all the other higher things, translucent and full of light. Why then should I not accept that the formlessness of matter — which you had made without form, that from it you might make a world of form — was so conveniently intimated to men that it should be called 'earth invisible and unordered'? [Chapter V. Why formless matter seems to be so called.] So that when thought searches in it for what sense may reach, and says to itself, It is not an intelligible form like life, like justice, since it is the matter of bodies; nor is it perceptible by sense, since what may be seen and what may be felt is not in the invisible and unordered — while human thought says this to itself, let it try either to know it by not knowing, or to be ignorant of it by knowing.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-a-name-for-us"],
    notes="The answer that takes the question away. The pair is not a description of the earth and not the name of a thing: it is the most serviceable word available for formlessness, chosen because earth and the deep are what slower minds already know as the least comely things there are. Augustine keeps it strictly as a name — formless matter is neither an intelligible form like justice nor anything the senses can reach, so the mind can only try to know it by not knowing. That is the exact opposite of the Chagigah baraita, which answers the same question by pointing at a green line and a heap of stones.")

add(id="aug-conf-12-21", work="aug-conf", author="augustine", tradition="latin",
    date=400, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Aliud sibi tollit qui dicit", "en": "One man takes one thing for himself when he says"},
    original=latin("7270", "Item quod attinet ad intellectum verborum sequentium", "usitatis notisque creaturis.", 32),
    english={"text": "Again, as regards the understanding of the words that follow, out of all those true meanings one man takes this for himself when he says: 'But the earth was invisible and unordered, and darkness was over the deep' — that is, That bodily thing which God made was still the formless matter of bodily things, without order, without light. Another when he says: 'But the earth was invisible and unordered, and darkness was over the deep' — that is, This whole which was called heaven and earth was still formless and dark matter, out of which bodily heaven and bodily earth were to be made, with all the things in them known to the bodily senses. Another when he says: 'But the earth was invisible and unordered, and darkness was over the deep' — that is, This whole which was called heaven and earth was still formless and dark matter, out of which was to be made the intelligible heaven, which is elsewhere called the heaven of heaven (Ps 115:16 [Vg 113:16]); and earth, that is, every bodily nature, under which name this bodily heaven too is to be understood: that is, out of which every invisible and visible creature was to be made. Another when he says: 'But the earth was invisible and unordered, and darkness was over the deep' — Scripture did not call that formlessness by the name of heaven and earth; rather, he says, that formlessness which he named 'earth invisible and unordered' and 'the dark deep' already was, and out of it, as he had said beforehand, God made heaven and earth, that is, the spiritual and the bodily creature. Another when he says: 'But the earth was invisible and unordered, and darkness was over the deep' — that is, A certain formlessness was already the matter out of which Scripture said beforehand that God made heaven and earth: namely the whole bodily mass of the world, divided into two greatest parts, the upper and the lower, with all the familiar and known creatures in them.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-many-senses", "pair-is-formless-matter"],
    notes="Augustine sets out five readings of this one clause, each introduced with the same formula, and does not choose. They differ over what the formlessness is the matter of — bodies only, or the whole of heaven and earth, or the intelligible heaven as well — and over whether Scripture called that formlessness 'heaven and earth' in verse 1 or only named it here. His point is that all five are true and none of them can be shown to be Moses' own, so a reader who insists on one against the others is defending himself rather than Scripture. This is the only place on either bench where the plurality of answers is itself the answer, and it is worth setting beside Bereshit Rabbah 2, which likewise prints four readings of the pair without adjudicating — though there the readings are of history and here they are of physics.")

add(id="isidore-quaest-1-2", work="isidore-quaest", author="isidore", tradition="latin",
    date=620, date_precision="circa", place="seville",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Terra scilicet carnis nostrae", "en": "the earth, that is, of our flesh"},
    original=latin("21433", "Terra autem erat inanis et vacua. Terra scilicet carnis nostrae", "obscuritas corda nostra tegebat.", 83),
    english={"text": "'But the earth was empty and void.' The earth, that is, of our flesh was empty and void, before it received the form of doctrine. 'And darkness was upon the face of the deep', because the blindness of our sins and the deep obscurity of ignorance covered our hearts.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["allegorical"],
    answers=["pair-is-our-flesh"],
    notes="Two sentences that found a lineage. Isidore is not asking what the earth was; he says at the head of the work that he is setting down how the Church's teachers take these things spiritually, and the earth is the flesh of the reader before it has taken the form of doctrine. Wigbod copies it verbatim, Rabanus copies it verbatim (PL 107:467A), Remigius has it at PL 131:55D, and Bruno of Segni turns the same move on the Church rather than the soul. It is the one Latin reading of the pair that does not ask a question about the world at all — and it is, in its structure, what Bereshit Rabbah 2:3 does with the generations.")

add(id="alcuin-int-30", work="alcuin-int", author="alcuin", tradition="latin",
    date=796, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Invisibilis propter obscuritatem; incomposita propter deformitatem", "en": "Invisible because of darkness; unordered because of shapelessness"},
    original=latin("21416", "Inter. 30. Quid est: Terra autem erat invisibilis et incomposita", "incomposita propter deformitatem.", 100),
    english={"text": "Question 30. What is: 'But the earth was invisible and unordered' (ibid., from the Septuagint version)? — Answer. Invisible because of darkness; unordered because of shapelessness.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal", "translation"],
    answers=["pair-is-under-water", "pair-is-formless-matter"],
    notes="The whole crux compressed into eight words for the schoolroom, and the most interesting thing about it is the parenthesis: 'ex vers. LXX'. Alcuin knows he is expounding a lemma that is not in the Bible his pupils carry, and says so. He splits the pair between the two answers the Latin bench will keep — invisible has to do with light, unordered with form — and gives no reason for either. Angelomus takes this answer over word for word two generations later and puts it inside a discussion of Jerome's text, where it becomes a gloss on 'the other translation'.")

add(id="wigbod-gen-1-2-tohu", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="aachen",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Cur inanis et vacua?", "en": "Why 'empty and void'?"},
    original=latin("8606", "D. Terra autem erat inanis et vacua (Gen. I, 2) . Cur inanis et vacua?", "priusquam doctrinae acceperit formam.", 96),
    english={"text": "D. 'But the earth was empty and void' (Gen 1:2). Why empty and void? M. That is, because it was not divided off from the sea; void, he says, because it was not surrounded by shores, nor adorned with its own furnishings, that is, with trees and animals. Likewise spiritually: the earth, namely, of our flesh was empty and void, before it received the form of doctrine.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal", "allegorical"],
    answers=["pair-is-unfurnished", "pair-is-our-flesh"],
    notes="The crux asked as a schoolroom question — Cur inanis et vacua? — and answered twice, once about coastlines and once about the soul; the second answer is Isidore word for word. What makes this witness matter is not the answer but where it stands. Five columns earlier, at PL 96:1111B, the same compilation prints Augustine's Manichaean paragraph on the same verse under the Old Latin lemma, terra invisibilis et incomposita, and at 1114C it prints Augustine again on the same words. Here it reads the Vulgate's lemma and asks a different question of it. Wigbod does not notice, and neither does the reader: the two Latin texts of Gen 1:2 sit in one book without a seam.")

# ---------------------------------------------------------------- latin bench, Carolingian to the Glossa
add(id="angelom-gen-1-2-tohu", work="angelom-gen", author="angelomus", tradition="latin",
    date=850, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Unde alia translatio dicit: Invisa et incomposita", "en": "Whence another translation says: unseen and unordered"},
    original=latin("9032", "Sequitur: VERS. 2.-- Terra autem erat inanis et vacua. Cum superius ait", "manet semper quietum.", 115),
    english={"text": "There follows, verse 2: 'But the earth was empty and void.' Since he said above, 'God created heaven and earth', why is it said, 'But the earth was empty and void'? — unless because that formless matter, which is called by the name of earth, was empty and void. Empty, that is, unordered and not yet gathered into its own kinds. Void, because it was free of any fruits to be brought forth. Whence another translation says: 'unseen and unordered'. Unseen because of darkness, unordered because of shapelessness, since it was still wholly covered by the deep, that is, by the measureless depth of the waters. Whence, by what he says — 'But the earth was empty and void' — it can be understood what kind of heaven it was that he had made first: namely that, set apart from all the turning state of this world, it remains always at rest in the divine presence.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal", "translation"],
    answers=["pair-is-formless-matter", "pair-is-under-water", "pair-is-not-of-heaven"],
    notes="A ninth-century compiler doing, in one paragraph, what this crux exists to show. He asks the Vulgate's question, answers it with Augustine's unformed matter, then reaches for the other version — 'unseen and unordered' — and glosses it with Alcuin's eight words from Interrogatio 30, unattributed; then he turns to Bede's argument that the phrase is withheld from heaven, and copies Bede's sentence about the heaven set apart from the turning of this world. Three sources and two Latin translations, spliced without a join. His 'invisa' for 'invisibilis' is his own or his exemplar's.")

add(id="remigius-gen-1-2-tohu", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Inutilis, infructuosa et incomposita", "en": "Useless, unfruitful, and unordered"},
    original=latin("9346", "Vers. 2. Terra autem inanis et vacua. Id est, inutilis", "supercoelestes aquae retinent.", 131),
    english={"text": "Verse 2. 'But the earth was empty and void.' That is, useless, unfruitful, and unordered. For all the elements were mingled and confused, and this whole space of air which is from the earth up to heaven was full of waters — which, however, were not of the same quality as they now are, but thin, after the manner of clouds, a quality which those waters above the heavens still keep.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-unfurnished", "pair-is-under-water"],
    notes="Three adjectives that outlived their author. 'Useless, unfruitful, and unordered' is the gloss the Glossa Ordinaria prints on this lemma under the siglum STRAB., word for word and with the sentence about the mingled elements and the thin waters after it; from the Glossa it reaches Comestor, who keeps 'useless and unfruitful' and drops 'unordered'. The last clause is worth noticing on its own: the waters above the firmament still have the quality the primordial waters had, so that a reader can look up and see what verse 2 was talking about.")

add(id="bede-gen-1-2-tohu", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="circa", place="jarrow",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Ut quid enim haec de terra, praetermisso coelo, intulit?", "en": "Why did he say these things of the earth and pass heaven by?"},
    original=latin("8466", "Terra autem erat inanis et vacua, et tenebrae super faciem abyssi. Ut quid enim", "et jubilarent omnes filii Dei (Ibid., 7)", 91),
    english={"text": "'But the earth was empty and void, and darkness upon the face of the deep.' For why did he say these things of the earth, passing heaven by, unless because he wanted nothing of the sort understood of heaven? For that is the heaven above, which, set apart from all the turning state of this world, remains always at rest [in the glory of the divine foreknowledge]. As for our heaven, in which are set the lights necessary to this age, Scripture declares in what follows both how and when it was made. That heaven above, then, which is unreachable by the sight of all mortals, was not created empty and void as the earth was, which in its first creation brought forth nothing of green shoots or of living creatures — because, of course, as soon as it was created it was filled with its own inhabitants, that is, with the most blessed ranks of the angels; and that these were founded in the beginning together with heaven and earth, and at once referred their own founding, and that of the whole first creation, to the praise of the Creator, the Founder himself bears witness, who speaking to his holy servant Job says: 'Where were you when I laid the foundations of the earth?' (Job 38:4), and a little after: 'When the morning stars praised me together, and all the sons of God shouted for joy' (Job 38:7).", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-not-of-heaven", "pair-is-unfurnished"],
    notes="Bede answers the crux by asking what the verse does not say. The pair is predicated of the earth and withheld from heaven, and that silence is information: the upper heaven was not empty, because it was filled with its inhabitants as soon as it was made, and Job 38:7 supplies the angels singing at the founding. It is the argument Abelard will make four hundred years later from the adversative conjunction, and the Glossa carries it in the margin at the head of verse 2. The Corpus Corporum text reads 'divinae gloria praescientiae' where Angelomus and the Glossa both have 'divinae praesentiae'; the English brackets the phrase. [CHECK the PL plate.]")

add(id="glossa-1-2-terra", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Terra autem erat inanis", "en": "But the earth was empty"},
    original=latin("8950", "VERS. 2.-- « Terra autem erat inanis, » etc. (BEDA, Hexaem. tom. II.)", "quomodo vel quando factum sit postea dicit.", 113),
    english={"text": "Verse 2. « But the earth was empty, » etc. [n: (BEDE, Hexaemeron, vol. II.)] He shows which heaven, and of what kind, was made in the beginning together with the earth. For he adds this of the earth, which he did not want understood of heaven. For that upper heaven, which is set apart from the turning of the world, as soon as it was created was filled with the holy angels — whom the Lord bears witness were founded in the beginning together with heaven and earth, saying in Job 38: « Where were you when the morning stars praised me, and all the sons of God shouted for joy? » He calls the same angels morning stars and sons of God. For of the heaven in which the lights are set, he says afterwards how and when it was made.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-not-of-heaven"],
    notes="The gloss that stands at the head of verse 2 in the margin, labelled BEDA and compressing his paragraph to five sentences, keeping Job 38:7 and the two heavens. The second gloss on this lemma — Walahfrid's 'useless, unfruitful, and unordered', which is Remigius verbatim — is already on the site inside the K7 witness glossa-1-2-ruach, where Wilson's edition appended it; it is not sliced again here. A third gloss, again from Bede, follows on 'and there was darkness' and ends by naming earth and water as the unformed matter: that belongs to K4. English here is a fresh draft, superseded when Wilson's Glossa edition reaches this lemma.")

# ---------------------------------------------------------------- latin bench, twelfth century
add(id="bruno-gen-1-2-tohu", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1100, date_precision="circa", place="segni",
    anchor={"verse": "gen.1.2"}, lemma={"la": "absque liberis erat Ecclesia", "en": "the Church was without children"},
    original=latin("21403", "Adhuc tamen inanis et vacua erat terra", "tantorum filiorum plenitudine inhabitata.", 164),
    english={"text": "Still, however, the earth was empty and void, still unfruitful, and the Church was without children — she whom the prophet also, comforting her for her barrenness and promising fruitfulness, addressed: « Rejoice, barren one, who do not bear; break forth and cry out, you who do not travail, for many are the children of the desolate, more than of her who has a husband » (Isa 54:1; Gal 4:27). But why empty and void? Because darkness was still upon the face of the deep. For no one understood the Scriptures, deep as they are and wrapped in the darkness of ignorance — which, that they may be understood, « deep calls unto deep » (Ps 42:7 [Vg 41:8]). But Christ took away this darkness when he opened the apostles' understanding, that they might understand the Scriptures. For if the Jews understood them, they would take refuge in the Church; but because, as the Apostle says, « to this day, while Moses is read, a veil is placed over their hearts » (2 Cor 3:15), they are not able to understand them. But when the fullness of the Gentiles has come in, then, the veil taken away, Israel shall be saved (Rom 11:25). For our earth shall no longer be called empty and void, inhabited by the fullness of so many sons.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["allegorical"],
    answers=["pair-is-history", "pair-is-our-flesh"],
    notes="Isidore's allegory moved off the individual soul and onto history: the empty earth is the Church before she had children, the darkness on the deep is the unread Scripture, and the emptiness ends not at the third day but at the end — when the fullness of the Gentiles has come in and Israel is saved, the earth will no longer be called empty and void. Structurally this is Bereshit Rabbah 2:3, which reads the same clause as the generations from Adam to Abraham and ends with the morning of Jacob; and it is Resh Lakish's four kingdoms in 2:4, which ends with the spirit of the Messiah. Three readings of one clause as a periodization of sacred history, with the same shape and opposite contents, and no possible contact. Bruno's Corpus Corporum text carries a stray '3' before 'ad Ecclesiam confugerent', which is dropped here as a printer's mark.")

add(id="rupert-gen-1-2-tohu", work="rupert-gen", author="rupert", tradition="latin",
    date=1114, date_precision="circa", place="liege",
    anchor={"verse": "gen.1.2"}, lemma={"la": "inanis ab omni germine … vacua a cunctis animantibus", "en": "empty of every shoot … void of all living things"},
    original=latin("10873", "Caeterum secundum quod jam dictum est, terra erat inanis et vacua", "quae nunc in ea moventur.", 167),
    english={"text": "For the rest, according to what has already been said, the earth was empty and void, because the Creator had not yet separated it as dry land from the waters, had not yet made it firm, had not yet clothed it with the mantle of the stars of this heaven, had not yet furnished it with so many kinds of creatures. And so, if you consider the letter carefully, the earth was not created in the beginning with the visible appearance of its own which it now shows, but was empty — empty, that is, of every shoot which is now rooted in it — and void, namely of all the living things which now move in it.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-unfurnished"],
    notes="'If you consider the letter carefully' — and the letter, considered carefully, yields a list of what was not there yet: dry land, firmness, stars, kinds. Rupert then splits the pair the way the twelfth century regularly splits it, empty of shoots and void of animals, which is Abelard's division (fruit and inhabitant) and Hugh's in the Adnotationes (seeds and shoots) with the terms moved about. None of the three cites another, and the distribution of the two terms differs each time: what they share is the conviction that the pair is a pair, and that each word must be given its own privation.")

add(id="abelard-hex-1-2-tohu", work="abelard-hex", author="abelard", tradition="latin",
    date=1130, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.2"}, lemma={"la": "ex illa apposita conjunctione adversativa", "en": "from that adversative conjunction set beside it"},
    original=latin("11118", "Terra autem erat inanis et vacua. Quoniam ad hominis creationem", "de divinis operibus deesse videatur.", 178),
    english={"text": "'But the earth was empty and void.' Since this treatise looks especially to the creation of man, who was to be formed from the earth and to live on the earth — in which the prophet, as we have said, intending to draw man to the worship of God, turned his pen to earthly works, passing over the creation of the heavenly and higher nature, that is the angelic; lest perhaps, if he examined it and displayed its excellence to the praise of its Creator, he should draw man less to the love of God, seeing another nature preferred to himself. And so, having said first that the earth in its creation stood empty and void, he declares by the works of the later days how the divine working afterwards saw to its emptiness and its voidness. He calls the earth empty of fruit, which it had not yet brought forth; void of an inhabitant, not only of man but of every kind of living thing whatever, since as yet no dwelling, whether of land or of water, held any living things — both of which, as we have said, he takes in under the word 'earth'. And so he calls 'earth', according to what has been set out, this lower region of the world consisting of the heavy elements. And it is to be noted that when he says 'but the earth was empty and void', he hints, from that adversative conjunction set beside it, that heaven is not to be so understood — since the angels are understood to have been created either before heaven itself or together with heaven, and are called, as it were, the dwellers in heaven; so that although the prophet does not pursue their creation, he yet touches it in passing, lest anything should seem missing from his account of the divine works.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-unfurnished", "pair-is-not-of-heaven"],
    notes="Abelard gets Bede's conclusion out of a single word. 'Terra AUTEM erat inanis et vacua': the adversative conjunction implies a contrast, so what is said of the earth is being denied of heaven, and heaven is not empty because the angels are its inhabitants — whose creation Moses passes over on purpose, lest man, drawn to the worship of God, should see another nature preferred to himself. That last reason is Abelard's own and belongs to no one else on this crux. The division of the pair — empty of fruit, void of an inhabitant — matches Rupert's and Hugh's without citing either.")

add(id="hugh-adnot-1-2-tohu", work="hugh-adnot", author="hugh-of-st-victor", tradition="latin",
    date=1130, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Inanis a seminibus; vacua a germinibus", "en": "Empty of seeds; void of shoots"},
    original=latin("11054", "Terra autem erat inanis et vacua. Inanis a seminibus", "non erat nisi aer et nebula.", 175),
    english={"text": "'But the earth was empty and void.' Empty of seeds; void of shoots; or empty on account of its hollowness; void, because in so great a hollowness of the earth there was nothing but air and mist.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-unfurnished"],
    notes="The school formula at its shortest, and it gives two distributions rather than one: empty of seeds and void of shoots — or else empty because the earth was hollow and void because there was nothing in the hollow but air and mist. The second is a physical picture, and it is the one Hugh's own Adnotationes go on to develop in the sentences on the mist, the deep and the waters that are built as the K7 witness hugh-adnot-gen-1-2, immediately after this.")

add(id="hugh-sacr-1-1-tohu", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.2"}, lemma={"la": "sive, ut alia translatio habet, incomposita", "en": "or, as another translation has it, unordered"},
    original=latin("11082", "Terra autem erat inanis et vacua (Gen. I) ; sive, ut alia translatio habet", "formandorum materia continebatur.", 176),
    english={"text": "'But the earth was empty and void' (Gen 1) — or, as another translation has it, « unordered » — 'and darkness was upon the face of the deep' (ibid.). For by 'heaven and earth' I think there is signified in this place that matter of all things heavenly and earthly, out of which were afterwards made, one after another, in form, the things which had first been created in it together in their essence. For there 'earth' was the element of earth itself, and 'heaven' was that mobile and light confusion of the remaining three, which was carried suspended around the earth lying in the middle; and in these two was contained the matter of all bodies, heavenly or earthly, that were to be formed.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["translation", "literal"],
    answers=["pair-is-formless-matter"],
    notes="The first plain statement on the Latin bench that there is another translation of this clause. Hugh quotes the Vulgate's lemma, gives the Old Latin word in the same breath, and then goes on to Augustine's reading — heaven and earth name the matter of everything, in which all things were made together in essence before they were made one after another in form. He does not say which text is better, or where the other comes from; he simply will not let a reader think there is only one. Alcuin had named the Septuagint three hundred years earlier and then expounded the Greek lemma as if it were the Bible; Hugh names the variant while expounding the Vulgate. Wigbod printed both, five columns apart, and said nothing.")

add(id="comestor-hs-1-2-tohu", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.2"}, lemma={"la": "machina mundialis adhuc erat inutilis", "en": "the world-machine was still useless"},
    original=latin("11575", "Terra autem erat inanis et vacua (Gen. I) , id est machina mundialis", "Unde et Graecus eam chaos dixit.", 198),
    english={"text": "'But the earth was empty and void' (Gen 1) — that is, the world-machine was still useless, and unfruitful, and void of its adornment. 'And darkness was upon the face of the deep.' The same machine which he had called earth he calls the deep, on account of its confusion and darkness. Whence the Greek called it chaos.", **APPROVED},
    cruxes=["tohu-vabohu"], senses=["literal"],
    answers=["pair-is-unfurnished", "pair-is-formless-matter"],
    notes="The gloss arrives at the Paris schools in its final form: Remigius' three adjectives, minus one, applied not to the earth but to the machina mundialis, the world considered as a piece of apparatus not yet fit for use. Comestor then identifies the deep with what the Greeks call chaos, which is the classical name the earlier bench avoids — Abelard, in the sentences that follow the slice built here (PL 178:734D), had said that 'certain of the philosophers or poets called this confusion chaos' and kept his distance; Comestor states it as a fact of vocabulary. From here it goes into the Historia's readership, which is everyone.")

# ---------------------------------------------------------------- threads (K6)
THREADS = [
 E("t-k6-01", "vulgate-1-2", "lxx-1-2", "transmits", "Jerome renders tohu va-vohu 'inanis et vacua', where the Greek had ἀόρατος καὶ ἀκατασκεύαστος and the Old Latin 'invisibilis et incomposita'. The two Latin lemmas ask different questions — what the earth looked like, and what it lacked — and both are on the bench from the fifth century on."),
 E("t-k6-02", "aug-gnm-1-3-5", "lxx-1-2", "transmits", "Augustine's lemma throughout is 'terra invisibilis et incomposita', the Old Latin of the Greek pair; he never quotes Jerome's 'inanis et vacua' on this verse, in the Manichaean books, the Confessions or De Genesi ad litteram."),
 E("t-k6-03", "basil-hex-2-4", "lxx-1-2", "transmits", "Basil expounds ἀόρατος καὶ ἀκατασκεύαστος word by word — invisible for two reasons, unordered because not yet fruitful — and Eustathius' Latin keeps the Old Latin pair, so the Greek argument reaches the Latin bench with its lemma intact."),
 E("t-k6-04", "ambrose-hex-1-7-25", "basil-hex-2-4", "echoes", "Basil asks why, of two elements built with equal honour, heaven was complete and the earth still unordered; Ambrose answers with the good craftsman who lays a foundation before he distinguishes the parts and adds the adornment. Ambrose is expounding Basil's Hexaemeron through this book (cf. the Syrian at K7)."),
 E("t-k6-05", "aug-conf-12-21", "aug-gnm-1-3-5", "echoes", "The first of the five readings set out in Confessions XII.21 — 'that bodily thing which God made was still the formless matter of bodily things, without order, without light' — is the answer Augustine had given the Manichaeans thirteen years earlier; in the Confessions it is one true reading among five rather than the reading."),
 E("t-k6-06", "alcuin-int-30", "lxx-1-2", "transmits", "Alcuin's question carries its own source-note, '(Ibid. ex vers. LXX)': he knows the lemma he is glossing is the Septuagint's and not the text his pupils read."),
 E("t-k6-07", "angelom-gen-1-2-tohu", "alcuin-int-30", "echoes", "'Invisa propter obscuritatem, Incomposita propter deformitatem' is Alcuin's answer to Interrogatio 30 word for word, unattributed, with 'invisa' for 'invisibilis' — and Angelomus has moved it inside a discussion of the Vulgate's lemma, where it glosses 'the other translation'."),
 E("t-k6-08", "angelom-gen-1-2-tohu", "bede-gen-1-2-tohu", "echoes", "'quale sit coelum, quod primum condiderat, potest intelligi, videlicet quod ab omni hujus mundi volubili statu secretum … manet semper quietum' is Bede's sentence (PL 91:13C), unnamed; Angelomus reads 'divinae praesentiae' where the Corpus Corporum Bede prints 'divinae gloria praescientiae'."),
 E("t-k6-09", "glossa-1-2-terra", "bede-gen-1-2-tohu", "cites", "The gloss is labelled '(BEDA, Hexaem. tom. II.)' and compresses Bede's paragraph — the two heavens, the upper one filled with angels as soon as it was made, Job 38:7 with the morning stars glossed as the angels — to five sentences."),
 E("t-k6-10", "glossa-1-2-ruach", "remigius-gen-1-2-tohu", "cites", "The gloss Migne prints under '(STRAB.)' on this lemma — 'Inanis et vacua. Inutilis scilicet, et infructuosa, et incomposita. Omnia enim elementa commixta, confusa, et totum hoc aeris spatium aquis plenum; non quales nunc sunt, sed sicut nebulae tenues' — is Remigius of Auxerre at PL 131:55A, verbatim to the last clause about the waters above the heavens."),
 E("t-k6-11", "comestor-hs-1-2-tohu", "glossa-1-2-ruach", "echoes", "'machina mundialis adhuc erat inutilis, et infructuosa, et vacua ornatu suo' keeps two of the Glossa's three adjectives and replaces the third ('incomposita') with a phrase of his own; the subject has moved from the earth to the world-machine."),
 E("t-k6-12", "wigbod-gen-1-2-tohu", "isidore-quaest-1-2", "cites", "'Item spiritaliter: Terra scilicet carnis nostrae inanis et vacua erat, priusquam doctrinae acceperit formam' is Isidore, Quaestiones in Genesim I.2 (PL 83:209B), verbatim."),
 E("t-k6-13", "wigbod-gen-1-2-tohu", "aug-gnm-1-3-5", "cites", "The same compilation prints Augustine's Manichaean paragraph on this verse verbatim at PL 96:1111B under the Old Latin lemma 'terra invisibilis et incomposita', five columns before it asks 'Cur inanis et vacua?' under the Vulgate's. One book, two Latin texts of Gen 1:2, no seam."),
 E("t-k6-14", "abelard-hex-1-2-tohu", "bede-gen-1-2-tohu", "parallel", "Both withhold the pair from heaven on the ground that heaven had its inhabitants from the first: Bede from the silence ('why did he say these things of the earth, passing heaven by?'), Abelard from the adversative conjunction in 'terra AUTEM erat inanis'. Abelard does not name Bede, and the reasons for the angels' being passed over are different."),
 E("t-k6-15", "abelard-hex-1-2-tohu", "rupert-gen-1-2-tohu", "parallel", "The same split of the pair into two privations, sixteen years apart and with the terms distributed differently: Abelard, empty of fruit and void of an inhabitant; Rupert, empty of every shoot and void of all living things. No citation either way."),
 E("t-k6-16", "hugh-adnot-1-2-tohu", "abelard-hex-1-2-tohu", "parallel", "'Inanis a seminibus; vacua a germinibus' is the same operation again with a third distribution — and Hugh then offers a fourth, hollowness and the mist in the hollow, as an alternative in the same breath. The formula is school property by 1130; no one on this crux claims it."),
 E("t-k6-17", "hugh-sacr-1-1-tohu", "lxx-1-2", "cites", "'sive, ut alia translatio habet, « incomposita »' names the variant in the act of expounding the Vulgate — the first place on this bench where a reader is told plainly that the clause exists in two Latin forms."),
 E("t-k6-18", "hugh-sacr-1-1-tohu", "aug-conf-12-21", "parallel", "Hugh's reading — 'heaven and earth' name the matter of all things heavenly and earthly, in which all were created together in essence before they were made one after another in form — is Augustine's fifth reading in Confessions XII.21, reached without citation and stated as the single sense rather than as one of five."),
 E("t-k6-19", "bruno-gen-1-2-tohu", "br-2-3", "parallel", "The same clause read as a periodization of sacred history, from opposite ends. R. Yehuda bar Simon: tohu is Adam, va-vohu is Cain, the darkness is the generation of Enosh, the deep is the Flood, 'let there be light' is Abraham. Bruno: the earth is empty while the Church is without children, the darkness is the unread Scripture, and the emptiness ends when the fullness of the Gentiles has come in and Israel is saved. No contact is possible; the shape is identical and the contents are opposed."),
 E("t-k6-20", "bruno-gen-1-2-tohu", "isidore-quaest-1-2", "echoes", "Isidore's 'terra carnis nostrae', the flesh before it takes the form of doctrine, moved from the soul to the Church: Bruno's 'terra nostra' will no longer be called empty and void when it is inhabited by the fullness of so many sons."),
 E("t-k6-21", "rashi-1-2a", "br-2-2", "echoes", "Rashi's 'tohu is a word for astonishment and desolation, for a person would be astonished and appalled at the bohu in it' is the verb of Bereshit Rabbah 2:2, where the earth sits toheh u-voheh over her lot. The midrash's parable has become a lexical entry, and the one who is astonished has changed from the earth to the reader."),
 E("t-k6-22", "rashi-1-2a", "targ-onk-1-2", "echoes", "Rashi glosses bohu as 'reikut ve-tzadu', emptiness and waste — the two Aramaic words Onkelos uses to render the whole pair, 'tzadya ve-reikanya', in the other order. Rashi's peshat on the pair is the targum's, split between the two Hebrew words."),
 E("t-k6-23", "ibn-ezra-1-2", "b-chag-12a-tohu", "contests", "'Now in Sefer Yetzira: tohu — this is the green line, and bohu — these are the mefulamot stones. What is correct is as the Aramaic translator said.' Ibn Ezra names the tradition the Chagigah baraita carries and sets it aside in favour of Onkelos: the pair is a privation, not two objects."),
 E("t-k6-24", "ibn-ezra-1-2", "targ-onk-1-2", "cites", "'as the Aramaic translator has said' — Onkelos' tzadya ve-reikanya, supported from 'the howling waste of tohu' (Deut 32:10) and 'after tohu' (1 Sam 12:21), where the word means without substance."),
 E("t-k6-25", "ramban-1-2-tohu", "b-chag-12a-tohu", "echoes", "Both build on Isa 34:11, 'the line of tohu and the stones of bohu', and read it as an inventory of what tohu and bohu are. The baraita: a green line encircling the world, and slimy stones sunk in the deep. Ramban: the cord with which the craftsman marks out the plan of his building, and the stones as the forms in it. Ramban cites Sefer Yetzirah by name in the same paragraph, so the tradition is in front of him."),
 E("t-k6-26", "ramban-1-2-tohu", "rashi-1-2a", "echoes", "Ramban quotes the Bahir's R. Berekhya — 'what is tohu? a thing which astonishes people' — which is Rashi's etymology from the same root; but in Ramban the thing that astonishes is the primary matter itself, which cannot hold a name, rather than the sight of an empty land."),
 E("t-k6-27", "ramban-1-2-tohu", "ibn-ezra-1-2", "contests", "Ibn Ezra sets Sefer Yetzirah's green line aside and takes tohu as 'without substance', following Onkelos; Ramban keeps Sefer Yetzirah, cites it approvingly, and makes tohu a substance — the hyle — with bohu for its form. The two commentators Ramban reads side by side on 1:1 divide here on whether the word names anything at all."),
 E("t-k6-28", "br-2-3", "br-2-1", "echoes", "Both hang on Jer 4:23, 'I have seen the land, and behold, it is tohu va-vohu'. The prophet's re-use of the phrase for a land under judgement is what licenses the whole series of historical readings in Bereshit Rabbah 2; no Latin witness on this crux cites Jer 4:23 at all."),
 E("t-k6-x1", "bruno-gen-1-2-tohu", "br-2-4", "parallel", "Phase 4. Both read the whole of Gen 1:2 as a periodization of sacred history running to a final redemption, and neither could have known the other. Resh Lakish: tohu is Babylon (Jer 4:23), va-vohu Media, the darkness Greece, the deep Edom, and the spirit hovering is the spirit of the messianic king (Isa 11:2). Bruno of Segni reads the same clause as the ages of the Church. Written at Phase 4 because `br-2-4` was built for K7 and did not carry this crux until then."),
]

FINDING = ("The Latin bench is not reading one verse but two. Augustine, Ambrose, Basil-in-Latin and Alcuin expound "
           "'invisibilis et incomposita', the Old Latin of the Septuagint's ἀόρατος καὶ ἀκατασκεύαστος, and answer a "
           "question about visibility and order; Jerome's 'inanis et vacua' asks instead what the earth lacked, and its "
           "heirs answer with seeds, shoots and living things. Wigbod prints both, five columns apart, without noticing; "
           "Angelomus splices them in one paragraph; Hugh of St Victor is the first to tell a reader plainly that there "
           "is another translation. Jerome himself never glosses the pair he made — the Hebrew Questions go straight "
           "from 'in principio' to 'Spiritus Dei ferebatur', and the phrase that shaped the Latin Middle Ages on this "
           "verse is left without a note by the man who wrote it.")

# ---------------------------------------------------------------- persons / places / answers this crux adds
PERSONS = {
 "r-abahu": {"name": "R. Abahu", "he": "רַבִּי אַבָּהוּ", "dates": "c. 250–320", "tradition": "rabbinic", "role": "tradent"},
}

PLACES = {}

ANSWERS = {
 "pair-is-formless-matter": {"label": "Unformed matter", "gloss": "The pair names the matter God had made and not yet given form to (Augustine, Angelomus, Hugh, Comestor)."},
 "pair-is-under-water": {"label": "Hidden under the waters", "gloss": "Invisible because the waters covered it, and because there was neither light nor anyone to see (Basil, Alcuin, Angelomus, Ibn Ezra)."},
 "pair-is-unfurnished": {"label": "No seed, no living thing", "gloss": "Empty of shoots and void of animals: a list of what was not there yet (Bede, Remigius, Rupert, Abelard, Hugh, Comestor, the targums)."},
 "pair-is-a-name-for-us": {"label": "A name fitted to slow minds", "gloss": "Not a description but the most serviceable word for formlessness, since earth and the deep are the least comely things men know (Augustine, Confessions XII)."},
 "pair-many-senses": {"label": "More than one true reading", "gloss": "Five readings of the clause are all true and none can be shown to be Moses' own (Augustine, Confessions XII.21)."},
 "pair-is-two-things": {"label": "A green line and slimy stones", "gloss": "Tohu and bohu are two creatures made on the first day: a line encircling the world, and stones sunk in the deep (b. Chagigah 12a, Sefer Yetzirah)."},
 "pair-is-matter-and-form": {"label": "Matter and its form", "gloss": "Tohu is the hyle, which can hold no name; bohu is bo hu, the form it puts on (Ramban)."},
 "pair-is-astonishment": {"label": "Astonishment", "gloss": "Tohu is what astonishes whoever looks at it — the earth bewildered at her lot, or the reader appalled at the emptiness (Bereshit Rabbah 2:2, Rashi, the Bahir)."},
 "pair-is-history": {"label": "The verse tells history", "gloss": "The clause is the first term of a periodization: the generations from Adam, the four kingdoms, or the Church before her children (Bereshit Rabbah 2:1, 2:3, 2:4; Bruno)."},
 "pair-is-our-flesh": {"label": "The earth of our flesh", "gloss": "The soul before it has taken the form of doctrine (Isidore, Wigbod, Rabanus, Remigius, Bruno)."},
 "pair-is-not-of-heaven": {"label": "Said of earth, not of heaven", "gloss": "The phrase is withheld from heaven, which was filled with angels as soon as it was made (Bede, the Glossa, Angelomus, Abelard)."},
}

LICENSES = {}

# ---------------------------------------------------------------- Chalcidius (Phase 6 part four)
# ⚠ Not sliced from the PL TEI — Chalcidius is not in Migne. The Latin is transcribed from the page
# image of a public-domain print; the leaf is in `source`. See the fuller note in
# cruxes/beginning-of-what.py, where the person, place and licence key are defined.
add(id="chalcidius-terra-sylua", work="chalcidius-tim", author="chalcidius", tradition="latin",
    date=350, date_precision="range-300-400", place="cordoba",
    anchor={"verse": "gen.1.2"},
    lemma={"la": "cum sit omnium qualitatum receptrix, propriam nullam habet ex natura", "en": "since it is the receiver of all qualities, it has none of its own by nature"},
    original={"lang": "la", "text": "Terra autem erat inuisibilis et informis, hoc est sylua corporea uetus mundi substantia, prius quam efficta Dei opificis sollertia sumeret formas, etiam tunc decolor et omni carens qualitate. Quod uero tale est, inuisibile certe habetur et informe. Inanis porro et nihil propterea dicta, quia cum sit omnium qualitatum receptrix, propriam nullam habet ex natura. Sylua ergo, ut quae cuncta quae accidunt recipiat in se, inanis appellata, ut quae compleri nunquam posse uideatur. Porro quia sit expers omnium, nihil dicta. Otiosa uero et indigesta nuncupatur a Symmacho: quodque quidem per se nihil ualeat, otiosa; quod uero habeat opportunitatem suscipiendi ordinis ab exornante semet Deo mundum moliente, indigesta censetur. Stupide uero ex admiratione significatio animae uim quandam similitudinemque declarat, siquidem opificis et auctoris sui maiestate capta stuperet.",
              "source": "Paris 1520, fo. LVIII recto (archive.org bub_gb_LxGcsxR3tWgC, page/n116.jpg)",
              "license": "chalcidius-1520",
              "version": "Chalcidii viri clarissimi luculenta Timaei Platonis traductio, et eiusdem argutissima explanatio (Paris: Josse Bade, 1520)"},
    english={"text": "'But the earth was invisible and formless' — that is, corporeal hyle, the old substance of the world, before it took on forms fashioned by the skill of God the craftsman, still then colourless and lacking every quality. And what is such is certainly held to be invisible and formless. It is called 'empty' and 'nothing' for this reason: that since it is the receiver of all qualities, it has none of its own by nature. Hyle, then, as that which receives into itself all the things that happen, is called empty, as that which can never seem able to be filled. And because it is devoid of all things, it is called nothing. But it is named 'idle' and 'undigested' by Symmachus: idle, in that of itself it avails nothing; and it is reckoned undigested in that it has the fitness to receive order from God adorning it as he sets about the world. But the signification 'stupefied, out of wonder' declares a certain force and likeness of soul, since it would be stupefied, seized by the majesty of its craftsman and author.", **DRAFT},
    tradents=["symmachus-translator"],
    cruxes=["tohu-vabohu", "ex-nihilo-or-matter"], senses=["literal", "translation"],
    answers=["hyle-is-tohu", "pair-is-formless-matter", "matter-is-coeval"],
    notes="Tohu va-vohu given four Latin renderings in one paragraph, each explained, by the earliest Latin on this daf. Invisible and formless is hyle: the old corporeal substance of the world, colourless and without quality before the craftsman's skill gave it forms. Empty and nothing are explained by the receptacle argument in its clean Platonic form — it is called empty because it receives all qualities and has none of its own, and nothing because it is devoid of all things — which is what Augustine will grope toward in Confessions XII, calling it a nothing-something, and what the Gloss will flatten into materia informis. Symmachus's otiosa and indigesta are then glossed separately: idle because of itself it avails nothing, undigested because it has the fitness to receive order. And the reading Origen credits to the Hebrews, stupide ex admiratione, is given a psychological explanation — the earth would be stupefied, seized by the majesty of its maker. That last one is the crux's rabbinic answer arriving on the Latin bench and being taken seriously: Bereshit Rabbah 2:2 reads tohu va-vohu as tohe u-bohe, bewildered and astonished, and Rashi's word for tohu is astonishment. Alcuin, Angelomus and Hugh all know that alia translatio says inordinata, without knowing whose translation it is or that a fourth-century Latin had named him and explained the word."
)

# ---------------------------------------------------------------- threads (K6, Chalcidius block)
_E6 = lambda i, f, t, ty, ev: thread("tohu-vabohu", i, f, t, ty, ev)
THREADS.extend([
 _E6("t-k6-c1", "chalcidius-terra-sylua", "br-2-2", "parallel", "The rabbinic reading of tohu va-vohu reaches the Latin bench in the fourth century, is explained, and goes nowhere. Bereshit Rabbah 2:2 hears tohe u-bohe in the words — bewildered and astonished — and Rashi's word for tohu at Troyes is astonishment. Chalcidius reports, from Origen and credited to the Hebrews, an exemplar reading terra autem stupida quadam erat admiratione, and then glosses it: the signification declares a certain force and likeness of soul, since the earth would be stupefied, seized by the majesty of its maker. A Latin has the other bench's reading of this verse, with its psychology, seven hundred years before Rashi writes it down."),
 _E6("t-k6-c2", "chalcidius-terra-sylua", "angelom-gen-1-2-tohu", "contests", "Angelomus knows there is another translation and does not know whose. 'Whence another translation says: unseen and unordered' is as far as the ninth century can get. Chalcidius names him — otiosa uero et indigesta nuncupatur a Symmacho — quotes him twice, and explains both words: idle because of itself it avails nothing, undigested because it has the fitness to receive order. The alia translatio of the Carolingian glosses is a named Greek version whose Latin attribution had been in print since the fourth century and was lost."),
 _E6("t-k6-c3", "chalcidius-terra-sylua", "aug-conf-12-4", "parallel", "Augustine groping for the word Chalcidius already has. Confessions XII asks what the formless is to be called if not by some familiar word, and settles on a nothing-something, a is-that-is-not. Chalcidius states the receptacle argument flat: it is called empty because, being the receiver of all qualities, it has none of its own by nature, and nothing because it is devoid of all things. The two men are describing the same thing and only one of them has the Platonic vocabulary intact; Augustine is reaching for it through a Latin Bible."),
 _E6("t-k6-c4", "chalcidius-terra-sylua", "basil-hex-2-4", "parallel", "The two fourth-century texts that give a Latin reader the Greek behind inuisibilis et incomposita, and only one of them stays on the bench. Basil, in Eustathius's Latin, expounds the earth as invisible and unordered and explains why the terms are apt. Chalcidius gives the same clause four renderings — the Septuagint's, Aquila's inanis et nihil, Symmachus's otiosum quid confusumque et inordinatum, and the Hebrews' stupida admiratione — and explains each. Basil is copied by Bede and reaches the twelfth century; Chalcidius is copied by nobody."),
 _E6("t-k6-c5", "chalcidius-terra-sylua", "ambrose-hex-1-1-hyle", "contests", "Both name hyle and take opposite views of it. Ambrose at Milan reports the philosophers' matter in order to refuse it, as a rival to the God who makes out of nothing. Chalcidius uses sylua as the plain sense of the verse — 'the earth was invisible and formless', that is, corporeal hyle, the old substance of the world before it took on forms — and has already said on the previous leaf that the Hebrews confess hyle was generated, which is what removes Ambrose's objection. The concession Ambrose needed was on a Latin page he never saw."),
])

# ================================================================ Philo (Phase 6 part five, 2026-09-06)
# No witness is defined here: philo-opif-21-22 belongs to K4 and philo-opif-29 to K5, and both
# carry `tohu-vabohu` in their own cruxes facet, so build-crux.py folds them into this roster.
# Only the threads that are this crux's own are written here. See scripts/philo.py.
import philo
PERSONS.update(philo.PERSONS)
LICENSES.update(philo.LICENSES)

_EP6 = lambda i, f, t, ty, ev: thread("tohu-vabohu", i, f, t, ty, ev)
THREADS.extend([
 _EP6("t-k6-p1", "philo-opif-21-22", "basil-hex-2-4", "parallel", "The same two Greek words, once as a doctrine and once as a lemma, and the Latin bench only ever saw the second. Basil's text of Gen 1:2 reads the earth was invisible and unordered, aoratos kai akataskeuastos, and the whole Latin argument about invisibilis et incomposita descends from it. Philo, writing before that Greek Bible reading had a history of interpretation, uses ataktos, without order, of substance in general, and pairs it with apoios, without quality. So the phrase the Latins treat as a fact reported about the earth is in Philo a philosophical description of matter as such. Basil then denies exactly what Philo asserted, that there is an unbegotten substance, and does not name him."),
 _EP6("t-k6-p2", "philo-opif-29", "aug-conf-12-4", "parallel", "Both are looking for names for what has no form, and both borrow from the verse. Augustine asks what it was to be called if not by some familiar word, and settles on earth and abyss as names given for the sake of our slowness. Philo takes the same two words and assigns them referents in his inventory: the darkness is the air, because air is black by nature, and the abyss is the void, because the void is deep and yawning. Augustine treats the words as a concession to the reader; Philo treats them as precise. The daf has the same problem solved in opposite directions eight hundred years and one language apart."),
 _EP6("t-k6-p3", "philo-opif-29", "b-chag-12a-tohu", "parallel", "Both give tohu and the abyss a physical identification rather than a moral one, and the two identifications have nothing in common. The Bavli: tohu is a green line that encircles the whole world and from which darkness goes out. Philo: the darkness is the air, which is black by nature, and the abyss is the void. Each bench reaches for the physics it has, and each ends with the same conviction, that the second verse names things and not merely states."),
 _EP6("t-k6-p4", "philo-opif-21-22", "chalcidius-hebraei-versiones", "contests", "Chalcidius reports that the Hebrews confess hyle was generated. Philo is a Hebrew who confesses nothing of the kind: he says the substance was of itself without order, quality or life, and he never says who made it. Chalcidius had read Philo and names him twice elsewhere in the commentary, so his generalisation about the Hebrews is made in full knowledge of the one Hebrew author he could actually read, and does not fit him. This is the sharpest place in the edition to watch a Latin report of a Jewish position round off its edges."),
])
