# MANA — website (v1)

One-page site for **mana-mgmt.com**. Built to the locked MANA brand system
(IKB `#002FA7` · bone `#F5F2EA` · Anton / Archivo / IBM Plex Mono · the woven four-ring mark).
See `Mesh/MANAMGMT/(SOP) Branding.md` for the brand rules this follows.

## What's here

| File | What it is |
|---|---|
| `index.html` | The entire site — self-contained (inline CSS + JS, no build step). |
| `favicon.svg` | The mark on an IKB tile, for the browser tab. |

Sections: hero (the mark literally weaves itself in on load) → what-we-do + stats →
roster (Hugo Zbor, Kevin Chiang) → brand marquee → "Work With Us" contact form → footer.
All content is real and pulled from the vault. Fonts load from Google Fonts, so keep online.

## View it locally

Just open `index.html` in a browser (double-click). Everything works offline except the
web fonts and the form submission.

## ⚠️ Before it goes live — connect the contact form (2 min)

The form is wired to **Formspree** but needs your form ID:

1. Go to https://formspree.io → sign up (free tier is fine) with **shei@mana-mgmt.com**.
2. Create a new form → copy its ID (looks like `xdorwknp` — the bit after `/f/`).
3. In `index.html`, find this line (near the bottom, in the `<script>`):
   ```js
   const FORMSPREE_ID = "REPLACE_WITH_FORMSPREE_ID";
   ```
   Replace `REPLACE_WITH_FORMSPREE_ID` with your ID and save.

Until then the form shows a friendly "email us directly" message instead of failing silently.
Submissions land in your Formspree inbox **and** get emailed to you.

## Going live at mana-mgmt.com

The site is a single static file — it can be hosted anywhere:

- **Fastest / free:** drag the `mana-mgmt` folder onto **Netlify Drop** (app.netlify.com/drop),
  or push to a GitHub repo and enable **Cloudflare Pages / GitHub Pages** — then point the
  `mana-mgmt.com` DNS at it (the host gives you the records). Gets you real **HTTPS**.
- **On the existing VPS** (`170.64.167.205`): drop `index.html` + `favicon.svg` into a new
  nginx route and point the domain's A record at the box — see
  `~/Downloads/(SOP) VPS Deployment — for Claude.md`. Note the VPS is **HTTP-only**; a
  static host (Netlify/Cloudflare) is the better home for the public domain because it's HTTPS.

Once the site is live on HTTPS, also move the email-signature banner image there
(currently `http://170.64.167.205/mana-sig.png`) — see `(SOP) Branding.md` §6.

## Editing

- **Brand facts** (creators, stats, brands): all in the HTML markup — search for `HUGO ZBOR`,
  `KEVIN CHIANG`, or the `marquee` blocks. Keep the brand-wall names to real, closed partners.
- **Colours / type:** the `:root` CSS variables at the top.
- **Motion** respects `prefers-reduced-motion` (animations off for users who ask for that).

*v1 — 2026-07-17. No logo animation beyond the hero weave, per (SOP) Branding §6 ("Website v1: typographic").*
