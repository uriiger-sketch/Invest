# Invest — Top 15 report

_Generated: **2026-04-30 15:14 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T15:14:10Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.060 | 1.277 | 1.277 | 100.0% | -13.6% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.065 | 0.860 | 0.860 | 98.7% | +20.6% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.912 | 0.796 | 0.796 | 97.4% | +10.1% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.449 | 0.602 | 0.602 | 96.2% | +5.6% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.295 | 0.537 | 0.537 | 94.9% | +9.1% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.289 | 0.535 | 0.535 | 93.6% | +4.2% | 14 | 8 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.055 | 0.437 | 0.437 | 92.3% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.991 | 0.410 | 0.410 | 91.0% | +9.3% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.966 | 0.399 | 0.399 | 89.7% | +21.2% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.874 | 0.361 | 0.361 | 88.5% | +25.4% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.826 | 0.340 | 0.340 | 87.2% | -1.3% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.793 | 0.327 | 0.327 | 85.9% | +9.8% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.681 | 0.280 | 0.280 | 84.6% | +16.1% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.672 | 0.276 | 0.276 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.652 | 0.268 | 0.268 | 82.1% | +15.3% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.714 | 0.644 | 0.644 | 100.0% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.492 | 0.560 | 0.560 | 98.7% | +33.7% | 45 | 3 | 1 | 19 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.479 | 0.555 | 0.555 | 97.4% | +63.3% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.476 | 0.554 | 0.554 | 96.2% | +10.1% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **CRH** | CRH plc | Basic Materials | 1.407 | 0.528 | 0.528 | 94.9% | +21.2% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.185 | 0.444 | 0.444 | 93.6% | +47.6% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.164 | 0.436 | 0.436 | 92.3% | +49.9% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.148 | 0.430 | 0.430 | 91.0% | +20.6% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.101 | 0.412 | 0.412 | 89.7% | +5.6% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.054 | 0.394 | 0.394 | 88.5% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.997 | 0.372 | 0.372 | 87.2% | +51.8% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.892 | 0.332 | 0.332 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.888 | 0.331 | 0.331 | 84.6% | +9.8% | 31 | 14 | 2 | 13 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.862 | 0.321 | 0.321 | 83.3% | +16.1% | 14 | 3 | 1 | 3 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.852 | 0.317 | 0.317 | 82.1% | +10.1% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.108 | 0.919 | 0.919 | 100.0% | +63.3% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.842 | 0.802 | 0.802 | 98.7% | +49.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.517 | 0.659 | 0.659 | 97.4% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.429 | 0.620 | 0.620 | 96.2% | +51.8% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.297 | 0.562 | 0.562 | 94.9% | +46.9% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.265 | 0.548 | 0.548 | 93.6% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.250 | 0.542 | 0.542 | 92.3% | +47.6% | 36 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.208 | 0.523 | 0.523 | 91.0% | +50.4% | 28 | 7 | 0 | 22 | 0 |
| 9 |  | **ABT** | Abbott Laboratories | Healthcare | 1.145 | 0.496 | 0.496 | 89.7% | +31.2% | 21 | 7 | 0 | 11 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.118 | 0.484 | 0.484 | 88.5% | +33.7% | 45 | 3 | 1 | 19 | 0 |
| 11 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.048 | 0.453 | 0.453 | 87.2% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.032 | 0.446 | 0.446 | 85.9% | +41.0% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.030 | 0.445 | 0.445 | 84.6% | +59.4% | 16 | 20 | 0 | 14 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.982 | 0.424 | 0.424 | 83.3% | +33.0% | 31 | 7 | 0 | 26 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.942 | 0.406 | 0.406 | 82.1% | +18.7% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-04-30 01:17:31Z |  |
| yfinance.prices | ok | 7110 | 2026-04-30 01:17:27Z |  |
| stooq.prices | ok | 0 | 2026-04-30 00:10:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 00:10:48Z |  |
