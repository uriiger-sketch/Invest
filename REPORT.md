# Invest — Top 15 report

_Generated: **2026-04-30 00:11 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T00:10:58Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **BAC**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.129 | 1.266 | 1.266 | 100.0% | -12.3% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.214 | 0.895 | 0.895 | 98.7% | +19.1% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.697 | 0.685 | 0.685 | 97.4% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.502 | 0.606 | 0.606 | 96.2% | +6.6% | 27 | 3 | 0 | 11 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.063 | 0.428 | 0.428 | 94.9% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.054 | 0.424 | 0.424 | 93.6% | +7.9% | 62 | 5 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.020 | 0.410 | 0.410 | 92.3% | +24.6% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.913 | 0.367 | 0.367 | 91.0% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 9 |  | **APH** | Amphenol Corporation | Technology | 0.866 | 0.348 | 0.348 | 89.7% | +14.4% | 14 | 3 | 1 | 3 | 0 |
| 10 | ★★ | **AAPL** | Apple Inc. | Technology | 0.833 | 0.335 | 0.335 | 88.5% | +10.2% | 31 | 14 | 2 | 13 | 0 |
| 11 |  | **CLS** | Celestica Inc. | Technology | 0.832 | 0.334 | 0.334 | 87.2% | +6.3% | 18 | 2 | 0 | 7 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.808 | 0.324 | 0.324 | 85.9% | +1.0% | 29 | 5 | 1 | 16 | 0 |
| 13 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.802 | 0.322 | 0.322 | 84.6% | +2.7% | 13 | 9 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.649 | 0.260 | 0.260 | 83.3% | +15.7% | 22 | 2 | 0 | 8 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.637 | 0.255 | 0.255 | 82.1% | +18.8% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.779 | 0.670 | 0.670 | 100.0% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.519 | 0.571 | 0.571 | 98.7% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.458 | 0.548 | 0.548 | 97.4% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.452 | 0.545 | 0.545 | 96.2% | +57.2% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.295 | 0.486 | 0.486 | 94.9% | +50.3% | 32 | 1 | 0 | 19 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.271 | 0.477 | 0.477 | 93.6% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.215 | 0.456 | 0.456 | 92.3% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.146 | 0.429 | 0.429 | 91.0% | +19.1% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.121 | 0.420 | 0.420 | 89.7% | +6.6% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.108 | 0.415 | 0.415 | 88.5% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.972 | 0.363 | 0.363 | 87.2% | +20.7% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.941 | 0.351 | 0.351 | 85.9% | +48.4% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.917 | 0.342 | 0.342 | 84.6% | +10.2% | 31 | 14 | 2 | 13 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.911 | 0.340 | 0.340 | 83.3% | +18.8% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.896 | 0.334 | 0.334 | 82.1% | +46.5% | 20 | 1 | 0 | 9 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.997 | 0.875 | 0.875 | 100.0% | +50.3% | 32 | 1 | 0 | 19 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.924 | 0.843 | 0.843 | 98.7% | +57.2% | 21 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.532 | 0.669 | 0.669 | 97.4% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.353 | 0.590 | 0.590 | 96.2% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.332 | 0.580 | 0.580 | 94.9% | +48.4% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.325 | 0.577 | 0.577 | 93.6% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.279 | 0.557 | 0.557 | 92.3% | +50.9% | 28 | 7 | 0 | 22 | 0 |
| 8 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.274 | 0.555 | 0.555 | 91.0% | +46.5% | 20 | 1 | 0 | 9 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.238 | 0.539 | 0.539 | 89.7% | +20.7% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.137 | 0.494 | 0.494 | 88.5% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.116 | 0.485 | 0.485 | 87.2% | +29.9% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.074 | 0.466 | 0.466 | 85.9% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.951 | 0.412 | 0.412 | 84.6% | +39.0% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.948 | 0.411 | 0.411 | 83.3% | +33.0% | 31 | 7 | 0 | 22 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.900 | 0.389 | 0.389 | 82.1% | +18.8% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 00:10:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 00:10:48Z |  |
| stooq.prices | ok | 0 | 2026-04-29 23:13:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 23:13:33Z |  |
| stooq.prices | ok | 0 | 2026-04-29 22:13:28Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 22:13:20Z |  |
| stooq.prices | ok | 0 | 2026-04-29 21:07:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 21:07:12Z |  |
| stooq.prices | ok | 0 | 2026-04-29 19:56:36Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 19:56:30Z |  |
| stooq.prices | ok | 0 | 2026-04-29 18:14:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 18:14:45Z |  |
| stooq.prices | ok | 0 | 2026-04-29 16:57:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 16:57:30Z |  |
| stooq.prices | ok | 0 | 2026-04-29 15:20:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 15:20:11Z |  |
| stooq.prices | ok | 0 | 2026-04-29 12:58:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-29 11:09:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 11:09:50Z |  |
