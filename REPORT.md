# Invest — Top 15 report

_Generated: **2026-05-07 19:18 UTC** · Scores as of: **2026-05-07**_

🟢 last successful crawl: 0 min ago (at 2026-05-07T19:18:14Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **AMZN**, **ANET**, **APH**, **BSX**, **CHWY**, **CI**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.577 | 1.438 | 1.438 | 100.0% | +6.7% | 22 | 18 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.106 | 0.654 | 0.654 | 98.7% | -23.1% | 35 | 14 | 0 | 22 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.097 | 0.652 | 0.652 | 97.4% | -4.8% | 44 | 3 | 1 | 17 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.755 | 0.543 | 0.543 | 96.2% | +11.5% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.252 | 0.384 | 0.384 | 94.9% | +13.9% | 61 | 5 | 0 | 32 | 0 |
| 6 | ★★ | **AAPL** | Apple Inc. | Technology | 1.058 | 0.322 | 0.322 | 93.6% | +5.9% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.041 | 0.317 | 0.317 | 92.3% | -1.8% | 42 | 11 | 0 | 27 | 0 |
| 8 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.842 | 0.254 | 0.254 | 91.0% | -21.1% | 10 | 4 | 0 | 11 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.819 | 0.247 | 0.247 | 89.7% | +4.0% | 14 | 8 | 0 | 9 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.786 | 0.236 | 0.236 | 88.5% | +17.4% | 22 | 8 | 0 | 11 | 0 |
| 11 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.771 | 0.231 | 0.231 | 87.2% | +6.4% | 23 | 3 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.711 | 0.212 | 0.212 | 85.9% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.680 | 0.202 | 0.202 | 84.6% | +18.5% | 27 | 3 | 1 | 5 | 0 |
| 14 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.637 | 0.189 | 0.189 | 83.3% | +11.2% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **CVX** | Chevron Corporation | Energy | 0.601 | 0.177 | 0.177 | 82.1% | +17.4% | 18 | 6 | 1 | 11 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.006 | 0.703 | 0.703 | 100.0% | +75.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.852 | 0.649 | 0.649 | 98.7% | +6.7% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.528 | 0.533 | 0.533 | 97.4% | +49.7% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.526 | 0.532 | 0.532 | 96.2% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.277 | 0.444 | 0.444 | 94.9% | +29.4% | 27 | 2 | 0 | 13 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.220 | 0.424 | 0.424 | 93.6% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.140 | 0.395 | 0.395 | 92.3% | +17.4% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.125 | 0.390 | 0.390 | 91.0% | +45.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.082 | 0.374 | 0.374 | 89.7% | +44.1% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **APH** | Amphenol Corporation | Technology | 0.934 | 0.322 | 0.322 | 88.5% | +34.5% | 15 | 3 | 0 | 7 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.930 | 0.320 | 0.320 | 87.2% | -1.8% | 42 | 11 | 0 | 27 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.917 | 0.316 | 0.316 | 85.9% | -4.8% | 44 | 3 | 1 | 17 | 0 |
| 13 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.912 | 0.314 | 0.314 | 84.6% | +13.9% | 61 | 5 | 0 | 32 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.849 | 0.291 | 0.291 | 83.3% | +19.8% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.813 | 0.278 | 0.278 | 82.1% | +5.9% | 31 | 15 | 2 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.528 | 1.127 | 1.127 | 100.0% | +75.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.987 | 0.883 | 0.883 | 98.7% | +49.7% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.648 | 0.731 | 0.731 | 97.4% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.304 | 0.576 | 0.576 | 96.2% | +35.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.231 | 0.543 | 0.543 | 94.9% | +45.2% | 35 | 10 | 0 | 21 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.228 | 0.542 | 0.542 | 93.6% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **APH** | Amphenol Corporation | Technology | 1.182 | 0.521 | 0.521 | 92.3% | +34.5% | 15 | 3 | 0 | 7 | 0 |
| 8 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.169 | 0.515 | 0.515 | 91.0% | +44.1% | 33 | 8 | 1 | 24 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.140 | 0.502 | 0.502 | 89.7% | +29.4% | 27 | 2 | 0 | 13 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.109 | 0.488 | 0.488 | 88.5% | +22.5% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.031 | 0.453 | 0.453 | 87.2% | +19.8% | 22 | 2 | 0 | 10 | 0 |
| 12 |  | **BAC** | Bank of America Corporation | Financial Services | 0.968 | 0.425 | 0.425 | 85.9% | +19.6% | 22 | 3 | 0 | 9 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.959 | 0.421 | 0.421 | 84.6% | +24.3% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.945 | 0.414 | 0.414 | 83.3% | +30.4% | 30 | 7 | 0 | 25 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.945 | 0.414 | 0.414 | 82.1% | +38.6% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.actions | ok | 1123 | 2026-05-07 01:17:49Z |  |
| yfinance.consensus | ok | 79 | 2026-05-07 01:17:40Z |  |
