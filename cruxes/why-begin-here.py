"""K2 — why-begin-here (Gen 1:1). Why does Scripture open with creation at all?
Built 2026-09-05 (Phase 2, crux 9 of 9 — the last).

⚠ **Anchor rule.** Four of this crux's ten witnesses are not comments on Gen 1:1: m. Chagigah 2:1
forbids expounding the work of creation, and the Hugh and Comestor witnesses are prologues about
what Scripture is for. They are built because **PLAN.md §5's own K2 entry specifies them** —
"Glossa prothemata; Comestor prologue; Hugh Sacr. prologue" — so the plan contemplated prologues
for this crux before the anchor rule was frozen, and the checklist's step 1 is to read that entry.
This is not a general widening of the rule and it is flagged for Wilson in notes/SOURCES-FINDINGS.md;
if he rules the other way, the four are removable without touching the rest. The crux does not
depend on them: BR 1:10 carries m. Chagigah's four forbidden questions verbatim as a comment on the
first letter of Gen 1:1, so the ban is on the daf either way.

Gen 1:1 now carries 34 witnesses from K1 and 13 from K3. Every Latin slice was checked with
scripts/overlap.py by OFFSET; two came back COVERED (Ambrose's Plato inside K4's
`ambrose-hex-1-1-hyle`, Hugh's three principles inside K4's `hugh-sacr-1-1-nihilo`) and are threaded
to rather than rebuilt. Rashi's Gen 1:1 comment is two dibburim in one Sefaria segment: K1 built the
second (`rashi-1-1b`), and the first — R. Isaac on why the Torah does not begin at Exod 12:2 — is
this crux's centre and is built here as `rashi-1-1`.
"""
import json, pathlib
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, APPROVED, thread

CRUX_ID = "why-begin-here"
SHORT = "why begin here?"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

def _flat(x): return x if isinstance(x, str) else " ".join(_flat(i) for i in x)
def _raw(f, lang, idx=None):
    d = json.load(open(RAW / f))
    v = [x for x in d["versions"] if x["language"] == lang][0]
    t = v["text"] if idx is None else v["text"][idx]
    return _flat(t), v["versionTitle"]

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True}

add(id="rashi-1-1", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1075-1105", place="troyes",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית", "en": "In the beginning"},
    original={"lang": "he", "text": hcut(_raw("rashi-gen-1.json", "he", 0)[0], "אמר רבי יצחק",
                                         "ובִרְצוֹנוֹ נְטָלָהּ מֵהֶם וּנְתָנָהּ לָנוּ", "K2 rashi he"),
              "source": "Rashi on Gen 1:1, s.v. בראשית", "license": "pd", "version": "Rosenbaum–Silbermann, 1929–34"},
    english={"text": hcut(_raw("rashi-gen-1.json", "en", 0)[0], "בראשית IN THE BEGINNING — Rabbi Isaac said",
                          "(Yalkut Shimoni on Torah 187)", "K2 rashi en"),
             "translator": "Rosenbaum–Silbermann 1929–34", "license": "silbermann"},
    tradents=["r-yitzchak"],
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["should-have-begun-at-exodus", "claim-on-the-land"],
    notes="The most famous opening sentence in the history of Jewish Bible commentary, and it is an objection to the book it is opening. R. Isaac said: the Torah, which is Israel's law book, ought to have begun at 'this month shall be to you the first of the months' (Exod 12:2), the first commandment given to Israel. Why then does it begin with the creation? Because of Ps 111:6, 'he declared to his people the power of his works, in order to give them the inheritance of the nations' — so that when the peoples of the world say to Israel, you are robbers, for you seized the lands of the seven nations, Israel may answer: the whole earth belongs to the Holy One, blessed be He; he made it and gave it to whom he pleased, and when he willed he took it from them and gave it to us. The chapter, on this account, is not there for its own sake at all. It is title to land, and Rashi puts it at the head of a commentary that will be read for nine hundred years.")

add(id="br-1-2", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "כֹּחַ מַעֲשָׂיו הִגִּיד לְעַמּוֹ", "en": "the power of his deeds he told to his people"},
    original={"lang": "he", "text": _raw("br-1-he.json", "he", 1)[0], "source": "Bereshit Rabbah 1:2 (Vilna numbering)", **_BR_SRC},
    english={"text": _raw("br-1.json", "en", 1)[0], **_BR_EN},
    tradents=["r-yehoshua-of-sikhnin", "r-levi"],
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["claim-on-the-land"],
    notes="Rashi's answer four hundred years before Rashi, and with the objection left out. R. Yehoshua of Sikhnin in the name of R. Levi opens on Ps 111:6 and asks the question directly: what is the reason that the Holy One revealed what was created on the first day and what on the second? Because of the idolaters, so that they should not be able to rebuke Israel and say, you are a nation of robbers. And Israel answers — is your own land not in your hands by robbery? did not the Kaftorim destroy the Avvim and settle in their place (Deut 2:23)? The world and all in it belongs to the Holy One; when he wished he gave it to you, and when he wished he took it from you and gave it to us. Every element of Rashi's comment is here except R. Isaac's opening move, that the book should have started at Exod 12:2 — which is the part that makes it a question about the shape of Scripture rather than about a controversy over land.")

add(id="br-1-5a", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "תֵּאָלַמְנָה שִׂפְתֵי שָׁקֶר", "en": "may they be silenced, those lying lips"},
    original={"lang": "he", "text": hcut(_raw("br-1-he.json", "he", 4)[0], "רַב הוּנָא בְּשֵׁם בַּר קַפָּרָא פָּתַח",
                                         "מָה רַב טוּבְךָ", "K2 br-1-5a he"),
              "source": "Bereshit Rabbah 1:5, first half (Vilna numbering)", **_BR_SRC},
    english={"text": hcut(_raw("br-1.json", "en", 4)[0], "Rav Huna began in the name of bar Kapara",
                          "They will not be included in: “How great is the goodness.”", "K2 br-1-5a en"), **_BR_EN},
    tradents=["r-huna", "bar-kappara", "r-yose-b-chanina"],
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["do-not-expound-it", "honour-of-the-maker"],
    notes="A curse on the expositors, at the head of the commentary that expounds it. Rav Huna in the name of Bar Kappara takes Ps 31:19, 'may they be silenced, those lying lips that speak against the righteous one with arrogance and contempt', and reads every word of it against people doing what Bereshit Rabbah is doing: may they be bound, may they be made mute, may they be silenced; 'against the Righteous One' means him of eternal life; 'harsh words' means matters he concealed from his creatures; 'with arrogance' — is it in order to boast, I am expounding the work of creation? 'and contempt' — is it in order to show contempt for my honour? And R. Yose bar Ḥanina's rule follows: anyone who attains honour through another's degradation has no portion in the world to come, and how much more so where the honour is the Omnipresent's. The section that says this is section five of a commentary that runs to a hundred sections on this book. **Slice note**: K4 built the palace parable that follows as `br-1-5b`; this is the half before it.")

add(id="br-1-10", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "לָמָּה נִבְרָא הָעוֹלָם בְּבֵי\"ת", "en": "why was the world created with a bet?"},
    original={"lang": "he", "text": _raw("br-1-he.json", "he", 9)[0], "source": "Bereshit Rabbah 1:10 (Vilna numbering)", **_BR_SRC},
    english={"text": _raw("br-1.json", "en", 9)[0], **_BR_EN},
    tradents=["r-yona", "r-levi", "bar-kappara", "r-shimon-b-pazi"],
    cruxes=["why-begin-here"], senses=["literal", "spiritual"],
    answers=["do-not-expound-it", "the-bet-is-closed", "beginning-is-blessing"],
    notes="The ban on the four questions derived from the shape of the first letter of the verse, which is as close to the crux as a comment can get. R. Yona in the name of R. Levi: why was the world created with a bet? Because just as the bet is closed on its three sides and open at the front, so you have no permission to ask what is below, what is above, what was before and what is after — but only from the day the world was created and onward. Bar Kappara gets the same fence out of Deut 4:32: from the day they were created you may enquire, but not before that; from one end of the heavens to the other you may investigate, but not beyond. The rest of the section is a sequence of further answers — two worlds, this and the world to come; bet for berakhah rather than alef for arirah, so that the heretics should not be able to say the world was made with a curse — and each of them is a reason for the letter that is also a reason for where the book starts. This is m. Chagigah 2:1's four forbidden matters, made into an exegesis of a single consonant.")

_mc_he, _mc_vt = _raw("m-chag-2-1.json", "he")
add(id="m-chag-2-1", work="mishnah-chagigah", author="mishnah", tradition="rabbinic",
    date=210, date_precision="redaction-200-220", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "וְלֹא בְמַעֲשֵׂה בְרֵאשִׁית בִּשְׁנַיִם", "en": "nor the work of creation before two"},
    original={"lang": "he", "text": _mc_he, "source": "m. Chagigah 2:1", "license": "pd", "version": _mc_vt},
    english={"text": "One does not expound the forbidden sexual relations before three, nor the work of creation before two, nor the Chariot before one — unless he was wise and understood of his own knowledge. Whoever looks at four things, it were fitting for him that he had not come into the world: what is above, what is below, what is before, and what is after. And whoever has no care for the honour of his Maker, it were fitting for him that he had not come into the world.", **APPROVED},
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["do-not-expound-it", "honour-of-the-maker"],
    notes="The rule the whole rabbinic bench on this site is working under, and it is not a comment on Gen 1:1 but a restriction on commenting. The work of creation may not be expounded before two, and the Chariot not before one, unless he is wise and understands of his own knowledge — a rule about audience size, so that what is said cannot become public teaching. Then the four things: what is above, what is below, what is before, what is after; and whoever looks at them, it were fitting he had not come into the world. Those four are what Bereshit Rabbah 1:10 reads out of the closed sides of the letter bet, and they are, item for item, the questions the Manichees put to Augustine and that he answers at length in the first chapters of De Genesi contra Manichaeos. ⚠ **Anchor note**: this is a witness by PLAN.md §5's specification for K2, not by the general anchor rule; see the file docstring. The Sefaria English here is the William Davidson Edition, which is not licensed for this site, so the English is a fresh draft from the Hebrew.")

# ---------------------------------------------------------------- Latin bench
add(id="ambrose-hex-1-1b", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "tamquam testis divini operis ausus est dicere", "en": "as a witness of the divine work he dared to say"},
    original=latin("6958", "Denique non in persuasione humanae sapientiae",
                   "nec vanis abducamur opinionibus.", 14),
    english={"text": "Finally it was not in the persuasion of human wisdom, nor in the counterfeit disputations of philosophy, but in the showing of the Spirit and of power, as a witness of the divine work, that he dared to say: In the beginning God made heaven and earth. Not he, so that the world should come together by a concourse of atoms […]. For a man full of prudence perceived that the divine mind alone contains the substances of things visible and invisible, their origins and their causes — not, as the philosophers dispute, that a stronger interlacing of atoms furnishes the cause of unbroken endurance: but he judged that they were weaving a spider's web who gave such minute and unsubstantial first principles to heaven and earth — principles which, as they were joined by chance, would by chance and at random be dissolved, did they not stand fast in the divine power of their governor. Nor is it without cause that they do not know the governor, who have not known God, by whom all things are ruled and governed. Let us follow him, then, who knows both the author and the governor, and let us not be led away by empty opinions.", **APPROVED},
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["moses-is-a-witness", "against-the-philosophers"],
    notes="The Latin bench's reason for the chapter, and it is a claim about the writer's standing rather than about the chapter's contents. Moses did not speak in the persuasion of human wisdom nor in philosophy's counterfeit disputations but in the showing of the Spirit and of power, and he dared to say 'In the beginning God made heaven and earth' as a witness — testis — of the divine work. Everything Ambrose has said in the preceding column about Plato's three principles and the atomists is cleared away by that one word: a witness does not argue, he reports, and what he reports is what the divine mind alone contains. The spider's web is aimed at Epicurus. Note what the Latin answer does not contain: any suggestion that the chapter should not have been written, or that it is doing something the book is not otherwise for. That question is asked only on the other bench, and there it is asked first.")

add(id="ambrose-hex-1-5", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"}, lemma={"la": "dum opus videtur, praefertur operator", "en": "while the work is seen, the worker is put forward"},
    original=latin("6958", "Est ergo hic mundus divinae specimen operationis",
                   "peritiam ejus ostendunt", 14),
    english={"text": "This world, then, is a specimen of the divine working; because while the work is seen, the worker is put forward. For as of these arts of ours some are active, which consist in the movement of the body or the sound of the voice — the movement or the sound ceased, nothing was left over, nothing remained to those who watched or listened; others are theoretical, which exercise the vigour of the mind; others of such a kind that, the office of working having ceased, the work's own service still appears, as building and weaving, which even when the craftsman is silent show his skill.", **APPROVED},
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["the-work-shows-the-maker"],
    notes="Why creation and not something else: because a made thing goes on saying who made it after the maker has stopped speaking. Ambrose sorts the arts into three — those that leave nothing behind when the movement or the sound stops, those that exercise the mind, and those whose product keeps working when the craftsman is silent, like building and weaving — and puts the world in the third class. The argument is Rom 1:20 turned into a workshop, and it answers the crux from the side of the reader rather than the writer: Scripture begins here because this is where God can be inferred from what is in front of anyone. Set against Rashi's answer, the two benches could hardly be further apart. For Ambrose the chapter is the most natural possible opening; for R. Isaac it is the one that has to be explained away.")

add(id="aug-gnm-1-1", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-390", place="thagaste",
    anchor={"verse": "gen.1.1"}, lemma={"la": "non ornato politoque sermone, sed rebus manifestis", "en": "not with ornate and polished speech, but with plain facts"},
    original={**latin("7303", "Si eligerent Manichaei quos deciperent",
                      "illum autem indocti non intelligunt.", 34),
              "source": "PL 34, col. 173"},  # slice precedes the first <pb>, so latin() computes '?'

    english={"text": "If the Manichees chose whom they deceive, we too would choose the words with which to answer them: but since they pursue both those learned in letters and the unlearned with their error, and while they promise truth try to turn men away from truth, their emptiness must be refuted not with ornate and polished speech but with plain facts. For I was pleased by the judgement of certain truly Christian men who, being themselves educated in liberal letters, when they had read our other books which we published against the Manichees, saw that they were either not understood by the less skilled, or understood with difficulty, and most kindly warned me not to abandon the common manner of speaking, if I meant to drive errors so ruinous out of the minds even of the unlearned. For this usual and simple speech the learned also understand, but that other the unlearned do not understand.", **APPROVED},
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["against-the-heretics", "written-for-the-unlearned"],
    notes="Augustine explaining, before he has expounded a syllable, why this commentary exists and why it is written the way it is — which is the one thing on the Latin bench that answers the crux in the same register as Rashi's opening. The reason is an opponent: the Manichees pursue the learned and the unlearned alike, so the reply cannot be a learned one. And the reason for the style is a piece of received advice, reported with its embarrassment intact — educated friends read his earlier anti-Manichaean books, saw that ordinary readers could not follow them, and told him kindly to stop writing like that. The chapter that follows is then a defence of Gen 1:1 against the question 'in what beginning? and what was God doing before?' — which is m. Chagigah's 'what was before', put by an opponent who has to be answered rather than by a student who has to be stopped.")

add(id="hugh-sacr-prologus", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "materia divinarum Scripturarum omnium sunt opera restaurationis", "en": "the matter of all the divine Scriptures is the works of restoration"},
    original=latin("11082", "CAP. II. Quae sit materia divinarum Scripturarum.",
                   "haec vero non nisi aetatibus sex compleri possunt.", 176, occurrence=1),
    english={"text": "CHAPTER II. What is the matter of the divine Scriptures. The matter of all the divine Scriptures is the works of human restoration. For there are two works in which is contained everything that has been made. The first is the work of foundation. The second is the work of restoration. The work of foundation is that by which it was brought about that the things which were not should be. The work of restoration is that by which it was brought about that the things which had perished should be better. Therefore the work of foundation is the creation of the world with all its elements. The work of restoration is the incarnation of the Word with all its sacraments, whether those which went before from the beginning of the age or those which follow to the end of the world. For the incarnate Word is our King, who came into this world to fight with the devil; and all the saints who were before his coming are as soldiers going before the face of the King, and those who came after and will come to the end of the world are soldiers following their King. And the King himself is in the midst of his army, walking hedged about on this side and that and thronged by his companies. And although in so great a multitude various kinds of arms appear in the sacraments and observances of the peoples going before and following after, yet all are proved to serve one King and to follow one standard, and to pursue one enemy and to be crowned with one victory. In all these the works of restoration are considered; on which the whole intention of the divine Scriptures turns. Worldly or secular writings have for their matter the works of foundation. The divine Scripture has for its matter the works of restoration. Therefore it is rightly believed to be more excellent than all writings, by as much as the matter is worthier and more sublime in which its consideration and treatment is engaged. For the works of restoration are far worthier than the works of foundation; because those were made for service, that they might be under man while he stood; these for salvation, that they might raise him fallen. Therefore those, as some small thing, were completed in six days; but these cannot be completed save in six ages.", **APPROVED},
    cruxes=["why-begin-here"], senses=["literal"],
    answers=["scripture-is-about-restoration", "foundation-is-for-secular-writings"],
    notes="The sharpest Latin answer on this crux, and it is sharp because Hugh gives away more than he means to. The matter of all divine Scripture is the works of restoration; the works of foundation — the creation of the world with all its elements — are the matter of secular writings. That is a clean division and it leaves Genesis 1 on the wrong side of it, which is why the next chapter has to explain how divine Scripture descends through the works of foundation to narrate the works of restoration. Hugh is therefore saying, in the technical vocabulary of a Paris master, exactly what R. Isaac says in Troyes at the head of Rashi's commentary: this chapter is not what the book is for. The two go on to give incompatible reasons — Hugh that Scripture passes through the creation on its way to the Incarnation, Rashi that Israel needs a title to the land — and neither bench ever hears the other's. ⚠ **Anchor note**: a prologue, built by PLAN.md §5's specification for K2; see the file docstring.")

add(id="comestor-hs-prologus", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.1"}, lemma={"la": "historia fundamentum est", "en": "history is the foundation"},
    original=latin("11575", "Imperatoriae majestatis est, in palatio tres habere mansiones",
                   "quid a nobis sit faciendum insinuat. Prima planior, secunda acutior, tertia suavior", 198),
    english={"text": "It belongs to imperial majesty to have three chambers in the palace: the hall of audience or council, in which it decrees laws; the dining-hall, in which it distributes food; the bedchamber, in which it rests. After this manner our Emperor, who commands the winds and the sea, has this world for his hall of audience, where all things are disposed at his nod — whence that word of Isaiah: I fill heaven and earth. According to this he is called Lord: whence, The earth is the Lord's, and the fulness thereof. He has the soul of the just for his bedchamber, because his delights are to rest there and to be with the sons of men: according to this he is called the bridegroom, and each soul the bride. He has holy Scripture for his dining-hall, in which he so makes his own drunk that he renders them sober: whence, We walked in the house of God with consent — being of one mind in holy Scripture. According to this he is called the householder. Of this dining-hall there are three parts: foundation, wall, roof. History is the foundation, of which there are three kinds: annals, calendars, day-books. Allegory is the wall leaning upon it, which figures one deed by another. Tropology is the roof set on the summit, which by what has been done intimates what is to be done by us. The first is plainer, the second sharper, the third sweeter.", **APPROVED},
    cruxes=["why-begin-here"], senses=["allegorical"],
    answers=["history-is-the-foundation"],
    notes="Why a book of Scripture begins with a narrative of events, answered by a builder's metaphor that is also a curriculum. Scripture is the Emperor's dining-hall, and the hall has a foundation, a wall and a roof: history, allegory, tropology — the first plainer, the second sharper, the third sweeter. History is the foundation, so it comes first because nothing can be built before it is laid, and the Historia scholastica is a whole book written on that principle. It is the most institutional answer on the daf: not why God began the book here, but why a master beginning to teach it must begin here. The three kinds of history — annals, calendars, day-books — are the technical vocabulary of a twelfth-century classroom. ⚠ **Anchor note**: a prologue, built by PLAN.md §5's specification for K2; see the file docstring.")

# ---------------------------------------------------------------- threads (K2)
THREADS = [
 E("t-k2-01", "rashi-1-1", "br-1-2", "cites", "Rashi's answer is Bereshit Rabbah 1:2 almost entire — Ps 111:6, 'he declared to his people the power of his works, in order to give them the inheritance of the nations'; the nations calling Israel robbers; and Israel's reply that the whole earth belongs to the Holy One, who gave it and took it and gave it again. What Rashi adds, and what makes it the opening of a commentary rather than a piece of polemic, is R. Isaac's premise: the Torah should have begun at Exod 12:2."),
 E("t-k2-02", "hugh-sacr-prologus", "rashi-1-1", "parallel", "The star thread of this crux, and both benches say it about the book they are expounding. R. Isaac: the Torah is Israel's law book and ought to have begun with the first commandment given to Israel, at Exod 12:2. Hugh: the matter of all divine Scripture is the works of restoration, and the works of foundation are the matter of secular writings. Each has ruled that the first chapter of Genesis is not what its book is for, in Troyes and in Paris within fifty years, and each then supplies a reason external to the chapter — a claim on the land, a descent toward the Incarnation."),
 E("t-k2-03", "m-chag-2-1", "br-1-10", "cites", "Bereshit Rabbah reads the Mishnah's four forbidden matters out of the shape of the first letter of the verse: as the bet is closed on its three sides and open at the front, you have no permission to ask what is below, what is above, what was before and what is after. The list is the Mishnah's, item for item and in the same order; what is new is that it is now a property of the text rather than a rule of the school."),
 E("t-k2-04", "br-1-5a", "m-chag-2-1", "echoes", "The Mishnah restricts the audience and the midrash curses the motive. Rav Huna in the name of Bar Kappara reads Ps 31:19 against those who speak 'with arrogance' — is it in order to boast, I am expounding the work of creation? — and 'with contempt', for the honour of the Maker. The Mishnah's closing clause is the same: whoever has no care for the honour of his Maker, it were fitting he had not come into the world."),
 E("t-k2-05", "br-1-5a", "br-1-10", "echoes", "Two fences in one chapter of the same commentary, five sections apart, and both about the same book they are introducing: a curse on those who expound the work of creation for their own honour, and a letter shaped so that the questions before and behind may not be put. Bereshit Rabbah opens by making the case against itself twice."),
 E("t-k2-06", "aug-gnm-1-1", "m-chag-2-1", "contests", "The identical question and the opposite discipline. The Mishnah: whoever looks at what is above, what is below, what is before, what is after, it were fitting for him that he had not come into the world. Augustine, in the chapter following this one: the Manichees ask 'in what beginning? if God made heaven and earth in some beginning of time, what was he doing before he made heaven and earth?' — and he answers it, at length and in the plainest Latin he can manage. On one bench the question is put by a student who must be stopped; on the other by an opponent who must be answered, and being answered it becomes part of the commentary tradition for good."),
 E("t-k2-07", "aug-gnm-1-1", "br-1-5a", "contests", "Both texts stand at the head of an exposition of Genesis 1 and both are about who should be doing the expounding. Bereshit Rabbah: may they be silenced, may they be made mute — is it in order to boast, I am expounding the work of creation? Augustine: since the Manichees pursue the learned and the unlearned alike, the reply must be made not in ornate and polished speech but in plain facts, and educated friends warned him kindly that his earlier books could not be followed by ordinary readers. One tradition's answer to a wide audience is to restrict the teaching; the other's is to change the prose."),
 E("t-k2-08", "ambrose-hex-1-1b", "rashi-1-1", "contests", "The two benches' reasons for the chapter, and they do not meet at any point. Ambrose: Moses spoke not in the persuasion of human wisdom nor in philosophy's counterfeit disputations but as a witness of the divine work, and therefore dared to say 'in the beginning God made heaven and earth'. R. Isaac: the book should have begun at the first commandment, and begins here so that Israel may answer the charge of robbery. One answers from the writer's authority, the other from the reader's need; neither would recognise the other's question as the question."),
 E("t-k2-09", "ambrose-hex-1-5", "ambrose-hex-1-1b", "echoes", "Two answers a few columns apart and they are the two halves of one: Moses could write it because he was a witness of the divine work, and it is worth writing because a work goes on showing its worker after he has fallen silent, as building and weaving do. The first secures the text, the second secures the subject."),
 E("t-k2-10", "comestor-hs-prologus", "hugh-sacr-prologus", "echoes", "Two Paris prologues a generation apart, and the second answers the difficulty the first creates. Hugh has left the works of foundation to secular writings and must explain how Scripture descends through them; Comestor makes history the foundation of the building and allegory the wall that leans upon it, so that beginning with the creation is not a detour but the first course of masonry. Comestor is Hugh's pupil's pupil and the metaphor is doing structural work."),
 E("t-k2-11", "comestor-hs-prologus", "br-1-5a", "contests", "The most complete opposition on the daf, and neither text knows the other exists. Comestor's Scripture is a dining-hall in which the Emperor makes his own drunk so as to render them sober, with a threefold curriculum built on it and a book to follow. Bereshit Rabbah's fifth section curses those who expound the work of creation for their own honour and reserves the concealed matters to the Righteous One. One tradition institutionalises the exposition; the other keeps warning itself against it — and both then produce the exposition anyway."),
 E("t-k2-12", "hugh-sacr-prologus", "ambrose-hex-1-5", "contests", "Ambrose puts the world in the class of works that keep showing their maker when the maker is silent, which makes the creation the natural first subject of any book about God. Hugh assigns the works of foundation to secular writings and keeps the works of restoration for Scripture, which makes it the least natural. The Latin bench holds both, seven hundred years apart, and Hugh does not mention that anyone had thought otherwise."),
 E("t-k2-13", "br-1-10", "aug-gnm-1-1", "parallel", "Both fence the same question from opposite sides at the head of the same chapter. R. Yona in the name of R. Levi: the bet is closed behind, so you may not ask what was before, only from the day the world was created onward. Augustine's opponents ask precisely what was before, and his answer — that no time could pass before God made time, since none can be the maker of times except one who is before times — is the fence rebuilt as an argument. Bar Kappara reaches for Deut 4:32, 'ask now of the early days that were before you, from the day God created man'; Augustine reaches for Titus 1:2, 'before eternal times'. Each has a verse for the boundary and only one of them will say what lies past it."),
 E("t-k2-14", "rashi-1-1", "m-chag-2-1", "contests", "The first sentence of the most-read Jewish commentary on the Torah asks why the book begins with the work of creation, in a tradition whose Mishnah says the work of creation may not be expounded before two. Rashi does not cite the rule and does not need to break it: his answer removes the chapter from the domain the Mishnah is fencing by making it a matter of public law rather than of hidden things — the peoples of the world say, and Israel answers."),
 E("t-k2-15", "br-1-2", "ambrose-hex-1-5", "parallel", "Both make the creation account public evidence, and for opposite audiences. R. Yehoshua of Sikhnin in R. Levi's name: God revealed what was made on each day because of the idolaters, so that Israel could answer the charge of robbery. Ambrose: the world is a specimen of the divine working, so that while the work is seen the worker is put forward, as a building shows its craftsman when he is silent. The rabbinic bench's evidence is a text and its jury is the nations; the Latin bench's evidence is the world and its jury is anyone with eyes."),
 E("t-k2-x1", "ambrose-hex-1-1b", "ambrose-hex-1-1-hyle", "echoes", "Phase 4. Two halves of Ambrose's first chapter, split between two cruxes. The earlier passage sets out what the philosophers held — Plato's three principles, uncreated and coeternal with God, and the atomists' concourse; this one clears them away in a sentence by making Moses a witness rather than a disputant. The refutation is unintelligible without the doxography that precedes it."),
 E("t-k2-x2", "hugh-sacr-prologus", "hugh-sacr-1-1-nihilo", "echoes", "Phase 4. Hugh sets out in his prologue that the matter of secular writings is the works of foundation, and then, when he reaches the works of foundation himself, opens by refuting the philosophers of the nations who posited three first principles without a beginning — workman, matter and form. The prologue explains why that refutation has to come first: he is on ground he has just assigned to somebody else."),
]

FINDING = (
 "This is the crux where each tradition's reason for having a commentary is exposed, and the two "
 "reasons turn out to be the same shape and opposite in content. Rashi opens the most-read Jewish "
 "commentary on the Torah with an objection to the book: R. Isaac said the Torah, which is Israel's "
 "law book, ought to have begun at 'this month shall be to you the first of the months', the first "
 "commandment given to Israel — and it begins with the creation only so that when the nations call "
 "Israel robbers, Israel may answer that the earth is the Lord's and he gave it to whom he pleased. "
 "Hugh of St Victor, in Paris within fifty years of Troyes, opens his own summa with the same "
 "verdict in scholastic terms: the matter of all divine Scripture is the works of restoration, and "
 "the works of foundation — the creation of the world with all its elements — are the matter of "
 "secular writings. Both have ruled that Genesis 1 is not what its book is for; both then supply a "
 "reason from outside the chapter, and the reasons have nothing to do with each other. Hugh needs a "
 "whole further chapter to explain how Scripture descends through the works of foundation on its way "
 "to the Incarnation, and Comestor a generation later repairs the difficulty with a builder's "
 "metaphor — history is the foundation, allegory the wall leaning on it, tropology the roof — so "
 "that starting here is the first course of masonry rather than a detour.\n\n"
 "What the Latin bench never does is ask whether the chapter should be expounded at all, and what "
 "the rabbinic bench never stops doing is asking exactly that. The Mishnah rules that the work of "
 "creation may not be expounded before two, and that whoever looks at four things — what is above, "
 "what is below, what is before, what is after — it were fitting for him that he had not come into "
 "the world. Bereshit Rabbah puts the same four questions into the shape of the first letter of the "
 "first word: the bet is closed on three sides and open at the front, so you have permission to ask "
 "only from the day the world was created and onward. And five sections earlier the same commentary "
 "curses the people doing what it is doing — may they be silenced, those lying lips — 'with "
 "arrogance', is it in order to boast, I am expounding the work of creation? A commentary that makes "
 "the case against itself twice in its first chapter has no counterpart on the Latin side at all.\n\n"
 "The reason it has none is visible in Augustine, and it is not that the Latin bench is less "
 "reverent. In the first chapter of De Genesi contra Manichaeos he explains why the book exists and "
 "why it is written the way it is: the Manichees pursue the learned and the unlearned alike, so they "
 "must be refuted 'not with ornate and polished speech but with plain facts' — educated friends had "
 "read his earlier books and warned him kindly that ordinary readers could not follow them. And in "
 "the next chapter the Manichees put their question: in what beginning, and what was God doing "
 "before he made heaven and earth? That is the Mishnah's 'what is before', asked by an opponent "
 "instead of a student. On one bench the question is put by someone who must be stopped, and the "
 "tradition builds a fence; on the other it is put by someone who must be answered, and the answer "
 "becomes the commentary. Ambrose settles the matter from the other end — Moses spoke not in the "
 "persuasion of human wisdom but as a witness, testis, of the divine work, and the world is a "
 "specimen of the divine working, because while the work is seen the worker is put forward, as a "
 "building shows its craftsman when the craftsman is silent. Beginning here is, for the Latin bench, "
 "the most natural thing a book about God could do. For R. Isaac it is the one thing that has to be "
 "explained away."
)

# ---------------------------------------------------------------- new persons / places / answers
PERSONS = {
 "mishnah": {"name": "the Mishnah", "he": "מִשְׁנָה", "dates": "redacted c. 200–220", "tradition": "rabbinic", "role": "work"},
 "r-yehoshua-of-sikhnin": {"name": "R. Yehoshua of Sikhnin", "dates": "fl. c. 330", "tradition": "rabbinic", "role": "tradent"},
 "r-yona": {"name": "R. Yona", "dates": "fl. c. 350", "tradition": "rabbinic", "role": "tradent"},
 "r-shimon-b-pazi": {"name": "R. Shimon ben Pazi", "dates": "fl. c. 280", "tradition": "rabbinic", "role": "tradent"},
}

PLACES = {}

ANSWERS = {
 "should-have-begun-at-exodus": {"label": "It should have begun at Exodus 12:2", "gloss": "The Torah is Israel's law book and ought to have opened with the first commandment given to Israel; the creation account has to be accounted for (R. Isaac, in Rashi)."},
 "claim-on-the-land": {"label": "Title to the land", "gloss": "'He declared to his people the power of his works, to give them the inheritance of the nations' (Ps 111:6) — so that Israel may answer the charge of robbery (Bereshit Rabbah 1:2; Rashi)."},
 "do-not-expound-it": {"label": "It may not be expounded", "gloss": "Not before two, and not the four questions — what is above, what is below, what is before, what is after (m. Chagigah 2:1; Bereshit Rabbah 1:5 and 1:10)."},
 "honour-of-the-maker": {"label": "For the honour of the Maker", "gloss": "Whoever has no care for the honour of his Maker, it were fitting he had not come into the world; and the concealed matters are not to be published for the expositor's own glory (m. Chagigah 2:1; Rav Huna in the name of Bar Kappara)."},
 "the-bet-is-closed": {"label": "The bet is closed behind", "gloss": "The world was made with a bet, closed on three sides and open in front: you may ask only from the day of creation onward (R. Yona in the name of R. Levi)."},
 "beginning-is-blessing": {"label": "Bet for blessing, not alef for curse", "gloss": "Made with the letter of berakhah rather than of arirah, so that the heretics could not say the world was created with a curse (Bereshit Rabbah 1:10)."},
 "moses-is-a-witness": {"label": "Moses wrote as a witness", "gloss": "Not in the persuasion of human wisdom nor in the counterfeit disputations of philosophy, but in the showing of the Spirit and of power, as a witness of the divine work (Ambrose)."},
 "against-the-philosophers": {"label": "Against the philosophers", "gloss": "Plato's three principles and the atomists' concourse are a spider's web; the divine mind alone contains the origins and causes of things (Ambrose)."},
 "against-the-heretics": {"label": "Because the heretics attack it", "gloss": "The Manichees mock the Old Testament before the unlearned, so the first book must be defended, and defended plainly (Augustine)."},
 "written-for-the-unlearned": {"label": "In plain speech, for the unlearned", "gloss": "Not with ornate and polished speech but with plain facts — the usual and simple speech the learned also understand (Augustine)."},
 "the-work-shows-the-maker": {"label": "The work shows the worker", "gloss": "The world is a specimen of the divine working: like building and weaving, it shows the craftsman's skill even when the craftsman is silent (Ambrose)."},
 "scripture-is-about-restoration": {"label": "Scripture is about restoration", "gloss": "The matter of all divine Scripture is the works of human restoration, completed not in six days but in six ages (Hugh of St Victor)."},
 "foundation-is-for-secular-writings": {"label": "Foundation belongs to secular writings", "gloss": "The works of foundation are the matter of worldly writings; divine Scripture only descends through them on its way to the Incarnation (Hugh of St Victor)."},
 "history-is-the-foundation": {"label": "History is the foundation", "gloss": "Scripture is a hall with foundation, wall and roof — history, allegory, tropology — and nothing can be built before the foundation is laid (Comestor)."},
}

LICENSES = {}
