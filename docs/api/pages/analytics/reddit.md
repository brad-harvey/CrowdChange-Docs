---
title: Reddit
slug: analytics/reddit
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/reddit
nav_path:
- Documentation
- Analytics & Tracking
- Reddit
nav_order: 5
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
description: Add the Reddit Pixel and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation purchase events from Reddit ads.
retrieved: '2026-10-14'
word_count: 554
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/reddit | Nav: Documentation > Analytics & Tracking > Reddit | Mirrored 2026-10-14 -->

# Reddit

> Add the Reddit Pixel and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation purchase events from Reddit ads.

## Reddit Pixel Integration

CrowdChange supports Reddit Pixel browser tracking and optional Reddit Conversions API purchase tracking.

Once connected, your Reddit Pixel receives `PageVisit`, `AddToCart`, and `Purchase` events.

If a Reddit Conversions API access token is configured, CrowdChange also sends completed purchases from the server.

***

## Setup

1. Go to **Admin -> Layout Settings -> Meta & Analytics**
2. Scroll to the **Reddit pixel** section
3. Enter your **Reddit Pixel ID**, for example `t2_xxxxxxx`
4. Optional: enter your **Reddit ads account ID**
5. Optional: enter your **Reddit Conversions API access token**
6. Click **Save**

The browser Pixel snippet is automatically injected into every page once the Pixel ID is saved. Conversions API tokens are stored as write-only encrypted values; leave the token field blank to keep an existing token.

***

## Tracked Events

### PageVisit

Fired automatically on page load and virtual page navigation.

```javascript
rdt('track', 'PageVisit');
```

***

### AddToCart

Fired when an item is added to the checkout cart.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code, for example `USD`, `CAD` |
| `value` | `number` | Total value of the item payload |
| `itemCount` | `number` | Sum of item quantities |
| `products` | `object[]` | Array of `{ id, name, category }` objects |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 50,
  "itemCount": 1,
  "products": [
    {
      "id": "registration",
      "name": "Registration",
      "category": "registration"
    }
  ]
}
```

***

### Purchase

Fired when a donor successfully completes a transaction.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code |
| `value` | `number` | Total transaction amount |
| `transactionId` | `string` | CrowdChange transaction ID |
| `conversionId` | `string` | `transaction_<transaction_id>` dedupe identifier |
| `products` | `object[]` | Array of `{ id, name, category }` objects |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 100,
  "transactionId": "1000",
  "conversionId": "transaction_1000",
  "products": [
    {
      "id": "donation",
      "name": "Donation",
      "category": "donation"
    }
  ]
}
```

***

## Server-Side Purchase Tracking

When both a Reddit ads account ID and Reddit Conversions API access token are configured, CrowdChange sends a server-side `Purchase` conversion.

| Field | Description |
| - | - |
| `click_id` | Captured `rdt_cid` URL parameter when available |
| `conversion_id` | `transaction_<transaction_id>` |
| `transaction_id` | CrowdChange transaction ID |
| `item_count` | Purchased item count |
| `currency` | Transaction currency |
| `value` | Transaction value in minor currency units |
| `value_decimal` | Decimal transaction value |
| `email` | SHA-256 hashed donor email when available |
| `external_id` | SHA-256 hashed CrowdChange user ID when available |
| `ip_address` | Request IP address |
| `user_agent` | Request user agent |

Ad-network failures are logged and do not interrupt the donor checkout flow.

***

## Click ID Attribution (`rdt_cid`)

When a visitor arrives via a Reddit ad, Reddit may append `rdt_cid` to the URL. CrowdChange captures this value in the browser session and passes it to the server-side conversion as `click_id`. CrowdChange also reads the `_rdt_uuid` cookie when present for future server-side attribution support.

***

## Verifying Your Setup

After saving your Pixel ID:

1. Visit any page on your platform and confirm Reddit Pixel loads from `https://www.redditstatic.com/ads/pixel.js`
2. Navigate between pages and confirm `PageVisit` events fire
3. Add an item to the cart and confirm `AddToCart` fires
4. Complete a test transaction and confirm `Purchase` fires with the expected value, currency, and `conversionId`

If you configured Conversions API, verify the server-side purchase in Reddit Ads reporting or diagnostics.

***

## Additional Information

See [Reddit Pixel docs](https://business.reddithelp.com/s/article/Reddit-Pixel-Set-Up-Guide) and [Reddit Conversions API docs](https://www.postman.com/reddit-ads-api/documentation/15705402-bf943e0e-521e-47dd-ae2e-2525568a8368) for further information.
