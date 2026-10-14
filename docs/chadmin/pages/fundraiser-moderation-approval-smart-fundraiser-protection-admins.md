---
title: 'Fundraiser Moderation: Approval & Smart Fundraiser Protection (Admins)'
slug: fundraiser-moderation-approval-smart-fundraiser-protection-admins
collection: chadmin
source_url: https://chadmin.crowdchange.help/ct/fundraiser-moderation-approval-smart-fundraiser-protection-admins
nav_path:
- 'Fundraiser Moderation: Approval & Smart Fundraiser Protection (Admins)'
nav_order: 144
parent: null
children: []
page_type: reference
tags:
- communications
- donations
- fundraiser-setup
- peer-to-peer
- teams
crm_relevant: false
description: 'CrowdChange provides two complementary systems to help you manage fundraiser quality and prevent spam on your site: Fundraiser Approval (manual review) Smart F…'
last_modified: '2026-06-03T15:42:02.258Z'
retrieved: '2026-10-14'
audience: Charity Admins (CrowdChange admin help center space CT)
word_count: 1131
---

<!-- Source: https://chadmin.crowdchange.help/ct/fundraiser-moderation-approval-smart-fundraiser-protection-admins | Nav: Fundraiser Moderation: Approval & Smart Fundraiser Protection (Admins) | Mirrored 2026-10-14 -->

# Fundraiser Moderation: Approval & Smart Fundraiser Protection (Admins)

CrowdChange provides two complementary systems to help you manage fundraiser quality and prevent spam on your site:

* **Fundraiser Approval** (manual review)

* **Smart Fundraiser Protection** (automated safeguards)

Together, these tools help you balance **control** , **security** , and **fundraiser speed**.

*** ** * ** ***

## 1. Overview

When a fundraiser is created on your site, it may either:

* **Go live instantly**, or

* Be placed in **Pending Approval** for review

This outcome depends on:

* Your **Fundraiser Approval setting**, and

* Whether the fundraiser is **flagged by Smart Fundraiser Protection**

*** ** * ** ***

## 2. Understanding Fundraiser Approval

Fundraiser Approval is a setting that allows your team to **manually review and approve all fundraisers before they go live**.

### When Approval is Enabled

* All new fundraisers are placed in **Pending Approval**

* Fundraisers **cannot accept donations** until approved

### When Approval is Disabled

* Fundraisers typically go live instantly

* Only flagged fundraisers (see below) require approval

*** ** * ** ***

### Benefits of Fundraiser Approval

* Full control over fundraiser content

* Ensures alignment with your organization's brand and policies

* Useful for regulated or high-visibility campaigns

*** ** * ** ***

### Considerations

* Introduces delays before fundraisers can begin

* Requires active monitoring by your team

* May impact fundraiser momentum and participation

*** ** * ** ***

## 3. What is Smart Fundraiser Protection?

Smart Fundraiser Protection is an automated system that reviews fundraisers **at the time of creation** to help prevent spam and suspicious activity.

### What it does

* Automatically evaluates fundraisers using a combination of signals, including:

  * Content quality (e.g., titles and descriptions)

  * Account credibility

  * Email verification status

### What happens next

* **Most fundraisers** → go live instantly

* **Suspicious fundraisers** → are flagged and placed in **Pending Approval**

This ensures that:

* Legitimate fundraisers are not delayed

* Potentially risky fundraisers are reviewed before going live

*** ** * ** ***

## 4. How These Systems Work Together

|  Configuration   |                                 Outcome                                  |
|------------------|--------------------------------------------------------------------------|
| **Approval OFF** | Most fundraisers go live instantly; flagged fundraisers require approval |
| **Approval ON**  | All fundraisers require approval before going live                       |

Smart Fundraiser Protection is always active and works in the background.

*** ** * ** ***

## 5. Email Verification \& Account Settings

### Requiring verified accounts to activate fundraisers

By default, a fundraiser must have a **verified email address** before it can go live. This helps keep spam and fake accounts off your site. You can control this behavior in **Admin → General Settings** with the setting:
> **"Users must have verified accounts to activate fundraisers."**

* **Enabled (default):** A new fundraiser stays inactive until its owner verifies their email. The owner sees a "verify your email" prompt with the option to resend the verification email.

* **Disabled:** New fundraisers can activate immediately without waiting for email verification. A verification email is still sent and the prompt still appears, but it no longer blocks the fundraiser from going live. Ownership reassignments also take effect immediately, without requiring the new owner to verify or accept.

Disabling this setting only affects the **email-verification step** . Smart Fundraiser Protection's spam and content safeguards stay active at all times. This option is most useful for organizations that create or reassign fundraisers **on behalf of** their participants.

### Assigning a fundraiser owner (admin-created fundraisers)

When an admin creates a fundraiser, you can set a **Fundraiser owner** by entering that person's email (and name, if they're a new user). The fundraiser owner is set as the **banking owner** for that fundraiser when user-level banking is used.

*** ** * ** ***

## 6. Why a Fundraiser May Be Inactive

An inactive fundraiser is not visible and cannot accept donations. The platform distinguishes between the common reasons so you can resolve them quickly:

* **Pending approval** --- awaiting manual review (see below)

* **Banking not set up** --- the fundraiser's banking details are incomplete

* **Unverified account** --- when the verified-accounts setting is enabled, the owner has not yet verified their email

*** ** * ** ***

## 7. Why a Fundraiser May Require Approval

A fundraiser may appear in **Pending Approval** for several reasons:

* Your organization has **Fundraiser Approval enabled**

* The fundraiser was **flagged by Smart Fundraiser Protection**, due to:

  * Suspicious or inappropriate content

  * Low-confidence user information

  * Lack of verified email

*** ** * ** ***

## 8. How to Approve or Reject a Fundraiser

If a fundraiser requires approval, follow these steps:

1. Go to the **Browse Fundraisers** page on your site

2. Click **Show All** , then select **Pending Approval**

3. Click on the fundraiser you want to review

4. Click **Manage Fundraiser** in the top right corner

5. *(Optional)* Review and update fundraiser details before approval

6. Click **Approve** to make the fundraiser live

To reject a fundraiser:

* Click **Reject** (this will remove the fundraiser from your site)

> **Note:** Once approved, a fundraiser can begin accepting donations immediately.

*** ** * ** ***

## 9. Best Practices

* **Review pending fundraisers regularly** to avoid delays for legitimate users

* Consider setting an internal response time (e.g., within 24 hours)

* If you prioritize speed, consider keeping Approval OFF and relying on Smart Fundraiser Protection

* Use Approval ON for campaigns requiring strict oversight

*** ** * ** ***

## 10. Frequently Asked Questions

### Why did one fundraiser go live instantly and another require approval?

This is expected behavior. Fundraisers that meet quality and trust checks go live instantly, while others may be flagged for review.

*** ** * ** ***

### Can I disable Smart Fundraiser Protection?

The spam and content safeguards (such as blocking inappropriate titles and flagging suspicious content) are platform-level and **cannot be turned off** . However, you *can* control the email-verification requirement: the **"Users must have verified accounts to activate fundraisers"** setting in **Admin → General Settings** lets you choose whether fundraisers must have a verified email before they go live. Disabling that setting does **not** turn off spam protection --- it only allows fundraisers to activate before email verification.

*** ** * ** ***

### What does the "verified accounts" setting do?

When enabled (the default), a fundraiser must have a verified email before it can go live. When disabled, fundraisers can activate immediately and ownership reassignments take effect right away --- useful if your team creates or reassigns fundraisers on behalf of your participants. The verification email is still sent either way.

*** ** * ** ***

### What happens if I don't approve a fundraiser?

The fundraiser will remain in **Pending Approval** and will not be visible or accept donations.

*** ** * ** ***

### Can I edit a fundraiser before approving it?

Yes. You can review and update fundraiser details before approving.

*** ** * ** ***

### What happens when I reject a fundraiser?

Rejecting a fundraiser removes it from your site. This action cannot be undone.

*** ** * ** ***

## 11. Additional Notes

* In some cases, fundraisers can only be edited from the site where they were created

  * For example, if a child site (sub-site) uses custom questions, you may be redirected to that site to make edits

* If a fundraiser is mistakenly approved, you can close it using:

  **How to Reopen or Close a Fundraiser**

*** ** * ** ***

## 12. Summary

CrowdChange's fundraiser moderation system is designed to:

* Keep fundraiser creation **fast and accessible**

* Reduce spam and malicious activity

* Give your team **flexible control** when needed

By combining **Smart Fundraiser Protection** with optional **Fundraiser Approval** --- and the ability to control email-verification requirements --- you can tailor the right balance for your organization.
