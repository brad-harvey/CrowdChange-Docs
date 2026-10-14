---
title: TikTok
slug: analytics/tiktok
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/tiktok
nav_path:
- Documentation
- Analytics & Tracking
- TikTok
nav_order: 6
page_type: guide
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- analytics-tracking
- donations
- payments-and-receipts
crm_relevant: false
description: Add the TikTok Pixel and Events API to CrowdChange to track pageviews, add-to-cart, and completed donation payment events from TikTok ads.
retrieved: '2026-10-14'
word_count: 534
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/tiktok | Nav: Documentation > Analytics & Tracking > TikTok | Mirrored 2026-10-14 -->

# TikTok

> Add the TikTok Pixel and Events API to CrowdChange to track pageviews, add-to-cart, and completed donation payment events from TikTok ads.

## TikTok Pixel Integration

CrowdChange supports TikTok Pixel browser tracking and optional TikTok Events API purchase tracking.

Once connected, your TikTok Pixel receives page, `AddToCart`, and `CompletePayment` events.

If a TikTok Events API access token is configured, CrowdChange also sends completed payments from the server.

***

## Setup

1. Go to **Admin -> Layout Settings -> Meta & Analytics**
2. Scroll to the **TikTok pixel** section
3. Enter your **TikTok Pixel ID**, for example `CXXXXXXXXXXXXXXX`
4. Optional: enter your **TikTok Events API access token**
5. Click **Save**

The browser Pixel snippet is automatically injected into every page once the Pixel ID is saved. Events API tokens are stored as write-only encrypted values; leave the token field blank to keep an existing token.

***

## Tracked Events

### Page

Fired automatically on page load and virtual page navigation.

```javascript
ttq.page();
```

***

### AddToCart

Fired when an item is added to the checkout cart.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code, for example `USD`, `CAD` |
| `value` | `number` | Total value of the item payload |
| `contents` | `object[]` | TikTok content payloads |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 50,
  "contents": [
    {
      "content_id": "registration",
      "content_name": "Registration",
      "content_category": "registration",
      "price": 50,
      "quantity": 1
    }
  ]
}
```

***

### CompletePayment

Fired when a donor successfully completes a transaction.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code |
| `value` | `number` | Total transaction amount |
| `order_id` | `string` | CrowdChange transaction ID |
| `event_id` | `string` | `transaction_<transaction_id>` dedupe identifier |
| `contents` | `object[]` | TikTok content payloads |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 100,
  "order_id": "1000",
  "event_id": "transaction_1000",
  "contents": [
    {
      "content_id": "donation",
      "content_name": "Donation",
      "content_category": "donation",
      "price": 100,
      "quantity": 1
    }
  ]
}
```

***

## Server-Side Payment Tracking

When both a TikTok Pixel ID and TikTok Events API access token are configured, CrowdChange sends a server-side `CompletePayment` event.

| Field | Description |
| - | - |
| `pixel_code` | TikTok Pixel ID |
| `event` | `CompletePayment` |
| `event_id` | `transaction_<transaction_id>` |
| `timestamp` | Event timestamp |
| `currency` | Transaction currency |
| `value` | Transaction total |
| `order_id` | CrowdChange transaction ID |
| `contents` | Purchased content IDs and quantities |
| `callback` | Captured `ttclid` value when available |
| `ttp` | TikTok `_ttp` browser cookie when available |
| `email` | SHA-256 hashed donor email when available |
| `external_id` | SHA-256 hashed CrowdChange user ID when available |
| `ip` | Request IP address |
| `user_agent` | Request user agent |

Ad-network failures are logged and do not interrupt the donor checkout flow.

***

## Click ID Attribution (`ttclid`)

When a visitor arrives via a TikTok ad, TikTok may append `ttclid` to the URL. CrowdChange captures this value in the browser session and passes it to server-side Events API calls as `callback`. CrowdChange also forwards the `_ttp` cookie when available.

***

## Verifying Your Setup

After saving your Pixel ID:

1. Visit any page on your platform and confirm TikTok Pixel loads from `https://analytics.tiktok.com/i18n/pixel/events.js`
2. Navigate between pages and confirm page events fire
3. Add an item to the cart and confirm `AddToCart` fires
4. Complete a test transaction and confirm `CompletePayment` fires with the expected value, currency, and `event_id`

If you configured Events API, verify the server-side event in TikTok Events Manager.

***

## Additional Information

See [TikTok Pixel docs](https://ads.tiktok.com/help/article/tiktok-pixel) and [TikTok Events API docs](https://ads.us.tiktok.com/help/article/events-api) for further information.
