# Invest — Top 15 report

_Generated: **2026-05-02 19:30 UTC** · Scores as of: **2026-05-02**_

🟢 last successful crawl: 0 min ago (at 2026-05-02T19:30:29Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.648 | 1.418 | 1.418 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 2.785 | 1.081 | 1.081 | 98.7% | +4.9% | 19 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.538 | 0.985 | 0.985 | 97.4% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.213 | 0.858 | 0.858 | 96.2% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.410 | 0.545 | 0.545 | 94.9% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.083 | 0.417 | 0.417 | 93.6% | +17.1% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.060 | 0.408 | 0.408 | 92.3% | +13.6% | 59 | 5 | 0 | 32 | 0 |
| 8 |  | **AAPL** | Apple Inc. | Technology | 0.838 | 0.322 | 0.322 | 91.0% | +7.6% | 32 | 14 | 2 | 11 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.834 | 0.320 | 0.320 | 89.7% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.715 | 0.274 | 0.274 | 88.5% | +25.8% | 44 | 3 | 1 | 19 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.696 | 0.266 | 0.266 | 87.2% | -1.1% | 29 | 5 | 1 | 16 | 0 |
| 12 |  | **AVGO** | Broadcom Inc. | Technology | 0.575 | 0.219 | 0.219 | 85.9% | +12.9% | 43 | 3 | 0 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.555 | 0.211 | 0.211 | 84.6% | +11.5% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.546 | 0.208 | 0.208 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.529 | 0.201 | 0.201 | 82.1% | +18.2% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.153 | 0.820 | 0.820 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.595 | 0.607 | 0.607 | 98.7% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.491 | 0.567 | 0.567 | 97.4% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.443 | 0.549 | 0.549 | 96.2% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.371 | 0.521 | 0.521 | 94.9% | +25.8% | 44 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **CLS** | Celestica Inc. | Technology | 1.201 | 0.456 | 0.456 | 93.6% | +4.9% | 19 | 1 | 0 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.184 | 0.449 | 0.449 | 92.3% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.124 | 0.426 | 0.426 | 91.0% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.030 | 0.390 | 0.390 | 89.7% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.004 | 0.380 | 0.380 | 88.5% | +46.8% | 34 | 9 | 1 | 24 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.992 | 0.376 | 0.376 | 87.2% | +11.9% | 18 | 5 | 1 | 10 | 0 |
| 12 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.970 | 0.367 | 0.367 | 85.9% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 13 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 0.919 | 0.347 | 0.347 | 84.6% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 14 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.873 | 0.330 | 0.330 | 83.3% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.845 | 0.319 | 0.319 | 82.1% | +16.3% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.133 | 0.957 | 0.957 | 100.0% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.114 | 0.949 | 0.949 | 98.7% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.700 | 0.762 | 0.762 | 97.4% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.364 | 0.610 | 0.610 | 96.2% | +51.6% | 28 | 7 | 0 | 22 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.355 | 0.606 | 0.606 | 94.9% | +46.8% | 34 | 9 | 1 | 24 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.243 | 0.555 | 0.555 | 93.6% | +32.6% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.128 | 0.503 | 0.503 | 92.3% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.064 | 0.475 | 0.475 | 91.0% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.062 | 0.474 | 0.474 | 89.7% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.060 | 0.473 | 0.473 | 88.5% | +21.2% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.039 | 0.463 | 0.463 | 87.2% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.018 | 0.454 | 0.454 | 85.9% | +38.6% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.016 | 0.453 | 0.453 | 84.6% | +20.0% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.009 | 0.450 | 0.450 | 83.3% | +32.4% | 30 | 7 | 0 | 27 | 0 |
| 15 |  | **FROG** | JFrog Ltd. | Technology | 0.923 | 0.411 | 0.411 | 82.1% | +34.9% | 20 | 1 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-02 19:30:28Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 19:30:23Z |  |
| stooq.prices | ok | 0 | 2026-05-02 18:05:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 18:04:59Z |  |
| stooq.prices | ok | 0 | 2026-05-02 17:09:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 17:09:45Z |  |
| stooq.prices | ok | 0 | 2026-05-02 16:03:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 16:03:23Z |  |
| stooq.prices | ok | 0 | 2026-05-02 15:08:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 15:08:18Z |  |
| stooq.prices | ok | 0 | 2026-05-02 14:16:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 14:16:14Z |  |
| stooq.prices | ok | 0 | 2026-05-02 13:09:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 13:09:15Z |  |
| stooq.prices | ok | 0 | 2026-05-02 11:47:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 11:47:29Z |  |
| stooq.prices | ok | 0 | 2026-05-02 10:56:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 10:56:49Z |  |
| stooq.prices | ok | 0 | 2026-05-02 09:57:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-02 09:57:52Z |  |
