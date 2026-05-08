# Invest — Top 15 report

_Generated: **2026-05-08 18:48 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T18:48:12Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BSX**, **BUD**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.765 | 1.728 | 1.728 | 100.0% | -3.3% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.087 | 1.480 | 1.480 | 98.7% | +4.8% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.022 | 0.728 | 0.728 | 97.4% | -9.9% | 44 | 3 | 1 | 16 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.261 | 0.450 | 0.450 | 96.2% | -6.2% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.180 | 0.420 | 0.420 | 94.9% | +11.2% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.136 | 0.405 | 0.405 | 93.6% | +8.3% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.866 | 0.306 | 0.306 | 92.3% | +3.7% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.678 | 0.238 | 0.238 | 91.0% | +14.2% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.619 | 0.216 | 0.216 | 89.7% | +4.6% | 23 | 3 | 0 | 8 | 0 |
| 10 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.611 | 0.213 | 0.213 | 88.5% | +3.1% | 14 | 8 | 0 | 9 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.557 | 0.194 | 0.194 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.549 | 0.190 | 0.190 | 85.9% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.510 | 0.176 | 0.176 | 84.6% | -4.3% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.426 | 0.146 | 0.146 | 83.3% | +19.8% | 27 | 3 | 1 | 6 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.378 | 0.128 | 0.128 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.974 | 0.707 | 0.707 | 100.0% | +79.1% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.899 | 0.680 | 0.680 | 98.7% | +4.8% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.594 | 0.569 | 0.569 | 97.4% | +57.2% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.580 | 0.564 | 0.564 | 96.2% | -3.3% | 40 | 10 | 0 | 22 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.497 | 0.534 | 0.534 | 94.9% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.200 | 0.426 | 0.426 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.192 | 0.423 | 0.423 | 92.3% | +45.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.191 | 0.423 | 0.423 | 91.0% | +52.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.087 | 0.385 | 0.385 | 89.7% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.039 | 0.368 | 0.368 | 88.5% | -6.2% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.924 | 0.326 | 0.326 | 87.2% | +40.8% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.889 | 0.314 | 0.314 | 85.9% | -9.9% | 44 | 3 | 1 | 16 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.848 | 0.299 | 0.299 | 84.6% | +40.2% | 21 | 7 | 0 | 11 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.773 | 0.271 | 0.271 | 83.3% | +15.7% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.771 | 0.271 | 0.271 | 82.1% | +3.7% | 31 | 15 | 2 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.534 | 1.134 | 1.134 | 100.0% | +79.1% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.136 | 0.954 | 0.954 | 98.7% | +57.2% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.651 | 0.735 | 0.735 | 97.4% | +45.7% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.401 | 0.622 | 0.622 | 96.2% | +52.2% | 35 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.385 | 0.615 | 0.615 | 94.9% | +40.2% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **APH** | Amphenol Corporation | Technology | 1.340 | 0.595 | 0.595 | 93.6% | +40.8% | 15 | 3 | 0 | 7 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.247 | 0.553 | 0.553 | 92.3% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.224 | 0.542 | 0.542 | 91.0% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.090 | 0.482 | 0.482 | 89.7% | +22.5% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **BAC** | Bank of America Corporation | Financial Services | 1.042 | 0.460 | 0.460 | 88.5% | +22.5% | 22 | 3 | 0 | 9 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.010 | 0.446 | 0.446 | 87.2% | +34.1% | 30 | 7 | 0 | 24 | 0 |
| 12 |  | **ANET** | Arista Networks, Inc. | Technology | 1.002 | 0.442 | 0.442 | 85.9% | +32.2% | 26 | 2 | 0 | 13 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 0.960 | 0.423 | 0.423 | 84.6% | +18.7% | 22 | 2 | 0 | 10 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.952 | 0.419 | 0.419 | 83.3% | +25.3% | 24 | 8 | 0 | 9 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.940 | 0.414 | 0.414 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 18:48:11Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 18:48:02Z |  |
| stooq.prices | ok | 0 | 2026-05-08 17:16:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 17:16:46Z |  |
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
