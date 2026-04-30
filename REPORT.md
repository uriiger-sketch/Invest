# Invest — Top 15 report

_Generated: **2026-04-30 23:14 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T23:14:16Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.076 | 1.282 | 1.282 | 100.0% | -15.2% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.977 | 0.822 | 0.822 | 98.7% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.887 | 0.784 | 0.784 | 97.4% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.456 | 0.604 | 0.604 | 96.2% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.404 | 0.582 | 0.582 | 94.9% | +4.5% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.286 | 0.533 | 0.533 | 93.6% | +3.3% | 14 | 8 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.065 | 0.440 | 0.440 | 92.3% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.033 | 0.427 | 0.427 | 91.0% | +7.1% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.955 | 0.394 | 0.394 | 89.7% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.899 | 0.371 | 0.371 | 88.5% | +23.0% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.823 | 0.339 | 0.339 | 87.2% | -2.3% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.781 | 0.321 | 0.321 | 85.9% | +9.8% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.683 | 0.280 | 0.280 | 84.6% | +15.3% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.654 | 0.268 | 0.268 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.648 | 0.266 | 0.266 | 82.1% | +13.9% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.704 | 0.637 | 0.637 | 100.0% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.500 | 0.560 | 0.560 | 98.7% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.500 | 0.560 | 0.560 | 97.4% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.421 | 0.530 | 0.530 | 96.2% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **CRH** | CRH plc | Basic Materials | 1.410 | 0.526 | 0.526 | 94.9% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.197 | 0.445 | 0.445 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.126 | 0.419 | 0.419 | 92.3% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.120 | 0.416 | 0.416 | 91.0% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.095 | 0.407 | 0.407 | 89.7% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.058 | 0.393 | 0.393 | 88.5% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.007 | 0.374 | 0.374 | 87.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.908 | 0.337 | 0.337 | 85.9% | +9.8% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.908 | 0.336 | 0.336 | 84.6% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.875 | 0.324 | 0.324 | 83.3% | +9.8% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.863 | 0.319 | 0.319 | 82.1% | +15.3% | 14 | 3 | 1 | 3 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.997 | 0.872 | 0.872 | 100.0% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.762 | 0.768 | 0.768 | 98.7% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.515 | 0.659 | 0.659 | 97.4% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.446 | 0.629 | 0.629 | 96.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.327 | 0.576 | 0.576 | 94.9% | +71.8% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.291 | 0.561 | 0.561 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **FROG** | JFrog Ltd. | Technology | 1.264 | 0.549 | 0.549 | 92.3% | +46.0% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.232 | 0.534 | 0.534 | 91.0% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.173 | 0.508 | 0.508 | 89.7% | +49.5% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.136 | 0.492 | 0.492 | 88.5% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.133 | 0.491 | 0.491 | 87.2% | +30.7% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.076 | 0.465 | 0.465 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.012 | 0.437 | 0.437 | 84.6% | +33.6% | 31 | 7 | 0 | 26 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.002 | 0.433 | 0.433 | 83.3% | +40.2% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.992 | 0.429 | 0.429 | 82.1% | +19.5% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 23:14:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 23:14:11Z |  |
| stooq.prices | ok | 0 | 2026-04-30 22:04:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 22:04:24Z |  |
| stooq.prices | ok | 0 | 2026-04-30 21:00:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 21:00:00Z |  |
| stooq.prices | ok | 0 | 2026-04-30 19:52:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 19:52:35Z |  |
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
