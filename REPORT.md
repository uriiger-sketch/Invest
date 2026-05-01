# Invest — Top 15 report

_Generated: **2026-05-01 00:10 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T00:10:19Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **AMD**, **ANET**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.838 | 1.556 | 1.556 | 100.0% | -15.2% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.618 | 1.061 | 1.061 | 98.7% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.959 | 0.794 | 0.794 | 97.4% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 4 |  | **CLS** | Celestica Inc. | Technology | 1.616 | 0.655 | 0.655 | 96.2% | +4.5% | 19 | 1 | 0 | 10 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.494 | 0.606 | 0.606 | 94.9% | +3.3% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.430 | 0.580 | 0.580 | 93.6% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.028 | 0.417 | 0.417 | 92.3% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.985 | 0.399 | 0.399 | 91.0% | +7.1% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.913 | 0.370 | 0.370 | 89.7% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.847 | 0.344 | 0.344 | 88.5% | +23.0% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.768 | 0.312 | 0.312 | 87.2% | -2.3% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.735 | 0.298 | 0.298 | 85.9% | +9.8% | 31 | 14 | 2 | 7 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.594 | 0.241 | 0.241 | 84.6% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.577 | 0.234 | 0.234 | 83.3% | +13.9% | 44 | 3 | 0 | 16 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.551 | 0.224 | 0.224 | 82.1% | +17.7% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.890 | 0.678 | 0.678 | 100.0% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.770 | 0.635 | 0.635 | 98.7% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.554 | 0.556 | 0.556 | 97.4% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CRH** | CRH plc | Basic Materials | 1.459 | 0.522 | 0.522 | 96.2% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.457 | 0.521 | 0.521 | 94.9% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.222 | 0.437 | 0.437 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.148 | 0.410 | 0.410 | 92.3% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.142 | 0.408 | 0.408 | 91.0% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.129 | 0.403 | 0.403 | 89.7% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.077 | 0.385 | 0.385 | 88.5% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.023 | 0.365 | 0.365 | 87.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.982 | 0.350 | 0.350 | 85.9% | -15.2% | 36 | 13 | 0 | 15 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.938 | 0.334 | 0.334 | 84.6% | +9.8% | 31 | 14 | 2 | 7 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.920 | 0.328 | 0.328 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.903 | 0.322 | 0.322 | 82.1% | +9.8% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.999 | 0.873 | 0.873 | 100.0% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.765 | 0.769 | 0.769 | 98.7% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.517 | 0.660 | 0.660 | 97.4% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.448 | 0.630 | 0.630 | 96.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.326 | 0.576 | 0.576 | 94.9% | +71.8% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.294 | 0.562 | 0.562 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **FROG** | JFrog Ltd. | Technology | 1.267 | 0.550 | 0.550 | 92.3% | +46.0% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.239 | 0.538 | 0.538 | 91.0% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.173 | 0.509 | 0.509 | 89.7% | +49.5% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.142 | 0.495 | 0.495 | 88.5% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.136 | 0.492 | 0.492 | 87.2% | +30.7% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.078 | 0.467 | 0.467 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.014 | 0.438 | 0.438 | 84.6% | +33.6% | 31 | 7 | 0 | 26 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.005 | 0.434 | 0.434 | 83.3% | +40.2% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.994 | 0.430 | 0.430 | 82.1% | +19.5% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 00:10:18Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 00:10:13Z |  |
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
