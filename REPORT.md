# Invest — Top 20 report

_Generated: **2026-04-20 22:27 UTC** · Scores as of: **2026-04-20**_

🟢 last successful crawl: 0 min ago (at 2026-04-20T22:27:39Z)

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
| 1 | **AAPL** | Apple Inc. | Technology | 4.511 | 1.784 | 1.784 | 100.0% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 2 | **CVX** | Chevron Corporation | Energy | 3.585 | 1.415 | 1.415 | 98.7% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 3 | **TXN** | Texas Instruments Incorporated | Technology | 2.975 | 1.173 | 1.173 | 100.0% | -3.7% | 15 | 18 | 4 | 15 | 0 |
| 4 | **AFRM** | Affirm Holdings | Financials | 2.118 | 0.832 | 0.832 | 97.4% | +17.1% | 22 | 8 | 0 | 0 | 0 |
| 5 | **SBUX** | Starbucks Corporation | Consumer Cyclical | 1.481 | 0.585 | 0.585 | 96.2% | +1.4% | 17 | 18 | 4 | 15 | 0 |
| 6 | **DIS** | The Walt Disney Company | Communication Servic | 1.329 | 0.518 | 0.518 | 96.2% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 7 | **TSLA** | Tesla, Inc. | Consumer Cyclical | 1.243 | 0.491 | 0.491 | 95.0% | +5.6% | 23 | 18 | 7 | 15 | 0 |
| 8 | **XOM** | Exxon Mobil Corporation | Energy | 1.177 | 0.465 | 0.465 | 93.8% | +11.6% | 13 | 12 | 1 | 14 | 0 |
| 9 | **ADI** | Analog Devices, Inc. | Technology | 1.085 | 0.421 | 0.421 | 94.9% | +2.5% | 29 | 6 | 0 | 16 | 0 |
| 10 | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.020 | 0.395 | 0.395 | 93.6% | +13.3% | 62 | 5 | 0 | 27 | 0 |
| 11 | **C** | Citigroup Inc. | Financial Services | 0.989 | 0.382 | 0.382 | 92.3% | +6.1% | 18 | 4 | 0 | 12 | 0 |
| 12 | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.979 | 0.378 | 0.378 | 91.0% | +6.0% | 35 | 13 | 0 | 16 | 0 |
| 13 | **CRH** | CRH plc | Materials | 0.952 | 0.368 | 0.368 | 89.7% | +20.3% | 21 | 2 | 0 | 0 | 0 |
| 14 | **BAC** | Bank of America Corporation | Financial Services | 0.951 | 0.367 | 0.367 | 88.5% | +15.5% | 22 | 3 | 0 | 10 | 0 |
| 15 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 0.859 | 0.340 | 0.340 | 87.5% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 16 | **CHWY** | Chewy Inc. | Consumer Discretiona | 0.824 | 0.317 | 0.317 | 87.2% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 17 | **DE** | Deere & Company | Industrials | 0.802 | 0.308 | 0.308 | 85.9% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 18 | **MS** | Morgan Stanley | Financial Services | 0.765 | 0.303 | 0.303 | 83.8% | +2.3% | 10 | 14 | 1 | 11 | 0 |
| 19 | **NVDA** | NVIDIA Corporation | Technology | 0.725 | 0.287 | 0.287 | 82.5% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 20 | **DASH** | DoorDash Inc. | Consumer Discretiona | 0.721 | 0.276 | 0.276 | 84.6% | +32.5% | 35 | 10 | 0 | 0 | 0 |


## Weeks horizon

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CVX** | Chevron Corporation | Energy | 2.832 | 1.055 | 1.055 | 100.0% | +16.4% | 19 | 6 | 1 | 9 | 0 |
| 2 | **AAPL** | Apple Inc. | Technology | 2.807 | 1.046 | 1.046 | 98.7% | +8.9% | 31 | 14 | 2 | 14 | 0 |
| 3 | **DIS** | The Walt Disney Company | Communication Servic | 2.130 | 0.791 | 0.791 | 97.4% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 4 | **MBLY** | Mobileye Global | Technology | 1.580 | 0.600 | 0.600 | 97.4% | +77.4% | 16 | 13 | 0 | 0 | 0 |
| 5 | **MSFT** | Microsoft Corporation | Technology | 1.468 | 0.579 | 0.579 | 100.0% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 6 | **BSX** | Boston Scientific | Health Care | 1.451 | 0.537 | 0.537 | 96.2% | +58.5% | 32 | 1 | 0 | 0 | 0 |
| 7 | **MNDY** | Monday.com Ltd. | Technology | 1.418 | 0.538 | 0.538 | 95.7% | +82.2% | 20 | 6 | 0 | 0 | 0 |
| 8 | **CHWY** | Chewy Inc. | Consumer Discretiona | 1.405 | 0.520 | 0.520 | 94.9% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 9 | **GLBE** | Global-E Online | Technology | 1.343 | 0.496 | 0.496 | 93.6% | +47.5% | 11 | 1 | 0 | 0 | 0 |
| 10 | **NVDA** | NVIDIA Corporation | Technology | 1.302 | 0.514 | 0.514 | 96.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 11 | **DE** | Deere & Company | Industrials | 1.273 | 0.470 | 0.470 | 92.3% | +11.9% | 13 | 11 | 0 | 13 | 0 |
| 12 | **TMO** | Thermo Fisher Scientific Inc. | Healthcare | 1.169 | 0.462 | 0.462 | 93.8% | +23.2% | 25 | 2 | 0 | 4 | 0 |
| 13 | **V** | Visa Inc. | Financial Services | 1.114 | 0.440 | 0.440 | 91.2% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 14 | **ICE** | Intercontinental Exchange | Financials | 0.996 | 0.377 | 0.377 | 90.6% | +23.8% | 15 | 1 | 0 | 0 | 0 |
| 15 | **MA** | Mastercard Incorporated | Financial Services | 0.981 | 0.372 | 0.372 | 89.7% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 16 | **FROG** | JFrog Ltd. | Technology | 0.980 | 0.360 | 0.360 | 91.0% | +51.8% | 20 | 1 | 0 | 0 | 0 |
| 17 | **BUD** | Anheuser-Busch InBev | Consumer Staples | 0.961 | 0.353 | 0.353 | 89.7% | +18.3% | 10 | 1 | 0 | 0 | 0 |
| 18 | **DASH** | DoorDash Inc. | Consumer Discretiona | 0.936 | 0.344 | 0.344 | 88.5% | +32.5% | 35 | 10 | 0 | 0 | 0 |
| 19 | **CRH** | CRH plc | Materials | 0.925 | 0.339 | 0.339 | 87.2% | +20.3% | 21 | 2 | 0 | 0 | 0 |
| 20 | **DHR** | Danaher Corporation | Healthcare | 0.910 | 0.334 | 0.334 | 85.9% | +31.0% | 22 | 3 | 0 | 6 | 0 |


## Months horizon

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BSX** | Boston Scientific | Health Care | 2.567 | 1.090 | 1.090 | 100.0% | +58.5% | 32 | 1 | 0 | 0 | 0 |
| 2 | **NOW** | ServiceNow, Inc. | Technology | 2.199 | 1.102 | 1.102 | 100.0% | +69.1% | 41 | 4 | 1 | 20 | 0 |
| 3 | **MNDY** | Monday.com Ltd. | Technology | 2.185 | 0.978 | 0.978 | 99.1% | +82.2% | 20 | 6 | 0 | 0 | 0 |
| 4 | **GLBE** | Global-E Online | Technology | 2.094 | 0.887 | 0.887 | 98.7% | +47.5% | 11 | 1 | 0 | 0 | 0 |
| 5 | **MBLY** | Mobileye Global | Technology | 1.857 | 0.831 | 0.831 | 97.4% | +77.4% | 16 | 13 | 0 | 0 | 0 |
| 6 | **DKNG** | DraftKings Inc. | Consumer Discretiona | 1.707 | 0.722 | 0.722 | 97.4% | +53.8% | 28 | 7 | 0 | 0 | 0 |
| 7 | **MSFT** | Microsoft Corporation | Technology | 1.562 | 0.783 | 0.783 | 97.5% | +38.6% | 53 | 3 | 0 | 18 | 0 |
| 8 | **INTU** | Intuit Inc. | Technology | 1.507 | 0.674 | 0.674 | 96.6% | +48.1% | 29 | 5 | 0 | 10 | 0 |
| 9 | **FROG** | JFrog Ltd. | Technology | 1.477 | 0.624 | 0.624 | 96.2% | +51.8% | 20 | 1 | 0 | 0 | 0 |
| 10 | **ICE** | Intercontinental Exchange | Financials | 1.363 | 0.610 | 0.610 | 94.9% | +23.8% | 15 | 1 | 0 | 0 | 0 |
| 11 | **CRM** | Salesforce, Inc. | Technology | 1.326 | 0.559 | 0.559 | 94.9% | +44.3% | 35 | 10 | 1 | 24 | 0 |
| 12 | **CHWY** | Chewy Inc. | Consumer Discretiona | 1.266 | 0.533 | 0.533 | 93.6% | +41.4% | 21 | 5 | 0 | 0 | 0 |
| 13 | **DIS** | The Walt Disney Company | Communication Servic | 1.251 | 0.527 | 0.527 | 92.3% | +20.8% | 27 | 3 | 1 | 7 | 0 |
| 14 | **V** | Visa Inc. | Financial Services | 1.250 | 0.626 | 0.626 | 95.0% | +25.3% | 35 | 3 | 0 | 9 | 0 |
| 15 | **DHR** | Danaher Corporation | Healthcare | 1.239 | 0.522 | 0.522 | 91.0% | +31.0% | 22 | 3 | 0 | 6 | 0 |
| 16 | **NVDA** | NVIDIA Corporation | Technology | 1.186 | 0.595 | 0.595 | 91.2% | +32.9% | 56 | 2 | 1 | 19 | 0 |
| 17 | **DDOG** | Datadog Inc. | Technology | 1.151 | 0.484 | 0.484 | 89.7% | +38.2% | 44 | 3 | 1 | 0 | 0 |
| 18 | **ABT** | Abbott Laboratories | Healthcare | 1.148 | 0.483 | 0.483 | 88.5% | +25.0% | 22 | 6 | 0 | 13 | 0 |
| 19 | **MA** | Mastercard Incorporated | Financial Services | 1.142 | 0.511 | 0.511 | 89.7% | +26.7% | 35 | 3 | 0 | 14 | 0 |
| 20 | **BUD** | Anheuser-Busch InBev | Consumer Staples | 1.136 | 0.478 | 0.478 | 87.2% | +18.3% | 10 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-20 22:27:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 22:27:29Z |  |
| stooq.prices | ok | 0 | 2026-04-20 21:30:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 21:30:26Z |  |
| stooq.prices | ok | 0 | 2026-04-20 21:24:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-20 21:24:44Z |  |
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
