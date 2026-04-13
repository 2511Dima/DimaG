# Project Descriptions

---

## hardClicker.py — Automated Test Passer

### Description:

A tool for automatically passing online tests for medical professionals. It can be used in different fields that require accreditation (for example, obstetricians need to pass around 100 tests).

### Problem Solved:

Saves time when completing tests.

### Advantages:

* Completes any test in about 5 minutes. For example, 100 tests can be done in ~8 hours instead of 60 hours.
* Automatically logs in and selects correct answers using a Chrome extension.
* Works in the background and simulates user behavior (without breaking site rules and respecting time limits).

### Requirements:

* Path to the extension (download link provided)
* Login and password for the website
* List of tests

### Last Used:

12.2024

---

## AutoUTM_orig.py — Salebot → Google Sheets Analytics Transfer

### Description:

This service transfers analytics data from Salebot tables to Google Sheets without using internal credits of the Salebot platform.

### Problem Solved:

Automates reporting, conversion calculations, and improves data handling (Salebot does not allow full analytics directly inside its tables).

### Advantages:

* Saves time (about 2 hours for each calculation).
* Reduces costs by bypassing platform limits.
* Allows analytics creation and data visualization.

### Requirements:

* Link to the table in Salebot
* Cookies for Salebot login
* Google Sheets service account credentials
* Name of the Google Sheet

### Last Used:

11.2025

---

## RssSpamer.py — AI News Aggregator

### Description:

A bot that collects news from different websites and posts them to a Telegram channel, adding AI-based text processing.

### Problem Solved:

Automates content creation and adapts news to the target audience (RAG system).

### Advantages:

* Fully automated posting (every 4 hours).
* AI-based text processing.
* Suitable for niche or themed channels.

### Requirements:

* Telegram bot token (from @FatherBot)
* Telegram chat ID

### Last Used:

07.2024

---

## Reklamagorodbot.py — Multi-Admin Support Bot

### Description:

A bot for managing customer messages. All requests are sent to one shared interface for multiple administrators.

### Problem Solved:

Reduces manager workload and simplifies communication with clients.

### Advantages:

* Supports multiple admins using one account.
* Simplifies interaction with customers.
* Good for small businesses and marketing agencies.

### Requirements:

* Telegram bot token (from @FatherBot)
* Telegram chat ID
* Telegram username

### Last Used:

07.2024

---

## parser.py — VK Post Parser

### Description:

Gets the latest post from any VK community and sends it to your Telegram.

### Problem Solved:

Automates content reposting to news or themed channels.

### Advantages:

* Removes the need for manual searching and copying posts.
* Allows setting custom update frequency.
* Can fully replace a content manager for posting news.

### Requirements:

* Telegram bot token (from @FatherBot)
* VK API token

### Last Used:

08.2024

---

## files_deals.py — Table Processing Module (.csv, .pickle, .txt)

### Description:

This file contains a set of functions for loading, processing, and saving tabular data from CSV files.

### Main Features:

* Load multiple CSV files and merge them into one table
* Automatically replace empty values with `None`
* Get rows and columns by index or number
* Detect and set column data types
* Modify single values or entire columns
* Save results to CSV or binary `.pickle` format
* Helper functions for filtering, calculations, and displaying data

This module works as a simple API for table processing without using large libraries like pandas.

### How to Use:

At the end of the file, there are comments with functions that can be called in any order.

### Requirements:

* Exact file paths (and file names if needed)

### Example Files:

* `Group.csv`
* `Group.pickle`
* `Group2.csv`

### Last Used:

11.2025
