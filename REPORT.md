# Invest — Top 15 report

_Generated: **2026-04-24 14:45 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T14:45:13Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.763 | 1.590 | 1.590 | 100.0% | +9.5% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.235 | 1.367 | 1.367 | 98.7% | +14.4% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.220 | 0.937 | 0.937 | 97.4% | +11.9% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.121 | 0.895 | 0.895 | 96.2% | +7.1% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.419 | 0.598 | 0.598 | 94.9% | +4.1% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.128 | 0.474 | 0.474 | 93.6% | -15.2% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.014 | 0.426 | 0.426 | 92.3% | -26.2% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 0.984 | 0.413 | 0.413 | 91.0% | +1.4% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.920 | 0.386 | 0.386 | 89.7% | +25.2% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.879 | 0.369 | 0.369 | 88.5% | +25.3% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.834 | 0.350 | 0.350 | 87.2% | +9.2% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.769 | 0.322 | 0.322 | 85.9% | -2.4% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.744 | 0.311 | 0.311 | 84.6% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.534 | 0.223 | 0.223 | 83.3% | +13.7% | 14 | 3 | 1 | 5 | 0 |
| 15 |  | **CLS** | Celestica Inc. | Technology | 0.533 | 0.222 | 0.222 | 82.1% | -3.1% | 18 | 2 | 0 | 6 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.277 | 0.864 | 0.864 | 100.0% | +14.4% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.255 | 0.855 | 0.855 | 98.7% | +9.5% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.812 | 0.686 | 0.686 | 97.4% | +11.9% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.677 | 0.634 | 0.634 | 96.2% | +25.2% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.321 | 0.499 | 0.499 | 94.9% | +41.0% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.271 | 0.480 | 0.480 | 93.6% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.261 | 0.476 | 0.476 | 92.3% | +57.5% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.106 | 0.417 | 0.417 | 91.0% | +55.4% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.027 | 0.387 | 0.387 | 89.7% | +40.5% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.974 | 0.366 | 0.366 | 88.5% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.906 | 0.340 | 0.340 | 87.2% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.902 | 0.339 | 0.339 | 85.9% | +52.9% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.837 | 0.314 | 0.314 | 84.6% | +7.1% | 16 | 1 | 0 | 7 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.836 | 0.314 | 0.314 | 83.3% | +16.0% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.818 | 0.307 | 0.307 | 82.1% | +4.1% | 21 | 20 | 2 | 14 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.862 | 0.790 | 0.790 | 100.0% | +57.5% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.584 | 0.671 | 0.671 | 98.7% | +40.5% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **FROG** | JFrog Ltd. | Technology | 1.508 | 0.638 | 0.638 | 97.4% | +53.6% | 20 | 1 | 0 | 9 | 0 |
| 4 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.458 | 0.617 | 0.617 | 96.2% | +55.4% | 28 | 7 | 0 | 22 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.391 | 0.588 | 0.588 | 94.9% | +52.9% | 35 | 10 | 1 | 24 | 0 |
| 6 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.359 | 0.574 | 0.574 | 93.6% | +37.1% | 32 | 1 | 0 | 19 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.348 | 0.570 | 0.570 | 92.3% | +41.0% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.257 | 0.530 | 0.530 | 91.0% | +25.2% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.234 | 0.521 | 0.521 | 89.7% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.122 | 0.473 | 0.473 | 88.5% | +22.3% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.084 | 0.456 | 0.456 | 87.2% | +29.1% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.029 | 0.433 | 0.433 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.987 | 0.415 | 0.415 | 84.6% | +22.7% | 19 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.983 | 0.413 | 0.413 | 83.3% | +42.0% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.943 | 0.396 | 0.396 | 82.1% | +25.0% | 23 | 9 | 0 | 11 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 14:45:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 14:45:06Z |  |
| stooq.prices | ok | 0 | 2026-04-24 12:42:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 12:42:38Z |  |
| stooq.prices | ok | 0 | 2026-04-24 11:37:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 11:37:32Z |  |
| stooq.prices | ok | 0 | 2026-04-24 10:13:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 10:13:04Z |  |
| stooq.prices | ok | 0 | 2026-04-24 08:25:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 08:25:41Z |  |
| stooq.prices | ok | 0 | 2026-04-24 06:08:27Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-24 06:08:18Z |  |
| stooq.prices | ok | 0 | 2026-04-24 03:54:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 03:54:08Z |  |
| edgar.13f | error | 0 | 2026-04-24 00:11:13Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-24 00:11:12Z |  |
| yfinance.actions | ok | 1056 | 2026-04-24 00:10:57Z |  |
| yfinance.consensus | ok | 79 | 2026-04-24 00:10:49Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-24 00:10:38Z |  |
| yfinance.prices | ok | 7110 | 2026-04-24 00:10:32Z |  |
