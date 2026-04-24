# Invest — Top 15 report

_Generated: **2026-04-24 00:05 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T00:05:55Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BAC**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.883 | 1.614 | 1.614 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.289 | 1.366 | 1.366 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.189 | 0.908 | 0.908 | 97.4% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.918 | 0.795 | 0.795 | 96.2% | +10.0% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **ARM** | Arm Holdings plc | Technology | 1.353 | 0.559 | 0.559 | 94.9% | -17.1% | 27 | 10 | 2 | 18 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.047 | 0.431 | 0.431 | 93.6% | -4.2% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.013 | 0.417 | 0.417 | 92.3% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.006 | 0.414 | 0.414 | 91.0% | +2.7% | 20 | 21 | 2 | 14 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.967 | 0.398 | 0.398 | 89.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.937 | 0.385 | 0.385 | 88.5% | +24.2% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.874 | 0.359 | 0.359 | 87.2% | +10.8% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.782 | 0.321 | 0.321 | 85.9% | -2.7% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.740 | 0.303 | 0.303 | 84.6% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.480 | 0.195 | 0.195 | 83.3% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.479 | 0.194 | 0.194 | 82.1% | +19.3% | 21 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.329 | 0.877 | 0.877 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.299 | 0.866 | 0.866 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.710 | 0.643 | 0.643 | 97.4% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.559 | 0.585 | 0.585 | 96.2% | +10.0% | 41 | 12 | 0 | 27 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.476 | 0.554 | 0.554 | 94.9% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.278 | 0.479 | 0.479 | 93.6% | +39.5% | 44 | 3 | 1 | 19 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.269 | 0.475 | 0.475 | 92.3% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.033 | 0.386 | 0.386 | 91.0% | +43.4% | 22 | 2 | 0 | 9 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.005 | 0.375 | 0.375 | 89.7% | +58.8% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.993 | 0.370 | 0.370 | 88.5% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 11 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.964 | 0.360 | 0.360 | 87.2% | +57.3% | 20 | 1 | 0 | 9 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.933 | 0.348 | 0.348 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.923 | 0.344 | 0.344 | 84.6% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.895 | 0.334 | 0.334 | 83.3% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.833 | 0.310 | 0.310 | 82.1% | +12.4% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.807 | 0.768 | 0.768 | 100.0% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.657 | 0.703 | 0.703 | 98.7% | +43.4% | 22 | 2 | 0 | 9 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.625 | 0.690 | 0.690 | 97.4% | +58.8% | 28 | 7 | 0 | 22 | 0 |
| 4 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.583 | 0.672 | 0.672 | 96.2% | +45.8% | 32 | 1 | 0 | 19 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.536 | 0.651 | 0.651 | 94.9% | +57.3% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.465 | 0.621 | 0.621 | 93.6% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.265 | 0.535 | 0.535 | 92.3% | +39.5% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.246 | 0.527 | 0.527 | 91.0% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.217 | 0.515 | 0.515 | 89.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.187 | 0.502 | 0.502 | 88.5% | +29.2% | 22 | 6 | 0 | 12 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.049 | 0.442 | 0.442 | 87.2% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.023 | 0.431 | 0.431 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.011 | 0.426 | 0.426 | 84.6% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.926 | 0.389 | 0.389 | 83.3% | +40.5% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.910 | 0.383 | 0.383 | 82.1% | +19.3% | 21 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 00:05:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 00:05:49Z |  |
| stooq.prices | ok | 0 | 2026-04-23 23:09:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 23:09:49Z |  |
| stooq.prices | ok | 0 | 2026-04-23 22:04:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 22:04:12Z |  |
| stooq.prices | ok | 0 | 2026-04-23 21:10:49Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 21:10:43Z |  |
| stooq.prices | ok | 0 | 2026-04-23 20:15:01Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-23 20:14:56Z |  |
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
