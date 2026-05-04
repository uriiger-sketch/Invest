# Invest — Top 15 report

_Generated: **2026-05-04 21:13 UTC** · Scores as of: **2026-05-04**_

🟢 last successful crawl: 0 min ago (at 2026-05-04T21:13:44Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **BAC**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.594 | 1.445 | 1.445 | 100.0% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 3.013 | 1.211 | 1.211 | 98.7% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.780 | 1.117 | 1.117 | 97.4% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.808 | 0.724 | 0.724 | 96.2% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.380 | 0.552 | 0.552 | 94.9% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.205 | 0.481 | 0.481 | 93.6% | +13.1% | 59 | 5 | 0 | 32 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.047 | 0.417 | 0.417 | 92.3% | +17.9% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.851 | 0.338 | 0.338 | 91.0% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.770 | 0.306 | 0.306 | 89.7% | +8.6% | 32 | 15 | 2 | 11 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.768 | 0.304 | 0.304 | 88.5% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.762 | 0.302 | 0.302 | 87.2% | -1.0% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.706 | 0.279 | 0.279 | 85.9% | +8.6% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AVGO** | Broadcom Inc. | Technology | 0.594 | 0.234 | 0.234 | 84.6% | +14.2% | 43 | 3 | 0 | 16 | 0 |
| 14 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.470 | 0.184 | 0.184 | 83.3% | +6.7% | 21 | 19 | 2 | 14 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.466 | 0.183 | 0.183 | 82.1% | +20.6% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.102 | 0.816 | 0.816 | 100.0% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.690 | 0.655 | 0.655 | 98.7% | +67.1% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.559 | 0.604 | 0.604 | 97.4% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.420 | 0.550 | 0.550 | 96.2% | +49.8% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★ | **CLS** | Celestica Inc. | Technology | 1.350 | 0.522 | 0.522 | 94.9% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.256 | 0.486 | 0.486 | 93.6% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.174 | 0.454 | 0.454 | 92.3% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.117 | 0.431 | 0.431 | 91.0% | +44.7% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.093 | 0.422 | 0.422 | 89.7% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.013 | 0.391 | 0.391 | 88.5% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.982 | 0.379 | 0.379 | 87.2% | +45.4% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.905 | 0.349 | 0.349 | 85.9% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.881 | 0.339 | 0.339 | 84.6% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.875 | 0.337 | 0.337 | 83.3% | +11.0% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.866 | 0.334 | 0.334 | 82.1% | +18.9% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.352 | 1.065 | 1.065 | 100.0% | +67.1% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.067 | 0.935 | 0.935 | 98.7% | +49.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.717 | 0.776 | 0.776 | 97.4% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.342 | 0.605 | 0.605 | 96.2% | +35.5% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.326 | 0.598 | 0.598 | 94.9% | +45.4% | 34 | 8 | 1 | 24 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.269 | 0.572 | 0.572 | 93.6% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.249 | 0.563 | 0.563 | 92.3% | +44.7% | 35 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.231 | 0.555 | 0.555 | 91.0% | +47.9% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.148 | 0.517 | 0.517 | 89.7% | +18.9% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.119 | 0.504 | 0.504 | 88.5% | +35.7% | 30 | 7 | 0 | 27 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.106 | 0.498 | 0.498 | 87.2% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.085 | 0.488 | 0.488 | 85.9% | +22.0% | 9 | 1 | 0 | 0 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.081 | 0.487 | 0.487 | 84.6% | +21.6% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.010 | 0.454 | 0.454 | 83.3% | +38.3% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.970 | 0.436 | 0.436 | 82.1% | +20.6% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-04 21:13:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 21:13:33Z |  |
| stooq.prices | ok | 0 | 2026-05-04 19:58:18Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 19:58:12Z |  |
| stooq.prices | ok | 0 | 2026-05-04 18:05:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 18:04:59Z |  |
| stooq.prices | ok | 0 | 2026-05-04 16:21:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 16:21:37Z |  |
| stooq.prices | ok | 0 | 2026-05-04 14:34:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 14:34:16Z |  |
| stooq.prices | ok | 0 | 2026-05-04 12:07:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 12:07:23Z |  |
| stooq.prices | ok | 0 | 2026-05-04 10:13:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 10:13:35Z |  |
| stooq.prices | ok | 0 | 2026-05-04 07:47:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 07:47:19Z |  |
| stooq.prices | ok | 0 | 2026-05-04 04:52:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 04:52:38Z |  |
| stooq.prices | ok | 0 | 2026-05-04 01:19:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 01:19:18Z |  |
