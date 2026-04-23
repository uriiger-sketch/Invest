# Invest — Top 15 report

_Generated: **2026-04-23 02:33 UTC** · Scores as of: **2026-04-23**_

🟢 last successful crawl: 0 min ago (at 2026-04-23T02:33:17Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.889 | 1.601 | 1.601 | 100.0% | +9.0% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.283 | 1.351 | 1.351 | 98.7% | +13.5% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.093 | 0.859 | 0.859 | 97.4% | +10.5% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.868 | 0.766 | 0.766 | 96.2% | +5.0% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.114 | 0.454 | 0.454 | 94.9% | -3.6% | 36 | 13 | 0 | 16 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.089 | 0.444 | 0.444 | 93.6% | +17.5% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.064 | 0.434 | 0.434 | 92.3% | -13.7% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.956 | 0.389 | 0.389 | 91.0% | +1.1% | 20 | 21 | 2 | 14 | 0 |
| 9 |  | **ANET** | Arista Networks, Inc. | Technology | 0.954 | 0.388 | 0.388 | 89.7% | -0.2% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.930 | 0.378 | 0.378 | 88.5% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.807 | 0.328 | 0.328 | 87.2% | +10.7% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.792 | 0.321 | 0.321 | 85.9% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 13 |  | **CLS** | Celestica Inc. | Technology | 0.756 | 0.306 | 0.306 | 84.6% | -1.5% | 18 | 2 | 0 | 6 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.711 | 0.288 | 0.288 | 83.3% | +3.0% | 29 | 6 | 0 | 16 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.579 | 0.233 | 0.233 | 82.1% | +17.9% | 21 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.248 | 0.877 | 0.877 | 100.0% | +13.5% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.246 | 0.876 | 0.876 | 98.7% | +9.0% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.655 | 0.644 | 0.644 | 97.4% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.541 | 0.599 | 0.599 | 96.2% | +47.7% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.484 | 0.577 | 0.577 | 94.9% | +50.9% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.350 | 0.524 | 0.524 | 93.6% | +5.0% | 41 | 12 | 0 | 27 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.334 | 0.518 | 0.518 | 92.3% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.182 | 0.458 | 0.458 | 91.0% | +35.0% | 44 | 3 | 1 | 19 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.084 | 0.420 | 0.420 | 89.7% | +56.7% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.061 | 0.411 | 0.411 | 88.5% | +39.1% | 22 | 2 | 0 | 9 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.936 | 0.361 | 0.361 | 87.2% | +21.5% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.913 | 0.353 | 0.353 | 85.9% | +38.0% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.891 | 0.344 | 0.344 | 84.6% | +14.7% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.873 | 0.337 | 0.337 | 83.3% | +10.5% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.829 | 0.319 | 0.319 | 82.1% | +23.1% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.801 | 0.799 | 0.799 | 100.0% | +47.6% | 32 | 1 | 0 | 19 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.748 | 0.775 | 0.775 | 98.7% | +56.7% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.675 | 0.742 | 0.742 | 97.4% | +50.9% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.610 | 0.713 | 0.713 | 96.2% | +39.1% | 22 | 2 | 0 | 9 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.514 | 0.670 | 0.670 | 94.9% | +47.7% | 20 | 1 | 0 | 9 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.309 | 0.579 | 0.579 | 93.6% | +30.3% | 22 | 6 | 0 | 13 | 0 |
| 7 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.287 | 0.569 | 0.569 | 92.3% | +21.5% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.239 | 0.547 | 0.547 | 91.0% | +35.0% | 44 | 3 | 1 | 19 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.215 | 0.536 | 0.536 | 89.7% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.200 | 0.529 | 0.529 | 88.5% | +41.7% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.155 | 0.509 | 0.509 | 87.2% | +23.1% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.082 | 0.477 | 0.477 | 85.9% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.021 | 0.449 | 0.449 | 84.6% | +38.0% | 35 | 10 | 0 | 20 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.964 | 0.424 | 0.424 | 83.3% | +24.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.884 | 0.388 | 0.388 | 82.1% | +29.3% | 31 | 7 | 0 | 22 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-23 02:33:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 02:33:09Z |  |
| edgar.13f | error | 0 | 2026-04-23 00:12:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-23 00:12:25Z |  |
| yfinance.actions | ok | 1040 | 2026-04-23 00:12:16Z |  |
| yfinance.consensus | ok | 79 | 2026-04-23 00:12:02Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-23 00:11:42Z |  |
| yfinance.prices | ok | 7110 | 2026-04-23 00:11:33Z |  |
| stooq.prices | ok | 0 | 2026-04-22 23:45:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 23:44:55Z |  |
| stooq.prices | ok | 0 | 2026-04-22 22:47:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 22:47:02Z |  |
| stooq.prices | ok | 0 | 2026-04-22 21:50:56Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 21:50:51Z |  |
| stooq.prices | ok | 0 | 2026-04-22 20:54:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 20:54:38Z |  |
| stooq.prices | ok | 0 | 2026-04-22 19:42:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 19:42:09Z |  |
| stooq.prices | ok | 0 | 2026-04-22 18:06:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 18:06:02Z |  |
