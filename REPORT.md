# Invest — Top 20 report

_Generated: **2026-04-20 19:54 UTC** · Scores as of: **2026-04-20**_

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
| 1 | **TXN** | Texas Instruments Incorporated | Technology | 2.974 | 1.173 | 1.173 | 100.0% | -3.6% | 15 | 18 | 4 | 15 | 0 |
| 2 | **AAPL** | Apple Inc. | Technology | 2.429 | 0.958 | 0.958 | 98.8% | +9.1% | 31 | 14 | 2 | 14 | 0 |
| 3 | **SBUX** | Starbucks Corporation | Consumer Cyclical | 1.487 | 0.587 | 0.587 | 97.5% | +1.4% | 17 | 18 | 4 | 15 | 0 |
| 4 | **CVX** | Chevron Corporation | Energy | 1.484 | 0.586 | 0.586 | 96.2% | +16.5% | 19 | 6 | 1 | 9 | 0 |
| 5 | **TSLA** | Tesla, Inc. | Consumer Cyclical | 1.258 | 0.497 | 0.497 | 95.0% | +5.5% | 23 | 18 | 7 | 15 | 0 |
| 6 | **XOM** | Exxon Mobil Corporation | Energy | 1.179 | 0.466 | 0.466 | 93.8% | +11.7% | 13 | 12 | 1 | 14 | 0 |
| 7 | **ADI** | Analog Devices, Inc. | Technology | 1.086 | 0.429 | 0.429 | 92.5% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 8 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.052 | 0.416 | 0.416 | 91.2% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 9 | **BAC** | Bank of America Corporation | Financial Services | 1.047 | 0.414 | 0.414 | 90.0% | +15.8% | 22 | 3 | 0 | 10 | 0 |
| 10 | **C** | Citigroup Inc. | Financial Services | 0.961 | 0.380 | 0.380 | 88.8% | +6.2% | 18 | 4 | 0 | 12 | 0 |
| 11 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 0.879 | 0.348 | 0.348 | 87.5% | +22.8% | 25 | 2 | 0 | 4 | 0 |
| 12 | **DIS** | The Walt Disney Company | Communication Servic | 0.852 | 0.337 | 0.337 | 86.2% | +20.7% | 27 | 3 | 1 | 7 | 0 |
| 13 | **MS** | Morgan Stanley | Financial Services | 0.776 | 0.307 | 0.307 | 85.0% | +2.2% | 10 | 14 | 1 | 11 | 0 |
| 14 | **AVGO** | Broadcom Inc. | Technology | 0.765 | 0.303 | 0.303 | 83.8% | +19.2% | 44 | 3 | 0 | 11 | 0 |
| 15 | **NVDA** | NVIDIA Corporation | Technology | 0.723 | 0.287 | 0.287 | 82.5% | +33.0% | 56 | 2 | 1 | 19 | 0 |
| 16 | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.568 | 0.225 | 0.225 | 81.2% | +6.1% | 35 | 13 | 0 | 16 | 0 |
| 17 | **V** | Visa Inc. | Financial Services | 0.566 | 0.225 | 0.225 | 80.0% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 18 | **GOOG** | Alphabet Inc. | Communication Servic | 0.551 | 0.219 | 0.219 | 78.8% | +8.0% | 61 | 7 | 0 | 5 | 0 |
| 19 | **GOOGL** | Alphabet Inc. | Communication Servic | 0.548 | 0.217 | 0.217 | 77.5% | +11.5% | 60 | 7 | 0 | 23 | 0 |
| 20 | **MA** | Mastercard Incorporated | Financial Services | 0.506 | 0.201 | 0.201 | 76.2% | +26.8% | 35 | 3 | 0 | 14 | 0 |


## Weeks horizon

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | Microsoft Corporation | Technology | 1.468 | 0.579 | 0.579 | 100.0% | +38.9% | 53 | 3 | 0 | 18 | 0 |
| 2 | **DIS** | The Walt Disney Company | Communication Servic | 1.414 | 0.558 | 0.558 | 98.8% | +20.7% | 27 | 3 | 1 | 7 | 0 |
| 3 | **CVX** | Chevron Corporation | Energy | 1.354 | 0.534 | 0.534 | 97.5% | +16.5% | 19 | 6 | 1 | 9 | 0 |
| 4 | **NVDA** | NVIDIA Corporation | Technology | 1.299 | 0.513 | 0.513 | 96.2% | +33.0% | 56 | 2 | 1 | 19 | 0 |
| 5 | **AAPL** | Apple Inc. | Technology | 1.206 | 0.476 | 0.476 | 95.0% | +9.1% | 31 | 14 | 2 | 14 | 0 |
| 6 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.161 | 0.458 | 0.458 | 93.8% | +22.8% | 25 | 2 | 0 | 4 | 0 |
| 7 | **MA** | Mastercard Incorporated | Financial Services | 1.113 | 0.439 | 0.439 | 92.5% | +26.8% | 35 | 3 | 0 | 14 | 0 |
| 8 | **V** | Visa Inc. | Financial Services | 1.111 | 0.439 | 0.439 | 91.2% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 9 | **DHR** | Danaher Corporation | Healthcare | 1.055 | 0.416 | 0.416 | 90.0% | +31.1% | 22 | 3 | 0 | 6 | 0 |
| 10 | **BAC** | Bank of America Corporation | Financial Services | 1.021 | 0.403 | 0.403 | 88.8% | +15.8% | 22 | 3 | 0 | 10 | 0 |
| 11 | **NOW** | ServiceNow, Inc. | Technology | 0.876 | 0.346 | 0.346 | 87.5% | +69.5% | 41 | 4 | 1 | 20 | 0 |
| 12 | **META** | Meta Platforms, Inc. | Communication Servic | 0.869 | 0.343 | 0.343 | 86.2% | +27.5% | 58 | 6 | 0 | 0 | 0 |
| 13 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.836 | 0.330 | 0.330 | 85.0% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 14 | **SYK** | Stryker Corporation | Healthcare | 0.785 | 0.310 | 0.310 | 83.8% | +23.8% | 22 | 7 | 0 | 8 | 0 |
| 15 | **INTU** | Intuit Inc. | Technology | 0.773 | 0.305 | 0.305 | 82.5% | +48.8% | 29 | 5 | 0 | 10 | 0 |
| 16 | **ORCL** | Oracle Corporation | Technology | 0.759 | 0.300 | 0.300 | 81.2% | +37.7% | 34 | 8 | 1 | 21 | 0 |
| 17 | **TXN** | Texas Instruments Incorporated | Technology | 0.749 | 0.296 | 0.296 | 80.0% | -3.6% | 15 | 18 | 4 | 15 | 0 |
| 18 | **CRM** | Salesforce, Inc. | Technology | 0.734 | 0.290 | 0.290 | 78.8% | +44.6% | 35 | 10 | 1 | 24 | 0 |
| 19 | **BLK** | BlackRock, Inc. | Financial Services | 0.698 | 0.276 | 0.276 | 77.5% | +19.4% | 14 | 3 | 0 | 9 | 0 |
| 20 | **NFLX** | Netflix, Inc. | Communication Servic | 0.647 | 0.256 | 0.256 | 76.2% | +20.5% | 38 | 12 | 1 | 23 | 0 |


## Months horizon

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NOW** | ServiceNow, Inc. | Technology | 2.205 | 1.105 | 1.105 | 100.0% | +69.5% | 41 | 4 | 1 | 20 | 0 |
| 2 | **INTU** | Intuit Inc. | Technology | 1.599 | 0.801 | 0.801 | 98.8% | +48.8% | 29 | 5 | 0 | 10 | 0 |
| 3 | **MSFT** | Microsoft Corporation | Technology | 1.568 | 0.786 | 0.786 | 97.5% | +38.9% | 53 | 3 | 0 | 18 | 0 |
| 4 | **DHR** | Danaher Corporation | Healthcare | 1.258 | 0.631 | 0.631 | 96.2% | +31.1% | 22 | 3 | 0 | 6 | 0 |
| 5 | **MA** | Mastercard Incorporated | Financial Services | 1.246 | 0.624 | 0.624 | 95.0% | +26.8% | 35 | 3 | 0 | 14 | 0 |
| 6 | **V** | Visa Inc. | Financial Services | 1.244 | 0.623 | 0.623 | 93.8% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 7 | **CRM** | Salesforce, Inc. | Technology | 1.196 | 0.599 | 0.599 | 92.5% | +44.6% | 35 | 10 | 1 | 24 | 0 |
| 8 | **NVDA** | NVIDIA Corporation | Technology | 1.184 | 0.593 | 0.593 | 91.2% | +33.0% | 56 | 2 | 1 | 19 | 0 |
| 9 | **ABT** | Abbott Laboratories | Healthcare | 1.148 | 0.575 | 0.575 | 90.0% | +25.0% | 22 | 6 | 0 | 13 | 0 |
| 10 | **SYK** | Stryker Corporation | Healthcare | 1.081 | 0.542 | 0.542 | 88.8% | +23.8% | 22 | 7 | 0 | 8 | 0 |
| 11 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.067 | 0.534 | 0.534 | 87.5% | +22.8% | 25 | 2 | 0 | 4 | 0 |
| 12 | **DIS** | The Walt Disney Company | Communication Servic | 1.004 | 0.503 | 0.503 | 86.2% | +20.7% | 27 | 3 | 1 | 7 | 0 |
| 13 | **SPGI** | S&P Global Inc. | Financial Services | 0.890 | 0.446 | 0.446 | 85.0% | +20.8% | 23 | 1 | 0 | 9 | 0 |
| 14 | **META** | Meta Platforms, Inc. | Communication Servic | 0.873 | 0.438 | 0.438 | 83.8% | +27.5% | 58 | 6 | 0 | 0 | 0 |
| 15 | **LLY** | Eli Lilly and Company | Healthcare | 0.854 | 0.428 | 0.428 | 82.5% | +31.2% | 24 | 6 | 1 | 11 | 0 |
| 16 | **BAC** | Bank of America Corporation | Financial Services | 0.843 | 0.422 | 0.422 | 81.2% | +15.8% | 22 | 3 | 0 | 10 | 0 |
| 17 | **ABBV** | AbbVie Inc. | Healthcare | 0.832 | 0.417 | 0.417 | 80.0% | +22.0% | 22 | 9 | 0 | 10 | 0 |
| 18 | **KO** | The Coca-Cola Company | Consumer Defensive | 0.798 | 0.400 | 0.400 | 78.8% | +10.9% | 19 | 5 | 0 | 9 | 0 |
| 19 | **PM** | Philip Morris International Inc. | Consumer Defensive | 0.788 | 0.395 | 0.395 | 77.5% | +22.4% | 12 | 5 | 0 | 6 | 0 |
| 20 | **CVX** | Chevron Corporation | Energy | 0.784 | 0.393 | 0.393 | 76.2% | +16.5% | 19 | 6 | 1 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| yfinance.consensus_fast | ok | 80 | 2026-04-20 19:54:03Z |  |
| yfinance.prices_fast | ok | 7200 | 2026-04-20 19:53:56Z |  |
| edgar.13f | error | 0 | 2026-04-20 19:41:34Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| yfinance.actions | ok | 1241 | 2026-04-20 19:41:21Z |  |
| yfinance.consensus | ok | 80 | 2026-04-20 19:41:13Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-20 19:40:59Z |  |
| yfinance.prices | ok | 7200 | 2026-04-20 19:40:54Z |  |
