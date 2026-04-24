# Invest — Top 15 report

_Generated: **2026-04-24 18:03 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T18:03:42Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.757 | 1.574 | 1.574 | 100.0% | +10.3% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.256 | 1.364 | 1.364 | 98.7% | +14.9% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.284 | 0.956 | 0.956 | 97.4% | +9.9% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.110 | 0.883 | 0.883 | 96.2% | +5.8% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.441 | 0.602 | 0.602 | 94.9% | +3.3% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.116 | 0.465 | 0.465 | 93.6% | -16.1% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.033 | 0.431 | 0.431 | 92.3% | -27.5% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 0.993 | 0.413 | 0.413 | 91.0% | +0.3% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.915 | 0.381 | 0.381 | 89.7% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.893 | 0.372 | 0.372 | 88.5% | +23.8% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.859 | 0.357 | 0.357 | 87.2% | +7.6% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★ | **CRH** | CRH plc | Basic Materials | 0.788 | 0.327 | 0.327 | 85.9% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.746 | 0.310 | 0.310 | 84.6% | -2.5% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.551 | 0.228 | 0.228 | 83.3% | -4.5% | 18 | 2 | 0 | 6 | 0 |
| 15 |  | **APH** | Amphenol Corporation | Technology | 0.544 | 0.225 | 0.225 | 82.1% | +12.9% | 14 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.296 | 0.871 | 0.871 | 100.0% | +14.9% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.266 | 0.860 | 0.860 | 98.7% | +10.3% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.789 | 0.678 | 0.678 | 97.4% | +9.9% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.689 | 0.639 | 0.639 | 96.2% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.279 | 0.483 | 0.483 | 94.9% | +37.2% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **CRH** | CRH plc | Basic Materials | 1.250 | 0.472 | 0.472 | 93.6% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.243 | 0.469 | 0.469 | 92.3% | +55.0% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.043 | 0.393 | 0.393 | 91.0% | +40.1% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.028 | 0.387 | 0.387 | 89.7% | +50.0% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.986 | 0.371 | 0.371 | 88.5% | +41.8% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.928 | 0.349 | 0.349 | 87.2% | +52.7% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.925 | 0.348 | 0.348 | 85.9% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.857 | 0.322 | 0.322 | 84.6% | +17.0% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.811 | 0.304 | 0.304 | 83.3% | +3.3% | 21 | 20 | 2 | 14 | 0 |
| 15 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.801 | 0.301 | 0.301 | 82.1% | +5.8% | 16 | 1 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.803 | 0.767 | 0.767 | 100.0% | +55.0% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.593 | 0.677 | 0.677 | 98.7% | +40.1% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **FROG** | JFrog Ltd. | Technology | 1.461 | 0.620 | 0.620 | 97.4% | +51.4% | 20 | 1 | 0 | 9 | 0 |
| 4 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.435 | 0.609 | 0.609 | 96.2% | +38.6% | 32 | 1 | 0 | 19 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.417 | 0.601 | 0.601 | 94.9% | +52.7% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.288 | 0.545 | 0.545 | 93.6% | +50.0% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.280 | 0.542 | 0.542 | 92.3% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 8 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.276 | 0.541 | 0.541 | 91.0% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.236 | 0.523 | 0.523 | 89.7% | +37.2% | 44 | 3 | 1 | 20 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.201 | 0.508 | 0.508 | 88.5% | +24.0% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.139 | 0.482 | 0.482 | 87.2% | +30.1% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.053 | 0.444 | 0.444 | 85.9% | +41.8% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.020 | 0.430 | 0.430 | 84.6% | +42.3% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BAC** | Bank of America Corporation | Financial Services | 0.985 | 0.415 | 0.415 | 83.3% | +20.5% | 22 | 3 | 0 | 9 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.984 | 0.415 | 0.415 | 82.1% | +25.5% | 23 | 9 | 0 | 11 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 18:03:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 18:03:34Z |  |
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
