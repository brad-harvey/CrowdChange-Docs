---
title: Find Personal Page
slug: api-reference/server-side/global-apis/post_v2-private-personal-pages-search
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/global-apis/post_v2-private-personal-pages-search
nav_path:
- API Reference
- Server Side APIs
- Global APIs
- Find Personal Page
nav_order: 15
page_type: endpoint
endpoint: POST /v2/private/personal-pages/search
http_method: POST
endpoint_path: /v2/private/personal-pages/search
api_surface: server-side
auth: API key
tags:
- peer-to-peer
- search
crm_relevant: true
description: Search CrowdChange personal fundraising pages server-side with rich filters and retrieve a paginated list with goal, raised, and owner details.
retrieved: '2026-10-14'
word_count: 760
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/global-apis/post_v2-private-personal-pages-search | Nav: API Reference > Server Side APIs > Global APIs > Find Personal Page | Mirrored 2026-10-14 -->

# Find Personal Page

> Search CrowdChange personal fundraising pages server-side with rich filters and retrieve a paginated list with goal, raised, and owner details.

**Endpoint:** `POST /v2/private/personal-pages/search`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `text` (string, body) — Search term.
- `page` (integer, body) — Page number. Default: `1`
- `limit` (integer, body) — Number of results to return. Default: `100`
- `sort` (string, body) — Key to sort by. Allowed values: `id`, `name`, `amount_raised`, `amount_goal`
- `direction` (string, body) — Direction of sorting. Allowed values: `asc`, `desc`
- `email` (string, body) — Email filter.
- `created_at` (object, body) — Page's creation date filter.
  - `<` (string, body)
  - `<=` (string, body)
  - `=` (string, body)
  - `>=` (string, body)
  - `>` (string, body)
- `amount_goal` (object, body) — Page's amount goal filter.
  - `<` (number, body)
  - `<=` (number, body)
  - `=` (number, body)
  - `>=` (number, body)
  - `>` (number, body)
- `amount_raised` (object, body) — Page's amount raised filter.
  - `<` (number, body)
  - `<=` (number, body)
  - `=` (number, body)
  - `>=` (number, body)
  - `>` (number, body)
- `fundraiser_id` (integer, body) — Campaign ID filter.
- `after_id` (integer, body) — Return teams after Page ID.
- `lang` (string, body) — API's locale. Allowed values: `en`, `fr`
- `filter_by_lang` (integer, body) — Filter pages only available in locale
- `tags` (string[], body) — List of fundraiser tags.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Personal page ID.
- `transaction_id` (integer) — Transaction ID (if was created through transaction).
- `name` (string) — Personal page name.
- `amount_goal` (number) — Goal amount.
- `amount_raised` (number) — Amount raised by the personal page.
- `amount_pledged` (number) — Pending offline donation amount attributed to the personal page. This amount is included in `amount_raised` until the offline donation is received.
- `amount_matched` (number) — Amount contributed by donation matching assigned directly to the personal page.
- `created_at` (string) — Creation date
- `language` (string) — Personal page language. Allowed values: `en`, `fr`
- `team` (object) — Team name that personal page belongs to (if assigned to a team).
  - `id` (integer) — Team ID.
  - `name` (string) — Team name.
  - `amount_goal` (number) — Team's goal amount.
  - `language` (string) — Team language. Allowed values: `en`, `fr`
  - `custom_data` (object[]) — List of custom questions and responses.
    - `field_id` (integer) — Custom field id.
    - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
    - `name` (string) — Custom field label.
    - `content` (string) — User's answer to custom field.
    - `field_custom_id` (string) — Custom ID.
    - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
  - `url` (string) — Full URL to team's page.
- `fundraiser` (object)
  - `id` (integer) — Fundraiser ID
  - `partner_id` (integer) — Site ID.
  - `fundraiser_template_id` (integer) — Template ID.
  - `name` (string) — Fundraiser name
  - `url` (string) — Fundraiser URL
  - `amount_goal` (number) — Fundraiser goal amount.
  - `user` (object)
    - `id` (integer) — Fundraiser owner's ID
    - `email` (string) — Fundraiser owner's email
    - `first_name` (string) — Fundraiser owner's first name
    - `last_name` (string) — Fundraiser owner's last name
    - `title` (string) — Fundraiser owner's title
    - `name` (string) — Fundraiser owner's name
  - `fundraiser_template` (object)
    - `id` (integer) — Template ID.
    - `name` (string) — Template Name.
  - `tags_list` (any[]) — Campaign tags.
- `user` (object)
  - `id` (integer) — Team captain's ID
  - `email` (string) — Team captain's email
  - `first_name` (string) — Team captain's first name
  - `last_name` (string) — Team captain's last name
  - `title` (string) — Team captain's title
  - `name` (string) — Team captain's name
- `custom_data` (object[]) — List of custom questions and responses.
  - `field_id` (integer) — Custom field id.
  - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
  - `name` (string) — Custom field label.
  - `content` (string) — User's answer to custom field.
  - `field_custom_id` (string) — Custom ID.
  - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
- `url` (string) — Full URL to personal page.

**Other responses**

| Status | Description |
| - | - |
| `400` | Bad Request |
| `403` | Forbidden |

**Response example:**

```json
[
  {
    "id": 1,
    "transaction_id": 12345678,
    "name": "John Snow",
    "amount_goal": 1000,
    "amount_raised": 550,
    "amount_pledged": 125,
    "amount_matched": 50,
    "created_at": "2022-03-01 00:00:00",
    "language": "en",
    "team": {
      "id": 1,
      "name": "Gala Night",
      "amount_goal": 10000,
      "language": "en",
      "custom_data": [
        {
          "field_id": 1001,
          "source_id": 11,
          "name": "Phone Number",
          "content": "555-123-4567",
          "field_custom_id": "ABC-123",
          "response_custom_id": "ABC-123"
        }
      ],
      "url": "https://demo.crowdchange.co/1/team/2"
    },
    "fundraiser": {
      "id": 101,
      "partner_id": 10,
      "fundraiser_template_id": 1,
      "name": "Gala Night",
      "url": "https://demo.crowdchange.co/101",
      "amount_goal": 1000,
      "user": {
        "id": 1,
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Snow",
        "title": "Mr.",
        "name": "John Snow"
      },
      "fundraiser_template": {
        "id": 1,
        "name": "Template"
      },
      "tags_list": [
        "tag1",
        "tag2"
      ]
    },
    "user": {
      "id": 1,
      "email": "john@example.com",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr.",
      "name": "John Snow"
    },
    "custom_data": [
      {
        "field_id": 1001,
        "source_id": 11,
        "name": "Phone Number",
        "content": "555-123-4567",
        "field_custom_id": "ABC-123",
        "response_custom_id": "ABC-123"
      }
    ],
    "url": "https://demo.crowdchange.co/1/page/2"
  }
]
```
