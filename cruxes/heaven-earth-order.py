"""K5 — heaven-earth-order (Gen 1:1). Which was created first, and what is 'heaven' here?
Built 2026-09-05 (Phase 2, crux 5 of 9). See PHASES.md for the spec-file contract.

Two witnesses already carry this crux from earlier builds — `b-chag-12a` (K10: the ten things
created on the first day, which opens with heaven and earth) and `b-chag-15a` (K7) — and
build-crux.py folds them into the roster. They are not rebuilt here.

Gen 1:1 is crowded: K1 (`beginning-of-what`) built 34 witnesses on this verse. Every Latin slice
below was checked against K1's slice boundaries and none overlaps. Three passages that belong here
were already taken whole by K1 and are left for Phase 4 — see notes/cross-crux.md.
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, thread

CRUX_ID = "heaven-earth-order"
SHORT = "heaven and earth"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "cc-by", "attribution_required": True}

add(id="br-1-14", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ", "en": "et the heavens and et the earth"},
    original={"lang": "he", "text": hcut(sef("br-1", "he", 13, he_file="br-1-he.json")[0],
                                        "רַבִּי יִשְׁמָעֵאל שָׁאַל אֶת רַבִּי עֲקִיבָא",
                                        "לְרַבּוֹת אִילָנוֹת וּדְשָׁאִין וְגַן עֵדֶן.", "K5 br-1-14 he"),
              "source": "Bereshit Rabbah 1:14 (Vilna numbering)", **_BR_SRC},
    english={"text": hcut(sef("br-1", "en", 13)[0], "Rabbi Yishmael asked Rabbi Akiva",
                          "to include trees, vegetation, and the Garden of Eden.", "K5 br-1-14 en"), **_BR_EN},
    tradents=["r-yishmael", "r-akiva", "nachum-of-gam-zo"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["et-includes", "heaven-earth-is-everything"],
    notes="The question of what 'heaven and earth' contains, asked as a question about a particle. R. Yishmael puts it to R. Akiva, who served Naḥum of Gam Zo twenty-two years and learned from him that akh and rak restrict while et and gam include: what, then, are the two ets doing here? Akiva's first answer is theological — without them we might have said that the heavens and the earth are deities — and R. Yishmael slaps it down with Deut 32:47, if the Torah is empty it is empty because of you, because you do not exert yourself in it. Then the real answer, and it is an inventory: et ha-shamayim brings in the sun, the moon and the constellations; ve-et ha-aretz brings in the trees, the plants and the Garden of Eden. Augustine asks the identical question in Latin — what is signified by the name of heaven and earth — and answers that the two words are a name for the whole creation, given in visible terms for the sake of little ones. Ramban quotes this passage by name eight hundred years later and treats it as settling the matter.")

add(id="br-1-15", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "כְּקַדֵּרָה וְכִסּוּיָהּ", "en": "like a stewpot and its lid"},
    original={"lang": "he", "text": sef("br-1", "he", 14, he_file="br-1-he.json")[0], "source": "Bereshit Rabbah 1:15 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-1", "en", 14)[0], **_BR_EN},
    tradents=["bet-shammai", "bet-hillel", "r-yehuda-b-ilai", "r-hanin", "r-yochanan", "r-tanchuma", "r-shimon-b-yochai", "r-elazar-b-r-shimon"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-first", "earth-first", "both-at-once", "order-of-dignity"],
    notes="The crux in its classical rabbinic form, with five answers and a refusal. Beit Shammai: the heavens first, because a king has his throne made and then its footstool (Isa 66:1). Beit Hillel: the earth first, because a king building a palace builds the lower parts first, and because Gen 2:4 says 'earth and heavens'. R. Yehuda bar Ilai adds Ps 102:26, 'you laid the foundations of the earth in times past, and the heavens are the work of your hands'. R. Ḥanin turns Beit Shammai's own proof against them: 'the earth WAS' — it already was. R. Yoḥanan in the sages' name splits the question: in creation heaven was first, in completion the earth. Then R. Shimon ben Yoḥai says he is astonished that the fathers of the world should have disputed it at all, since both were created together like a stewpot and its lid (Isa 48:13, 'I call to them, they stand up together'). The section closes with a rule for reading Scripture's word order generally: where the sequence is reversed in one place, that teaches that the two are equal — turtledoves and pigeons, father and mother, heaven and earth. That rule is what Ambrose reaches independently in Milan.")

_chag = json.load(open(RAW / "b-chag-12a.json"))
def _seg(lang, a, b):
    v = [x for x in _chag["versions"] if x["language"] == lang][0]["text"]
    def flat(x): return x if isinstance(x, str) else " ".join(flat(i) for i in x)
    return " ".join(flat(v[i]) for i in range(a, b))
_CHAG_HE = {"license": "cc-by-sa", "version": [x for x in _chag["versions"] if x["language"] == "he"][0]["versionTitle"]}
_CHAG_EN = {"translator": "Sefaria Community Translation", "license": "cc0"}

add(id="b-chag-12a-order", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בֵּית שַׁמַּאי אוֹמְרִים שָׁמַיִם נִבְרְאוּ תְּחִלָּה", "en": "Beit Shammai say: the heavens were created first"},
    original={"lang": "arc", "text": _seg("he", 15, 18), "source": "b. Chagigah 12a (Vilna)", **_CHAG_HE},
    english={"text": _seg("en", 15, 18), **_CHAG_EN},
    tradents=["bet-shammai", "bet-hillel", "resh-lakish"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-first", "earth-first", "both-at-once", "created-then-stretched"],
    notes="The Babylonian redaction of the same dispute, and it argues where Bereshit Rabbah illustrates. Beit Hillel now put the objection as a question — on your view does a man build the upper storey and then the house? (Amos 9:6) — and Beit Shammai answer in kind: on your view does a man make a footstool and then a throne? (Isa 66:1). The sages say both at once, from Isa 48:13, and the Bavli will not leave it there: if 'together' only means that once made they cannot be parted, the two proof-texts still contradict each other, and Resh Lakish settles it with a distinction the Palestinian version does not have — when they were created, heaven was created first; when they were stretched out, the earth was stretched out first. It is the same move Hugh of St Victor makes in Paris six hundred years later with 'not order but dignity', and R. Yoḥanan's 'in creation first, in completion first' in Bereshit Rabbah: the sequence of the words is not the sequence of the acts.")

add(id="b-chag-12a-shamayim", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.1"}, lemma={"he": "מַאי שָׁמַיִם", "en": "What is 'heaven'?"},
    original={"lang": "arc", "text": _seg("he", 18, 19), "source": "b. Chagigah 12a (Vilna)", **_CHAG_HE},
    english={"text": _seg("en", 18, 19), **_CHAG_EN},
    tradents=["r-yose-b-chanina"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["shamayim-is-water"],
    notes="The crux's second half asked in three words — mai shamayim, what is heaven — and answered from the name itself. R. Yose bar Ḥanina: sham mayim, 'there is water'. A mishnaic tradition: fire and water, which the Holy One brought and mingled with each other, and out of them made the firmament. It is an answer of exactly the kind the Latin bench never gives, because the Latin word yields nothing: caelum can be etymologised (Isidore tries chaos, others caelare, 'to engrave', for the stars) but it cannot be made to spell out what heaven is made of. Where the Bavli reads the substance out of the noun, Remigius and the Glossa have to import a substance — the empyrean, fiery not by heat but by brightness — from elsewhere.")

add(id="b-chag-12a-akiva", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.1"}, lemma={"he": "מַאי דָּרַשׁ בְּאֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ", "en": "what did he expound on 'et the heavens and et the earth'?"},
    original={"lang": "arc", "text": _seg("he", 19, 20), "source": "b. Chagigah 12a (Vilna)", **_CHAG_HE},
    english={"text": _seg("en", 19, 20), **_CHAG_EN},
    tradents=["r-yishmael", "r-akiva", "nachum-of-gam-zo"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["et-includes"],
    notes="The same encounter as Bereshit Rabbah 1:14 — R. Yishmael asking R. Akiva what Naḥum of Gam Zo made of the two ets — and the answer has changed. Here Akiva says that without the particles he would have taken shamayim to be a name of the Holy One, blessed be He; now that the text reads et ha-shamayim ve-et ha-aretz, heaven means heaven literally and earth means earth literally. In the Palestinian version the danger is that the heavens and the earth would be taken for deities and Akiva is rebuked for the answer; here the danger is narrower, that one word would be a divine name, and the answer stands unchallenged. Both are a Jewish witness to the same anxiety the Latin bench meets at Megillah 9a and in the Greek word order (K3). And note what neither version does: it never occurs to either that the et might include the angels.")

_ie = json.load(open(RAW / "ibn-ezra-gen-1.json"))
def _ie_text(lang, idx):
    v = [x for x in _ie["versions"] if x["language"] == lang][0]["text"][idx]
    return v if isinstance(v, str) else " ".join(v)
add(id="ibn-ezra-1-1b", work="ibn-ezra-gen", author="ibn-ezra", tradition="rabbinic",
    date=1155, date_precision="circa", place="lucca",
    anchor={"verse": "gen.1.1"}, lemma={"he": "שְׁמֵי הַשָּׁמַיִם", "en": "the heavens of the heavens"},
    original={"lang": "he", "text": hcut(_ie_text("he", 1), 'ואל תתמה על וי"ו והארץ', "כי רחוק הוא מאמצע הארץ", "K5 ibn-ezra he"),
              "source": "Ibn Ezra on Gen 1:2, s.v. והארץ (on the heavens of v. 1)", "license": "pd", "version": "Piotrkow, 1907–1911"},
    english={"text": hcut(_ie_text("en", 1), "Now don’t be surprised by the vav of veha’aretz",
                          "for it was distant from the center of the earth.", "K5 ibn-ezra en"),
             **{"translator": "Sefaria Community Translation", "license": "cc0"}},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["one-earth-only"],
    notes="A grammarian refusing the whole allegorical apparatus, and the argument is a symmetry argument. Moses, he says, did not speak of the world to come, which is the world of the angels, but of this world of coming-to-be and passing-away; and to those who explain that the heavens of the first verse are really the heavens of the heavens he puts one question — then what will you do with the earth? If shamayim in v. 1 is the intelligible heaven, aretz beside it must be something other than the ground, and no one is willing to say so. That is precisely the position of Remigius, the Glossa and Comestor, who take the heaven of v. 1 to be the empyrean and are then obliged to make the earth beside it into prime matter or the four elements. Ibn Ezra also disposes of the seven earths: there is one earth, divided into seven settled regions, with the Temple at the centre of the settlement and not at the centre of the globe.")

_ram = json.load(open(RAW / "ramban-gen-1.json"))
def _ram_text(lang):
    v = [x for x in _ram["versions"] if x["language"] == lang][0]["text"][0]
    return v if isinstance(v, str) else " ".join(v)
add(id="ramban-1-1b", work="ramban-gen", author="ramban", tradition="rabbinic",
    date=1267, date_precision="range-1263-1270", place="girona",
    anchor={"verse": "gen.1.1"}, lemma={"he": "וְהָאָרֶץ תִּכְלֹל אַרְבַּע הַיְּסוֹדוֹת", "en": "'the earth' includes all four elements"},
    original={"lang": "he", "text": hcut(_ram_text("he"), '"וְהָאָרֶץ" תִּכְלֹל אַרְבַּע הַיְּסוֹדוֹת',
                                        "וְאֵלּוּ כְּלַל כָּל הַנִּבְרָאִים בַּעַל הַגּוּף.", "K5 ramban he"),
              "source": "Ramban on Gen 1:1, s.v. בראשית (the four elements and the particle et)", "license": "cc-by", "version": "Sefaria 'Vocalized Edition'"},
    english={"text": hcut(_ram_text("en"), "And the earth, includes all the four elements",
                          "These include all created things which are corporeal.", "K5 ramban en"),
             "translator": "Charles B. Chavel, 1971–76", "license": "chavel-ramban"},
    tradents=["r-yishmael", "r-akiva"],
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-earth-four-elements", "et-includes", "heaven-earth-is-everything"],
    notes="Ramban gives the Latin schools' answer and the midrash's answer in the same paragraph, and does not notice that they are two. 'The earth' takes in all four elements — as in 'the heavens and the earth were finished', which covers the whole lower sphere, and 'praise the Lord from the earth, you sea-monsters and all deeps' — which is Abelard's reading of the verse to the letter, and Ambrose's before him. Then the particle: et is like 'the essence of a thing', and the Sages have always expounded it as including, so that et ha-shamayim brings in the sun, moon, stars and constellations and ve-et ha-aretz the trees, herbs and the Garden of Eden. He names Bereshit Rabbah for it. The two answers pull opposite ways — one makes the two words a physics of elements, the other an inventory of furniture — and the sentence that joins them is 'these include all created things which are corporeal'. Chavel's English shows on Sefaria as CC BY; licence key chavel-ramban is marked for checking before publication.")

# ---------------------------------------------------------------- latin bench, patristic
add(id="ambrose-hex-1-6-20", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "In his enim quatuor illa elementa creata sunt", "en": "For in these two the four elements were created"},
    original=latin("6958", "In principio itaque temporis coelum et terram Deus fecit.", "quae in omnibus sibi mixta sunt.", 14),
    english={"text": "In the beginning of time, then, God made heaven and earth. For time is from this world, not before the world; and a day is a portion of time, not its beginning. And although from the order of the reading we could establish that the Lord first made day and night, which are the alternations of times, and on the second day made the firmament, by which he divided the water which is under heaven from the water which is above heaven — yet for the present assertion it is enough that in the beginning he made heaven, from which comes the prerogative of generation and its cause; and made earth, in which the substance of generation should be. For in these two the four elements were created, out of which are generated all these things which belong to the world. And the elements are four — air, fire, water, and earth — which are mingled with one another in all things. Indeed you will find fire in the earth too, which is often struck out of stones and iron; and in heaven, since the vault is fiery and glitters with shining stars, water can be understood to be, which is either above heaven, or is often sent down from that upper place upon the earth in a full shower.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-earth-four-elements"],
    notes="The chapter heading Migne prints over this is the crux itself: 'that in heaven and earth the four elements were created, out of which all things are composed; of what substance heaven is, and what the position of the earth.' Ambrose's answer is that the two words are a container for the four elements — heaven supplying the prerogative and cause of generation, earth the substance of it — and he proves the mixture empirically, fire struck from flint and iron in the earth, water inferred in heaven from the rain and from the waters above. It is Abelard's reading of the verse seven hundred years early and Ramban's a century after Abelard, and none of the three cites another. Rabanus copies this paragraph verbatim at PL 107:444B, where K1 has already built it.")

add(id="ambrose-hex-1-6-24", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "nihil interest quid prius exprimas, cum simul utrumque sit factum", "en": "it makes no difference which you utter first, since both were made together"},
    original=latin("6958", "Dixit enim David: Principio terram tu fundasti", "primogenitae creaturae privilegio potior aestimetur.", 14),
    english={"text": "For David said: 'In the beginning you founded the earth, Lord, and the heavens are the works of your hands. They shall perish, but you remain, and all shall grow old as a garment, and as a cloak you shall change them, and they shall be changed; but you are the same, and your years shall not fail' (Ps 102:26 [Vg 101:26]). Which the Lord so confirmed in the Gospel that he said: 'Heaven and earth shall pass away, but my words shall not pass away' (Matt 24:35). Those, then, accomplish nothing who thought a fifth, ethereal body had to be brought in to establish the perpetuity of heaven — since they equally see that a part of a single limb joined on unlike the rest usually brings more harm to the body. Note this at the same time, that when the prophet David named the earth in the first place (Ps 148:5) and heaven afterwards, he judged that the work of the Lord had to be declared; for when he said 'and they were made', it makes no difference which you utter first, since both were made together — and at the same time, lest even this prerogative should seem to be adjudged to heaven's divine substance, that it should be reckoned the better by the privilege of being the firstborn creature.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["both-at-once", "order-of-dignity"],
    notes="The Latin answer that matches the rabbinic one exactly, and it turns on the same verse. Ps 102:26 names the earth first and the heavens second — the proof R. Yehuda bar Ilai brings for Beit Hillel in Bereshit Rabbah 1:15 — and Ambrose draws from it not that the earth was made first but that the order of naming decides nothing, since both were made together; and then the reason, which is the interesting half: lest heaven be given the privilege of the firstborn. That is R. Shimon ben Yoḥai's stewpot and its lid, and it is Bereshit Rabbah's closing rule that a reversed order teaches equality of honour. Two benches, one psalm verse, the same conclusion, and no contact of any kind.")

add(id="aug-gnm-1-7-11", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-389", place="thagaste",
    anchor={"verse": "gen.1.1"}, lemma={"la": "coeli et terrae nomine universa creatura significata est", "en": "by the name of heaven and earth the whole creation is signified"},
    original=latin("7303", "Sed illud quod dictum est, In principio fecit Deus coelum et terram, coeli et terrae nomine", "quod aliqui codices habent, de materia invisa.", 34),
    english={"text": "But as to what is said, 'In the beginning God made heaven and earth' — by the name of heaven and earth the whole creation is signified, which God made and founded. And these were called by the names of visible things on account of the weakness of little ones, who are less able to grasp invisible things. First, then, was made the confused and formless matter, out of which should be made all the things that are distinguished and formed — which I believe is called chaos by the Greeks. For so we read it said elsewhere too, in the praises of God: 'You who made the world out of formless matter' (Wis 11:17) — which some manuscripts have as 'out of unseen matter'.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-earth-is-everything", "pair-is-formless-matter"],
    notes="The answer that dissolves the question. 'Heaven and earth' is not a list of two things in an order; it is a name for everything God made, put in visible words because the audience cannot yet hold invisible ones. The Bavli's ten-things list is answering the same question — what does 'heaven and earth' contain, and what else was made with them — and answers it by enumeration where Augustine answers it by generalisation. Note also the variant Augustine records at the end: some copies of Wis 11:17 read 'de materia invisa' for 'de materia informi'. His own text of Gen 1:2, 'invisibilis et incomposita', is the reason he notices.")

add(id="aug-gnl-1-9", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "prius universaliter … deinde per partes", "en": "first universally … then in its parts"},
    original=latin("7302", "Et cur ita dictum est, In principio fecit Deus coelum et terram; et non dictum est", "quidquid fecit?", 34),
    english={"text": "And why is it said thus, 'In the beginning God made heaven and earth', and not said, 'In the beginning God said, Let heaven and earth be made; and heaven and earth were made', as it is told of the light, 'God said, Let there be light; and light was made'? Was it that first, under the name of heaven and earth, what God made had to be taken in universally and commended; and then to be gone through in its parts — how he made it — when at each thing it is said, 'God said', that is, because through his Word he made whatever he made?", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["whole-then-parts", "heaven-earth-is-everything"],
    notes="A question about the shape of the sentence, and the answer settles what 'heaven and earth' is doing in it: the phrase is a heading. Scripture takes the whole in at one stroke and commends it, and only then goes through the parts with 'God said' at each — which is why v. 1 has no 'let there be' in it. Augustine offers a second answer immediately after (that formless matter cannot be addressed with 'let it be made', since it does not yet imitate the Word), which belongs to K4. This paragraph is the one the Carolingians take: Angelomus compresses it into two lines, and it stands at the head of the Glossa's VERS. 1 in the margin, which K1 has already sliced whole.")

add(id="alcuin-int-28", work="alcuin-int", author="alcuin", tradition="latin",
    date=796, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.1"}, lemma={"la": "non quia jam hoc erat, sed quia jam hoc esse poterat", "en": "not because it already was this, but because it already could be this"},
    original=latin("21416", "Inter. 28. Quid in coeli terraeque nomine significatur", "spirituales et terrenae creaturae intelligi possunt.", 100),
    english={"text": "Question 28. What is signified by the name of heaven and earth, when it is said, 'In the beginning God made heaven and earth' (Gen 1:1)? — Answer. That formless matter, which God made out of nothing, was first called heaven and earth: not because it already was this, but because it already could be this. For on the second day this starry heaven is read to have been made, and on the third day the earth to have appeared and begun to be clothed with flowers. Or else, by the name of heaven and earth the spiritual and the earthly creatures can be understood.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-earth-is-everything", "heaven-is-empyrean"],
    notes="Augustine reduced to a rule a pupil can hold: heaven and earth in v. 1 are the names of formless matter, given proleptically — not because it already was this, but because it already could be this — and the proof is the calendar, since the starry heaven comes on the second day and the earth appears on the third. Then, as usual, Alcuin adds the alternative without weighing it: 'or else the spiritual and the earthly creatures'. That second answer is the seed of the empyrean reading which Remigius, the Glossa and Comestor will make the standard one.")

# ---------------------------------------------------------------- latin bench, Carolingian and after
add(id="angelom-gen-1-1b", work="angelom-gen", author="angelomus", tradition="latin",
    date=850, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.1"}, lemma={"la": "prius universaliter nomine coeli et terrae comprehendendum erat", "en": "first it had to be taken in universally under the name of heaven and earth"},
    original=latin("9032", "Sed quaeritur cur ita dictum est: In principio fecit Deus coelum et terram", "sicuti actum legitur.", 115),
    english={"text": "But it is asked why it is said thus: 'In the beginning God made heaven and earth', and not said: 'In the beginning God said, Let heaven and earth be made', as it is told of the light: 'God said, Let there be light', and the rest? — Unless because first what he made had to be taken in universally under the name of heaven and earth, and commended, and then gone through in its parts, as it is read to have been done.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["whole-then-parts"],
    notes="Augustine's question and his first answer, compressed to two sentences and shorn of the second answer that made the first provisional. What in De Genesi ad litteram is one horn of a dilemma ('was it that…? or was it that…?') is here the explanation, flatly. The sentences that follow immediately are Angelomus' treatment of 'empty and void' (built at K6), so this witness and that one are one continuous stretch of his commentary divided between two cruxes.")

add(id="remigius-gen-1-1b", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.1"}, lemma={"la": "illud empyreum, id est igneum, vel intellectuale coelum", "en": "that empyrean, that is fiery, or intellectual heaven"},
    original=latin("9346", "Creavit enim coelum et terram. Coelum non istud visibile", "in sequentibus fit commemoratio.", 131),
    english={"text": "'For he created heaven and earth.' By 'heaven' we ought not to understand this visible firmament, but that empyrean — that is, fiery, or intellectual — heaven, which is called fiery not from burning but from brightness, and which was at once filled with the angelic spirits, of whom it is said in Job: 'When the morning stars praised me together, and all the sons of God shouted for joy' (Job 38:7). And note that three elements are named here. For under the name of heaven gather the air; under the name of earth, the earth itself, and the fire that lies hidden in its bowels. Of the fourth element, that is water, mention is made in what follows.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-is-empyrean", "heaven-earth-four-elements"],
    notes="The empyrean enters the Latin gloss tradition here in the form it will keep: not the visible firmament but a fiery heaven, and fiery from brightness rather than heat — the qualification matters, because it is what makes the fire intelligible rather than physical — filled with angels the moment it was made, on the authority of Job 38:7. The Glossa prints this sentence almost word for word at PL 113:68C, inside the VERS. 1 block that K1 slices whole, and from there it reaches Comestor. Remigius then counts the elements out of the two words and finds only three, water being held over to v. 2 — where Ambrose and Abelard find all four.")

add(id="abelard-hex-1-1b", work="abelard-hex", author="abelard", tradition="latin",
    date=1130, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Coeli et terrae nomine hoc loco quatuor elementa comprehendi arbitror", "en": "By the name of heaven and earth I judge the four elements to be taken in here"},
    original=latin("11118", "Coeli et terrae nomine hoc loco quatuor elementa", "humanae igitur res Providentia reguntur. »", 178),
    english={"text": "By the name of heaven and earth I judge the four elements to be taken in here, out of which, as out of a material first beginning, all other bodies are agreed to be composed. By 'heaven' he means the two light elements, that is fire and air. The remaining two, which are heavy, he calls generally 'earth'. For we call heaven both the airy — as in 'the birds of heaven' — and the ethereal, which is fiery. Whence it is not unfitting that he here names both air and fire 'heaven'. It is agreed too that the ethereal heaven, in that its fire is purer, is properly wont to be called heaven; whence with reason the name of heaven, since the purer the fire the lighter its nature, is here put, as has been said, for the two light elements, fire and air. Just so, on the contrary, by 'earth', whose nature is most heavy and weighty, he marks out both the earth itself and the water that clings to it. These four elements, then, as the first principles of all other bodies, he announces that God made in the beginning. And what he says is as if he said: In the beginning, before all those things which he enumerates in order, and of whose completion he adds afterwards, 'Thus the heavens were finished' (Gen 2:1). What he says, 'in the beginning' of the works that follow, is as if he said: In the beginning of the world, that is, before he brought about anything of those things which belong to the world. For the angels, being of an incorporeal nature, are not included among the creatures of the world, as men are, of whom the philosopher makes mention in the third book of the Topics: 'The world,' he says, 'is governed by Providence; but men are a part of the world; therefore human affairs are governed by Providence.'", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-earth-four-elements", "one-earth-only"],
    notes="The most thoroughly physical reading of the verse on the Latin bench, and it ends by throwing the angels out. Heaven names the two light elements, fire and air; earth names the two heavy, earth and the water that clings to it; and the whole verse announces that God made the four elements as the first principles of bodies. Then the consequence, stated without embarrassment: the angels are not included among the creatures of the world at all, being incorporeal, so 'in the beginning of the world' does not touch them — and Boethius' Topics is quoted for the premise that men are a part of the world. That is the exact position Remigius and the Glossa deny, and it is what Ibn Ezra argues for in Lucca, from the other direction, when he asks those who make the heavens of v. 1 the heaven of heavens what they will then do with the earth.")

add(id="hugh-sacr-1-1b", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "non ordinis sed dignitatis causa sic positum", "en": "so placed not for the sake of order but of dignity"},
    original=latin("11082", "Duo in principio posita sunt coelum et terra.", "Ergo coelum supra terram erat.", 176),
    english={"text": "Two things are set down in the beginning, heaven and earth. Which of these do you suppose was below, and which shall we say was above? Either earth above and heaven below, or earth below and heaven above? But is it to be believed that in that first condition of things heaven was created underneath, and afterwards in the forming was set above? Perhaps, because Scripture named heaven before earth, someone may say that heaven was created below as a foundation. But I judge it to be so placed not for the sake of order but of dignity; and because the discourse that follows had to be about the element of earth, as about the nearer thing — and for this reason named later — therefore heaven had to be named first and earth afterwards. Nor indeed would the very nature of the things founded allow any other order of position or placing than that the weighty should be disposed downward and the light upward. Therefore the earth was below and heaven above, and what was above the earth was heaven. Therefore heaven was above the earth.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["order-of-dignity"],
    notes="Hugh takes the question seriously enough to consider the absurd answer — that heaven was made underneath, as a foundation, because it is named first — and then gives the school's rule: word order is dignity, not sequence. His second reason is better than his first and is entirely about composition: the discourse that follows is going to be about the earth, so the earth is named last, nearest to what comes next. That is a claim about how the sentence was written rather than about what happened, and it is R. Yoḥanan's distinction between creation and completion, and Resh Lakish's between creating and stretching, arrived at from the writer's side rather than the world's.")

add(id="comestor-hs-1-1b", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "id est continens et contentum", "en": "that is, the container and the thing contained"},
    original=latin("11575", "Mundus quatuor modis dicitur", "terram inferiores et palpabiles.", 198),
    english={"text": "'World' is said in four ways: sometimes the empyrean heaven is called world, on account of its cleanness; sometimes the sensible world, which is called by the Greeks pan and by the Latins 'all', because the philosopher did not know the empyrean; sometimes the region below the moon alone, because this alone has the living creatures known to us — of which it is said, 'The prince of this world shall be cast out' (John 12:31); sometimes man is called a world, because he presents in himself the image of the whole world, whence by the Lord man was called 'every creature', and the Greek calls man microcosm, that is, the lesser world. Now the empyrean and the sensible world and the sublunary region God created, that is, made out of nothing; but man he created, that is, moulded. Of the creation, then, of those three the lawgiver says: 'In the beginning God created heaven and earth' (Gen 1) — that is, the container and the thing contained, that is, the empyrean heaven and the angelic nature. But 'earth' is the matter of all bodies, that is, the four elements, that is, the sensible world consisting of them. Some understand 'heaven' as the upper parts of the sensible world, and 'earth' as the lower and palpable.", **DRAFT},
    cruxes=["heaven-earth-order"], senses=["literal"],
    answers=["heaven-is-empyrean", "heaven-earth-four-elements", "heaven-earth-is-everything"],
    notes="The twelfth-century synthesis, and it is the most systematic thing said on this crux in Latin: four senses of 'world' laid out first, so that when the verse is read the reader already knows which world is meant. Heaven and earth are then 'the container and the thing contained' — the empyrean heaven with the angelic nature, and the matter of all bodies, the four elements. Remigius' empyrean and Abelard's elements are here in one sentence, which is what Comestor is for; and the aside that the philosopher did not know the empyrean is a quiet acknowledgement that the best-attested part of this reading has no ancient authority behind it. He then reports the rival, flatter reading — heaven the upper parts of the sensible world, earth the lower — without deciding.")

# ---------------------------------------------------------------- threads (K5)
THREADS = [
 E("t-k5-01", "b-chag-12a-order", "br-1-15", "parallel", "The same dispute in two redactions. Both give Beit Shammai the throne and footstool (Isa 66:1), Beit Hillel Gen 2:4, and the sages 'both at once' from Isa 48:13. Bereshit Rabbah adds the palace built from the ground up, R. Ḥanin's turning of Beit Shammai's proof, and R. Shimon ben Yoḥai's stewpot and lid; the Bavli adds Amos 9:6 for the upper storey and Resh Lakish's created-first/stretched-first distinction. Independent redactions of one Palestinian dispute."),
 E("t-k5-02", "b-chag-12a-akiva", "br-1-14", "parallel", "One encounter, two answers. Both have R. Yishmael asking R. Akiva what Naḥum of Gam Zo made of the two ets. In Bereshit Rabbah, Akiva's first answer is that without them we might have said heaven and earth were deities, and he is rebuked for it with Deut 32:47 before the real answer (the sun, moon and constellations; the trees, plants and Eden). In the Bavli the danger is narrower — shamayim would be a name of the Holy One — and the answer, that heaven means heaven literally, stands unchallenged."),
 E("t-k5-03", "b-chag-12a-shamayim", "b-chag-12a-order", "echoes", "The sugya passes from when heaven was made to what heaven is without a break: Resh Lakish's stretching, then 'mai shamayim' — sham mayim, or fire and water mingled into the firmament. The Bavli treats the two halves of this crux as one question."),
 E("t-k5-04", "ramban-1-1b", "br-1-14", "cites", "'And so did our Rabbis say: eth hashamayim — eth includes the sun, moon, stars and constellations; ve'eth ha'aretz — ve'eth includes the trees, herbs, and the Garden of Eden.' Ramban names Bereshit Rabbah (parashah 1) and reproduces the inventory, adding only the derivation of et from 'atha boker' (Isa 21:12)."),
 E("t-k5-05", "ramban-1-1b", "abelard-hex-1-1b", "parallel", "'The word ha'aretz includes these four elements' and 'by the name of heaven and earth I judge the four elements to be taken in here' are the same reading of the verse, reached in Girona and at the Paraclete a century and a half apart with no possible contact. The distribution differs: Abelard splits the four between the two words, Ramban puts all four under 'earth'."),
 E("t-k5-06", "abelard-hex-1-1b", "ambrose-hex-1-6-20", "parallel", "'In these two the four elements were created' (Ambrose) and 'by the name of heaven and earth the four elements are taken in' (Abelard) are one doctrine, and both argue it from the mixture of the elements in each other. Abelard does not cite Ambrose, and his division of the four is his own: Ambrose puts all four in the pair without assigning them, Abelard gives fire and air to heaven, earth and water to earth."),
 E("t-k5-07", "ambrose-hex-1-6-24", "br-1-15", "parallel", "The star thread of this crux. Both turn on Ps 102:26 [Vg 101:26], 'you founded the earth … and the heavens are the work of your hands' — which names the earth first. R. Yehuda bar Ilai brings it as proof for Beit Hillel that the earth was created first. Ambrose brings the same reversal (from Ps 148:5) to prove that the order of naming settles nothing, since both were made together, and adds the reason: lest heaven be reckoned the better by the privilege of being the firstborn creature. That is R. Shimon ben Yoḥai's stewpot and lid and Bereshit Rabbah's closing rule that a reversed order teaches equality of honour, in Milan, four hundred years earlier, with no contact of any kind."),
 E("t-k5-08", "b-chag-12a", "aug-gnm-1-7-11", "parallel", "Both answer the question 'what is contained in heaven and earth?' — and answer it in opposite modes. Rav Yehudah in Rav's name enumerates: ten things were created on the first day, and heaven and earth head the list, each proved from its verse. Augustine generalises: by the name of heaven and earth the whole creation is signified, put in visible words for the weakness of little ones. An enumeration and a generalisation of the same clause, at roughly the same date, with no contact."),
 E("t-k5-09", "aug-gnl-1-9", "aug-gnm-1-7-11", "echoes", "Twenty years apart, the same observation about the shape of v. 1 — that it commends the whole before the parts — first as a remark about visible names for little ones, then as the answer to why Scripture does not say 'let heaven and earth be made'."),
 E("t-k5-10", "angelom-gen-1-1b", "aug-gnl-1-9", "cites", "'Sed quaeritur cur ita dictum est … Nisi quia prius universaliter nomine coeli et terrae comprehendendum erat, et commendandum quod fecit, et deinde per partes exsequendum' reproduces De Genesi ad litteram I.9 sentence for sentence, unnamed, and drops the second answer that made the first one provisional."),
 E("t-k5-11", "alcuin-int-28", "aug-gnm-1-7-11", "echoes", "'Informis illa materia, quam de nihilo fecit Deus, appellata est primo coelum et terra' is Augustine's answer with the proleptic reason added ('not because it already was this, but because it already could be this'); the alternative Alcuin appends without weighing it — 'or else the spiritual and the earthly creatures' — is not Augustine's here and is the seed of the empyrean reading."),
 E("t-k5-12", "comestor-hs-1-1b", "remigius-gen-1-1b", "echoes", "The empyrean heaven, fiery from brightness and not from heat, filled at once with the angelic spirits: Remigius states it at PL 131:54D, the Glossa prints it almost verbatim at 113:68C, and Comestor has it as 'the empyrean heaven and the angelic nature'. Comestor adds the admission Remigius does not make — that the philosopher did not know the empyrean."),
 E("t-k5-13", "comestor-hs-1-1b", "abelard-hex-1-1b", "echoes", "'Terram vero materiam omnium corporum, id est quatuor elementa' is Abelard's reading of the second word, absorbed into a scheme that keeps the empyrean for the first; Comestor then reports the rival reading — 'some understand heaven as the upper parts of the sensible world, and earth as the lower' — without deciding between them."),
 E("t-k5-14", "abelard-hex-1-1b", "remigius-gen-1-1b", "contests", "Directly opposed on what 'heaven' names in this verse. Remigius: not the visible firmament but the empyrean, filled at once with angels. Abelard: fire and air, and 'the angels, being of an incorporeal nature, are not included among the creatures of the world at all'. Abelard does not name Remigius, but the empyrean-with-angels is the standing gloss he is writing against."),
 E("t-k5-15", "ibn-ezra-1-1b", "remigius-gen-1-1b", "parallel", "The objection to the empyrean reading, made from the other bench and with no knowledge of it: those who explain that the heavens of the first verse are the heavens of the heavens — what will they then do with the earth beside it? Ibn Ezra's symmetry argument is exactly what forces Remigius, the Glossa and Comestor to turn 'earth' into prime matter or the four elements once they have made 'heaven' the empyrean."),
 E("t-k5-16", "hugh-sacr-1-1b", "br-1-15", "parallel", "Both refuse to read the sequence of the words as the sequence of the acts, and both put something else in its place. Hugh: 'not for the sake of order but of dignity', and because the discourse that follows is about the earth, which is therefore named last. R. Yoḥanan in the sages' name: in creation the heavens were first, in completion the earth. The Latin reason is compositional, the rabbinic one is about the work itself."),
 E("t-k5-17", "hugh-sacr-1-1b", "b-chag-12a-order", "parallel", "Resh Lakish resolves the contradiction of the proof-texts by splitting the act — created in one order, stretched out in the other. Hugh resolves the same difficulty by splitting the sentence from the act. Neither will let one verse's word order overrule the other's."),
 E("t-k5-18", "br-1-15", "b-chag-15a", "echoes", "Both measure the relation of the upper and lower by a physical image and refuse to let them come apart: the stewpot and its lid, which are made together and belong together (Isa 48:13); Ben Zoma's three fingerbreadths between the upper and lower waters, a gap that is not a separation. The same instinct about heaven and earth, in the two Chagigah contexts this project has built."),
 E("t-k5-19", "comestor-hs-1-1b", "alcuin-int-28", "echoes", "Alcuin's unweighed alternative — 'or else, by the name of heaven and earth the spiritual and the earthly creatures can be understood' — is what Comestor has hardened into 'the container and the thing contained, that is, the empyrean heaven and the angelic nature' on one side and the four elements on the other."),
 E("t-k5-20", "ramban-1-1b", "b-chag-12a-akiva", "parallel", "Ramban gives the Palestinian form of the et-derivation (sun, moon, stars, constellations; trees, herbs, Eden) and not the Babylonian one (that without the particles shamayim would be a divine name), although both were before him — the inventory is usable for his physics and the anxiety about the divine name is not."),
]

FINDING = ("Both benches ask which was made first, and both end by refusing the question — and they refuse it with the "
           "same psalm. Ps 102:26 names the earth before the heavens: R. Yehuda bar Ilai brings it for Beit Hillel, "
           "Ambrose brings the same reversal to prove that the order of naming settles nothing, 'lest heaven be "
           "reckoned the better by the privilege of being the firstborn creature' — which is R. Shimon ben Yoḥai's "
           "stewpot and its lid and Bereshit Rabbah's closing rule that a reversed order teaches equality of honour. "
           "Where the two benches genuinely divide is on the second half of the question. Asked what 'heaven' is, the "
           "Bavli reads the answer out of the Hebrew noun — sham mayim, 'there is water' — while Latin, whose word "
           "will not spell anything, has to import a substance, and imports the empyrean: a fiery heaven, fiery from "
           "brightness and not from heat, filled with angels the moment it was made, which Comestor admits in passing "
           "that no ancient philosopher knew. Abelard throws it out and puts the four elements back, and Ibn Ezra, who "
           "never heard of him, makes the same objection from the other side: if the heavens of v. 1 are the heavens "
           "of the heavens, what will you do with the earth?")

# ---------------------------------------------------------------- persons / places / answers this crux adds
PERSONS = {
 "bet-shammai": {"name": "Beit Shammai", "he": "בֵּית שַׁמַּאי", "dates": "1st c.", "tradition": "rabbinic", "role": "tradent"},
 "bet-hillel": {"name": "Beit Hillel", "he": "בֵּית הִלֵּל", "dates": "1st c.", "tradition": "rabbinic", "role": "tradent"},
 "r-yishmael": {"name": "R. Yishmael", "he": "רַבִּי יִשְׁמָעֵאל", "dates": "d. c. 135", "tradition": "rabbinic", "role": "tradent"},
 "r-akiva": {"name": "R. Akiva", "he": "רַבִּי עֲקִיבָא", "dates": "c. 50–135", "tradition": "rabbinic", "role": "tradent"},
 "nachum-of-gam-zo": {"name": "Naḥum of Gam Zo", "he": "נַחוּם אִישׁ גַּם זוּ", "dates": "fl. c. 90–110", "tradition": "rabbinic", "role": "tradent"},
 "r-yehuda-b-ilai": {"name": "R. Yehuda bar Ilai", "dates": "fl. c. 140–165", "tradition": "rabbinic", "role": "tradent"},
 "r-hanin": {"name": "R. Ḥanin", "dates": "fl. c. 300", "tradition": "rabbinic", "role": "tradent"},
 "r-tanchuma": {"name": "R. Tanḥuma", "dates": "fl. c. 380", "tradition": "rabbinic", "role": "tradent"},
 "r-shimon-b-yochai": {"name": "R. Shimon ben Yoḥai", "he": "רַבִּי שִׁמְעוֹן בֶּן יוֹחַאי", "dates": "fl. c. 140–165", "tradition": "rabbinic", "role": "tradent"},
 "r-elazar-b-r-shimon": {"name": "R. Elazar be-Rabbi Shimon", "dates": "fl. c. 165–200", "tradition": "rabbinic", "role": "tradent"},
 "r-yose-b-chanina": {"name": "R. Yose bar Ḥanina", "dates": "fl. c. 270", "tradition": "rabbinic", "role": "tradent"},
}

PLACES = {}

ANSWERS = {
 "heaven-first": {"label": "Heaven first", "gloss": "Beit Shammai: the word order is the order of the acts, and a king has his throne made before its footstool (Isa 66:1)."},
 "earth-first": {"label": "Earth first", "gloss": "Beit Hillel: a builder raises the lower storey first (Amos 9:6), and Gen 2:4 and Ps 102:26 name the earth before the heavens."},
 "both-at-once": {"label": "Both together", "gloss": "The sages, and R. Shimon ben Yoḥai's stewpot and its lid (Isa 48:13); Ambrose, that the order of naming gives heaven no privilege of the firstborn."},
 "order-of-dignity": {"label": "Named for dignity, not order", "gloss": "Heaven stands first because it is worthier, or because the account is about to turn to the earth (Hugh of St Victor; R. Yoḥanan's creation-and-completion)."},
 "created-then-stretched": {"label": "Created in one order, stretched in the other", "gloss": "Resh Lakish: heaven was created first, the earth was stretched out first — so both proof-texts stand."},
 "heaven-earth-is-everything": {"label": "A name for the whole creation", "gloss": "Two visible words standing for all that God made, given so for the weakness of little ones (Augustine, Alcuin, Angelomus, Comestor)."},
 "heaven-is-empyrean": {"label": "The empyrean heaven", "gloss": "Not the visible firmament but a fiery — from brightness, not heat — and intellectual heaven, filled with angels as soon as it was made (Remigius, the Glossa, Comestor)."},
 "heaven-earth-four-elements": {"label": "The four elements", "gloss": "Heaven names fire and air, earth names earth and water; the verse announces the material first principles of bodies (Ambrose, Abelard, Ramban, Comestor)."},
 "et-includes": {"label": "The particle includes", "gloss": "Et ha-shamayim brings in the sun, moon and constellations; ve-et ha-aretz the trees, the plants and the Garden of Eden (Bereshit Rabbah 1:14, b. Chagigah 12a, Ramban)."},
 "shamayim-is-water": {"label": "Sham mayim — 'there is water'", "gloss": "The name itself says what heaven is made of: water, or fire and water mingled into the firmament (b. Chagigah 12a)."},
 "one-earth-only": {"label": "One earth, and no heaven of heavens here", "gloss": "If the heavens of v. 1 were the intelligible heaven, the earth beside it could not be the ground; the seven earths are seven regions of the one (Ibn Ezra; Abelard, from the other end)."},
 "whole-then-parts": {"label": "The whole first, then the parts", "gloss": "V. 1 is a heading: Scripture commends everything God made in two words before going through it with 'God said' (Augustine, Angelomus, the Glossa)."},
}

LICENSES = {}
