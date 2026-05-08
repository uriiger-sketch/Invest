# Invest — Top 15 report

_Generated: **2026-05-08 14:19 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T14:19:52Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.700 | 1.725 | 1.725 | 100.0% | -0.6% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.078 | 1.495 | 1.495 | 98.7% | +3.6% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.998 | 0.728 | 0.728 | 97.4% | -8.0% | 44 | 3 | 1 | 16 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.273 | 0.460 | 0.460 | 96.2% | +10.8% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.187 | 0.428 | 0.428 | 94.9% | -3.3% | 42 | 11 | 0 | 27 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.106 | 0.399 | 0.399 | 93.6% | +11.1% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.876 | 0.314 | 0.314 | 92.3% | +3.5% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.698 | 0.248 | 0.248 | 91.0% | +14.0% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.628 | 0.222 | 0.222 | 89.7% | +5.2% | 23 | 3 | 0 | 8 | 0 |
| 10 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.595 | 0.210 | 0.210 | 88.5% | +4.3% | 14 | 8 | 0 | 9 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.549 | 0.193 | 0.193 | 87.2% | +25.8% | 21 | 2 | 0 | 3 | 0 |
| 12 | ★★ | **CVX** | Chevron Corporation | Energy | 0.546 | 0.192 | 0.192 | 85.9% | +18.3% | 18 | 6 | 1 | 11 | 0 |
| 13 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.506 | 0.177 | 0.177 | 84.6% | +18.1% | 22 | 8 | 0 | 6 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.440 | 0.153 | 0.153 | 83.3% | +19.5% | 27 | 3 | 1 | 6 | 0 |
| 15 |  | **FROG** | JFrog Ltd. | Technology | 0.410 | 0.142 | 0.142 | 82.1% | +1.4% | 20 | 1 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.015 | 0.720 | 0.720 | 100.0% | +79.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.869 | 0.667 | 0.667 | 98.7% | +3.6% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.640 | 0.584 | 0.584 | 97.4% | -0.6% | 40 | 10 | 0 | 22 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.539 | 0.548 | 0.548 | 96.2% | +53.9% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.483 | 0.528 | 0.528 | 94.9% | +25.8% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.195 | 0.423 | 0.423 | 93.6% | +45.4% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.192 | 0.422 | 0.422 | 92.3% | +18.3% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.172 | 0.415 | 0.415 | 91.0% | +50.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.141 | 0.404 | 0.404 | 89.7% | +50.0% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.076 | 0.380 | 0.380 | 88.5% | -3.3% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.918 | 0.323 | 0.323 | 87.2% | -8.0% | 44 | 3 | 1 | 16 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 0.831 | 0.291 | 0.291 | 85.9% | +35.5% | 15 | 3 | 0 | 7 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.807 | 0.283 | 0.283 | 84.6% | +38.2% | 21 | 7 | 0 | 11 | 0 |
| 14 |  | **APP** | AppLovin Corporation | Communication Servic | 0.774 | 0.271 | 0.271 | 83.3% | +42.1% | 26 | 4 | 0 | 15 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.759 | 0.266 | 0.266 | 82.1% | +3.5% | 31 | 15 | 2 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.620 | 1.156 | 1.156 | 100.0% | +79.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.077 | 0.914 | 0.914 | 98.7% | +53.9% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.678 | 0.737 | 0.737 | 97.4% | +45.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.367 | 0.598 | 0.598 | 96.2% | +50.2% | 35 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.350 | 0.590 | 0.590 | 94.9% | +38.2% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.337 | 0.584 | 0.584 | 93.6% | +50.0% | 33 | 8 | 1 | 24 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.216 | 0.531 | 0.531 | 92.3% | +25.8% | 21 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.196 | 0.522 | 0.522 | 91.0% | +35.5% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.124 | 0.490 | 0.490 | 89.7% | +23.1% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **ANET** | Arista Networks, Inc. | Technology | 1.060 | 0.461 | 0.461 | 88.5% | +33.4% | 26 | 2 | 0 | 13 | 0 |
| 11 |  | **ACN** | Accenture plc | Technology | 1.004 | 0.436 | 0.436 | 87.2% | +41.6% | 18 | 10 | 0 | 12 | 0 |
| 12 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.980 | 0.426 | 0.426 | 85.9% | +32.7% | 30 | 7 | 0 | 24 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 0.977 | 0.425 | 0.425 | 84.6% | +19.0% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.969 | 0.421 | 0.421 | 83.3% | +25.4% | 24 | 8 | 0 | 9 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.968 | 0.420 | 0.420 | 82.1% | +20.0% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 14:19:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 14:19:46Z |  |
| stooq.prices | ok | 0 | 2026-05-08 12:08:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 12:08:10Z |  |
| stooq.prices | ok | 0 | 2026-05-08 10:52:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 10:51:58Z |  |
| stooq.prices | ok | 0 | 2026-05-08 09:19:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 09:19:54Z |  |
| stooq.prices | ok | 0 | 2026-05-08 07:48:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 07:48:20Z |  |
| stooq.prices | ok | 0 | 2026-05-08 05:57:56Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 05:57:51Z |  |
| stooq.prices | ok | 0 | 2026-05-08 03:56:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 03:56:32Z |  |
| edgar.13f | error | 0 | 2026-05-08 01:20:06Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-08 01:20:05Z |  |
| yfinance.actions | ok | 1123 | 2026-05-08 01:19:56Z |  |
| yfinance.consensus | ok | 79 | 2026-05-08 01:19:40Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-08 01:19:15Z |  |
| yfinance.prices | ok | 7110 | 2026-05-08 01:19:06Z |  |
