---
title: Find Campaign
slug: api-reference/server-side/global-apis/post_v2-private-fundraisers-search
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/server-side/global-apis/post_v2-private-fundraisers-search
nav_path:
- API Reference
- Server Side APIs
- Global APIs
- Find Campaign
nav_order: 13
page_type: endpoint
endpoint: POST /v2/private/fundraisers/search
http_method: POST
endpoint_path: /v2/private/fundraisers/search
api_surface: server-side
auth: API key
tags:
- donations
- search
crm_relevant: true
description: Search CrowdChange campaigns server-side with rich filters and retrieve a paginated list of matching fundraisers with goal, raised, and status data.
retrieved: '2026-10-14'
word_count: 844
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/server-side/global-apis/post_v2-private-fundraisers-search | Nav: API Reference > Server Side APIs > Global APIs > Find Campaign | Mirrored 2026-10-14 -->

# Find Campaign

> Search CrowdChange campaigns server-side with rich filters and retrieve a paginated list of matching fundraisers with goal, raised, and status data.

**Endpoint:** `POST /v2/private/fundraisers/search`  
**Surface:** Server Side API (server-to-server only; never call from a browser) · **Auth:** API key — `Authorization: Bearer {api-key}` header  
**Base URLs:** Production (US) `https://api.crowdchange.co` · Production (CA) `https://api.crowdchange.ca` · Development `https://api.crowdchange.dev` (see [Overview](../../overview.md))

## Body

- `text` (string, body) — Search term.
- `page` (integer, body) — Page number. Default: `1`
- `limit` (integer, body) — Number of results to return. Default: `100`
- `sort` (string, body) — Key to sort by. Allowed values: `id`, `name`, `amount_raised`, `amount_goal`
- `direction` (string, body) — Direction of sorting. Allowed values: `asc`, `desc`
- `email` (string, body) — Email filter.
- `status` (string, body) — Campaign status. Allowed values: `approved`, `pending`
- `is_hidden` (boolean, body) — True if campaign is hidden, otherwise false.
- `created_at` (object, body) — Campaign's creation date filter.
  - `<` (string, body)
  - `<=` (string, body)
  - `=` (string, body)
  - `>=` (string, body)
  - `>` (string, body)
- `amount_goal` (object, body) — Campaign's amount goal filter.
  - `<` (number, body)
  - `<=` (number, body)
  - `=` (number, body)
  - `>=` (number, body)
  - `>` (number, body)
- `amount_raised` (object, body) — Campaign's amount raised filter.
  - `<` (number, body)
  - `<=` (number, body)
  - `=` (number, body)
  - `>=` (number, body)
  - `>` (number, body)
- `after_id` (integer, body) — Return teams after Team ID.
- `lang` (string, body) — API's locale. Allowed values: `en`, `fr`
- `filter_by_lang` (integer, body) — Filter campaigns only available in locale
- `tags` (string[], body) — List of fundraiser tags.

## Response

Returns an array of objects with the following fields.

- `id` (integer) — Campaign ID.
- `partner_id` (integer) — Site ID.
- `name` (string) — Campaign name.
- `created_at` (string) — Campaign creation date.
- `amount_goal` (number) — Goal amount.
- `amount_raised` (number) — Amount raised by the campaign.
- `amount_pledged` (number) — Pending offline donation amount attributed to the campaign. This amount is included in `amount_raised` until the offline donation is received.
- `amount_matched` (number) — Amount contributed by donation matching assigned directly to the campaign. Team- and personal-page-level matching is not included.
- `amount_raised_formatted` (string) — Formatted amount raised by the campaign, includes currency symbol.
- `dt_start` (string) — Date and time when campaign starts.
- `dt_end` (string) — Date and time when campaign ends.
- `location_type` (string | null) — Campaign location type. Allowed values: `venue`, `online`, `other`.
- `location` (string | null) — Display location. Uses the legacy event address when no display value exists.
- `location_details` (string | null) — Location instructions or free-form text stored on the campaign.
- `location_data` (object | null) — Structured location data. For `venue`, contains `address` and/or `geo`; for `online`, contains `link`; otherwise `null`. Missing nested fields are omitted.
- `url` (string) — URL to campaign.
- `n_donors` (integer) — Number of donors.
- `n_teams` (integer) — Number of teams.
- `n_pages` (integer) — Number of pages.
- `status` (string) — Campaign's approval status. Allowed values: `approved`, `pending`
- `status_code` (string) — Campaign's activity status code. Allowed values: `live`, `deleted`, `archived`, `pending_approval`, `opening_soon`, `closed`
- `is_hidden` (boolean) — True if campaign is hidden, otherwise false.
- `auto_open_at` (string) — Date when campaign is scheduled to auto-open
- `auto_close_at` (string) — Date when campaign is scheduled to auto-close
- `closed_at` (string) — Date when campaign was closed
- `archived_at` (string) — Date when campaign was archived
- `language` (string) — Campaign language. Allowed values: `en`, `fr`
- `in_support_name` (string) — Value of `In support of` field associated with campaign.
- `in_support_code` (string) — Code provided for `In support of` field.
- `appeal_code` (string) — Appeal code.
- `user` (object)
  - `id` (integer) — Campaign owner's ID
  - `name` (string) — Campaign owner's name
  - `first_name` (string) — Campaign owner's first name
  - `last_name` (string) — Campaign owner's last name
  - `title` (string) — Campaign owner's title
  - `email` (string) — Campaign owner's email
- `organization` (object)
  - `id` (integer) — Campaign organization's ID
  - `name` (string) — Campaign organization's name
  - `custom_id` (string) — Campaign organization's Custom ID
- `fundraiser_template` (object)
  - `id` (integer) — Template ID.
  - `name` (string) — Template Name.
- `images` (object)
  - `original` (string) — URL to original campaign's image.
- `custom_data` (object[]) — List of custom questions and responses.
  - `field_id` (integer) — Custom field id.
  - `source_id` (integer) — If field was copied from Blueprint, this will reference the source field id from blueprint (similar to group id).
  - `name` (string) — Custom field label.
  - `content` (string) — User's answer to custom field.
  - `field_custom_id` (string) — Custom ID.
  - `response_custom_id` (string) — Custom ID for the response (multiple choice questions).
- `tags_list` (any[]) — Campaign tags.

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
    "partner_id": 10,
    "name": "Campaign",
    "created_at": "2022-01-01 16:00:03",
    "amount_goal": 1000,
    "amount_raised": 550,
    "amount_pledged": 125,
    "amount_matched": 50,
    "amount_raised_formatted": "$550",
    "dt_start": "2021-01-01 08:00:00",
    "dt_end": "2021-01-01 16:00:00",
    "location": "100 Main Street, Toronto, ON",
    "url": "https://demo.crowdchange.dev/2",
    "n_donors": 100,
    "n_teams": 50,
    "n_pages": 50,
    "status": "approved",
    "status_code": "approved",
    "is_hidden": false,
    "auto_open_at": "2022-03-01 00:00:00",
    "auto_close_at": "2022-03-01 00:00:00",
    "closed_at": "2022-03-01 00:00:00",
    "archived_at": "2022-03-01 00:00:00",
    "language": "en",
    "in_support_name": "Cancer Research",
    "in_support_code": "CR-123",
    "appeal_code": "GEN-123",
    "user": {
      "id": 1,
      "name": "John Snow",
      "first_name": "John",
      "last_name": "Snow",
      "title": "Mr.",
      "email": "john@crowdchange.co"
    },
    "organization": {
      "id": 1,
      "name": "Crowdchange",
      "custom_id": "CrowdchangeID"
    },
    "fundraiser_template": {
      "id": 1,
      "name": "Template"
    },
    "images": {
      "original": "https://img.crowdchange.co/files/abc.png?tr=w-[width],h-[height]"
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
    "tags_list": [
      "tag1",
      "tag2"
    ]
  }
]
```
