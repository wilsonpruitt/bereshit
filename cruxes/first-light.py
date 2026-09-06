"""K8 — first-light (Gen 1:3). What was the light of day one, before sun and moon?
Built 2026-09-05 (Phase 2, crux 3 of 9). See PHASES.md for the spec-file contract.

Latin sliced from the local PL TEI by anchor phrase; rabbinic from raw/sefaria/*.json;
Bonaventure from ~/bonaventure-sentences/vol2 (Wilson's edition, Latin + his English).
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, APPROVED, thread

CRUX_ID = "first-light"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

BON = pathlib.Path.home() / "bonaventure-sentences" / "vol2"

# ---------------------------------------------------------------- scripture-level witnesses
add(id="lxx-1-3", work="lxx", author="lxx-translators", tradition="greek-jewish",
    date=-250, date_precision="circa", place="alexandria",
    anchor={"verse": "gen.1.3"}, lemma={"el": "γενηθήτω φῶς", "en": "let there be light"},
    original={"lang": "el", "text": "καὶ εἶπεν ὁ θεός Γενηθήτω φῶς. καὶ ἐγένετο φῶς.", "source": "LXX Gen 1:3 (Rahlfs)", "license": "pd"},
    english={"text": "And God said, Let light be made. And light was made.", **APPROVED},
    cruxes=["first-light"], senses=["translation"],
    answers=["fiat-is-instantaneous"],
    notes="The Greek uses one verb twice, γενηθήτω and ἐγένετο, so that the command and the thing commanded are the same word — which is the whole of the Latin argument about how God speaks, transplanted from a feature of the Greek that Latin's fiat / facta est reproduces exactly. Abelard is the only Latin on this crux who knows that the Hebrew does something different again.")

add(id="vulgate-1-3", work="vulgate", author="jerome", tradition="latin",
    date=392, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Fiat lux", "en": "Let there be light"},
    original=latin("7204", "Dixitque Deus: Fiat lux", "facta est lux.", 28),
    english={"text": "And God said: Let there be light. And light was made.", **APPROVED},
    cruxes=["first-light"], senses=["translation"],
    answers=["fiat-is-instantaneous"],
    notes="Four words that carry the crux: the light is made on the first day, the sun on the fourth, and Scripture never says what this light is. Every witness on both benches is answering a question the verse creates by silence.")

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "cc-by-sa", "version": "Sefaria 'Wikisource Bereshit Rabbah' (CC BY-SA). Phase 6, 2026-09-05: moved off 'Midrash Rabbah -- TE', whose own site asserts all rights reserved"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True}

add(id="br-3-4", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.3"}, lemma={"he": "מֵהֵיכָן נִבְרֵאת הָאוֹרָה", "en": "from what was the light created"},
    original={"lang": "he", "text": sef("br-3", "he", 3)[0], "source": "Bereshit Rabbah 3:4 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-3", "en", 3)[0], **_BR_EN},
    tradents=["r-shimon-b-yehotzadak", "r-shmuel-b-nachman", "r-berekhya", "r-yitzchak"],
    cruxes=["first-light"], senses=["allegorical", "literal"],
    answers=["lux-garment", "lux-from-temple"],
    notes="The question of this crux asked in the rabbinic idiom — not what the light was but what it was made from — and answered in a whisper. R. Shmuel bar Naḥman says the Holy One wrapped himself in it like a garment and the radiance shone from one end of the world to the other, and he says it under his breath even though Ps 104:2 says it outright; when challenged he answers only that he heard it whispered and so passes it on whispered. Then a second answer that no Latin witness could have imagined: R. Berekhya in the name of R. Yitzḥak, that the light was created from the site of the Temple. The Latin bench asks where the light shone (Bede: in the upper parts of the earth, where the sun's daylight falls now); this bench asks where it came from, and answers with a place in Jerusalem.")

add(id="br-3-6", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.3"}, lemma={"he": "גְּנָזוֹ לַצַּדִּיקִים לֶעָתִיד לָבוֹא", "en": "he stored it away for the righteous in the time to come"},
    # Phase 4 (2026-09-05): trimmed to the first half. K9 found that this slice took the whole Sefaria
    # segment, including the va-yavdel block that is K9's core text and is now built as `br-3-6b`.
    # Two distinct arguments on two clauses were on one card, which the frozen rule forbids.
    # ⚠ Phase 6: the Hebrew moved to the Wikisource recension, which does NOT have the opening
    # question — «ויקרא אלהים לאור יום, לא הוא אור ולא הוא יום, אתמהא» — that Torat Emet prints and
    # that Sefaria's English still translates ("are light and day not the same thing? This is
    # bewildering"). Both sides are therefore cut to the material the two recensions share, and the
    # English now opens at "It is taught" rather than at the lemma. The missing question is a real
    # divergence between the recensions, not a slicing loss; see notes/SOURCES-FINDINGS.md.
    original={"lang": "he", "text": hcut(sef("br-3", "he", 5)[0],
                                        "תְּנִי אוֹרָה שֶׁנִּבְרֵאת בְּשֵׁשֶׁת יְמֵי בְרֵאשִׁית",
                                        "שֶׁהִשְׁפִּיעַ לָהֶן הַקָּדוֹשׁ בָּרוּךְ הוּא אוֹרָה.", "K8 br-3-6 he"),
              "source": "Bereshit Rabbah 3:6, the stored light (Vilna numbering)", **_BR_SRC},
    english={"text": hcut(sef("br-3", "en", 5)[0], "It is taught: The light that was created",
                          "the Holy One blessed be He conferred extra light upon them.", "K8 br-3-6 en"), **_BR_EN},
    tradents=["r-nechemya"],
    cruxes=["first-light"], senses=["literal", "allegorical"],
    answers=["lux-hidden"],
    notes="The rabbinic answer proper, and it has no Latin counterpart at all. The light of the six days cannot shine by day, because it would make the sun's disc look dim, and it was not made to shine by night: so where is it? It was stored away, designated for the righteous in the time to come (Isa 30:26). The section then has to explain why Isaiah says seven days when the luminaries were made on the fourth, and answers with a wedding feast and, in R. Neḥemya's name, with the seven days of mourning for Methuselah. The Latin bench never hides the light: it either turns it into the angels or turns it into a proto-sun, and the one thing it never does is take it out of the world and keep it. Slice note (Phase 4): this witness originally ran to the end of the Sefaria segment and so swallowed the va-yavdel material — R. Ze'eira on the havdala blessing, hivdilo lo, R. Yoḥanan and Resh Lakish's two generals, R. Tanḥuma on Isa 45:7 and R. Elazar on the missing divine name. That is a different argument on a different clause and is now `br-3-6b` on K9. The slice was trimmed here rather than the new witness deleted.")

_chag = json.load(open(RAW / "b-chag-12a.json"))
def _seg(lang, a, b):
    v = [x for x in _chag["versions"] if x["language"] == lang][0]["text"]
    def flat(x): return x if isinstance(x, str) else " ".join(flat(i) for i in x)
    return " ".join(flat(v[i]) for i in range(a, b))
add(id="b-chag-12a-light", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.3"}, lemma={"he": "אוֹר שֶׁבָּרָא הַקָּדוֹשׁ בָּרוּךְ הוּא בַּיּוֹם רִאשׁוֹן", "en": "the light the Holy One created on the first day"},
    original={"lang": "arc", "text": _seg("he", 7, 12), "source": "b. Chagigah 12a (Vilna)", "license": "cc-by-sa", "version": [x for x in _chag["versions"] if x["language"] == "he"][0]["versionTitle"]},
    english={"text": _seg("en", 7, 12), "translator": "Sefaria Community Translation", "license": "cc0"},
    tradents=["r-elazar", "r-yaakov"],
    cruxes=["first-light", "good-and-separated"], senses=["literal"],
    answers=["lux-hidden", "lux-becomes-luminaries"],
    notes="The whole crux in five short segments, and it opens with the objection in the same form the Latin bench uses: was light created on the first day? But it is written that God set them in the firmament, and that was the fourth day. Two answers follow. R. Elazar's: by that light Adam saw from one end of the world to the other, and when God looked at the generations of the Flood and the Dispersion he hid it, storing it for the righteous. And then a tannaitic dispute — R. Yaakov holds the seeing-light, and the sages say 'these are the lights that were created on the first day but were not hung up until the fourth.' That second answer is exactly the one Augustine reports as having been said 'by someone' at De Genesi ad litteram I.11, without a name.")

_rashi = json.load(open(RAW / "rashi-gen-1.json"))
add(id="rashi-1-4", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1080-1105", place="troyes",
    anchor={"verse": "gen.1.4"}, lemma={"he": "וַיַּרְא … וַיַּבְדֵּל", "en": "and he saw … and he divided"},
    original={"lang": "he", "text": [v for v in _rashi["versions"] if v["language"] == "he"][0]["text"][3][0], "source": "Rashi on Gen 1:4, s.v. וירא אלהים את האור כי טוב ויבדל", "license": "pd"},
    english={"text": [v for v in _rashi["versions"] if v["language"] == "en"][0]["text"][3][0], "translator": "Rosenbaum–Silbermann 1929–34", "license": "silbermann"},
    cruxes=["first-light", "good-and-separated"], senses=["literal", "allegorical"],
    answers=["lux-hidden"],
    notes="Rashi puts the two rabbinic answers in his usual order and names both sources. First 'here too we must depend on the statement of the Agada': God saw that the wicked were unworthy of the light, so he set it apart for the righteous in the world to come — and he cites Chagigah 12a for it. Then the plain sense, from Bereshit Rabbah 3:6: it was not seemly that light and darkness should work in confusion, so he gave each its own hours. The hiding is aggada and the division is peshat, and Rashi does not merge them. Note that the hiding is derived from the word va-yavdel, 'and he divided' — the same word K9 is built on.")

_pdre = json.load(open(RAW / "pdre-3.json"))
add(id="pdre-3-6", work="pdre", author="pirkei-derabbi-eliezer", tradition="rabbinic",
    date=800, date_precision="range-750-850", place="palestine",
    anchor={"verse": "gen.1.3"}, lemma={"he": "מֵאוֹר לְבוּשׁוֹ", "en": "from the light of his garment"},
    original={"lang": "he", "text": [v for v in _pdre["versions"] if v["language"] == "he"][0]["text"][6], "source": "Pirkei de-Rabbi Eliezer 3", "license": "pd", "version": "Sefaria Vocalized Edition"},
    english={"text": [v for v in _pdre["versions"] if v["language"] == "en"][0]["text"][6], "translator": "Gerald Friedlander, 1916", "license": "pd"},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-garment"],
    notes="The garment of Bereshit Rabbah 3:4, no longer whispered and turned into cosmogony: the heavens were made out of the light of the garment God wraps himself in, taken and stretched like a curtain until he said Dai, enough — which is why he is called El Shaddai. Ps 104:2 supplies both halves in one verse, 'who covers himself with light as with a garment, who stretches out the heavens like a curtain'. The first light is thus not merely prior to the luminaries but prior to the sky and the material of it. Nothing on the Latin bench makes the light the stuff of anything; the nearest is Augustine's report at De Gen. ad litt. I.11 that someone held the luminaries were made out of it.")

# ---------------------------------------------------------------- latin bench, patristic
add(id="basil-hex-2-7", work="basil-hex-lat", author="basil", tradition="latin",
    date=550, date_precision="range-500-600", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Prima vox Dei naturam luminis fabricavit", "en": "The first voice of God fashioned the nature of light"},
    original=latin("7608", "Et dixit Deus, Fiat lux. Prima vox Dei", "per omnes suos terminos intendebat", 53),
    english={"text": "And God said, Let there be light. The first voice of God fashioned the nature of light, and drove away the darkness, and dissolved gloom, and suddenly brought forth every glad and pleasant appearance. Then the vault appeared, which had until then been hidden by the Lord; and so great a beauty of it shone out as the sight bears witness to even now. And the air was lit up by that light which had been mingled with it, and it stretched the sharp penetration of its own brightness everywhere through all its bounds.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="The Greek tradition entering Latin, and it has no doubt at all: the light is a nature that God's voice fashioned, and what it does is physical — the air takes it up and carries it to its limits, the water throws it back, the sky becomes visible. Basil is the only Father on this bench who describes the light as a phenomenon rather than as a question, and Eustathius' Latin keeps that. The twelfth-century schoolmen — Hugh, Honorius, Comestor — end up where Basil starts, and they get there without citing him.")

add(id="ambrose-hex-1-9", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Naturae opifex lucem locutus est, et creavit", "en": "The maker of nature spoke light, and created it"},
    original=latin("6958", "Fiat, inquit, lux. Unde vox Dei", "Naturae opifex lucem locutus est, et creavit.", 14),
    english={"text": "'Let there be light,' he says. Where should the voice of God in divine Scripture begin, if not from light? Whence should the adorning of the world take its start, if not from light? For it would be in vain, if it were not seen. God himself was indeed in light, for he dwells in light inaccessible, and he was the true light, which enlightens every man coming into this world; but he made that light which we see. […] Where the builder lays the foundations he looks out from where he may pour light into it, and that is the first grace, and if it is wanting the whole house bristles with an unlovely neglect. It is light that commends the rest of the house's ornament. 'Let there be light,' he says. A full utterance of light — it does not signify the apparatus of an arrangement, but shines out with the effect of an operation. The maker of nature spoke light, and created it.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis", "fiat-is-instantaneous"],
    notes="Ambrose keeps two lights apart in one paragraph and the distinction is the whole crux in miniature: God dwells in light inaccessible and is himself the true light of John 1:9, 'but he made that light' — hanc, this one, the one under discussion. The rest is the ornament argument, that a world had to be lit before it could be seen at all, with the builder's house for an image. Nothing here is angelic. Elided at […]: the sentence on the darkness fleeing and the intervening image of the householder choosing where his windows go.")

add(id="aug-gnl-1-3", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.3"}, lemma={"la": "utrum spirituale quid, an corporale?", "en": "whether something spiritual or something bodily?"},
    original=latin("7302", "Et quid est lux ipsa quae facta est?", "conversio ejus facta atque illuminata intelligatur.", 34),
    english={"text": "And what is that light itself which was made? Is it something spiritual, or something bodily? For if spiritual, it can itself be the first creature, already made perfect by this saying, which was first called heaven when it was said, 'In the beginning God made heaven and earth' — so that what God said, 'Let there be light, and light was made', may be understood as its turning and illumination, the Creator calling it back to himself.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-angelica"],
    notes="The crux as a disjunction, in the sentence that decided the Latin question for eight centuries: spiritual or bodily? Augustine leaves the alternative open here in form, but the whole of his exposition follows the first limb, and the doctrine is already complete in the second half of the sentence — the light is the spiritual creature that was called 'heaven' in verse 1, and 'let there be light' is not its making but its conversion, its turning back to the Creator and being illuminated by him. Bonaventure will state this position fairly and decline it, and give the reason: not that it is unreasonable, but that the text more readily intimates the other.")

add(id="aug-gnl-1-11", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Utquid ergo factus est sol", "en": "Why then was the sun made"},
    original=latin("7302", "Utquid ergo factus est sol in potestatem diei", "ordine dierum, quo visum est Creatori cuncta esse facienda", 34),
    english={"text": "Why then was the sun made 'to rule the day' (Ps 136:8), to shine over the earth, if that light was sufficient for making a day — the light that was itself called Day? Or did that earlier light illuminate regions high and far from the earth, so that it could not be felt on earth, and so the sun had to be made, through which day might appear to the lower parts of the world? This too can be said: that the brightness was increased by the addition of the sun, so that the day is believed to have been less bright by that earlier light than it is now. This too I know to have been said by someone: that the nature of light was first brought in in the Creator's work, when it was said 'Let there be light, and light was made'; but afterwards, when the luminaries are spoken of, it was recorded what was made out of that same light, in the order of the days in which it seemed good to the Creator that all things should be made.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-becomes-luminaries", "lux-corporalis"],
    notes="The crux's hardest question, asked plainly: if that light already made a day, what is the sun for? Augustine offers three answers and holds none of them. The third is the one that matters here — 'this too I know to have been said by someone', a quodam dictum scio: that the nature of light was made on the first day and the luminaries were afterwards made out of it. That anonymous opinion is, word for word in substance, what b. Chagigah 12a attributes to the sages against R. Yaakov: 'these are the lights that were created on the first day but were not hung up until the fourth.' Augustine does not know whose it is, and the Talmud names the party that holds it.")

add(id="bede-gen-1-3", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="range-717-725", place="jarrow",
    anchor={"verse": "gen.1.3"}, lemma={"la": "primam materialis gratiam lucis donavit", "en": "he gave the first grace of material light"},
    original=latin("8466", "Congruit operibus Dei, ut mundi ornatum a luce incipiat", "ut esset unde caetera quae crearet apparerent.", 91),
    english={"text": "It befits the works of God that he should begin the adorning of the world from light: he who, being himself the true light and dwelling in light inaccessible, in the beholding of which the angels, newly created in the heaven of heavens, had already begun to rejoice, fittingly gave to this world too, for its adorning, the first grace of material light, so that there might be something from which the rest that he would create could appear.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="Bede does the thing that decides the crux for the whole Carolingian line, and does it in one sentence without argument: he distinguishes three lights — God who is the true light, the inaccessible light the angels were already enjoying in the heaven of heavens, and 'the first grace of material light' given to this world. The angels are on the page and are not the light; they were made earlier and elsewhere. Augustine's identification is not refuted here, it is quietly stepped around, and Alcuin, Rabanus and the Glossa all inherit the step.")

add(id="bede-gen-1-3b", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="range-717-725", place="jarrow",
    anchor={"verse": "gen.1.3"}, lemma={"la": "quibus in locis facta sit lux", "en": "in what places the light was made"},
    original=latin("8466", "Si autem quaeritur quibus in locis", "quantum Deus per Spiritum oris sui creare posse credendus est", 91),
    english={"text": "But if it is asked in what places, at God's bidding, the light was made, since the abyss still covered the whole breadth of the earth — it is quite plain that that first light shone in the upper parts of that same earth, the parts which the daily light of the sun is now accustomed to illumine. Nor should we wonder that by a divine working light can shine in the waters, since it is agreed that they are often lit by a human working too: by sailors, that is, who, sunk in the deep of the sea, make it clear and bright for themselves by letting oil out of their mouths. For if a man can do such things by the oil of his mouth, how much must God be believed able to create by the Spirit of his mouth.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="Once the light is material it acquires a location, and Bede supplies one: in the upper parts of the earth, where the sun's daylight falls now. The objection that the abyss covered everything he answers with an observed fact about divers, who let oil out of their mouths to see under water, and a pun that carries the argument — if a man can do it by the oil of his mouth, what can God do by the Spirit of his mouth. The Glossa keeps both the location and the divers and cuts the pun.")

add(id="alcuin-int-33", work="alcuin-int", author="alcuin", tradition="latin",
    date=800, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.3"}, lemma={"la": "a luce aeterna lux temporalis", "en": "from the eternal light, a temporal light"},
    original=latin("21416", "Inter. 33. Quare prima die lux creata legitur?", "ut esset unde caetera quae crearet, apparerent.", 100),
    english={"text": "Question 33. Why is light read to have been created on the first day? — Answer. It befits the works of God that on the first day a temporal light should first be made from the eternal light, so that there might be something from which the rest that he would create could appear.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="Bede's sentence reduced to a schoolroom answer, with one word added that is not Bede's and that does the work: a luce aeterna, from the eternal light. Bede had set the eternal light beside the material one; Alcuin makes the temporal light come out of it, which is a claim about derivation and not merely about order. Compare Pirkei de-Rabbi Eliezer, where the heavens are made out of the light of God's garment: on both benches the first light acquires a source in God himself, and on neither is that reading argued for.")

add(id="rabanus-gen-1-3", work="rabanus-gen", author="rabanus", tradition="latin",
    date=822, date_precision="range-819-822", place="fulda",
    anchor={"verse": "gen.1.3"}, lemma={"la": "CAPUT II. Ubi lux primum fieri jubetur", "en": "Chapter II. Where light is first commanded to be made"},
    original=latin("8885", "Congruit operibus Dei ut mundi ornatum a luce incipiat", "in superioribus ejusdem terrae partibus", 107),
    english={"text": "It befits the works of God that he should begin the adorning of the world from light, since he himself is the true light and dwells in light inaccessible (1 Tim 6:16); in the most blessed beholding of which the angels, newly created in the heaven of heavens, had already begun to rejoice. Fittingly he gave to this world too, for its adorning, the first grace of material light, so that there might be something from which the rest that he would create could appear. […] But if it is asked in what places, at God's bidding, the light was made, since the abyss still covered the whole breadth of the earth — it is quite plain that it was in the upper parts of that same earth.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="Bede again, verbatim and unattributed, as at K1 and K7 and K10; the only visible editorial act is the chapter heading Rabanus puts over it, 'Where light is first commanded to be made', which turns Bede's continuous exposition into a lemma. Elided at […] is the long passage on how God speaks — that Moses' 'God said' and John's 'all things were made through the Word' are one statement — which Rabanus also takes from Bede entire.")

add(id="angelom-gen-1-3", work="angelom-gen", author="angelomus", tradition="latin",
    date=845, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.3"}, lemma={"la": "nomine lucis angelica dignitas figuratur", "en": "by the name of light the angelic dignity is figured"},
    original=latin("9032", "Caeterum quod ait, fiat lux, ob celeritatem", "Convertatur ad contemplandum incessabiliter me", 115),
    english={"text": "As for his saying 'let there be light', it is said on account of the swiftness of the divine power. For if the luminaries which supply light are described as made on the fourth day, what is it that he said, 'Let there be light'? Was there perhaps already some light created above the firmament, by whose illumination the sun was lit? Rather, by the name of light the angelic dignity is figured, which is signified by the higher heaven and is here called light. It was founded first, then, but was afterwards made light by turning to behold the glory of its creator. And therefore it was said, 'Let there be light, and light was made' — as if it were plainly being said: Let it turn to contemplate me unceasingly.", **APPROVED},
    cruxes=["first-light"], senses=["literal", "allegorical"],
    answers=["lux-angelica"],
    notes="The one Carolingian on this bench who takes Augustine's side rather than Bede's, and he states the doctrine more sharply than Augustine does: the angelic nature was founded first and became light afterwards, by turning to behold its creator, so that 'let there be light' is a command to contemplate. He reaches it by the same route the Talmud's objectors take — if the luminaries are made on the fourth day, what is this? — and he even floats the physical answer (a light above the firmament from which the sun was lit) before rejecting it. K7 found Angelomus splicing Augustine onto Jerome without naming either; here he does the same with Augustine's angelic light.")

add(id="remigius-gen-1-3", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.3"}, lemma={"la": "qualis esse solet vel ante solis ortum, vel post ejus occubitum", "en": "such as it is wont to be before sunrise or after sunset"},
    original=latin("9346", "Fiat lux. Lux dicitur a luendo", "vel post ejus occubitum.", 131),
    english={"text": "'Let there be light.' Light (lux) is so called from cleansing (luendo), that is, from purging away the darkness. But that light was not of the kind that now is, with the sun set above; rather it was such as it is wont to be before the rising of the sun, or after its setting.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis", "lux-twilight"],
    notes="Two sentences, and the second is the answer the twelfth century will build a physics on: the light was twilight — what the sky is like before sunrise or after sunset. Honorius says the same (a brightness such as there is now before sunrise), Comestor calls it a luminous cloud thin as the dawn, and Hugh gives it a body and an orbit. The etymology in the first sentence is Isidore's manner and is false; it is kept because Remigius is arguing from it.")

# ---------------------------------------------------------------- the Glossa and the twelfth century
add(id="glossa-1-3", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Lux primo die facta spiritualis vel corporalis intelligitur", "en": "The light made on the first day is understood as spiritual or bodily"},
    original=latin("8950", "VERS. 3.--", "usque ad nondum enim erant animalia quibus haec vicissitudo exhiberetur.", 113),
    english={"text": "Verse 3. 'And God said: Let there be light.' (AUGUSTINE, on Genesis to the letter, book I, ch. 17, vol. III.) The light made on the first day is understood as spiritual or bodily, etc., down to: morning, the beginning of what is to come. (BEDE, Hexaemeron.) But if bodily light was made on the first day, fittingly is the adorning of the world begun from light, whence the rest that were to be created might be seen. And if it is asked where it was made, since the abyss covered the whole height of the earth — it is plain that it was in those parts which the daily light of the sun now illumines. Nor is it a wonder that light can shine in the waters, since they are often lit even by the working of sailors, who, sunk in the deep, let oil out of their mouths and light the waters for themselves: which waters were then much thinner than they now are, in the beginning, because they were not yet gathered into one place. 'And God said: Let there be light.' (AUGUSTINE, ibid., ch. 2.) Not temporally: for if temporally, then changeably; if changeably, then through a creature subject to him, and light is not the first creature. But perhaps, etc., down to: that it may be and may abide. 'Let there be light.' (AUGUSTINE, ibid., ch. 4, 5, 9.) On that condition, namely, by which all things subsist timelessly in the wisdom of God before they subsist in themselves. 'And light was made', that is, the angelic and heavenly substance, in itself temporally; as it was in wisdom, so far as concerns its unchangeableness, eternally. Or the unformedness of this creature is noted, that is, its imperfection before it was formed in the love of its Maker: for it is formed when it is turned to the unchangeable light of the Word. 'Let there be light.' (AUGUSTINE, ibid., ch. 10, 11, 16.) If light was made bodily, etc., down to: for there were not yet animals to whom this alternation might be exhibited.", **APPROVED},
    cruxes=["first-light"], senses=["literal", "allegorical"],
    answers=["lux-angelica", "lux-corporalis"],
    notes="The margin refuses to decide, and it does so by putting four glosses on one verse of which three are Augustine and one is Bede. The first Augustine gloss states the disjunction and abbreviates the discussion with the Glossa's 'etc., usque ad'; Bede's supplies the bodily answer with its location and its divers; then two more Augustine glosses give the angelic answer in full, 'et facta est lux, id est angelica et coelestis substantia'. A reader of this page is told what both parties hold and given no verdict, which is the opposite of what the same margin does at Gen 1:1, where Alcuin's one-word Filio stands unopposed. Note that the Bede gloss cuts his oil-of-the-mouth / Spirit-of-the-mouth pun and keeps the divers.")

add(id="bruno-gen-1-3", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1090, date_precision="range-1079-1123", place="segni",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Lux igitur pro die ponitur", "en": "Light, therefore, is put for day"},
    original=latin("21403", "Sed quae est ista lux, quae prior sole", "Lux igitur pro die ponitur.", 164),
    english={"text": "But what is that light, which is said to be prior to the sun, the moon and the stars? Hear what follows: 'He called the light Day, and the darkness Night.' Light, therefore, is put for day.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-is-day"],
    notes="The crux asked in the Latin bench's own words — quae est ista lux, quae prior sole, luna et stellis esse perhibetur? — and then dismissed in six. Bruno's answer is that the verse answers itself two clauses later: God called the light Day, so 'light' here simply means the day, and there is nothing further to look for. Of every witness on this crux he is the only one who declines the question rather than answering it, and he does it by the same appeal to the text's own next words that he uses at K10 to settle dies unus.")

add(id="abelard-hex-1-3", work="abelard-hex", author="abelard", tradition="latin",
    date=1133, date_precision="range-1130-1135", place="paraclete",
    anchor={"verse": "gen.1.3"}, lemma={"la": "ipsam sequentium operum distinctionem", "en": "the distinction of the works that follow"},
    original=latin("11118", "Lucem vero istam quae praedictas tenebras removit", "vel ad quid creata esset ex ipsa adhuc percipi valebat", 178),
    english={"text": "But that light which removed the aforesaid darkness we take to be the distinction itself of the works that follow — that distinction, namely, by which that confused heap, which did not yet present itself as visible, nor could be known as fit for any use, nor could yet be perceived from itself for what it had been created…", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-is-distinction"],
    notes="An answer nobody else on either bench gives: the light is neither a body nor an angel but the ordering of the works themselves — the coming-into-distinctness of the confused heap, so that it could be seen and known for what it was made for. Abelard reaches it by taking 'darkness' as unintelligibility rather than as absence of illumination, which is Augustine's privation doctrine turned from optics to knowledge. It is also the only reading on the crux that makes the first light not a thing at all, and so the only one for which the sun on the fourth day raises no difficulty whatever.")

add(id="abelard-hex-1-3b", work="abelard-hex", author="abelard", tradition="latin",
    date=1133, date_precision="range-1130-1135", place="paraclete",
    anchor={"verse": "gen.1.3"}, lemma={"la": "in Hebraeo haberi: Sit lux, et fuit lux", "en": "in the Hebrew it is: Let light be, and light was"},
    original=latin("11118", "Notandum vero pro eo quod dicimus: Fiat lux", "nulla interposita mora perfectio rei", 178),
    english={"text": "It is to be noted that, where we say 'Let there be light, and light was made', in the Hebrew it is: 'Let light be, and light was'; and likewise in the rest that follow, wherever we have 'God said, Let this be made, and it was made so', in the Hebrew it is 'Let this be, and it was so'. By which words perhaps the greatest swiftness of the divine working is expressed. For while something is being made which is not yet, there can be some delay in the making. But when it is said 'let it be' and 'it was', with no delay interposed the perfecting of the thing…", **APPROVED},
    cruxes=["first-light"], senses=["translation", "literal"],
    answers=["fiat-is-instantaneous"],
    notes="Abelard reporting the Hebrew against the Latin, exactly as K7 found him doing at PL 178:735B with volitabat. The observation is correct — yehi or va-yehi or is one verb twice, as the Greek's γενηθήτω / ἐγένετο is, while the Latin's fiat / facta est is two — and he draws a conclusion from it that the whole bench had been reaching for by other means: no delay is interposed, because a thing that is merely told to be is not first made and then finished. Where he got the Hebrew is unknown, as at K7. He is the only Latin on this crux who looks at the other language at all.")

add(id="hugh-adnot-1-3", work="hugh-adnot", author="hugh-of-st-victor", tradition="latin",
    date=1130, date_precision="range-1125-1135", place="paris",
    anchor={"verse": "gen.1.3"}, lemma={"la": "quasi quaedam lucida nubes circumferebatur, sicut modo sol", "en": "it was carried round like a kind of luminous cloud, as the sun is now"},
    original=latin("11054", "Ignis vero distinctus lumen praebuit mundo inferiori", "sicut modo sol.", 175),
    english={"text": "But fire, once distinguished, furnished light of some kind to the lower world, and had a circular motion: it was carried round like a kind of luminous cloud, as the sun is now.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis", "lux-twilight"],
    notes="One sentence of physics, and it names the material: the first light is the element of fire, separated out and carried round the world in a circuit. Honorius says the same in the same decade — this bodily light he brought forth from the element of fire — and Comestor's luminous cloud is the same image. Hugh's fuller treatment is in De sacramentis and is built separately; the Adnotationes give the picture without the argument.")

add(id="hugh-sacr-1-3", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.3"}, lemma={"la": "ipsamque vice et loco solis factam", "en": "and that it was made in the sun's stead and place"},
    original=latin("11082", "corporalibus rebus et visibilibus illuminandis", "et noctem diemque discerneret.", 176),
    english={"text": "…for the lighting of bodily and visible things, nothing but a bodily light could have been suitable. And every body, however fine and however near it comes to a spiritual nature, must be circumscribed by place. And again, unless that light had been mobile, it could in no way have distinguished day and night by their alternating turns, nor traversed any space of time at all without motion. According to this consideration, then, I think it more fitting that we believe that light, made in the beginning for the lighting of bodily things, to have been beyond doubt bodily — such as some luminous body might perhaps have been, by whose presence all things were lit, as can now be seen in the sun — and that it was made in the sun's stead and place, so that for the time being it was carried round by its own motion, and marked off night and day.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis"],
    notes="The argument the Victorines put under the twelfth century's physical answer, and it is an argument from fitness of means: bodily things can only be lit by a bodily light; every body is in a place; and a light that made evening and morning must have moved, since without motion no span of time is traversed. From which the first light was a luminous body standing in the sun's stead and turning as the sun turns. The chapter headings of De sacramentis announce the whole programme — 'why light was made first', 'of what kind that light was made, and where', 'that light illumined three days, and why it was made before the sun' — which is the crux set out as a syllabus.")

add(id="honorius-hex-1-3", work="honorius-hex", author="honorius", tradition="latin",
    date=1120, date_precision="range-1110-1130", place="regensburg",
    anchor={"verse": "gen.1.3"}, lemma={"la": "hanc corporalem lucem de elemento ignis protulit", "en": "he brought forth this bodily light from the element of fire"},
    original=latin("10991", "Et dixit Deus: Fiat lux. Cum de Deo", "inferiora orbis illuminavit.", 172),
    english={"text": "And God said: Let there be light. When 'he said' is written of God, it is said after our manner, and the efficacy of the one commanding is expressed. But for God to speak is nothing other than to found all things through his Word. Through this Word he brought forth this bodily light from the element of fire, and brought it into this world. Which light then showed such a brightness as there now is before the rising of the sun; and it lit the waters, then thin, as it now lights the air. For twelve hours it remained above the earth, as the sun does now; and for twelve it lit the lower parts of the globe.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis", "lux-twilight"],
    notes="The physical answer at its most confident and most specific: the light is drawn from the element of fire, its brightness is that of the sky before sunrise, it lights the waters as light now lights the air, and it keeps a twelve-hour circuit above and below. Honorius gives no argument for any of it. Rupert, writing in the same years, describes precisely this opinion — that the light was nothing but an illumination of the air, alternating over twelve hours through three days — in order to demolish it.")

add(id="rupert-gen-1-3", work="rupert-gen", author="rupert", tradition="latin",
    date=1117, date_precision="range-1112-1117", place="liege",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Quaenam est ista lux?", "en": "What kind of light is that?"},
    original=latin("10873", "Quid autem est hoc ipsum quod dixit: Fiat lux?", "luminis gratia refulgentem.", 167),
    english={"text": "But what is this very thing that he said, 'Let there be light'? What kind of light is that? For it seems to some that the light then made was nothing other than an illumination of the air, and that those darknesses which were over the face of the abyss were divided by night and day so alternating that, when the space of daytime — twelve hours, that is — was passed, the light was put out and darkness succeeded; and again, when the space of nighttime was over, the light shone out; and so for three days, day and night, without these bodily luminaries, that is without sun and moon and stars, gave way and succeeded to one another of their own accord. But on this reading this one day is the poorest of all days: for whereas each of the other days is made illustrious by the creation or forming of substances, this day is dismissed with nothing but an unstable colour of some accident thrown over it, when it is said 'let there be light'. For whatever was made on the other days is substantial and abides; but that accidental light, once relit on the third day, thereafter perished utterly. And see whether it be worthy of so great a majesty that the works of the other days — the sun, for instance, and moon and stars that were made on the fourth day, and the division of the waters that was made on the second — he should establish for ever and ever, and lay upon them a decree that shall not pass away (Ps 148:6), but should make the work of the first light such that, changing his counsel, he should utterly put it out after a scant three days. What then? Was it for this that the Spirit of God was borne over the waters, and that he said 'let it be' — a saying that holy Scripture wonders at and celebrates as the uttering of a truly good word — that only such a light should come to be, an accident of the air soon to perish, and no substance be created? The great and most renowned Fathers understood better: the angelic nature, signified by the name of light. Their view we approve as the more reasonable and follow it, that the angelic creature is rightly called light — an intellectual light; light, I say, not only as having the power of discerning, but also as shining with the grace of the true and uncircumscribed light.", **APPROVED},
    cruxes=["first-light"], senses=["literal", "allegorical"],
    answers=["lux-angelica"],
    notes="The best argument on the crux, and it is an argument from what would be unworthy. Rupert states the physical reading in full and with its details — twelve hours, three days, no luminaries — and then asks what it would make of the first day: every other day makes a substance that abides, and this one would make an unstable accident, a colour thrown over the air, snuffed out after three days when God changed his mind. Would the majesty that laid on sun and moon a decree that shall not pass away do that? Therefore the light is the angelic nature. He then adds, in the next chapter, that this is not said by likeness but of the thing itself: the visible light and the stars were made in the likeness of that light, not the other way about. Written in the same decade as Honorius' twelve-hour circuit and Hugh's luminous body.")

add(id="comestor-hs-1-3", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="range-1169-1173", place="paris",
    anchor={"verse": "gen.1.3"}, lemma={"la": "quamdam nubem lucidam", "en": "a kind of luminous cloud"},
    original=latin("11575", "Dixitque Deus: Fiat lux. Et facta est lux (Gen. I)", "et inferius vicissim illuminat.", 198),
    english={"text": "And God said: Let there be light. And light was made (Gen 1) — that is, he begot the Word in whom it was that light should be made; that is, as easily as if someone were to say it in a word. By 'light' he means a kind of luminous cloud, lighting the upper parts of the world, but with a thin brightness, such as comes about at dawn; and this driven round much as the sun is. By its presence it lights the upper hemisphere and in turn the lower.", **APPROVED},
    cruxes=["first-light"], senses=["literal"],
    answers=["lux-corporalis", "lux-twilight"],
    notes="The settlement, and it is the physical answer, stated as fact in a handbook with no mention that anybody ever thought otherwise. A luminous cloud, thin as the dawn, driven round like the sun, lighting one hemisphere and then the other. Rupert had argued at length that this cannot be right and Bonaventure will say Augustine's view is the subtler; the Historia scholastica simply prints the cloud, and that is what most of Europe learned. Comestor's angelic-light material, where he has it, is elsewhere and not on this verse.")

_bon = (BON / "bon-sent-II-d13-a1-q1.md").read_text().split("\n")
def _bon_slice(idx):
    """Join Wilson's edition's paragraphs, drop page markers and the Quaracchi marginal italics,
    and repair the hyphenation the Quaracchi page break leaves behind (appro- / baverunt)."""
    t = re.sub(r"<!--.*?-->", "", "\n\n".join(_bon[i] for i in idx)).strip()
    t = t.replace("*", "")   # Quaracchi's marginal labels are italic in Wilson's markdown
    t = re.sub(r"-\s*\n\s*\n\s*", "", t)
    t = re.sub(r"—\s*\n\s*\n\s*", "— ", t)
    return re.sub(r"[ \t]+", " ", t).strip()
add(id="bonaventure-sent-2-13-1-1", work="bonaventure-sent", author="bonaventure", tradition="latin",
    date=1252, date_precision="range-1250-1252", place="paris",
    anchor={"verse": "gen.1.3"}, lemma={"la": "Utrum lux primo die facta fuerit corporalis, an spiritualis", "en": "Whether the light made on the first day was corporeal or spiritual"},
    original={"lang": "la", "text": _bon_slice([68, 70, 72, 74, 78, 80]), "source": "In II Sent., d. XIII, a. 1, q. 1 (Quaracchi 1885, II.312–313)", "license": "pd", "edition": "Opera Omnia, Tomus II, Quaracchi 1885; text re-set from the plates in ~/bonaventure-sentences"},
    english={"text": _bon_slice([150, 152, 154, 156, 158, 160]), "translator": "wilson-pruitt", "license": "wroot-bonaventure", "edition": "bonaventure.wrootpress.com, In II Sent. d.13 a.1 q.1"},
    cruxes=["first-light"], senses=["literal", "spiritual"],
    answers=["lux-corporalis", "lux-angelica"],
    notes="The crux put as a disputed question and closed, eight hundred years after Augustine opened it — and closed the same way K10's d.12 a.1 q.2 closes the question of the days. Bonaventure sets out Augustine's position at length and fairly: by 'heaven' unformed spiritual nature, by 'light' the angelic nature formed, by 'day' the angelic consideration, by the seven days a sevenfold consideration; and he grants that Augustine conforms Scripture to it well enough, noting the argument that the text does not say fiat and fecit and factum est of the light as it does of bodily things. Then: however probable and reasonable that position was, the Catholic treatise-writers who followed Augustine approved another way — a material distinction of days and a corporeal light making three days before the sun — and because the text more readily intimates this and the expositors more generally follow it, this position is the safer and more useful to hold. The question is decided by weight of exposition, not by exegesis.")

# ---------------------------------------------------------------- threads
THREADS = [
 # the rabbinic bench
 E("t-k8-01", "pdre-3-6", "br-3-4", "echoes", "The garment of Ps 104:2, no longer whispered: Bereshit Rabbah has the Holy One wrap himself in the light like a garment; Pirkei de-Rabbi Eliezer takes the next clause of the same verse — 'who stretches out the heavens like a curtain' — and makes the heavens out of that light."),
 E("t-k8-02", "br-3-4", "br-3-6", "parallel", "Two sections of one compilation asking the crux from opposite ends: 3:4 asks what the light was made from and answers with God's garment and the site of the Temple; 3:6 asks where it is now and answers that it was stored away for the righteous."),
 E("t-k8-03", "b-chag-12a-light", "br-3-6", "parallel", "The same doctrine on two proof texts and neither cites the other: the midrash hides the light because it would dim the sun's disc, and proves the storing from Isa 30:26; the Talmud hides it from the generations of the Flood and the Dispersion, and proves it from Job 38:15 and from 'God saw the light, that it was good' read through Isa 3:10, since 'good' means the righteous."),
 E("t-k8-04", "rashi-1-4", "b-chag-12a-light", "cites", "Rashi names his source — 'here too we must depend upon the statement of the Agada' — and gives R. Elazar's answer: God saw the wicked were unworthy of the light and set it apart for the righteous in the world to come. Silbermann's note supplies the reference to Chagigah 12a."),
 E("t-k8-05", "rashi-1-4", "br-3-6", "cites", "The plain sense, taken from Bereshit Rabbah: it was not seemly that light and darkness should work in confusion, so he assigned each its own hours. Rashi keeps the aggadic hiding and the peshat division side by side and does not merge them."),
 # the two benches
 E("t-k8-06", "aug-gnl-1-11", "b-chag-12a-light", "parallel", "The one place on this crux where the benches hold the same opinion in the same words. Augustine: 'this too I know to have been said by someone, that the nature of light was first brought in when it was said Let there be light, but afterwards, when the luminaries are spoken of, it was recorded what was made out of that same light.' The Bavli: 'the sages say, these are the lights that were created on the first day but were not hung up until the fourth.' Augustine cannot name whose opinion it is; the Talmud names the party that holds it, against R. Yaakov."),
 E("t-k8-07", "alcuin-int-33", "pdre-3-6", "parallel", "Both make the first light derive from God himself rather than merely follow him: Alcuin adds to Bede's sentence the words a luce aeterna, so that the temporal light is made out of the eternal one, and Pirkei de-Rabbi Eliezer makes the heavens out of the light of the garment God wears. Neither argues for it; both state it as though it needed none."),
 E("t-k8-08", "bede-gen-1-3b", "br-3-4", "parallel", "The same question — where — and two answers that could not be further apart. Bede: in the upper parts of the earth, the parts the sun's daylight now falls on, and he defends it with the divers who let oil from their mouths. R. Berekhya in the name of R. Yitzḥak: the light was created from the site of the Temple, proved from Ezek 43:2 and Jer 17:12."),
 E("t-k8-09", "hugh-sacr-1-3", "b-chag-12a-light", "parallel", "Both make the first light continuous with the sun rather than replaced by it: the sages hold that the lights were created on the first day and hung on the fourth; Hugh holds that a luminous body was made in the sun's stead and place, turning as the sun turns, until the sun came. The Latin argument is from the fitness of means, the rabbinic from the wording of Gen 1:17."),
 E("t-k8-10", "pdre-3-6", "aug-gnl-1-11", "parallel", "Both make the first light the material of something later: Augustine's unnamed authority has the luminaries made out of it, and Pirkei de-Rabbi Eliezer has the heavens made out of it. On the Latin side this is one option among three and is not adopted; on the rabbinic side it is stated as cosmogony."),
 # the patristic line
 E("t-k8-11", "ambrose-hex-1-9", "basil-hex-2-7", "parallel", "Ambrose's Hexaemeron follows Basil's Greek homilies closely and this passage is no exception — the light as the world's first ornament, the air taking it up, the suddenness. The witness date here is that of Eustathius' Latin version, which is later than Ambrose; Basil's Greek (378) precedes him and is his source, so the dependence runs the other way from what the dates on this page suggest."),
 E("t-k8-12", "aug-gnl-1-3", "ambrose-hex-1-9", "contests", "Ambrose says God dwells in inaccessible light and is the true light of John 1:9, 'but he made that light' — hanc, the one in the verse, a thing among things. Augustine asks whether the light is spiritual or bodily and answers that it can be the first creature, the spiritual nature called heaven in verse 1, and that 'let there be light' is its conversion. The two positions the rest of the bench divides between are already both in place by 410."),
 E("t-k8-13", "aug-gnl-1-11", "aug-gnl-1-3", "echoes", "Book I asks what the light is; eight chapters later the same book asks what the sun can be for if that light already made a day. The second question is the pressure that produces every physical answer on this crux, and Augustine raises it against himself."),
 E("t-k8-14", "bede-gen-1-3", "aug-gnl-1-3", "contests", "Bede does not refute the angelic light; he steps round it, and the step is in one sentence. He names three lights — God who is the true light, the inaccessible light the angels already enjoyed in the heaven of heavens, and 'the first grace of material light' given to this world — so that the angels are on the page, already made, and are not the light. Alcuin, Rabanus and the Glossa's Bede gloss all inherit the step."),
 E("t-k8-15", "bede-gen-1-3b", "bede-gen-1-3", "parallel", "The same exposition a page later, asking the question a material light forces: where was it, since the abyss covered everything? Bede's answer, the upper parts of the earth, only makes sense because he has already declined to make the light angelic."),
 E("t-k8-16", "alcuin-int-33", "bede-gen-1-3", "cites", "'Congruit operibus Dei … ut esset unde caetera quae crearet apparerent' is Bede word for word, compressed into a schoolroom answer, with a luce aeterna added and the angels of the heaven of heavens dropped."),
 E("t-k8-17", "rabanus-gen-1-3", "bede-gen-1-3", "cites", "Bede reproduced verbatim and unattributed, as at K1, K7 and K10; the only visible editorial act is the chapter heading Rabanus sets over it, 'Ubi lux primum fieri jubetur', which turns a continuous exposition into a lemma."),
 E("t-k8-18", "angelom-gen-1-3", "aug-gnl-1-3", "echoes", "Angelomus takes the side of the bench Bede stepped away from, and states it more sharply than Augustine: the angelic dignity was founded first and was made light afterwards by turning to behold its creator, so that 'let there be light' means 'let it turn to contemplate me unceasingly'."),
 E("t-k8-19", "angelom-gen-1-3", "b-chag-12a-light", "parallel", "The same objection in the same form on both benches: if the luminaries are made on the fourth day, what is this light? The Talmud raises it from Gen 1:17 and answers with R. Elazar's hidden light; Angelomus raises it, floats a light above the firmament from which the sun was lit, and answers with the angels."),
 # the Glossa
 E("t-k8-20", "glossa-1-3", "aug-gnl-1-3", "cites", "Three of the four glosses on this verse are Augustine, cited by book and chapter, and between them they give the angelic reading entire: 'et facta est lux, id est angelica et coelestis substantia, in se temporaliter', with the doctrine that the creature is formed when it turns to the unchangeable light of the Word."),
 E("t-k8-21", "glossa-1-3", "bede-gen-1-3b", "cites", "The Bede gloss keeps the bodily light with its location and its divers letting oil from their mouths, and cuts the pun that carried Bede's argument — if a man can do it by the oil of his mouth, what can God do by the Spirit of his mouth. What is left is the observation without the reason for making it."),
 # the twelfth century
 E("t-k8-22", "bruno-gen-1-3", "aug-gnl-1-3", "contests", "Bruno asks Augustine's question in Augustine's terms — what is that light, said to be prior to sun and moon and stars? — and then refuses to answer it: God called the light Day, so light here is put for day, and there is nothing further to look for."),
 E("t-k8-23", "abelard-hex-1-3", "aug-gnl-1-3", "contests", "Neither limb of Augustine's disjunction. Abelard makes the light the distinction of the works themselves, the coming-into-distinctness of the confused heap so that it could be seen and known for what it was made for — which is Augustine's own doctrine that darkness is privation, moved from optics to knowledge, and used against him."),
 E("t-k8-24", "abelard-hex-1-3b", "vulgate-1-3", "contests", "'Notandum vero pro eo quod dicimus: Fiat lux, et facta est lux, in Hebraeo haberi: Sit lux, et fuit lux.' Abelard reports the Hebrew against the Latin he is expounding, as K7 found him doing with volitabat at PL 178:735B; the observation is right, and where he got it is unknown."),
 E("t-k8-25", "abelard-hex-1-3b", "lxx-1-3", "parallel", "The feature Abelard finds in the Hebrew — one verb twice, 'let it be' and 'it was' — is exactly what the Greek does with γενηθήτω and ἐγένετο, and exactly what the Latin's fiat / facta est does not. He draws from it the conclusion the whole bench had been reaching for by other means: no delay is interposed."),
 E("t-k8-26", "honorius-hex-1-3", "remigius-gen-1-3", "echoes", "Remigius' twilight — 'not of the kind that now is, with the sun set above, but such as is wont to be before sunrise or after sunset' — becomes Honorius' 'such a brightness as there now is before the rising of the sun', with twelve hours above the earth and twelve below added."),
 E("t-k8-27", "hugh-adnot-1-3", "honorius-hex-1-3", "parallel", "Two Paris and Regensburg sentences of the same decade with the same physics: the light is the element of fire, separated out, carried round the world in a circuit like a luminous cloud, as the sun is now."),
 E("t-k8-28", "hugh-sacr-1-3", "hugh-adnot-1-3", "echoes", "The same author giving the picture in the Adnotationes and the argument in De sacramentis: bodily things can only be lit by a bodily light, every body is in a place, and a light that made evening and morning must have moved, since without motion no span of time is traversed."),
 E("t-k8-29", "hugh-sacr-1-3", "aug-gnl-1-11", "echoes", "Augustine's question — what is the sun for, if that light already made a day — answered by making the first light the sun's placeholder: made vice et loco solis, turning by its own motion until the sun came."),
 E("t-k8-30", "rupert-gen-1-3", "honorius-hex-1-3", "contests", "Rupert states the physical reading with its details — an illumination of the air, twelve hours, three days, no luminaries — and demolishes it on a ground nobody else uses: every other day makes a substance that abides, and this one would make an unstable accident thrown over the air and snuffed out after three days, which is unworthy of the majesty that laid on sun and moon a decree that shall not pass away."),
 E("t-k8-31", "rupert-gen-1-3", "angelom-gen-1-3", "echoes", "'Melius magni et nominatissimi Patres intellexerunt naturam angelicam, lucis nomine significatam' — Rupert appeals to the Fathers for the angelic light and then goes further than they do, insisting in the next chapter that it is said not by likeness but of the thing itself: the visible light and the stars were made in the likeness of that light, not the other way about."),
 E("t-k8-32", "comestor-hs-1-3", "hugh-adnot-1-3", "echoes", "The luminous cloud verbatim — nubes lucida, driven round much as the sun is — with Hugh's element of fire dropped and the dawn brightness of Remigius and Honorius kept."),
 E("t-k8-33", "comestor-hs-1-3", "remigius-gen-1-3", "echoes", "'Claritate tamen tenui, ut fieri solet diluculo' is Remigius' before-sunrise light, two hundred and seventy years on, stated in a handbook as fact rather than as opinion."),
 E("t-k8-34", "bonaventure-sent-2-13-1-1", "aug-gnl-1-3", "contests", "Augustine's position set out at length and fairly — heaven the unformed spiritual nature, light the angelic nature formed, day the angelic consideration — granted to be probable and reasonable, and then declined: the Catholic treatise-writers approved another way, the text more readily intimates it, and the expositors more generally follow it, so it is the safer and more useful to hold."),
 E("t-k8-35", "bonaventure-sent-2-13-1-1", "comestor-hs-1-3", "parallel", "The schools' settled answer in its two registers, as at K10: Comestor prints the luminous cloud in a handbook without noticing that anyone ever thought otherwise, and Bonaventure raises the question in a disputation in order to rule the same way. The corporeal light wins by handbook and by quaestio at once."),
]

FINDING = "The two benches ask the same question and each is shut out of the other's answer by a ruling it made somewhere else. The Latin bench's dominant answer, Augustine's, is that the light is the angelic creation, made and formed on the first day; the rabbinic bench cannot reach for it, because Bereshit Rabbah has already ruled — twice, at 1:3 and again at 3:8, which is K10's witness — that nothing whatever was created on the first day besides God, precisely so that nobody could say Michael held the sky at the south and Gabriel at the north while God measured in the middle. And the rabbinic answer, that the light was too good for the wicked and was stored away for the righteous in the time to come, has no Latin counterpart at all: the Latin either turns the light into angels or turns it into a proto-sun, and the one thing it never does is take the light out of the world and keep it. Where the two do meet, they meet on the compromise nobody on either side prefers. Augustine reports, at De Genesi ad litteram I.11, that 'this too I know to have been said by someone' — that the nature of light was made on the first day and the luminaries were afterwards made out of it — and he cannot say whose opinion it is; b. Chagigah 12a gives it as the sages' answer against R. Yaakov, in the same words and to the same objection from Gen 1:17. On the Latin side alone, the crux is decided twice and each time by weight rather than by argument. Bede does not refute the angelic light, he steps round it in a single sentence by naming three lights instead of two and leaving the angels already made and elsewhere; and Bonaventure, closing the question in the schools eight hundred years after Augustine opened it, grants that Augustine's position is 'multum rationabilis' and declines it because the expositors more generally follow the other. In between, the twelfth century simply builds a physics for the light it has decided on — a body of fire in the sun's stead (Hugh), a brightness like the sky before sunrise on a twelve-hour circuit (Honorius), a luminous cloud thin as the dawn (Comestor) — while Rupert of Deutz, in the same decade, argues that a light of that kind would make the first day the poorest of the six, an unstable accident snuffed out after three days by a God who changed his mind."

# ---------------------------------------------------------------- persons new to this crux
PERSONS = {
 "pirkei-derabbi-eliezer": {"name": "Pirkei de-Rabbi Eliezer", "he": "פִּרְקֵי דְּרַבִּי אֱלִיעֶזֶר", "dates": "c. 750–850", "tradition": "rabbinic", "role": "compilation"},
 "r-shimon-b-yehotzadak": {"name": "R. Shimon ben Yehotzadak", "dates": "fl. c. 250", "tradition": "rabbinic", "role": "tradent"},
 "r-shmuel-b-nachman": {"name": "R. Shmuel bar Naḥman", "dates": "fl. c. 280", "tradition": "rabbinic", "role": "tradent"},
 "r-yitzchak": {"name": "R. Yitzḥak", "dates": "fl. c. 300", "tradition": "rabbinic", "role": "tradent"},
 "r-nechemya": {"name": "R. Neḥemya", "dates": "fl. c. 150", "tradition": "rabbinic", "role": "tradent"},
 "r-zeeira": {"name": "R. Ze'eira son of R. Abahu", "tradition": "rabbinic", "role": "tradent"},
 "r-yehuda-b-simon": {"name": "R. Yehuda bar Simon", "dates": "fl. c. 320", "tradition": "rabbinic", "role": "tradent"},
 "r-elazar": {"name": "R. Elazar ben Pedat", "dates": "d. c. 279", "tradition": "rabbinic", "role": "tradent"},
 "r-yaakov": {"name": "R. Yaakov", "tradition": "rabbinic", "role": "tradent"},
}

# ---------------------------------------------------------------- answer families new to this crux
ANSWERS = {
 "lux-corporalis": {"label": "A bodily light", "gloss": "A material light made to light material things, standing in the sun's place until the fourth day (Basil, Ambrose, Bede, Hugh, Honorius, Comestor, Bonaventure)."},
 "lux-angelica": {"label": "The angelic creation", "gloss": "The light is the spiritual creature called 'heaven' in v. 1, made light by turning to its Creator (Augustine, Angelomus, Rupert)."},
 "lux-hidden": {"label": "Stored for the righteous", "gloss": "Too good for the wicked, it was hidden away and is kept for the righteous in the time to come (Bereshit Rabbah, b. Chagigah, Rashi)."},
 "lux-garment": {"label": "From the light of his garment", "gloss": "God wrapped himself in it like a garment (Ps 104:2); the heavens were stretched out of it (Bereshit Rabbah, Pirkei de-Rabbi Eliezer)."},
 "lux-from-temple": {"label": "From the site of the Temple", "gloss": "The light was created from the place of the sanctuary (Ezek 43:2; Jer 17:12)."},
 "lux-becomes-luminaries": {"label": "The luminaries were made from it", "gloss": "The nature of light was made on day one and hung in the firmament on day four (the sages in b. Chagigah 12a; an unnamed opinion in Augustine)."},
 "lux-twilight": {"label": "A light like the dawn", "gloss": "Not the sun's brightness but what the sky is before sunrise or after sunset (Remigius, Honorius, Comestor, Hugh)."},
 "lux-is-day": {"label": "'Light' just means day", "gloss": "The verse answers itself: he called the light Day, so light here is put for day (Bruno)."},
 "lux-is-distinction": {"label": "The distinguishing of the works", "gloss": "The light is the confused heap becoming distinct and knowable, not a thing at all (Abelard)."},
 "fiat-is-instantaneous": {"label": "Speaking is making", "gloss": "No interval between the command and the thing: the Hebrew says only 'let it be, and it was' (Ambrose, Basil, Angelomus, Abelard)."},
}
SHORT = "Yehi or / fiat lux"

# ================================================================ Philo (Phase 6 part five, 2026-09-06)
# philo-opif-31 is defined here; philo-opif-30, defined on K7, also carries this crux and is folded
# into the roster by build-crux.py. The `lux-intelligibilis` answer is defined in K7's spec with
# that witness. See scripts/philo.py.
import philo
from philo import BASE as _PH, PDRAFT
from bench import greek as _gk

PERSONS.update(philo.PERSONS)
LICENSES = dict(philo.LICENSES)

add(**_PH, id="philo-opif-31",
    anchor={"verse": "gen.1.3"},
    lemma={"el": "τὸ δὲ ἀόρατον καὶ νοητὸν φῶς ἐκεῖνο θείου λόγου γέγονεν εἰκών",
           "en": "and that invisible and intelligible light has come to be an image of the divine Reason"},
    original=_gk(31),
    english={"text": "And that invisible and intelligible light has come to be an image of the divine Reason, which interpreted its genesis; and it is a supercelestial star, spring of the perceptible stars, which one would not be wide of the mark in calling all-brightness, from which the sun and the moon and the other wandering and fixed stars draw, so far as each has the power, the beams that befit them, that unmixed and pure radiance being dimmed when it begins to turn by the change from the intelligible to the perceptible.",
             **PDRAFT},
    tradents=[], cruxes=["first-light"], senses=["literal", "spiritual"],
    answers=["lux-intelligibilis", "lux-becomes-luminaries"],
    notes="The oldest answer on this daf to the question the whole crux is, and the one that gives the mechanism the others only gesture at. The light of the first day is invisible and intelligible, an image of the divine Reason; it is a supercelestial star and the spring of the perceptible stars, and the sun and moon and the rest draw their beams from it, each so far as it can, the pure radiance dimming as it turns from the intelligible to the perceptible. That is an answer to the objection that governs the Latin discussion, which is what the light was doing for three days before the sun: on this account the sun does not replace it but is filled from it. Bereshit Rabbah 3:4 asks from what the light was created and answers from the light of God's garment; the Pirkei de-Rabbi Eliezer says the same; the Latin bench splits between a bodily light and the angelic creation. Philo alone makes the relation between the first light and the luminaries a matter of derivation and degree, which is what lux-becomes-luminaries means in the Latin sources without any account of how.")

THREADS.extend([
 thread("first-light", "t-k8-p1", "philo-opif-31", "br-3-4", "parallel", "The same question, asked in the same terms, with two answers that are structurally identical and materially unrelated. Bereshit Rabbah 3:4: from what was the light created? R. Shimon says the Holy One wrapped himself in it like a garment and the splendour of his majesty shone from one end of the world to the other. Philo: the intelligible light is an image of the divine Reason, a supercelestial star and the spring of the perceptible stars. Both make the first light an overflow from God rather than a creature standing on its own, and both make the visible lights derivative from it. Neither can have read the other."),
 thread("first-light", "t-k8-p2", "philo-opif-31", "aug-gnl-1-3", "parallel", "Augustine's whether something spiritual or something bodily is the question Philo has already answered, and answered in a way that dissolves the alternative. For Philo the light of the first day is intelligible and the visible lights draw from it, so it is neither a body nor a substitute for one; it is the model. Augustine has no such category available at this point in the Genesis literature and works the question as a disjunction, which is how the Latin bench holds it for the next seven hundred years."),
 thread("first-light", "t-k8-p3", "philo-opif-31", "pdre-3-6", "parallel", "Pirkei de-Rabbi Eliezer: the light was created from the light of his garment. Philo: it is an image of the divine Reason. The two answers are the same shape, an emanation from something of God's own rather than a thing made from nothing, and they are the only two on this daf that make the first light continuous with its source. The Latin witnesses that come nearest, the angelic light of Angelomus and the Glossa's spiritual light, all make it a creature."),
 thread("first-light", "t-k8-p4", "philo-opif-30", "b-chag-12a-light", "parallel", "The Bavli says the light the Holy One created on the first day was such that a man could see from one end of the world to the other, and that seeing what the generations would do he stored it away for the righteous. Philo says the intelligible outshines the visible as the mind outshines the eyes of the body. Both are saying that the first light is out of proportion to any use the world has for it; the Bavli answers by removing it from the world, Philo by putting it in a different order of being."),
])
