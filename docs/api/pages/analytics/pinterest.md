---
title: Pinterest
slug: analytics/pinterest
collection: api
source_url: https://apidoc.crowdchange.dev/analytics/pinterest
nav_path:
- Documentation
- Analytics & Tracking
- Pinterest
nav_order: 4
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
description: Add the Pinterest Tag and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation checkout events from Pinterest ads.
retrieved: '2026-10-14'
word_count: 578
---

<!-- Source: https://apidoc.crowdchange.dev/analytics/pinterest | Nav: Documentation > Analytics & Tracking > Pinterest | Mirrored 2026-10-14 -->

# Pinterest

> Add the Pinterest Tag and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation checkout events from Pinterest ads.

## Pinterest Tag Integration

CrowdChange supports Pinterest Tag browser tracking, enhanced match, and optional Pinterest Conversions API checkout tracking.

Once connected, your Pinterest Tag receives `page`, `addtocart`, and `checkout` events.

If a Pinterest Conversions API access token is configured, CrowdChange also sends completed checkout events from the server.

***

## Setup

1. Go to **Admin -> Layout Settings -> Meta & Analytics**
2. Scroll to the **Pinterest tag** section
3. Enter your **Pinterest Tag ID**, for example `2612345678901`
4. Optional: enter your **Pinterest ad account ID**
5. Optional: enter your **Pinterest Conversions API access token**
6. Click **Save**

The browser Tag snippet and noscript fallback are automatically injected once the Tag ID is saved. Conversions API tokens are stored as write-only encrypted values; leave the token field blank to keep an existing token.

***

## Tracked Events

### page

Fired automatically on page load and virtual page navigation.

```javascript
pintrk('page');
```

***

### addtocart

Fired when an item is added to the checkout cart.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code, for example `USD`, `CAD` |
| `value` | `number` | Total value of the item payload |
| `line_items` | `object[]` | Pinterest line item payloads |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 50,
  "line_items": [
    {
      "product_id": "registration",
      "product_name": "Registration",
      "product_price": 50,
      "product_quantity": 1
    }
  ]
}
```

***

### checkout

Fired when a donor successfully completes a transaction.

| Parameter | Type | Description |
| - | - | - |
| `currency` | `string` | ISO 4217 currency code |
| `value` | `number` | Total transaction amount |
| `order_id` | `string` | CrowdChange transaction ID |
| `event_id` | `string` | `transaction_<transaction_id>` dedupe identifier |
| `order_quantity` | `number` | Number of transaction items |
| `line_items` | `object[]` | Pinterest line item payloads |

**Example payload**

```json
{
  "currency": "CAD",
  "value": 100,
  "order_id": "1000",
  "event_id": "transaction_1000",
  "order_quantity": 1,
  "line_items": [
    {
      "product_id": "donation",
      "product_name": "Donation",
      "product_price": 100,
      "product_quantity": 1
    }
  ]
}
```

***

## Enhanced Match

When a logged-in user is available, CrowdChange loads Pinterest enhanced match with a normalized SHA-256 email hash. Raw email addresses are not sent to the browser tag.

***

## Server-Side Checkout Tracking

When both a Pinterest ad account ID and Pinterest Conversions API access token are configured, CrowdChange sends a server-side `checkout` event.

| Field | Description |
| - | - |
| `event_name` | `checkout` |
| `action_source` | `web` |
| `event_id` | `transaction_<transaction_id>` |
| `event_source_url` | Checkout page URL when available |
| `currency` | Transaction currency |
| `value` | Transaction total |
| `order_id` | CrowdChange transaction ID |
| `num_items` | Purchased item count |
| `contents` | Purchased content IDs and quantities |
| `click_id` | Captured Pinterest `epik` value when available |
| `em` | SHA-256 hashed donor email when available |
| `external_id` | SHA-256 hashed CrowdChange user ID when available |
| `client_ip_address` | Request IP address |
| `client_user_agent` | Request user agent |

Ad-network failures are logged and do not interrupt the donor checkout flow.

***

## Click ID Attribution (`epik`)

When a visitor arrives via a Pinterest ad, Pinterest may append `epik` to the URL or set an `_epik` cookie. CrowdChange captures either value and passes it to server-side checkout events as `click_id`.

***

## Verifying Your Setup

After saving your Tag ID:

1. Visit any page on your platform and confirm Pinterest Tag loads from `https://s.pinimg.com/ct/core.js`
2. Navigate between pages and confirm `page` events fire
3. Add an item to the cart and confirm `addtocart` fires
4. Complete a test transaction and confirm `checkout` fires with the expected value, currency, and `event_id`

If you configured Conversions API, verify the server-side checkout in Pinterest Events Manager.

***

## Additional Information

See [Pinterest Tag docs](https://help.pinterest.com/en/business/article/install-the-pinterest-tag) and [Pinterest Conversions API docs](https://developers.pinterest.com/docs/track-conversions/track-conversions-in-the-api/) for further information.
