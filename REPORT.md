# Invest — Top 20 report

_Generated: **2026-04-21 08:21 UTC** · Scores as of: **2026-04-21**_

🟢 last successful crawl: 0 min ago (at 2026-04-21T08:21:33Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

## How to read this

| Column | What it means |
|---|---|
| **#** | Rank (1 = highest blended score in this horizon). |
| **Ticker** | Stock symbol as used on US exchanges. |
| **Name** | Company name from Yahoo Finance. |
| **Sector** | GICS sector classification. |
| **Blended** | Final score = 0.6 · z(composite) + 0.4 · z(ml). Z-scored across the universe for this horizon, so 0 is average. +1 ≈ 1 std-dev above the pack. Higher = more attractive. |
| **Composite** | Rule-based score from the weighted sum of nine transparent features (analyst consensus, price-target upside, rating momentum 7 d & 30 d, target revision 30 d, 13F institutional flow, insider net buy 90 d, 21-day price momentum, realised-volatility risk penalty). |
| **ML** | LightGBM regressor's predicted forward return for this horizon. Cold-start fallback = composite until ≥ 60 daily snapshots exist. |
| **Pctile** | Percentile of the blended score inside this horizon (100 % = top). |
| **Upside** | Analyst consensus price target / last close − 1. Positive = analysts think there is room above the current price. |
| **Buy / Hold / Sell** | Aggregated analyst rating counts (most recent consensus snapshot). Strong Buy + Buy are combined into 'Buy'; Strong Sell + Sell into 'Sell'. |
| **Firms** | Count of distinct analyst firms that have issued an action (upgrade / downgrade / reiterate) on this ticker in the last 90 days. |
| **Insts** | Count of tracked institutional 13F filers (Berkshire, BlackRock, Bridgewater, Renaissance, Citadel, Tiger, ARK …) currently holding the stock in their most recent 13F-HR. |

## Days horizon

_5-day holding. Weights analyst rating momentum and short-term price momentum most; less weight on long-run price-target upside._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | Apple Inc. | Technology | 3.946 | 1.731 | 1.731 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | **CVX** | Chevron Corporation | Energy | 3.109 | 1.363 | 1.363 | 98.7% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 3 | **CRH** | CRH plc | Basic Materials | 2.113 | 0.925 | 0.925 | 97.4% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 4 | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.882 | 0.823 | 0.823 | 96.2% | +17.1% | 22 | 8 | 0 | 11 | 0 |
| 5 | **GM** | General Motors Company | Consumer Cyclical | 1.757 | 0.768 | 0.768 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | **F** | Ford Motor Company | Consumer Cyclical | 1.285 | 0.560 | 0.560 | 93.6% | +7.9% | 6 | 15 | 1 | 7 | 0 |
| 7 | **DIS** | The Walt Disney Company | Communication Servic | 1.054 | 0.458 | 0.458 | 92.3% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 8 | **ADI** | Analog Devices, Inc. | Technology | 0.948 | 0.412 | 0.412 | 91.0% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 9 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.889 | 0.386 | 0.386 | 89.7% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 10 | **C** | Citigroup Inc. | Financial Services | 0.860 | 0.373 | 0.373 | 88.5% | +6.1% | 18 | 4 | 0 | 12 | 0 |
| 11 | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.852 | 0.369 | 0.369 | 87.2% | +6.0% | 35 | 13 | 0 | 16 | 0 |
| 12 | **BAC** | Bank of America Corporation | Financial Services | 0.827 | 0.358 | 0.358 | 85.9% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 13 | **CHWY** | Chewy, Inc. | Consumer Cyclical | 0.711 | 0.308 | 0.308 | 84.6% | +41.4% | 21 | 5 | 0 | 12 | 0 |
| 14 | **BP** | BP p.l.c. | Energy | 0.624 | 0.269 | 0.269 | 83.3% | +5.8% | 8 | 8 | 3 | 5 | 0 |
| 15 | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.619 | 0.267 | 0.267 | 82.1% | +32.5% | 35 | 10 | 0 | 20 | 0 |
| 16 | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.601 | 0.259 | 0.259 | 80.8% | +18.3% | 10 | 1 | 0 | 2 | 0 |
| 17 | **DE** | Deere & Company | Industrials | 0.578 | 0.249 | 0.249 | 79.5% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 18 | **GOOGL** | Alphabet Inc. | Communication Servic | 0.441 | 0.189 | 0.189 | 78.2% | +11.6% | 60 | 7 | 0 | 23 | 0 |
| 19 | **GOOG** | Alphabet Inc. | Communication Servic | 0.434 | 0.185 | 0.185 | 76.9% | +8.1% | 61 | 7 | 0 | 5 | 0 |
| 20 | **AVGO** | Broadcom Inc. | Technology | 0.372 | 0.159 | 0.159 | 75.6% | +19.0% | 44 | 3 | 0 | 11 | 0 |


## Weeks horizon

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CVX** | Chevron Corporation | Energy | 2.525 | 0.976 | 0.976 | 100.0% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 2 | **AAPL** | Apple Inc. | Technology | 2.501 | 0.966 | 0.966 | 98.7% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 3 | **DIS** | The Walt Disney Company | Communication Servic | 1.841 | 0.710 | 0.710 | 97.4% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | **CRH** | CRH plc | Basic Materials | 1.750 | 0.675 | 0.675 | 96.2% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 5 | **GM** | General Motors Company | Consumer Cyclical | 1.579 | 0.608 | 0.608 | 94.9% | +17.0% | 21 | 4 | 2 | 13 | 0 |
| 6 | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.334 | 0.513 | 0.513 | 93.6% | +41.4% | 21 | 5 | 0 | 12 | 0 |
| 7 | **FROG** | JFrog Ltd. | Technology | 1.328 | 0.511 | 0.511 | 92.3% | +51.8% | 20 | 1 | 0 | 9 | 0 |
| 8 | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 1.274 | 0.489 | 0.489 | 91.0% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 9 | **DE** | Deere & Company | Industrials | 1.014 | 0.388 | 0.388 | 89.7% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 10 | **BSX** | Boston Scientific Corporation | Healthcare | 0.974 | 0.373 | 0.373 | 88.5% | +58.5% | 32 | 1 | 0 | 18 | 0 |
| 11 | **DDOG** | Datadog, Inc. | Technology | 0.955 | 0.365 | 0.365 | 87.2% | +38.2% | 44 | 3 | 1 | 20 | 0 |
| 12 | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.906 | 0.346 | 0.346 | 85.9% | +18.3% | 10 | 1 | 0 | 2 | 0 |
| 13 | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.881 | 0.337 | 0.337 | 84.6% | +32.5% | 35 | 10 | 0 | 20 | 0 |
| 14 | **DHR** | Danaher Corporation | Healthcare | 0.856 | 0.327 | 0.327 | 83.3% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 15 | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.841 | 0.321 | 0.321 | 82.1% | +53.8% | 28 | 7 | 0 | 22 | 0 |
| 16 | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.820 | 0.313 | 0.313 | 80.8% | +17.1% | 22 | 8 | 0 | 11 | 0 |
| 17 | **BAC** | Bank of America Corporation | Financial Services | 0.803 | 0.306 | 0.306 | 79.5% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 18 | **CI** | The Cigna Group | Healthcare | 0.754 | 0.288 | 0.288 | 78.2% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 19 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.698 | 0.266 | 0.266 | 76.9% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 20 | **CRM** | Salesforce, Inc. | Technology | 0.692 | 0.263 | 0.263 | 75.6% | +44.3% | 35 | 10 | 1 | 24 | 0 |


## Months horizon

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BSX** | Boston Scientific Corporation | Healthcare | 2.439 | 1.036 | 1.036 | 100.0% | +58.5% | 32 | 1 | 0 | 18 | 0 |
| 2 | **GLBE** | Global-E Online Ltd. | Consumer Cyclical | 2.088 | 0.886 | 0.886 | 98.7% | +47.5% | 11 | 1 | 0 | 4 | 0 |
| 3 | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.702 | 0.721 | 0.721 | 97.4% | +53.8% | 28 | 7 | 0 | 22 | 0 |
| 4 | **FROG** | JFrog Ltd. | Technology | 1.595 | 0.675 | 0.675 | 96.2% | +51.8% | 20 | 1 | 0 | 9 | 0 |
| 5 | **CRM** | Salesforce, Inc. | Technology | 1.322 | 0.558 | 0.558 | 94.9% | +44.3% | 35 | 10 | 1 | 24 | 0 |
| 6 | **DDOG** | Datadog, Inc. | Technology | 1.269 | 0.535 | 0.535 | 93.6% | +38.2% | 44 | 3 | 1 | 20 | 0 |
| 7 | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.261 | 0.532 | 0.532 | 92.3% | +41.4% | 21 | 5 | 0 | 12 | 0 |
| 8 | **DHR** | Danaher Corporation | Healthcare | 1.235 | 0.521 | 0.521 | 91.0% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 9 | **DIS** | The Walt Disney Company | Communication Servic | 1.188 | 0.501 | 0.501 | 89.7% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 10 | **ABT** | Abbott Laboratories | Healthcare | 1.144 | 0.482 | 0.482 | 88.5% | +25.0% | 22 | 6 | 0 | 13 | 0 |
| 11 | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.131 | 0.477 | 0.477 | 87.2% | +18.3% | 10 | 1 | 0 | 2 | 0 |
| 12 | **CI** | The Cigna Group | Healthcare | 1.038 | 0.437 | 0.437 | 85.9% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 13 | **CVX** | Chevron Corporation | Energy | 1.020 | 0.429 | 0.429 | 84.6% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 14 | **CHKP** | Check Point Software Technologies Ltd. | Technology | 0.864 | 0.362 | 0.362 | 83.3% | +43.1% | 17 | 20 | 0 | 12 | 0 |
| 15 | **CRH** | CRH plc | Basic Materials | 0.860 | 0.361 | 0.361 | 82.1% | +20.3% | 21 | 2 | 0 | 3 | 0 |
| 16 | **ABBV** | AbbVie Inc. | Healthcare | 0.855 | 0.358 | 0.358 | 80.8% | +22.2% | 22 | 9 | 0 | 10 | 0 |
| 17 | **BAC** | Bank of America Corporation | Financial Services | 0.742 | 0.310 | 0.310 | 79.5% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 18 | **BLK** | BlackRock, Inc. | Financial Services | 0.726 | 0.303 | 0.303 | 78.2% | +19.4% | 14 | 3 | 0 | 9 | 0 |
| 19 | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.683 | 0.285 | 0.285 | 76.9% | +32.5% | 35 | 10 | 0 | 20 | 0 |
| 20 | **GM** | General Motors Company | Consumer Cyclical | 0.593 | 0.246 | 0.246 | 75.6% | +17.0% | 21 | 4 | 2 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-20 21:30:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 21:30:26Z |  |
