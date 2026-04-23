# Invest — Top 15 report

_Generated: **2026-04-23 21:10 UTC** · Scores as of: **2026-04-23**_

🟢 last successful crawl: 0 min ago (at 2026-04-23T21:10:50Z)

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.885 | 1.609 | 1.609 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.289 | 1.361 | 1.361 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.192 | 0.906 | 0.906 | 97.4% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.913 | 0.790 | 0.790 | 96.2% | +10.0% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **ARM** | Arm Holdings plc | Technology | 1.350 | 0.556 | 0.556 | 94.9% | -17.1% | 27 | 10 | 2 | 18 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.046 | 0.429 | 0.429 | 93.6% | -4.2% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.009 | 0.414 | 0.414 | 92.3% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.999 | 0.410 | 0.410 | 91.0% | +2.7% | 20 | 21 | 2 | 14 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.959 | 0.393 | 0.393 | 89.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.936 | 0.384 | 0.384 | 88.5% | +24.2% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.873 | 0.357 | 0.357 | 87.2% | +10.8% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.781 | 0.319 | 0.319 | 85.9% | -2.7% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.734 | 0.299 | 0.299 | 84.6% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.478 | 0.193 | 0.193 | 83.3% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.477 | 0.193 | 0.193 | 82.1% | +19.3% | 21 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.293 | 0.870 | 0.870 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.263 | 0.859 | 0.859 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.679 | 0.635 | 0.635 | 97.4% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.544 | 0.584 | 0.584 | 96.2% | +57.3% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.528 | 0.578 | 0.578 | 94.9% | +10.0% | 41 | 12 | 0 | 27 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.459 | 0.551 | 0.551 | 93.6% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.254 | 0.473 | 0.473 | 92.3% | +39.5% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.245 | 0.470 | 0.470 | 91.0% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.018 | 0.383 | 0.383 | 89.7% | +43.4% | 22 | 2 | 0 | 9 | 0 |
| 10 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.990 | 0.372 | 0.372 | 88.5% | +58.8% | 28 | 7 | 0 | 22 | 0 |
| 11 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.978 | 0.368 | 0.368 | 87.2% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.920 | 0.345 | 0.345 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.910 | 0.342 | 0.342 | 84.6% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.882 | 0.331 | 0.331 | 83.3% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.807 | 0.303 | 0.303 | 82.1% | +12.4% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.799 | 0.767 | 0.767 | 100.0% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.704 | 0.726 | 0.726 | 98.7% | +57.3% | 20 | 1 | 0 | 9 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.649 | 0.702 | 0.702 | 97.4% | +43.4% | 22 | 2 | 0 | 9 | 0 |
| 4 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.617 | 0.689 | 0.689 | 96.2% | +58.8% | 28 | 7 | 0 | 22 | 0 |
| 5 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.578 | 0.672 | 0.672 | 94.9% | +45.8% | 32 | 1 | 0 | 19 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.458 | 0.620 | 0.620 | 93.6% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.257 | 0.533 | 0.533 | 92.3% | +39.5% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.239 | 0.526 | 0.526 | 91.0% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.207 | 0.512 | 0.512 | 89.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.181 | 0.501 | 0.501 | 88.5% | +29.2% | 22 | 6 | 0 | 13 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.043 | 0.441 | 0.441 | 87.2% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.017 | 0.430 | 0.430 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.004 | 0.424 | 0.424 | 84.6% | +21.9% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.920 | 0.388 | 0.388 | 83.3% | +40.5% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.905 | 0.382 | 0.382 | 82.1% | +19.3% | 21 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-04-23 09:07:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 09:07:09Z |  |
| stooq.prices | ok | 0 | 2026-04-23 07:12:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 07:11:59Z |  |
| stooq.prices | ok | 0 | 2026-04-23 05:17:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 05:17:45Z |  |
