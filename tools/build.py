#!/usr/bin/env python3
"""Builds the static site for mana-mgmt.com into public/.

Usage: python3 tools/build.py
Content lives in tools/content.py. Design follows MANA (SOP) Design Rules (22 Oct 2026):
neutral page, MANA blue #002FA7 at about 10%, Archivo, sentence case, AA contrast.
Never hand-edit public/; change this file or content.py and rebuild.
"""
import datetime, html, json, pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import content as C  # noqa: E402

SRC, OUT = ROOT / "src", ROOT / "public"
SITE = "https://www.mana-mgmt.com"
TODAY = datetime.date.today().isoformat()
FORMSPREE_ID = "mvzekrgq"
e = html.escape

MARK = (SRC / "assets/brand/mark-blue.svg").read_text()
MARK_PATHS = MARK[MARK.index("<path"):MARK.rindex("</svg>")]


def mark(color="#002FA7", size=28, label=None):
    a = 'role="img" aria-label="%s"' % e(label) if label else 'aria-hidden="true"'
    return '<svg class="mk" viewBox="0 0 200 200" width="%d" height="%d" %s>%s</svg>' % (
        size, size, a, MARK_PATHS.replace("#002FA7", color))


def lockup(color="#002FA7", text="#0A0A0A", sub="#52525B"):
    return ('<span class="lockup">%s<span class="lk-t"><span class="lk-w" style="color:%s">MANA</span>'
            '<span class="lk-s" style="color:%s">Talent management</span></span></span>') % (mark(color, 30), text, sub)


CSS = r"""
:root{
  --blue:#002FA7;--blue-deep:#00248A;--blue-tint:#EEF2FB;
  --text:#0A0A0A;--text-2:#52525B;--label:#71717A;
  --bg:#FAFAFA;--card:#FFFFFF;--line:#E4E4E7;--err:#D2372B;
  --f:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--fd:'Anton',Impact,sans-serif;
  --maxw:1160px;--r:12px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:80px}
body{background:var(--bg);color:var(--text);font:400 16px/1.6 var(--f);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:inherit}
img{display:block;max-width:100%;height:auto}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:16px;background:var(--card);padding:8px 12px;z-index:50}
:focus-visible{outline:2px solid var(--blue);outline-offset:2px;border-radius:4px}

/* lockup: the one spaced-caps brand mark allowed */
.lockup{display:inline-flex;align-items:center;gap:10px;text-decoration:none}
.lk-t{display:flex;flex-direction:column;line-height:1}
.lk-w{font:400 22px/1 var(--fd);letter-spacing:.14em}
.lk-s{font:600 9px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;margin-top:4px}

/* header */
.hd{position:sticky;top:0;z-index:20;background:rgba(250,250,250,.92);backdrop-filter:saturate(1.4) blur(10px);-webkit-backdrop-filter:saturate(1.4) blur(10px);border-bottom:1px solid var(--line)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:68px;gap:24px}
.hd nav{display:flex;align-items:center;gap:28px}
.hd nav a{font-size:15px;font-weight:500;color:var(--text-2);text-decoration:none}
.hd nav a:hover{color:var(--text)}
.hd nav a.btn-p,.hd nav a.btn-p:hover{color:#fff}
@media(max-width:820px){.hd nav a.nl{display:none}}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font:600 16px/1 var(--f);padding:14px 20px;border-radius:999px;text-decoration:none;border:1.5px solid transparent;cursor:pointer;transition:background .2s,border-color .2s,color .2s}
.btn-p{background:var(--blue);color:#fff}.btn-p:hover{background:var(--blue-deep)}
.btn-s{background:transparent;color:var(--text);border-color:#D4D4D8}.btn-s:hover{border-color:var(--text)}
.btn-sm{font-size:14px;padding:10px 16px}

/* type */
.eyebrow{font-size:13px;font-weight:600;color:var(--blue);margin-bottom:16px;display:block}
h1{font-weight:700;font-size:clamp(39px,6vw,61px);line-height:1.04;letter-spacing:-.03em;max-width:15ch}
h2{font-weight:700;font-size:clamp(31px,4vw,39px);line-height:1.12;letter-spacing:-.02em;max-width:22ch}
h3{font-weight:700;font-size:20px;line-height:1.3;letter-spacing:-.01em}
.lede{font-size:20px;line-height:1.55;color:var(--text-2);max-width:56ch;margin-top:24px}
.lede b{color:var(--text);font-weight:600}
.sub{font-size:16px;color:var(--text-2);max-width:60ch;margin-top:12px}
.label{font-size:13px;color:var(--label)}
section{padding:96px 0}
@media(max-width:720px){section{padding:64px 0}}
.sec-head{margin-bottom:32px}

/* hero */
.hero{padding:72px 0 96px}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:56px;align-items:center}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px}
.hero .trust{margin-top:24px;font-size:14px;color:var(--label)}
.stack{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.stack figure{border-radius:var(--r);overflow:hidden;background:#E4E4E7;aspect-ratio:4/5}
.stack figure:nth-child(2){transform:translateY(32px)}
.stack img{width:100%;height:100%;object-fit:cover}
.stack figcaption{position:absolute;left:-9999px}
@media(max-width:900px){.hero .wrap{grid-template-columns:minmax(0,1fr);gap:40px}.stack figure:nth-child(2){transform:none}}


/* roster */
.roster{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.cr{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column}
.cr .ph{aspect-ratio:4/5;background:#E4E4E7}
.cr .ph img{width:100%;height:100%;object-fit:cover}
.cr .bd{padding:24px;display:flex;flex-direction:column;gap:12px;flex:1}
.cr .niche{font-size:14px;font-weight:600;color:var(--blue)}
.cr p{font-size:15px;color:var(--text-2)}
.cr dl{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding-top:12px;border-top:1px solid var(--line);margin-top:auto}
.cr dt{font-size:13px;color:var(--label);order:2}
.cr dd{font-weight:700;font-size:20px;line-height:1.1;font-variant-numeric:tabular-nums}
.cr dl div{display:flex;flex-direction:column;gap:4px}
.cr .act{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:space-between}
.cr .ig{font-size:14px;color:var(--text-2);text-decoration:none}.cr .ig:hover{color:var(--text);text-decoration:underline}
@media(max-width:900px){.roster{grid-template-columns:minmax(0,1fr);max-width:520px}}

/* work */
.work{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.cs{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;display:flex;flex-direction:column}
.cs .vis{aspect-ratio:16/10;background:#F4F4F5;display:flex;align-items:flex-end;padding:20px;position:relative;overflow:hidden}
.cs .vis img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cs .vis .big{font-weight:700;font-size:49px;line-height:1;letter-spacing:-.03em;color:var(--blue);font-variant-numeric:tabular-nums}
.cs .vis .big small{display:block;font-size:15px;font-weight:600;letter-spacing:0;color:var(--text-2);margin-top:8px}
.cs .bd{padding:24px;display:flex;flex-direction:column;gap:12px;flex:1}
.cs .who{font-size:13px;color:var(--label)}
.cs p{font-size:15px;color:var(--text-2)}
.cs ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:8px}
.cs li{font-size:13px;font-weight:600;background:#F4F4F5;border-radius:999px;padding:6px 12px}
@media(max-width:900px){.work{grid-template-columns:minmax(0,1fr);max-width:620px}}

/* brands */
.brands{display:flex;flex-wrap:wrap;gap:8px 32px;margin-top:8px}
.brands li{list-style:none;font-weight:600;font-size:20px;color:var(--text-2);letter-spacing:-.01em}

/* process */
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;counter-reset:s}
.st{border-top:2px solid var(--text);padding-top:16px}
.st::before{counter-increment:s;content:counter(s);display:block;font-size:13px;font-weight:600;color:var(--label);margin-bottom:8px}
.st p{font-size:15px;color:var(--text-2);margin-top:8px}
.st:first-child{border-top-color:var(--blue)}
@media(max-width:900px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:520px){.steps{grid-template-columns:minmax(0,1fr)}}

/* creators band */
.join{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:32px;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.join p{color:var(--text-2);max-width:60ch;margin-top:8px}

/* faq */
.faq{max-width:780px}
.faq details{border-bottom:1px solid var(--line);padding:20px 0}
.faq summary{font-weight:600;font-size:18px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-weight:400;font-size:24px;line-height:1;color:var(--label)}
.faq details[open] summary::after{content:"–"}
.faq details p{color:var(--text-2);margin-top:12px;max-width:68ch}

/* contact */
.contact .wrap{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:56px;align-items:start}
.contact .direct{margin-top:32px;display:flex;flex-direction:column;gap:8px;font-size:16px}
.contact .direct a{color:var(--text);text-decoration:underline;text-underline-offset:3px;text-decoration-color:#A1A1AA}
.form{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:32px}
.field{margin-bottom:20px}
.field label{display:block;font-size:14px;font-weight:600;margin-bottom:8px}
.field label span{font-weight:400;color:var(--label)}
.field input,.field select,.field textarea{width:100%;font:400 16px/1.4 var(--f);color:var(--text);background:var(--card);border:1px solid #D4D4D8;border-radius:8px;padding:12px 14px}
.field select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2352525B' stroke-width='1.6' fill='none'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;padding-right:36px}
.field textarea{min-height:120px;resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--blue);box-shadow:0 0 0 3px rgba(0,47,167,.15)}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.hp{position:absolute;left:-9999px}
.form .btn{width:100%;margin-top:4px}
.form .note{font-size:13px;color:var(--label);margin-top:12px}
.status{display:none;margin-top:16px;font-size:15px;padding:12px 14px;border-radius:8px}
.status.ok{display:block;background:var(--blue-tint);color:var(--blue)}
.status.err{display:block;background:#FDECEA;color:#A1271D}
@media(max-width:900px){.contact .wrap{grid-template-columns:minmax(0,1fr);gap:40px}}
@media(max-width:520px){.row2{grid-template-columns:minmax(0,1fr)}.form{padding:24px}}

/* footer: a lockup surface, so full blue is allowed here */
.ft{background:var(--blue);color:#fff;padding:64px 0 40px}
.ft .top{display:flex;justify-content:space-between;gap:40px;flex-wrap:wrap}
.ft .blurb{max-width:40ch;color:#fff;font-size:15px;margin-top:16px}
.ft .cols{display:flex;gap:56px;flex-wrap:wrap}
.ft h4{font-size:13px;font-weight:600;color:#fff;margin-bottom:12px}
.ft .cols a{display:block;color:#fff;text-decoration:none;font-size:15px;margin-bottom:8px;opacity:1}
.ft .cols a:hover{text-decoration:underline}
.ft .bot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:48px;padding-top:24px;border-top:1px solid rgba(255,255,255,.25);font-size:13px;color:#fff}

/* 404 */
.nf{padding:120px 0;min-height:60vh}
.nf .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px}
"""

JS = r"""
(function(){
  var form=document.getElementById('lead'); if(!form) return;
  var sel=document.getElementById('need'), st=document.getElementById('status'), btn=form.querySelector('button');
  document.querySelectorAll('[data-need]').forEach(function(a){
    a.addEventListener('click',function(){ sel.value=a.getAttribute('data-need'); });
  });
  var q=new URLSearchParams(location.search).get('need'); if(q){ sel.value=q; }
  form.addEventListener('submit',async function(ev){
    ev.preventDefault(); st.className='status';
    var data=new FormData(form); data.append('page',location.pathname);
    data.append('_subject','Website lead: '+sel.options[sel.selectedIndex].text);
    btn.disabled=true; var t=btn.textContent; btn.textContent='Sending…';
    try{
      var r=await fetch('https://formspree.io/f/%(FS)s',{method:'POST',body:data,headers:{'Accept':'application/json'}});
      if(!r.ok) throw new Error('send failed');
      form.reset(); st.className='status ok';
      st.textContent='Thanks, it’s with us. You’ll get a reply from shei@mana-mgmt.com, usually within a day.';
      btn.textContent='Sent';
    }catch(err){
      st.className='status err';
      st.textContent='That didn’t send. Please email shei@mana-mgmt.com directly.';
      btn.disabled=false; btn.textContent=t;
    }
  });
})();
""" % {"FS": FORMSPREE_ID}


def head(title, desc, path, jsonld=None, og_image="/assets/og/home.png"):
    url = SITE + (path if path != "/" else "/")
    ld = ""
    if jsonld:
        ld = '<script type="application/ld+json">%s</script>\n' % json.dumps(jsonld, ensure_ascii=False, separators=(",", ":"))
    return """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{u}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#FAFAFA">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MANA">
<meta property="og:locale" content="en_AU">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{site}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
""".format(t=e(title), d=e(desc), u=url, site=SITE, og=og_image, ld=ld)


def header():
    links = "".join('<a class="nl" href="%s">%s</a>' % (h, e(t)) for h, t in C.NAV)
    return """<header class="hd"><div class="wrap">
<a href="/" aria-label="MANA, home">{lk}</a>
<nav aria-label="Main">{links}<a class="btn btn-p btn-sm" href="/#contact" data-need="kit-all">Get a media kit</a></nav>
</div></header>
""".format(lk=lockup(), links=links)


def footer():
    cols = []
    for title, items in C.FOOTER:
        cols.append("<div><h4>%s</h4>%s</div>" % (e(title), "".join(
            '<a href="%s"%s>%s</a>' % (h, ' rel="noopener"' if h.startswith("http") else "", e(t)) for t, h in items)))
    return """<footer class="ft"><div class="wrap">
<div class="top"><div>{lk}<p class="blurb">{blurb}</p></div><div class="cols">{cols}</div></div>
<div class="bot"><span>© {y} MANA · Melbourne, Australia</span><span>shei@mana-mgmt.com</span></div>
</div></footer>
<script src="/assets/site.js" defer></script>
<script>window.va=window.va||function(){{(window.vaq=window.vaq||[]).push(arguments)}};</script>
<script defer src="/_vercel/insights/script.js"></script>
</body></html>
""".format(lk=lockup("#FFFFFF", "#FFFFFF", "#FFFFFF"), blurb=e(C.FOOTER_BLURB), cols="".join(cols), y=datetime.date.today().year)


def lead_form():
    opts = "".join('<option value="%s">%s</option>' % (v, e(t)) for v, t in C.NEEDS)
    return """<form class="form" id="lead" novalidate>
<div class="row2">
<div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
</div>
<div class="field"><label for="f-co">Brand or company <span>(or your @handle)</span></label><input id="f-co" name="company" autocomplete="organization"></div>
<div class="field"><label for="need">What do you need?</label><select id="need" name="need">{opts}</select></div>
<div class="field"><label for="f-msg">Brief, timing or budget <span>(optional)</span></label><textarea id="f-msg" name="message" placeholder="Product, what you want made, and when it should go live."></textarea></div>
<input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-p" type="submit">Send</button>
<div class="status" id="status" role="status" aria-live="polite"></div>
<p class="note">We usually reply within a day.</p>
</form>""".format(opts=opts)


def home():
    h = C.HOME
    pics = "".join('<figure><img src="/assets/img/%s.webp" alt="%s" width="800" height="1000"%s><figcaption>%s</figcaption></figure>' % (
        c["slug"], e(c["photo_alt"]), "" if i == 0 else ' loading="lazy"', e(c["name"])) for i, c in enumerate(C.CREATORS))
    roster = []
    for c in C.CREATORS:
        stats = "".join("<div><dd>%s</dd><dt>%s</dt></div>" % (e(v), e(k)) for v, k in c["stats"])
        roster.append("""<article class="cr" id="{slug}">
<div class="ph"><img src="/assets/img/{slug}.webp" alt="{alt}" width="800" height="1000" loading="lazy"></div>
<div class="bd"><span class="niche">{niche}</span><h3>{name}</h3>
<dl>{stats}</dl>
<div class="act"><a class="btn btn-s btn-sm" href="#contact" data-need="kit-{key}">Get {first}’s media kit</a><a class="ig" href="{ig}" rel="noopener">{handle} on Instagram</a></div>
</div></article>""".format(slug=c["slug"], alt=e(c["photo_alt"]), niche=e(c["niche"]), name=e(c["name"]), blurb=e(c["blurb"]),
                           stats=stats, key=c["key"], first=e(c["name"].split()[0]), ig=c["instagram"], handle=e(c["handle"])))
    work = []
    for w in C.WORK:
        vis = ('<img src="/assets/img/%s" alt="%s" loading="lazy" width="960" height="540">' % (w["image"], e(w["image_alt"]))) if w.get("image") \
            else '<div class="big">%s<small>%s</small></div>' % (e(w["big"]), e(w["big_label"]))
        work.append("""<article class="cs"><div class="vis">{vis}</div><div class="bd">
<span class="who">{who}</span><h3>{title}</h3><ul>{chips}</ul></div></article>""".format(
            vis=vis, who=e(w["who"]), title=e(w["title"]), body=e(w["body"]), chips="".join("<li>%s</li>" % e(x) for x in w["chips"])))
    brands = "".join("<li>%s</li>" % e(b) for b in C.BRANDS)
    steps = "".join('<div class="st"><h3>%s</h3><p>%s</p></div>' % (e(t), e(b)) for t, b in C.STEPS)
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in C.FAQ)

    body = """<main id="main">
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<div class="cta"><a class="btn btn-p" href="#contact" data-need="kit-all">Get a media kit</a><a class="btn btn-s" href="#contact" data-need="brief">Send a brief</a></div>
<p class="trust">{trust}</p>
</div>
<div class="stack">{pics}</div>
</div></section>

<section id="creators" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>{roster_h}</h2></div>
<div class="roster">{roster}</div>
</div></section>

<section id="work" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>{work_h}</h2></div>
<div class="work">{work}</div>
<div style="margin-top:56px"><h3>Brands our creators have made work for</h3><ul class="brands">{brands}</ul></div>
</div></section>

<section id="process" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>{proc_h}</h2></div>
<div class="steps">{steps}</div>
<div class="join" style="margin-top:56px"><h3>{join_h}</h3><a class="btn btn-s" href="#contact" data-need="creator">Apply for management</a></div>
</div></section>

<section id="faq" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>Questions</h2></div>
<div class="faq">{faq}</div>
</div></section>

<section class="contact" id="contact" style="padding-top:0"><div class="wrap">
<div><h2>{contact_h}</h2><p class="sub">{contact_sub}</p>
<div class="direct"><a href="mailto:shei@mana-mgmt.com">shei@mana-mgmt.com</a><a href="https://www.instagram.com/manamgmt/" rel="noopener">@manamgmt on Instagram</a></div></div>
{form}
</div></section>
</main>
""".format(eyebrow=e(h["eyebrow"]), h1=e(h["h1"]), lede=h["lede_html"], trust=e(h["trust"]), pics=pics,
           roster_h=e(h["roster_h"]), roster_sub=e(h["roster_sub"]), roster="".join(roster),
           work_h=e(h["work_h"]), work_sub=e(h["work_sub"]), work="".join(work), brands=brands,
           proc_h=e(h["proc_h"]), proc_sub=e(h["proc_sub"]), steps=steps, join_h=e(h["join_h"]), join_p=e(h["join_p"]),
           faq=faq, contact_h=e(h["contact_h"]), contact_sub=e(h["contact_sub"]), form=lead_form())
    return head(h["title"], h["description"], "/", jsonld_home()) + header() + body + footer()


def org():
    return {
        "@type": "Organization", "@id": SITE + "/#org", "name": "MANA", "alternateName": ["MANA Talent Management", "MANA MGMT"],
        "url": SITE + "/", "logo": SITE + "/assets/brand/mana-logo-512.png", "image": SITE + "/assets/og/home.png",
        "description": C.ORG_DESCRIPTION, "email": "shei@mana-mgmt.com", "foundingLocation": "Melbourne, Australia",
        "address": {"@type": "PostalAddress", "addressLocality": "Melbourne", "addressRegion": "VIC", "addressCountry": "AU"},
        "areaServed": ["Australia", "United States", "United Kingdom", "Worldwide"],
        "knowsAbout": C.KNOWS_ABOUT, "sameAs": C.ORG_SAMEAS,
        "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": "shei@mana-mgmt.com", "areaServed": "Worldwide", "availableLanguage": "English"},
    }


def person(c):
    return {"@type": "Person", "@id": SITE + "/#" + c["slug"], "name": c["name"], "jobTitle": c["job_title"],
            "description": c["blurb"], "image": SITE + "/assets/img/%s.webp" % c["slug"],
            "homeLocation": {"@type": "Place", "name": "Melbourne, Australia"}, "knowsAbout": c["knows_about"],
            "sameAs": c["same_as"], "affiliation": {"@id": SITE + "/#org"}}


def jsonld_home():
    return {"@context": "https://schema.org", "@graph": [
        org(),
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "MANA", "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-AU"},
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": C.HOME["title"], "description": C.HOME["description"],
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#org"}, "dateModified": TODAY, "inLanguage": "en-AU"},
        *[person(c) for c in C.CREATORS],
        {"@type": "FAQPage", "@id": SITE + "/#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in C.FAQ]},
    ]}


def not_found():
    body = """<main id="main" class="nf"><div class="wrap">
<span class="eyebrow">404</span><h1>That page isn’t here.</h1>
<p class="lede">It may have moved while we rebuilt the site. Everything about our creators and how to work with us starts on the home page.</p>
<div class="cta"><a class="btn btn-p" href="/">Go to the home page</a><a class="btn btn-s" href="/#contact">Contact us</a></div>
</div></main>
"""
    h = head("Page not found | MANA", "This page doesn't exist on mana-mgmt.com.", "/404")
    return h.replace('content="index,follow,max-image-preview:large"', 'content="noindex"') + header() + body + footer()


def robots():
    return "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE


def sitemap(paths):
    urls = "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (SITE, p, TODAY) for p in paths)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls


def llms():
    lines = ["# MANA", "", "> " + C.ORG_DESCRIPTION, "",
             "MANA is based in Melbourne, Australia, and works with brands in Australia and worldwide. "
             "Brands contact MANA for creator media kits and campaign briefs; rates are shared on request, not published.", "",
             "## Creators"]
    for c in C.CREATORS:
        lines.append("- %s (%s, %s): %s" % (c["name"], c["handle"], c["niche"], c["blurb"]))
    lines += ["", "## Selected work"]
    for w in C.WORK:
        lines.append("- %s, %s: %s (%s)" % (w["title"], w["who"], w["body"], ", ".join(w["chips"])))
    lines += ["", "## Contact", "- Email: shei@mana-mgmt.com", "- Media kit or brief: %s/#contact" % SITE,
              "- Instagram: https://www.instagram.com/manamgmt/", ""]
    return "\n".join(lines)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copytree(SRC / "assets/img", OUT / "assets/img")
    shutil.copytree(SRC / "assets/brand", OUT / "assets/brand")
    if (SRC / "assets/og").exists():
        shutil.copytree(SRC / "assets/og", OUT / "assets/og")
    for name in ("favicon.svg", "apple-touch-icon.png"):
        if (SRC / "assets/brand" / name).exists():
            shutil.copy(SRC / "assets/brand" / name, OUT / name)
    (OUT / "assets/site.css").write_text(CSS.strip() + "\n")
    (OUT / "assets/site.js").write_text(JS.strip() + "\n")
    (OUT / "index.html").write_text(home())
    (OUT / "404.html").write_text(not_found())
    (OUT / "robots.txt").write_text(robots())
    (OUT / "sitemap.xml").write_text(sitemap(["/"]))
    (OUT / "llms.txt").write_text(llms())
    print("built", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file()))


if __name__ == "__main__":
    main()
