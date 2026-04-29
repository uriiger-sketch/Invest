# Invest — Top 15 report

_Generated: **2026-04-29 00:10 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T00:10:54Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.367 | 1.382 | 1.382 | 100.0% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.044 | 1.249 | 1.249 | 98.7% | -8.5% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.806 | 0.740 | 0.740 | 97.4% | +26.1% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.694 | 0.694 | 0.694 | 96.2% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.359 | 0.556 | 0.556 | 94.9% | +8.7% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.286 | 0.526 | 0.526 | 93.6% | +25.2% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.157 | 0.473 | 0.473 | 92.3% | +9.3% | 62 | 5 | 0 | 26 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.020 | 0.417 | 0.417 | 91.0% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.911 | 0.372 | 0.372 | 89.7% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.775 | 0.316 | 0.316 | 88.5% | +2.6% | 29 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.754 | 0.307 | 0.307 | 87.2% | +6.6% | 13 | 9 | 0 | 9 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.737 | 0.300 | 0.300 | 85.9% | +10.0% | 31 | 14 | 2 | 12 | 0 |
| 13 |  | **C** | Citigroup Inc. | Financial Services | 0.670 | 0.272 | 0.272 | 84.6% | +10.9% | 19 | 4 | 0 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.661 | 0.269 | 0.269 | 83.3% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.645 | 0.262 | 0.262 | 82.1% | +19.3% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.698 | 0.636 | 0.636 | 100.0% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.633 | 0.611 | 0.611 | 98.7% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.479 | 0.553 | 0.553 | 97.4% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.459 | 0.546 | 0.546 | 96.2% | +59.5% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.444 | 0.540 | 0.540 | 94.9% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.347 | 0.503 | 0.503 | 93.6% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.203 | 0.449 | 0.449 | 92.3% | +45.9% | 36 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.163 | 0.434 | 0.434 | 91.0% | +26.1% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.079 | 0.402 | 0.402 | 89.7% | +39.8% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.066 | 0.397 | 0.397 | 88.5% | +8.7% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.955 | 0.355 | 0.355 | 87.2% | +48.3% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.924 | 0.344 | 0.344 | 85.9% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.908 | 0.338 | 0.338 | 84.6% | +49.0% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.842 | 0.313 | 0.313 | 83.3% | +18.1% | 14 | 3 | 1 | 5 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.814 | 0.302 | 0.302 | 82.1% | +10.0% | 31 | 14 | 2 | 12 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.043 | 0.883 | 0.883 | 100.0% | +59.5% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.772 | 0.765 | 0.765 | 98.7% | +47.0% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.527 | 0.657 | 0.657 | 97.4% | +39.8% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.379 | 0.593 | 0.593 | 96.2% | +49.0% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.320 | 0.567 | 0.567 | 94.9% | +48.3% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.258 | 0.540 | 0.540 | 93.6% | +26.4% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.222 | 0.524 | 0.524 | 92.3% | +49.2% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.219 | 0.523 | 0.523 | 91.0% | +45.9% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.126 | 0.482 | 0.482 | 89.7% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.112 | 0.476 | 0.476 | 88.5% | +18.1% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.056 | 0.452 | 0.452 | 87.2% | +24.9% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.021 | 0.436 | 0.436 | 85.9% | +40.9% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.014 | 0.433 | 0.433 | 84.6% | +26.1% | 23 | 9 | 0 | 10 | 0 |
| 14 |  | **ABT** | Abbott Laboratories | Healthcare | 1.008 | 0.431 | 0.431 | 83.3% | +26.4% | 21 | 7 | 0 | 12 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.950 | 0.405 | 0.405 | 82.1% | +18.7% | 22 | 2 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-28 17:46:31Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 17:46:25Z |  |
| stooq.prices | ok | 0 | 2026-04-28 15:42:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 15:42:01Z |  |
| stooq.prices | ok | 0 | 2026-04-28 13:18:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 13:18:21Z |  |
| stooq.prices | ok | 0 | 2026-04-28 11:24:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 11:24:40Z |  |
| stooq.prices | ok | 0 | 2026-04-28 09:21:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 09:21:05Z |  |
