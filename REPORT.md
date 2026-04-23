# Invest — Top 15 report

_Generated: **2026-04-23 19:07 UTC** · Scores as of: **2026-04-23**_

🟢 last successful crawl: 0 min ago (at 2026-04-23T19:07:27Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.896 | 1.615 | 1.615 | 100.0% | +8.5% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.277 | 1.358 | 1.358 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.162 | 0.894 | 0.894 | 97.4% | +14.5% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.904 | 0.787 | 0.787 | 96.2% | +10.3% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **ARM** | Arm Holdings plc | Technology | 1.352 | 0.557 | 0.557 | 94.9% | -16.7% | 27 | 10 | 2 | 18 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.053 | 0.432 | 0.432 | 93.6% | -3.9% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.015 | 0.417 | 0.417 | 92.3% | +3.0% | 27 | 3 | 0 | 11 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.997 | 0.409 | 0.409 | 91.0% | +2.8% | 20 | 21 | 2 | 14 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.948 | 0.389 | 0.389 | 89.7% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.944 | 0.387 | 0.387 | 88.5% | +24.6% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.887 | 0.363 | 0.363 | 87.2% | +10.7% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.770 | 0.315 | 0.315 | 85.9% | -2.1% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.721 | 0.295 | 0.295 | 84.6% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.488 | 0.198 | 0.198 | 83.3% | +13.0% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.485 | 0.196 | 0.196 | 82.1% | +21.2% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.284 | 0.868 | 0.868 | 100.0% | +8.5% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.254 | 0.856 | 0.856 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.681 | 0.637 | 0.637 | 97.4% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.557 | 0.590 | 0.590 | 96.2% | +58.0% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.528 | 0.579 | 0.579 | 94.9% | +10.3% | 41 | 12 | 0 | 27 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.437 | 0.544 | 0.544 | 93.6% | +57.1% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.251 | 0.473 | 0.473 | 92.3% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.248 | 0.472 | 0.472 | 91.0% | +39.1% | 44 | 3 | 1 | 19 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.011 | 0.381 | 0.381 | 89.7% | +43.0% | 22 | 2 | 0 | 9 | 0 |
| 10 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.005 | 0.379 | 0.379 | 88.5% | +14.5% | 16 | 1 | 0 | 7 | 0 |
| 11 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.001 | 0.377 | 0.377 | 87.2% | +59.4% | 28 | 7 | 0 | 22 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.938 | 0.353 | 0.353 | 85.9% | +43.4% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.905 | 0.340 | 0.340 | 84.6% | +21.2% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.881 | 0.331 | 0.331 | 83.3% | +55.0% | 35 | 10 | 1 | 24 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.801 | 0.301 | 0.301 | 82.1% | +12.2% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.736 | 0.741 | 0.741 | 100.0% | +57.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.733 | 0.739 | 0.739 | 98.7% | +58.0% | 20 | 1 | 0 | 9 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.643 | 0.701 | 0.701 | 97.4% | +59.4% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.639 | 0.699 | 0.699 | 96.2% | +43.0% | 22 | 2 | 0 | 9 | 0 |
| 5 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.552 | 0.661 | 0.661 | 94.9% | +45.0% | 32 | 1 | 0 | 19 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.459 | 0.621 | 0.621 | 93.6% | +55.0% | 35 | 10 | 1 | 24 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.241 | 0.527 | 0.527 | 92.3% | +39.1% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.228 | 0.521 | 0.521 | 91.0% | +21.2% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.219 | 0.518 | 0.518 | 89.7% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.204 | 0.511 | 0.511 | 88.5% | +29.8% | 22 | 6 | 0 | 13 | 0 |
| 11 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.062 | 0.450 | 0.450 | 87.2% | +43.4% | 35 | 10 | 0 | 20 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.061 | 0.449 | 0.449 | 85.9% | +21.4% | 22 | 2 | 0 | 8 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.022 | 0.433 | 0.433 | 84.6% | +22.4% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **BAC** | Bank of America Corporation | Financial Services | 0.904 | 0.382 | 0.382 | 83.3% | +19.4% | 21 | 3 | 0 | 9 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.898 | 0.379 | 0.379 | 82.1% | +39.7% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-23 19:07:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 19:07:20Z |  |
| stooq.prices | ok | 0 | 2026-04-23 17:49:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 17:49:40Z |  |
| stooq.prices | ok | 0 | 2026-04-23 14:05:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 14:05:06Z |  |
| stooq.prices | ok | 0 | 2026-04-23 11:59:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 11:59:16Z |  |
| stooq.prices | ok | 0 | 2026-04-23 10:51:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 10:50:57Z |  |
| stooq.prices | ok | 0 | 2026-04-23 09:07:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 09:07:09Z |  |
| stooq.prices | ok | 0 | 2026-04-23 07:12:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 07:11:59Z |  |
| stooq.prices | ok | 0 | 2026-04-23 05:17:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 05:17:45Z |  |
| stooq.prices | ok | 0 | 2026-04-23 02:33:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 02:33:09Z |  |
| edgar.13f | error | 0 | 2026-04-23 00:12:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-23 00:12:25Z |  |
