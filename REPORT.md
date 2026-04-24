# Invest — Top 15 report

_Generated: **2026-04-24 17:16 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T17:16:44Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.763 | 1.577 | 1.577 | 100.0% | +10.3% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.249 | 1.361 | 1.361 | 98.7% | +15.2% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.278 | 0.953 | 0.953 | 97.4% | +10.4% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.088 | 0.873 | 0.873 | 96.2% | +6.8% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.445 | 0.603 | 0.603 | 94.9% | +3.4% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.131 | 0.471 | 0.471 | 93.6% | -16.0% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.029 | 0.429 | 0.429 | 92.3% | -27.0% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 1.006 | 0.419 | 0.419 | 91.0% | +0.4% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.919 | 0.383 | 0.383 | 89.7% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.897 | 0.373 | 0.373 | 88.5% | +24.1% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.862 | 0.359 | 0.359 | 87.2% | +7.9% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★ | **CRH** | CRH plc | Basic Materials | 0.790 | 0.328 | 0.328 | 85.9% | +20.9% | 19 | 2 | 0 | 3 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.755 | 0.314 | 0.314 | 84.6% | -2.4% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.563 | 0.233 | 0.233 | 83.3% | -4.4% | 18 | 2 | 0 | 6 | 0 |
| 15 |  | **APH** | Amphenol Corporation | Technology | 0.556 | 0.230 | 0.230 | 82.1% | +12.8% | 14 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.294 | 0.870 | 0.870 | 100.0% | +15.2% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.265 | 0.859 | 0.859 | 98.7% | +10.3% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.795 | 0.680 | 0.680 | 97.4% | +10.4% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.683 | 0.637 | 0.637 | 96.2% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.295 | 0.489 | 0.489 | 94.9% | +38.8% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.250 | 0.472 | 0.472 | 93.6% | +56.2% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **CRH** | CRH plc | Basic Materials | 1.249 | 0.471 | 0.471 | 92.3% | +20.9% | 19 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.084 | 0.408 | 0.408 | 91.0% | +53.7% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.033 | 0.389 | 0.389 | 89.7% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.973 | 0.366 | 0.366 | 88.5% | +41.7% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.918 | 0.345 | 0.345 | 87.2% | +20.9% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.917 | 0.345 | 0.345 | 85.9% | +53.1% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.850 | 0.319 | 0.319 | 84.6% | +16.8% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.814 | 0.305 | 0.305 | 83.3% | +6.8% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.813 | 0.305 | 0.305 | 82.1% | +3.4% | 21 | 20 | 2 | 14 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.827 | 0.777 | 0.777 | 100.0% | +56.2% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.582 | 0.672 | 0.672 | 98.7% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **FROG** | JFrog Ltd. | Technology | 1.455 | 0.617 | 0.617 | 97.4% | +51.8% | 20 | 1 | 0 | 9 | 0 |
| 4 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.418 | 0.601 | 0.601 | 96.2% | +38.6% | 32 | 1 | 0 | 19 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.408 | 0.597 | 0.597 | 94.9% | +53.1% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.408 | 0.597 | 0.597 | 93.6% | +53.7% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.280 | 0.542 | 0.542 | 92.3% | +38.8% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.269 | 0.537 | 0.537 | 91.0% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.261 | 0.534 | 0.534 | 89.7% | +20.9% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.186 | 0.501 | 0.501 | 88.5% | +23.9% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.124 | 0.475 | 0.475 | 87.2% | +30.0% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.057 | 0.446 | 0.446 | 85.9% | +43.9% | 18 | 10 | 0 | 12 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.030 | 0.434 | 0.434 | 84.6% | +41.7% | 35 | 10 | 0 | 20 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.985 | 0.415 | 0.415 | 83.3% | +25.9% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.973 | 0.410 | 0.410 | 82.1% | +20.5% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 17:16:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 17:16:36Z |  |
| stooq.prices | ok | 0 | 2026-04-24 16:04:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 16:04:44Z |  |
| stooq.prices | ok | 0 | 2026-04-24 14:45:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 14:45:06Z |  |
| stooq.prices | ok | 0 | 2026-04-24 12:42:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 12:42:38Z |  |
| stooq.prices | ok | 0 | 2026-04-24 11:37:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 11:37:32Z |  |
| stooq.prices | ok | 0 | 2026-04-24 10:13:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 10:13:04Z |  |
| stooq.prices | ok | 0 | 2026-04-24 08:25:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 08:25:41Z |  |
| stooq.prices | ok | 0 | 2026-04-24 06:08:27Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-24 06:08:18Z |  |
| stooq.prices | ok | 0 | 2026-04-24 03:54:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 03:54:08Z |  |
| edgar.13f | error | 0 | 2026-04-24 00:11:13Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-24 00:11:12Z |  |
