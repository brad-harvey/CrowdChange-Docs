# CrowdChange API & Developer Docs - Index

Mirrored from https://apidoc.crowdchange.dev on 2026-10-14. Sections and order match the site's sidebar.
Endpoint entries show `METHOD /path`. Start with [Overview](pages/api-reference/overview.md) for base URLs, authentication, status codes and error formats. Topic index across both collections: [../TAGS.md](../TAGS.md).

## Documentation

### Analytics & Tracking

- [Google Analytics (GA4)](pages/analytics/google-analytics.md) — Connect CrowdChange to Google Analytics 4 to track pageviews, donation events, and fundraising campaign performance across your site.
- [Google Tag Manager](pages/analytics/google-tag-manager.md) — Set up Google Tag Manager on CrowdChange to forward donation, checkout, and pageview events to your marketing and analytics tools.
- [Facebook Pixel](pages/analytics/facebook-pixel.md) — Install the Facebook Pixel and Conversions API in CrowdChange to track donations, retarget visitors, and measure ad performance on Meta.
- [Pinterest](pages/analytics/pinterest.md) — Add the Pinterest Tag and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation checkout events from Pinterest ads.
- [Reddit](pages/analytics/reddit.md) — Add the Reddit Pixel and Conversions API to CrowdChange to track pageviews, add-to-cart, and donation purchase events from Reddit ads.
- [TikTok](pages/analytics/tiktok.md) — Add the TikTok Pixel and Events API to CrowdChange to track pageviews, add-to-cart, and completed donation payment events from TikTok ads.

### Widgets

- [Widgets Overview](pages/widgets/overview.md) — Embed CrowdChange fundraising widgets on your website with a single script tag, then add donation forms, progress bars, and thermometers anywhere on the page.
- [Donation Form Widget](pages/widgets/donation-form-widget.md) — Embed the CrowdChange donation form on your site to accept donations inline or in a popup, with customizable colors, language, and layout.
- [Progress Widget](pages/widgets/progress-widget.md) — Embed the CrowdChange progress widget to display a live fundraising progress bar for any campaign, team, or personal page, with customizable colors.
- [Thermometer Widget](pages/widgets/thermometer-widget.md) — Embed the CrowdChange thermometer widget to display a live fundraising thermometer with goal and raised amounts for any campaign, team, or personal page.

## API Reference

### Introduction

- [Overview](pages/api-reference/overview.md) — Learn how to authenticate with the CrowdChange API, the base URLs, HTTP methods, response codes, date formatting, and error conventions used.

### Server Side APIs

#### Transactions

- [Get All](pages/api-reference/server-side/transactions/get_v2-private-transactions.md) — `GET /v2/private/transactions` — Retrieve all CrowdChange transactions within a time window or by payout ID, with full payment processor, donor, and campaign attribution details.

#### Global APIs

- [Find Campaign](pages/api-reference/server-side/global-apis/post_v2-private-fundraisers-search.md) — `POST /v2/private/fundraisers/search` — Search CrowdChange campaigns server-side with rich filters and retrieve a paginated list of matching fundraisers with goal, raised, and status data.
- [Find Team](pages/api-reference/server-side/global-apis/post_v2-private-teams-search.md) — `POST /v2/private/teams/search` — Search CrowdChange fundraising teams server-side with rich filters and retrieve a paginated list with captain, goal, and raised totals for each.
- [Find Personal Page](pages/api-reference/server-side/global-apis/post_v2-private-personal-pages-search.md) — `POST /v2/private/personal-pages/search` — Search CrowdChange personal fundraising pages server-side with rich filters and retrieve a paginated list with goal, raised, and owner details.

#### Campaign-Specific APIs

- [Get Campaign](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id.md) — `GET /v2/private/fundraiser/{id}` — Retrieve detailed server-side information about a CrowdChange campaign by its fundraiser ID, including configuration, goal, raised, and donor stats.
- [Get Campaign Teams](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-teams.md) — `GET /v2/private/fundraiser/{id}/teams` — Search teams registered under a CrowdChange campaign by keyword and retrieve a paginated list with captain, goal, and raised totals for each.
- [Create Offline Transaction](pages/api-reference/server-side/campaign-specific-apis/post_v2-private-fundraiser-id-offline-donations.md) — `POST /v2/private/fundraiser/{id}/offline-donations` — Record an offline donation transaction against a CrowdChange campaign on behalf of a donor, including amount, payment method, and donor details.
- [Get offline transactions](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-offline-donations-list.md) — `GET /v2/private/fundraiser/{id}/offline-donations/list` — Retrieve a paginated list of offline donation transactions recorded against a CrowdChange campaign, including amount, donor, and entry metadata.

#### User-Specific APIs

- [Sign In](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-login.md) — `POST /v2/private/user/login` — Authenticate a CrowdChange user and receive an auth token for user-specific API calls, including the two-factor authentication challenge flow.
- [Sign Out](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-logout.md) — `POST /v2/private/user/logout` — Invalidate the current CrowdChange auth token to sign the authenticated user out of the active session on a single device or client.
- [Sign Out All Devices](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-logout-all.md) — `POST /v2/private/user/logout/all` — Invalidate every active auth token for the authenticated CrowdChange user, signing them out of all devices and sessions in a single call.
- [Upload Image](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-upload-image.md) — `POST /v2/private/user/upload/image` — Upload an image file to CrowdChange on behalf of the authenticated user, returning a hosted URL you can attach to personal pages or teams.
- [Get Campaigns](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraisers.md) — `GET /v2/private/user/fundraisers` — Retrieve a paginated list of CrowdChange campaigns where the authenticated user is registered, including role, goal, and amount raised per campaign.
- [Get Personal Pages](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-personal-pages.md) — `GET /v2/private/user/personal-pages` — Retrieve a paginated list of the authenticated user's personal fundraising pages across all CrowdChange campaigns, with goals and raised amounts.
- [Get Teams](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-teams.md) — `GET /v2/private/user/teams` — Retrieve a paginated list of CrowdChange fundraising teams the authenticated user belongs to, including role, campaign, goal, and raised totals.
- [Get Team's Personal Pages](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-personal-pages.md) — `GET /v2/private/user/fundraiser/{id}/team/{teamId}/personal-pages` — Retrieve a paginated list of personal fundraising pages registered under the authenticated user's team within a CrowdChange campaign.
- [Update Personal Page](pages/api-reference/server-side/user-specific-apis/put_v2-private-user-fundraiser-id-personal-page-pageid.md) — `PUT /v2/private/user/fundraiser/{id}/personal-page/{pageId}` — Update the authenticated user's personal fundraising page within a CrowdChange campaign, including title, story, goal, and cover image.
- [Update Team](pages/api-reference/server-side/user-specific-apis/put_v2-private-user-fundraiser-id-team-teamid.md) — `PUT /v2/private/user/fundraiser/{id}/team/{teamId}` — Update the authenticated user's CrowdChange fundraising team within a campaign, including name, description, goal, and team cover image.
- [Page Donors List](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-personal-page-pageid-donors.md) — `GET /v2/private/user/fundraiser/{id}/personal-page/{pageId}/donors` — Retrieve a paginated list of donors for the authenticated user's personal page within a campaign, returning 10 donors per page with amount details.
- [Create Offline Transaction](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-fundraiser-id-offline-donation.md) — `POST /v2/private/user/fundraiser/{id}/offline-donation` — Record an offline donation transaction on behalf of the authenticated user against a CrowdChange campaign, with amount and donor details.
- [Team Donors List](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-donors.md) — `GET /v2/private/user/fundraiser/{id}/team/{teamId}/donors` — Retrieve a paginated list of donors for the authenticated user's team within a campaign, returning 10 donors per page with names and amounts.

#### Webhooks

- [Subscribe Webhook](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-subscribe.md) — `POST /v2/private/webhooks/subscribe` — Register a new CrowdChange webhook subscription pointing at your target URL to start receiving event payloads from the fundraising platform.
- [Unsubscribe webhook](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-unsubscribe.md) — `POST /v2/private/webhooks/unsubscribe` — Remove an existing CrowdChange webhook subscription so the target URL stops receiving event payloads from the fundraising platform.
- [Get webhooks](pages/api-reference/server-side/webhooks/get_v2-private-webhooks.md) — `GET /v2/private/webhooks` — Retrieve a paginated list of every CrowdChange webhook subscription registered on your account, with target URL, subscribed events, and status.
- [Subscribe Webhook events](pages/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-subscribe.md) — `PUT /v2/private/webhooks/{webhookId}/events/subscribe` — Add specific CrowdChange system events to an existing webhook subscription so the target URL starts receiving those event payloads.
- [Unsubscribe Webhook events](pages/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-unsubscribe.md) — `PUT /v2/private/webhooks/{webhookId}/events/unsubscribe` — Remove specific CrowdChange system events from an existing webhook subscription so the target URL stops receiving those event payloads.
- [Get logs](pages/api-reference/server-side/webhooks/get_v2-private-webhooks-id-logs.md) — `GET /v2/private/webhooks/{webhookId}/logs` — Retrieve a paginated log of webhook delivery attempts for a CrowdChange webhook subscription, including event type, status, and response details.
- [Resend logged event](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-logid-resend.md) — `POST /v2/private/webhooks/{webhookId}/logs/{logId}/resend` — Resend a previously logged CrowdChange webhook event to its subscriber URL, useful for retrying failed deliveries or debugging webhook handlers.
- [Resend event by payload hash](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-hash-payloadhash-resend.md) — `POST /v2/private/webhooks/{webhookId}/logs/hash/{payloadHash}/resend` — Resend the newest logged CrowdChange webhook delivery that matches a payload hash, creating a new delivery attempt with the same payload.
- [Send event](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-events-send.md) — `POST /v2/private/webhooks/{webhookId}/events/send` — Trigger a CrowdChange webhook to fire an event payload based on an existing entity, useful for testing endpoints and replaying historical data.

#### Webhook Reference

- [Event payloads](pages/api-reference/server-side/webhooks/event-payloads.md) — Reference the JSON payloads sent by CrowdChange webhook events.

### Client Side APIs

#### Campaign-Specific APIs

- [Goal / Raised Amounts](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id.md) — `GET /v2/client/fundraiser/{id}` — Retrieve the goal amount, raised amount, donor count, and core campaign metadata for a specific CrowdChange campaign by its fundraiser ID.
- [Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-donors.md) — `GET /v2/client/fundraiser/{id}/donors` — Retrieve a paginated list of donors for a specific CrowdChange campaign, returning 10 donor records per page with name, amount, and donation date.
- [Heatmap](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-heatmap.md) — `GET /v2/client/fundraiser/{id}/heatmap` — Retrieve aggregated donation counts and amounts raised by country and state for a CrowdChange campaign, suitable for rendering a geographic heatmap.
- [Team Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-team-teamid-donors.md) — `GET /v2/client/fundraiser/{id}/team/{teamId}/donors` — Retrieve a paginated list of donors for a specific team within a CrowdChange campaign, returning 10 donors per page with names and donation amounts.
- [Page Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-personal-page-pageid-donors.md) — `GET /v2/client/fundraiser/{id}/personal-page/{pageId}/donors` — Retrieve a paginated list of donors for a personal fundraising page within a CrowdChange campaign, returning 10 donors per page with amount details.

#### Global APIs

- [Find Campaign](pages/api-reference/client-side/global-apis/get_v2-client-fundraisers-search.md) — `GET /v2/client/fundraisers/search` — Search CrowdChange campaigns by keyword and retrieve a paginated list of matching fundraisers with goal, raised, and status data for each.
- [Find Team](pages/api-reference/client-side/global-apis/get_v2-client-teams-search.md) — `GET /v2/client/teams/search` — Search CrowdChange fundraising teams by keyword and retrieve a paginated list of matching teams with goal, raised amount, and campaign details.
- [Get Team](pages/api-reference/client-side/global-apis/get_v2-client-teams-id.md) — `GET /v2/client/teams/{id}` — Retrieve a single CrowdChange fundraising team by ID, including parent campaign, captain, member count, goal, and total raised so far.
- [Find Personal Page](pages/api-reference/client-side/global-apis/get_v2-client-personal-pages-search.md) — `GET /v2/client/personal-pages/search` — Search public CrowdChange personal fundraising pages by keyword and retrieve a paginated list of matches with goal, raised, and owner details.
- [Get Personal Page](pages/api-reference/client-side/global-apis/get_v2-client-personal-pages-id.md) — `GET /v2/client/personal-pages/{id}` — Retrieve a single CrowdChange personal fundraising page by ID, including owner, parent campaign, goal, raised amount, and recent donor activity.
- [Activities Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard.md) — `GET /v2/client/activity-trackers/leaderboard` — Retrieve the activity tracker leaderboard of personal pages, returning 10 participants per page ranked by tracked steps, distance, or minutes.
- [Activities Teams Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard-teams.md) — `GET /v2/client/activity-trackers/leaderboard/teams` — Retrieve the activity tracker teams leaderboard with up to 10 teams per page, ranked by tracked steps, distance, or activity minutes raised.
- [Activities Campaigns Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard-fundraisers.md) — `GET /v2/client/activity-trackers/leaderboard/fundraisers` — Retrieve the activity tracker campaigns leaderboard with up to 10 fundraisers per page, ranked by tracked steps, distance, or activity minutes.
- [Site wide stats](pages/api-reference/client-side/global-apis/get_v2-client-wl-stats.md) — `GET /v2/client/wl/stats` — Retrieve site-wide aggregated stats across all CrowdChange campaigns, including total raised, donor count, and number of active fundraisers.

#### Top Daily

- [Top Daily Campaigns](pages/api-reference/client-side/top-daily/get_v2-client-fundraisers-top-daily.md) — `GET /v2/client/fundraisers/top/daily` — Retrieve the daily ranking of top CrowdChange campaigns by amount raised over the last 24 hours, ideal for a leaderboard or homepage widget.
- [Top Daily Teams](pages/api-reference/client-side/top-daily/get_v2-client-teams-top-daily.md) — `GET /v2/client/teams/top/daily` — Retrieve the daily ranking of top CrowdChange fundraising teams by amount raised over the last 24 hours, for leaderboards and homepage widgets.
- [Top Daily Pages](pages/api-reference/client-side/top-daily/get_v2-client-personal-pages-top-daily.md) — `GET /v2/client/personal-pages/top/daily` — Retrieve the daily ranking of top CrowdChange personal fundraising pages by amount raised over the last 24 hours, for leaderboards and widgets.

## Endpoint quick reference

| Method | Path | Surface | Auth | Page |
| :- | :- | :- | :- | :- |
| GET | `/v2/client/activity-trackers/leaderboard` | client-side | API key | [Activities Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard.md) |
| GET | `/v2/client/activity-trackers/leaderboard/fundraisers` | client-side | API key | [Activities Campaigns Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard-fundraisers.md) |
| GET | `/v2/client/activity-trackers/leaderboard/teams` | client-side | API key | [Activities Teams Leaderboard](pages/api-reference/client-side/global-apis/get_v2-client-activity-trackers-leaderboard-teams.md) |
| GET | `/v2/client/fundraiser/{id}` | client-side | API key | [Goal / Raised Amounts](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id.md) |
| GET | `/v2/client/fundraiser/{id}/donors` | client-side | API key | [Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-donors.md) |
| GET | `/v2/client/fundraiser/{id}/heatmap` | client-side | API key | [Heatmap](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-heatmap.md) |
| GET | `/v2/client/fundraiser/{id}/personal-page/{pageId}/donors` | client-side | API key | [Page Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-personal-page-pageid-donors.md) |
| GET | `/v2/client/fundraiser/{id}/team/{teamId}/donors` | client-side | API key | [Team Donors List](pages/api-reference/client-side/campaign-specific-apis/get_v2-client-fundraiser-id-team-teamid-donors.md) |
| GET | `/v2/client/fundraisers/search` | client-side | API key | [Find Campaign](pages/api-reference/client-side/global-apis/get_v2-client-fundraisers-search.md) |
| GET | `/v2/client/fundraisers/top/daily` | client-side | API key | [Top Daily Campaigns](pages/api-reference/client-side/top-daily/get_v2-client-fundraisers-top-daily.md) |
| GET | `/v2/client/personal-pages/search` | client-side | API key | [Find Personal Page](pages/api-reference/client-side/global-apis/get_v2-client-personal-pages-search.md) |
| GET | `/v2/client/personal-pages/top/daily` | client-side | API key | [Top Daily Pages](pages/api-reference/client-side/top-daily/get_v2-client-personal-pages-top-daily.md) |
| GET | `/v2/client/personal-pages/{id}` | client-side | API key | [Get Personal Page](pages/api-reference/client-side/global-apis/get_v2-client-personal-pages-id.md) |
| GET | `/v2/client/teams/search` | client-side | API key | [Find Team](pages/api-reference/client-side/global-apis/get_v2-client-teams-search.md) |
| GET | `/v2/client/teams/top/daily` | client-side | API key | [Top Daily Teams](pages/api-reference/client-side/top-daily/get_v2-client-teams-top-daily.md) |
| GET | `/v2/client/teams/{id}` | client-side | API key | [Get Team](pages/api-reference/client-side/global-apis/get_v2-client-teams-id.md) |
| GET | `/v2/client/wl/stats` | client-side | API key | [Site wide stats](pages/api-reference/client-side/global-apis/get_v2-client-wl-stats.md) |
| GET | `/v2/private/fundraiser/{id}` | server-side | API key | [Get Campaign](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id.md) |
| POST | `/v2/private/fundraiser/{id}/offline-donations` | server-side | API key | [Create Offline Transaction](pages/api-reference/server-side/campaign-specific-apis/post_v2-private-fundraiser-id-offline-donations.md) |
| GET | `/v2/private/fundraiser/{id}/offline-donations/list` | server-side | API key | [Get offline transactions](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-offline-donations-list.md) |
| GET | `/v2/private/fundraiser/{id}/teams` | server-side | API key | [Get Campaign Teams](pages/api-reference/server-side/campaign-specific-apis/get_v2-private-fundraiser-id-teams.md) |
| POST | `/v2/private/fundraisers/search` | server-side | API key | [Find Campaign](pages/api-reference/server-side/global-apis/post_v2-private-fundraisers-search.md) |
| POST | `/v2/private/personal-pages/search` | server-side | API key | [Find Personal Page](pages/api-reference/server-side/global-apis/post_v2-private-personal-pages-search.md) |
| POST | `/v2/private/teams/search` | server-side | API key | [Find Team](pages/api-reference/server-side/global-apis/post_v2-private-teams-search.md) |
| GET | `/v2/private/transactions` | server-side | API key | [Get All](pages/api-reference/server-side/transactions/get_v2-private-transactions.md) |
| POST | `/v2/private/user/fundraiser/{id}/offline-donation` | server-side | API key + user token | [Create Offline Transaction](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-fundraiser-id-offline-donation.md) |
| PUT | `/v2/private/user/fundraiser/{id}/personal-page/{pageId}` | server-side | API key + user token | [Update Personal Page](pages/api-reference/server-side/user-specific-apis/put_v2-private-user-fundraiser-id-personal-page-pageid.md) |
| GET | `/v2/private/user/fundraiser/{id}/personal-page/{pageId}/donors` | server-side | API key + user token | [Page Donors List](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-personal-page-pageid-donors.md) |
| PUT | `/v2/private/user/fundraiser/{id}/team/{teamId}` | server-side | API key + user token | [Update Team](pages/api-reference/server-side/user-specific-apis/put_v2-private-user-fundraiser-id-team-teamid.md) |
| GET | `/v2/private/user/fundraiser/{id}/team/{teamId}/donors` | server-side | API key + user token | [Team Donors List](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-donors.md) |
| GET | `/v2/private/user/fundraiser/{id}/team/{teamId}/personal-pages` | server-side | API key + user token | [Get Team's Personal Pages](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraiser-id-team-teamid-personal-pages.md) |
| GET | `/v2/private/user/fundraisers` | server-side | API key + user token | [Get Campaigns](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-fundraisers.md) |
| POST | `/v2/private/user/login` | server-side | API key | [Sign In](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-login.md) |
| POST | `/v2/private/user/logout` | server-side | API key + user token | [Sign Out](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-logout.md) |
| POST | `/v2/private/user/logout/all` | server-side | API key + user token | [Sign Out All Devices](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-logout-all.md) |
| GET | `/v2/private/user/personal-pages` | server-side | API key + user token | [Get Personal Pages](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-personal-pages.md) |
| GET | `/v2/private/user/teams` | server-side | API key + user token | [Get Teams](pages/api-reference/server-side/user-specific-apis/get_v2-private-user-teams.md) |
| POST | `/v2/private/user/upload/image` | server-side | API key + user token | [Upload Image](pages/api-reference/server-side/user-specific-apis/post_v2-private-user-upload-image.md) |
| GET | `/v2/private/webhooks` | server-side | API key | [Get webhooks](pages/api-reference/server-side/webhooks/get_v2-private-webhooks.md) |
| POST | `/v2/private/webhooks/subscribe` | server-side | API key | [Subscribe Webhook](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-subscribe.md) |
| POST | `/v2/private/webhooks/unsubscribe` | server-side | API key | [Unsubscribe webhook](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-unsubscribe.md) |
| POST | `/v2/private/webhooks/{webhookId}/events/send` | server-side | API key | [Send event](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-events-send.md) |
| PUT | `/v2/private/webhooks/{webhookId}/events/subscribe` | server-side | API key | [Subscribe Webhook events](pages/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-subscribe.md) |
| PUT | `/v2/private/webhooks/{webhookId}/events/unsubscribe` | server-side | API key | [Unsubscribe Webhook events](pages/api-reference/server-side/webhooks/put_v2-private-webhooks-id-events-unsubscribe.md) |
| GET | `/v2/private/webhooks/{webhookId}/logs` | server-side | API key | [Get logs](pages/api-reference/server-side/webhooks/get_v2-private-webhooks-id-logs.md) |
| POST | `/v2/private/webhooks/{webhookId}/logs/hash/{payloadHash}/resend` | server-side | API key | [Resend event by payload hash](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-hash-payloadhash-resend.md) |
| POST | `/v2/private/webhooks/{webhookId}/logs/{logId}/resend` | server-side | API key | [Resend logged event](pages/api-reference/server-side/webhooks/post_v2-private-webhooks-id-logs-logid-resend.md) |
