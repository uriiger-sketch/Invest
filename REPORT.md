# Invest — Top 15 report

_Generated: **2026-04-29 15:20 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T15:20:18Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.305 | 1.339 | 1.339 | 100.0% | +7.0% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.771 | 1.122 | 1.122 | 98.7% | -10.3% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.107 | 0.853 | 0.853 | 97.4% | +22.5% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.838 | 0.743 | 0.743 | 96.2% | +9.6% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.364 | 0.551 | 0.551 | 94.9% | +9.4% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.043 | 0.420 | 0.420 | 93.6% | +7.8% | 62 | 5 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.980 | 0.395 | 0.395 | 92.3% | +25.8% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.967 | 0.390 | 0.390 | 91.0% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **APH** | Amphenol Corporation | Technology | 0.875 | 0.352 | 0.352 | 89.7% | +11.9% | 14 | 3 | 1 | 5 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.864 | 0.348 | 0.348 | 88.5% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.810 | 0.326 | 0.326 | 87.2% | +0.4% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.740 | 0.298 | 0.298 | 85.9% | +10.8% | 31 | 14 | 2 | 13 | 0 |
| 13 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.721 | 0.290 | 0.290 | 84.6% | +5.0% | 13 | 9 | 0 | 9 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.690 | 0.277 | 0.277 | 83.3% | +10.3% | 18 | 2 | 0 | 7 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.622 | 0.250 | 0.250 | 82.1% | +18.7% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.806 | 0.668 | 0.668 | 100.0% | +9.6% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.712 | 0.633 | 0.633 | 98.7% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.469 | 0.542 | 0.542 | 97.4% | +59.4% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.464 | 0.540 | 0.540 | 96.2% | +36.2% | 45 | 3 | 1 | 19 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.436 | 0.530 | 0.530 | 94.9% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.364 | 0.503 | 0.503 | 93.6% | +7.0% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.265 | 0.466 | 0.466 | 92.3% | +52.4% | 36 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.197 | 0.441 | 0.441 | 91.0% | +22.5% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.108 | 0.408 | 0.408 | 89.7% | +9.4% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.081 | 0.398 | 0.398 | 88.5% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.937 | 0.344 | 0.344 | 87.2% | +20.0% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.926 | 0.340 | 0.340 | 85.9% | +49.5% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.902 | 0.331 | 0.331 | 84.6% | +48.4% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.840 | 0.307 | 0.307 | 83.3% | +10.8% | 31 | 14 | 2 | 13 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.814 | 0.298 | 0.298 | 82.1% | +18.5% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.971 | 0.858 | 0.858 | 100.0% | +59.4% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.801 | 0.783 | 0.783 | 98.7% | +51.0% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.513 | 0.656 | 0.656 | 97.4% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.439 | 0.624 | 0.624 | 96.2% | +52.4% | 36 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.338 | 0.579 | 0.579 | 94.9% | +49.5% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.330 | 0.576 | 0.576 | 93.6% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.308 | 0.566 | 0.566 | 92.3% | +48.4% | 20 | 1 | 0 | 9 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.284 | 0.556 | 0.556 | 91.0% | +51.9% | 28 | 7 | 0 | 23 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.185 | 0.512 | 0.512 | 89.7% | +20.0% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.181 | 0.510 | 0.510 | 88.5% | +36.2% | 45 | 3 | 1 | 19 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.060 | 0.457 | 0.457 | 87.2% | +25.2% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ABT** | Abbott Laboratories | Healthcare | 1.043 | 0.449 | 0.449 | 85.9% | +28.6% | 21 | 7 | 0 | 12 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.000 | 0.430 | 0.430 | 84.6% | +41.2% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.971 | 0.418 | 0.418 | 83.3% | +34.5% | 31 | 7 | 0 | 22 | 0 |
| 15 |  | **APP** | AppLovin Corporation | Communication Servic | 0.968 | 0.416 | 0.416 | 82.1% | +47.1% | 26 | 4 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-29 15:20:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 15:20:11Z |  |
| stooq.prices | ok | 0 | 2026-04-29 12:58:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-29 11:09:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 11:09:50Z |  |
| stooq.prices | ok | 0 | 2026-04-29 09:09:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 09:09:27Z |  |
| stooq.prices | ok | 0 | 2026-04-29 06:40:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 06:40:50Z |  |
| stooq.prices | ok | 0 | 2026-04-29 04:05:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 04:05:50Z |  |
| edgar.13f | error | 0 | 2026-04-29 01:18:49Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-29 01:18:48Z |  |
| yfinance.actions | ok | 1063 | 2026-04-29 01:18:37Z |  |
| yfinance.consensus | ok | 79 | 2026-04-29 01:18:19Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-29 01:17:54Z |  |
| yfinance.prices | ok | 7110 | 2026-04-29 01:17:45Z |  |
| stooq.prices | ok | 0 | 2026-04-29 00:10:53Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 00:10:48Z |  |
