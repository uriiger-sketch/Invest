# Invest — Top 15 report

_Generated: **2026-04-27 18:52 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T18:52:50Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.807 | 1.597 | 1.597 | 100.0% | +7.6% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.000 | 1.258 | 1.258 | 98.7% | -12.3% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.642 | 1.108 | 1.108 | 97.4% | +4.2% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.889 | 0.791 | 0.791 | 96.2% | +16.7% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.312 | 0.549 | 0.549 | 94.9% | +4.7% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.135 | 0.474 | 0.474 | 93.6% | -3.7% | 18 | 2 | 0 | 7 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.059 | 0.442 | 0.442 | 92.3% | +22.2% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.942 | 0.393 | 0.393 | 91.0% | +25.4% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.918 | 0.383 | 0.383 | 89.7% | +21.4% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.902 | 0.376 | 0.376 | 88.5% | +8.6% | 63 | 5 | 0 | 26 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.691 | 0.288 | 0.288 | 87.2% | +15.0% | 14 | 3 | 1 | 5 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.670 | 0.279 | 0.279 | 85.9% | +1.1% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.634 | 0.264 | 0.264 | 84.6% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.581 | 0.242 | 0.242 | 83.3% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.555 | 0.231 | 0.231 | 82.1% | +14.4% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.539 | 0.952 | 0.952 | 100.0% | +7.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.696 | 0.635 | 0.635 | 98.7% | +25.4% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.434 | 0.535 | 0.535 | 97.4% | +59.9% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.393 | 0.520 | 0.520 | 96.2% | +21.4% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.328 | 0.496 | 0.496 | 94.9% | +33.0% | 45 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.099 | 0.409 | 0.409 | 93.6% | +43.8% | 35 | 10 | 0 | 20 | 0 |
| 7 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.028 | 0.382 | 0.382 | 92.3% | +4.2% | 21 | 20 | 2 | 14 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.028 | 0.382 | 0.382 | 91.0% | +38.3% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.992 | 0.369 | 0.369 | 89.7% | +16.7% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.980 | 0.364 | 0.364 | 88.5% | +4.7% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.979 | 0.364 | 0.364 | 87.2% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.917 | 0.340 | 0.340 | 85.9% | +48.1% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.888 | 0.330 | 0.330 | 84.6% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.883 | 0.327 | 0.327 | 83.3% | +13.8% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.829 | 0.307 | 0.307 | 82.1% | +15.0% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.083 | 0.890 | 0.890 | 100.0% | +59.9% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.610 | 0.686 | 0.686 | 98.7% | +42.3% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.512 | 0.643 | 0.643 | 97.4% | +38.3% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.344 | 0.571 | 0.571 | 96.2% | +48.1% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.309 | 0.556 | 0.556 | 94.9% | +45.4% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.283 | 0.544 | 0.544 | 93.6% | +25.4% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.233 | 0.523 | 0.523 | 92.3% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.216 | 0.516 | 0.516 | 91.0% | +48.5% | 28 | 7 | 0 | 23 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.183 | 0.501 | 0.501 | 89.7% | +43.8% | 35 | 10 | 0 | 20 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.160 | 0.491 | 0.491 | 88.5% | +33.0% | 45 | 3 | 1 | 20 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.089 | 0.461 | 0.461 | 87.2% | +28.1% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.066 | 0.451 | 0.451 | 85.9% | +20.0% | 22 | 2 | 0 | 8 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.039 | 0.439 | 0.439 | 84.6% | +26.1% | 23 | 9 | 0 | 11 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.992 | 0.419 | 0.419 | 83.3% | +39.7% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.969 | 0.409 | 0.409 | 82.1% | +21.4% | 19 | 2 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-27 18:52:49Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 18:52:44Z |  |
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
