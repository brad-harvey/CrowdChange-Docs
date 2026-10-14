---
title: Overview
slug: api-reference/overview
collection: api
source_url: https://apidoc.crowdchange.dev/api-reference/overview
nav_path:
- API Reference
- Introduction
- Overview
nav_order: 11
page_type: reference
endpoint: null
http_method: null
endpoint_path: null
api_surface: null
auth: null
tags:
- authentication
- troubleshooting
crm_relevant: true
description: Learn how to authenticate with the CrowdChange API, the base URLs, HTTP methods, response codes, date formatting, and error conventions used.
retrieved: '2026-10-14'
word_count: 542
---

<!-- Source: https://apidoc.crowdchange.dev/api-reference/overview | Nav: API Reference > Introduction > Overview | Mirrored 2026-10-14 -->

# Overview

> Learn how to authenticate with the CrowdChange API, the base URLs, HTTP methods, response codes, date formatting, and error conventions used.

The CrowdChange API gives you programmatic access to the fundraising platform: campaigns, teams, personal pages, donors, transactions, and webhooks. It is organized into two surfaces:

* **Server Side APIs** (`/v2/private/...`) — for trusted, server-to-server integrations. These return richer data and support write operations such as offline donations and webhook management. Never call them from a browser.
* **Client Side APIs** (`/v2/client/...`) — read-mostly endpoints (plus donation processing) that are safe to call from public-facing pages, such as widgets and custom donation flows.

All requests and responses use JSON, and every request must be made over HTTPS.

## Base URLs

Use the base URL that matches the region your account is hosted in:

| Environment | Base URL |
| :- | :- |
| Production (US) | `https://api.crowdchange.co` |
| Production (CA) | `https://api.crowdchange.ca` |
| Development | `https://api.crowdchange.dev` |

## Authentication

Every request must include your **API key** in the `Authorization` header. The `Bearer` prefix is optional.

```http
Authorization: Bearer {api-key}
```

Your API key identifies your organization (site). Requests without a valid key are rejected with `403 Forbidden`. Keep your key secret and use it only from trusted server environments.

### User authentication

A subset of Server Side endpoints act on behalf of an individual user (for example, managing the campaigns, teams, or personal pages a user owns). These require an additional **user token** on top of your API key.

1. Obtain a token by calling [Sign In](server-side/user-specific-apis/post_v2-private-user-login.md) with the user's credentials.
2. Send the returned token with each user-specific request, either in the `auth-token` header or as a `token` request parameter.

```http
Authorization: Bearer {api-key}
auth-token: {user-token}
```

User tokens expire after 30 days of inactivity. A user may be signed in on up to 10 devices at once.

## HTTP Methods

The API follows standard REST conventions:

| Method | Usage |
| :- | :- |
| `GET` | Retrieve a resource or a list of resources. |
| `POST` | Create a resource, or run a search or an action. |
| `PUT` | Replace an existing resource with the supplied representation. |

## Dates and Times

All date and time values follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard and are stored and returned in UTC. Date-time values are formatted as `YYYY-MM-DD hh:mm:ss`.

## Status Codes

The API uses conventional HTTP status codes to indicate the result of a request:

| Code | Meaning |
| :- | :- |
| `200 OK` | The request succeeded. |
| `400 Bad Request` | The request was malformed or could not be processed. |
| `401 Unauthorized` | Authentication is missing or invalid. |
| `403 Forbidden` | Authentication succeeded, but you do not have access to the resource. |
| `404 Not Found` | The requested resource does not exist. |
| `405 Method Not Allowed` | The HTTP method is not supported for this endpoint. |
| `422 Unprocessable Entity` | The request body failed validation. |
| `429 Too Many Requests` | You have exceeded the rate limit; retry later. |

## Errors

When validation fails (`422`), the response lists each invalid field and its messages:

```json
{
  "message": "The given data was invalid.",
  "errors": {
    "fieldname": [
      "Error message"
    ]
  }
}
```

Other errors return a consistent envelope with a `status` and a `message`:

```json
{
  "status": "error",
  "message": {
    "error": [
      "A description of what went wrong."
    ]
  }
}
```
