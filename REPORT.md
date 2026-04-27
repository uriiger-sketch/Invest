# Invest — Top 15 report

_Generated: **2026-04-27 09:59 UTC** · Scores as of: **2026-04-27**_

🟢 last successful crawl: 0 min ago (at 2026-04-27T09:59:14Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.851 | 1.625 | 1.625 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.879 | 1.215 | 1.215 | 98.7% | -15.0% | 37 | 12 | 0 | 14 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.692 | 1.135 | 1.135 | 97.4% | +3.1% | 21 | 20 | 2 | 14 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.138 | 0.901 | 0.901 | 96.2% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ANET** | Arista Networks, Inc. | Technology | 1.083 | 0.455 | 0.455 | 94.9% | +1.6% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.976 | 0.409 | 0.409 | 93.6% | +24.1% | 23 | 8 | 0 | 12 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.940 | 0.394 | 0.394 | 92.3% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.936 | 0.393 | 0.393 | 91.0% | +7.5% | 63 | 5 | 0 | 26 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.869 | 0.364 | 0.364 | 89.7% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.747 | 0.313 | 0.313 | 88.5% | -1.6% | 29 | 5 | 1 | 16 | 0 |
| 11 | ★★ | **AAPL** | Apple Inc. | Technology | 0.739 | 0.310 | 0.310 | 87.2% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 12 |  | **APH** | Amphenol Corporation | Technology | 0.623 | 0.260 | 0.260 | 85.9% | +13.4% | 14 | 3 | 1 | 5 | 0 |
| 13 |  | **CLS** | Celestica Inc. | Technology | 0.597 | 0.250 | 0.250 | 84.6% | -2.4% | 18 | 2 | 0 | 7 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.588 | 0.245 | 0.245 | 83.3% | +12.5% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.520 | 0.217 | 0.217 | 82.1% | +21.1% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.646 | 0.988 | 0.988 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.688 | 0.628 | 0.628 | 98.7% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.390 | 0.517 | 0.517 | 97.4% | +36.7% | 45 | 3 | 1 | 20 | 0 |
| 4 | ★★ | **CRH** | CRH plc | Basic Materials | 1.371 | 0.509 | 0.509 | 96.2% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.369 | 0.508 | 0.508 | 94.9% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.082 | 0.401 | 0.401 | 93.6% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.071 | 0.397 | 0.397 | 92.3% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.052 | 0.390 | 0.390 | 91.0% | +3.1% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.987 | 0.365 | 0.365 | 89.7% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.969 | 0.358 | 0.358 | 88.5% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.922 | 0.341 | 0.341 | 87.2% | +14.2% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.898 | 0.332 | 0.332 | 85.9% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.877 | 0.324 | 0.324 | 84.6% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.849 | 0.313 | 0.313 | 83.3% | +18.2% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.833 | 0.307 | 0.307 | 82.1% | +22.7% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.904 | 0.814 | 0.814 | 100.0% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.584 | 0.676 | 0.676 | 98.7% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.438 | 0.613 | 0.613 | 97.4% | +38.4% | 32 | 1 | 0 | 19 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.430 | 0.609 | 0.609 | 96.2% | +49.8% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.377 | 0.586 | 0.586 | 94.9% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.278 | 0.544 | 0.544 | 93.6% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.257 | 0.534 | 0.534 | 92.3% | +50.6% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.255 | 0.534 | 0.534 | 91.0% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.244 | 0.529 | 0.529 | 89.7% | +36.7% | 45 | 3 | 1 | 20 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.161 | 0.493 | 0.493 | 88.5% | +22.7% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.156 | 0.491 | 0.491 | 87.2% | +30.2% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.089 | 0.462 | 0.462 | 85.9% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.993 | 0.420 | 0.420 | 84.6% | +20.7% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.989 | 0.419 | 0.419 | 83.3% | +25.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.975 | 0.412 | 0.412 | 82.1% | +40.5% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-27 09:59:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 09:59:07Z |  |
| stooq.prices | ok | 0 | 2026-04-27 07:34:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 07:34:20Z |  |
| stooq.prices | ok | 0 | 2026-04-27 04:44:00Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 04:43:54Z |  |
| stooq.prices | ok | 0 | 2026-04-27 01:13:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-27 01:13:43Z |  |
| edgar.13f | error | 0 | 2026-04-27 00:08:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-27 00:08:21Z |  |
| yfinance.actions | ok | 1056 | 2026-04-27 00:08:13Z |  |
| yfinance.consensus | ok | 79 | 2026-04-27 00:07:59Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-27 00:07:39Z |  |
| yfinance.prices | ok | 7110 | 2026-04-27 00:07:30Z |  |
| stooq.prices | ok | 0 | 2026-04-26 23:24:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 23:23:56Z |  |
| stooq.prices | ok | 0 | 2026-04-26 22:37:34Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 22:37:30Z |  |
| stooq.prices | ok | 0 | 2026-04-26 21:50:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 21:50:30Z |  |
