# Invest — Top 15 report

_Generated: **2026-04-27 15:48 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T15:48:13Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.788 | 1.594 | 1.594 | 100.0% | +8.0% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.958 | 1.244 | 1.244 | 98.7% | -11.4% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.664 | 1.120 | 1.120 | 97.4% | +3.3% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.899 | 0.797 | 0.797 | 96.2% | +17.0% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.302 | 0.546 | 0.546 | 94.9% | +5.1% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.104 | 0.463 | 0.463 | 93.6% | -2.7% | 18 | 2 | 0 | 7 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.074 | 0.450 | 0.450 | 92.3% | +22.2% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.969 | 0.406 | 0.406 | 91.0% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.907 | 0.379 | 0.379 | 89.7% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.906 | 0.379 | 0.379 | 88.5% | +8.6% | 63 | 5 | 0 | 26 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.702 | 0.293 | 0.293 | 87.2% | +14.8% | 14 | 3 | 1 | 5 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.690 | 0.288 | 0.288 | 85.9% | +0.8% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.644 | 0.269 | 0.269 | 84.6% | +11.5% | 31 | 14 | 2 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.585 | 0.244 | 0.244 | 83.3% | +19.7% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.580 | 0.242 | 0.242 | 82.1% | +14.0% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.546 | 0.955 | 0.955 | 100.0% | +8.0% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.674 | 0.626 | 0.626 | 98.7% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.466 | 0.548 | 0.548 | 97.4% | +61.5% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.401 | 0.523 | 0.523 | 96.2% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.379 | 0.515 | 0.515 | 94.9% | +35.6% | 45 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.064 | 0.396 | 0.396 | 93.6% | +41.7% | 35 | 10 | 0 | 20 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.034 | 0.384 | 0.384 | 92.3% | +38.6% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.014 | 0.377 | 0.377 | 91.0% | +3.3% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.005 | 0.374 | 0.374 | 89.7% | +17.0% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.988 | 0.367 | 0.367 | 88.5% | +5.1% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.975 | 0.362 | 0.362 | 87.2% | +19.7% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.918 | 0.341 | 0.341 | 85.9% | +48.2% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.891 | 0.331 | 0.331 | 84.6% | +14.5% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.882 | 0.327 | 0.327 | 83.3% | +11.5% | 31 | 14 | 2 | 12 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.827 | 0.307 | 0.307 | 82.1% | +14.8% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.149 | 0.917 | 0.917 | 100.0% | +61.5% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.558 | 0.662 | 0.662 | 98.7% | +40.8% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.527 | 0.649 | 0.649 | 97.4% | +38.6% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.351 | 0.573 | 0.573 | 96.2% | +48.2% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.326 | 0.562 | 0.562 | 94.9% | +51.3% | 28 | 7 | 0 | 23 | 0 |
| 6 |  | **FROG** | JFrog Ltd. | Technology | 1.316 | 0.558 | 0.558 | 93.6% | +45.5% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.265 | 0.536 | 0.536 | 92.3% | +35.6% | 45 | 3 | 1 | 20 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.234 | 0.522 | 0.522 | 91.0% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.226 | 0.519 | 0.519 | 89.7% | +19.7% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.104 | 0.467 | 0.467 | 88.5% | +41.7% | 35 | 10 | 0 | 20 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.073 | 0.453 | 0.453 | 87.2% | +27.7% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.033 | 0.436 | 0.436 | 85.9% | +19.2% | 22 | 2 | 0 | 8 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.993 | 0.419 | 0.419 | 84.6% | +24.8% | 23 | 9 | 0 | 11 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.988 | 0.416 | 0.416 | 83.3% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.980 | 0.413 | 0.413 | 82.1% | +39.3% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-04-27 00:07:39Z |  |
| yfinance.prices | ok | 7110 | 2026-04-27 00:07:30Z |  |
