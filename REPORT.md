# Invest — Top 15 report

_Generated: **2026-04-23 17:49 UTC** · Scores as of: **2026-04-23**_

🟢 last successful crawl: 0 min ago (at 2026-04-23T17:49:47Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BAC**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.887 | 1.616 | 1.616 | 100.0% | +9.5% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.291 | 1.368 | 1.368 | 98.7% | +12.8% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.130 | 0.883 | 0.883 | 97.4% | +16.2% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.875 | 0.776 | 0.776 | 96.2% | +11.9% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **ARM** | Arm Holdings plc | Technology | 1.358 | 0.561 | 0.561 | 94.9% | -15.9% | 27 | 10 | 2 | 18 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.057 | 0.435 | 0.435 | 93.6% | -2.9% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.017 | 0.419 | 0.419 | 92.3% | +3.9% | 27 | 3 | 0 | 11 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.985 | 0.405 | 0.405 | 91.0% | +4.0% | 20 | 21 | 2 | 14 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.955 | 0.393 | 0.393 | 89.7% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.899 | 0.369 | 0.369 | 88.5% | +11.4% | 63 | 5 | 0 | 27 | 0 |
| 11 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.872 | 0.358 | 0.358 | 87.2% | +27.3% | 23 | 8 | 0 | 12 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.795 | 0.326 | 0.326 | 85.9% | -1.6% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.711 | 0.291 | 0.291 | 84.6% | +23.8% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.521 | 0.212 | 0.212 | 83.3% | +13.3% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.497 | 0.202 | 0.202 | 82.1% | +19.7% | 21 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.302 | 0.870 | 0.870 | 100.0% | +9.5% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.256 | 0.853 | 0.853 | 98.7% | +12.8% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.677 | 0.632 | 0.632 | 97.4% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.552 | 0.585 | 0.585 | 96.2% | +61.0% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.542 | 0.581 | 0.581 | 94.9% | +11.9% | 41 | 12 | 0 | 27 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.437 | 0.541 | 0.541 | 93.6% | +60.9% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.261 | 0.474 | 0.474 | 92.3% | +42.4% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.257 | 0.472 | 0.472 | 91.0% | +23.8% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.016 | 0.381 | 0.381 | 89.7% | +16.2% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.994 | 0.373 | 0.373 | 88.5% | +44.7% | 22 | 2 | 0 | 9 | 0 |
| 11 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.989 | 0.371 | 0.371 | 87.2% | +62.1% | 28 | 7 | 0 | 22 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.921 | 0.345 | 0.345 | 85.9% | +44.9% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.900 | 0.337 | 0.337 | 84.6% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.853 | 0.319 | 0.319 | 83.3% | +57.2% | 35 | 10 | 1 | 24 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.815 | 0.304 | 0.304 | 82.1% | +13.5% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.779 | 0.756 | 0.756 | 100.0% | +60.9% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.753 | 0.745 | 0.745 | 98.7% | +61.0% | 20 | 1 | 0 | 9 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.652 | 0.702 | 0.702 | 97.4% | +62.1% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.630 | 0.692 | 0.692 | 96.2% | +44.7% | 22 | 2 | 0 | 9 | 0 |
| 5 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.537 | 0.652 | 0.652 | 94.9% | +46.3% | 32 | 1 | 0 | 19 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.446 | 0.614 | 0.614 | 93.6% | +57.2% | 35 | 10 | 1 | 24 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.297 | 0.549 | 0.549 | 92.3% | +42.4% | 44 | 3 | 1 | 19 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.220 | 0.516 | 0.516 | 91.0% | +31.6% | 22 | 6 | 0 | 13 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.212 | 0.513 | 0.513 | 89.7% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.200 | 0.508 | 0.508 | 88.5% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.059 | 0.447 | 0.447 | 87.2% | +22.5% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.047 | 0.442 | 0.442 | 85.9% | +44.9% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.032 | 0.435 | 0.435 | 84.6% | +23.8% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.944 | 0.398 | 0.398 | 83.3% | +43.2% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.877 | 0.369 | 0.369 | 82.1% | +19.7% | 21 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-23 17:49:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 17:49:40Z |  |
| stooq.prices | ok | 0 | 2026-04-23 14:05:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 14:05:06Z |  |
| stooq.prices | ok | 0 | 2026-04-23 11:59:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 11:59:16Z |  |
| stooq.prices | ok | 0 | 2026-04-23 10:51:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 10:50:57Z |  |
| stooq.prices | ok | 0 | 2026-04-23 09:07:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 09:07:09Z |  |
| stooq.prices | ok | 0 | 2026-04-23 07:12:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 07:11:59Z |  |
| stooq.prices | ok | 0 | 2026-04-23 05:17:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 05:17:45Z |  |
| stooq.prices | ok | 0 | 2026-04-23 02:33:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 02:33:09Z |  |
| edgar.13f | error | 0 | 2026-04-23 00:12:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-23 00:12:25Z |  |
| yfinance.actions | ok | 1040 | 2026-04-23 00:12:16Z |  |
| yfinance.consensus | ok | 79 | 2026-04-23 00:12:02Z |  |
