# Invest — Top 15 report

_Generated: **2026-04-27 21:19 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T21:19:14Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.805 | 1.591 | 1.591 | 100.0% | +8.0% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.937 | 1.227 | 1.227 | 98.7% | -11.6% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.648 | 1.106 | 1.106 | 97.4% | +4.4% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.893 | 0.790 | 0.790 | 96.2% | +16.0% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.319 | 0.549 | 0.549 | 94.9% | +4.2% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.185 | 0.493 | 0.493 | 93.6% | -5.2% | 18 | 2 | 0 | 7 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.068 | 0.444 | 0.444 | 92.3% | +21.4% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.949 | 0.394 | 0.394 | 91.0% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.893 | 0.371 | 0.371 | 89.7% | +8.7% | 63 | 5 | 0 | 26 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.890 | 0.370 | 0.370 | 88.5% | +22.5% | 19 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.713 | 0.296 | 0.296 | 87.2% | +14.2% | 14 | 3 | 1 | 5 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.705 | 0.292 | 0.292 | 85.9% | +0.1% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.657 | 0.272 | 0.272 | 84.6% | +11.2% | 31 | 14 | 2 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.585 | 0.242 | 0.242 | 83.3% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.568 | 0.235 | 0.235 | 82.1% | +13.7% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.550 | 0.955 | 0.955 | 100.0% | +8.0% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.692 | 0.632 | 0.632 | 98.7% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.459 | 0.544 | 0.544 | 97.4% | +61.8% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.407 | 0.524 | 0.524 | 96.2% | +22.5% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.331 | 0.495 | 0.495 | 94.9% | +33.4% | 45 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.099 | 0.408 | 0.408 | 93.6% | +44.5% | 35 | 10 | 0 | 20 | 0 |
| 7 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.036 | 0.385 | 0.385 | 92.3% | +4.4% | 21 | 20 | 2 | 14 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.026 | 0.381 | 0.381 | 91.0% | +38.5% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.976 | 0.362 | 0.362 | 89.7% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.973 | 0.361 | 0.361 | 88.5% | +4.2% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.969 | 0.359 | 0.359 | 87.2% | +16.0% | 16 | 1 | 0 | 7 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.930 | 0.345 | 0.345 | 85.9% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.900 | 0.333 | 0.333 | 84.6% | +14.4% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.883 | 0.327 | 0.327 | 83.3% | +11.2% | 31 | 14 | 2 | 12 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.815 | 0.301 | 0.301 | 82.1% | +14.2% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.124 | 0.909 | 0.909 | 100.0% | +61.8% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.626 | 0.694 | 0.694 | 98.7% | +43.3% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.502 | 0.640 | 0.640 | 97.4% | +38.5% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.366 | 0.581 | 0.581 | 96.2% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.344 | 0.572 | 0.572 | 94.9% | +46.8% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.268 | 0.539 | 0.539 | 93.6% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.224 | 0.520 | 0.520 | 92.3% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.194 | 0.507 | 0.507 | 91.0% | +44.5% | 35 | 10 | 0 | 20 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.193 | 0.507 | 0.507 | 89.7% | +48.4% | 28 | 7 | 0 | 23 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.164 | 0.494 | 0.494 | 88.5% | +33.4% | 45 | 3 | 1 | 20 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.065 | 0.451 | 0.451 | 87.2% | +27.8% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.048 | 0.444 | 0.444 | 85.9% | +19.7% | 22 | 2 | 0 | 8 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.044 | 0.442 | 0.442 | 84.6% | +41.6% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.036 | 0.439 | 0.439 | 83.3% | +26.3% | 23 | 9 | 0 | 11 | 0 |
| 15 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.005 | 0.425 | 0.425 | 82.1% | +22.5% | 19 | 2 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-27 21:19:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 21:19:08Z |  |
| stooq.prices | ok | 0 | 2026-04-27 20:08:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 20:08:10Z |  |
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
