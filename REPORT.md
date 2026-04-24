# Invest — Top 15 report

_Generated: **2026-04-24 20:04 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T20:04:10Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.751 | 1.582 | 1.582 | 100.0% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.243 | 1.367 | 1.367 | 98.7% | +14.3% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.289 | 0.964 | 0.964 | 97.4% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.078 | 0.875 | 0.875 | 96.2% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.450 | 0.609 | 0.609 | 94.9% | +2.8% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.136 | 0.477 | 0.477 | 93.6% | -15.9% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.069 | 0.448 | 0.448 | 92.3% | -27.8% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 0.958 | 0.402 | 0.402 | 91.0% | +1.6% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.921 | 0.386 | 0.386 | 89.7% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.913 | 0.382 | 0.382 | 88.5% | +23.9% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.875 | 0.366 | 0.366 | 87.2% | +7.4% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★ | **CRH** | CRH plc | Basic Materials | 0.780 | 0.326 | 0.326 | 85.9% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.719 | 0.300 | 0.300 | 84.6% | -1.6% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.535 | 0.223 | 0.223 | 83.3% | +13.4% | 14 | 3 | 1 | 5 | 0 |
| 15 |  | **CLS** | Celestica Inc. | Technology | 0.533 | 0.222 | 0.222 | 82.1% | -3.6% | 18 | 2 | 0 | 6 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.277 | 0.866 | 0.866 | 100.0% | +14.3% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.254 | 0.857 | 0.857 | 98.7% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.782 | 0.676 | 0.676 | 97.4% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.685 | 0.639 | 0.639 | 96.2% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.290 | 0.488 | 0.488 | 94.9% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.278 | 0.483 | 0.483 | 93.6% | +36.8% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★ | **CRH** | CRH plc | Basic Materials | 1.258 | 0.476 | 0.476 | 92.3% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.066 | 0.402 | 0.402 | 91.0% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.054 | 0.398 | 0.398 | 89.7% | +50.6% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.004 | 0.379 | 0.379 | 88.5% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.921 | 0.347 | 0.347 | 87.2% | +20.8% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.902 | 0.340 | 0.340 | 85.9% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.865 | 0.326 | 0.326 | 84.6% | +18.2% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.825 | 0.310 | 0.310 | 83.3% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.798 | 0.300 | 0.300 | 82.1% | +2.8% | 21 | 20 | 2 | 14 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.890 | 0.804 | 0.804 | 100.0% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.643 | 0.698 | 0.698 | 98.7% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.502 | 0.637 | 0.637 | 97.4% | +40.3% | 32 | 1 | 0 | 19 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.418 | 0.601 | 0.601 | 96.2% | +49.8% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.366 | 0.579 | 0.579 | 94.9% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.328 | 0.563 | 0.563 | 93.6% | +50.6% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.273 | 0.539 | 0.539 | 92.3% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 8 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.267 | 0.536 | 0.536 | 91.0% | +20.8% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.229 | 0.520 | 0.520 | 89.7% | +36.8% | 44 | 3 | 1 | 20 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.157 | 0.489 | 0.489 | 88.5% | +22.7% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.150 | 0.486 | 0.486 | 87.2% | +30.2% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.079 | 0.455 | 0.455 | 85.9% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.985 | 0.415 | 0.415 | 84.6% | +20.5% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.985 | 0.415 | 0.415 | 83.3% | +25.5% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.965 | 0.406 | 0.406 | 82.1% | +40.5% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 20:04:10Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 20:04:05Z |  |
| stooq.prices | ok | 0 | 2026-04-24 19:15:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 19:15:40Z |  |
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
