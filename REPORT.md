# Invest — Top 15 report

_Generated: **2026-05-03 14:48 UTC** · Scores as of: **2026-05-03**_

🟢 last successful crawl: 0 min ago (at 2026-05-03T14:48:26Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.571 | 1.399 | 1.399 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 2.938 | 1.150 | 1.150 | 98.7% | +4.9% | 19 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.692 | 1.053 | 1.053 | 97.4% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.191 | 0.856 | 0.856 | 96.2% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.394 | 0.543 | 0.543 | 94.9% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.070 | 0.415 | 0.415 | 93.6% | +17.1% | 23 | 8 | 0 | 12 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.047 | 0.406 | 0.406 | 92.3% | +13.6% | 59 | 5 | 0 | 32 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.820 | 0.317 | 0.317 | 91.0% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.817 | 0.316 | 0.316 | 89.7% | +7.6% | 32 | 14 | 2 | 11 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.702 | 0.271 | 0.271 | 88.5% | +25.8% | 44 | 3 | 1 | 19 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.686 | 0.264 | 0.264 | 87.2% | -1.1% | 29 | 5 | 1 | 16 | 0 |
| 12 |  | **AVGO** | Broadcom Inc. | Technology | 0.575 | 0.221 | 0.221 | 85.9% | +12.9% | 43 | 3 | 0 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.546 | 0.209 | 0.209 | 84.6% | +11.5% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.537 | 0.206 | 0.206 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.520 | 0.199 | 0.199 | 82.1% | +18.2% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.151 | 0.821 | 0.821 | 100.0% | +7.9% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.589 | 0.606 | 0.606 | 98.7% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.486 | 0.566 | 0.566 | 97.4% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.434 | 0.546 | 0.546 | 96.2% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.361 | 0.518 | 0.518 | 94.9% | +25.8% | 44 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **CLS** | Celestica Inc. | Technology | 1.299 | 0.494 | 0.494 | 93.6% | +4.9% | 19 | 1 | 0 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.180 | 0.448 | 0.448 | 92.3% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.119 | 0.425 | 0.425 | 91.0% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.026 | 0.390 | 0.390 | 89.7% | +4.4% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.017 | 0.386 | 0.386 | 88.5% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.000 | 0.379 | 0.379 | 87.2% | +46.8% | 34 | 9 | 1 | 24 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.973 | 0.369 | 0.369 | 85.9% | +11.9% | 18 | 5 | 1 | 10 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.966 | 0.366 | 0.366 | 84.6% | +13.4% | 17 | 1 | 0 | 8 | 0 |
| 14 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.869 | 0.329 | 0.329 | 83.3% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.841 | 0.318 | 0.318 | 82.1% | +16.3% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.133 | 0.957 | 0.957 | 100.0% | +60.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.114 | 0.949 | 0.949 | 98.7% | +50.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.700 | 0.762 | 0.762 | 97.4% | +42.8% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.360 | 0.608 | 0.608 | 96.2% | +51.6% | 28 | 7 | 0 | 22 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.355 | 0.606 | 0.606 | 94.9% | +46.8% | 34 | 9 | 1 | 24 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.243 | 0.555 | 0.555 | 93.6% | +32.6% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.128 | 0.503 | 0.503 | 92.3% | +42.0% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.064 | 0.475 | 0.475 | 91.0% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.061 | 0.473 | 0.473 | 89.7% | +23.6% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.059 | 0.472 | 0.472 | 88.5% | +21.1% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.039 | 0.463 | 0.463 | 87.2% | +24.4% | 27 | 3 | 1 | 7 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.018 | 0.454 | 0.454 | 85.9% | +38.6% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.016 | 0.453 | 0.453 | 84.6% | +20.0% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.009 | 0.450 | 0.450 | 83.3% | +32.4% | 30 | 7 | 0 | 27 | 0 |
| 15 |  | **FROG** | JFrog Ltd. | Technology | 0.923 | 0.411 | 0.411 | 82.1% | +34.9% | 20 | 1 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-03 14:48:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 14:48:21Z |  |
| stooq.prices | ok | 0 | 2026-05-03 13:42:50Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 13:42:45Z |  |
| stooq.prices | ok | 0 | 2026-05-03 12:00:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 12:00:28Z |  |
| stooq.prices | ok | 0 | 2026-05-03 11:10:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 11:09:57Z |  |
| stooq.prices | ok | 0 | 2026-05-03 10:03:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 10:03:41Z |  |
| stooq.prices | ok | 0 | 2026-05-03 08:46:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 08:46:18Z |  |
| stooq.prices | ok | 0 | 2026-05-03 06:43:50Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 06:43:45Z |  |
| stooq.prices | ok | 0 | 2026-05-03 04:14:31Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 04:14:25Z |  |
| edgar.13f | error | 0 | 2026-05-03 00:10:43Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-03 00:10:43Z |  |
| yfinance.actions | ok | 1140 | 2026-05-03 00:10:31Z |  |
| yfinance.consensus | ok | 79 | 2026-05-03 00:10:22Z |  |
