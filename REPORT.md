# Invest — Top 15 report

_Generated: **2026-05-09 08:21 UTC** · Scores as of: **2026-05-09**_

🟢 last successful crawl: 0 min ago (at 2026-05-09T08:21:41Z)

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.283 | 2.038 | 2.038 | 100.0% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.896 | 1.501 | 1.501 | 98.7% | +5.4% | 22 | 18 | 2 | 19 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.971 | 0.755 | 0.755 | 97.4% | -11.6% | 44 | 3 | 1 | 22 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.259 | 0.480 | 0.480 | 96.2% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.066 | 0.405 | 0.405 | 94.9% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.048 | 0.398 | 0.398 | 93.6% | +7.2% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.844 | 0.319 | 0.319 | 92.3% | +3.4% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.613 | 0.229 | 0.229 | 91.0% | +14.0% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.589 | 0.220 | 0.220 | 89.7% | +2.9% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.563 | 0.210 | 0.210 | 88.5% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.558 | 0.208 | 0.208 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.546 | 0.203 | 0.203 | 85.9% | +4.6% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.463 | 0.172 | 0.172 | 84.6% | -1.1% | 20 | 1 | 0 | 12 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.458 | 0.169 | 0.169 | 83.3% | +10.6% | 43 | 3 | 0 | 16 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.377 | 0.138 | 0.138 | 82.1% | +19.7% | 27 | 3 | 1 | 7 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.987 | 0.727 | 0.727 | 100.0% | +5.4% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.922 | 0.703 | 0.703 | 98.7% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.907 | 0.697 | 0.697 | 97.4% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.570 | 0.572 | 0.572 | 96.2% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.509 | 0.550 | 0.550 | 94.9% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.244 | 0.452 | 0.452 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.168 | 0.424 | 0.424 | 92.3% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.137 | 0.412 | 0.412 | 91.0% | +51.2% | 35 | 10 | 0 | 22 | 0 |
| 9 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.130 | 0.410 | 0.410 | 89.7% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.042 | 0.377 | 0.377 | 88.5% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.915 | 0.330 | 0.330 | 87.2% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.905 | 0.326 | 0.326 | 85.9% | -11.6% | 44 | 3 | 1 | 22 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.832 | 0.300 | 0.300 | 84.6% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.814 | 0.293 | 0.293 | 83.3% | +3.4% | 31 | 15 | 2 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.699 | 0.250 | 0.250 | 82.1% | +22.7% | 22 | 3 | 0 | 9 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.509 | 1.132 | 1.132 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.147 | 0.967 | 0.967 | 98.7% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.655 | 0.743 | 0.743 | 97.4% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.391 | 0.623 | 0.623 | 96.2% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.368 | 0.613 | 0.613 | 94.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.365 | 0.611 | 0.611 | 93.6% | +51.2% | 35 | 10 | 0 | 22 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.225 | 0.547 | 0.547 | 92.3% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.200 | 0.536 | 0.536 | 91.0% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.080 | 0.481 | 0.481 | 89.7% | +22.4% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 1.044 | 0.465 | 0.465 | 88.5% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.043 | 0.465 | 0.465 | 87.2% | +35.2% | 30 | 7 | 0 | 24 | 0 |
| 12 |  | **ANET** | Arista Networks, Inc. | Technology | 1.000 | 0.445 | 0.445 | 85.9% | +32.2% | 26 | 2 | 0 | 13 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.944 | 0.419 | 0.419 | 84.6% | +25.1% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.938 | 0.417 | 0.417 | 83.3% | +18.2% | 22 | 2 | 0 | 10 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.937 | 0.416 | 0.416 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-09 08:21:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 08:21:35Z |  |
| stooq.prices | ok | 0 | 2026-05-09 06:24:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 06:24:17Z |  |
| stooq.prices | ok | 0 | 2026-05-09 03:59:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 03:59:49Z |  |
| edgar.13f | error | 0 | 2026-05-09 01:17:18Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-09 01:17:17Z |  |
| yfinance.actions | ok | 1172 | 2026-05-09 01:17:07Z |  |
| yfinance.consensus | ok | 79 | 2026-05-09 01:16:58Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-09 01:16:43Z |  |
| yfinance.prices | ok | 7110 | 2026-05-09 01:16:37Z |  |
| stooq.prices | ok | 0 | 2026-05-09 00:13:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 00:13:35Z |  |
| stooq.prices | ok | 0 | 2026-05-08 23:13:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 23:13:48Z |  |
| stooq.prices | ok | 0 | 2026-05-08 22:17:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 22:16:13Z |  |
| stooq.prices | ok | 0 | 2026-05-08 21:19:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 21:19:04Z |  |
