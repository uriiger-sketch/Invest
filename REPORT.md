# Invest — Top 15 report

_Generated: **2026-04-21 09:43 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T09:43:25Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 4.085 | 1.727 | 1.727 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★★ | **CVX** | Chevron Corporation | Energy | 3.438 | 1.452 | 1.452 | 98.7% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.110 | 0.889 | 0.889 | 97.4% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 5 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.520 | 0.639 | 0.639 | 96.2% | +17.1% | 22 | 8 | 0 | 11 | 0 |
| 6 |  | **F** | Ford Motor Company | Consumer Cyclical | 1.367 | 0.574 | 0.574 | 94.9% | +7.9% | 6 | 15 | 1 | 7 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.122 | 0.470 | 0.470 | 93.6% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **CRDO** | Credo Technology | Technology | 0.885 | 0.369 | 0.369 | 92.3% | — | 0 | 0 | 0 | 0 | 0 |
| 9 |  | **BP** | BP p.l.c. | Energy | 0.835 | 0.348 | 0.348 | 91.0% | +5.8% | 8 | 8 | 3 | 5 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.812 | 0.338 | 0.338 | 89.7% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.791 | 0.329 | 0.329 | 88.5% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 12 |  | **BAC** | Bank of America Corporation | Financial Services | 0.759 | 0.316 | 0.316 | 87.2% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 13 |  | **C** | Citigroup Inc. | Financial Services | 0.747 | 0.311 | 0.311 | 85.9% | +6.1% | 18 | 4 | 0 | 12 | 0 |
| 14 | ★★ | **DE** | Deere & Company | Industrials | 0.690 | 0.286 | 0.286 | 84.6% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 15 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.668 | 0.277 | 0.277 | 83.3% | +6.0% | 35 | 13 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **CVX** | Chevron Corporation | Energy | 2.630 | 1.071 | 1.071 | 100.0% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.532 | 1.031 | 1.031 | 98.7% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.896 | 0.770 | 0.770 | 97.4% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.748 | 0.710 | 0.710 | 96.2% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.488 | 0.603 | 0.603 | 94.9% | +51.8% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.356 | 0.549 | 0.549 | 93.6% | +41.4% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | ★★ | **DE** | Deere & Company | Industrials | 1.169 | 0.472 | 0.472 | 92.3% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 10 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.139 | 0.460 | 0.460 | 91.0% | +58.5% | 32 | 1 | 0 | 18 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.133 | 0.457 | 0.457 | 89.7% | +38.2% | 44 | 3 | 1 | 20 | 0 |
| 12 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.046 | 0.422 | 0.422 | 88.5% | +53.8% | 28 | 7 | 0 | 22 | 0 |
| 13 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.950 | 0.383 | 0.383 | 87.2% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 14 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.944 | 0.380 | 0.380 | 85.9% | +18.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.939 | 0.378 | 0.378 | 84.6% | +32.5% | 35 | 10 | 0 | 20 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.261 | 1.095 | 1.095 | 100.0% | +58.5% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.680 | 0.811 | 0.811 | 98.7% | +53.8% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.638 | 0.791 | 0.791 | 97.4% | +51.8% | 20 | 1 | 0 | 9 | 0 |
| 5 |  | **CRM** | Salesforce, Inc. | Technology | 1.348 | 0.649 | 0.649 | 96.2% | +44.3% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.331 | 0.641 | 0.641 | 94.9% | +41.4% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.324 | 0.637 | 0.637 | 93.6% | +38.2% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.248 | 0.600 | 0.600 | 92.3% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.228 | 0.590 | 0.590 | 91.0% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 10 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.140 | 0.547 | 0.547 | 89.7% | +18.3% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.140 | 0.547 | 0.547 | 88.5% | +25.0% | 22 | 6 | 0 | 13 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.070 | 0.513 | 0.513 | 87.2% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CVX** | Chevron Corporation | Energy | 1.058 | 0.507 | 0.507 | 85.9% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.958 | 0.458 | 0.458 | 84.6% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 15 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 0.954 | 0.457 | 0.457 | 83.3% | +43.1% | 17 | 20 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.actions | ok | 1020 | 2026-04-21 00:08:55Z |  |
| yfinance.consensus | ok | 79 | 2026-04-21 00:08:46Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-21 00:08:33Z |  |
| yfinance.prices | ok | 7110 | 2026-04-21 00:08:28Z |  |
| stooq.prices | ok | 0 | 2026-04-20 23:26:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 23:26:21Z |  |
| stooq.prices | ok | 0 | 2026-04-20 22:27:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 22:27:29Z |  |
