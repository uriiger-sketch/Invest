# Invest — Top 15 report

_Generated: **2026-05-01 15:57 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T15:57:24Z)

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.407 | 1.413 | 1.413 | 100.0% | -15.3% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.785 | 1.155 | 1.155 | 98.7% | +7.7% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CLS** | Celestica Inc. | Technology | 1.986 | 0.824 | 0.824 | 97.4% | +3.3% | 19 | 1 | 0 | 10 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.952 | 0.809 | 0.809 | 96.2% | +18.8% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.804 | 0.748 | 0.748 | 94.9% | +4.0% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.427 | 0.591 | 0.591 | 93.6% | +2.3% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.998 | 0.413 | 0.413 | 92.3% | +5.0% | 62 | 5 | 0 | 32 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.996 | 0.413 | 0.413 | 91.0% | +23.5% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.955 | 0.395 | 0.395 | 89.7% | +20.4% | 23 | 8 | 0 | 12 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.806 | 0.333 | 0.333 | 88.5% | +4.7% | 32 | 14 | 2 | 7 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.790 | 0.327 | 0.327 | 87.2% | +22.6% | 18 | 2 | 0 | 3 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.688 | 0.285 | 0.285 | 85.9% | +24.6% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.668 | 0.276 | 0.276 | 84.6% | -0.9% | 29 | 5 | 1 | 16 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.580 | 0.240 | 0.240 | 83.3% | +12.8% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.513 | 0.212 | 0.212 | 82.1% | +15.8% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.924 | 0.705 | 0.705 | 100.0% | +7.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.749 | 0.640 | 0.640 | 98.7% | +23.5% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.541 | 0.564 | 0.564 | 97.4% | +61.3% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.461 | 0.534 | 0.534 | 96.2% | +22.6% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.394 | 0.510 | 0.510 | 94.9% | +47.7% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.372 | 0.502 | 0.502 | 93.6% | +24.6% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.156 | 0.422 | 0.422 | 92.3% | +42.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.132 | 0.413 | 0.413 | 91.0% | +18.8% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.129 | 0.412 | 0.412 | 89.7% | +42.3% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.080 | 0.394 | 0.394 | 88.5% | +2.3% | 27 | 3 | 0 | 11 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.969 | 0.353 | 0.353 | 87.2% | +11.5% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.951 | 0.346 | 0.346 | 85.9% | +47.1% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **CLS** | Celestica Inc. | Technology | 0.915 | 0.333 | 0.333 | 84.6% | +3.3% | 19 | 1 | 0 | 10 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.878 | 0.320 | 0.320 | 83.3% | +15.8% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.824 | 0.300 | 0.300 | 82.1% | -15.3% | 36 | 13 | 0 | 15 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.100 | 0.924 | 0.924 | 100.0% | +61.3% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.980 | 0.870 | 0.870 | 98.7% | +47.7% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.685 | 0.739 | 0.739 | 97.4% | +42.7% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.313 | 0.575 | 0.575 | 96.2% | +47.1% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.291 | 0.565 | 0.565 | 94.9% | +50.6% | 28 | 7 | 0 | 22 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.266 | 0.554 | 0.554 | 93.6% | +23.5% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.235 | 0.540 | 0.540 | 92.3% | +66.1% | 16 | 20 | 0 | 14 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.208 | 0.528 | 0.528 | 91.0% | +31.5% | 21 | 7 | 0 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.108 | 0.484 | 0.484 | 89.7% | +42.3% | 36 | 10 | 0 | 21 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.094 | 0.478 | 0.478 | 88.5% | +21.2% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.090 | 0.476 | 0.476 | 87.2% | +15.8% | 10 | 1 | 0 | 2 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.047 | 0.457 | 0.457 | 85.9% | +39.9% | 18 | 10 | 0 | 12 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.045 | 0.456 | 0.456 | 84.6% | +22.6% | 18 | 2 | 0 | 3 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 1.024 | 0.446 | 0.446 | 83.3% | +19.3% | 22 | 2 | 0 | 8 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.971 | 0.423 | 0.423 | 82.1% | +31.5% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 15:57:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 15:57:17Z |  |
| stooq.prices | ok | 0 | 2026-05-01 14:55:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 14:55:01Z |  |
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
