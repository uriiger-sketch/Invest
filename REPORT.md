# Invest — Top 15 report

_Generated: **2026-04-30 18:37 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T18:37:27Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **APH**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.063 | 1.277 | 1.277 | 100.0% | -14.8% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.019 | 0.840 | 0.840 | 98.7% | +19.7% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.861 | 0.773 | 0.773 | 97.4% | +11.2% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.475 | 0.612 | 0.612 | 96.2% | +3.8% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.330 | 0.551 | 0.551 | 94.9% | +6.8% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.251 | 0.518 | 0.518 | 93.6% | +4.4% | 14 | 8 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.059 | 0.438 | 0.438 | 92.3% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.011 | 0.418 | 0.418 | 91.0% | +7.9% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.955 | 0.394 | 0.394 | 89.7% | +21.0% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.930 | 0.384 | 0.384 | 88.5% | +22.3% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.823 | 0.339 | 0.339 | 87.2% | -2.1% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.808 | 0.333 | 0.333 | 85.9% | +8.8% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.688 | 0.282 | 0.282 | 84.6% | +15.3% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.664 | 0.272 | 0.272 | 83.3% | +16.0% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.640 | 0.263 | 0.263 | 82.1% | +14.4% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.712 | 0.640 | 0.640 | 100.0% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.507 | 0.563 | 0.563 | 98.7% | +11.2% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.504 | 0.562 | 0.562 | 97.4% | +34.1% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.436 | 0.536 | 0.536 | 96.2% | +61.1% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **CRH** | CRH plc | Basic Materials | 1.412 | 0.527 | 0.527 | 94.9% | +21.0% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.169 | 0.435 | 0.435 | 93.6% | +47.0% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.129 | 0.420 | 0.420 | 92.3% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.120 | 0.417 | 0.417 | 91.0% | +19.7% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.089 | 0.405 | 0.405 | 89.7% | +3.8% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.049 | 0.390 | 0.390 | 88.5% | +39.2% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.008 | 0.375 | 0.375 | 87.2% | +52.5% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.898 | 0.333 | 0.333 | 85.9% | +16.0% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.889 | 0.330 | 0.330 | 84.6% | +8.8% | 31 | 14 | 2 | 13 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.870 | 0.322 | 0.322 | 83.3% | +9.8% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.861 | 0.319 | 0.319 | 82.1% | +15.3% | 14 | 3 | 1 | 3 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.019 | 0.882 | 0.882 | 100.0% | +61.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.765 | 0.770 | 0.770 | 98.7% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.496 | 0.651 | 0.651 | 97.4% | +39.2% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.444 | 0.628 | 0.628 | 96.2% | +52.5% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.323 | 0.575 | 0.575 | 94.9% | +47.6% | 20 | 1 | 0 | 9 | 0 |
| 6 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.292 | 0.561 | 0.561 | 93.6% | +70.1% | 16 | 20 | 0 | 14 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.248 | 0.542 | 0.542 | 92.3% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.228 | 0.533 | 0.533 | 91.0% | +47.0% | 36 | 10 | 0 | 21 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.212 | 0.526 | 0.526 | 89.7% | +50.5% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.143 | 0.495 | 0.495 | 88.5% | +34.1% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.134 | 0.491 | 0.491 | 87.2% | +30.7% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.055 | 0.457 | 0.457 | 85.9% | +16.0% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.032 | 0.446 | 0.446 | 84.6% | +41.0% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.974 | 0.421 | 0.421 | 83.3% | +32.6% | 31 | 7 | 0 | 26 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.953 | 0.412 | 0.412 | 82.1% | +18.6% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 18:37:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 18:37:21Z |  |
| stooq.prices | ok | 0 | 2026-04-30 18:09:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 18:09:46Z |  |
| stooq.prices | ok | 0 | 2026-04-30 16:50:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 16:50:49Z |  |
| stooq.prices | ok | 0 | 2026-04-30 15:14:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 15:14:04Z |  |
| stooq.prices | ok | 0 | 2026-04-30 12:58:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-30 11:10:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 11:10:54Z |  |
| stooq.prices | ok | 0 | 2026-04-30 09:11:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 09:10:56Z |  |
| stooq.prices | ok | 0 | 2026-04-30 06:44:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 06:44:48Z |  |
| stooq.prices | ok | 0 | 2026-04-30 04:07:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 04:07:41Z |  |
| edgar.13f | error | 0 | 2026-04-30 01:18:07Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-30 01:18:07Z |  |
