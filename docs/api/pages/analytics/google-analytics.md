---
title: Google Analytics (GA4)
slug: analytics/google-analytics
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/google-analytics
nav_path:
- Documentation
- Analytics & Tracking
- Google Analytics (GA4)
nav_order: 1
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
description: Connect CrowdChange to Google Analytics 4 to track pageviews, donation events, and fundraising campaign performance across your site.
retrieved: '2026-10-14'
word_count: 710
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/google-analytics | Nav: Documentation > Analytics & Tracking > Google Analytics (GA4) | Mirrored 2026-10-14 -->

# Google Analytics (GA4)

> Connect CrowdChange to Google Analytics 4 to track pageviews, donation events, and fundraising campaign performance across your site.

Once you connect a Google Analytics 4 property, CrowdChange automatically tracks pageviews and fires structured events for the key moments in the donor journey — from viewing a campaign to completing a transaction. Events are sent from both the main platform and embedded donation forms.

Every URL change is tracked as a `pageview` event.

All events include a `context` property indicating the source:

| Value | Description |
| :- | :- |
| `platform` | Event fired from the main CrowdChange platform |
| `embed` | Event fired from an embedded donation form |

## Events

Event names that are tracked by Google Analytics.

**Checkout:**

| Description | Path | Event Name |
| :- | :- | :- |
| User views donation page | /donate | Donate: View Page |
| User views `Pay for Pledge` page | /donate | Donate Pledge: View Donate Page |
| User clicks "Donate" | /donate/submit | Donate: Submit |
| Transaction succeeds | \[path]/success | Donate: Completed |
| Transaction fails | \[path]/failed | Donate: Failed |
| User views `Thank you` page after transaction is completed | \[path-to-page] | Donate: Thank You |
| User selects amount from Donation Bar preset amount | \[path-to-page] | Clicked: Donation Bar: Button #\[number] |
| User selects `Other` on Donation Bar | \[path-to-page] | Clicked: Donation Bar: Other |

**List of fundraisers (main page):**

| Description | Path | Event Name | Data |
| :- | :- | :- | :- |
| User changes organization filter | /fundraisers/organizations | Fundraisers: Organization | `{ value: id }` |
| User sorts fundraisers | /fundraisers/sort | Fundraisers: Sort | `{ value: sort }` |
| User filters fundraisers | /fundraisers/filter | Fundraisers: Filter | `{ value: filter }` |
| User searches for a fundraiser | /fundraisers/search | Fundraisers: Search | |

**Fundraiser:**

| Description | Path | Event Name |
| :- | :- | :- |
| User clicked "Setup banking" | \[path-to-page] | Clicked: Fundraiser: banking-setup |
| | | Clicked: Donate Button (Multiple Options - Toggle Dropdown) |
| | | Clicked: Create Page, Start/Join Teams Button - Toggle Dropdown |
| | | Clicked: Create Page Button |
| | | Clicked: Join Team: From Team Button |
| | | Clicked: Join team: from personal page Button |
| | | Clicked: Sponsors Button |
| | | Clicked: Create Page, Start/Join Teams Dropdown - Join Team |
| | | Clicked: Create Page, Start/Join Teams Dropdown - Start a Team |
| | | Clicked: Create Page, Start/Join Teams Dropdown - Create a page |
| | | Clicked: Donate Button (Multiple Options Dropdown - Donate in General) |
| | | Clicked: Donate Button (Multiple Options Dropdown - Donate to Team) |
| | | Clicked: Donate Button (Multiple Options Dropdown - Donate to page) |

**Personal Pages:**

| Description | Path | Event Name |
| :- | :- | :- |
| User views personal page creation page | /page/create | Create a personal page: View page |
| User creates a personal page (regular flow) | /page/create/completed | Page Created |
| User closes self-donation prompt | \[path-to-page] | Closed donate own page modal |
| | \[path-to-page] | Clicked: Fundraiser Page Strength: add-custom-image |
| | \[path-to-page] | Clicked: Fundraiser Page Strength: add-custom-message |
| | \[path-to-page] | Clicked: Fundraiser Page Strength: donate |
| | \[path-to-page] | Clicked: Fundraiser Page Strength: share |
| | \[path-to-page] | Clicked: Fundraiser Page Strength: email-list |

**Teams:**

| Description | Path | Event Name |
| :- | :- | :- |
| User views team creation page | /team/create | Create a team page: View page |
| User creates a team (regular flow) | /team/create/completed | Team Created |

**Participant Center:**

| Path | Event Name |
| :- | :- |
| \[path-to-page] | Clicked: Fundraiser Page Strength: add-custom-image |
| \[path-to-page] | Clicked: Fundraiser Page Strength: add-custom-message |
| \[path-to-page] | Clicked: Fundraiser Page Strength: donate |
| \[path-to-page] | Clicked: Fundraiser Page Strength: share |
| \[path-to-page] | Clicked: Fundraiser Page Strength: email-list |

## Purchase

**Note:** ecommerce must be enabled in GA settings.

When a transaction is completed, a `purchase` event is sent in GA4 ecommerce format:

```javascript
gtag('event', 'purchase', {
  context: 'platform',  // or 'embed'
  transaction_id: 1000,
  currency: 'CAD',      // CAD, USD, AUD, etc.
  value: 500,           // total transaction $ value
  coupon: null,         // coupon code if applied

  // items depend on enabled features and fundraiser configuration
  items: [
    { item_id: 'donation',     item_name: 'Donation',        price: 100,   quantity: 1 },
    { item_id: 'cards',        item_name: 'eCards',          price: 20,    quantity: 1 },
    { item_id: 'apparel',      item_name: 'Apparel / Items', price: 49.49, quantity: 1 },
    { item_id: 'ticket',       item_name: 'Tickets',         price: 25.50, quantity: 1 },
    { item_id: 'registration', item_name: 'Registration',    price: 50,    quantity: 1 },
    { item_id: 'sponsor',      item_name: 'Sponsorship',     price: 500,   quantity: 1 },
    { item_id: 'covered_fee',  item_name: 'Covered Fee',     price: 5,     quantity: 1 },
  ]
});
```

## Tag Type Restrictions

The platform applies a GTM allowlist/blocklist alongside the GA4 snippet, restricting which tag types can run on the page.

**Custom HTML tags are blocked**; sandboxed JavaScript templates and Google/pixel tag types are allowed.

If you are loading additional tags through GTM alongside GA4, see the [Tag Type Restrictions](https://apidoc.crowdchange.dev/docs/google-tag-manager) section in the GTM documentation for full details.
