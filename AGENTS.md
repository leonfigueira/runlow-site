# AGENTS.md — site-shared (the runlow-site repo)

Read `../AGENTS-CORE.md` first (absolute: `/Users/leon/Desktop/Projects/AGENTS-CORE.md`). That is
the working method: understand, plan, build, check against an objective gate, fix, record. This
file adds the specifics, and the hard constraints below OVERRIDE the default "keep going"
posture. When in doubt here, stop and ask Leon.

## This is the single most sensitive repo Leon owns. Read this before touching anything.

- GitHub repo: `github.com/leonfigueira/runlow-site` (remote `origin`, branch `main`).
- Live URL: `https://leonfigueira.github.io/runlow-site/` (GitHub Pages, served from `main`).
- This one repo serves the LIVE privacy and support pages for EVERY app Leon ships (Runlow,
  Fieldmark, GainScout, Gridsong, Recast, Recomp, Refast, Reprompt, Squarecut, ADHD Days), PLUS
  the JSON feeds that already-shipped apps poll on customers' devices:
  - `notices/v1.json` — the in-app developer-notices feed. Shipped apps fetch this on a timer.
  - `recipes/v1.json` — a feed consumed by a shipped app.
  - `data/gainsites-snapshot-v1.json` — a data snapshot.
- The Pages URL above is COMPILED INTO apps that are already on customers' devices. There is no
  redirect layer. If the URL changes, those apps break in the field and cannot be fixed without a
  new App Store release.

## Never do these (they break live apps in customers' hands)

- NEVER rename or move this repo, and never change its default branch. The URL is the contract.
- NEVER give it a custom domain and never add a `CNAME` file. It must stay on
  `leonfigueira.github.io/runlow-site/`. There is deliberately no CNAME today.
- NEVER break, malform, or delete `notices/v1.json`, `recipes/v1.json`, or the `data/` snapshot.
  A broken JSON body is a broken feed for every device polling it. Validate JSON before any commit.
- NEVER change the shape (schema) of a feed without checking what shipped apps expect. `notices`
  entries use `id`, `severity`, `title`, `body`, `platforms`, `appVersions` (`min`/`max`),
  `starts`, `ends`, `dismissible`, `pinned`. Keep the schema; only Leon decides schema changes.
- Publishing a notice is CUSTOMER-FACING. Every notice body is copy that appears inside the app
  on real devices. Leon drafts and approves the exact wording before it is committed or pushed.
  Do not write, edit, or time-schedule a notice on your own initiative.

## Build / structure (verified on disk)

- Static HTML, no framework, served as-is by Pages. Editing a `.html` file is the whole edit.
- `build-support.py` regenerates the localized Runlow support pages: English at `support.html`,
  the rest at `support/<lang>.html` (de, es, fr, it, nl, pt-BR, ja, zh-Hans, ko). Run
  `python3 build-support.py` after changing the support template or copy, then review the output.
- Per-app pages follow `<'app'>.html`, `<'app'>-privacy.html`, `<'app'>-support.html`.

## Web verification before any publish

- Preview locally (e.g. `python3 -m http.server` from the repo root) and open the pages you
  changed. Check the browser console and network tab: no 404s, no JS errors, no broken links.
- Validate every JSON feed you touched: `python3 -m json.tool notices/v1.json` (and the same for
  `recipes/v1.json`, `data/…`). It must parse. Diff against the previous version and confirm you
  only changed what you meant to.
- Check that internal links and asset paths (`assets/…`) still resolve. No broken pages.

## Publishing rule

Committing to `main` publishes to live immediately for all apps and all customers. Do NOT commit,
push, or deploy. Prepare the change, verify it, show Leon the diff and any notice copy, and let
Leon push. Every publish and every piece of customer-facing copy is drafted and shown to Leon
first. No em dashes.
