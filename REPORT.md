# Invest — Top 15 report

_Generated: **2026-05-01 18:06 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T18:06:02Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.446 | 1.423 | 1.423 | 100.0% | -16.8% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.784 | 1.150 | 1.150 | 98.7% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.024 | 0.835 | 0.835 | 97.4% | +15.4% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CLS** | Celestica Inc. | Technology | 1.983 | 0.818 | 0.818 | 96.2% | +2.5% | 19 | 1 | 0 | 10 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.776 | 0.733 | 0.733 | 94.9% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.400 | 0.577 | 0.577 | 93.6% | +2.1% | 27 | 3 | 0 | 11 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.988 | 0.407 | 0.407 | 92.3% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.982 | 0.405 | 0.405 | 91.0% | +18.3% | 23 | 8 | 0 | 12 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.962 | 0.396 | 0.396 | 89.7% | +5.5% | 62 | 5 | 0 | 32 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.794 | 0.327 | 0.327 | 88.5% | +22.5% | 18 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **AAPL** | Apple Inc. | Technology | 0.776 | 0.320 | 0.320 | 87.2% | +6.3% | 32 | 14 | 2 | 7 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.673 | 0.277 | 0.277 | 85.9% | +24.9% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.642 | 0.264 | 0.264 | 84.6% | -0.7% | 29 | 5 | 1 | 16 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.552 | 0.227 | 0.227 | 83.3% | +12.7% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.509 | 0.209 | 0.209 | 82.1% | +16.2% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.924 | 0.705 | 0.705 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.757 | 0.643 | 0.643 | 98.7% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.537 | 0.563 | 0.563 | 97.4% | +61.1% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.457 | 0.533 | 0.533 | 96.2% | +22.5% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.430 | 0.523 | 0.523 | 94.9% | +49.3% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.369 | 0.501 | 0.501 | 93.6% | +24.9% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.158 | 0.423 | 0.423 | 92.3% | +42.6% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.137 | 0.415 | 0.415 | 91.0% | +43.2% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.065 | 0.389 | 0.389 | 89.7% | +15.4% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.061 | 0.387 | 0.387 | 88.5% | +2.1% | 27 | 3 | 0 | 11 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.976 | 0.356 | 0.356 | 87.2% | +11.6% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.945 | 0.345 | 0.345 | 85.9% | +46.9% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **CLS** | Celestica Inc. | Technology | 0.890 | 0.324 | 0.324 | 84.6% | +2.5% | 19 | 1 | 0 | 10 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.883 | 0.322 | 0.322 | 83.3% | +16.2% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.846 | 0.308 | 0.308 | 82.1% | +6.3% | 32 | 14 | 2 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.065 | 0.916 | 0.916 | 100.0% | +61.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.010 | 0.891 | 0.891 | 98.7% | +49.3% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.658 | 0.734 | 0.734 | 97.4% | +42.6% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.341 | 0.593 | 0.593 | 96.2% | +52.5% | 28 | 7 | 0 | 22 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.285 | 0.568 | 0.568 | 94.9% | +46.9% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.274 | 0.563 | 0.563 | 93.6% | +24.1% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.212 | 0.535 | 0.535 | 92.3% | +66.3% | 16 | 20 | 0 | 14 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.212 | 0.535 | 0.535 | 91.0% | +32.1% | 21 | 7 | 0 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.128 | 0.498 | 0.498 | 89.7% | +43.2% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.093 | 0.482 | 0.482 | 88.5% | +16.2% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.075 | 0.474 | 0.474 | 87.2% | +21.1% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.031 | 0.454 | 0.454 | 85.9% | +22.5% | 18 | 2 | 0 | 3 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.022 | 0.450 | 0.450 | 84.6% | +19.6% | 22 | 2 | 0 | 8 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.013 | 0.446 | 0.446 | 83.3% | +39.5% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.992 | 0.437 | 0.437 | 82.1% | +32.4% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-01 04:32:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 04:32:36Z |  |
