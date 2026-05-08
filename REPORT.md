# Invest — Top 15 report

_Generated: **2026-05-08 09:20 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T09:19:59Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **AMZN**, **APH**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

## How to read this

| Column | What it means |
|---|---|
| **#** | Rank (1 = highest blended score in this horizon). |
| **★★ / ★★★** | Cross-horizon highlight. ★★ = this ticker ranks in two of the three top-15 lists; ★★★ (rare) = it's in all three. High-conviction names. |
| **Ticker** | Stock symbol as used on US exchanges. |
| **Name** | Company name from Yahoo Finance. |
| **Sector** | GICS sector classification. |
| **Blended** | Final score = 0.6 · z(composite) + 0.4 · z(ml). Z-scored across the universe for this horizon, so 0 is average. +1 ≈ 1 std-dev above the pack. Higher = more attractive. |
| **Composite** | Rule-based score from the weighted sum of nine transparent features (analyst consensus, price-target upside, rating momentum 7 d & 30 d, target revision 30 d, 13F institutional flow, insider net buy 90 d, 21-day price momentum, realised-volatility risk penalty). |
| **ML** | LightGBM regressor's predicted forward return for this horizon. Cold-start fallback = composite until ≥ 60 daily snapshots exist. |
| **Pctile** | Percentile of the blended score inside this horizon (100 % = top). |
| **Upside** | Analyst consensus price target / last close − 1. Positive = analysts think there is room above the current price. |
| **Buy / Hold / Sell** | Aggregated analyst rating counts (most recent consensus snapshot). Strong Buy + Buy are combined into 'Buy'; Strong Sell + Sell into 'Sell'. |
| **Firms** | Count of distinct sell-side analyst firms that have publicly issued an action (upgrade / downgrade / reiterate) on this ticker in the last 90 days — sourced from yfinance's upgrades/downgrades feed and Finnhub's upgrade-downgrade endpoint when a key is configured. The Buy / Hold / Sell columns aggregate the ratings of every firm that publicly covers the stock (typically 10–30 firms for US large caps, 5–15 for small caps, fewer for non-US). |
| **Insts** | Count of tracked institutional 13F filers (Berkshire, BlackRock, Bridgewater, Renaissance, Citadel, Tiger, ARK …) currently holding the stock in their most recent 13F-HR. |

## Days horizon — top 15

_5-day holding. Weights analyst rating momentum and short-term price momentum most; less weight on long-run price-target upside._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.731 | 1.767 | 1.767 | 100.0% | +6.0% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.926 | 1.465 | 1.465 | 98.7% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.746 | 0.646 | 0.646 | 97.4% | -6.2% | 44 | 3 | 1 | 16 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.390 | 0.512 | 0.512 | 96.2% | +11.0% | 17 | 1 | 0 | 8 | 0 |
| 5 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.979 | 0.358 | 0.358 | 94.9% | +16.8% | 10 | 4 | 0 | 11 | 0 |
| 6 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.978 | 0.358 | 0.358 | 93.6% | +14.6% | 62 | 4 | 0 | 29 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.918 | 0.335 | 0.335 | 92.3% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 8 | ★★ | **AAPL** | Apple Inc. | Technology | 0.891 | 0.325 | 0.325 | 91.0% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.644 | 0.232 | 0.232 | 89.7% | +4.3% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.598 | 0.215 | 0.215 | 88.5% | +26.6% | 21 | 2 | 0 | 3 | 0 |
| 11 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.579 | 0.208 | 0.208 | 87.2% | +17.4% | 22 | 8 | 0 | 6 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.567 | 0.203 | 0.203 | 85.9% | +6.3% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.522 | 0.186 | 0.186 | 84.6% | +19.0% | 27 | 3 | 1 | 6 | 0 |
| 14 | ★★ | **CVX** | Chevron Corporation | Energy | 0.506 | 0.180 | 0.180 | 83.3% | +17.8% | 18 | 6 | 1 | 11 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.468 | 0.166 | 0.166 | 82.1% | +15.0% | 10 | 1 | 0 | 3 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.981 | 0.719 | 0.719 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.844 | 0.669 | 0.669 | 98.7% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.810 | 0.656 | 0.656 | 97.4% | +6.0% | 40 | 10 | 0 | 22 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.530 | 0.553 | 0.553 | 96.2% | +26.6% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.517 | 0.549 | 0.549 | 94.9% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.165 | 0.419 | 0.419 | 93.6% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.144 | 0.411 | 0.411 | 92.3% | +17.8% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.076 | 0.386 | 0.386 | 91.0% | +44.6% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.050 | 0.377 | 0.377 | 89.7% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.912 | 0.326 | 0.326 | 88.5% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.847 | 0.302 | 0.302 | 87.2% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.830 | 0.296 | 0.296 | 85.9% | +14.6% | 62 | 4 | 0 | 29 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.790 | 0.281 | 0.281 | 84.6% | -6.2% | 44 | 3 | 1 | 16 | 0 |
| 14 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.788 | 0.280 | 0.280 | 83.3% | +36.4% | 21 | 7 | 0 | 11 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.781 | 0.278 | 0.278 | 82.1% | +5.5% | 31 | 15 | 2 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.599 | 1.148 | 1.148 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.085 | 0.919 | 0.919 | 98.7% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.668 | 0.733 | 0.733 | 97.4% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.357 | 0.594 | 0.594 | 96.2% | +36.4% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.263 | 0.553 | 0.553 | 94.9% | +44.6% | 35 | 10 | 0 | 21 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.260 | 0.551 | 0.551 | 93.6% | +26.6% | 21 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.217 | 0.532 | 0.532 | 92.3% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.143 | 0.499 | 0.499 | 91.0% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.093 | 0.477 | 0.477 | 89.7% | +22.6% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **ANET** | Arista Networks, Inc. | Technology | 1.054 | 0.459 | 0.459 | 88.5% | +32.2% | 26 | 2 | 0 | 13 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.005 | 0.438 | 0.438 | 87.2% | +19.9% | 22 | 2 | 0 | 10 | 0 |
| 12 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.976 | 0.424 | 0.424 | 85.9% | +31.0% | 30 | 7 | 0 | 24 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.970 | 0.422 | 0.422 | 84.6% | +38.3% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.954 | 0.415 | 0.415 | 83.3% | +24.4% | 24 | 8 | 0 | 9 | 0 |
| 15 |  | **BILL** | BILL Holdings, Inc. | Technology | 0.952 | 0.414 | 0.414 | 82.1% | +43.0% | 14 | 9 | 0 | 5 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 09:19:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 09:19:54Z |  |
| stooq.prices | ok | 0 | 2026-05-08 07:48:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 07:48:20Z |  |
| stooq.prices | ok | 0 | 2026-05-08 05:57:56Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 05:57:51Z |  |
| stooq.prices | ok | 0 | 2026-05-08 03:56:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 03:56:32Z |  |
| edgar.13f | error | 0 | 2026-05-08 01:20:06Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-08 01:20:05Z |  |
| yfinance.actions | ok | 1123 | 2026-05-08 01:19:56Z |  |
| yfinance.consensus | ok | 79 | 2026-05-08 01:19:40Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-08 01:19:15Z |  |
| yfinance.prices | ok | 7110 | 2026-05-08 01:19:06Z |  |
| stooq.prices | ok | 0 | 2026-05-08 00:10:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 00:10:38Z |  |
| stooq.prices | ok | 0 | 2026-05-07 23:02:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 23:02:46Z |  |
| stooq.prices | ok | 0 | 2026-05-07 21:57:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 21:57:38Z |  |
