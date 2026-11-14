# MANA website (v2)

Source for **www.mana-mgmt.com**. Static pages built by a small Python script and served by Vercel.

| Path | What it is |
|---|---|
| `tools/content.py` | All copy and facts: creators, case studies, brands, FAQ. Figures only from the vault's Facts files and media kits. **No prices.** |
| `tools/build.py` | Turns content into `public/`: pages, CSS, JS, `robots.txt`, `sitemap.xml`, `llms.txt`, structured data |
| `src/assets/` | Photos, logo files and the share image |
| `public/` | The built site that Vercel serves. Never edit by hand; rebuild instead. |
| `vercel.json` | Serve `public/`, clean URLs, caching |

```sh
python3 tools/build.py                      # rebuild public/
cd public && python3 -m http.server 8765    # preview at http://localhost:8765
```

Design follows the vault's `MANAMGMT/(SOP) Design Rules.md` (neutral, MANA blue about 10%, Archivo, sentence case); the logo follows `(SOP) Branding.md`.
Leads come in through the form, which posts to https://manacreators.com/site-lead (our own endpoint since 15 Nov 2026, was Formspree `mvzekrgq`): saved in the MANA Creators DB (`site_leads`), emailed to shei@manacreators.com with Reply-To set to the sender, and pinged to Anam on Telegram. Only mana-mgmt.com origins may post.

Pushing to `main` deploys to production. Work on a branch; merge only on Anam's go.
