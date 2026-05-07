# Invest — Top 15 report

_Generated: **2026-05-07 15:40 UTC** · Scores as of: **2026-05-07**_

🟢 last successful crawl: 0 min ago (at 2026-05-07T15:40:20Z)

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.617 | 1.432 | 1.432 | 100.0% | +6.3% | 22 | 18 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.054 | 0.630 | 0.630 | 98.7% | -24.2% | 35 | 14 | 0 | 22 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.986 | 0.608 | 0.608 | 97.4% | -5.3% | 44 | 3 | 1 | 17 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.913 | 0.586 | 0.586 | 96.2% | +6.2% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.230 | 0.372 | 0.372 | 94.9% | +13.2% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 1.071 | 0.322 | 0.322 | 93.6% | +4.7% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.008 | 0.302 | 0.302 | 92.3% | -2.2% | 42 | 11 | 0 | 27 | 0 |
| 8 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.890 | 0.265 | 0.265 | 91.0% | -23.5% | 10 | 4 | 0 | 11 | 0 |
| 9 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.768 | 0.227 | 0.227 | 89.7% | +15.4% | 22 | 8 | 0 | 11 | 0 |
| 10 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.766 | 0.227 | 0.227 | 88.5% | +5.0% | 23 | 3 | 0 | 8 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.757 | 0.224 | 0.224 | 87.2% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.717 | 0.211 | 0.211 | 85.9% | +25.7% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.712 | 0.210 | 0.210 | 84.6% | +16.2% | 27 | 3 | 1 | 5 | 0 |
| 14 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.622 | 0.181 | 0.181 | 83.3% | +10.9% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.587 | 0.171 | 0.171 | 82.1% | -4.4% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.998 | 0.701 | 0.701 | 100.0% | +73.9% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.861 | 0.652 | 0.652 | 98.7% | +6.3% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.537 | 0.536 | 0.536 | 97.4% | +25.7% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.501 | 0.523 | 0.523 | 96.2% | +47.6% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.257 | 0.437 | 0.437 | 94.9% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.251 | 0.434 | 0.434 | 93.6% | +26.9% | 27 | 2 | 0 | 13 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.213 | 0.421 | 0.421 | 92.3% | +48.5% | 35 | 10 | 0 | 21 | 0 |
| 8 |  | **CVX** | Chevron Corporation | Energy | 1.190 | 0.413 | 0.413 | 91.0% | +18.8% | 18 | 6 | 1 | 11 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.070 | 0.370 | 0.370 | 89.7% | +43.0% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.927 | 0.319 | 0.319 | 88.5% | -2.2% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.926 | 0.319 | 0.319 | 87.2% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.906 | 0.312 | 0.312 | 85.9% | +13.2% | 61 | 5 | 0 | 32 | 0 |
| 13 | ★★ | **CI** | The Cigna Group | Healthcare | 0.883 | 0.303 | 0.303 | 84.6% | +20.5% | 22 | 2 | 0 | 10 | 0 |
| 14 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.877 | 0.301 | 0.301 | 83.3% | -5.3% | 44 | 3 | 1 | 17 | 0 |
| 15 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.844 | 0.290 | 0.290 | 82.1% | +35.7% | 21 | 7 | 0 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.495 | 1.117 | 1.117 | 100.0% | +73.9% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.930 | 0.862 | 0.862 | 98.7% | +47.6% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.682 | 0.750 | 0.750 | 97.4% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.379 | 0.612 | 0.612 | 96.2% | +48.5% | 35 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.328 | 0.589 | 0.589 | 94.9% | +35.7% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.238 | 0.549 | 0.549 | 93.6% | +25.7% | 21 | 2 | 0 | 3 | 0 |
| 7 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.159 | 0.513 | 0.513 | 92.3% | +23.3% | 9 | 1 | 0 | 0 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.159 | 0.513 | 0.513 | 91.0% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.155 | 0.511 | 0.511 | 89.7% | +43.0% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.086 | 0.480 | 0.480 | 88.5% | +20.5% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.080 | 0.477 | 0.477 | 87.2% | +26.9% | 27 | 2 | 0 | 13 | 0 |
| 12 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.994 | 0.438 | 0.438 | 85.9% | +24.5% | 24 | 8 | 0 | 9 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.980 | 0.432 | 0.432 | 84.6% | +38.8% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BAC** | Bank of America Corporation | Financial Services | 0.938 | 0.413 | 0.413 | 83.3% | +17.9% | 22 | 3 | 0 | 9 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.937 | 0.413 | 0.413 | 82.1% | +29.5% | 30 | 7 | 0 | 25 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-06 23:51:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 23:51:43Z |  |
