# Invest — Top 15 report

_Generated: **2026-04-28 11:24 UTC** · Scores as of: **2026-04-28**_

🟢 last successful crawl: 0 min ago (at 2026-04-28T11:24:46Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.902 | 1.617 | 1.617 | 100.0% | +8.2% | 42 | 11 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.624 | 1.086 | 1.086 | 98.7% | -11.6% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.575 | 1.066 | 1.066 | 97.4% | +4.7% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.921 | 0.794 | 0.794 | 96.2% | +16.0% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.346 | 0.555 | 0.555 | 94.9% | +4.2% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.206 | 0.497 | 0.497 | 93.6% | -5.2% | 18 | 2 | 0 | 7 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.090 | 0.449 | 0.449 | 92.3% | +21.4% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.951 | 0.391 | 0.391 | 91.0% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.914 | 0.376 | 0.376 | 89.7% | +8.7% | 62 | 5 | 0 | 26 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.907 | 0.373 | 0.373 | 88.5% | +22.5% | 19 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.728 | 0.299 | 0.299 | 87.2% | +14.2% | 14 | 3 | 1 | 5 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.723 | 0.296 | 0.296 | 85.9% | +0.1% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.656 | 0.269 | 0.269 | 84.6% | +11.2% | 31 | 14 | 2 | 12 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.605 | 0.247 | 0.247 | 83.3% | +13.7% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.603 | 0.247 | 0.247 | 82.1% | +19.9% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.661 | 0.997 | 0.997 | 100.0% | +8.2% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.668 | 0.623 | 0.623 | 98.7% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.473 | 0.549 | 0.549 | 97.4% | +61.8% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.408 | 0.525 | 0.525 | 96.2% | +22.5% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.334 | 0.497 | 0.497 | 94.9% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.101 | 0.409 | 0.409 | 93.6% | +44.2% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.037 | 0.385 | 0.385 | 92.3% | +38.5% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.016 | 0.377 | 0.377 | 91.0% | +4.7% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.984 | 0.365 | 0.365 | 89.7% | +4.2% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.983 | 0.365 | 0.365 | 88.5% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.975 | 0.362 | 0.362 | 87.2% | +16.0% | 16 | 1 | 0 | 7 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.943 | 0.349 | 0.349 | 85.9% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.888 | 0.329 | 0.329 | 84.6% | +14.9% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.857 | 0.317 | 0.317 | 83.3% | +11.2% | 31 | 14 | 2 | 12 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.815 | 0.301 | 0.301 | 82.1% | +14.2% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.134 | 0.914 | 0.914 | 100.0% | +61.8% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.632 | 0.696 | 0.696 | 98.7% | +43.3% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.506 | 0.642 | 0.642 | 97.4% | +38.5% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.373 | 0.585 | 0.585 | 96.2% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.350 | 0.575 | 0.575 | 94.9% | +46.8% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.261 | 0.536 | 0.536 | 93.6% | +25.3% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.225 | 0.521 | 0.521 | 92.3% | +19.9% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.190 | 0.505 | 0.505 | 91.0% | +44.2% | 36 | 10 | 0 | 21 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.187 | 0.504 | 0.504 | 89.7% | +48.4% | 28 | 7 | 0 | 23 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.166 | 0.495 | 0.495 | 88.5% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.067 | 0.452 | 0.452 | 87.2% | +27.8% | 21 | 7 | 0 | 12 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.050 | 0.445 | 0.445 | 85.9% | +41.6% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.048 | 0.444 | 0.444 | 84.6% | +19.7% | 22 | 2 | 0 | 8 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.038 | 0.440 | 0.440 | 83.3% | +26.3% | 23 | 9 | 0 | 10 | 0 |
| 15 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.005 | 0.425 | 0.425 | 82.1% | +22.5% | 19 | 2 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-28 11:24:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 11:24:40Z |  |
| stooq.prices | ok | 0 | 2026-04-28 09:21:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 09:21:05Z |  |
| stooq.prices | ok | 0 | 2026-04-28 06:47:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 06:47:39Z |  |
| stooq.prices | ok | 0 | 2026-04-28 04:09:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 04:09:39Z |  |
| edgar.13f | error | 0 | 2026-04-28 01:16:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-28 01:16:32Z |  |
| yfinance.actions | ok | 1053 | 2026-04-28 01:16:25Z |  |
| yfinance.consensus | ok | 79 | 2026-04-28 01:16:15Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-28 01:15:58Z |  |
| yfinance.prices | ok | 7110 | 2026-04-28 01:15:52Z |  |
| stooq.prices | ok | 0 | 2026-04-28 00:09:42Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 00:09:36Z |  |
| stooq.prices | ok | 0 | 2026-04-27 23:13:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 23:13:50Z |  |
| stooq.prices | ok | 0 | 2026-04-27 22:11:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 22:11:38Z |  |
