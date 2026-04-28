# Invest — Top 15 report

_Generated: **2026-04-28 15:42 UTC** · Scores as of: **2026-04-28**_

🟢 last successful crawl: 0 min ago (at 2026-04-28T15:42:07Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 4.092 | 1.713 | 1.713 | 100.0% | +8.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.745 | 1.148 | 1.148 | 98.7% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.601 | 1.088 | 1.088 | 97.4% | -7.2% | 36 | 13 | 0 | 15 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.807 | 0.755 | 0.755 | 96.2% | +25.7% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.265 | 0.527 | 0.527 | 94.9% | +24.9% | 23 | 8 | 0 | 12 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.262 | 0.526 | 0.526 | 93.6% | +9.9% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.113 | 0.463 | 0.463 | 92.3% | +9.3% | 62 | 5 | 0 | 26 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.971 | 0.404 | 0.404 | 91.0% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.860 | 0.357 | 0.357 | 89.7% | +24.8% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.741 | 0.307 | 0.307 | 88.5% | +2.4% | 29 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.727 | 0.301 | 0.301 | 87.2% | +6.3% | 13 | 9 | 0 | 9 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.678 | 0.281 | 0.281 | 85.9% | +10.2% | 31 | 14 | 2 | 12 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.619 | 0.256 | 0.256 | 84.6% | +17.8% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **C** | Citigroup Inc. | Financial Services | 0.617 | 0.255 | 0.255 | 83.3% | +11.1% | 19 | 4 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.610 | 0.253 | 0.253 | 82.1% | +18.8% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.692 | 1.028 | 1.028 | 100.0% | +8.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.650 | 0.628 | 0.628 | 98.7% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.447 | 0.550 | 0.550 | 97.4% | +61.0% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.436 | 0.546 | 0.546 | 96.2% | +34.3% | 45 | 3 | 1 | 19 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.405 | 0.534 | 0.534 | 94.9% | +24.8% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.189 | 0.451 | 0.451 | 93.6% | +47.1% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.147 | 0.435 | 0.435 | 92.3% | +25.7% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.059 | 0.401 | 0.401 | 91.0% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.055 | 0.399 | 0.399 | 89.7% | +40.5% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.048 | 0.397 | 0.397 | 88.5% | +9.9% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.910 | 0.344 | 0.344 | 87.2% | +50.9% | 20 | 1 | 0 | 9 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.906 | 0.342 | 0.342 | 85.9% | +47.6% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.888 | 0.335 | 0.335 | 84.6% | +17.8% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.817 | 0.308 | 0.308 | 83.3% | +18.4% | 14 | 3 | 1 | 5 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.788 | 0.297 | 0.297 | 82.1% | +10.2% | 31 | 14 | 2 | 12 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.108 | 0.909 | 0.909 | 100.0% | +61.0% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.725 | 0.742 | 0.742 | 98.7% | +45.5% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.560 | 0.670 | 0.670 | 97.4% | +40.5% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.457 | 0.625 | 0.625 | 96.2% | +50.9% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.296 | 0.555 | 0.555 | 94.9% | +47.6% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.266 | 0.542 | 0.542 | 93.6% | +47.1% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.249 | 0.534 | 0.534 | 92.3% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.218 | 0.521 | 0.521 | 91.0% | +49.0% | 28 | 7 | 0 | 23 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.119 | 0.478 | 0.478 | 89.7% | +34.3% | 45 | 3 | 1 | 19 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.101 | 0.470 | 0.470 | 88.5% | +17.8% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.055 | 0.450 | 0.450 | 87.2% | +24.8% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ABT** | Abbott Laboratories | Healthcare | 1.021 | 0.435 | 0.435 | 85.9% | +26.5% | 21 | 7 | 0 | 12 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.000 | 0.426 | 0.426 | 84.6% | +25.6% | 23 | 9 | 0 | 10 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.973 | 0.414 | 0.414 | 83.3% | +39.6% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.899 | 0.382 | 0.382 | 82.1% | +17.5% | 22 | 2 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-04-28 01:15:58Z |  |
| yfinance.prices | ok | 7110 | 2026-04-28 01:15:52Z |  |
| stooq.prices | ok | 0 | 2026-04-28 00:09:42Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 00:09:36Z |  |
