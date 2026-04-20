# Invest — Top 20 report

_Generated: **2026-04-20 20:26 UTC** · Scores as of: **2026-04-20**_

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
| 1 | **AAPL** | Apple Inc. | Technology | 4.877 | 1.831 | 1.831 | 100.0% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 2 | **CVX** | Chevron Corporation | Energy | 3.933 | 1.476 | 1.476 | 99.1% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 3 | **TXN** | Texas Instruments Incorporated | Technology | 2.975 | 1.173 | 1.173 | 100.0% | -3.7% | 15 | 18 | 4 | 15 | 0 |
| 4 | **AFRM** | Affirm Holdings | Financials | 2.317 | 0.867 | 0.867 | 98.3% | +17.1% | 22 | 8 | 0 | 0 | 0 |
| 5 | **DIS** | The Walt Disney Company | Communication Servic | 1.578 | 0.589 | 0.589 | 97.4% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 6 | **SBUX** | Starbucks Corporation | Consumer Cyclical | 1.481 | 0.585 | 0.585 | 96.2% | +1.4% | 17 | 18 | 4 | 15 | 0 |
| 7 | **ADI** | Analog Devices, Inc. | Technology | 1.259 | 0.469 | 0.469 | 96.6% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 8 | **TSLA** | Tesla, Inc. | Consumer Cyclical | 1.243 | 0.491 | 0.491 | 95.0% | +5.6% | 23 | 18 | 7 | 15 | 0 |
| 9 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.182 | 0.440 | 0.440 | 95.7% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 10 | **XOM** | Exxon Mobil Corporation | Energy | 1.177 | 0.465 | 0.465 | 93.8% | +11.6% | 13 | 12 | 1 | 14 | 0 |
| 11 | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.174 | 0.437 | 0.437 | 94.9% | +6.0% | 35 | 13 | 0 | 16 | 0 |
| 12 | **C** | Citigroup Inc. | Financial Services | 1.161 | 0.432 | 0.432 | 94.0% | +6.1% | 18 | 4 | 0 | 12 | 0 |
| 13 | **CRH** | CRH plc | Materials | 1.106 | 0.411 | 0.411 | 93.2% | +20.3% | 21 | 2 | 0 | 0 | 0 |
| 14 | **BAC** | Bank of America Corporation | Financial Services | 1.103 | 0.410 | 0.410 | 92.3% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 15 | **DE** | Deere & Company | Industrials | 1.055 | 0.392 | 0.392 | 91.5% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 16 | **CHWY** | Chewy Inc. | Consumer Discretiona | 0.971 | 0.361 | 0.361 | 90.6% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 17 | **DASH** | DoorDash Inc. | Consumer Discretiona | 0.872 | 0.323 | 0.323 | 89.7% | +32.5% | 35 | 10 | 0 | 0 | 0 |
| 18 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 0.859 | 0.340 | 0.340 | 87.5% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 19 | **BUD** | Anheuser-Busch InBev | Consumer Staples | 0.847 | 0.314 | 0.314 | 88.9% | +18.3% | 10 | 1 | 0 | 0 | 0 |
| 20 | **MS** | Morgan Stanley | Financial Services | 0.765 | 0.303 | 0.303 | 83.8% | +2.3% | 10 | 14 | 1 | 11 | 0 |


## Weeks horizon

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | Apple Inc. | Technology | 2.985 | 1.135 | 1.135 | 100.0% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 2 | **CVX** | Chevron Corporation | Energy | 2.982 | 1.134 | 1.134 | 99.1% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 3 | **DIS** | The Walt Disney Company | Communication Servic | 2.279 | 0.866 | 0.866 | 98.3% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | **MBLY** | Mobileye Global | Technology | 1.580 | 0.600 | 0.600 | 97.4% | +77.4% | 16 | 13 | 0 | 0 | 0 |
| 5 | **DE** | Deere & Company | Industrials | 1.502 | 0.570 | 0.570 | 96.6% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 6 | **MSFT** | Microsoft Corporation | Technology | 1.468 | 0.579 | 0.579 | 100.0% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 7 | **MNDY** | Monday.com Ltd. | Technology | 1.418 | 0.538 | 0.538 | 95.7% | +82.2% | 20 | 6 | 0 | 0 | 0 |
| 8 | **CHWY** | Chewy Inc. | Consumer Discretiona | 1.379 | 0.523 | 0.523 | 94.9% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 9 | **BSX** | Boston Scientific | Health Care | 1.351 | 0.513 | 0.513 | 94.0% | +58.5% | 32 | 1 | 0 | 0 | 0 |
| 10 | **NVDA** | NVIDIA Corporation | Technology | 1.302 | 0.514 | 0.514 | 96.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 11 | **GLBE** | Global-E Online | Technology | 1.301 | 0.494 | 0.494 | 93.2% | +47.5% | 11 | 1 | 0 | 0 | 0 |
| 12 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.169 | 0.462 | 0.462 | 93.8% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 13 | **V** | Visa Inc. | Financial Services | 1.114 | 0.440 | 0.440 | 91.2% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 14 | **BUD** | Anheuser-Busch InBev | Consumer Staples | 1.047 | 0.397 | 0.397 | 92.3% | +18.3% | 10 | 1 | 0 | 0 | 0 |
| 15 | **CRH** | CRH plc | Materials | 1.006 | 0.381 | 0.381 | 91.5% | +20.3% | 21 | 2 | 0 | 0 | 0 |
| 16 | **ICE** | Intercontinental Exchange | Financials | 0.996 | 0.377 | 0.377 | 90.6% | +23.8% | 15 | 1 | 0 | 0 | 0 |
| 17 | **MA** | Mastercard Incorporated | Financial Services | 0.981 | 0.372 | 0.372 | 89.7% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 18 | **AFRM** | Affirm Holdings | Financials | 0.980 | 0.371 | 0.371 | 88.9% | +17.1% | 22 | 8 | 0 | 0 | 0 |
| 19 | **DASH** | DoorDash Inc. | Consumer Discretiona | 0.968 | 0.367 | 0.367 | 88.0% | +32.5% | 35 | 10 | 0 | 0 | 0 |
| 20 | **FROG** | JFrog Ltd. | Technology | 0.959 | 0.363 | 0.363 | 87.2% | +51.8% | 20 | 1 | 0 | 0 | 0 |


## Months horizon

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BSX** | Boston Scientific | Health Care | 2.278 | 1.020 | 1.020 | 100.0% | +58.5% | 32 | 1 | 0 | 0 | 0 |
| 2 | **NOW** | ServiceNow, Inc. | Technology | 2.199 | 1.102 | 1.102 | 100.0% | +69.1% | 41 | 4 | 1 | 20 | 0 |
| 3 | **MNDY** | Monday.com Ltd. | Technology | 2.185 | 0.978 | 0.978 | 99.1% | +82.2% | 20 | 6 | 0 | 0 | 0 |
| 4 | **GLBE** | Global-E Online | Technology | 1.900 | 0.850 | 0.850 | 98.3% | +47.5% | 11 | 1 | 0 | 0 | 0 |
| 5 | **MBLY** | Mobileye Global | Technology | 1.857 | 0.831 | 0.831 | 97.4% | +77.4% | 16 | 13 | 0 | 0 | 0 |
| 6 | **MSFT** | Microsoft Corporation | Technology | 1.562 | 0.783 | 0.783 | 97.5% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 7 | **INTU** | Intuit Inc. | Technology | 1.507 | 0.674 | 0.674 | 96.6% | +48.1% | 29 | 5 | 0 | 10 | 0 |
| 8 | **DKNG** | DraftKings Inc. | Consumer Discretiona | 1.502 | 0.672 | 0.672 | 95.7% | +53.8% | 28 | 7 | 0 | 0 | 0 |
| 9 | **ICE** | Intercontinental Exchange | Financials | 1.363 | 0.610 | 0.610 | 94.9% | +23.8% | 15 | 1 | 0 | 0 | 0 |
| 10 | **FROG** | JFrog Ltd. | Technology | 1.330 | 0.595 | 0.595 | 94.0% | +51.8% | 20 | 1 | 0 | 0 | 0 |
| 11 | **DIS** | The Walt Disney Company | Communication Servic | 1.269 | 0.567 | 0.567 | 93.2% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 12 | **V** | Visa Inc. | Financial Services | 1.250 | 0.626 | 0.626 | 95.0% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 13 | **NVDA** | NVIDIA Corporation | Technology | 1.186 | 0.595 | 0.595 | 91.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 14 | **CRM** | Salesforce, Inc. | Technology | 1.186 | 0.530 | 0.530 | 92.3% | +44.3% | 35 | 10 | 1 | 24 | 0 |
| 15 | **DHR** | Danaher Corporation | Healthcare | 1.168 | 0.522 | 0.522 | 91.5% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 16 | **CHWY** | Chewy Inc. | Consumer Discretiona | 1.162 | 0.519 | 0.519 | 90.6% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 17 | **MA** | Mastercard Incorporated | Financial Services | 1.142 | 0.511 | 0.511 | 89.7% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 18 | **BUD** | Anheuser-Busch InBev | Consumer Staples | 1.141 | 0.510 | 0.510 | 88.9% | +18.3% | 10 | 1 | 0 | 0 | 0 |
| 19 | **CVX** | Chevron Corporation | Energy | 1.127 | 0.504 | 0.504 | 88.0% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 20 | **ABT** | Abbott Laboratories | Healthcare | 1.109 | 0.496 | 0.496 | 87.2% | +25.0% | 22 | 6 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-20 20:26:13Z |  |
| yfinance.consensus_fast | ok | 118 | 2026-04-20 20:25:52Z |  |
| yfinance.prices_fast | ok | 10620 | 2026-04-20 20:25:43Z |  |
| stooq.prices | ok | 0 | 2026-04-20 20:23:18Z |  |
| yfinance.consensus_fast | ok | 118 | 2026-04-20 20:22:56Z |  |
| yfinance.prices_fast | ok | 10620 | 2026-04-20 20:22:48Z |  |
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
