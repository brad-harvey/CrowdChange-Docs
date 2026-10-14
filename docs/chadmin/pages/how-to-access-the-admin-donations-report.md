---
title: How to Access the Admin Donations Report
slug: how-to-access-the-admin-donations-report
collection: chadmin
source_url: https://chadmin.crowdchange.help/ct/how-to-access-the-admin-donations-report
nav_path:
- How to Access the Admin Donations Report
nav_order: 58
parent: null
children:
- how-to-edit-display-name-comment-and-show-or-hide-
- how-to-move-general-donations-to-registrant-person
- beta-moving-a-transaction-to-a-different-fundraise
page_type: how-to
tags:
- donations
- payments-and-receipts
- reporting-and-data
crm_relevant: true
description: 'The Admin Donations Report allows you to: View detailed information for all transactions across your CrowdChange site. Edit public-facing donation information …'
last_modified: '2024-08-08T16:06:06.378Z'
retrieved: '2026-10-14'
audience: Charity Admins (CrowdChange admin help center space CT)
word_count: 586
---

<!-- Source: https://chadmin.crowdchange.help/ct/how-to-access-the-admin-donations-report | Nav: How to Access the Admin Donations Report | Mirrored 2026-10-14 -->

# How to Access the Admin Donations Report

The **Admin** **Donations Report**allows you to:

* View detailed information for all transactions across your CrowdChange site.

* Edit public-facing donation information (Displayed name, comment, and whether amount is shown).

* Edit donor's answers to custom checkout questions (on their request).

* Issue, re-issue, re-send, and download Tax Receipts.

* Refund transactions (fully or partially).

Please note that the report's default date range filter is set to **one month**.

Transactions are sorted by `fundraiser + id` in descending order. If you need to view all transactions by date for all fundraisers - you would need to manually sort them after opening the CSV file in Excel.

Larger datasets (10,000+ records) may take longer to generate. If you have not received exported data from your CrowdChange site after a few hours, please contact customer support.

To access this report, follow these simple steps:

1. Go to your CrowdChange site and **Log In**.

2. Click **Profile** in in the top right corner, then**Admin**.

3. Go to **Reports** **\> Donations Report**using the left sidebar.

   ![donationsreport3.png](../assets/how-to-access-the-admin-donations-report/donationsreport3.png)
4. To find a specific transaction, you can use the search bar to search by email, name, or transaction ID.

5. Click **Filters** in the top right corner to filter for a specific Time Period, Organization, Subsite, or Fundraiser. If you are using a site with Blueprints enabled, you will be able to filter by Blueprint as well. Be sure to click **Show results** to apply these filters.

   ![show results.png](../assets/how-to-access-the-admin-donations-report/show_results.png)
6. Clicking on a specific transaction will take you to the **transaction page** where you can see it's full details including purchase options, answers to custom questions, covered fees and more. From here you can:

   1. **Issue, Download, Re-send, or Re-issue Tax Receipts** within the **Tax Receipt** section.

      ![image-20230911-150212.png](/__attachments/a_fbd38ad15b836747c9f14be625a4c1cbac8b5fda1139ad98bfd2a9bcdb584d77/image-20230911-150212.png?cb=8077f53e4f5d680438cbda86a37c6bbf)
   2. [**Edit Display Name, Comment and Show or Hide Amount on a Donation**](how-to-edit-display-name-comment-and-show-or-hide-.md) by clicking **Edit** within the **Additional Information**section.

      ![image-20230911-150306.png](/__attachments/a_3ae67678514ba5bd1441e510ef023c514e2619cc0cb6b99900481482fe092ee4/image-20230911-150306.png?cb=a17eb133acb5ec0145bd46bb26d7e810)
   3. **View** and **Edit** answers to custom questions within the **Custom Questions** section.

      ![image-20230911-150356.png](/__attachments/a_30266385dcdbf3337fad58042fe89fb3ee46801df1c20e8a4758c8ec877147fb/image-20230911-150356.png?cb=8bb19f7d09ccbf40acf7a7eb750bd495)
   4. [**Issue a Full or Partial Refund**](how-to-issue-full-and-partial-refunds.md) by clicking **Refund** in the bottom right.

      ![move3.png](/__attachments/a_7e62e9c4fe6cc937df758d411d5478bfe77cadeb7edc5f9adaf9d3b5a66cb98f/move3.png?cb=7b23f0959525cfddccec2a39f84c5cb5)
7. Download the Excel CSV versions of this report by clicking **Download** and selecting either:

   1. **Summary Only** - Downloads a ZIP archive containing the Summary CSV file only.

   2. **Summary and transactions** - Downloads a ZIP archive containing the Summary, (all) Transactions and (all) Registrations CSV files.

   3. **Full detailed report** - Downloads a ZIP archive containing the Summary, (all) Transactions, (all) Registrations, and Failed transactions CSV files, as well as individual CSV files for each fundraiser's transactions which are named as follows: `f - {fundraiser ID}`.

      ![fulldetailedreport.png](/__attachments/a_f844750326d32f092579ca33fbcf3d9ed990d9688e2b97f0a345b83c80528df7/fulldetailedreport.png?cb=77ec3fcea0c0fb736d3f18a3860c4600)

**IMPORTANT:** If you are looking for the answers to**Custom Checkout Questions** in the Excel CSV reports, download the 'Full Detailed Report' and open your fundraiser's specific CSV file (Eg: f-7246).

The fundraiser ID is the number at the end of your main fundraising page's URL.

Once in the Excel CSV file, you must scroll horizontally all the way to the right. The answers to custom checkout questions will be in the last few columns.  
Re-issuing a tax receipt will **VOID** the initial receipt. This will be displayed within the Admin Tax Receipts report and a **VOID**stamp will be added to the PDF copy of the original receipt.

The donor will receive notification of this and the re-issued receipt will communicate that it is a replacement for the original receipt.
