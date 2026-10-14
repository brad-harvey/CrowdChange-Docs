---
title: Google Tag Manager
slug: analytics/google-tag-manager
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/google-tag-manager
nav_path:
- Documentation
- Analytics & Tracking
- Google Tag Manager
nav_order: 2
page_type: guide
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- analytics-tracking
- donations
crm_relevant: false
description: Set up Google Tag Manager on CrowdChange to forward donation, checkout, and pageview events to your marketing and analytics tools.
retrieved: '2026-10-14'
word_count: 880
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/google-tag-manager | Nav: Documentation > Analytics & Tracking > Google Tag Manager | Mirrored 2026-10-14 -->

# Google Tag Manager

> Set up Google Tag Manager on CrowdChange to forward donation, checkout, and pageview events to your marketing and analytics tools.

When you connect a Google Tag Manager container, CrowdChange pushes structured events to the GTM `dataLayer` as donors browse and transact. You can use these events to trigger tags and forward conversions to your marketing and analytics tools.

All events include a `context` property indicating the source:

| Value | Description |
| :- | :- |
| `platform` | Event fired from the main CrowdChange platform |
| `embed` | Event fired from an embedded donation form |

## General Events

### Pageview / URL changes

Triggered on every page change.

```json
{
  context: 'platform',
  event: 'Pageview',
  pagePath: 'https://demo.crowdchange.co/10001',
  pageLanguage: 'en', // possible values: en, fr
  previousPagePath: 'https://demo.crowdchange.co'
}
```

## User Authentication

### Sign In

There are two ways this event can be fired:

1. When user actually signs into the website through Sign In workflow. In this case the event is set to `login`
2. When user loads (or re-loads) the page and is already signed in from the previous session. In this case the event is set to `auth`

```json
{
  context: 'platform',
  event: 'login', // possible events: login, auth
  page_language: 'en', // possible values: en, fr
  user_id: 1
}
```

### Log Out

Triggered when user manually logs out.

```json
{
  context: 'platform',
  event: 'logout',
  page_language: 'en',
  user_id: 1
}
```

## Fundraisers

### Sharing

Triggered when user shares a fundraiser, or a team, or a personal page. Could be shared from Participant Center, directly from Fundraiser / Page / Team, or from `Thank You` page after a successful transaction.

```json
{
  context: 'platform',
  event: 'share',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1, // team id (if team is shared, or shared page belongs to the team)
  fundraiser_page_id: 1, // personal page id (if page is shared)
  is_fundraiser_owner: false, // boolean indicating if user owns the fundraiser
  is_team_owner: false, // boolean indicating if user owns the team
  is_page_owner: false // boolean indicating if user owns the shared page
}
```

## Teams

### Edit

Triggered when user saves changes to their team.

```json
{
  context: 'platform',
  event: 'team:edit',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  edit_types: ['name', 'amount_goal'] // array of edits. Possible values: image, image-fr, description, video, amount_goal, name, has_translation, slug
}
```

### Delete

Triggered when user deletes their team.

```json
{
  context: 'platform',
  event: 'team:delete',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1
}
```

## Personal Pages

### Edit

Triggered when user saves changes to their personal page.

```json
{
  context: 'platform',
  event: 'page:edit',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  fundraiser_page_id: 1,
  edit_types: ['name', 'team'] // array of edits. Possible values: image, image-fr, team, description, video, amount_goal, name, has_translation, slug, is_amount_raised_shown, site_cause_id
}
```

### Delete

Triggered when user deletes their personal page.

```json
{
  context: 'platform',
  event: 'personal-page:delete',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  fundraiser_page_id: 1
}
```

## Mailing List

### Preview

Triggered when user clicks "Preview" before sending mailing list email.

```json
{
  context: 'platform',
  event: 'mailing-list:preview',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  fundraiser_page_id: 1
}
```

### Send

Triggered when user clicks "Send" from mailing list.

```json
{
  context: 'platform',
  event: 'mailing-list:send',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  fundraiser_page_id: 1,
  n_contacts: 10 // total number of contacts email will be sent to
}
```

## Participant Center

### Personal Page's Dashboard

Triggered when user loads Dashboard page for their Personal Page.

```json
{
  context: 'platform',
  event: 'participant-center:page:dashboard',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  fundraiser_page_id: 1,
  is_team_captain: false,
  fundraiser_name: 'Toronto Walk',
  fundraiser_team_name: 'Best Toronto Team',
  fundraiser_page_name: 'Smith Family Page'
}
```

### Team's Dashboard

Triggered when user loads Dashboard page for their Team.

```json
{
  context: 'platform',
  event: 'participant-center:team:dashboard',
  page_language: 'en',
  fundraiser_id: 1,
  fundraiser_team_id: 1,
  is_team_captain: true,
  fundraiser_name: 'Toronto Walk',
  fundraiser_team_name: 'Best Toronto Team'
}
```

## Transactions

### Transaction Completed

Note: `items` will depend on enabled features and fundraiser type.

```json
{
  context: 'platform',
  event: 'purchase',
  pageLanguage: 'en', // possible values: en, fr
  ecommerce: {
    currencyCode: 'CAD',
    purchase: {
      transaction_id: 123456,
      fundraiser_id: 10001,
      fundraiser_name: 'Demo Event',
      organization_id: 201,
      organization_name: 'Ontario',
      organization_code: 'ONT',
      revenue: 650.99,
      coupon: 'DISCOUNT-123',
      breakdown: {
        amount_covered_fee: 5,
        amount_donation: 100,
        amount_apparel: 49.49,
        amount_ticket: 25.50,
        amount_registration: 50,
        amount_sponsor: 500,
        amount_cards: 20,
        frequency: 'once' // possible values: once, month, year
      },
      items: [
        { item_id: 'donation',     item_name: 'Donation',        item_price: 100,   frequency: 'once' },
        { item_id: 'cards',        item_name: 'eCards',          item_price: 20 },
        { item_id: 'apparel',      item_name: 'Apparel / Items', item_price: 49.49 },
        { item_id: 'ticket',       item_name: 'Tickets',         item_price: 25.50 },
        { item_id: 'registration', item_name: 'Registration',    item_price: 50 },
        { item_id: 'sponsor',      item_name: 'Sponsorship',     item_price: 500 },
        { item_id: 'covered_fee',  item_name: 'Covered Fee',     item_price: 5 }
      ]
    }
  }
}
```

Reference: See Google's [Enhanced Ecommerce for Tag Manager](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce#purchases) for more details.

## Tag Type Restrictions

For security, the platform enforces a GTM tag type allowlist and blocklist on every page load. This restricts which tag types your GTM container is permitted to fire, regardless of what is configured in your container.

| Status | Tag types |
| :- | :- |
| **Allowed** | `google` — Google tags (GA4, Google Ads, Floodlight, etc.) |
| **Allowed** | `sandboxedScripts` — Sandboxed JavaScript templates |
| **Allowed** | `nonGooglePixels` — Non-Google pixel tags (image/iframe pixels, e.g. Facebook Pixel via pixel tag type) |
| **Blocked** | `nonGoogleScripts` — Custom HTML tags / arbitrary `<script>` injection |

**In practice this means:**

* Standard Google tags, GA4 configurations, and Google Ads conversion tags will fire normally
* Facebook Pixel and similar third-party pixels loaded as pixel tag types will fire
* **Custom HTML tags** (which allow arbitrary JavaScript) **will not fire** — use sandboxed JavaScript templates instead

For a full reference of which GTM tag types fall into each category, see the [GTM tag type restriction guide](https://developers.google.com/tag-platform/tag-manager/restrict).

<br />
