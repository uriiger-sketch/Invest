# Invest — Top 15 report

_Generated: **2026-04-30 18:09 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T18:09:56Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.079 | 1.286 | 1.286 | 100.0% | -15.0% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.003 | 0.835 | 0.835 | 98.7% | +20.1% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.886 | 0.786 | 0.786 | 97.4% | +10.5% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.482 | 0.616 | 0.616 | 96.2% | +3.7% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.315 | 0.546 | 0.546 | 94.9% | +7.4% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.253 | 0.520 | 0.520 | 93.6% | +4.5% | 14 | 8 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.060 | 0.439 | 0.439 | 92.3% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.996 | 0.412 | 0.412 | 91.0% | +8.5% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.939 | 0.388 | 0.388 | 89.7% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.894 | 0.370 | 0.370 | 88.5% | +23.6% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.827 | 0.341 | 0.341 | 87.2% | -2.1% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.815 | 0.336 | 0.336 | 85.9% | +8.7% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.703 | 0.289 | 0.289 | 84.6% | +14.9% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.665 | 0.273 | 0.273 | 83.3% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.651 | 0.267 | 0.267 | 82.1% | +14.2% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.712 | 0.639 | 0.639 | 100.0% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.501 | 0.560 | 0.560 | 98.7% | +34.2% | 45 | 3 | 1 | 19 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.498 | 0.558 | 0.558 | 97.4% | +10.5% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.451 | 0.541 | 0.541 | 96.2% | +62.5% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.429 | 0.533 | 0.533 | 94.9% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.174 | 0.436 | 0.436 | 93.6% | +47.7% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.121 | 0.416 | 0.416 | 92.3% | +20.1% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.113 | 0.413 | 0.413 | 91.0% | +47.6% | 31 | 2 | 0 | 19 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.089 | 0.405 | 0.405 | 89.7% | +3.7% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.043 | 0.387 | 0.387 | 88.5% | +39.3% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.010 | 0.374 | 0.374 | 87.2% | +53.1% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.899 | 0.333 | 0.333 | 85.9% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.886 | 0.328 | 0.328 | 84.6% | +8.7% | 31 | 14 | 2 | 13 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.874 | 0.323 | 0.323 | 83.3% | +10.1% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.853 | 0.316 | 0.316 | 82.1% | +14.9% | 14 | 3 | 1 | 3 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.054 | 0.894 | 0.894 | 100.0% | +62.5% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.743 | 0.758 | 0.758 | 98.7% | +47.6% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.489 | 0.646 | 0.646 | 97.4% | +39.3% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.453 | 0.630 | 0.630 | 96.2% | +53.1% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.295 | 0.561 | 0.561 | 94.9% | +47.2% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.246 | 0.539 | 0.539 | 93.6% | +24.2% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.243 | 0.538 | 0.538 | 92.3% | +47.7% | 36 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.221 | 0.528 | 0.528 | 91.0% | +51.1% | 28 | 7 | 0 | 22 | 0 |
| 9 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.219 | 0.527 | 0.527 | 89.7% | +67.8% | 16 | 20 | 0 | 14 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.139 | 0.492 | 0.492 | 88.5% | +34.2% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.114 | 0.481 | 0.481 | 87.2% | +30.4% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.057 | 0.456 | 0.456 | 85.9% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.034 | 0.446 | 0.446 | 84.6% | +41.4% | 18 | 10 | 0 | 12 | 0 |
| 14 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.974 | 0.420 | 0.420 | 83.3% | +21.9% | 19 | 2 | 0 | 3 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.972 | 0.419 | 0.419 | 82.1% | +32.8% | 31 | 7 | 0 | 26 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.actions | ok | 1071 | 2026-04-30 01:17:53Z |  |
| yfinance.consensus | ok | 79 | 2026-04-30 01:17:44Z |  |
