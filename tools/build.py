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
.mark-wrap{display:flex;justify-content:center;align-items:center}
.hero-mark{width:min(340px,100%);height:auto;aspect-ratio:1}
.hero-mark path{stroke-dasharray:1;stroke-dashoffset:1;animation:weave 1.6s cubic-bezier(.7,0,.2,1) forwards}
.hero-mark path:nth-child(1){animation-delay:.2s}.hero-mark path:nth-child(2){animation-delay:.45s}
.hero-mark path:nth-child(3){animation-delay:.7s}.hero-mark path:nth-child(4){animation-delay:.95s}
@keyframes weave{to{stroke-dashoffset:0}}
@media(max-width:900px){.hero .wrap{grid-template-columns:minmax(0,1fr);gap:40px}.mark-wrap{justify-content:flex-start}.hero-mark{width:160px}}


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

/* brand marquee */
.brands-mq{padding:8px 0 96px}
.mq-h{text-align:center;font-size:13px;color:var(--label);margin-bottom:24px}
.mq{display:flex;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.mq+.mq{margin-top:16px}
.mq-t{display:flex;flex:none;list-style:none;animation:mq 45s linear infinite}
.mq-t.rev{animation-direction:reverse}
.mq:hover .mq-t{animation-play-state:paused}
.mq-i{flex:none;height:56px;padding:0 36px;display:flex;align-items:center}
.mq-i img{height:30px;width:auto;max-width:150px;object-fit:contain;filter:grayscale(1) brightness(0);opacity:.6}
.mq-i span{font-weight:700;font-size:20px;letter-spacing:-.01em;color:#52525B}
@keyframes mq{to{transform:translateX(-100%)}}
@media(prefers-reduced-motion:reduce){.mq-t{animation:none}.mq-t[aria-hidden]{display:none}.mq{flex-wrap:wrap;justify-content:center;-webkit-mask-image:none;mask-image:none}.hero-mark path{animation:none;stroke-dashoffset:0}}

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


def lead_form(need=None):
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
    hero_mark = '<svg class="hero-mark" viewBox="0 0 200 200" role="img" aria-label="MANA mark">%s</svg>' % MARK_PATHS.replace("<path ", '<path pathLength="1" ')
    logos = []
    for name, f in C.BRAND_LOGOS:
        logos.append('<li class="mq-i">%s</li>' % (
            '<img src="/assets/logos/%s" alt="%s" loading="lazy" height="32">' % (f, e(name)) if f else '<span>%s</span>' % e(name)))
    half = (len(logos) + 1) // 2
    def track(items, rev=""):
        return '<div class="mq"><ul class="mq-t%s">%s</ul><ul class="mq-t%s" aria-hidden="true">%s</ul></div>' % (rev, "".join(items), rev, "".join(items))
    marquee = track(logos[:half]) + track(logos[half:], " rev")
    roster = []
    for c in C.CREATORS:
        stats = "".join("<div><dd>%s</dd><dt>%s</dt></div>" % (e(v), e(k)) for v, k in c["stats"])
        roster.append("""<article class="cr" id="{slug}">
<div class="ph"><img src="/assets/img/{slug}.webp" alt="{alt}" width="800" height="1000" loading="lazy"></div>
<div class="bd"><span class="niche">{niche}</span><h3><a href="/creators/{slug}">{name}</a></h3>
<dl>{stats}</dl>
<div class="act"><a class="btn btn-s btn-sm" href="#contact" data-need="kit-{key}">Get {first}’s media kit</a><a class="ig" href="/creators/{slug}">View profile</a></div>
</div></article>""".format(slug=c["slug"], alt=e(c["photo_alt"]), niche=e(c["niche"]), name=e(c["name"]), blurb=e(c["blurb"]),
                           stats=stats, key=c["key"], first=e(c["name"].split()[0]), ig=c["instagram"], handle=e(c["handle"])))
    steps = "".join('<div class="st"><h3>%s</h3><p>%s</p></div>' % (e(t), e(b)) for t, b in C.STEPS)
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in C.FAQ)

    body = """<main id="main">
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<div class="cta"><a class="btn btn-p" href="#contact" data-need="kit-all">Get a media kit</a><a class="btn btn-s" href="#contact" data-need="brief">Send a brief</a></div>
</div>
<div class="mark-wrap">{hero_mark}</div>
</div></section>

<section class="brands-mq" aria-label="Brands our creators have worked with">
<p class="mq-h">Our creators have worked with</p>
{marquee}
</section>

<section id="creators" style="padding-top:0"><div class="wrap">
<div class="sec-head"><h2>{roster_h}</h2></div>
<div class="roster">{roster}</div>
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

{contact}</main>
""".format(eyebrow=e(h["eyebrow"]), h1=e(h["h1"]), lede=h["lede_html"], trust=e(h["trust"]), hero_mark=hero_mark, marquee=marquee,
           roster_h=e(h["roster_h"]), roster_sub=e(h["roster_sub"]), roster="".join(roster),
           proc_h=e(h["proc_h"]), proc_sub=e(h["proc_sub"]), steps=steps, join_h=e(h["join_h"]), join_p=e(h["join_p"]),
           faq=faq, contact=contact_section(h["contact_h"], h["contact_sub"]).replace('class="contact" id="contact"', 'class="contact" id="contact" style="padding-top:0"'))
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


# ---------------------------------------------------------------- interior pages
INDEXNOW_KEY = "7c3e9a51d84b4f2e9b6a0c1d2e3f4a5b"
PAGES = []  # (path, priority) for the sitemap, filled by build_pages()


def contact_section(h2="Get a media kit", sub="We’ll reply with the media kit, usually within a day.", need=None):
    return """<section class="contact" id="contact"><div class="wrap">
<div><h2>{h2}</h2><p class="sub">{sub}</p>
<div class="direct"><a href="mailto:shei@mana-mgmt.com">shei@mana-mgmt.com</a><a href="https://www.instagram.com/manamgmt/" rel="noopener">@manamgmt on Instagram</a></div></div>
{form}
</div></section>
""".format(h2=e(h2), sub=e(sub), form=lead_form(need))


def crumbs(trail):
    """trail: [(name, path)], last item is the current page."""
    html = '<nav class="crumbs" aria-label="Breadcrumb">' + ' <span aria-hidden="true">/</span> '.join(
        ('<a href="%s">%s</a>' % (p, e(n)) if i < len(trail) - 1 else '<span aria-current="page">%s</span>' % e(n))
        for i, (n, p) in enumerate(trail)) + '</nav>'
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(trail)]}
    return html, ld


def faq_block(items, title="Questions"):
    html = '<section class="pg-sec"><div class="wrap"><h2>%s</h2><div class="faq">%s</div></div></section>' % (
        e(title), "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in items))
    ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld


def page_hero(trail, eyebrow, h1, lede, side=""):
    ch, cld = crumbs(trail)
    return """<section class="pg-hero"><div class="wrap">{ch}<div class="pg-grid">
<div><span class="eyebrow">{eb}</span><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="cta"><a class="btn btn-p" href="#contact">Get a media kit</a><a class="btn btn-s" href="#contact" data-need="brief">Send a brief</a></div></div>
{side}</div></div></section>
""".format(ch=ch, eb=e(eyebrow), h1=e(h1), lede=e(lede), side=side), cld


def write_page(path, title, desc, body, graph, og="/assets/og/home.png", priority="0.8"):
    ld = {"@context": "https://schema.org", "@graph": [org(), {"@type": "WebPage", "@id": SITE + path + "#webpage", "url": SITE + path,
          "name": title, "description": desc, "isPartOf": {"@type": "WebSite", "@id": SITE + "/#website"}, "dateModified": TODAY,
          "inLanguage": "en-AU"}] + graph}
    html = head(title, desc, path, ld, og) + header() + '<main id="main">' + body + "</main>" + footer()
    out = OUT / (path.strip("/") + ".html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    PAGES.append((path, priority))


def creator_by_key(k):
    return next(c for c in C.CREATORS if c["key"] == k)


def profile_page(key):
    c, p = creator_by_key(key), C.PROFILES[key]
    path = "/creators/" + c["slug"]
    side = '<div class="pg-photo"><img src="/assets/img/%s.webp" alt="%s" width="800" height="1000"></div>' % (c["slug"], e(c["photo_alt"]))
    hero, cld = page_hero([("Home", "/"), ("Creators", "/creators"), (c["name"], path)], p["eyebrow"], c["name"], p["lede"], side)
    facts = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(k), e(v)) for k, v in p["facts"])
    hl = "".join("<li>%s</li>" % e(x) for x in p["highlights"])
    brands = ('<h3 class="mt">Brands %s has made work for</h3><ul class="chips">%s</ul>' % (e(c["name"].split()[0]), "".join(
        "<li>%s</li>" % e(b) for b in p["brands"]))) if p["brands"] else ""
    gal = ""
    if len(p["gallery"]) > 1:
        gal = '<section class="pg-sec"><div class="wrap"><h2>Selected work</h2><div class="gal">%s</div></div></section>' % "".join(
            '<figure><img src="/assets/img/%s" alt="%s, %s by %s" width="640" height="800" loading="lazy"><figcaption><b>%s</b><span>%s</span></figcaption></figure>' % (
                f, e(b), e(w), e(c["name"]), e(b), e(w)) for f, b, w in p["gallery"])
    fq, fld = faq_block(p["faq"])
    body = hero + """<section class="pg-sec"><div class="wrap pg-two">
<div><h2>At a glance</h2><dl class="facts">{facts}</dl></div>
<div><h2>Results</h2><ul class="hl">{hl}</ul>{brands}<h3 class="mt">Best for</h3><p class="sub">{fit}</p></div>
</div></section>
{gal}{fq}""".format(facts=facts, hl=hl, brands=brands, fit=e(p["fit"]), gal=gal, fq=fq) + contact_section(
        "Get %s’s media kit" % c["name"].split()[0], "Audience data, past results and options for your campaign. We usually reply within a day.")
    body = body.replace('<option value="kit-%s">' % key, '<option value="kit-%s" selected>' % key)
    person_ld = person(c)
    person_ld["@id"] = SITE + path + "#person"
    person_ld["url"] = SITE + path
    graph = [{"@type": "ProfilePage", "@id": SITE + path + "#profile", "url": SITE + path, "mainEntity": {"@id": SITE + path + "#person"}},
             person_ld, cld, fld]
    write_page(path, p["title"], p["description"], body, graph, og="/assets/og/%s.png" % c["slug"], priority="0.9")


def creators_page():
    d = C.CREATORS_PAGE
    hero, cld = page_hero([("Home", "/"), ("Creators", "/creators")], d["eyebrow"], d["h1"], d["lede"])
    cards = "".join("""<article class="cr"><a class="ph" href="/creators/{slug}"><img src="/assets/img/{slug}.webp" alt="{alt}" width="800" height="1000" loading="lazy"></a>
<div class="bd"><span class="niche">{niche}</span><h3><a href="/creators/{slug}">{name}</a></h3><p class="fol"><b>{fol}</b> followers on Instagram</p><p>{blurb}</p>
<div class="act"><a class="btn btn-s btn-sm" href="/creators/{slug}">View profile</a><a class="ig" href="{ig}" rel="noopener">{handle}</a></div></div></article>""".format(
        slug=c["slug"], alt=e(c["photo_alt"]), niche=e(c["niche"]), name=e(c["name"]), blurb=e(c["blurb"]), ig=c["instagram"], handle=e(c["handle"]),
        fol=e(c["followers"])) for c in C.CREATORS)
    fit = "".join('<div><dt>%s</dt><dd><a href="/creators/%s">%s</a></dd></div>' % (
        e(k), next(c["slug"] for c in C.CREATORS if c["name"] == v), e(v)) for k, v in d["fit"])
    fq, fld = faq_block(d["faq"])
    body = hero + """<section class="pg-sec" style="padding-top:0"><div class="wrap"><div class="roster">{cards}</div><p class="k" style="margin-top:16px">{fnote}</p></div></section>
<section class="pg-sec"><div class="wrap"><h2>{fit_h}</h2><dl class="facts wide">{fit}</dl></div></section>{fq}""".format(
        cards=cards, fnote=e(d["followers_note"]), fit_h=e(d["fit_h"]), fit=fit, fq=fq) + contact_section("Get the media kits")
    items = {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE + "/creators/" + c["slug"], "name": c["name"]}
                                                       for i, c in enumerate(C.CREATORS)]}
    write_page("/creators", d["title"], d["description"], body, [items, cld, fld], og="/assets/og/creators.png", priority="0.9")


def brands_page():
    d = C.BRANDS_PAGE
    hero, cld = page_hero([("Home", "/"), ("For brands", "/brands")], d["eyebrow"], d["h1"], d["lede"])
    book = "".join("<li>%s</li>" % e(x) for x in d["book"])
    steps = "".join('<div class="st"><h3>%s</h3><p>%s</p></div>' % (e(t), e(b)) for t, b in d["steps"])
    wr = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (e(k), e(v)) for k, v in d["writing"])
    logos = "".join('<li><img src="/assets/logos/%s" alt="%s" loading="lazy" height="28"></li>' % (f, e(n)) for n, f in C.BRAND_LOGOS if f)
    fq, fld = faq_block(d["faq"])
    body = hero + """<section class="pg-sec" style="padding-top:0"><div class="wrap pg-two">
<div><h2>{book_h}</h2><ul class="hl">{book}</ul></div>
<div><h2>{wr_h}</h2><dl class="facts">{wr}</dl></div></div></section>
<section class="pg-sec"><div class="wrap"><h2>How a campaign runs</h2><div class="steps" style="margin-top:32px">{steps}</div></div></section>
<section class="pg-sec"><div class="wrap"><h2>Brands our creators have worked with</h2><ul class="logo-grid">{logos}</ul></div></section>
{fq}""".format(book_h=e(d["book_h"]), book=book, wr_h=e(d["writing_h"]), wr=wr, steps=steps, logos=logos, fq=fq) + contact_section(
        "Send a brief", "Or ask for the media kits. We usually reply within a day.")
    body = body.replace('<option value="brief">', '<option value="brief" selected>')
    svc = {"@type": "Service", "name": "Creator and influencer partnerships", "serviceType": "Influencer marketing and talent management",
           "provider": {"@id": SITE + "/#org"}, "areaServed": ["Australia", "Worldwide"], "description": d["lede"]}
    write_page("/brands", d["title"], d["description"], body, [svc, cld, fld], og="/assets/og/brands.png", priority="0.9")


def ugc_page():
    d = C.UGC_PAGE
    hero, cld = page_hero([("Home", "/"), ("UGC creators", "/ugc-creators-australia")], d["eyebrow"], d["h1"], d["lede"])
    rows = "".join("<tr><th scope=\"row\">%s</th><td>%s</td><td>%s</td></tr>" % (e(a), e(b), e(c)) for a, b, c in d["vs"])
    who = "".join('<li><a href="/creators/{slug}"><b>{name}</b></a> · {t}</li>'.format(
        slug=creator_by_key(k)["slug"], name=e(creator_by_key(k)["name"]), t=e(t)) for k, t in d["who"])
    steps = "".join('<div class="st"><h3>%s</h3><p>%s</p></div>' % (e(t), e(b)) for t, b in d["steps"])
    fq, fld = faq_block(d["faq"])
    body = hero + """<section class="pg-sec" style="padding-top:0"><div class="wrap"><h2>{vs_h}</h2>
<div class="tbl"><table><thead><tr><th></th><th>UGC</th><th>Sponsored post</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section class="pg-sec"><div class="wrap"><h2>{who_h}</h2><ul class="hl">{who}</ul></div></section>
<section class="pg-sec"><div class="wrap"><h2>How UGC works with MANA</h2><div class="steps" style="margin-top:32px">{steps}</div></div></section>
{fq}""".format(vs_h=e(d["vs_h"]), rows=rows, who_h=e(d["who_h"]), who=who, steps=steps, fq=fq) + contact_section("Ask about UGC", "Tell us the product and where the content will run. We usually reply within a day.")
    body = body.replace('<option value="brief">', '<option value="brief" selected>')
    svc = {"@type": "Service", "name": "UGC creators in Australia", "serviceType": "User-generated content production",
           "provider": {"@id": SITE + "/#org"}, "areaServed": "Australia", "description": d["lede"]}
    write_page("/ugc-creators-australia", d["title"], d["description"], body, [svc, cld, fld], og="/assets/og/ugc.png", priority="0.8")


def about_page():
    d = C.ABOUT_PAGE
    hero, cld = page_hero([("Home", "/"), ("About", "/about")], d["eyebrow"], d["h1"], d["lede"])
    pts = "".join('<div class="st"><h3>%s</h3><p>%s</p></div>' % (e(t), e(b)) for t, b in d["points"])
    fq, fld = faq_block(d["faq"])
    body = hero + '<section class="pg-sec" style="padding-top:0"><div class="wrap"><h2>How we work</h2><div class="steps nonum" style="margin-top:32px">%s</div></div></section>%s' % (
        pts, fq) + contact_section("Work with us", "Ask for a media kit or send a brief. We usually reply within a day.")
    about = {"@type": "AboutPage", "@id": SITE + "/about#about", "url": SITE + "/about", "about": {"@id": SITE + "/#org"}}
    write_page("/about", d["title"], d["description"], body, [about, cld, fld], priority="0.6")


def build_pages():
    for k in ("hugo", "kevin", "preston"):
        profile_page(k)
    creators_page()
    brands_page()
    ugc_page()
    about_page()


PAGE_CSS = """
/* interior pages */
.crumbs{font-size:13px;color:var(--label);margin-bottom:32px}.crumbs a{text-decoration:none}.crumbs a:hover{text-decoration:underline}
.pg-hero{padding:48px 0 72px}
.pg-grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:56px;align-items:center}
.pg-hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:32px}
.pg-photo img{border-radius:var(--r);aspect-ratio:4/5;object-fit:cover;width:100%}
.pg-sec{padding:0 0 96px}
.pg-two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:start}
.pg-sec h2{margin-bottom:24px}
.facts{border-top:1px solid var(--line)}
.facts div{display:grid;grid-template-columns:150px minmax(0,1fr);gap:16px;padding:14px 0;border-bottom:1px solid var(--line)}
.facts.wide div{grid-template-columns:minmax(0,1fr) 220px}
.facts dt{font-size:14px;color:var(--label)}.facts dd{font-size:16px;font-weight:500}
.facts dd a{color:var(--blue)}
.hl{list-style:none;display:flex;flex-direction:column;gap:12px}
.hl li{position:relative;padding-left:28px;color:var(--text-2)}
.hl li::before{content:"\\2713";position:absolute;left:0;top:0;color:var(--blue);font-weight:700}
.hl li a{color:var(--text)}
.mt{margin-top:32px;margin-bottom:12px}
.chips{list-style:none;display:flex;flex-wrap:wrap;gap:8px}
.chips li{font-size:14px;font-weight:600;background:#F4F4F5;border-radius:999px;padding:6px 12px}
.gal{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px}
.gal img{border-radius:8px;aspect-ratio:4/5;object-fit:cover;width:100%;background:#18181B}
.gal figcaption{font-size:14px;margin-top:8px;line-height:1.35}.gal figcaption b{display:block}.gal figcaption span{color:var(--text-2)}
.cr .bd h3 a{text-decoration:none}.cr .bd h3 a:hover{text-decoration:underline}
.cr .bd p{font-size:15px;color:var(--text-2)}
.cr .bd p.fol{font-size:16px;color:var(--text)}.cr .bd p.fol b{font-weight:700}
.k{font-size:13px;color:var(--label)}
.logo-grid{list-style:none;display:flex;flex-wrap:wrap;gap:24px 48px;align-items:center}
.logo-grid img{height:28px;width:auto;max-width:140px;object-fit:contain;filter:grayscale(1) brightness(0);opacity:.6}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r);background:var(--card)}
.tbl table{width:100%;border-collapse:collapse;font-size:15px}
.tbl th,.tbl td{text-align:left;padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:top}
.tbl thead th{font-size:13px;color:var(--label);font-weight:600}
.tbl tbody th{font-weight:600}.tbl tr:last-child th,.tbl tr:last-child td{border-bottom:0}
.steps.nonum .st::before{content:none}
@media(max-width:900px){.pg-grid,.pg-two{grid-template-columns:minmax(0,1fr);gap:32px}.pg-photo{max-width:360px}.gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:520px){.facts div{grid-template-columns:minmax(0,1fr);gap:4px}.facts.wide div{grid-template-columns:minmax(0,1fr)}}
"""


def indexnow_ping(paths):
    """Tell Bing, Yandex and other IndexNow engines about changed URLs. Run after a deploy: python3 tools/build.py --ping"""
    import urllib.request
    body = json.dumps({"host": "www.mana-mgmt.com", "key": INDEXNOW_KEY, "keyLocation": SITE + "/%s.txt" % INDEXNOW_KEY,
                       "urlList": [SITE + p for p in paths]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=20) as r:
        print("IndexNow", r.status, len(paths), "urls")


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
    lines += ["", "## Pages", "- Creators: %s/creators" % SITE] + ["- %s: %s/creators/%s" % (c["name"], SITE, c["slug"]) for c in C.CREATORS] + [
        "- For brands: %s/brands" % SITE, "- UGC creators in Australia: %s/ugc-creators-australia" % SITE, "- About: %s/about" % SITE]
    lines += ["", "## Contact", "- Email: shei@mana-mgmt.com", "- Media kit or brief: %s/#contact" % SITE,
              "- Instagram: https://www.instagram.com/manamgmt/", ""]
    return "\n".join(lines)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copytree(SRC / "assets/img", OUT / "assets/img")
    shutil.copytree(SRC / "assets/brand", OUT / "assets/brand")
    shutil.copytree(SRC / "assets/logos", OUT / "assets/logos")
    if (SRC / "assets/og").exists():
        shutil.copytree(SRC / "assets/og", OUT / "assets/og")
    for name in ("favicon.svg", "apple-touch-icon.png"):
        if (SRC / "assets/brand" / name).exists():
            shutil.copy(SRC / "assets/brand" / name, OUT / name)
    (OUT / "assets/site.css").write_text(CSS.strip() + "\n" + PAGE_CSS.strip() + "\n")
    (OUT / "assets/site.js").write_text(JS.strip() + "\n")
    (OUT / "index.html").write_text(home())
    (OUT / "404.html").write_text(not_found())
    (OUT / "robots.txt").write_text(robots())
    build_pages()
    (OUT / "sitemap.xml").write_text(sitemap(["/"] + [p for p, _ in PAGES]))
    (OUT / ("%s.txt" % INDEXNOW_KEY)).write_text(INDEXNOW_KEY)
    if "--ping" in sys.argv:
        indexnow_ping(["/"] + [p for p, _ in PAGES])
    (OUT / "llms.txt").write_text(llms())
    print("built", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file()))


if __name__ == "__main__":
    main()
