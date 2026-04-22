# Invest — Top 15 report

_Generated: **2026-04-22 16:59 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T16:59:10Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.831 | 1.633 | 1.633 | 100.0% | +9.2% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.243 | 1.382 | 1.382 | 98.7% | +13.1% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.323 | 0.989 | 0.989 | 97.4% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.996 | 0.849 | 0.849 | 96.2% | +11.0% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.644 | 0.698 | 0.698 | 94.9% | +3.5% | 8 | 7 | 3 | 5 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.141 | 0.484 | 0.484 | 93.6% | +5.9% | 41 | 12 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.025 | 0.434 | 0.434 | 92.3% | +18.7% | 23 | 8 | 0 | 12 | 0 |
| 8 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.017 | 0.431 | 0.431 | 91.0% | -1.8% | 36 | 13 | 0 | 16 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.938 | 0.397 | 0.397 | 89.7% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ARM** | Arm Holdings plc | Technology | 0.897 | 0.379 | 0.379 | 88.5% | -12.0% | 27 | 10 | 2 | 18 | 0 |
| 11 |  | **ANET** | Arista Networks, Inc. | Technology | 0.824 | 0.348 | 0.348 | 87.2% | +0.6% | 27 | 3 | 0 | 11 | 0 |
| 12 |  | **CLS** | Celestica Inc. | Technology | 0.771 | 0.325 | 0.325 | 85.9% | -1.9% | 18 | 2 | 0 | 6 | 0 |
| 13 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.739 | 0.312 | 0.312 | 84.6% | +11.9% | 63 | 5 | 0 | 27 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.664 | 0.280 | 0.280 | 83.3% | +3.6% | 29 | 6 | 0 | 16 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.547 | 0.229 | 0.229 | 82.1% | +17.9% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.336 | 0.920 | 0.920 | 100.0% | +9.2% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.316 | 0.912 | 0.912 | 98.7% | +13.1% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.935 | 0.762 | 0.762 | 97.4% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.735 | 0.682 | 0.682 | 96.2% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.506 | 0.591 | 0.591 | 94.9% | +50.3% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.460 | 0.573 | 0.573 | 93.6% | +51.7% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.142 | 0.447 | 0.447 | 92.3% | +37.1% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.032 | 0.404 | 0.404 | 91.0% | +56.4% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.989 | 0.387 | 0.387 | 89.7% | +36.5% | 22 | 2 | 0 | 6 | 0 |
| 10 |  | **DE** | Deere & Company | Industrials | 0.959 | 0.375 | 0.375 | 88.5% | +13.8% | 13 | 11 | 0 | 13 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.957 | 0.374 | 0.374 | 87.2% | +5.9% | 41 | 12 | 0 | 27 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.946 | 0.370 | 0.370 | 85.9% | +22.4% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.916 | 0.358 | 0.358 | 84.6% | +40.0% | 35 | 10 | 0 | 20 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.860 | 0.336 | 0.336 | 83.3% | +11.0% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.774 | 0.301 | 0.301 | 82.1% | +21.3% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.901 | 0.837 | 0.837 | 100.0% | +50.2% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.720 | 0.757 | 0.757 | 98.7% | +56.4% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.689 | 0.743 | 0.743 | 97.4% | +51.7% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.588 | 0.698 | 0.698 | 96.2% | +50.3% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.508 | 0.662 | 0.662 | 94.9% | +36.5% | 22 | 2 | 0 | 6 | 0 |
| 6 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.306 | 0.573 | 0.573 | 93.6% | +22.4% | 10 | 1 | 0 | 2 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.299 | 0.570 | 0.570 | 92.3% | +37.1% | 44 | 3 | 1 | 20 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.288 | 0.564 | 0.564 | 91.0% | +29.9% | 22 | 6 | 0 | 13 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.251 | 0.548 | 0.548 | 89.7% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.176 | 0.515 | 0.515 | 88.5% | +41.4% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.083 | 0.473 | 0.473 | 87.2% | +40.0% | 35 | 10 | 0 | 20 | 0 |
| 12 | ★★ | **CI** | The Cigna Group | Healthcare | 1.071 | 0.468 | 0.468 | 85.9% | +21.3% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.032 | 0.451 | 0.451 | 84.6% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.920 | 0.401 | 0.401 | 83.3% | +23.5% | 23 | 9 | 0 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.866 | 0.377 | 0.377 | 82.1% | +17.9% | 21 | 3 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-22 00:06:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 00:06:30Z |  |
