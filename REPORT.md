# Invest — Top 15 report

_Generated: **2026-04-22 19:42 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T19:42:15Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.854 | 1.632 | 1.632 | 100.0% | +9.1% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.269 | 1.383 | 1.383 | 98.7% | +13.3% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.296 | 0.970 | 0.970 | 97.4% | +23.4% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.987 | 0.839 | 0.839 | 96.2% | +10.1% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.660 | 0.701 | 0.701 | 94.9% | +3.2% | 8 | 7 | 3 | 5 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.166 | 0.491 | 0.491 | 93.6% | +5.1% | 41 | 12 | 0 | 27 | 0 |
| 7 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.064 | 0.448 | 0.448 | 92.3% | -3.5% | 36 | 13 | 0 | 16 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.032 | 0.434 | 0.434 | 91.0% | +17.7% | 23 | 8 | 0 | 12 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.939 | 0.395 | 0.395 | 89.7% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ARM** | Arm Holdings plc | Technology | 0.913 | 0.383 | 0.383 | 88.5% | -12.9% | 27 | 10 | 2 | 18 | 0 |
| 11 |  | **ANET** | Arista Networks, Inc. | Technology | 0.821 | 0.344 | 0.344 | 87.2% | +0.2% | 27 | 3 | 0 | 11 | 0 |
| 12 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.760 | 0.318 | 0.318 | 85.9% | +10.8% | 63 | 5 | 0 | 27 | 0 |
| 13 |  | **CLS** | Celestica Inc. | Technology | 0.732 | 0.307 | 0.307 | 84.6% | -1.7% | 18 | 2 | 0 | 6 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.663 | 0.278 | 0.278 | 83.3% | +3.2% | 29 | 6 | 0 | 16 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.536 | 0.224 | 0.224 | 82.1% | +18.0% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.336 | 0.921 | 0.921 | 100.0% | +9.1% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.328 | 0.918 | 0.918 | 98.7% | +13.3% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.949 | 0.767 | 0.767 | 97.4% | +23.4% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.735 | 0.683 | 0.683 | 96.2% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.484 | 0.583 | 0.583 | 94.9% | +49.3% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.449 | 0.569 | 0.569 | 93.6% | +51.5% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.112 | 0.436 | 0.436 | 92.3% | +35.4% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.042 | 0.408 | 0.408 | 91.0% | +56.9% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.020 | 0.399 | 0.399 | 89.7% | +38.7% | 22 | 2 | 0 | 6 | 0 |
| 10 |  | **DE** | Deere & Company | Industrials | 0.974 | 0.381 | 0.381 | 88.5% | +14.5% | 13 | 11 | 0 | 13 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.954 | 0.373 | 0.373 | 87.2% | +22.8% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.948 | 0.371 | 0.371 | 85.9% | +5.1% | 41 | 12 | 0 | 27 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.895 | 0.350 | 0.350 | 84.6% | +38.9% | 35 | 10 | 0 | 20 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.833 | 0.325 | 0.325 | 83.3% | +10.1% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.797 | 0.311 | 0.311 | 82.1% | +22.7% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.868 | 0.830 | 0.830 | 100.0% | +49.8% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.723 | 0.765 | 0.765 | 98.7% | +56.9% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.666 | 0.739 | 0.739 | 97.4% | +51.5% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.573 | 0.698 | 0.698 | 96.2% | +38.7% | 22 | 2 | 0 | 6 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.536 | 0.681 | 0.681 | 94.9% | +49.3% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.317 | 0.583 | 0.583 | 93.6% | +22.8% | 10 | 1 | 0 | 2 | 0 |
| 7 |  | **ABT** | Abbott Laboratories | Healthcare | 1.295 | 0.573 | 0.573 | 92.3% | +30.4% | 22 | 6 | 0 | 13 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.246 | 0.551 | 0.551 | 91.0% | +22.7% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.221 | 0.540 | 0.540 | 89.7% | +35.4% | 44 | 3 | 1 | 20 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.189 | 0.525 | 0.525 | 88.5% | +42.0% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.124 | 0.496 | 0.496 | 87.2% | +22.7% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.072 | 0.473 | 0.473 | 85.9% | +23.4% | 20 | 2 | 0 | 3 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.035 | 0.456 | 0.456 | 84.6% | +38.9% | 35 | 10 | 0 | 20 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.956 | 0.421 | 0.421 | 83.3% | +24.6% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.881 | 0.387 | 0.387 | 82.1% | +29.7% | 31 | 7 | 0 | 21 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 19:42:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 19:42:09Z |  |
| stooq.prices | ok | 0 | 2026-04-22 18:06:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 18:06:02Z |  |
| stooq.prices | ok | 0 | 2026-04-22 16:59:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 16:59:04Z |  |
| stooq.prices | ok | 0 | 2026-04-22 15:44:12Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-22 15:44:01Z |  |
| stooq.prices | ok | 0 | 2026-04-22 14:13:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 14:13:25Z |  |
| stooq.prices | ok | 0 | 2026-04-22 12:11:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 12:11:19Z |  |
| stooq.prices | ok | 0 | 2026-04-22 11:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 11:05:00Z |  |
| stooq.prices | ok | 0 | 2026-04-22 09:55:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 09:55:54Z |  |
| stooq.prices | ok | 0 | 2026-04-22 08:03:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 08:03:07Z |  |
| stooq.prices | ok | 0 | 2026-04-22 05:59:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 05:59:51Z |  |
