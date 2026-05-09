# Invest — Top 15 report

_Generated: **2026-05-09 00:13 UTC** · Scores as of: **2026-05-09**_

🟢 last successful crawl: 0 min ago (at 2026-05-09T00:13:43Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BAC**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.757 | 1.736 | 1.736 | 100.0% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.096 | 1.493 | 1.493 | 98.7% | +5.4% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.097 | 0.760 | 0.760 | 97.4% | -11.6% | 44 | 3 | 1 | 16 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.335 | 0.480 | 0.480 | 96.2% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.136 | 0.407 | 0.407 | 94.9% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.117 | 0.400 | 0.400 | 93.6% | +7.2% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.912 | 0.325 | 0.325 | 92.3% | +3.4% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.658 | 0.232 | 0.232 | 91.0% | +14.0% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.620 | 0.218 | 0.218 | 89.7% | +2.9% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.611 | 0.215 | 0.215 | 88.5% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.610 | 0.214 | 0.214 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.587 | 0.206 | 0.206 | 85.9% | +4.6% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AVGO** | Broadcom Inc. | Technology | 0.494 | 0.172 | 0.172 | 84.6% | +10.6% | 43 | 3 | 0 | 16 | 0 |
| 14 |  | **FROG** | JFrog Ltd. | Technology | 0.474 | 0.164 | 0.164 | 83.3% | -4.6% | 20 | 1 | 0 | 9 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.409 | 0.140 | 0.140 | 82.1% | +19.7% | 27 | 3 | 1 | 6 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.979 | 0.716 | 0.716 | 100.0% | +5.4% | 22 | 18 | 2 | 14 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.942 | 0.703 | 0.703 | 98.7% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.588 | 0.573 | 0.573 | 97.4% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.543 | 0.557 | 0.557 | 96.2% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.539 | 0.555 | 0.555 | 94.9% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.278 | 0.459 | 0.459 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.183 | 0.425 | 0.425 | 92.3% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.151 | 0.413 | 0.413 | 91.0% | +51.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.143 | 0.410 | 0.410 | 89.7% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.056 | 0.378 | 0.378 | 88.5% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.931 | 0.332 | 0.332 | 87.2% | -11.6% | 44 | 3 | 1 | 16 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 0.928 | 0.331 | 0.331 | 85.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.845 | 0.301 | 0.301 | 84.6% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.845 | 0.301 | 0.301 | 83.3% | +3.4% | 31 | 15 | 2 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.712 | 0.252 | 0.252 | 82.1% | +22.7% | 22 | 3 | 0 | 9 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.506 | 1.131 | 1.131 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.145 | 0.966 | 0.966 | 98.7% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.655 | 0.743 | 0.743 | 97.4% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.391 | 0.623 | 0.623 | 96.2% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.368 | 0.613 | 0.613 | 94.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.364 | 0.611 | 0.611 | 93.6% | +51.2% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.224 | 0.547 | 0.547 | 92.3% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.203 | 0.538 | 0.538 | 91.0% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.081 | 0.482 | 0.482 | 89.7% | +22.4% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 1.045 | 0.466 | 0.466 | 88.5% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.044 | 0.465 | 0.465 | 87.2% | +35.2% | 30 | 7 | 0 | 24 | 0 |
| 12 |  | **ANET** | Arista Networks, Inc. | Technology | 1.001 | 0.445 | 0.445 | 85.9% | +32.2% | 26 | 2 | 0 | 13 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.945 | 0.420 | 0.420 | 84.6% | +25.1% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.940 | 0.418 | 0.418 | 83.3% | +18.2% | 22 | 2 | 0 | 10 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.939 | 0.417 | 0.417 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-09 00:13:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 00:13:35Z |  |
| stooq.prices | ok | 0 | 2026-05-08 23:13:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 23:13:48Z |  |
| stooq.prices | ok | 0 | 2026-05-08 22:17:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 22:16:13Z |  |
| stooq.prices | ok | 0 | 2026-05-08 21:19:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 21:19:04Z |  |
| stooq.prices | ok | 0 | 2026-05-08 20:07:19Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 20:07:13Z |  |
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
