# Invest — Top 15 report

_Generated: **2026-04-27 13:51 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T13:51:28Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **APH**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.797 | 1.600 | 1.600 | 100.0% | +7.8% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.945 | 1.240 | 1.240 | 98.7% | -10.3% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.675 | 1.126 | 1.126 | 97.4% | +2.7% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.959 | 0.824 | 0.824 | 96.2% | +17.6% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.273 | 0.535 | 0.535 | 94.9% | +6.5% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.072 | 0.450 | 0.450 | 93.6% | +23.6% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **CLS** | Celestica Inc. | Technology | 1.017 | 0.426 | 0.426 | 92.3% | +0.0% | 18 | 2 | 0 | 7 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.971 | 0.407 | 0.407 | 91.0% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.917 | 0.384 | 0.384 | 89.7% | +8.8% | 63 | 5 | 0 | 26 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.889 | 0.373 | 0.373 | 88.5% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.711 | 0.297 | 0.297 | 87.2% | +0.6% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.644 | 0.269 | 0.269 | 85.9% | +11.3% | 31 | 14 | 2 | 12 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.633 | 0.265 | 0.265 | 84.6% | +17.4% | 14 | 3 | 1 | 5 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.612 | 0.255 | 0.255 | 83.3% | +14.0% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.600 | 0.250 | 0.250 | 82.1% | +19.0% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.528 | 0.954 | 0.954 | 100.0% | +7.8% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.674 | 0.630 | 0.630 | 98.7% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.417 | 0.533 | 0.533 | 97.4% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.392 | 0.523 | 0.523 | 96.2% | +35.7% | 45 | 3 | 1 | 20 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.390 | 0.522 | 0.522 | 94.9% | +56.7% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.063 | 0.398 | 0.398 | 93.6% | +40.4% | 35 | 10 | 0 | 20 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.048 | 0.392 | 0.392 | 92.3% | +17.6% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.042 | 0.390 | 0.390 | 91.0% | +38.6% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.003 | 0.375 | 0.375 | 89.7% | +6.5% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.993 | 0.372 | 0.372 | 88.5% | +2.7% | 21 | 20 | 2 | 14 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.962 | 0.360 | 0.360 | 87.2% | +19.0% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.904 | 0.338 | 0.338 | 85.9% | +46.7% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.872 | 0.326 | 0.326 | 84.6% | +11.3% | 31 | 14 | 2 | 12 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.865 | 0.323 | 0.323 | 83.3% | +17.4% | 14 | 3 | 1 | 5 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.843 | 0.315 | 0.315 | 82.1% | +12.7% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.013 | 0.860 | 0.860 | 100.0% | +56.7% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.572 | 0.669 | 0.669 | 98.7% | +40.3% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.552 | 0.661 | 0.661 | 97.4% | +38.6% | 22 | 2 | 0 | 10 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.388 | 0.590 | 0.590 | 96.2% | +46.4% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.327 | 0.563 | 0.563 | 94.9% | +46.7% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.293 | 0.549 | 0.549 | 93.6% | +35.7% | 45 | 3 | 1 | 20 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.251 | 0.531 | 0.531 | 92.3% | +48.5% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.243 | 0.527 | 0.527 | 91.0% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.203 | 0.510 | 0.510 | 89.7% | +19.0% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.088 | 0.460 | 0.460 | 88.5% | +27.6% | 21 | 7 | 0 | 12 | 0 |
| 11 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.075 | 0.455 | 0.455 | 87.2% | +40.4% | 35 | 10 | 0 | 20 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.067 | 0.451 | 0.451 | 85.9% | +19.8% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.030 | 0.435 | 0.435 | 84.6% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.983 | 0.415 | 0.415 | 83.3% | +38.7% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.978 | 0.413 | 0.413 | 82.1% | +24.1% | 23 | 9 | 0 | 11 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-27 13:51:27Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 13:51:23Z |  |
| stooq.prices | ok | 0 | 2026-04-27 11:52:11Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 11:52:02Z |  |
| stooq.prices | ok | 0 | 2026-04-27 09:59:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 09:59:07Z |  |
| stooq.prices | ok | 0 | 2026-04-27 07:34:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 07:34:20Z |  |
| stooq.prices | ok | 0 | 2026-04-27 04:44:00Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 04:43:54Z |  |
| stooq.prices | ok | 0 | 2026-04-27 01:13:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 01:13:43Z |  |
| edgar.13f | error | 0 | 2026-04-27 00:08:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-27 00:08:21Z |  |
| yfinance.actions | ok | 1056 | 2026-04-27 00:08:13Z |  |
| yfinance.consensus | ok | 79 | 2026-04-27 00:07:59Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-27 00:07:39Z |  |
| yfinance.prices | ok | 7110 | 2026-04-27 00:07:30Z |  |
| stooq.prices | ok | 0 | 2026-04-26 23:24:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 23:23:56Z |  |
