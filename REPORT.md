# Invest — Top 15 report

_Generated: **2026-04-21 17:19 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T17:19:15Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 4.049 | 1.664 | 1.664 | 100.0% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★★ | **CVX** | Chevron Corporation | Energy | 3.542 | 1.455 | 1.455 | 98.7% | +15.1% | 19 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.058 | 0.842 | 0.842 | 97.4% | +22.0% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 5 |  | **F** | Ford Motor Company | Consumer Cyclical | 1.373 | 0.560 | 0.560 | 96.2% | +8.4% | 6 | 15 | 1 | 7 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.315 | 0.536 | 0.536 | 94.9% | +20.9% | 22 | 8 | 0 | 11 | 0 |
| 7 |  | **CRDO** | Credo Technology | Technology | 1.146 | 0.466 | 0.466 | 93.6% | — | 0 | 0 | 0 | 0 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.014 | 0.412 | 0.412 | 92.3% | +23.2% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **BP** | BP p.l.c. | Energy | 0.988 | 0.401 | 0.401 | 91.0% | +4.0% | 8 | 8 | 3 | 5 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.861 | 0.349 | 0.349 | 89.7% | +12.0% | 62 | 5 | 0 | 27 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.800 | 0.323 | 0.323 | 88.5% | +3.4% | 35 | 13 | 0 | 16 | 0 |
| 12 | ★★ | **DE** | Deere & Company | Industrials | 0.691 | 0.278 | 0.278 | 87.2% | +12.8% | 13 | 11 | 0 | 13 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.684 | 0.275 | 0.275 | 85.9% | +4.2% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **C** | Citigroup Inc. | Financial Services | 0.669 | 0.269 | 0.269 | 84.6% | +6.8% | 18 | 4 | 0 | 12 | 0 |
| 15 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 0.662 | 0.266 | 0.266 | 83.3% | +45.6% | 21 | 5 | 0 | 12 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **CVX** | Chevron Corporation | Energy | 2.607 | 1.053 | 1.053 | 100.0% | +15.1% | 19 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.563 | 1.035 | 1.035 | 98.7% | +11.8% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.903 | 0.767 | 0.767 | 97.4% | +23.2% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.748 | 0.704 | 0.704 | 96.2% | +22.0% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.448 | 0.582 | 0.582 | 94.9% | +49.7% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.443 | 0.580 | 0.580 | 93.6% | +45.6% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | ★★ | **DE** | Deere & Company | Industrials | 1.190 | 0.477 | 0.477 | 92.3% | +12.8% | 13 | 11 | 0 | 13 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.171 | 0.469 | 0.469 | 91.0% | +38.8% | 44 | 3 | 1 | 20 | 0 |
| 11 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.152 | 0.462 | 0.462 | 89.7% | +60.7% | 32 | 1 | 0 | 18 | 0 |
| 12 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.096 | 0.439 | 0.439 | 88.5% | +54.1% | 28 | 7 | 0 | 22 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.006 | 0.402 | 0.402 | 87.2% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.983 | 0.393 | 0.393 | 85.9% | +36.9% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.967 | 0.387 | 0.387 | 84.6% | +33.6% | 22 | 3 | 0 | 6 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.272 | 1.108 | 1.108 | 100.0% | +60.7% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.608 | 0.781 | 0.781 | 98.7% | +54.1% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.494 | 0.725 | 0.725 | 97.4% | +49.7% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.424 | 0.691 | 0.691 | 96.2% | +45.6% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.316 | 0.638 | 0.638 | 94.9% | +33.6% | 22 | 3 | 0 | 6 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.303 | 0.631 | 0.631 | 93.6% | +23.2% | 27 | 3 | 1 | 7 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.284 | 0.622 | 0.622 | 92.3% | +38.8% | 44 | 3 | 1 | 20 | 0 |
| 9 |  | **CRM** | Salesforce, Inc. | Technology | 1.258 | 0.609 | 0.609 | 91.0% | +43.1% | 35 | 10 | 1 | 24 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.238 | 0.600 | 0.600 | 89.7% | +28.9% | 22 | 6 | 0 | 13 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.233 | 0.597 | 0.597 | 88.5% | +21.8% | 10 | 1 | 0 | 2 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.067 | 0.516 | 0.516 | 87.2% | +21.4% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.008 | 0.486 | 0.486 | 85.9% | +22.0% | 21 | 2 | 0 | 3 | 0 |
| 14 | ★★★ | **CVX** | Chevron Corporation | Energy | 0.994 | 0.479 | 0.479 | 84.6% | +15.1% | 19 | 6 | 1 | 9 | 0 |
| 15 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.973 | 0.469 | 0.469 | 83.3% | +36.9% | 35 | 10 | 0 | 20 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-21 06:23:39Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 06:23:31Z |  |
| stooq.prices | ok | 0 | 2026-04-21 04:23:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 04:22:55Z |  |
