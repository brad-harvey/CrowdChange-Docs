# CrowdChange-Docs

An offline, LLM-friendly mirror of the **CrowdChange Help Center** (charity / non-admin space):
<https://ch.crowdchange.help/cnak>

It's the reference knowledge base for a CrowdChange ↔ CRM integration project. Every page in the help center's
left navigation is saved as Markdown with YAML metadata, along with its screenshots.

> Unofficial copy. All content © CrowdChange. The live site is authoritative. Check `last_modified` and
> `retrieved` in each page's front matter to see how current it is.

## Layout

```
CLAUDE.md / AGENTS.md   Instructions for LLM agents using this repo (read first)
llms.txt                llmstxt.org-style index: one line per page with a summary
llms-full.txt           Every page concatenated into one file (~390 KB) for whole-corpus context
manifest.json           Machine-readable metadata for every page (tags, hierarchy, dates, file path)
docs/INDEX.md           Navigation tree, same order and nesting as the site's left nav
docs/TAGS.md            Pages grouped by topic tag, plus the "crm-relevant" list
docs/pages/<slug>.md    One file per help-center page (slug = the live URL's last segment)
docs/assets/<slug>/     Screenshots for that page, referenced by relative links
scripts/scrape.py       The scraper that rebuilds all of the above
```

## Page format

Each page begins with YAML front matter:

| Field | Meaning |
|---|---|
| `title`, `slug`, `source_url` | Page identity; `source_url` is the live page |
| `nav_path`, `nav_order`, `parent`, `children` | Position in the left-nav hierarchy (`parent`/`children` are slugs) |
| `page_type` | `how-to`, `concept` ("How X Works"), `reference`, `troubleshooting`, `navigation` |
| `tags` | Topic tags (keyword-derived), e.g. `donations`, `ticketing`, `reporting-and-data` |
| `crm_relevant` | `true` if the page is about data or records a CRM integration probably cares about (heuristic) |
| `description` | The site's own summary |
| `last_modified` | When CrowdChange last edited the page |
| `retrieved` | When this mirror was taken |
| `word_count` | Text size, excluding images |

Links between help pages are rewritten to relative `.md` links, so they work offline and in GitHub.
That includes old Confluence-style links and the site's bold "related tutorials" lists.

## Refreshing

```sh
uv run scripts/scrape.py
```

Run it from the repo root. If your machine stops Python from opening the script file, pipe it in:
`uv run --with pyyaml python - < scripts/scrape.py`. The scraper uses the site's own Scroll Sites endpoints
(`/cnak/__pagetree.json`, `/llms.txt`, the sitemap, and `/<page>.md`), so nothing is parsed out of HTML except
the metadata tags. Commit the result, and `git diff` shows exactly what CrowdChange changed.

## Coverage note

This help center is written for charity staff and fundraisers using the CrowdChange UI. It does **not**
document an API, webhooks, or CRM connectors; the only third-party integration it describes is Strava. For a
CRM integration, the useful material is the reports and exports, CSV imports, and the data model you can infer
from donations, registrations, tickets, custom questions, recurring donations, refunds and receipts. Start with the
`crm-relevant` section of [docs/TAGS.md](docs/TAGS.md). API or integration documentation will need to come from
CrowdChange directly. Add it under `docs/vendor/` so it sits alongside this mirror.
