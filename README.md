# CrowdChange-Docs

An offline, LLM-friendly mirror of CrowdChange's two documentation sites:

| Collection | Source | What it covers | Pages |
|---|---|---|---|
| **Help Center** (`docs/help-center/`) | <https://ch.crowdchange.help/cnak> | Using the CrowdChange UI as a charity: fundraisers, donations, ticketing, registration, P2P/teams, reports, receipts | 96 |
| **API & Developer Docs** (`docs/api/`) | <https://apidoc.crowdchange.dev> | REST API (server-side and client-side), webhooks and event payloads, embeddable widgets, analytics/pixel integrations | 59 (47 endpoints) |

It's the reference knowledge base for a CrowdChange ↔ CRM integration project. The two collections answer
different questions:
- **Help Center:** what a feature does and how staff use it.
- **API docs:** how to read or write that data programmatically.

`docs/TAGS.md` puts both side by side by topic.

> Unofficial copy. All content © CrowdChange. The live sites are authoritative. Check `retrieved` (and, for help-center
> pages, `last_modified`) in each page's front matter to see how current it is.

## Layout

```
llms.txt                     Entry point (llmstxt.org format): every page in both collections, one line each
CLAUDE.md / AGENTS.md        Instructions for LLM agents using this repo
docs/
  TAGS.md                    Topic index across both collections, plus the "crm-relevant" list
  help-center/
    INDEX.md                 Navigation tree, same order and nesting as the site's left nav
    manifest.json            Metadata for every page (tags, hierarchy, dates, file path)
    llms-full.txt            Every help-center page in one file (~390 KB)
    pages/<slug>.md          One file per page (slug = last segment of the live URL)
    assets/<slug>/           Screenshots for that page
  api/
    INDEX.md                 Sidebar tree with METHOD /path per endpoint, plus an endpoint quick-reference table
    manifest.json            Metadata for every page, including http_method / endpoint_path / auth
    llms-full.txt            Every API page in one file
    pages/<site path>.md     One file per page, mirroring the site's URL path, e.g.
                             pages/api-reference/server-side/webhooks/event-payloads.md
    assets/                  Images used by the API docs
scripts/scrape.py            The scraper that rebuilds everything
```

## Page format

Every page starts with YAML front matter. Common fields:

| Field | Meaning |
|---|---|
| `title`, `slug`, `collection`, `source_url` | Page identity. `collection` is `help-center` or `api`; `source_url` is the live page |
| `nav_path`, `nav_order` | Position in the site's navigation |
| `page_type` | Help center: `how-to`, `concept`, `reference`, `troubleshooting`, `navigation`. API: `endpoint`, `reference`, `guide` |
| `tags` | Topic tags (keyword-derived), shared vocabulary across both collections. See `docs/TAGS.md` |
| `crm_relevant` | Heuristic flag for pages a CRM integration probably cares about |
| `description` | The site's own summary |
| `retrieved` | When this mirror was taken |
| `word_count` | Text size, excluding images |

Help-center pages also have `parent` / `children` (slugs) and `last_modified`.

API pages also have:
- `endpoint` (e.g. `GET /v2/private/transactions`), `http_method`, `endpoint_path`
- `api_surface` (`server-side` / `client-side`)
- `auth` (`API key`, or `API key + user token`)

Each endpoint page repeats the method, path, auth and base URLs in a short block under its title.

### How the API pages were converted

The API site is built with Mintlify, which writes parameters and response schemas as MDX components
(`<ParamField>`, `<ResponseField>`, `<Expandable>` …). GitHub and most LLM tooling either drop those tags or show
them raw. So they're converted to nested Markdown lists:

```
- `amount` (object) — Summary of collected funds for transaction.
  - `currency` (string) — Currency code. Allowed values: `CAD`, `USD`, `AUD`, `EUR`
  - `is_recurring` (boolean) — Is this a recurring transaction?
```

Parameters show their location (`path`, `query`, `body`) and whether they're **required**. The page Markdown doesn't
state each endpoint's method and path, so those come from the site's sidebar data. Response examples, callouts
(`> **Note:**`) and code samples are kept. The site's Canadian French translation isn't mirrored.

Links between pages are rewritten to relative `.md` links in both collections, so they work offline and on GitHub.

## Refreshing

```sh
uv run scripts/scrape.py              # both collections + shared indexes
uv run scripts/scrape.py api          # just the API docs (or: help-center)
```

Run it from the repo root. If your machine stops Python from opening the script file, pipe it in instead:
`uv run --with pyyaml python - [all|help-center|api] < scripts/scrape.py`.

The scraper only uses endpoints that the two platforms publish themselves:
- **Help Center (K15t Scroll Sites):** `__pagetree.json`, `llms.txt`, the sitemap and `<page>.md`
- **API docs (Mintlify):** `llms.txt`, the sitemap, `<page>.md` and the sidebar data

Commit the result, and `git diff` shows exactly what CrowdChange changed.
