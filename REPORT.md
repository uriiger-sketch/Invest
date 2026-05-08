# Invest — Top 15 report

_Generated: **2026-05-08 15:56 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T15:56:05Z)

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.751 | 1.739 | 1.739 | 100.0% | -2.2% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.098 | 1.499 | 1.499 | 98.7% | +2.9% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.965 | 0.714 | 0.714 | 97.4% | -7.8% | 44 | 3 | 1 | 16 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.232 | 0.444 | 0.444 | 96.2% | -4.9% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.154 | 0.415 | 0.415 | 94.9% | +9.3% | 10 | 4 | 0 | 11 | 0 |
| 6 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.121 | 0.403 | 0.403 | 93.6% | +13.8% | 17 | 1 | 0 | 8 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.869 | 0.310 | 0.310 | 92.3% | +3.8% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.696 | 0.247 | 0.247 | 91.0% | +13.9% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.636 | 0.224 | 0.224 | 89.7% | +4.7% | 23 | 3 | 0 | 8 | 0 |
| 10 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.609 | 0.215 | 0.215 | 88.5% | +3.6% | 14 | 8 | 0 | 9 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.555 | 0.195 | 0.195 | 87.2% | +18.1% | 18 | 6 | 1 | 11 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.551 | 0.193 | 0.193 | 85.9% | +25.9% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.471 | 0.164 | 0.164 | 84.6% | -1.4% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.446 | 0.155 | 0.155 | 83.3% | +19.1% | 27 | 3 | 1 | 6 | 0 |
| 15 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.417 | 0.144 | 0.144 | 82.1% | +20.6% | 22 | 8 | 0 | 6 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.050 | 0.732 | 0.732 | 100.0% | +81.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.858 | 0.663 | 0.663 | 98.7% | +2.9% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.615 | 0.575 | 0.575 | 97.4% | -2.2% | 40 | 10 | 0 | 22 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.540 | 0.548 | 0.548 | 96.2% | +54.1% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.485 | 0.528 | 0.528 | 94.9% | +25.9% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.190 | 0.421 | 0.421 | 93.6% | +18.1% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.176 | 0.416 | 0.416 | 92.3% | +44.6% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.141 | 0.404 | 0.404 | 91.0% | +48.9% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.132 | 0.400 | 0.400 | 89.7% | +49.8% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.056 | 0.373 | 0.373 | 88.5% | -4.9% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.916 | 0.322 | 0.322 | 87.2% | -7.8% | 44 | 3 | 1 | 16 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 0.888 | 0.312 | 0.312 | 85.9% | +38.6% | 15 | 3 | 0 | 7 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.822 | 0.288 | 0.288 | 84.6% | +38.9% | 21 | 7 | 0 | 11 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.767 | 0.268 | 0.268 | 83.3% | +3.8% | 31 | 15 | 2 | 11 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.742 | 0.259 | 0.259 | 82.1% | +14.6% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.656 | 1.178 | 1.178 | 100.0% | +81.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.066 | 0.914 | 0.914 | 98.7% | +54.1% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.638 | 0.722 | 0.722 | 97.4% | +44.6% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.361 | 0.598 | 0.598 | 96.2% | +38.9% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.318 | 0.579 | 0.579 | 94.9% | +49.8% | 33 | 8 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.312 | 0.576 | 0.576 | 93.6% | +48.9% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **APH** | Amphenol Corporation | Technology | 1.288 | 0.565 | 0.565 | 92.3% | +38.6% | 15 | 3 | 0 | 7 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.210 | 0.531 | 0.531 | 91.0% | +25.9% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.115 | 0.488 | 0.488 | 89.7% | +23.0% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **ANET** | Arista Networks, Inc. | Technology | 1.089 | 0.477 | 0.477 | 88.5% | +34.5% | 26 | 2 | 0 | 13 | 0 |
| 11 |  | **BAC** | Bank of America Corporation | Financial Services | 1.029 | 0.450 | 0.450 | 87.2% | +22.0% | 22 | 3 | 0 | 9 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 0.978 | 0.427 | 0.427 | 85.9% | +19.1% | 22 | 2 | 0 | 10 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.973 | 0.425 | 0.425 | 84.6% | +25.7% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.947 | 0.413 | 0.413 | 83.3% | +32.0% | 30 | 7 | 0 | 24 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.935 | 0.408 | 0.408 | 82.1% | +15.4% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 15:56:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 15:55:59Z |  |
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
