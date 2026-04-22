# Invest — Top 15 report

_Generated: **2026-04-22 18:06 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T18:06:09Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BAC**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.852 | 1.635 | 1.635 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.272 | 1.388 | 1.388 | 98.7% | +13.0% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.298 | 0.974 | 0.974 | 97.4% | +23.2% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.994 | 0.844 | 0.844 | 96.2% | +9.6% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.646 | 0.696 | 0.696 | 94.9% | +3.5% | 8 | 7 | 3 | 5 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.147 | 0.484 | 0.484 | 93.6% | +5.6% | 41 | 12 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.041 | 0.439 | 0.439 | 92.3% | +17.3% | 23 | 8 | 0 | 12 | 0 |
| 8 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.011 | 0.426 | 0.426 | 91.0% | -2.7% | 36 | 13 | 0 | 16 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.938 | 0.395 | 0.395 | 89.7% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ARM** | Arm Holdings plc | Technology | 0.921 | 0.388 | 0.388 | 88.5% | -13.3% | 27 | 10 | 2 | 18 | 0 |
| 11 |  | **ANET** | Arista Networks, Inc. | Technology | 0.818 | 0.344 | 0.344 | 87.2% | +0.1% | 27 | 3 | 0 | 11 | 0 |
| 12 |  | **CLS** | Celestica Inc. | Technology | 0.771 | 0.324 | 0.324 | 85.9% | -2.7% | 18 | 2 | 0 | 6 | 0 |
| 13 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.741 | 0.311 | 0.311 | 84.6% | +11.3% | 63 | 5 | 0 | 27 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.667 | 0.280 | 0.280 | 83.3% | +3.0% | 29 | 6 | 0 | 16 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.538 | 0.225 | 0.225 | 82.1% | +17.9% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.339 | 0.919 | 0.919 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.332 | 0.916 | 0.916 | 98.7% | +13.0% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.949 | 0.765 | 0.765 | 97.4% | +23.2% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.739 | 0.682 | 0.682 | 96.2% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.489 | 0.583 | 0.583 | 94.9% | +49.6% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.440 | 0.564 | 0.564 | 93.6% | +51.0% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.130 | 0.441 | 0.441 | 92.3% | +36.3% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.040 | 0.406 | 0.406 | 91.0% | +56.8% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.006 | 0.392 | 0.392 | 89.7% | +37.5% | 22 | 2 | 0 | 6 | 0 |
| 10 |  | **DE** | Deere & Company | Industrials | 0.969 | 0.378 | 0.378 | 88.5% | +14.0% | 13 | 11 | 0 | 13 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.958 | 0.373 | 0.373 | 87.2% | +5.6% | 41 | 12 | 0 | 27 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.949 | 0.370 | 0.370 | 85.9% | +22.4% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.895 | 0.348 | 0.348 | 84.6% | +39.0% | 35 | 10 | 0 | 20 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.826 | 0.321 | 0.321 | 83.3% | +9.6% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.790 | 0.307 | 0.307 | 82.1% | +22.2% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.849 | 0.815 | 0.815 | 100.0% | +49.2% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.724 | 0.760 | 0.760 | 98.7% | +56.8% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.653 | 0.728 | 0.728 | 97.4% | +51.0% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.553 | 0.684 | 0.684 | 96.2% | +49.6% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.540 | 0.678 | 0.678 | 94.9% | +37.5% | 22 | 2 | 0 | 6 | 0 |
| 6 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.307 | 0.574 | 0.574 | 93.6% | +22.4% | 10 | 1 | 0 | 2 | 0 |
| 7 |  | **ABT** | Abbott Laboratories | Healthcare | 1.285 | 0.564 | 0.564 | 92.3% | +30.0% | 22 | 6 | 0 | 13 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.263 | 0.555 | 0.555 | 91.0% | +36.3% | 44 | 3 | 1 | 20 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.252 | 0.550 | 0.550 | 89.7% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.183 | 0.519 | 0.519 | 88.5% | +41.8% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.108 | 0.485 | 0.485 | 87.2% | +22.2% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.067 | 0.467 | 0.467 | 85.9% | +23.2% | 20 | 2 | 0 | 3 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.041 | 0.456 | 0.456 | 84.6% | +39.0% | 35 | 10 | 0 | 20 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.939 | 0.410 | 0.410 | 83.3% | +24.0% | 23 | 9 | 0 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.871 | 0.380 | 0.380 | 82.1% | +17.9% | 21 | 3 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 18:06:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 18:06:02Z |  |
| stooq.prices | ok | 0 | 2026-04-22 16:59:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 16:59:04Z |  |
| stooq.prices | ok | 0 | 2026-04-22 15:44:12Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-22 15:44:01Z |  |
| stooq.prices | ok | 0 | 2026-04-22 14:13:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 14:13:25Z |  |
| stooq.prices | ok | 0 | 2026-04-22 12:11:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 12:11:19Z |  |
| stooq.prices | ok | 0 | 2026-04-22 11:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 11:05:00Z |  |
| stooq.prices | ok | 0 | 2026-04-22 09:55:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 09:55:54Z |  |
| stooq.prices | ok | 0 | 2026-04-22 08:03:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 08:03:07Z |  |
| stooq.prices | ok | 0 | 2026-04-22 05:59:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 05:59:51Z |  |
| stooq.prices | ok | 0 | 2026-04-22 03:44:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 03:44:42Z |  |
