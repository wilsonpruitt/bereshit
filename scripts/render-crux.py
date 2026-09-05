#!/usr/bin/env python3
"""Render one crux page as a self-contained HTML prototype (the Astro build will replace this).
Usage: render-crux.py <crux-id>  → out/crux-<id>.html"""
import json, pathlib, sys, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
crux_id = sys.argv[1] if len(sys.argv) > 1 else "ruach-hovering"
cruxes = {c["id"]: c for c in json.load(open(ROOT / "data" / "cruxes.json"))}
crux = cruxes[crux_id]
threads = [t for t in json.load(open(ROOT / "data" / "threads.json")) if t["crux"] == crux_id]
persons = json.load(open(ROOT / "data" / "persons.json"))
places = json.load(open(ROOT / "data" / "places.json"))
scripture = json.load(open(ROOT / "data" / "scripture" / "gen-1.json"))
W = {}
for wid in crux["witnesses"]:
    W[wid] = json.load(open(ROOT / "data" / "witnesses" / f"{wid}.json"))
order = sorted(W.values(), key=lambda w: (w["date"], w["id"]))
verse = next(v for v in scripture["verses"] if v["ref"] == crux["verse"])

def esc(s): return html.escape(str(s), quote=True)
def year(d):
    return f"{-d} BCE" if d < 0 else f"{d}"
TRAD = {"latin": "Latin", "rabbinic": "Rabbinic", "greek-jewish": "Greek-Jewish"}
LANGDIR = {"he": "rtl", "arc": "rtl"}
LANGCLS = {"he": "heb", "arc": "heb", "el": "grk", "la": "lat"}

cards = []
prev = None
for w in order:
    p = persons.get(w["author"], {"name": w["author"]})
    pl = places.get(w["place"], {"name": w["place"]})
    gap = ""
    if prev is not None and w["date"] - prev >= 120:
        gap = f'<div class="gap" aria-hidden="true"><span>{w["date"] - prev} years</span></div>'
    prev = w["date"]
    o = w["original"]; e = w["english"]
    slot = w.get("status") == "slot"
    draft = e.get("translator") == "claude-draft"
    lem = w.get("lemma", {})
    lem_html = " ".join(
        f'<span class="lem {LANGCLS.get(k,"")}" dir="{LANGDIR.get(k,"ltr")}">{esc(v)}</span>'
        for k, v in lem.items() if k != "en")
    prec = w.get("date_precision", "")
    prec_txt = {"circa": "c."}.get(prec, "")
    if prec.startswith("range-") or prec.startswith("compilation-") or prec.startswith("redaction-"):
        kind, _, rng = prec.partition("-")
        prec_txt = f"{'' if kind=='range' else kind + ' '}{rng.replace('-', '–')}"
        datelabel = prec_txt
    else:
        datelabel = f"{prec_txt} {year(w['date'])}".strip()
    edges_out = [t for t in threads if t["from"] == w["id"]]
    edges_in = [t for t in threads if t["to"] == w["id"]]
    def chip(t, other, arrow):
        ow = W.get(other); nm = persons.get(ow["author"], {}).get("name", other) if ow else other
        return f'<button class="chip {t["type"]}" data-thread="{t["id"]}" title="{esc(t["evidence"])}">{arrow} {esc(t["type"])} · {esc(nm)}</button>'
    chips = "".join(chip(t, t["to"], "→") for t in edges_out) + "".join(chip(t, t["from"], "←") for t in edges_in)
    trad = w["tradition"]
    cards.append(f'''
<article class="w {trad}{' slot' if slot else ''}" id="{w["id"]}" data-date="{w["date"]}">
  <div class="axis"><span class="yr">{esc(datelabel)}</span></div>
  <div class="node" aria-hidden="true"></div>
  <div class="body">
    <header>
      <span class="trad">{TRAD.get(trad, trad)}</span>
      <span class="who">{esc(p.get("name"))}</span>
      <span class="what">{esc(w["work"])}</span>
      <span class="where">{esc(pl["name"])}</span>
    </header>
    <p class="lemma">{lem_html}</p>
    <div class="en{' draft' if draft else ''}">{esc(e["text"])}</div>
    <details class="orig">
      <summary>{'Hebrew' if o.get('lang') in ('he','arc') else 'Greek' if o.get('lang')=='el' else 'Latin'} · {esc(o.get("source",""))}</summary>
      <div class="{LANGCLS.get(o.get('lang'),'')}" dir="{LANGDIR.get(o.get('lang'),'ltr')}">{esc(o["text"])}</div>
    </details>
    <p class="note">{esc(w.get("notes",""))}</p>
    <footer>
      <span class="cred">{'Draft English (Claude), awaiting Wilson' if draft else 'English: ' + esc(e.get("translator","")) + ' · ' + esc(e.get("license","")).upper()}</span>
      <span class="chips">{chips}</span>
    </footer>
  </div>
</article>''')
    gap and cards.insert(len(cards) - 1, gap)

people = sorted({w["author"] for w in order} | {t for w in order for t in w.get("tradents", [])})
rail_people = "".join(f'<li><span>{esc(persons.get(a, {}).get("name", a))}</span><small>{esc(persons.get(a, {}).get("dates", ""))}</small></li>' for a in people)
rail_places = "".join(f'<li>{esc(places.get(pid, {}).get("name", pid))}</li>' for pid in sorted({w["place"] for w in order}))
thread_json = json.dumps(threads, ensure_ascii=False)

q = crux["question"]
page = f'''<title>Ruach Merahefet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&family=Frank+Ruhl+Libre:wght@400;500&display=swap">
<style>
:root {{
  --bg:#F3F4F1; --ink:#1A1E21; --mute:#5B615E; --rule:#CBCFC9; --card:#FAFAF7;
  --lat:#A0392A; --rab:#2B4A9C; --grk:#67762B; --hi:#FFF3C4;
  --edge-cites:#1A1E21; --edge-echo:#6B716D; --edge-contest:#A0392A; --edge-par:#A7ACA7; --edge-trans:#2B4A9C;
  --serif:"EB Garamond",Garamond,"Times New Roman",serif; --sans:Inter,system-ui,sans-serif; --heb:"Frank Ruhl Libre","Times New Roman",serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#151819; --ink:#E7E5DD; --mute:#9AA09B; --rule:#33393B; --card:#1C2022;
  --lat:#E28A73; --rab:#8EA6EC; --grk:#B9C66A; --hi:#3A3520;
  --edge-cites:#E7E5DD; --edge-echo:#9AA09B; --edge-contest:#E28A73; --edge-par:#5A605C; --edge-trans:#8EA6EC; }} }}
:root[data-theme="dark"] {{
  --bg:#151819; --ink:#E7E5DD; --mute:#9AA09B; --rule:#33393B; --card:#1C2022;
  --lat:#E28A73; --rab:#8EA6EC; --grk:#B9C66A; --hi:#3A3520;
  --edge-cites:#E7E5DD; --edge-echo:#9AA09B; --edge-contest:#E28A73; --edge-par:#5A605C; --edge-trans:#8EA6EC; }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--ink); font-family:var(--serif); font-size:17px; line-height:1.5 }}
.wrap {{ max-width:1180px; margin:0 auto; padding:40px 24px 96px }}
.eyebrow {{ font:500 12px/1 var(--sans); letter-spacing:.12em; text-transform:uppercase; color:var(--mute) }}
h1 {{ font:500 40px/1.15 var(--serif); margin:12px 0 4px; text-wrap:balance; max-width:22ch }}
.q {{ display:grid; gap:6px; margin:18px 0 0; max-width:64ch }}
.q .la {{ font-style:italic; font-size:22px }}
.q .heb {{ font-family:var(--heb); font-size:22px; direction:rtl; text-align:right; max-width:36ch }}
.q .en {{ font-size:19px; color:var(--mute) }}
.verse {{ margin:28px 0 0; padding:18px 0; border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); display:grid; grid-template-columns:1fr 1fr 1fr; gap:24px }}
.verse > div {{ display:grid; gap:6px; align-content:start }}
.verse .heb {{ font-family:var(--heb); font-size:21px; direction:rtl; text-align:right; line-height:1.7 }}
.verse .lat {{ font-style:italic; font-size:19px }}
.verse .web {{ font-size:18px }}
.verse mark {{ background:var(--hi); color:inherit; padding:0 .15em }}
.summary {{ max-width:66ch; font-size:18px; margin:24px 0 0 }}
.finding {{ max-width:66ch; margin:12px 0 0; padding-left:14px; border-left:2px solid var(--lat); color:var(--ink) }}
.legend {{ display:flex; flex-wrap:wrap; gap:18px; margin:22px 0 0; font:13px var(--sans); color:var(--mute); align-items:center }}
.legend i {{ display:inline-block; width:34px; height:0; border-top:2px solid var(--edge-cites); vertical-align:middle; margin-right:8px }}
.legend .echo i {{ border-top-style:dashed; border-color:var(--edge-echo) }}
.legend .contest i {{ border-color:var(--edge-contest) }}
.legend .par i {{ border-top-style:dotted; border-color:var(--edge-par); border-top-width:3px }}
.legend .trans i {{ border-color:var(--edge-trans) }}
.legend b {{ font-weight:600; color:var(--ink) }}
.layout {{ display:grid; grid-template-columns:minmax(0,1fr) 220px; gap:40px; margin-top:36px; align-items:start }}
.stream {{ position:relative; display:grid; grid-template-columns:88px 56px minmax(0,1fr) }}
.stream svg {{ position:absolute; left:88px; top:0; width:56px; height:100%; overflow:visible; pointer-events:none }}
.stream svg path {{ fill:none; stroke-width:1.5; pointer-events:stroke; transition:stroke-width .15s }}
.stream svg path.cites {{ stroke:var(--edge-cites) }}
.stream svg path.echoes {{ stroke:var(--edge-echo); stroke-dasharray:6 4 }}
.stream svg path.contests {{ stroke:var(--edge-contest) }}
.stream svg path.parallel {{ stroke:var(--edge-par); stroke-dasharray:2 4; stroke-width:2 }}
.stream svg path.transmits {{ stroke:var(--edge-trans) }}
.stream svg path.on {{ stroke-width:3.5 }}
.w {{ display:contents }}
.w .axis {{ grid-column:1; padding:22px 12px 0 0; text-align:right; font:500 13px var(--sans); color:var(--mute); font-variant-numeric:tabular-nums; border-top:1px solid var(--rule) }}
.w .node {{ grid-column:2; position:relative; border-top:1px solid var(--rule) }}
.w .node::after {{ content:""; position:absolute; left:50%; top:24px; width:9px; height:9px; margin-left:-4.5px; border-radius:50%; background:var(--bg); border:2px solid var(--ink) }}
.w.latin .node::after {{ border-color:var(--lat) }} .w.rabbinic .node::after {{ border-color:var(--rab) }} .w.greek-jewish .node::after {{ border-color:var(--grk) }}
.w .body {{ grid-column:3; padding:18px 0 26px; border-top:1px solid var(--rule); max-width:72ch; min-width:0 }}
.w.hot .body {{ background:var(--card); box-shadow:0 0 0 12px var(--card) }}
.w header {{ display:flex; flex-wrap:wrap; gap:0 14px; font:500 12.5px/1.6 var(--sans); color:var(--mute); align-items:baseline }}
.w .trad {{ letter-spacing:.1em; text-transform:uppercase; font-weight:600 }}
.w.latin .trad {{ color:var(--lat) }} .w.rabbinic .trad {{ color:var(--rab) }} .w.greek-jewish .trad {{ color:var(--grk) }}
.w .who {{ color:var(--ink); font-size:14px; font-weight:600 }}
.w .lemma {{ margin:8px 0 6px; font-size:19px; line-height:1.5 }}
.lem.lat {{ font-style:italic }} .lem.heb {{ font-family:var(--heb); font-size:20px; unicode-bidi:isolate }} .lem.grk {{ font-style:italic }}
.w .en {{ font-size:17.5px }}
.w .en.draft::before {{ content:"draft"; float:right; font:500 10.5px var(--sans); letter-spacing:.1em; text-transform:uppercase; color:var(--mute); border:1px solid var(--rule); padding:2px 6px; margin:4px 0 0 12px }}
.orig {{ margin:10px 0 0 }}
.orig summary {{ cursor:pointer; font:500 12.5px var(--sans); color:var(--mute); list-style:none; display:inline-flex; gap:6px; align-items:center }}
.orig summary::before {{ content:"+"; font-weight:600; width:1em; display:inline-block }}
.orig[open] summary::before {{ content:"–" }}
.orig > div {{ margin-top:8px; padding:10px 14px; background:var(--card); border-left:1px solid var(--rule); font-size:16.5px; line-height:1.55 }}
.orig .lat {{ font-style:italic }} .orig .heb {{ font-family:var(--heb); font-size:19px; line-height:1.8 }}
.w .note {{ margin:12px 0 0; font-size:15.5px; color:var(--mute); max-width:64ch }}
.w footer {{ margin-top:12px; display:flex; flex-wrap:wrap; gap:8px 12px; align-items:center; font:12px var(--sans); color:var(--mute) }}
.chips {{ display:flex; flex-wrap:wrap; gap:6px }}
.chip {{ font:500 11.5px var(--sans); color:var(--ink); background:none; border:1px solid var(--rule); border-radius:2px; padding:3px 8px; cursor:pointer }}
.chip.cites {{ border-color:var(--ink) }} .chip.contests {{ border-color:var(--edge-contest); color:var(--edge-contest) }} .chip.parallel {{ border-style:dotted }} .chip.echoes {{ border-style:dashed }} .chip.transmits {{ border-color:var(--edge-trans) }}
.chip:focus-visible, .orig summary:focus-visible {{ outline:2px solid var(--rab); outline-offset:2px }}
.w.slot .body {{ opacity:.55 }} .w.slot .en {{ font-style:italic }}
.gap {{ grid-column:1 / 4; display:grid; grid-template-columns:88px 56px 1fr; align-items:center; height:34px }}
.gap span {{ grid-column:2; justify-self:center; font:11px var(--sans); color:var(--mute); background:var(--bg); padding:2px 4px; letter-spacing:.06em; white-space:nowrap }}
.rail {{ position:sticky; top:24px; display:grid; gap:26px; font-family:var(--sans); font-size:13px }}
.rail h3 {{ margin:0 0 8px; font:600 11px var(--sans); letter-spacing:.12em; text-transform:uppercase; color:var(--mute) }}
.rail ul {{ list-style:none; margin:0; padding:0; display:grid; gap:4px }}
.rail li {{ display:flex; justify-content:space-between; gap:8px; border-bottom:1px solid var(--rule); padding:3px 0 }}
.rail li small {{ color:var(--mute); font-variant-numeric:tabular-nums; white-space:nowrap }}
.rail .ev {{ font-family:var(--serif); font-size:15px; line-height:1.45; min-height:4lh; color:var(--ink); border-top:2px solid var(--ink); padding-top:8px }}
.rail .ev b {{ font:600 11px var(--sans); letter-spacing:.1em; text-transform:uppercase; color:var(--mute); display:block; margin-bottom:4px }}
.colophon {{ margin-top:56px; padding-top:18px; border-top:1px solid var(--rule); font:13px/1.6 var(--sans); color:var(--mute); max-width:80ch }}
@media (max-width: 900px) {{
  .layout {{ grid-template-columns:1fr }} .rail {{ position:static }} .verse {{ grid-template-columns:1fr }}
  .stream {{ grid-template-columns:64px 32px minmax(0,1fr) }} .stream svg {{ left:64px; width:32px }} .gap {{ grid-template-columns:64px 32px 1fr }}
}}
@media (prefers-reduced-motion: reduce) {{ .stream svg path {{ transition:none }} }}
</style>
<div class="wrap">
  <div class="eyebrow">Bereshit / In Principio · Crux {crux["verse"].replace("gen.", "Genesis ").replace(".", ":")} · K7</div>
  <h1>{esc(q["en"])}</h1>
  <div class="q">
    <div class="la">{esc(q["la"])}</div>
    <div class="heb">{esc(q["he"])}</div>
  </div>
  <div class="verse">
    <div><span class="eyebrow">Masoretic</span><div class="heb">{esc(verse["he"]["text"]).replace(esc("וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת"), "<mark>" + esc("וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת") + "</mark>")}</div></div>
    <div><span class="eyebrow">Vulgate</span><div class="lat">{esc(verse["la"]["text"]).replace("Spiritus Dei ferebatur", "<mark>Spiritus Dei ferebatur</mark>")}</div></div>
    <div><span class="eyebrow">WEB</span><div class="web">{esc(verse["en"]["text"]).replace("God’s Spirit was hovering", "<mark>God’s Spirit was hovering</mark>")}</div></div>
  </div>
  <p class="summary">{esc(crux["summary"])}</p>
  <p class="finding">{esc(crux.get("finding", ""))}</p>
  <div class="legend">
    <span><i></i><b>cites</b> named or verbatim</span>
    <span class="echo"><i></i><b>echoes</b> wording or image, argued</span>
    <span class="contest"><i></i><b>contests</b></span>
    <span class="par"><i></i><b>parallel</b> same move, no known contact</span>
    <span class="trans"><i></i><b>transmits</b> translation</span>
    <span>· {len(order)} witnesses, {len(threads)} threads · hover a line or chip for its evidence</span>
  </div>
  <div class="layout">
    <section class="stream" id="stream">
      <svg id="edges" aria-hidden="true"></svg>
      {"".join(cards)}
    </section>
    <aside class="rail">
      <div class="ev" id="ev"><b>Evidence</b>Hover or focus a thread to read why the edge exists.</div>
      <div><h3>Persons</h3><ul>{rail_people}</ul></div>
      <div><h3>Places</h3><ul>{rail_places}</ul></div>
    </aside>
  </div>
  <div class="colophon">
    Latin from the Patrologia Latina (public domain), located with the Corpus Corporum TEI and cited by PL volume and column. Hebrew and Aramaic from Sefaria: Wikisource Talmud Bavli (CC BY-SA), Bereshit Rabbah, Rashi (Silbermann, PD), Targums. English: Sefaria Midrash Rabbah 2022 (CC BY, attribution to be pasted), Silbermann (PD), Etheridge (PD), Brenton (PD); all other English is a fresh draft awaiting Wilson Pruitt's revision. The Glossa ordinaria slot awaits Wilson's edition (migne.app/glossa). No CC BY-NC text is embedded.
  </div>
</div>
<script>
(function(){{
  const T = {thread_json};
  const svg = document.getElementById('edges'), stream = document.getElementById('stream'), ev = document.getElementById('ev');
  const byId = id => document.getElementById(id);
  function draw(){{
    const sb = stream.getBoundingClientRect(); svg.innerHTML='';
    const W = svg.getBoundingClientRect().width || 56;
    const ys = {{}};
    T.forEach((t,i) => {{
      const a = byId(t.from), b = byId(t.to); if(!a||!b) return;
      const na = a.querySelector('.node'), nb = b.querySelector('.node');
      const ya = na.getBoundingClientRect().top - sb.top + 28.5, yb = nb.getBoundingClientRect().top - sb.top + 28.5;
      const x = W/2, bulge = Math.min(40, 10 + Math.abs(ya-yb)/40) * (i % 2 ? -1 : -1);
      const p = document.createElementNS('http://www.w3.org/2000/svg','path');
      p.setAttribute('d', `M ${{x}} ${{ya}} C ${{x+bulge}} ${{ya}}, ${{x+bulge}} ${{yb}}, ${{x}} ${{yb}}`);
      p.setAttribute('class', t.type); p.dataset.thread = t.id;
      p.addEventListener('mouseenter', ()=>hi(t.id,true)); p.addEventListener('mouseleave', ()=>hi(t.id,false));
      svg.appendChild(p);
    }});
  }}
  function hi(id,on){{
    const t = T.find(x=>x.id===id); if(!t) return;
    svg.querySelectorAll('path').forEach(p=>p.classList.toggle('on', on && p.dataset.thread===id));
    [t.from,t.to].forEach(w=>{{ const el=byId(w); el && el.classList.toggle('hot', on); }});
    if(on){{ const f=byId(t.from), g=byId(t.to);
      const nm = el => el ? el.querySelector('.who').textContent : '?';
      ev.innerHTML = '<b>'+t.type+' · '+nm(f)+' → '+nm(g)+'</b>'+t.evidence.replace(/</g,'&lt;'); }}
  }}
  document.querySelectorAll('.chip').forEach(c=>{{
    const id=c.dataset.thread;
    c.addEventListener('mouseenter',()=>hi(id,true)); c.addEventListener('mouseleave',()=>hi(id,false));
    c.addEventListener('focus',()=>hi(id,true)); c.addEventListener('blur',()=>hi(id,false));
    c.addEventListener('click',()=>{{ const t=T.find(x=>x.id===id); const other = c.textContent.startsWith('→')? t.to : t.from; const el=byId(other); el && el.querySelector('.body').scrollIntoView({{behavior:'smooth',block:'center'}}); }});
  }});
  draw();
  document.querySelectorAll('details').forEach(d=>d.addEventListener('toggle', draw));
  window.addEventListener('resize', draw);
  if (document.fonts) document.fonts.ready.then(draw);
}})();
</script>
'''
out = ROOT / "out"; out.mkdir(exist_ok=True)
(out / f"crux-{crux_id}.html").write_text(page)
print(f"wrote out/crux-{crux_id}.html  ({len(order)} witnesses, {len(threads)} threads)")
