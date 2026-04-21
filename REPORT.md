# Invest — Top 15 report

_Generated: **2026-04-21 19:40 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T19:40:41Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BSX**, **BUD**, **CHWY**, **CRH**, **CVX**, **DASH**, **DDOG**, **DE**, **DHR**, **DIS**, **DKNG**, **FROG**, **GLBE**, **GM**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 4.067 | 1.666 | 1.666 | 100.0% | +11.3% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★★ | **CVX** | Chevron Corporation | Energy | 3.575 | 1.464 | 1.464 | 98.7% | +14.6% | 19 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.065 | 0.843 | 0.843 | 97.4% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 5 |  | **F** | Ford Motor Company | Consumer Cyclical | 1.369 | 0.557 | 0.557 | 96.2% | +8.1% | 6 | 15 | 1 | 7 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.288 | 0.523 | 0.523 | 94.9% | +20.0% | 22 | 8 | 0 | 11 | 0 |
| 7 |  | **CRDO** | Credo Technology | Technology | 1.210 | 0.491 | 0.491 | 93.6% | — | 0 | 0 | 0 | 0 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.018 | 0.412 | 0.412 | 92.3% | +22.8% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **BP** | BP p.l.c. | Energy | 0.985 | 0.399 | 0.399 | 91.0% | +4.0% | 8 | 8 | 3 | 5 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.823 | 0.332 | 0.332 | 89.7% | +12.2% | 62 | 5 | 0 | 27 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.799 | 0.322 | 0.322 | 88.5% | +2.2% | 35 | 13 | 0 | 16 | 0 |
| 12 | ★★ | **DE** | Deere & Company | Industrials | 0.681 | 0.274 | 0.274 | 87.2% | +12.9% | 13 | 11 | 0 | 13 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.676 | 0.272 | 0.272 | 85.9% | +3.7% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **C** | Citigroup Inc. | Financial Services | 0.647 | 0.260 | 0.260 | 84.6% | +6.6% | 18 | 4 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.639 | 0.256 | 0.256 | 83.3% | +16.5% | 22 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **CVX** | Chevron Corporation | Energy | 2.619 | 1.054 | 1.054 | 100.0% | +14.6% | 19 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.571 | 1.034 | 1.034 | 98.7% | +11.3% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.910 | 0.767 | 0.767 | 97.4% | +22.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.741 | 0.698 | 0.698 | 96.2% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.462 | 0.585 | 0.585 | 94.9% | +46.8% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.452 | 0.581 | 0.581 | 93.6% | +49.5% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | ★★ | **DE** | Deere & Company | Industrials | 1.200 | 0.479 | 0.479 | 92.3% | +12.9% | 13 | 11 | 0 | 13 | 0 |
| 10 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.193 | 0.476 | 0.476 | 91.0% | +61.7% | 32 | 1 | 0 | 18 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.156 | 0.461 | 0.461 | 89.7% | +37.5% | 44 | 3 | 1 | 20 | 0 |
| 12 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.099 | 0.438 | 0.438 | 88.5% | +53.6% | 28 | 7 | 0 | 22 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.012 | 0.403 | 0.403 | 87.2% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.983 | 0.391 | 0.391 | 85.9% | +36.9% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.942 | 0.375 | 0.375 | 84.6% | +31.5% | 22 | 3 | 0 | 6 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.314 | 1.127 | 1.127 | 100.0% | +61.7% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.599 | 0.776 | 0.776 | 98.7% | +53.6% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.500 | 0.727 | 0.727 | 97.4% | +49.5% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.482 | 0.718 | 0.718 | 96.2% | +46.8% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.303 | 0.630 | 0.630 | 94.9% | +22.8% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **ABT** | Abbott Laboratories | Healthcare | 1.259 | 0.609 | 0.609 | 93.6% | +29.3% | 22 | 6 | 0 | 13 | 0 |
| 8 |  | **CRM** | Salesforce, Inc. | Technology | 1.253 | 0.606 | 0.606 | 92.3% | +42.7% | 35 | 10 | 1 | 24 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.251 | 0.605 | 0.605 | 91.0% | +31.5% | 22 | 3 | 0 | 6 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.245 | 0.602 | 0.602 | 89.7% | +37.5% | 44 | 3 | 1 | 20 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.244 | 0.602 | 0.602 | 88.5% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.108 | 0.535 | 0.535 | 87.2% | +22.2% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.992 | 0.478 | 0.478 | 85.9% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.986 | 0.475 | 0.475 | 84.6% | +36.9% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★★ | **CVX** | Chevron Corporation | Energy | 0.981 | 0.472 | 0.472 | 83.3% | +14.6% | 19 | 6 | 1 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-21 19:40:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 19:40:30Z |  |
| stooq.prices | ok | 0 | 2026-04-21 18:16:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 18:16:29Z |  |
| stooq.prices | ok | 0 | 2026-04-21 17:19:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 17:19:09Z |  |
| stooq.prices | ok | 0 | 2026-04-21 16:10:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 16:10:28Z |  |
| stooq.prices | ok | 0 | 2026-04-21 14:47:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 14:47:11Z |  |
| stooq.prices | ok | 0 | 2026-04-21 12:45:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 12:45:23Z |  |
| stooq.prices | ok | 0 | 2026-04-21 11:35:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 11:34:57Z |  |
| stooq.prices | ok | 0 | 2026-04-21 10:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 10:05:00Z |  |
| stooq.prices | ok | 0 | 2026-04-21 09:43:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 09:43:14Z |  |
| stooq.prices | ok | 0 | 2026-04-21 08:21:32Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 08:21:27Z |  |
