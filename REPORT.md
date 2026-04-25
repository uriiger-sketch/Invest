# Invest — Top 15 report

_Generated: **2026-04-25 22:36 UTC** · Scores as of: **2026-04-25**_

🟢 last successful crawl: 0 min ago (at 2026-04-25T22:36:44Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.911 | 1.597 | 1.597 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.272 | 1.335 | 1.335 | 98.7% | +2.8% | 21 | 20 | 2 | 14 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.218 | 0.903 | 0.903 | 97.4% | -15.9% | 36 | 13 | 0 | 16 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.194 | 0.893 | 0.893 | 96.2% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ANET** | Arista Networks, Inc. | Technology | 1.064 | 0.430 | 0.430 | 94.9% | +1.6% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.992 | 0.401 | 0.401 | 93.6% | +23.9% | 23 | 8 | 0 | 12 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.971 | 0.392 | 0.392 | 92.3% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.953 | 0.384 | 0.384 | 91.0% | +7.4% | 63 | 5 | 0 | 27 | 0 |
| 9 |  | **ARM** | Arm Holdings plc | Technology | 0.866 | 0.349 | 0.349 | 89.7% | -27.8% | 27 | 10 | 2 | 18 | 0 |
| 10 | ★★ | **CRH** | CRH plc | Basic Materials | 0.860 | 0.346 | 0.346 | 88.5% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.792 | 0.318 | 0.318 | 87.2% | -1.6% | 29 | 6 | 0 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.765 | 0.308 | 0.308 | 85.9% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 13 |  | **APH** | Amphenol Corporation | Technology | 0.607 | 0.243 | 0.243 | 84.6% | +13.4% | 14 | 3 | 1 | 5 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.597 | 0.239 | 0.239 | 83.3% | -3.5% | 18 | 2 | 0 | 7 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.580 | 0.232 | 0.232 | 82.1% | +12.5% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.569 | 0.945 | 0.945 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.719 | 0.630 | 0.630 | 98.7% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.674 | 0.614 | 0.614 | 97.4% | +2.8% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.361 | 0.498 | 0.498 | 96.2% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.357 | 0.496 | 0.496 | 94.9% | +36.8% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **CRH** | CRH plc | Basic Materials | 1.337 | 0.489 | 0.489 | 93.6% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.128 | 0.412 | 0.412 | 92.3% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.065 | 0.388 | 0.388 | 91.0% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.986 | 0.359 | 0.359 | 89.7% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.959 | 0.349 | 0.349 | 88.5% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.947 | 0.345 | 0.345 | 87.2% | +14.2% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.925 | 0.336 | 0.336 | 85.9% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.880 | 0.320 | 0.320 | 84.6% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.872 | 0.317 | 0.317 | 83.3% | +18.2% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.830 | 0.301 | 0.301 | 82.1% | +22.7% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.890 | 0.806 | 0.806 | 100.0% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.642 | 0.699 | 0.699 | 98.7% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.498 | 0.637 | 0.637 | 97.4% | +40.3% | 32 | 1 | 0 | 19 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.417 | 0.602 | 0.602 | 96.2% | +49.8% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.364 | 0.579 | 0.579 | 94.9% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 6 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.291 | 0.547 | 0.547 | 93.6% | +50.6% | 28 | 7 | 0 | 23 | 0 |
| 7 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.275 | 0.541 | 0.541 | 92.3% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.258 | 0.533 | 0.533 | 91.0% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.232 | 0.522 | 0.522 | 89.7% | +36.8% | 44 | 3 | 1 | 20 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.157 | 0.490 | 0.490 | 88.5% | +22.7% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.150 | 0.487 | 0.487 | 87.2% | +30.2% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.079 | 0.456 | 0.456 | 85.9% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.985 | 0.416 | 0.416 | 84.6% | +20.5% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.984 | 0.415 | 0.415 | 83.3% | +25.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.965 | 0.407 | 0.407 | 82.1% | +40.5% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-25 22:36:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 22:36:39Z |  |
| stooq.prices | ok | 0 | 2026-04-25 21:48:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 21:48:38Z |  |
| stooq.prices | ok | 0 | 2026-04-25 20:59:39Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 20:59:34Z |  |
| stooq.prices | ok | 0 | 2026-04-25 20:08:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 20:08:02Z |  |
| stooq.prices | ok | 0 | 2026-04-25 19:31:42Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 19:31:34Z |  |
| stooq.prices | ok | 0 | 2026-04-25 18:26:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 18:25:59Z |  |
| stooq.prices | ok | 0 | 2026-04-25 17:36:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 17:36:53Z |  |
| stooq.prices | ok | 0 | 2026-04-25 16:54:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 16:54:54Z |  |
| stooq.prices | ok | 0 | 2026-04-25 15:59:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 15:58:57Z |  |
| stooq.prices | ok | 0 | 2026-04-25 15:04:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-25 15:04:10Z |  |
