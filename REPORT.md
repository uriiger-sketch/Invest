# Invest — Top 15 report

_Generated: **2026-05-01 19:43 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T19:43:09Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.407 | 1.405 | 1.405 | 100.0% | -16.5% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.791 | 1.151 | 1.151 | 98.7% | +7.7% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.069 | 0.853 | 0.853 | 97.4% | +14.0% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CLS** | Celestica Inc. | Technology | 1.998 | 0.824 | 0.824 | 96.2% | +2.0% | 19 | 1 | 0 | 10 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.773 | 0.730 | 0.730 | 94.9% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.341 | 0.552 | 0.552 | 93.6% | +3.4% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.025 | 0.422 | 0.422 | 92.3% | +16.7% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.994 | 0.409 | 0.409 | 91.0% | +23.9% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.949 | 0.391 | 0.391 | 89.7% | +5.7% | 62 | 5 | 0 | 32 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.787 | 0.324 | 0.324 | 88.5% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **AAPL** | Apple Inc. | Technology | 0.774 | 0.318 | 0.318 | 87.2% | +6.4% | 32 | 14 | 2 | 7 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.673 | 0.276 | 0.276 | 85.9% | +24.8% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.660 | 0.271 | 0.271 | 84.6% | -1.2% | 29 | 5 | 1 | 16 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.543 | 0.223 | 0.223 | 83.3% | +12.8% | 44 | 3 | 0 | 16 | 0 |
| 15 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.512 | 0.210 | 0.210 | 82.1% | +11.7% | 23 | 3 | 0 | 8 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.921 | 0.703 | 0.703 | 100.0% | +7.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.758 | 0.643 | 0.643 | 98.7% | +23.9% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.525 | 0.558 | 0.558 | 97.4% | +59.9% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.465 | 0.536 | 0.536 | 96.2% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.450 | 0.530 | 0.530 | 94.9% | +49.6% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.371 | 0.501 | 0.501 | 93.6% | +24.8% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.166 | 0.426 | 0.426 | 92.3% | +42.5% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.139 | 0.416 | 0.416 | 91.0% | +42.9% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.070 | 0.391 | 0.391 | 89.7% | +3.4% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.046 | 0.382 | 0.382 | 88.5% | +14.0% | 16 | 1 | 0 | 7 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.977 | 0.356 | 0.356 | 87.2% | +11.5% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.940 | 0.343 | 0.343 | 85.9% | +46.3% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.884 | 0.322 | 0.322 | 84.6% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CLS** | Celestica Inc. | Technology | 0.878 | 0.320 | 0.320 | 83.3% | +2.0% | 19 | 1 | 0 | 10 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.848 | 0.309 | 0.309 | 82.1% | +6.4% | 32 | 14 | 2 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.035 | 0.902 | 0.902 | 100.0% | +59.9% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.033 | 0.901 | 0.901 | 98.7% | +49.6% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.662 | 0.736 | 0.736 | 97.4% | +42.5% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.320 | 0.583 | 0.583 | 96.2% | +51.6% | 28 | 7 | 0 | 22 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.315 | 0.581 | 0.581 | 94.9% | +68.7% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.271 | 0.561 | 0.561 | 93.6% | +23.9% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.269 | 0.560 | 0.560 | 92.3% | +46.3% | 35 | 10 | 1 | 24 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.212 | 0.535 | 0.535 | 91.0% | +32.0% | 21 | 7 | 0 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.128 | 0.497 | 0.497 | 89.7% | +42.9% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.092 | 0.481 | 0.481 | 88.5% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.070 | 0.472 | 0.472 | 87.2% | +20.9% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.046 | 0.461 | 0.461 | 85.9% | +22.8% | 18 | 2 | 0 | 3 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.025 | 0.451 | 0.451 | 84.6% | +39.6% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 1.012 | 0.446 | 0.446 | 83.3% | +19.2% | 22 | 2 | 0 | 8 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.972 | 0.428 | 0.428 | 82.1% | +31.8% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 19:43:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 19:43:03Z |  |
| stooq.prices | ok | 0 | 2026-05-01 18:06:01Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 18:05:56Z |  |
| stooq.prices | ok | 0 | 2026-05-01 17:00:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 17:00:20Z |  |
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
