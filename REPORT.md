# Invest — Top 15 report

_Generated: **2026-05-04 04:52 UTC** · Scores as of: **2026-05-04**_

🟢 last successful crawl: 0 min ago (at 2026-05-04T04:52:46Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.513 | 1.385 | 1.385 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 3.036 | 1.196 | 1.196 | 98.7% | +5.2% | 20 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.794 | 1.101 | 1.101 | 97.4% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.173 | 0.855 | 0.855 | 96.2% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.381 | 0.541 | 0.541 | 94.9% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.059 | 0.414 | 0.414 | 93.6% | +17.1% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.045 | 0.408 | 0.408 | 92.3% | +14.7% | 59 | 5 | 0 | 32 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.830 | 0.323 | 0.323 | 91.0% | +23.1% | 20 | 2 | 0 | 3 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.789 | 0.307 | 0.307 | 89.7% | +7.3% | 32 | 15 | 2 | 11 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.692 | 0.269 | 0.269 | 88.5% | +25.8% | 44 | 3 | 1 | 18 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.676 | 0.262 | 0.262 | 87.2% | -1.2% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **AVGO** | Broadcom Inc. | Technology | 0.576 | 0.223 | 0.223 | 85.9% | +12.9% | 43 | 3 | 0 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.538 | 0.208 | 0.208 | 84.6% | +11.3% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.531 | 0.205 | 0.205 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.514 | 0.198 | 0.198 | 82.1% | +18.2% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.139 | 0.823 | 0.823 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.591 | 0.611 | 0.611 | 98.7% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.486 | 0.570 | 0.570 | 97.4% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.456 | 0.559 | 0.559 | 96.2% | +23.1% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **CLS** | Celestica Inc. | Technology | 1.362 | 0.523 | 0.523 | 94.9% | +5.2% | 20 | 1 | 0 | 11 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.350 | 0.518 | 0.518 | 93.6% | +25.8% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.179 | 0.452 | 0.452 | 92.3% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.119 | 0.429 | 0.429 | 91.0% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.082 | 0.414 | 0.414 | 89.7% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.026 | 0.392 | 0.392 | 88.5% | +46.8% | 34 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.015 | 0.388 | 0.388 | 87.2% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 12 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.958 | 0.366 | 0.366 | 85.9% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.912 | 0.349 | 0.349 | 84.6% | +12.0% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.865 | 0.330 | 0.330 | 83.3% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.835 | 0.319 | 0.319 | 82.1% | +16.3% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.143 | 0.965 | 0.965 | 100.0% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.120 | 0.955 | 0.955 | 98.7% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.705 | 0.767 | 0.767 | 97.4% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.393 | 0.625 | 0.625 | 96.2% | +46.8% | 34 | 8 | 1 | 24 | 0 |
| 5 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.365 | 0.613 | 0.613 | 94.9% | +51.6% | 28 | 7 | 0 | 22 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.246 | 0.559 | 0.559 | 93.6% | +32.6% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.135 | 0.508 | 0.508 | 92.3% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.108 | 0.496 | 0.496 | 91.0% | +23.1% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.063 | 0.475 | 0.475 | 89.7% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.059 | 0.474 | 0.474 | 88.5% | +21.1% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.040 | 0.465 | 0.465 | 87.2% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.024 | 0.458 | 0.458 | 85.9% | +38.6% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.018 | 0.455 | 0.455 | 84.6% | +20.1% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.013 | 0.453 | 0.453 | 83.3% | +32.4% | 30 | 7 | 0 | 27 | 0 |
| 15 |  | **FROG** | JFrog Ltd. | Technology | 0.928 | 0.414 | 0.414 | 82.1% | +34.9% | 20 | 1 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-04 04:52:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 04:52:38Z |  |
| stooq.prices | ok | 0 | 2026-05-04 01:19:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 01:19:18Z |  |
| edgar.13f | error | 0 | 2026-05-04 00:13:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-04 00:13:26Z |  |
| yfinance.actions | ok | 1123 | 2026-05-04 00:13:18Z |  |
| yfinance.consensus | ok | 79 | 2026-05-04 00:13:07Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-04 00:12:48Z |  |
| yfinance.prices | ok | 7110 | 2026-05-04 00:12:41Z |  |
| stooq.prices | ok | 0 | 2026-05-03 23:28:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 23:28:41Z |  |
| stooq.prices | ok | 0 | 2026-05-03 22:40:42Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 22:40:37Z |  |
| stooq.prices | ok | 0 | 2026-05-03 21:40:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 21:40:51Z |  |
| stooq.prices | ok | 0 | 2026-05-03 20:47:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 20:47:22Z |  |
| stooq.prices | ok | 0 | 2026-05-03 19:57:07Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 19:57:02Z |  |
