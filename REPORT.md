# Invest — Top 15 report

_Generated: **2026-04-22 03:44 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T03:44:48Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.760 | 1.603 | 1.603 | 100.0% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.268 | 1.392 | 1.392 | 98.7% | +13.7% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.469 | 1.051 | 1.051 | 97.4% | +21.7% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.840 | 0.782 | 0.782 | 96.2% | +13.2% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.458 | 0.619 | 0.619 | 94.9% | +4.4% | 8 | 7 | 3 | 5 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.132 | 0.480 | 0.480 | 93.6% | +21.1% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **CLS** | Celestica Inc. | Technology | 1.043 | 0.441 | 0.441 | 92.3% | -1.8% | 18 | 2 | 0 | 6 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.035 | 0.438 | 0.438 | 91.0% | +9.0% | 41 | 12 | 0 | 27 | 0 |
| 9 |  | **ANET** | Arista Networks, Inc. | Technology | 0.829 | 0.350 | 0.350 | 89.7% | +2.6% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.824 | 0.348 | 0.348 | 88.5% | +23.0% | 27 | 3 | 1 | 7 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.745 | 0.314 | 0.314 | 87.2% | +13.1% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.733 | 0.309 | 0.309 | 85.9% | +2.8% | 36 | 13 | 0 | 16 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.600 | 0.252 | 0.252 | 84.6% | +4.7% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **ARM** | Arm Holdings plc | Technology | 0.586 | 0.246 | 0.246 | 83.3% | -3.4% | 27 | 10 | 2 | 18 | 0 |
| 15 |  | **C** | Citigroup Inc. | Financial Services | 0.567 | 0.238 | 0.238 | 82.1% | +8.1% | 18 | 4 | 0 | 12 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.355 | 0.931 | 0.931 | 100.0% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.325 | 0.919 | 0.919 | 98.7% | +13.7% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.965 | 0.776 | 0.776 | 97.4% | +21.7% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.680 | 0.663 | 0.663 | 96.2% | +23.0% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.497 | 0.590 | 0.590 | 94.9% | +50.0% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.379 | 0.543 | 0.543 | 93.6% | +47.1% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.187 | 0.467 | 0.467 | 92.3% | +38.0% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 0.986 | 0.387 | 0.387 | 91.0% | +62.4% | 32 | 1 | 0 | 18 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.979 | 0.384 | 0.384 | 89.7% | +53.2% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.976 | 0.383 | 0.383 | 88.5% | +9.0% | 41 | 12 | 0 | 27 | 0 |
| 11 |  | **DE** | Deere & Company | Industrials | 0.950 | 0.373 | 0.373 | 87.2% | +13.2% | 13 | 11 | 0 | 13 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.939 | 0.368 | 0.368 | 85.9% | +22.0% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.897 | 0.352 | 0.352 | 84.6% | +31.6% | 22 | 2 | 0 | 6 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.897 | 0.352 | 0.352 | 83.3% | +37.9% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.839 | 0.328 | 0.328 | 82.1% | +13.2% | 16 | 1 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.429 | 1.064 | 1.064 | 100.0% | +62.4% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.608 | 0.702 | 0.702 | 98.7% | +53.2% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.591 | 0.694 | 0.694 | 97.4% | +50.0% | 20 | 1 | 0 | 9 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.523 | 0.664 | 0.664 | 96.2% | +47.1% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.329 | 0.579 | 0.579 | 94.9% | +31.6% | 22 | 2 | 0 | 6 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.314 | 0.572 | 0.572 | 93.6% | +38.0% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.282 | 0.558 | 0.558 | 92.3% | +23.0% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **CRM** | Salesforce, Inc. | Technology | 1.282 | 0.558 | 0.558 | 91.0% | +43.7% | 35 | 10 | 1 | 24 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.281 | 0.558 | 0.558 | 89.7% | +22.0% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.253 | 0.545 | 0.545 | 88.5% | +28.9% | 22 | 6 | 0 | 13 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.118 | 0.486 | 0.486 | 87.2% | +22.3% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.992 | 0.430 | 0.430 | 85.9% | +37.9% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.975 | 0.423 | 0.423 | 84.6% | +21.7% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.845 | 0.365 | 0.365 | 83.3% | +21.6% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.828 | 0.358 | 0.358 | 82.1% | +17.1% | 21 | 3 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 03:44:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 03:44:42Z |  |
| stooq.prices | ok | 0 | 2026-04-22 00:06:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 00:06:30Z |  |
| edgar.13f | error | 0 | 2026-04-22 00:04:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-22 00:04:22Z |  |
| yfinance.actions | ok | 1022 | 2026-04-22 00:04:10Z |  |
| yfinance.consensus | ok | 79 | 2026-04-22 00:04:01Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-22 00:03:47Z |  |
| yfinance.prices | ok | 7110 | 2026-04-22 00:03:42Z |  |
| stooq.prices | ok | 0 | 2026-04-21 23:22:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 23:21:54Z |  |
| stooq.prices | ok | 0 | 2026-04-21 22:25:10Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-21 22:25:04Z |  |
| stooq.prices | ok | 0 | 2026-04-21 21:28:10Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 21:28:04Z |  |
| stooq.prices | ok | 0 | 2026-04-21 20:33:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 20:33:31Z |  |
| stooq.prices | ok | 0 | 2026-04-21 19:40:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 19:40:30Z |  |
