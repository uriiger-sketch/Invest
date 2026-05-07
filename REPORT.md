# Invest — Top 15 report

_Generated: **2026-05-07 06:10 UTC** · Scores as of: **2026-05-07**_

🟢 last successful crawl: 0 min ago (at 2026-05-07T06:10:22Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **ABT**, **AMZN**, **APH**, **BSX**, **CHWY**, **CI**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.681 | 1.468 | 1.468 | 100.0% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.182 | 0.677 | 0.677 | 98.7% | -25.9% | 35 | 14 | 0 | 22 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.783 | 0.551 | 0.551 | 97.4% | +5.4% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.260 | 0.386 | 0.386 | 96.2% | +12.6% | 61 | 5 | 0 | 32 | 0 |
| 5 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.107 | 0.337 | 0.337 | 94.9% | -27.2% | 10 | 4 | 0 | 11 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 1.028 | 0.312 | 0.312 | 93.6% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.958 | 0.290 | 0.290 | 92.3% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.918 | 0.277 | 0.277 | 91.0% | +23.2% | 44 | 3 | 1 | 17 | 0 |
| 9 |  | **CLS** | Celestica Inc. | Technology | 0.859 | 0.259 | 0.259 | 89.7% | +7.0% | 20 | 1 | 0 | 11 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.763 | 0.228 | 0.228 | 88.5% | -5.5% | 28 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.746 | 0.223 | 0.223 | 87.2% | +3.8% | 14 | 8 | 0 | 9 | 0 |
| 12 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.736 | 0.220 | 0.220 | 85.9% | +9.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.706 | 0.210 | 0.210 | 84.6% | +6.9% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.705 | 0.210 | 0.210 | 83.3% | +5.1% | 42 | 11 | 0 | 27 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.679 | 0.202 | 0.202 | 82.1% | +18.7% | 27 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.893 | 0.671 | 0.671 | 100.0% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.709 | 0.604 | 0.604 | 98.7% | +66.9% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.532 | 0.541 | 0.541 | 97.4% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.526 | 0.539 | 0.539 | 96.2% | +52.1% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.376 | 0.485 | 0.485 | 94.9% | +23.2% | 44 | 3 | 1 | 17 | 0 |
| 6 |  | **ANET** | Arista Networks, Inc. | Technology | 1.234 | 0.434 | 0.434 | 93.6% | +23.7% | 27 | 2 | 0 | 13 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.196 | 0.420 | 0.420 | 92.3% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.133 | 0.397 | 0.397 | 91.0% | +47.9% | 35 | 10 | 0 | 21 | 0 |
| 9 |  | **CVX** | Chevron Corporation | Energy | 1.045 | 0.365 | 0.365 | 89.7% | +16.0% | 18 | 6 | 1 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.039 | 0.363 | 0.363 | 88.5% | +5.1% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.036 | 0.362 | 0.362 | 87.2% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.888 | 0.309 | 0.309 | 85.9% | +12.6% | 61 | 5 | 0 | 32 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.887 | 0.309 | 0.309 | 84.6% | +31.2% | 15 | 3 | 0 | 7 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.849 | 0.295 | 0.295 | 83.3% | +20.8% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.845 | 0.294 | 0.294 | 82.1% | +37.5% | 21 | 7 | 0 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.124 | 0.964 | 0.964 | 100.0% | +66.9% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.989 | 0.902 | 0.902 | 98.7% | +52.1% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.576 | 0.712 | 0.712 | 97.4% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.317 | 0.594 | 0.594 | 96.2% | +37.5% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.285 | 0.579 | 0.579 | 94.9% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.263 | 0.569 | 0.569 | 93.6% | +47.9% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.096 | 0.492 | 0.492 | 92.3% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **CI** | The Cigna Group | Healthcare | 1.060 | 0.476 | 0.476 | 91.0% | +20.8% | 22 | 2 | 0 | 10 | 0 |
| 9 |  | **ACN** | Accenture plc | Technology | 1.059 | 0.475 | 0.475 | 89.7% | +42.7% | 18 | 10 | 0 | 12 | 0 |
| 10 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.038 | 0.466 | 0.466 | 88.5% | +45.7% | 28 | 7 | 0 | 22 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.035 | 0.464 | 0.464 | 87.2% | +21.0% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 1.020 | 0.457 | 0.457 | 85.9% | +31.2% | 15 | 3 | 0 | 7 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.002 | 0.449 | 0.449 | 84.6% | +33.3% | 30 | 7 | 0 | 25 | 0 |
| 14 |  | **BILL** | BILL Holdings, Inc. | Technology | 0.941 | 0.421 | 0.421 | 83.3% | +45.3% | 14 | 9 | 0 | 8 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.904 | 0.404 | 0.404 | 82.1% | +23.1% | 24 | 8 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-06 22:54:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 22:54:45Z |  |
| stooq.prices | ok | 0 | 2026-05-06 21:56:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 21:56:35Z |  |
| stooq.prices | ok | 0 | 2026-05-06 20:49:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 20:49:48Z |  |
| stooq.prices | ok | 0 | 2026-05-06 19:03:21Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 19:03:13Z |  |
