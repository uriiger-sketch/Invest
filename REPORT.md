# Invest — Top 15 report

_Generated: **2026-05-05 15:53 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T15:53:23Z)

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.355 | 1.645 | 1.645 | 100.0% | +3.6% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.072 | 1.538 | 1.538 | 98.7% | +5.3% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.848 | 0.694 | 0.694 | 97.4% | +7.7% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.296 | 0.484 | 0.484 | 96.2% | +3.9% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.121 | 0.418 | 0.418 | 94.9% | +11.4% | 59 | 5 | 0 | 32 | 0 |
| 6 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.079 | 0.402 | 0.402 | 93.6% | +6.1% | 21 | 19 | 2 | 15 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.887 | 0.329 | 0.329 | 92.3% | +20.1% | 44 | 3 | 1 | 18 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.850 | 0.315 | 0.315 | 91.0% | +2.9% | 42 | 11 | 0 | 27 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.736 | 0.271 | 0.271 | 89.7% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.715 | 0.263 | 0.263 | 88.5% | +7.3% | 32 | 15 | 2 | 11 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.650 | 0.239 | 0.239 | 87.2% | -13.6% | 36 | 13 | 0 | 16 | 0 |
| 12 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.630 | 0.231 | 0.231 | 85.9% | -31.9% | 10 | 4 | 0 | 10 | 0 |
| 13 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.624 | 0.229 | 0.229 | 84.6% | +17.4% | 23 | 8 | 0 | 11 | 0 |
| 14 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.592 | 0.217 | 0.217 | 83.3% | +8.1% | 23 | 3 | 0 | 8 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.565 | 0.207 | 0.207 | 82.1% | -2.2% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.937 | 0.708 | 0.708 | 100.0% | +3.6% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.706 | 0.622 | 0.622 | 98.7% | +5.3% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.648 | 0.601 | 0.601 | 97.4% | +66.7% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.516 | 0.552 | 0.552 | 96.2% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.440 | 0.524 | 0.524 | 94.9% | +51.3% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.306 | 0.474 | 0.474 | 93.6% | +20.1% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.174 | 0.426 | 0.426 | 92.3% | +50.4% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.126 | 0.408 | 0.408 | 91.0% | +42.3% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.041 | 0.376 | 0.376 | 89.7% | +3.9% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.015 | 0.367 | 0.367 | 88.5% | +2.9% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.959 | 0.346 | 0.346 | 87.2% | +45.8% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.946 | 0.341 | 0.341 | 85.9% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.931 | 0.336 | 0.336 | 84.6% | +11.0% | 18 | 6 | 1 | 11 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.850 | 0.306 | 0.306 | 83.3% | +23.5% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.832 | 0.299 | 0.299 | 82.1% | +30.5% | 15 | 3 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.212 | 0.981 | 0.981 | 100.0% | +66.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.041 | 0.905 | 0.905 | 98.7% | +51.3% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.612 | 0.712 | 0.712 | 97.4% | +42.3% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.383 | 0.609 | 0.609 | 96.2% | +50.4% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.310 | 0.577 | 0.577 | 94.9% | +35.8% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.265 | 0.556 | 0.556 | 93.6% | +45.8% | 34 | 8 | 1 | 24 | 0 |
| 7 | ★★ | **CI** | The Cigna Group | Healthcare | 1.182 | 0.519 | 0.519 | 92.3% | +23.5% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.180 | 0.519 | 0.519 | 91.0% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.154 | 0.507 | 0.507 | 89.7% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.152 | 0.506 | 0.506 | 88.5% | +23.6% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.080 | 0.474 | 0.474 | 87.2% | +45.9% | 28 | 7 | 0 | 22 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.063 | 0.466 | 0.466 | 85.9% | +41.5% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.055 | 0.463 | 0.463 | 84.6% | +34.2% | 30 | 7 | 0 | 27 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.993 | 0.435 | 0.435 | 83.3% | +30.5% | 15 | 3 | 0 | 7 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.919 | 0.401 | 0.401 | 82.1% | +18.3% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-05 03:53:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 03:53:24Z |  |
| edgar.13f | error | 0 | 2026-05-05 01:13:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-05 01:13:32Z |  |
| yfinance.actions | ok | 1126 | 2026-05-05 01:13:19Z |  |
| yfinance.consensus | ok | 79 | 2026-05-05 01:13:10Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-05 01:12:57Z |  |
| yfinance.prices | ok | 7110 | 2026-05-05 01:12:52Z |  |
