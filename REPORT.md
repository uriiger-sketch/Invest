# Invest — Top 15 report

_Generated: **2026-04-21 14:47 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T14:47:17Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BSX**, **BUD**, **CHWY**, **CRH**, **CVX**, **DDOG**, **DE**, **DHR**, **DIS**, **DKNG**, **FROG**, **GLBE**, **GM**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 4.100 | 1.668 | 1.668 | 100.0% | +10.4% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★★ | **CVX** | Chevron Corporation | Energy | 3.517 | 1.430 | 1.430 | 98.7% | +16.2% | 19 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.110 | 0.856 | 0.856 | 97.4% | +19.8% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 5 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.473 | 0.595 | 0.595 | 96.2% | +16.6% | 22 | 8 | 0 | 11 | 0 |
| 6 |  | **F** | Ford Motor Company | Consumer Cyclical | 1.388 | 0.561 | 0.561 | 94.9% | +7.0% | 6 | 15 | 1 | 7 | 0 |
| 7 |  | **CRDO** | Credo Technology | Technology | 1.086 | 0.438 | 0.438 | 93.6% | — | 0 | 0 | 0 | 0 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.026 | 0.413 | 0.413 | 92.3% | +21.8% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **BP** | BP p.l.c. | Energy | 0.938 | 0.377 | 0.377 | 91.0% | +4.4% | 8 | 8 | 3 | 5 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.842 | 0.338 | 0.338 | 89.7% | +11.3% | 62 | 5 | 0 | 27 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.708 | 0.283 | 0.283 | 88.5% | +4.3% | 35 | 13 | 0 | 16 | 0 |
| 12 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 0.695 | 0.278 | 0.278 | 87.2% | +43.5% | 21 | 5 | 0 | 12 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.686 | 0.274 | 0.274 | 85.9% | +3.1% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **C** | Citigroup Inc. | Financial Services | 0.685 | 0.274 | 0.274 | 84.6% | +5.3% | 18 | 4 | 0 | 12 | 0 |
| 15 | ★★ | **DE** | Deere & Company | Industrials | 0.682 | 0.272 | 0.272 | 83.3% | +12.0% | 13 | 11 | 0 | 13 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **CVX** | Chevron Corporation | Energy | 2.647 | 1.069 | 1.069 | 100.0% | +16.2% | 19 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.555 | 1.032 | 1.032 | 98.7% | +10.4% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.913 | 0.771 | 0.771 | 97.4% | +21.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.740 | 0.700 | 0.700 | 96.2% | +19.8% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.476 | 0.593 | 0.593 | 94.9% | +43.5% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.473 | 0.592 | 0.592 | 93.6% | +47.1% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | ★★ | **DE** | Deere & Company | Industrials | 1.189 | 0.477 | 0.477 | 92.3% | +12.0% | 13 | 11 | 0 | 13 | 0 |
| 10 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.175 | 0.471 | 0.471 | 91.0% | +57.4% | 32 | 1 | 0 | 18 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.167 | 0.467 | 0.467 | 89.7% | +35.6% | 44 | 3 | 1 | 20 | 0 |
| 12 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.103 | 0.441 | 0.441 | 88.5% | +50.5% | 28 | 7 | 0 | 22 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.016 | 0.406 | 0.406 | 87.2% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.968 | 0.386 | 0.386 | 85.9% | +32.7% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.928 | 0.370 | 0.370 | 84.6% | +29.0% | 22 | 3 | 0 | 6 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.280 | 1.109 | 1.109 | 100.0% | +57.4% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.589 | 0.770 | 0.770 | 98.7% | +50.5% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.505 | 0.729 | 0.729 | 97.4% | +47.1% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.450 | 0.702 | 0.702 | 96.2% | +43.5% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.316 | 0.636 | 0.636 | 94.9% | +21.8% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.251 | 0.604 | 0.604 | 93.6% | +35.6% | 44 | 3 | 1 | 20 | 0 |
| 8 |  | **CRM** | Salesforce, Inc. | Technology | 1.247 | 0.602 | 0.602 | 92.3% | +40.3% | 35 | 10 | 1 | 24 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.246 | 0.602 | 0.602 | 91.0% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.239 | 0.598 | 0.598 | 89.7% | +26.9% | 22 | 6 | 0 | 13 | 0 |
| 11 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.218 | 0.588 | 0.588 | 88.5% | +29.0% | 22 | 3 | 0 | 6 | 0 |
| 12 | ★★★ | **CVX** | Chevron Corporation | Energy | 1.082 | 0.521 | 0.521 | 87.2% | +16.2% | 19 | 6 | 1 | 9 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.059 | 0.510 | 0.510 | 85.9% | +19.7% | 22 | 2 | 0 | 8 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.980 | 0.471 | 0.471 | 84.6% | +19.8% | 21 | 2 | 0 | 3 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.945 | 0.454 | 0.454 | 83.3% | +22.0% | 22 | 9 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| edgar.13f | error | 0 | 2026-04-21 00:09:09Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-21 00:09:08Z |  |
