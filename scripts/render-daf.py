#!/usr/bin/env python3
"""Version C: the crux as a daf. The verse sits in the middle; the rabbinic bench runs down the right
column, the patristic Latin down the left, the Carolingian and twelfth-century Latin along the foot.
Each note opens on its lemma (dibbur ha-matchil). Hover or focus a note to read it whole and to see
its threads drawn. Usage: render-daf.py <crux-id> — with no crux-id, renders every crux whose
data/cruxes.json status is "built" and (re)writes out/index.html listing them."""
import json, pathlib, sys, html

ROOT = pathlib.Path(__file__).resolve().parent.parent

if len(sys.argv) <= 1:
    import subprocess
    from indexpage import write_index
    built = [c["id"] for c in json.load(open(ROOT / "data" / "cruxes.json")) if c.get("status") == "built"]
    for cid in built:
        subprocess.run([sys.executable, __file__, cid], check=True)
    write_index(ROOT)
    sys.exit(0)

crux_id = sys.argv[1]
crux = {c["id"]: c for c in json.load(open(ROOT / "data" / "cruxes.json"))}[crux_id]
threads = [t for t in json.load(open(ROOT / "data" / "threads.json")) if t["crux"] == crux_id]
persons = json.load(open(ROOT / "data" / "persons.json"))
places = json.load(open(ROOT / "data" / "places.json"))
answers = json.load(open(ROOT / "data" / "answers.json"))
scripture = json.load(open(ROOT / "data" / "scripture" / "gen-1.json"))
verse = next(v for v in scripture["verses"] if v["ref"] == crux["verse"])
esc = lambda s: html.escape(str(s or ""), quote=True)

W = {}
for wid in crux["witnesses"]:
    w = json.load(open(ROOT / "data" / "witnesses" / f"{wid}.json"))
    prec = w.get("date_precision", "")
    if "-" in prec and prec.split("-", 1)[1][0].isdigit():
        kind, rng = prec.split("-", 1); w["datelabel"] = ("" if kind == "range" else kind + " ") + rng.replace("-", "–")
    else:
        w["datelabel"] = ("c. " if prec == "circa" else "") + (f"{-w['date']} BCE" if w["date"] < 0 else str(w["date"]))
    W[wid] = w

# ------------------------------------------------------------ regions of the page
def region(pred): return sorted([w for w in W.values() if pred(w)], key=lambda w: (w["date"], w["id"]))
center_tr = region(lambda w: w["work"] in ("lxx", "vulgate"))
glossa = [w for w in W.values() if w["work"] == "glossa"]
rab = region(lambda w: w["tradition"] == "rabbinic")
lat_early = region(lambda w: w["tradition"] == "latin" and w["work"] not in ("vulgate", "glossa") and w["date"] <= 750)
lat_late = region(lambda w: w["tradition"] == "latin" and w["work"] not in ("vulgate", "glossa") and w["date"] > 750)

def excerpt(s, n=170):
    s = s.strip()
    if len(s) <= n: return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",;:.") + " …"

def snippet(w):
    p = persons.get(w["author"], {}); pl = places.get(w["place"], {})
    lem = w.get("lemma", {})
    dh = lem.get("he") or lem.get("arc") or lem.get("la") or lem.get("el") or ""
    dh_lang = "he" if (lem.get("he") or lem.get("arc")) else ("el" if lem.get("el") else "la")
    slot = w.get("status") == "slot"
    draft = w["english"].get("translator") == "claude-draft"
    o = w["original"]
    ocls = "heb" if o.get("lang") in ("he", "arc") else "grk" if o.get("lang") == "el" else "lat"
    return f'''<div class="sn {w["tradition"]}{" slot" if slot else ""}" id="{w["id"]}" tabindex="0" role="button" aria-expanded="false">
  <span class="sig">{esc(p.get("name", w["author"]))} · {esc(w["datelabel"])}</span>
  <b class="dh {dh_lang}" dir="{'rtl' if dh_lang=='he' else 'ltr'}">{esc(dh)}</b> <span class="ex">{esc(excerpt(w["english"]["text"]))}</span>
  <template>
    <p class="eyebrow">{esc(w["tradition"].replace("-", " "))} · {esc(w["datelabel"])} · {esc(pl.get("name", w["place"]))}</p>
    <h3>{esc(p.get("name", w["author"]))} <small>{esc(o.get("source", ""))}</small></h3>
    <p class="full">{esc(w["english"]["text"]).replace(chr(10)+chr(10), "</p><p class=\"full\">")}</p>
    <details><summary>{'Hebrew / Aramaic' if ocls=='heb' else 'Greek' if ocls=='grk' else 'Latin'}</summary><div class="orig {ocls}" dir="{'rtl' if ocls=='heb' else 'ltr'}">{esc(o["text"]).replace(chr(10)+chr(10), "<br><br>")}</div></details>
    <p class="note">{esc(w.get("notes", ""))}</p>
    <p class="ans">{" ".join(f"<span>{esc(answers[a]['label'])}</span>" for a in w.get("answers", []))}</p>
    <p class="cred">{"Draft English (Claude), awaiting Wilson" if draft else "English: " + esc(w["english"].get("translator", ""))}</p>
  </template>
</div>'''

def block(ws): return "\n".join(snippet(w) for w in ws)
q = crux["question"]
tj = json.dumps([{"id": t["id"], "from": t["from"], "to": t["to"], "type": t["type"], "evidence": t["evidence"]} for t in threads], ensure_ascii=False)
names = json.dumps({wid: persons.get(w["author"], {}).get("name", w["author"]) for wid, w in W.items()}, ensure_ascii=False)

page = f'''<title>Ruach Merahefet Daf</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&family=Frank+Ruhl+Libre:wght@400;500;700&display=swap">
<style>
:root{{--bg:#F3F4F1;--paper:#F8F8F4;--ink:#1A1E21;--mute:#5B615E;--rule:#CBCFC9;--lat:#A0392A;--rab:#2B4A9C;--grk:#67762B;--hi:#FFF3C4;
 --e-cites:#1A1E21;--e-echo:#7A807C;--e-contest:#A0392A;--e-par:#B4B9B4;--e-trans:#2B4A9C;
 --serif:"EB Garamond",Garamond,"Times New Roman",serif;--sans:Inter,system-ui,sans-serif;--heb:"Frank Ruhl Libre","Times New Roman",serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151819;--paper:#1B1F21;--ink:#E7E5DD;--mute:#9AA09B;--rule:#33393B;--lat:#E28A73;--rab:#8EA6EC;--grk:#B9C66A;--hi:#3A3520;--e-cites:#E7E5DD;--e-echo:#8A908C;--e-contest:#E28A73;--e-par:#4C5250;--e-trans:#8EA6EC}}}}
:root[data-theme="dark"]{{--bg:#151819;--paper:#1B1F21;--ink:#E7E5DD;--mute:#9AA09B;--rule:#33393B;--lat:#E28A73;--rab:#8EA6EC;--grk:#B9C66A;--hi:#3A3520;--e-cites:#E7E5DD;--e-echo:#8A908C;--e-contest:#E28A73;--e-par:#4C5250;--e-trans:#8EA6EC}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:var(--serif);font-size:15px;line-height:1.42}}
.sheet{{max-width:1280px;margin:28px auto 80px;padding:0 20px}}
.head{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 24px;padding:0 4px 10px;border-bottom:1px solid var(--rule);font:12px var(--sans);color:var(--mute)}}
.head b{{font:500 15px var(--serif);color:var(--ink)}}
.head .lg{{display:flex;gap:14px}} .head .lg i{{display:inline-block;width:20px;border-top:2px solid var(--e-cites);vertical-align:middle;margin-right:5px}}
.head .lg .e i{{border-top-style:dashed;border-color:var(--e-echo)}} .head .lg .c i{{border-color:var(--e-contest)}} .head .lg .p i{{border-top-style:dotted;border-top-width:3px;border-color:var(--e-par)}} .head .lg .t i{{border-color:var(--e-trans)}}
.daf{{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr) minmax(0,.92fr);grid-template-areas:"lat mid rab" "foot foot rab";column-gap:30px;row-gap:22px;padding:26px 8px 12px;background:var(--paper)}}
.lat{{grid-area:lat}} .mid{{grid-area:mid}} .rab{{grid-area:rab}} .foot{{grid-area:foot;column-count:2;column-gap:30px;border-top:1px solid var(--rule);padding-top:16px}}
.rab{{border-left:1px solid var(--rule);padding-left:26px}}
.lat{{border-right:1px solid var(--rule);padding-right:26px}}
.col-h{{font:600 10.5px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin:0 0 10px;display:flex;justify-content:space-between}}
.col-h.rab{{color:var(--rab)}} .col-h.lat{{color:var(--lat)}}
.mid .verse{{text-align:center;padding:6px 8px 14px}}
.mid .heb{{font-family:var(--heb);font-size:27px;line-height:1.7;direction:rtl}}
.mid .la{{font-style:italic;font-size:20px;margin-top:6px}}
.mid .en{{font-size:16.5px;color:var(--mute);margin-top:4px}}
.mid mark{{background:var(--hi);color:inherit;padding:0 .12em}}
.mid .q{{margin:8px 0 0;text-align:center;font-size:14px;color:var(--mute)}}
.mid .q .hq{{font-family:var(--heb);font-size:17px;direction:rtl;color:var(--ink)}} .mid .q .lq{{font-style:italic;font-size:15.5px;color:var(--ink)}}
.mid .tr{{margin-top:16px;border-top:1px solid var(--rule);padding-top:10px}}
.mid .gl{{margin-top:14px;border:1px dashed var(--rule);padding:10px 12px}}
.sn{{position:relative;margin:0 0 11px;text-align:justify;hyphens:auto;font-size:14.2px;line-height:1.4;break-inside:avoid;cursor:pointer;outline:0}}
.sn .sig{{display:block;font:500 10px var(--sans);letter-spacing:.06em;color:var(--mute);margin-bottom:1px}}
.sn .dh{{font-weight:600}} .sn .dh.he{{font-family:var(--heb);font-size:15.5px;unicode-bidi:isolate}} .sn .dh.la,.sn .dh.el{{font-style:italic;font-weight:500}}
.sn .dh::after{{content:" —"}}
.sn.rabbinic .dh{{color:var(--rab)}} .sn.latin .dh{{color:var(--lat)}} .sn.greek-jewish .dh{{color:var(--grk)}}
.sn.slot{{opacity:.55}} .sn.slot .ex{{font-style:italic}}
.sn.on{{background:var(--hi)}} .sn.rel{{box-shadow:inset 3px 0 0 var(--mute);padding-left:8px}} .sn.rel.rabbinic{{box-shadow:inset 3px 0 0 var(--rab)}} .sn.rel.latin{{box-shadow:inset 3px 0 0 var(--lat)}}
.sn:focus-visible{{outline:2px solid var(--rab);outline-offset:2px}}
.sn.dim{{opacity:.38}}
#wires{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}}
#wires path{{fill:none;stroke-width:1.5}} #wires .cites{{stroke:var(--e-cites)}} #wires .echoes{{stroke:var(--e-echo);stroke-dasharray:5 4}} #wires .contests{{stroke:var(--e-contest);stroke-width:2}} #wires .parallel{{stroke:var(--e-par);stroke-dasharray:2 4;stroke-width:2}} #wires .transmits{{stroke:var(--e-trans)}}
#wires text{{font:500 9.5px var(--sans);fill:var(--mute);letter-spacing:.06em;text-transform:uppercase}}
#wires circle{{fill:var(--paper);stroke:var(--ink);stroke-width:1.2}}
.pop{{position:fixed;z-index:10;width:min(440px,92vw);max-height:78vh;overflow:auto;background:var(--paper);border:1px solid var(--rule);box-shadow:0 12px 40px rgba(0,0,0,.18);padding:16px 18px 18px;font-size:15.5px;line-height:1.48;display:none}}
.pop.show{{display:block}}
.pop .eyebrow{{font:600 10.5px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin:0 0 4px}}
.pop h3{{margin:0 0 8px;font:500 20px/1.2 var(--serif)}} .pop h3 small{{display:block;font:12px var(--sans);color:var(--mute);margin-top:2px}}
.pop .full{{margin:0}} .pop .full + .full{{margin-top:8px}}
.pop details{{margin:10px 0 0}} .pop summary{{cursor:pointer;font:500 12px var(--sans);color:var(--mute)}}
.pop .orig{{margin-top:6px;padding:8px 10px;background:var(--bg);border-left:1px solid var(--rule);font-size:14.5px}} .pop .orig.heb{{font-family:var(--heb);font-size:17px;line-height:1.8;text-align:right}} .pop .orig.lat{{font-style:italic}}
.pop .note{{font-size:14px;color:var(--mute);margin:10px 0 0}}
.pop .ans{{display:flex;flex-wrap:wrap;gap:5px;margin:8px 0 0}} .pop .ans span{{font:500 10.5px var(--sans);border:1px solid var(--rule);padding:2px 6px}}
.pop .cred{{font:11.5px var(--sans);color:var(--mute);margin:10px 0 0}}
.pop .th{{margin:12px 0 0;border-top:1px solid var(--rule);padding-top:8px;font-size:13.5px}} .pop .th p{{margin:0 0 6px}} .pop .th b{{font:600 10.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}}
.pop .pin{{position:absolute;top:8px;right:10px;font:500 11px var(--sans);color:var(--mute)}}
@media (max-width:980px){{.daf{{grid-template-columns:1fr;grid-template-areas:"mid" "rab" "lat" "foot"}} .rab,.lat{{border:0;padding:0}} .foot{{column-count:1}} #wires{{display:none}}}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
<div class="sheet">
  <div class="head">
    <span><b>Genesis 1:2</b> · Bereshit / In Principio · K7 · daf</span>
    <span class="lg"><span><i></i>cites</span><span class="e"><i></i>echoes</span><span class="c"><i></i>contests</span><span class="p"><i></i>parallel</span><span class="t"><i></i>transmits</span></span>
    <span>hover a note to read it whole and see its threads · click to pin</span>
  </div>
  <div class="daf" id="daf">
    <svg id="wires" aria-hidden="true"></svg>
    <section class="lat">
      <p class="col-h lat"><span>Patres</span><span>378–720</span></p>
      {block(lat_early)}
    </section>
    <section class="mid">
      <div class="verse">
        <div class="heb">{esc(verse["he"]["text"]).replace(esc("וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת"), "<mark>" + esc("וְר֣וּחַ אֱלֹהִ֔ים מְרַחֶ֖פֶת") + "</mark>")}</div>
        <div class="la">{esc(verse["la"]["text"]).replace("Spiritus Dei ferebatur", "<mark>Spiritus Dei ferebatur</mark>")}</div>
        <div class="en">{esc(verse["en"]["text"])}</div>
        <div class="q"><div class="hq">{esc(q["he"])}</div><div class="lq">{esc(q["la"])}</div>{esc(q["en"])}</div>
      </div>
      <div class="tr"><p class="col-h"><span>Versiones</span><span>LXX · Vulgate</span></p>{block(center_tr)}</div>
      <div class="gl"><p class="col-h"><span>Glossa ordinaria</span><span>Laon, c. 1120</span></p>{block(glossa)}</div>
    </section>
    <section class="rab">
      <p class="col-h rab"><span>מפרשים</span><span>Targums · Midrash · Bavli · Rashi</span></p>
      {block(rab)}
    </section>
    <section class="foot">
      <p class="col-h lat" style="column-span:all"><span>Scholae</span><span>Carolingian and twelfth-century Latin, 790–1170</span></p>
      {block(lat_late)}
    </section>
  </div>
  <div class="pop" id="pop" role="dialog" aria-live="polite"></div>
</div>
<script>
(function(){{
  const T = {tj}, N = {names};
  const daf = document.getElementById('daf'), wires = document.getElementById('wires'), pop = document.getElementById('pop');
  const sn = id => document.getElementById(id);
  let pinned = null, active = null;
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
  function anchor(el) {{ const r = el.getBoundingClientRect(), d = daf.getBoundingClientRect(); return {{x: r.left - d.left + r.width/2, y: r.top - d.top + r.height/2, l: r.left - d.left, r: r.right - d.left, t: r.top - d.top, b: r.bottom - d.top}}; }}
  function wire(a, b, type) {{
    // leave from the nearer horizontal edge of each block; curve through the page
    const A = anchor(a), B = anchor(b);
    const ax = B.x > A.x ? A.r : A.l, bx = B.x > A.x ? B.l : B.r;
    const ay = A.y, by = B.y, mx = (ax + bx) / 2;
    const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    p.setAttribute('d', `M ${{ax}} ${{ay}} C ${{mx}} ${{ay}}, ${{mx}} ${{by}}, ${{bx}} ${{by}}`);
    p.setAttribute('class', type); wires.appendChild(p);
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', mx); t.setAttribute('y', (ay + by) / 2 - 4); t.setAttribute('text-anchor', 'middle'); t.textContent = type; wires.appendChild(t);
    [[ax, ay], [bx, by]].forEach(([x, y]) => {{ const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', 3); wires.appendChild(c); }});
  }}
  function show(el, pin) {{
    if (pinned && !pin) return;
    clear(false); active = el;
    el.classList.add('on'); el.setAttribute('aria-expanded', 'true');
    const id = el.id, rel = T.filter(t => t.from === id || t.to === id);
    wires.innerHTML = '';
    const relIds = new Set();
    rel.forEach(t => {{ const o = t.from === id ? t.to : t.from; const oe = sn(o); if (!oe) return; relIds.add(o); oe.classList.add('rel'); wire(el, oe, t.type); }});
    document.querySelectorAll('.sn').forEach(s => {{ if (s !== el && !relIds.has(s.id)) s.classList.add('dim'); }});
    const tpl = el.querySelector('template').content.cloneNode(true);
    pop.innerHTML = ''; pop.appendChild(tpl);
    if (rel.length) {{
      const d = document.createElement('div'); d.className = 'th';
      d.innerHTML = rel.map(t => {{ const out = t.from === id; const o = out ? t.to : t.from; return `<p><b>${{out ? '→' : '←'}} ${{t.type}} · ${{esc(N[o] || o)}}</b><br>${{esc(t.evidence)}}</p>`; }}).join('');
      pop.appendChild(d);
    }}
    if (pin) {{ const s = document.createElement('span'); s.className = 'pin'; s.textContent = 'pinned · click page to release'; pop.appendChild(s); }}
    // place the popover on the side of the viewport away from the note
    const r = el.getBoundingClientRect(), vw = innerWidth, vh = innerHeight;
    pop.classList.add('show');
    const pw = pop.offsetWidth, ph = pop.offsetHeight;
    let x = r.left + r.width / 2 < vw / 2 ? Math.min(r.right + 18, vw - pw - 12) : Math.max(r.left - pw - 18, 12);
    let y = Math.min(Math.max(12, r.top - 20), vh - ph - 12);
    if (vw < 980) {{ x = 12; y = Math.min(r.bottom + 8, vh - ph - 12); }}
    pop.style.left = x + 'px'; pop.style.top = Math.max(12, y) + 'px';
  }}
  function clear(force) {{
    if (pinned && !force) return;
    document.querySelectorAll('.sn').forEach(s => {{ s.classList.remove('on', 'rel', 'dim'); s.setAttribute('aria-expanded', 'false'); }});
    wires.innerHTML = ''; pop.classList.remove('show'); active = null;
  }}
  document.querySelectorAll('.sn').forEach(el => {{
    el.addEventListener('mouseenter', () => show(el, false));
    el.addEventListener('focus', () => show(el, false));
    el.addEventListener('mouseleave', () => clear(false));
    el.addEventListener('blur', () => clear(false));
    el.addEventListener('click', e => {{ e.stopPropagation(); if (pinned === el) {{ pinned = null; clear(true); }} else {{ pinned = el; show(el, true); }} }});
    el.addEventListener('keydown', e => {{ if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); el.click(); }} if (e.key === 'Escape') {{ pinned = null; clear(true); }} }});
  }});
  pop.addEventListener('click', e => e.stopPropagation());
  document.addEventListener('click', () => {{ pinned = null; clear(true); }});
  window.addEventListener('resize', () => {{ if (active) show(active, !!pinned); }});
}})();
</script>
'''
out = ROOT / "out"; out.mkdir(exist_ok=True)
(out / f"C-daf-{crux_id}.html").write_text(page)
print(f"wrote out/C-daf-{crux_id}.html  (rab {len(rab)}, patres {len(lat_early)}, scholae {len(lat_late)}, versiones {len(center_tr)}, glossa {len(glossa)})")
