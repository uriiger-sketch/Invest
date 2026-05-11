# Invest — Top 15 report

_Generated: **2026-05-11 15:47 UTC** · Scores as of: **2026-05-11**_

🟢 last successful crawl: 0 min ago (at 2026-05-11T15:47:33Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **APP**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DHR**, **DIS**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.221 | 1.981 | 1.981 | 100.0% | -3.9% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.036 | 1.529 | 1.529 | 98.7% | +9.0% | 22 | 18 | 2 | 19 | 0 |
| 3 |  | **DDOG** | Datadog, Inc. | Technology | 1.629 | 0.613 | 0.613 | 97.4% | +5.9% | 44 | 3 | 1 | 22 | 0 |
| 4 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.510 | 0.567 | 0.567 | 96.2% | +11.5% | 10 | 4 | 0 | 11 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.457 | 0.547 | 0.547 | 94.9% | -7.7% | 42 | 11 | 0 | 27 | 0 |
| 6 | ★★ | **AAPL** | Apple Inc. | Technology | 0.883 | 0.328 | 0.328 | 93.6% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 7 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.788 | 0.292 | 0.292 | 92.3% | +2.0% | 17 | 1 | 0 | 8 | 0 |
| 8 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.697 | 0.257 | 0.257 | 91.0% | +5.1% | 22 | 3 | 0 | 8 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.643 | 0.237 | 0.237 | 89.7% | +3.0% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **CVX** | Chevron Corporation | Energy | 0.616 | 0.227 | 0.227 | 88.5% | +16.7% | 18 | 6 | 1 | 11 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.515 | 0.188 | 0.188 | 87.2% | +14.4% | 62 | 4 | 0 | 29 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.512 | 0.187 | 0.187 | 85.9% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.446 | 0.162 | 0.162 | 84.6% | +16.7% | 20 | 1 | 0 | 12 | 0 |
| 14 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.394 | 0.142 | 0.142 | 83.3% | +25.7% | 23 | 8 | 0 | 9 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.379 | 0.136 | 0.136 | 82.1% | +17.6% | 22 | 2 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.148 | 0.797 | 0.797 | 100.0% | +9.0% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.888 | 0.699 | 0.699 | 98.7% | -3.9% | 40 | 11 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.887 | 0.699 | 0.699 | 97.4% | +80.2% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.478 | 0.546 | 0.546 | 96.2% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.448 | 0.534 | 0.534 | 94.9% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.216 | 0.447 | 0.447 | 93.6% | -7.7% | 42 | 11 | 0 | 27 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.192 | 0.439 | 0.439 | 92.3% | +50.3% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **CVX** | Chevron Corporation | Energy | 1.191 | 0.438 | 0.438 | 91.0% | +16.7% | 18 | 6 | 1 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.154 | 0.424 | 0.424 | 89.7% | +54.7% | 34 | 10 | 0 | 22 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.046 | 0.384 | 0.384 | 88.5% | +50.3% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.887 | 0.325 | 0.325 | 87.2% | +45.7% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.849 | 0.310 | 0.310 | 85.9% | +43.7% | 21 | 7 | 0 | 11 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.839 | 0.306 | 0.306 | 84.6% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 14 | ★★ | **APP** | AppLovin Corporation | Communication Servic | 0.778 | 0.283 | 0.283 | 83.3% | +41.4% | 26 | 4 | 0 | 15 | 0 |
| 15 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.707 | 0.257 | 0.257 | 82.1% | +24.2% | 27 | 3 | 1 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.422 | 1.113 | 1.113 | 100.0% | +80.2% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.022 | 0.927 | 0.927 | 98.7% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.686 | 0.771 | 0.771 | 97.4% | +50.3% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.410 | 0.644 | 0.644 | 96.2% | +54.7% | 34 | 10 | 0 | 22 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.406 | 0.642 | 0.642 | 94.9% | +45.7% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.390 | 0.635 | 0.635 | 93.6% | +43.7% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.208 | 0.550 | 0.550 | 92.3% | +50.3% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.186 | 0.540 | 0.540 | 91.0% | +26.2% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **ANET** | Arista Networks, Inc. | Technology | 1.176 | 0.536 | 0.536 | 89.7% | +37.0% | 28 | 1 | 0 | 13 | 0 |
| 10 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.115 | 0.507 | 0.507 | 88.5% | +40.1% | 30 | 7 | 0 | 24 | 0 |
| 11 |  | **BAC** | Bank of America Corporation | Financial Services | 1.044 | 0.474 | 0.474 | 87.2% | +24.7% | 22 | 3 | 0 | 9 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.990 | 0.449 | 0.449 | 85.9% | +21.8% | 9 | 1 | 0 | 0 | 0 |
| 13 | ★★ | **APP** | AppLovin Corporation | Communication Servic | 0.912 | 0.413 | 0.413 | 84.6% | +41.4% | 26 | 4 | 0 | 15 | 0 |
| 14 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.906 | 0.410 | 0.410 | 83.3% | +15.9% | 10 | 1 | 0 | 3 | 0 |
| 15 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.900 | 0.408 | 0.408 | 82.1% | +24.2% | 27 | 3 | 1 | 7 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-11 15:47:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 15:47:22Z |  |
| stooq.prices | ok | 0 | 2026-05-11 12:31:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 12:31:42Z |  |
| stooq.prices | ok | 0 | 2026-05-11 09:37:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 09:37:39Z |  |
| stooq.prices | ok | 0 | 2026-05-11 05:43:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 05:43:01Z |  |
| stooq.prices | ok | 0 | 2026-05-11 01:29:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 01:29:39Z |  |
| edgar.13f | error | 0 | 2026-05-11 01:25:08Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-11 01:25:07Z |  |
| yfinance.actions | ok | 1153 | 2026-05-11 01:24:49Z |  |
| yfinance.consensus | ok | 79 | 2026-05-11 01:24:42Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-11 01:24:31Z |  |
| yfinance.prices | ok | 7110 | 2026-05-11 01:24:27Z |  |
| stooq.prices | ok | 0 | 2026-05-10 23:34:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 23:33:59Z |  |
| stooq.prices | ok | 0 | 2026-05-10 22:28:32Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 22:28:26Z |  |
