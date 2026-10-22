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
  --bg:#FAFAFA;--card:#FFFFFF;--line:#E4E4E7;
  --f:'Archivo',system-ui,-apple-system,'Segoe UI',sans-serif;--fd:'Anton',Impact,sans-serif;
  --maxw:1280px;--pad:clamp(16px,4vw,48px);
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:72px}
body{background:var(--bg);color:var(--text);font:400 16px/1.6 var(--f);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:inherit}
img{display:block;max-width:100%;height:auto}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 var(--pad)}
.skip{position:absolute;left:-9999px}.skip:focus{left:16px;top:16px;background:var(--card);padding:8px 12px;z-index:50}
:focus-visible{outline:2px solid var(--blue);outline-offset:3px}

/* lockup: the one spaced-caps brand mark allowed */
.lockup{display:inline-flex;align-items:center;gap:10px;text-decoration:none}
.lk-t{display:flex;flex-direction:column;line-height:1}
.lk-w{font:400 22px/1 var(--fd);letter-spacing:.14em}
.lk-s{font:600 9px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;margin-top:4px}

/* header */
.hd{position:sticky;top:0;z-index:20;background:rgba(250,250,250,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.hd .wrap{display:flex;align-items:center;justify-content:space-between;height:68px;gap:24px}
.hd nav{display:flex;gap:32px}
.hd nav a{font-size:15px;font-weight:500;text-decoration:none;color:var(--text)}
.hd nav a:hover{text-decoration:underline;text-underline-offset:4px}
@media(max-width:640px){.hd nav{gap:20px}.hd nav a.nl{display:none}}

/* links and the one real button */
.go{font-weight:600;font-size:16px;text-decoration:underline;text-underline-offset:5px;text-decoration-thickness:1.5px;text-decoration-color:var(--blue)}
.go:hover{color:var(--blue)}
.btn{display:inline-flex;align-items:center;justify-content:center;font:600 16px/1 var(--f);padding:16px 24px;border:0;border-radius:4px;background:var(--blue);color:#fff;cursor:pointer}
.btn:hover{background:var(--blue-deep)}

/* type */
h1{font-weight:700;font-size:clamp(39px,7vw,76px);line-height:1;letter-spacing:-.035em}
h2{font-weight:700;font-size:clamp(25px,3.2vw,39px);line-height:1.1;letter-spacing:-.025em}
h3{font-weight:700;font-size:20px;line-height:1.25;letter-spacing:-.01em}
.lede{font-size:clamp(18px,2vw,20px);line-height:1.5;color:var(--text-2);max-width:44ch}
.k{font-size:13px;color:var(--label)}
section{padding:112px 0}
@media(max-width:720px){section{padding:72px 0}}

/* hero */
.hero{padding:56px 0 48px}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:48px;align-items:end}
.hero .lede{margin-bottom:6px}
.hero .go{display:inline-block;margin-top:20px}
@media(max-width:860px){.hero .wrap{grid-template-columns:minmax(0,1fr);gap:24px}}

/* roster: big portraits */
.roster{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,24px)}
.cr{display:flex;flex-direction:column}
.cr .ph{display:block;aspect-ratio:4/5;overflow:hidden;background:#E4E4E7}
.cr .ph img{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.cr .ph:hover img{transform:scale(1.03)}
.cr h3{font-size:clamp(25px,2.6vw,31px);letter-spacing:-.025em;margin-top:16px}
.cr .niche{color:var(--text-2);font-size:16px;margin-top:4px}
.cr .ln{display:flex;gap:20px;margin-top:12px;font-size:15px}
.cr .ln a{text-decoration:underline;text-underline-offset:4px;text-decoration-color:#A1A1AA}
.cr .ln a:hover{text-decoration-color:var(--text)}
@media(max-width:860px){.roster{grid-template-columns:minmax(0,1fr);gap:48px}}

/* work: grid of stills */
.sec-h{display:flex;justify-content:space-between;align-items:baseline;gap:24px;margin-bottom:32px;flex-wrap:wrap}
.work{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(12px,1.6vw,24px) clamp(12px,1.6vw,24px)}
.wk figure{margin:0}
.wk .im{aspect-ratio:4/5;overflow:hidden;background:#18181B}
.wk img{width:100%;height:100%;object-fit:cover}
.wk figcaption{margin-top:12px;font-size:15px;line-height:1.4}
.wk figcaption b{font-weight:600}
.wk figcaption span{display:block;color:var(--text-2)}
@media(max-width:860px){.work{grid-template-columns:repeat(2,minmax(0,1fr))}}

/* about */
.brandline{font-weight:600;font-size:clamp(22px,2.6vw,31px);line-height:1.3;letter-spacing:-.02em;max-width:38ch}
.brandline em{font-style:normal;color:var(--label)}
.proof{font-size:18px;color:var(--text-2);max-width:60ch;margin-top:24px}
.two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:48px;margin-top:80px;padding-top:32px;border-top:1px solid var(--line)}
.two p{color:var(--text-2);margin-top:12px;max-width:52ch}
.two .go{display:inline-block;margin-top:16px}
@media(max-width:720px){.two{grid-template-columns:minmax(0,1fr);gap:40px;margin-top:56px}}

/* faq: folded, for readers and AI tools */
.faq{margin-top:80px;max-width:820px}
.faq h2{margin-bottom:16px}
.faq details{border-bottom:1px solid var(--line);padding:18px 0}
.faq summary{font-weight:600;font-size:17px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-weight:400;font-size:22px;line-height:1;color:var(--label)}
.faq details[open] summary::after{content:"\2013"}
.faq details p{color:var(--text-2);margin-top:10px;max-width:68ch}

/* contact */
.contact .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:64px;align-items:start}
.contact .lede{margin-top:16px}
.contact .mail{display:inline-block;margin-top:24px;font-weight:600;font-size:clamp(20px,2.4vw,25px);text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:2px;text-decoration-color:var(--blue)}
.field{margin-bottom:20px}
.field label{display:block;font-size:14px;font-weight:600;margin-bottom:6px}
.field label span{font-weight:400;color:var(--label)}
.field input,.field select,.field textarea{width:100%;font:400 16px/1.4 var(--f);color:var(--text);background:transparent;border:0;border-bottom:1.5px solid #A1A1AA;border-radius:0;padding:10px 0}
.field select{appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2352525B' stroke-width='1.6' fill='none'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 2px center;padding-right:24px}
.field textarea{min-height:96px;resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-bottom-color:var(--blue)}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.hp{position:absolute;left:-9999px}
.form .btn{margin-top:8px}
.form .note{font-size:13px;color:var(--label);margin-top:12px}
.status{display:none;margin-top:16px;font-size:15px;padding:12px 14px}
.status.ok{display:block;background:var(--blue-tint);color:var(--blue)}
.status.err{display:block;background:#FDECEA;color:#A1271D}
@media(max-width:860px){.contact .wrap{grid-template-columns:minmax(0,1fr);gap:40px}}
@media(max-width:520px){.row2{grid-template-columns:minmax(0,1fr);gap:0}}

/* footer: a lockup surface, so full blue is allowed here */
.ft{background:var(--blue);color:#fff;padding:56px 0 32px}
.ft .top{display:flex;justify-content:space-between;gap:40px;flex-wrap:wrap}
.ft .blurb{max-width:40ch;font-size:15px;margin-top:16px}
.ft .cols{display:flex;gap:56px;flex-wrap:wrap}
.ft h4{font-size:13px;font-weight:600;margin-bottom:12px}
.ft .cols a{display:block;color:#fff;text-decoration:none;font-size:15px;margin-bottom:8px}
.ft .cols a:hover{text-decoration:underline}
.ft .bot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:48px;padding-top:24px;border-top:1px solid rgba(255,255,255,.25);font-size:13px}

/* 404 */
.nf{padding:120px 0;min-height:60vh}
.nf .lede{margin-top:24px}
.nf .go{display:inline-block;margin-top:24px;margin-right:24px}
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
    links = "".join('<a%s href="%s">%s</a>' % ("" if h.endswith("contact") else ' class="nl"', h, e(t)) for h, t in C.NAV)
    return """<header class="hd"><div class="wrap">
<a href="/" aria-label="MANA, home">{lk}</a>
<nav aria-label="Main">{links}</nav>
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
<button class="btn" type="submit">Send</button>
<div class="status" id="status" role="status" aria-live="polite"></div>
<p class="note">We reply to every brand and creator, usually within a day. No mailing lists.</p>
</form>""".format(opts=opts)


def home():
    h = C.HOME
    roster = []
    for i, c in enumerate(C.CREATORS):
        roster.append("""<article class="cr" id="{slug}">
<a class="ph" href="{ig}" rel="noopener" aria-label="{name} on Instagram"><img src="/assets/img/{slug}.webp" alt="{alt}" width="800" height="1000"{lazy}></a>
<h3>{name}</h3><p class="niche">{niche}</p>
<p class="ln"><a href="{ig}" rel="noopener">{handle}</a><a href="#contact" data-need="kit-{key}">Media kit</a></p>
</article>""".format(slug=c["slug"], ig=c["instagram"], name=e(c["name"]), alt=e(c["photo_alt"]), niche=e(c["niche"]),
                     handle=e(c["handle"]), key=c["key"], lazy="" if i < 3 else ' loading="lazy"'))
    work = "".join("""<div class="wk"><figure><div class="im"><img src="/assets/img/{img}" alt="{alt}" width="640" height="800" loading="lazy"></div>
<figcaption><b>{brand}</b> · {creator}<span>{what}</span></figcaption></figure></div>""".format(
        img=w["image"], alt=e(w["alt"]), brand=e(w["brand"]), creator=e(w["creator"]), what=e(w["what"])) for w in C.WORK)
    brands = ", ".join(C.BRANDS[:-1]) + " and " + C.BRANDS[-1]
    faq = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in C.FAQ)

    body = """<main id="main">
<section class="hero"><div class="wrap">
<h1>{h1}</h1>
<div><p class="lede">{lede}</p><a class="go" href="#contact" data-need="kit-all">Get a media kit</a></div>
</div></section>

<section id="creators" style="padding-top:0" aria-label="Creators"><div class="wrap">
<div class="roster">{roster}</div>
</div></section>

<section id="work" style="padding-top:0"><div class="wrap">
<div class="sec-h"><h2>Work</h2><span class="k">Recent campaigns and reels from the roster</span></div>
<div class="work">{work}</div>
</div></section>

<section id="about" style="padding-top:0"><div class="wrap">
<p class="brandline"><em>Our creators have made work for</em> {brands}.</p>
<p class="proof">{proof}</p>
<div class="two">
<div><h3>{bh}</h3><p>{bp}</p><a class="go" href="#contact" data-need="brief">Send a brief</a></div>
<div><h3>{ch}</h3><p>{cp}</p><a class="go" href="#contact" data-need="creator">Apply for management</a></div>
</div>
<div class="faq" id="faq"><h2>Questions</h2>{faq}</div>
</div></section>

<section class="contact" id="contact" style="padding-top:0"><div class="wrap">
<div><h2>{contact_h}</h2><p class="lede">{contact_sub}</p><a class="mail" href="mailto:shei@mana-mgmt.com">shei@mana-mgmt.com</a></div>
{form}
</div></section>
</main>
""".format(h1=e(h["h1"]), lede=e(h["lede_html"]), roster="".join(roster), work=work, brands=e(brands), proof=e(h["proof"]),
           bh=e(h["brands_h"]), bp=e(h["brands_p"]), ch=e(h["creators_h"]), cp=e(h["creators_p"]), faq=faq,
           contact_h=e(h["contact_h"]), contact_sub=e(h["contact_sub"]), form=lead_form())
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
<a class="go" href="/">Go to the home page</a><a class="go" href="/#contact">Contact us</a>
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
        lines.append("- %s × %s: %s" % (w["brand"], w["creator"], w["what"]))
    lines += ["", C.HOME["proof"], "", "Brands the creators have made work for: " + ", ".join(C.BRANDS) + ".", "", "## Contact", "- Email: shei@mana-mgmt.com", "- Media kit or brief: %s/#contact" % SITE,
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
