# Invest — Top 15 report

_Generated: **2026-04-21 16:10 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T16:10:34Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 4.065 | 1.655 | 1.655 | 100.0% | +11.7% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★★ | **CVX** | Chevron Corporation | Energy | 3.550 | 1.444 | 1.444 | 98.7% | +15.6% | 19 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.074 | 0.841 | 0.841 | 97.4% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 5 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.398 | 0.565 | 0.565 | 96.2% | +18.1% | 22 | 8 | 0 | 11 | 0 |
| 6 |  | **F** | Ford Motor Company | Consumer Cyclical | 1.371 | 0.554 | 0.554 | 94.9% | +8.0% | 6 | 15 | 1 | 7 | 0 |
| 7 |  | **CRDO** | Credo Technology | Technology | 1.135 | 0.457 | 0.457 | 93.6% | — | 0 | 0 | 0 | 0 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.018 | 0.410 | 0.410 | 92.3% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **BP** | BP p.l.c. | Energy | 0.957 | 0.385 | 0.385 | 91.0% | +4.5% | 8 | 8 | 3 | 5 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.860 | 0.345 | 0.345 | 89.7% | +11.1% | 62 | 5 | 0 | 27 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.776 | 0.311 | 0.311 | 88.5% | +2.9% | 35 | 13 | 0 | 16 | 0 |
| 12 | ★★ | **DE** | Deere & Company | Industrials | 0.689 | 0.275 | 0.275 | 87.2% | +12.3% | 13 | 11 | 0 | 13 | 0 |
| 13 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 0.678 | 0.271 | 0.271 | 85.9% | +44.3% | 21 | 5 | 0 | 12 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.671 | 0.268 | 0.268 | 84.6% | +3.7% | 29 | 6 | 0 | 16 | 0 |
| 15 |  | **C** | Citigroup Inc. | Financial Services | 0.662 | 0.264 | 0.264 | 83.3% | +6.2% | 18 | 4 | 0 | 12 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **CVX** | Chevron Corporation | Energy | 2.629 | 1.063 | 1.063 | 100.0% | +15.6% | 19 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.565 | 1.037 | 1.037 | 98.7% | +11.7% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.911 | 0.771 | 0.771 | 97.4% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.748 | 0.704 | 0.704 | 96.2% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.467 | 0.590 | 0.590 | 94.9% | +48.5% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.456 | 0.585 | 0.585 | 93.6% | +44.3% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.194 | 0.479 | 0.479 | 92.3% | +59.9% | 32 | 1 | 0 | 18 | 0 |
| 10 | ★★ | **DE** | Deere & Company | Industrials | 1.189 | 0.477 | 0.477 | 91.0% | +12.3% | 13 | 11 | 0 | 13 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.151 | 0.462 | 0.462 | 89.7% | +36.1% | 44 | 3 | 1 | 20 | 0 |
| 12 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.094 | 0.438 | 0.438 | 88.5% | +51.7% | 28 | 7 | 0 | 22 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.011 | 0.405 | 0.405 | 87.2% | +21.0% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.979 | 0.392 | 0.392 | 85.9% | +34.9% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.977 | 0.391 | 0.391 | 84.6% | +32.5% | 22 | 3 | 0 | 6 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.311 | 1.128 | 1.128 | 100.0% | +59.9% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.580 | 0.768 | 0.768 | 98.7% | +51.7% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.511 | 0.735 | 0.735 | 97.4% | +48.5% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.433 | 0.696 | 0.696 | 96.2% | +44.3% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.320 | 0.641 | 0.641 | 94.9% | +32.5% | 22 | 3 | 0 | 6 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.316 | 0.639 | 0.639 | 93.6% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **CRM** | Salesforce, Inc. | Technology | 1.251 | 0.606 | 0.606 | 92.3% | +41.5% | 35 | 10 | 1 | 24 | 0 |
| 9 |  | **ABT** | Abbott Laboratories | Healthcare | 1.245 | 0.603 | 0.603 | 91.0% | +28.0% | 22 | 6 | 0 | 13 | 0 |
| 10 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.237 | 0.600 | 0.600 | 89.7% | +21.0% | 10 | 1 | 0 | 2 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.228 | 0.595 | 0.595 | 88.5% | +36.1% | 44 | 3 | 1 | 20 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.086 | 0.525 | 0.525 | 87.2% | +21.0% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CVX** | Chevron Corporation | Energy | 1.037 | 0.501 | 0.501 | 85.9% | +15.6% | 19 | 6 | 1 | 9 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.010 | 0.488 | 0.488 | 84.6% | +21.2% | 21 | 2 | 0 | 3 | 0 |
| 15 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.949 | 0.458 | 0.458 | 83.3% | +34.9% | 35 | 10 | 0 | 20 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-21 01:09:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-21 01:09:18Z |  |
