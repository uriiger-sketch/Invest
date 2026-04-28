# Invest — Top 15 report

_Generated: **2026-04-28 19:41 UTC** · Scores as of: **2026-04-28**_

🟢 last successful crawl: 0 min ago (at 2026-04-28T19:41:04Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **APH**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 4.119 | 1.725 | 1.725 | 100.0% | +7.8% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.718 | 1.137 | 1.137 | 98.7% | +5.9% | 21 | 20 | 2 | 14 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.658 | 1.112 | 1.112 | 97.4% | -8.8% | 36 | 13 | 0 | 15 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.743 | 0.728 | 0.728 | 96.2% | +25.8% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.279 | 0.533 | 0.533 | 94.9% | +9.0% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.213 | 0.506 | 0.506 | 93.6% | +25.3% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.087 | 0.452 | 0.452 | 92.3% | +9.4% | 62 | 5 | 0 | 26 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.954 | 0.397 | 0.397 | 91.0% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.843 | 0.350 | 0.350 | 89.7% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.730 | 0.303 | 0.303 | 88.5% | +2.3% | 29 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.708 | 0.294 | 0.294 | 87.2% | +6.3% | 13 | 9 | 0 | 9 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.680 | 0.282 | 0.282 | 85.9% | +10.0% | 31 | 14 | 2 | 12 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.612 | 0.253 | 0.253 | 84.6% | +17.9% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **C** | Citigroup Inc. | Financial Services | 0.607 | 0.251 | 0.251 | 83.3% | +11.1% | 19 | 4 | 0 | 12 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.597 | 0.247 | 0.247 | 82.1% | +17.4% | 14 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.677 | 1.021 | 1.021 | 100.0% | +7.8% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.662 | 0.631 | 0.631 | 98.7% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.443 | 0.547 | 0.547 | 97.4% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.419 | 0.538 | 0.538 | 96.2% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.412 | 0.535 | 0.535 | 94.9% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.168 | 0.442 | 0.442 | 93.6% | +45.6% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.126 | 0.426 | 0.426 | 92.3% | +25.8% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.064 | 0.402 | 0.402 | 91.0% | +5.9% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.046 | 0.395 | 0.395 | 89.7% | +39.5% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.033 | 0.390 | 0.390 | 88.5% | +9.0% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.914 | 0.345 | 0.345 | 87.2% | +47.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.891 | 0.336 | 0.336 | 85.9% | +17.9% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.867 | 0.327 | 0.327 | 84.6% | +48.2% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.804 | 0.302 | 0.302 | 83.3% | +17.4% | 14 | 3 | 1 | 5 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.786 | 0.295 | 0.295 | 82.1% | +10.0% | 31 | 14 | 2 | 12 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.034 | 0.879 | 0.879 | 100.0% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.792 | 0.773 | 0.773 | 98.7% | +47.4% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.523 | 0.655 | 0.655 | 97.4% | +39.5% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.353 | 0.581 | 0.581 | 96.2% | +48.2% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.297 | 0.557 | 0.557 | 94.9% | +47.6% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.269 | 0.545 | 0.545 | 93.6% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.237 | 0.531 | 0.531 | 92.3% | +49.5% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.214 | 0.520 | 0.520 | 91.0% | +45.6% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.131 | 0.484 | 0.484 | 89.7% | +34.5% | 45 | 3 | 1 | 19 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.107 | 0.474 | 0.474 | 88.5% | +17.9% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.070 | 0.458 | 0.458 | 87.2% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.033 | 0.442 | 0.442 | 85.9% | +41.1% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **ABT** | Abbott Laboratories | Healthcare | 1.027 | 0.439 | 0.439 | 84.6% | +26.8% | 21 | 7 | 0 | 12 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.026 | 0.439 | 0.439 | 83.3% | +26.3% | 23 | 9 | 0 | 10 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.952 | 0.406 | 0.406 | 82.1% | +18.7% | 22 | 2 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-28 06:47:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 06:47:39Z |  |
| stooq.prices | ok | 0 | 2026-04-28 04:09:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 04:09:39Z |  |
| edgar.13f | error | 0 | 2026-04-28 01:16:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-28 01:16:32Z |  |
| yfinance.actions | ok | 1053 | 2026-04-28 01:16:25Z |  |
| yfinance.consensus | ok | 79 | 2026-04-28 01:16:15Z |  |
