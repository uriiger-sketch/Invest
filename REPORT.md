# Invest — Top 15 report

_Generated: **2026-05-05 21:18 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T21:18:09Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **APH**, **BSX**, **CHWY**, **CI**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.322 | 1.613 | 1.613 | 100.0% | +5.5% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.110 | 1.534 | 1.534 | 98.7% | +5.4% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.840 | 0.683 | 0.683 | 97.4% | +8.0% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.224 | 0.452 | 0.452 | 96.2% | +5.9% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.088 | 0.401 | 0.401 | 94.9% | +6.1% | 21 | 19 | 2 | 15 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.088 | 0.400 | 0.400 | 93.6% | +12.4% | 59 | 5 | 0 | 32 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.856 | 0.313 | 0.313 | 92.3% | +21.3% | 44 | 3 | 1 | 18 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.849 | 0.311 | 0.311 | 91.0% | +3.2% | 42 | 11 | 0 | 27 | 0 |
| 9 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.751 | 0.274 | 0.274 | 89.7% | -34.5% | 10 | 4 | 0 | 10 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.751 | 0.274 | 0.274 | 88.5% | +5.8% | 32 | 15 | 2 | 11 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.723 | 0.264 | 0.264 | 87.2% | +26.3% | 20 | 2 | 0 | 3 | 0 |
| 12 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.637 | 0.231 | 0.231 | 85.9% | -13.4% | 36 | 13 | 0 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.617 | 0.224 | 0.224 | 84.6% | +7.3% | 23 | 3 | 0 | 8 | 0 |
| 14 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.592 | 0.214 | 0.214 | 83.3% | +18.4% | 23 | 8 | 0 | 11 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.589 | 0.213 | 0.213 | 82.1% | -2.9% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.956 | 0.717 | 0.717 | 100.0% | +5.5% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.704 | 0.623 | 0.623 | 98.7% | +5.4% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.652 | 0.604 | 0.604 | 97.4% | +67.3% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.531 | 0.559 | 0.559 | 96.2% | +26.3% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.452 | 0.530 | 0.530 | 94.9% | +52.2% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.324 | 0.482 | 0.482 | 93.6% | +21.3% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.167 | 0.424 | 0.424 | 92.3% | +50.3% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.141 | 0.414 | 0.414 | 91.0% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.063 | 0.386 | 0.386 | 89.7% | +5.9% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.021 | 0.370 | 0.370 | 88.5% | +3.2% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.942 | 0.341 | 0.341 | 87.2% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.928 | 0.336 | 0.336 | 85.9% | +10.8% | 18 | 6 | 1 | 11 | 0 |
| 13 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.923 | 0.334 | 0.334 | 84.6% | +44.3% | 34 | 8 | 1 | 24 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.846 | 0.305 | 0.305 | 83.3% | +31.5% | 15 | 3 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.843 | 0.304 | 0.304 | 82.1% | +23.2% | 22 | 2 | 0 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.211 | 0.988 | 0.988 | 100.0% | +67.3% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.052 | 0.916 | 0.916 | 98.7% | +52.2% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.630 | 0.726 | 0.726 | 97.4% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.369 | 0.608 | 0.608 | 96.2% | +50.3% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.310 | 0.581 | 0.581 | 94.9% | +36.1% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.209 | 0.535 | 0.535 | 93.6% | +26.3% | 20 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.201 | 0.532 | 0.532 | 92.3% | +44.3% | 34 | 8 | 1 | 24 | 0 |
| 8 | ★★ | **CI** | The Cigna Group | Healthcare | 1.167 | 0.516 | 0.516 | 91.0% | +23.2% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.147 | 0.508 | 0.508 | 89.7% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.141 | 0.504 | 0.504 | 88.5% | +23.5% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.043 | 0.460 | 0.460 | 87.2% | +34.0% | 30 | 7 | 0 | 27 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 1.024 | 0.452 | 0.452 | 85.9% | +31.5% | 15 | 3 | 0 | 7 | 0 |
| 13 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.014 | 0.447 | 0.447 | 84.6% | +44.2% | 28 | 7 | 0 | 22 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.977 | 0.431 | 0.431 | 83.3% | +39.2% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.922 | 0.406 | 0.406 | 82.1% | +18.5% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-05 21:18:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 21:18:03Z |  |
| stooq.prices | ok | 0 | 2026-05-05 20:09:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 20:09:30Z |  |
| stooq.prices | ok | 0 | 2026-05-05 18:57:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 18:56:58Z |  |
| stooq.prices | ok | 0 | 2026-05-05 17:23:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 17:23:39Z |  |
| stooq.prices | ok | 0 | 2026-05-05 15:53:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 15:53:16Z |  |
| stooq.prices | ok | 0 | 2026-05-05 13:52:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 13:52:51Z |  |
| stooq.prices | ok | 0 | 2026-05-05 11:51:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 11:51:08Z |  |
| stooq.prices | ok | 0 | 2026-05-05 10:23:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 10:23:38Z |  |
| stooq.prices | ok | 0 | 2026-05-05 08:30:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 08:30:25Z |  |
| stooq.prices | ok | 0 | 2026-05-05 06:15:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 06:15:15Z |  |
