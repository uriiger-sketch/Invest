# Invest — Top 15 report

_Generated: **2026-04-27 17:21 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T17:21:50Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **APH**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.805 | 1.600 | 1.600 | 100.0% | +7.7% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.975 | 1.250 | 1.250 | 98.7% | -11.3% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.653 | 1.114 | 1.114 | 97.4% | +3.8% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.866 | 0.783 | 0.783 | 96.2% | +18.3% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.336 | 0.560 | 0.560 | 94.9% | +4.7% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.112 | 0.466 | 0.466 | 93.6% | -2.5% | 18 | 2 | 0 | 7 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.073 | 0.449 | 0.449 | 92.3% | +22.8% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.970 | 0.405 | 0.405 | 91.0% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.932 | 0.390 | 0.390 | 89.7% | +8.1% | 63 | 5 | 0 | 26 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.908 | 0.380 | 0.380 | 88.5% | +22.1% | 19 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.696 | 0.290 | 0.290 | 87.2% | +15.3% | 14 | 3 | 1 | 5 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.665 | 0.277 | 0.277 | 85.9% | +1.5% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.644 | 0.268 | 0.268 | 84.6% | +11.5% | 31 | 14 | 2 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.580 | 0.241 | 0.241 | 83.3% | +20.1% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.569 | 0.237 | 0.237 | 82.1% | +14.6% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.532 | 0.953 | 0.953 | 100.0% | +7.7% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.675 | 0.628 | 0.628 | 98.7% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.462 | 0.548 | 0.548 | 97.4% | +60.9% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.402 | 0.525 | 0.525 | 96.2% | +22.1% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.339 | 0.501 | 0.501 | 94.9% | +33.4% | 45 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.085 | 0.405 | 0.405 | 93.6% | +42.5% | 35 | 10 | 0 | 20 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.023 | 0.382 | 0.382 | 92.3% | +38.1% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.017 | 0.379 | 0.379 | 91.0% | +18.3% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.014 | 0.378 | 0.378 | 89.7% | +3.8% | 21 | 20 | 2 | 14 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.982 | 0.366 | 0.366 | 88.5% | +4.7% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.980 | 0.365 | 0.365 | 87.2% | +20.1% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.915 | 0.341 | 0.341 | 85.9% | +47.8% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.884 | 0.329 | 0.329 | 84.6% | +14.5% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.877 | 0.326 | 0.326 | 83.3% | +11.5% | 31 | 14 | 2 | 12 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.832 | 0.309 | 0.309 | 82.1% | +15.3% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.137 | 0.913 | 0.913 | 100.0% | +60.9% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.579 | 0.672 | 0.672 | 98.7% | +41.2% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.509 | 0.642 | 0.642 | 97.4% | +38.1% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.343 | 0.570 | 0.570 | 96.2% | +47.8% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.334 | 0.566 | 0.566 | 94.9% | +45.8% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.240 | 0.526 | 0.526 | 93.6% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.240 | 0.526 | 0.526 | 92.3% | +20.1% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.183 | 0.501 | 0.501 | 91.0% | +33.4% | 45 | 3 | 1 | 20 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.176 | 0.498 | 0.498 | 89.7% | +47.3% | 28 | 7 | 0 | 23 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.141 | 0.483 | 0.483 | 88.5% | +42.5% | 35 | 10 | 0 | 20 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.089 | 0.460 | 0.460 | 87.2% | +28.0% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.080 | 0.456 | 0.456 | 85.9% | +20.3% | 22 | 2 | 0 | 8 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.014 | 0.428 | 0.428 | 84.6% | +25.4% | 23 | 9 | 0 | 11 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.992 | 0.419 | 0.419 | 83.3% | +22.1% | 19 | 2 | 0 | 3 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.982 | 0.415 | 0.415 | 82.1% | +39.3% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-27 17:21:50Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 17:21:42Z |  |
| stooq.prices | ok | 0 | 2026-04-27 15:48:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 15:48:08Z |  |
| stooq.prices | ok | 0 | 2026-04-27 13:51:27Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 13:51:23Z |  |
| stooq.prices | ok | 0 | 2026-04-27 11:52:11Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 11:52:02Z |  |
| stooq.prices | ok | 0 | 2026-04-27 09:59:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 09:59:07Z |  |
| stooq.prices | ok | 0 | 2026-04-27 07:34:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 07:34:20Z |  |
| stooq.prices | ok | 0 | 2026-04-27 04:44:00Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 04:43:54Z |  |
| stooq.prices | ok | 0 | 2026-04-27 01:13:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 01:13:43Z |  |
| edgar.13f | error | 0 | 2026-04-27 00:08:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-27 00:08:21Z |  |
| yfinance.actions | ok | 1056 | 2026-04-27 00:08:13Z |  |
| yfinance.consensus | ok | 79 | 2026-04-27 00:07:59Z |  |
