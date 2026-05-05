# Invest — Top 15 report

_Generated: **2026-05-05 06:15 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T06:15:20Z)

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.329 | 1.682 | 1.682 | 100.0% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.088 | 1.588 | 1.588 | 98.7% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.796 | 0.691 | 0.691 | 97.4% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.353 | 0.518 | 0.518 | 96.2% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.174 | 0.448 | 0.448 | 94.9% | +13.1% | 59 | 5 | 0 | 32 | 0 |
| 6 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.117 | 0.425 | 0.425 | 93.6% | +6.7% | 21 | 19 | 2 | 15 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.011 | 0.384 | 0.384 | 92.3% | +17.9% | 23 | 8 | 0 | 11 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.818 | 0.308 | 0.308 | 91.0% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.806 | 0.303 | 0.303 | 89.7% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 10 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.728 | 0.273 | 0.273 | 88.5% | -10.0% | 36 | 13 | 0 | 16 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.720 | 0.270 | 0.270 | 87.2% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 12 |  | **AAPL** | Apple Inc. | Technology | 0.717 | 0.269 | 0.269 | 85.9% | +8.6% | 32 | 15 | 2 | 11 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.717 | 0.269 | 0.269 | 84.6% | -1.0% | 28 | 5 | 1 | 16 | 0 |
| 14 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.659 | 0.246 | 0.246 | 83.3% | +8.6% | 23 | 3 | 0 | 8 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.551 | 0.204 | 0.204 | 82.1% | +14.2% | 43 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.903 | 0.719 | 0.719 | 100.0% | +4.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.701 | 0.642 | 0.642 | 98.7% | +67.1% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.641 | 0.619 | 0.619 | 97.4% | +4.6% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.562 | 0.589 | 0.589 | 96.2% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.424 | 0.536 | 0.536 | 94.9% | +49.8% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.251 | 0.470 | 0.470 | 93.6% | +20.5% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.173 | 0.440 | 0.440 | 92.3% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.114 | 0.418 | 0.418 | 91.0% | +44.7% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.007 | 0.377 | 0.377 | 89.7% | +4.5% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.979 | 0.367 | 0.367 | 88.5% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.976 | 0.365 | 0.365 | 87.2% | +45.4% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.897 | 0.335 | 0.335 | 85.9% | +26.6% | 27 | 3 | 1 | 5 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.873 | 0.326 | 0.326 | 84.6% | +16.1% | 17 | 1 | 0 | 8 | 0 |
| 14 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.858 | 0.320 | 0.320 | 83.3% | +18.9% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.854 | 0.319 | 0.319 | 82.1% | +11.0% | 18 | 6 | 1 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.352 | 1.066 | 1.066 | 100.0% | +67.1% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.067 | 0.935 | 0.935 | 98.7% | +49.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.718 | 0.776 | 0.776 | 97.4% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.342 | 0.605 | 0.605 | 96.2% | +35.5% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.326 | 0.598 | 0.598 | 94.9% | +45.4% | 34 | 8 | 1 | 24 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.268 | 0.572 | 0.572 | 93.6% | +28.3% | 20 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.249 | 0.563 | 0.563 | 92.3% | +44.7% | 35 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.229 | 0.554 | 0.554 | 91.0% | +47.9% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.149 | 0.517 | 0.517 | 89.7% | +18.9% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.119 | 0.504 | 0.504 | 88.5% | +35.7% | 30 | 7 | 0 | 27 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.106 | 0.498 | 0.498 | 87.2% | +26.6% | 27 | 3 | 1 | 5 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.085 | 0.488 | 0.488 | 85.9% | +22.0% | 9 | 1 | 0 | 0 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.081 | 0.487 | 0.487 | 84.6% | +21.6% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.010 | 0.454 | 0.454 | 83.3% | +38.3% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.970 | 0.436 | 0.436 | 82.1% | +20.6% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-05 06:15:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 06:15:15Z |  |
| stooq.prices | ok | 0 | 2026-05-05 03:53:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 03:53:24Z |  |
| edgar.13f | error | 0 | 2026-05-05 01:13:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-05 01:13:32Z |  |
| yfinance.actions | ok | 1126 | 2026-05-05 01:13:19Z |  |
| yfinance.consensus | ok | 79 | 2026-05-05 01:13:10Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-05 01:12:57Z |  |
| yfinance.prices | ok | 7110 | 2026-05-05 01:12:52Z |  |
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
