# Invest — Top 15 report

_Generated: **2026-05-07 20:42 UTC** · Scores as of: **2026-05-07**_

🟢 last successful crawl: 0 min ago (at 2026-05-07T20:42:34Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **ABT**, **AMZN**, **ANET**, **APH**, **BSX**, **CHWY**, **CI**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.604 | 1.441 | 1.441 | 100.0% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.103 | 0.651 | 0.651 | 98.7% | -23.5% | 35 | 14 | 0 | 22 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.099 | 0.650 | 0.650 | 97.4% | -6.2% | 44 | 3 | 1 | 17 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.734 | 0.535 | 0.535 | 96.2% | +11.0% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.227 | 0.374 | 0.374 | 94.9% | +14.1% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 1.061 | 0.322 | 0.322 | 93.6% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.055 | 0.320 | 0.320 | 92.3% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 8 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.883 | 0.266 | 0.266 | 91.0% | -22.1% | 10 | 4 | 0 | 11 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.793 | 0.237 | 0.237 | 89.7% | +4.3% | 14 | 8 | 0 | 9 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.760 | 0.227 | 0.227 | 88.5% | +17.4% | 22 | 8 | 0 | 11 | 0 |
| 11 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.758 | 0.226 | 0.226 | 87.2% | +6.3% | 23 | 3 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.705 | 0.210 | 0.210 | 85.9% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.685 | 0.203 | 0.203 | 84.6% | +18.0% | 27 | 3 | 1 | 5 | 0 |
| 14 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.608 | 0.179 | 0.179 | 83.3% | +11.8% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **CVX** | Chevron Corporation | Energy | 0.595 | 0.175 | 0.175 | 82.1% | +17.7% | 18 | 6 | 1 | 11 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.973 | 0.691 | 0.691 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.849 | 0.647 | 0.647 | 98.7% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.561 | 0.544 | 0.544 | 97.4% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.537 | 0.536 | 0.536 | 96.2% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.267 | 0.440 | 0.440 | 94.9% | +28.4% | 27 | 2 | 0 | 13 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.215 | 0.421 | 0.421 | 93.6% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.154 | 0.399 | 0.399 | 92.3% | +17.7% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.127 | 0.390 | 0.390 | 91.0% | +45.0% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.087 | 0.375 | 0.375 | 89.7% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.917 | 0.315 | 0.315 | 88.5% | +14.1% | 61 | 5 | 0 | 32 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.913 | 0.314 | 0.314 | 87.2% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.912 | 0.313 | 0.313 | 85.9% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.873 | 0.299 | 0.299 | 84.6% | -6.2% | 44 | 3 | 1 | 17 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.858 | 0.294 | 0.294 | 83.3% | +19.9% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.839 | 0.287 | 0.287 | 82.1% | +36.4% | 21 | 7 | 0 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.468 | 1.101 | 1.101 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.027 | 0.902 | 0.902 | 98.7% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.631 | 0.724 | 0.724 | 97.4% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.336 | 0.591 | 0.591 | 96.2% | +36.4% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.242 | 0.549 | 0.549 | 94.9% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.233 | 0.545 | 0.545 | 93.6% | +45.0% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.174 | 0.518 | 0.518 | 92.3% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.138 | 0.502 | 0.502 | 91.0% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.119 | 0.493 | 0.493 | 89.7% | +22.6% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.112 | 0.490 | 0.490 | 88.5% | +28.4% | 27 | 2 | 0 | 13 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.042 | 0.459 | 0.459 | 87.2% | +19.9% | 22 | 2 | 0 | 10 | 0 |
| 12 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.976 | 0.429 | 0.429 | 85.9% | +24.5% | 24 | 8 | 0 | 9 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.975 | 0.428 | 0.428 | 84.6% | +31.0% | 30 | 7 | 0 | 25 | 0 |
| 14 |  | **BAC** | Bank of America Corporation | Financial Services | 0.967 | 0.425 | 0.425 | 83.3% | +19.3% | 22 | 3 | 0 | 9 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.942 | 0.413 | 0.413 | 82.1% | +38.3% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-07 20:42:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 20:42:28Z |  |
| stooq.prices | ok | 0 | 2026-05-07 19:18:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 19:18:07Z |  |
| stooq.prices | ok | 0 | 2026-05-07 17:25:53Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 17:25:47Z |  |
| stooq.prices | ok | 0 | 2026-05-07 15:40:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 15:40:14Z |  |
| stooq.prices | ok | 0 | 2026-05-07 13:05:49Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 13:05:44Z |  |
| stooq.prices | ok | 0 | 2026-05-07 11:10:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 11:10:04Z |  |
| stooq.prices | ok | 0 | 2026-05-07 08:49:50Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 08:49:44Z |  |
| stooq.prices | ok | 0 | 2026-05-07 06:10:21Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 06:10:16Z |  |
| stooq.prices | ok | 0 | 2026-05-07 02:45:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 02:45:49Z |  |
| edgar.13f | error | 0 | 2026-05-07 01:18:01Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-07 01:18:00Z |  |
