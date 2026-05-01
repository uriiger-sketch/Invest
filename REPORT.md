# Invest — Top 15 report

_Generated: **2026-05-01 23:52 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T23:52:18Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.421 | 1.410 | 1.410 | 100.0% | -16.6% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.791 | 1.151 | 1.151 | 98.7% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.095 | 0.863 | 0.863 | 97.4% | +13.5% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CLS** | Celestica Inc. | Technology | 1.995 | 0.822 | 0.822 | 96.2% | +2.1% | 19 | 1 | 0 | 10 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.779 | 0.733 | 0.733 | 94.9% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.320 | 0.543 | 0.543 | 93.6% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.017 | 0.418 | 0.418 | 92.3% | +17.1% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.988 | 0.407 | 0.407 | 91.0% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.950 | 0.391 | 0.391 | 89.7% | +5.9% | 62 | 5 | 0 | 32 | 0 |
| 10 | ★★ | **AAPL** | Apple Inc. | Technology | 0.778 | 0.320 | 0.320 | 88.5% | +6.5% | 32 | 14 | 2 | 7 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.771 | 0.317 | 0.317 | 87.2% | +23.7% | 18 | 2 | 0 | 3 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.662 | 0.272 | 0.272 | 85.9% | -1.1% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.655 | 0.269 | 0.269 | 84.6% | +25.9% | 45 | 3 | 1 | 19 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.544 | 0.223 | 0.223 | 83.3% | +12.9% | 44 | 3 | 0 | 16 | 0 |
| 15 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.522 | 0.214 | 0.214 | 82.1% | +11.5% | 23 | 3 | 0 | 8 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.920 | 0.703 | 0.703 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.762 | 0.645 | 0.645 | 98.7% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.514 | 0.554 | 0.554 | 97.4% | +59.8% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.472 | 0.538 | 0.538 | 96.2% | +23.7% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.468 | 0.537 | 0.537 | 94.9% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.389 | 0.508 | 0.508 | 93.6% | +25.9% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.166 | 0.426 | 0.426 | 92.3% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.128 | 0.412 | 0.412 | 91.0% | +42.7% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.073 | 0.391 | 0.391 | 89.7% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.035 | 0.378 | 0.378 | 88.5% | +13.5% | 16 | 1 | 0 | 7 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.972 | 0.354 | 0.354 | 87.2% | +11.4% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.939 | 0.342 | 0.342 | 85.9% | +46.5% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.883 | 0.322 | 0.322 | 84.6% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CLS** | Celestica Inc. | Technology | 0.875 | 0.319 | 0.319 | 83.3% | +2.1% | 19 | 1 | 0 | 10 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.847 | 0.308 | 0.308 | 82.1% | +6.5% | 32 | 14 | 2 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.062 | 0.914 | 0.914 | 100.0% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.016 | 0.894 | 0.894 | 98.7% | +59.8% | 21 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.661 | 0.735 | 0.735 | 97.4% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.306 | 0.576 | 0.576 | 96.2% | +51.6% | 28 | 7 | 0 | 22 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.304 | 0.576 | 0.576 | 94.9% | +68.8% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.281 | 0.565 | 0.565 | 93.6% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.267 | 0.559 | 0.559 | 92.3% | +46.5% | 35 | 10 | 1 | 24 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.223 | 0.540 | 0.540 | 91.0% | +32.6% | 21 | 7 | 0 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.108 | 0.488 | 0.488 | 89.7% | +42.7% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.091 | 0.481 | 0.481 | 88.5% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.072 | 0.472 | 0.472 | 87.2% | +21.2% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.066 | 0.469 | 0.469 | 85.9% | +23.7% | 18 | 2 | 0 | 3 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.016 | 0.447 | 0.447 | 84.6% | +19.6% | 22 | 2 | 0 | 8 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.001 | 0.441 | 0.441 | 83.3% | +39.3% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.995 | 0.438 | 0.438 | 82.1% | +32.6% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 23:52:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 23:52:12Z |  |
| stooq.prices | ok | 0 | 2026-05-01 22:49:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 22:49:54Z |  |
| stooq.prices | ok | 0 | 2026-05-01 21:52:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 21:52:54Z |  |
| stooq.prices | ok | 0 | 2026-05-01 20:52:46Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-05-01 20:52:38Z |  |
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
