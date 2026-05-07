# Invest — Top 15 report

_Generated: **2026-05-07 17:25 UTC** · Scores as of: **2026-05-07**_

🟢 last successful crawl: 0 min ago (at 2026-05-07T17:25:54Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **ABT**, **AMZN**, **ANET**, **APH**, **BSX**, **CHWY**, **CI**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.564 | 1.438 | 1.438 | 100.0% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.082 | 0.649 | 0.649 | 98.7% | -22.6% | 35 | 14 | 0 | 22 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.024 | 0.630 | 0.630 | 97.4% | -1.9% | 44 | 3 | 1 | 17 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.808 | 0.562 | 0.562 | 96.2% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.262 | 0.388 | 0.388 | 94.9% | +13.8% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 1.093 | 0.334 | 0.334 | 93.6% | +4.9% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.014 | 0.309 | 0.309 | 92.3% | -1.0% | 42 | 11 | 0 | 27 | 0 |
| 8 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.853 | 0.258 | 0.258 | 91.0% | -21.1% | 10 | 4 | 0 | 11 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.816 | 0.246 | 0.246 | 89.7% | +4.1% | 14 | 8 | 0 | 9 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.786 | 0.237 | 0.237 | 88.5% | +17.6% | 22 | 8 | 0 | 11 | 0 |
| 11 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.770 | 0.232 | 0.232 | 87.2% | +6.5% | 23 | 3 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.721 | 0.216 | 0.216 | 85.9% | +25.6% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.693 | 0.207 | 0.207 | 84.6% | +18.0% | 27 | 3 | 1 | 5 | 0 |
| 14 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.640 | 0.190 | 0.190 | 83.3% | +11.1% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.597 | 0.177 | 0.177 | 82.1% | -3.6% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.970 | 0.691 | 0.691 | 100.0% | +73.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.848 | 0.648 | 0.648 | 98.7% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.524 | 0.532 | 0.532 | 97.4% | +49.6% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.513 | 0.528 | 0.528 | 96.2% | +25.6% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.266 | 0.440 | 0.440 | 94.9% | +29.0% | 27 | 2 | 0 | 13 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.228 | 0.427 | 0.427 | 93.6% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.153 | 0.400 | 0.400 | 92.3% | +46.4% | 35 | 10 | 0 | 21 | 0 |
| 8 |  | **CVX** | Chevron Corporation | Energy | 1.142 | 0.396 | 0.396 | 91.0% | +17.6% | 18 | 6 | 1 | 11 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.096 | 0.380 | 0.380 | 89.7% | +44.6% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.998 | 0.345 | 0.345 | 88.5% | -1.9% | 44 | 3 | 1 | 17 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.944 | 0.326 | 0.326 | 87.2% | -1.0% | 42 | 11 | 0 | 27 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 0.917 | 0.316 | 0.316 | 85.9% | +33.6% | 15 | 3 | 0 | 7 | 0 |
| 13 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.912 | 0.314 | 0.314 | 84.6% | +13.8% | 61 | 5 | 0 | 32 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.846 | 0.290 | 0.290 | 83.3% | +19.6% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.810 | 0.278 | 0.278 | 82.1% | +35.7% | 21 | 7 | 0 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.485 | 1.106 | 1.106 | 100.0% | +73.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.990 | 0.883 | 0.883 | 98.7% | +49.6% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.669 | 0.739 | 0.739 | 97.4% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.313 | 0.579 | 0.579 | 96.2% | +35.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.281 | 0.564 | 0.564 | 94.9% | +46.4% | 35 | 10 | 0 | 21 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.211 | 0.533 | 0.533 | 93.6% | +25.6% | 21 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.194 | 0.525 | 0.525 | 92.3% | +44.6% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.155 | 0.508 | 0.508 | 91.0% | +33.6% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.133 | 0.498 | 0.498 | 89.7% | +23.1% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.128 | 0.496 | 0.496 | 88.5% | +29.0% | 27 | 2 | 0 | 13 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.028 | 0.451 | 0.451 | 87.2% | +19.6% | 22 | 2 | 0 | 10 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 0.981 | 0.429 | 0.429 | 85.9% | +39.4% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.959 | 0.420 | 0.420 | 84.6% | +24.2% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.955 | 0.418 | 0.418 | 83.3% | +30.6% | 30 | 7 | 0 | 25 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.943 | 0.412 | 0.412 | 82.1% | +18.8% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-05-07 01:17:26Z |  |
| yfinance.prices | ok | 7110 | 2026-05-07 01:17:20Z |  |
