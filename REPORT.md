# Invest — Top 15 report

_Generated: **2026-05-05 00:11 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T00:11:41Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.306 | 1.675 | 1.675 | 100.0% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.066 | 1.581 | 1.581 | 98.7% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.794 | 0.690 | 0.690 | 97.4% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 4 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.433 | 0.549 | 0.549 | 96.2% | -10.0% | 36 | 13 | 0 | 15 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.353 | 0.518 | 0.518 | 94.9% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.173 | 0.447 | 0.447 | 93.6% | +13.1% | 59 | 5 | 0 | 32 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.010 | 0.383 | 0.383 | 92.3% | +17.9% | 23 | 8 | 0 | 11 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.808 | 0.304 | 0.304 | 91.0% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 9 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.804 | 0.303 | 0.303 | 89.7% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.725 | 0.272 | 0.272 | 88.5% | +8.6% | 32 | 15 | 2 | 11 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.722 | 0.271 | 0.271 | 87.2% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.716 | 0.268 | 0.268 | 85.9% | -1.0% | 28 | 5 | 1 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.658 | 0.246 | 0.246 | 84.6% | +8.6% | 23 | 3 | 0 | 8 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.543 | 0.200 | 0.200 | 83.3% | +14.2% | 43 | 3 | 0 | 16 | 0 |
| 15 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.416 | 0.151 | 0.151 | 82.1% | +6.7% | 21 | 19 | 2 | 14 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.880 | 0.708 | 0.708 | 100.0% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.706 | 0.642 | 0.642 | 98.7% | +67.1% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.618 | 0.608 | 0.608 | 97.4% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.572 | 0.591 | 0.591 | 96.2% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.429 | 0.536 | 0.536 | 94.9% | +49.8% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.260 | 0.472 | 0.472 | 93.6% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.176 | 0.440 | 0.440 | 92.3% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.118 | 0.418 | 0.418 | 91.0% | +44.7% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.012 | 0.377 | 0.377 | 89.7% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.979 | 0.365 | 0.365 | 88.5% | +45.4% | 34 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.963 | 0.359 | 0.359 | 87.2% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.900 | 0.335 | 0.335 | 85.9% | +26.6% | 27 | 3 | 1 | 5 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.876 | 0.326 | 0.326 | 84.6% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.870 | 0.324 | 0.324 | 83.3% | +11.0% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.860 | 0.320 | 0.320 | 82.1% | +18.9% | 10 | 1 | 0 | 2 | 0 |


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
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.106 | 0.498 | 0.498 | 87.2% | +26.6% | 27 | 3 | 1 | 5 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.085 | 0.488 | 0.488 | 85.9% | +22.0% | 9 | 1 | 0 | 0 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.081 | 0.487 | 0.487 | 84.6% | +21.6% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.010 | 0.454 | 0.454 | 83.3% | +38.3% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.970 | 0.436 | 0.436 | 82.1% | +20.6% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-05 00:11:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 00:11:33Z |  |
| stooq.prices | ok | 0 | 2026-05-04 23:14:01Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 23:13:56Z |  |
| stooq.prices | ok | 0 | 2026-05-04 22:17:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 22:17:02Z |  |
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
