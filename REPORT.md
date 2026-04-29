# Invest — Top 15 report

_Generated: **2026-04-29 06:40 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T06:40:55Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **AFRM**, **ANET**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.323 | 1.372 | 1.372 | 100.0% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.761 | 1.139 | 1.139 | 98.7% | -8.5% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.066 | 0.852 | 0.852 | 97.4% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.802 | 0.743 | 0.743 | 96.2% | +26.1% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.361 | 0.560 | 0.560 | 94.9% | +8.7% | 27 | 3 | 0 | 11 | 0 |
| 6 | ★★ | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.285 | 0.529 | 0.529 | 93.6% | +25.2% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.157 | 0.476 | 0.476 | 92.3% | +9.3% | 62 | 5 | 0 | 27 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.005 | 0.413 | 0.413 | 91.0% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.909 | 0.373 | 0.373 | 89.7% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.777 | 0.318 | 0.318 | 88.5% | +2.6% | 29 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.756 | 0.310 | 0.310 | 87.2% | +6.6% | 13 | 9 | 0 | 9 | 0 |
| 12 |  | **AAPL** | Apple Inc. | Technology | 0.724 | 0.297 | 0.297 | 85.9% | +10.0% | 31 | 14 | 2 | 13 | 0 |
| 13 |  | **C** | Citigroup Inc. | Financial Services | 0.672 | 0.275 | 0.275 | 84.6% | +10.9% | 19 | 4 | 0 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.664 | 0.272 | 0.272 | 83.3% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.658 | 0.269 | 0.269 | 82.1% | +18.9% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.839 | 0.692 | 0.692 | 100.0% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.671 | 0.629 | 0.629 | 98.7% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.472 | 0.553 | 0.553 | 97.4% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.458 | 0.548 | 0.548 | 96.2% | +59.5% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.437 | 0.540 | 0.540 | 94.9% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.342 | 0.504 | 0.504 | 93.6% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.202 | 0.451 | 0.451 | 92.3% | +45.9% | 36 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.163 | 0.436 | 0.436 | 91.0% | +26.1% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.079 | 0.404 | 0.404 | 89.7% | +39.8% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.070 | 0.400 | 0.400 | 88.5% | +8.7% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.955 | 0.357 | 0.357 | 87.2% | +48.3% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.925 | 0.345 | 0.345 | 85.9% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.909 | 0.339 | 0.339 | 84.6% | +49.0% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.837 | 0.312 | 0.312 | 83.3% | +18.1% | 14 | 3 | 1 | 5 | 0 |
| 15 | ★★ | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.805 | 0.300 | 0.300 | 82.1% | +25.2% | 23 | 8 | 0 | 12 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.044 | 0.883 | 0.883 | 100.0% | +59.5% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.775 | 0.766 | 0.766 | 98.7% | +47.0% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.528 | 0.658 | 0.658 | 97.4% | +39.8% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.380 | 0.593 | 0.593 | 96.2% | +49.0% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.321 | 0.567 | 0.567 | 94.9% | +48.3% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.252 | 0.537 | 0.537 | 93.6% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.220 | 0.523 | 0.523 | 92.3% | +45.9% | 36 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.213 | 0.520 | 0.520 | 91.0% | +49.2% | 28 | 7 | 0 | 23 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.125 | 0.482 | 0.482 | 89.7% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.113 | 0.477 | 0.477 | 88.5% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.055 | 0.451 | 0.451 | 87.2% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.022 | 0.437 | 0.437 | 85.9% | +40.9% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.015 | 0.434 | 0.434 | 84.6% | +26.1% | 23 | 9 | 0 | 10 | 0 |
| 14 |  | **ABT** | Abbott Laboratories | Healthcare | 1.009 | 0.431 | 0.431 | 83.3% | +26.4% | 21 | 7 | 0 | 12 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.951 | 0.406 | 0.406 | 82.1% | +18.7% | 22 | 2 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-29 06:40:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 06:40:50Z |  |
| stooq.prices | ok | 0 | 2026-04-29 04:05:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 04:05:50Z |  |
| edgar.13f | error | 0 | 2026-04-29 01:18:49Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-29 01:18:48Z |  |
| yfinance.actions | ok | 1063 | 2026-04-29 01:18:37Z |  |
| yfinance.consensus | ok | 79 | 2026-04-29 01:18:19Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-29 01:17:54Z |  |
| yfinance.prices | ok | 7110 | 2026-04-29 01:17:45Z |  |
| stooq.prices | ok | 0 | 2026-04-29 00:10:53Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 00:10:48Z |  |
| stooq.prices | ok | 0 | 2026-04-28 23:13:27Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 23:13:21Z |  |
| stooq.prices | ok | 0 | 2026-04-28 22:14:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 22:14:20Z |  |
| stooq.prices | ok | 0 | 2026-04-28 21:06:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 21:06:39Z |  |
| stooq.prices | ok | 0 | 2026-04-28 19:41:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 19:40:54Z |  |
