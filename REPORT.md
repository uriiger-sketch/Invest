# Invest — Top 20 report

_Generated: **2026-04-20 20:07 UTC** · Scores as of: **2026-04-20**_

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
| 1 | **TXN** | Texas Instruments Incorporated | Technology | 2.975 | 1.173 | 1.173 | 100.0% | -3.7% | 15 | 18 | 4 | 15 | 0 |
| 2 | **AAPL** | Apple Inc. | Technology | 2.435 | 0.960 | 0.960 | 98.8% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 3 | **CVX** | Chevron Corporation | Energy | 1.486 | 0.587 | 0.587 | 97.5% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 4 | **SBUX** | Starbucks Corporation | Consumer Cyclical | 1.481 | 0.585 | 0.585 | 96.2% | +1.4% | 17 | 18 | 4 | 15 | 0 |
| 5 | **TSLA** | Tesla, Inc. | Consumer Cyclical | 1.243 | 0.491 | 0.491 | 95.0% | +5.6% | 23 | 18 | 7 | 15 | 0 |
| 6 | **XOM** | Exxon Mobil Corporation | Energy | 1.177 | 0.465 | 0.465 | 93.8% | +11.6% | 13 | 12 | 1 | 14 | 0 |
| 7 | **ADI** | Analog Devices, Inc. | Technology | 1.081 | 0.427 | 0.427 | 92.5% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 8 | **BAC** | Bank of America Corporation | Financial Services | 1.057 | 0.418 | 0.418 | 91.2% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 9 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.052 | 0.416 | 0.416 | 90.0% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 10 | **C** | Citigroup Inc. | Financial Services | 0.961 | 0.380 | 0.380 | 88.8% | +6.1% | 18 | 4 | 0 | 12 | 0 |
| 11 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 0.859 | 0.340 | 0.340 | 87.5% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 12 | **DIS** | The Walt Disney Company | Communication Servic | 0.843 | 0.333 | 0.333 | 86.2% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 13 | **AVGO** | Broadcom Inc. | Technology | 0.776 | 0.307 | 0.307 | 85.0% | +19.0% | 44 | 3 | 0 | 11 | 0 |
| 14 | **MS** | Morgan Stanley | Financial Services | 0.765 | 0.303 | 0.303 | 83.8% | +2.3% | 10 | 14 | 1 | 11 | 0 |
| 15 | **NVDA** | NVIDIA Corporation | Technology | 0.725 | 0.287 | 0.287 | 82.5% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 16 | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.573 | 0.227 | 0.227 | 81.2% | +6.0% | 35 | 13 | 0 | 16 | 0 |
| 17 | **V** | Visa Inc. | Financial Services | 0.563 | 0.223 | 0.223 | 80.0% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 18 | **GOOG** | Alphabet Inc. | Communication Servic | 0.543 | 0.216 | 0.216 | 78.8% | +8.1% | 61 | 7 | 0 | 5 | 0 |
| 19 | **GOOGL** | Alphabet Inc. | Communication Servic | 0.541 | 0.215 | 0.215 | 77.5% | +11.6% | 60 | 7 | 0 | 23 | 0 |
| 20 | **MA** | Mastercard Incorporated | Financial Services | 0.507 | 0.201 | 0.201 | 76.2% | +26.7% | 35 | 3 | 0 | 14 | 0 |


## Weeks horizon

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | Microsoft Corporation | Technology | 1.468 | 0.579 | 0.579 | 100.0% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 2 | **DIS** | The Walt Disney Company | Communication Servic | 1.418 | 0.560 | 0.560 | 98.8% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 3 | **CVX** | Chevron Corporation | Energy | 1.352 | 0.534 | 0.534 | 97.5% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 4 | **NVDA** | NVIDIA Corporation | Technology | 1.302 | 0.514 | 0.514 | 96.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 5 | **AAPL** | Apple Inc. | Technology | 1.203 | 0.475 | 0.475 | 95.0% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 6 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.169 | 0.462 | 0.462 | 93.8% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 7 | **MA** | Mastercard Incorporated | Financial Services | 1.115 | 0.440 | 0.440 | 92.5% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 8 | **V** | Visa Inc. | Financial Services | 1.114 | 0.440 | 0.440 | 91.2% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 9 | **DHR** | Danaher Corporation | Healthcare | 1.056 | 0.417 | 0.417 | 90.0% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 10 | **BAC** | Bank of America Corporation | Financial Services | 1.018 | 0.402 | 0.402 | 88.8% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 11 | **NOW** | ServiceNow, Inc. | Technology | 0.874 | 0.345 | 0.345 | 87.5% | +69.1% | 41 | 4 | 1 | 20 | 0 |
| 12 | **META** | Meta Platforms, Inc. | Communication Servic | 0.873 | 0.345 | 0.345 | 86.2% | +27.6% | 58 | 6 | 0 | 0 | 0 |
| 13 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.836 | 0.330 | 0.330 | 85.0% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 14 | **SYK** | Stryker Corporation | Healthcare | 0.788 | 0.311 | 0.311 | 83.8% | +23.9% | 22 | 7 | 0 | 8 | 0 |
| 15 | **INTU** | Intuit Inc. | Technology | 0.759 | 0.300 | 0.300 | 82.5% | +48.1% | 29 | 5 | 0 | 10 | 0 |
| 16 | **ORCL** | Oracle Corporation | Technology | 0.758 | 0.300 | 0.300 | 81.2% | +37.3% | 34 | 8 | 1 | 21 | 0 |
| 17 | **TXN** | Texas Instruments Incorporated | Technology | 0.747 | 0.295 | 0.295 | 80.0% | -3.7% | 15 | 18 | 4 | 15 | 0 |
| 18 | **CRM** | Salesforce, Inc. | Technology | 0.734 | 0.290 | 0.290 | 78.8% | +44.4% | 35 | 10 | 1 | 24 | 0 |
| 19 | **BLK** | BlackRock, Inc. | Financial Services | 0.700 | 0.277 | 0.277 | 77.5% | +19.4% | 14 | 3 | 0 | 9 | 0 |
| 20 | **NFLX** | Netflix, Inc. | Communication Servic | 0.652 | 0.258 | 0.258 | 76.2% | +20.7% | 38 | 12 | 1 | 23 | 0 |


## Months horizon

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NOW** | ServiceNow, Inc. | Technology | 2.199 | 1.102 | 1.102 | 100.0% | +69.1% | 41 | 4 | 1 | 20 | 0 |
| 2 | **INTU** | Intuit Inc. | Technology | 1.573 | 0.788 | 0.788 | 98.8% | +48.1% | 29 | 5 | 0 | 10 | 0 |
| 3 | **MSFT** | Microsoft Corporation | Technology | 1.562 | 0.783 | 0.783 | 97.5% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 4 | **DHR** | Danaher Corporation | Healthcare | 1.260 | 0.631 | 0.631 | 96.2% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 5 | **V** | Visa Inc. | Financial Services | 1.250 | 0.626 | 0.626 | 95.0% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 6 | **MA** | Mastercard Incorporated | Financial Services | 1.248 | 0.625 | 0.625 | 93.8% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 7 | **CRM** | Salesforce, Inc. | Technology | 1.194 | 0.598 | 0.598 | 92.5% | +44.4% | 35 | 10 | 1 | 24 | 0 |
| 8 | **NVDA** | NVIDIA Corporation | Technology | 1.186 | 0.595 | 0.595 | 91.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 9 | **ABT** | Abbott Laboratories | Healthcare | 1.152 | 0.577 | 0.577 | 90.0% | +25.0% | 22 | 6 | 0 | 13 | 0 |
| 10 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.089 | 0.546 | 0.546 | 88.8% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 11 | **SYK** | Stryker Corporation | Healthcare | 1.089 | 0.546 | 0.546 | 87.5% | +23.9% | 22 | 7 | 0 | 8 | 0 |
| 12 | **DIS** | The Walt Disney Company | Communication Servic | 1.015 | 0.509 | 0.509 | 86.2% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 13 | **SPGI** | S&P Global Inc. | Financial Services | 0.890 | 0.446 | 0.446 | 85.0% | +20.6% | 23 | 1 | 0 | 9 | 0 |
| 14 | **META** | Meta Platforms, Inc. | Communication Servic | 0.881 | 0.441 | 0.441 | 83.8% | +27.6% | 58 | 6 | 0 | 0 | 0 |
| 15 | **LLY** | Eli Lilly and Company | Healthcare | 0.866 | 0.434 | 0.434 | 82.5% | +31.3% | 24 | 6 | 1 | 11 | 0 |
| 16 | **ABBV** | AbbVie Inc. | Healthcare | 0.848 | 0.425 | 0.425 | 81.2% | +22.3% | 22 | 9 | 0 | 10 | 0 |
| 17 | **BAC** | Bank of America Corporation | Financial Services | 0.835 | 0.419 | 0.419 | 80.0% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 18 | **KO** | The Coca-Cola Company | Consumer Defensive | 0.798 | 0.400 | 0.400 | 78.8% | +10.8% | 19 | 5 | 0 | 9 | 0 |
| 19 | **PM** | Philip Morris International Inc. | Consumer Defensive | 0.785 | 0.394 | 0.394 | 77.5% | +22.2% | 12 | 5 | 0 | 6 | 0 |
| 20 | **CVX** | Chevron Corporation | Energy | 0.782 | 0.392 | 0.392 | 76.2% | +16.4% | 19 | 6 | 1 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| edgar.13f | error | 0 | 2026-04-20 20:07:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| yfinance.actions | ok | 1241 | 2026-04-20 20:07:16Z |  |
| yfinance.consensus | ok | 80 | 2026-04-20 20:06:58Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-20 20:06:31Z |  |
| yfinance.prices | ok | 7200 | 2026-04-20 20:06:21Z |  |
| yfinance.consensus_fast | ok | 80 | 2026-04-20 19:54:03Z |  |
| yfinance.prices_fast | ok | 7200 | 2026-04-20 19:53:56Z |  |
| edgar.13f | error | 0 | 2026-04-20 19:41:34Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| yfinance.actions | ok | 1241 | 2026-04-20 19:41:21Z |  |
| yfinance.consensus | ok | 80 | 2026-04-20 19:41:13Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-20 19:40:59Z |  |
| yfinance.prices | ok | 7200 | 2026-04-20 19:40:54Z |  |
