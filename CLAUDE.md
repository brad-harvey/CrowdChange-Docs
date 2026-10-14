# Instructions for LLM agents

This repo is an offline mirror of CrowdChange's documentation, used as reference material for integrating CrowdChange
with our CRM. It has two collections:

- **`docs/help-center/`**: the charity Help Center (https://ch.crowdchange.help/cnak). It covers *what features do and
  how staff use them in the UI*: fundraisers, donations, tickets, registrations, teams/P2P, reports, receipts and refunds.
- **`docs/api/`**: the API & developer docs (https://apidoc.crowdchange.dev). It covers *how to get data in and out
  programmatically*: REST endpoints, webhooks and event payloads, widgets and analytics pixels.

Treat everything under `docs/` and `llms.txt` as **read-only source material**. `scripts/scrape.py` regenerates it,
so hand edits will be overwritten. Put our own notes, mappings and designs somewhere else, e.g. a top-level `notes/` folder.

## How to find things

1. **Entry point:** `llms.txt` lists every page in both collections with a one-line summary. API entries include
   `METHOD /path`.
2. **Trees:** `docs/help-center/INDEX.md` follows the help center's left nav. `docs/api/INDEX.md` follows the API
   sidebar and ends with an **endpoint quick-reference table** (method, path, surface, auth).
3. **By topic, across both:** `docs/TAGS.md`. Each tag lists help-center pages and API pages separately. For example,
   `offline-donations` shows the how-to articles next to the offline-transaction endpoints. Its `crm-relevant` section
   is the best starting list for integration work.
4. **Search:** grep `docs/*/pages/**/*.md`. Front matter fields can be grepped directly:
   - `grep -rl "endpoint: POST" docs/api/pages`
   - `grep -rl "api_surface: server-side" docs/api/pages`
   - `grep -rl "crm_relevant: true" docs`
5. **Structured:** `docs/<collection>/manifest.json` holds every page's metadata.
6. **Whole corpus:** `docs/<collection>/llms-full.txt`. Each is roughly 100K tokens, so load it only when you
   really need everything.

## Key API facts (details in `docs/api/pages/api-reference/overview.md`)

- **Two surfaces.** Server-side `/v2/private/...` is server-to-server only, returns richer data and allows writes.
  Client-side `/v2/client/...` is safe to call from public pages.
- **Auth.** Send the API key in the `Authorization` header. User-specific endpoints (`/v2/private/user/...`) also need a
  user token from Sign In, sent in the `auth-token` header or as the `token` param.
- **Base URLs.** Production US `https://api.crowdchange.co`, Production CA `https://api.crowdchange.ca`,
  Development `https://api.crowdchange.dev`.
- **Webhooks** (`docs/api/pages/api-reference/server-side/webhooks/`) are the main option for pushing changes to the CRM.
  `event-payloads.md` documents the JSON sent for each event.
- **Transactions.** `GET /v2/private/transactions` is the bulk pull for donations and payments, by date window or payout.

## Conventions

- **Help-center files** are `docs/help-center/pages/<slug>.md`, where the slug matches the live URL. `parent`/`children`
  in the front matter are slugs.
- **API files** mirror the site's URL path: `docs/api/pages/<path>.md`. Endpoint pages have `endpoint`,
  `http_method`, `endpoint_path`, `api_surface` and `auth` in the front matter, and repeat them under the H1.
- **API schemas** are nested lists in the form `` - `field` (type, location, **required**) — description ``.
  Indentation shows nesting, i.e. the properties of an object or of array items.
- **Links** are relative and work offline. Help-center screenshots carry little meaning (their alt text is just a
  filename), so rely on the step text around them.
- **Escapes.** Markdown escapes such as `\&` appear in help-center text. Read them as the plain character.

## When answering questions

- **Cite your sources.** Give the page's `title` and `source_url` so a person can check the live site.
- **Use both collections.** For integration questions, pair the API page (the field or endpoint) with the help-center
  page that explains the business meaning, e.g. what "covered fees" or "offline donation" means for staff.
- **Watch for drift.** Mention `retrieved` (and `last_modified` for help-center pages) when details matter. The mirror
  can lag the live sites, and the live sites are authoritative.
- **Don't guess.** If an endpoint, field or event isn't documented here, say so. Don't infer one from naming patterns.
- **Treat the metadata as hints.** `tags` and `crm_relevant` are keyword heuristics for narrowing a search, not
  ground truth.
