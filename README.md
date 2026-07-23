# Company Dossiers

Living research dossiers on the companies and products that matter most this decade — product sense, strategy, unit economics, moats, and the questions that would change the read. Built once, updated as news and earnings arrive.

Site: https://abhitsian.github.io/company-dossiers/

## Structure

- `source/{Company}/*.md` — the actual dossier markdown, the real source of truth.
- `build.py` — generator: parses the dossier markdown structure into styled HTML.
- `companies/{company}/` — generated site pages (one hub + one page per dossier).
- `css/style.css`, `js/nav.js` — shared design system and site chrome.

## Regenerating after a dossier changes

Edit the source markdown under `source/{Company}/`, then:

```
python3 build.py
```

Regenerates every page from scratch — fast, deterministic, no external dependencies.

## Methodology

See [`framework.html`](framework.html) once deployed, or the dossier template conventions this content follows: a 15-section arc (Facts → Insights → Differentiators → Plays), moats scored via the 7 Powers framework, needs-based segmentation, and a generative eigenquestion process for surfacing the pivotal open question per company.
