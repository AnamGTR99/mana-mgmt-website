#!/usr/bin/env python3
"""Renders the 1200x630 share images into src/assets/og/ with headless Chrome.
Usage: python3 tools/og.py   (needs Google Chrome; run when titles or photos change, then rebuild)"""
import os, pathlib, shutil, subprocess, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src/assets"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CARDS = {
    "creators": ("Australian content creators, managed by MANA.", "Hugo Zbor, Kevin Chiang and Preston Young.", ["hugo-zbor", "kevin-chiang", "preston-young"]),
    "hugo-zbor": ("Hugo Zbor", "Creative director. Green-screen concept films for Converse, ASICS and Named Collective.", ["hugo-zbor"]),
    "kevin-chiang": ("Kevin Chiang", "Architecture and design creator. 928K+ monthly views, 92% from non-followers.", ["kevin-chiang"]),
    "preston-young": ("Preston Young", "Lifestyle and self-growth creator. 1.86M views in 90 days.", ["preston-young"]),
    "brands": ("Work with Australian content creators.", "Briefs, scope, usage rights and posting, handled by MANA.", ["hugo-zbor", "kevin-chiang", "preston-young"]),
    "ugc": ("UGC creators in Australia.", "Videos for your channels and ads, with usage agreed up front.", ["kevin-chiang", "preston-young"]),
}

TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1200px;height:630px;overflow:hidden}
body{background:#FAFAFA;font-family:Archivo,sans-serif;color:#0A0A0A;display:grid;grid-template-columns:%(lw)dpx 1fr}
.l{padding:64px 0 56px 72px;display:flex;flex-direction:column}
.lk{display:flex;align-items:center;gap:14px}.lk img{width:44px;height:44px}
.lk b{font:400 32px/1 Anton;letter-spacing:.14em;display:block}.lk small{display:block;font:600 11px/1 Archivo;letter-spacing:.2em;color:#52525B;margin-top:6px}
h1{font-weight:700;font-size:%(fs)dpx;line-height:1.05;letter-spacing:-.03em;margin-top:auto}
p{font-size:22px;line-height:1.4;color:#52525B;margin-top:18px;max-width:30ch}
.bar{width:64px;height:6px;background:#002FA7;border-radius:3px;margin-top:28px}
.r{display:flex;gap:12px;padding:40px 48px 40px 24px;align-items:center;justify-content:flex-end}
.r img{width:%(iw)dpx;aspect-ratio:4/5;object-fit:cover;border-radius:14px}
</style></head><body>
<div class="l"><div class="lk"><img src="mark-blue.svg"><span><b>MANA</b><small>TALENT MANAGEMENT</small></span></div>
<h1>%(t)s</h1><p>%(s)s</p><div class="bar"></div></div>
<div class="r">%(imgs)s</div></body></html>"""


def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="og-", dir=os.environ.get("TMPDIR")))
    shutil.copy(SRC / "brand/mark-blue.svg", tmp)
    for f in (SRC / "img").glob("*.webp"):
        shutil.copy(f, tmp)
    (SRC / "og").mkdir(exist_ok=True)
    for name, (t, s, photos) in CARDS.items():
        one = len(photos) == 1
        html = TPL % dict(t=t, s=s, lw=720 if one else 600, fs=64 if one else 54, iw=360 if one else (160 if len(photos) == 3 else 240),
                          imgs="".join('<img src="%s.webp">' % p for p in photos))
        page = tmp / ("%s.html" % name)
        page.write_text(html)
        out = SRC / "og" / ("%s.png" % name)
        p = subprocess.Popen([CHROME, "--headless=new", "--no-first-run", "--disable-extensions", "--hide-scrollbars",
                              "--user-data-dir=%s" % (tmp / "prof"), "--allow-file-access-from-files", "--window-size=1200,630",
                              "--virtual-time-budget=4000", "--screenshot=%s" % out, page.as_uri()],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(40):
            if p.poll() is not None:
                break
            time.sleep(1)
        else:
            p.kill()
        print(name, out.exists())
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
