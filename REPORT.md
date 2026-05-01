# Invest — Top 15 report

_Generated: **2026-05-01 13:47 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T13:47:57Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AMD**, **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.409 | 1.412 | 1.412 | 100.0% | -14.6% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.790 | 1.156 | 1.156 | 98.7% | +7.8% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CLS** | Celestica Inc. | Technology | 1.985 | 0.822 | 0.822 | 97.4% | +4.0% | 19 | 1 | 0 | 10 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.956 | 0.810 | 0.810 | 96.2% | +19.9% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.779 | 0.737 | 0.737 | 94.9% | +4.9% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.467 | 0.608 | 0.608 | 93.6% | +1.9% | 27 | 3 | 0 | 11 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.989 | 0.409 | 0.409 | 92.3% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.956 | 0.396 | 0.396 | 91.0% | +21.2% | 23 | 8 | 0 | 12 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.925 | 0.383 | 0.383 | 89.7% | +7.4% | 62 | 5 | 0 | 32 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.786 | 0.325 | 0.325 | 88.5% | +5.6% | 32 | 14 | 2 | 7 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.783 | 0.324 | 0.324 | 87.2% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.674 | 0.279 | 0.279 | 85.9% | -0.9% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.660 | 0.273 | 0.273 | 84.6% | +26.2% | 45 | 3 | 1 | 19 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.582 | 0.241 | 0.241 | 83.3% | +13.2% | 44 | 3 | 0 | 16 | 0 |
| 15 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.519 | 0.214 | 0.214 | 82.1% | +12.2% | 23 | 3 | 0 | 8 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.921 | 0.706 | 0.706 | 100.0% | +7.8% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.747 | 0.642 | 0.642 | 98.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.509 | 0.554 | 0.554 | 97.4% | +59.8% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.461 | 0.536 | 0.536 | 96.2% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.423 | 0.522 | 0.522 | 94.9% | +49.2% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.408 | 0.516 | 0.516 | 93.6% | +26.2% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.165 | 0.427 | 0.427 | 92.3% | +19.9% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.139 | 0.417 | 0.417 | 91.0% | +42.5% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.115 | 0.408 | 0.408 | 89.7% | +40.8% | 22 | 2 | 0 | 8 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.083 | 0.396 | 0.396 | 88.5% | +1.9% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.949 | 0.347 | 0.347 | 87.2% | +47.1% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **CLS** | Celestica Inc. | Technology | 0.931 | 0.340 | 0.340 | 85.9% | +4.0% | 19 | 1 | 0 | 10 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.930 | 0.340 | 0.340 | 84.6% | +9.4% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.874 | 0.319 | 0.319 | 83.3% | +15.7% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.837 | 0.306 | 0.306 | 82.1% | -14.6% | 36 | 13 | 0 | 15 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.054 | 0.906 | 0.906 | 100.0% | +59.8% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.041 | 0.900 | 0.900 | 98.7% | +49.2% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.622 | 0.714 | 0.714 | 97.4% | +40.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.318 | 0.578 | 0.578 | 96.2% | +47.1% | 35 | 10 | 1 | 24 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.273 | 0.558 | 0.558 | 94.9% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.258 | 0.552 | 0.552 | 93.6% | +32.7% | 21 | 7 | 0 | 11 | 0 |
| 7 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.255 | 0.550 | 0.550 | 92.3% | +66.3% | 16 | 20 | 0 | 14 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.228 | 0.538 | 0.538 | 91.0% | +48.7% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.120 | 0.490 | 0.490 | 89.7% | +42.5% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.087 | 0.475 | 0.475 | 88.5% | +15.7% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.086 | 0.475 | 0.475 | 87.2% | +20.8% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.054 | 0.461 | 0.461 | 85.9% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.026 | 0.448 | 0.448 | 84.6% | +39.1% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 1.020 | 0.446 | 0.446 | 83.3% | +19.1% | 22 | 2 | 0 | 8 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.983 | 0.429 | 0.429 | 82.1% | +31.7% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 13:47:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 13:47:50Z |  |
| stooq.prices | ok | 0 | 2026-05-01 11:59:27Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 11:59:21Z |  |
| stooq.prices | ok | 0 | 2026-05-01 10:46:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 10:46:30Z |  |
| stooq.prices | ok | 0 | 2026-05-01 09:14:02Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-05-01 09:13:57Z |  |
| stooq.prices | ok | 0 | 2026-05-01 07:16:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 07:16:31Z |  |
| stooq.prices | ok | 0 | 2026-05-01 04:32:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 04:32:36Z |  |
| edgar.13f | error | 0 | 2026-05-01 01:22:52Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-01 01:22:51Z |  |
| yfinance.actions | ok | 1106 | 2026-05-01 01:22:40Z |  |
| yfinance.consensus | ok | 79 | 2026-05-01 01:22:31Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-01 01:22:17Z |  |
| yfinance.prices | ok | 7110 | 2026-05-01 01:22:11Z |  |
| stooq.prices | ok | 0 | 2026-05-01 00:10:18Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 00:10:13Z |  |
