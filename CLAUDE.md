# Instructions for LLM agents

This repo is an offline mirror of the CrowdChange Help Center (https://ch.crowdchange.help/cnak), used as
reference material for integrating CrowdChange with our CRM. Treat it as **read-only source material**: don't
edit files under `docs/pages/` by hand, because `scripts/scrape.py` regenerates them.

## How to find things

1. **Browse:** `docs/INDEX.md` is the full navigation tree with one-line summaries. `llms.txt` is the same list, flat.
2. **By topic:** `docs/TAGS.md` groups pages by tag. For integration work, start with its `crm-relevant` section.
3. **Search:** grep `docs/pages/*.md`. Front matter fields can be grepped directly, e.g.
   `grep -l "reporting-and-data" docs/pages/*.md` or `grep -l "crm_relevant: true" docs/pages/*.md`.
4. **Structured:** `manifest.json` has every page's metadata (tags, parent/children, type, dates, file path).
5. **Everything at once:** `llms-full.txt` is all pages concatenated (~100K tokens). Load it only when you
   really need the whole corpus.

## Conventions

- One page per file: `docs/pages/<slug>.md`, where the slug matches the live URL `https://ch.crowdchange.help/cnak/<slug>`.
- Every page opens with YAML front matter (see README.md for the fields). `parent`/`children` are slugs, so
  follow them to read related pages.
- Links between pages are relative (`other-page.md`). Images point to `../assets/<slug>/<file>`. Most images are
  UI screenshots, and their alt text is only a filename, so the step text around them carries the meaning.
- Markdown escapes such as `\&` appear in the text. Read them as the plain character.

## When answering questions

- Cite the page you used by its `title` and `source_url`, so a person can check the live site.
- Mention `last_modified` when the answer depends on UI details. The mirror can be out of date, and the live
  site is authoritative.
- These docs cover the CrowdChange **UI for charity staff and fundraisers**. They don't document an API,
  webhooks or CRM connectors. Say so plainly rather than guessing. For data questions, rely on what the
  reports, CSV imports and exports, and record-level pages (donations, registrations, tickets, custom questions,
  recurring donations, refunds, receipts) actually describe.
- `tags` and `crm_relevant` are keyword heuristics. Use them to narrow a search, not as ground truth.
