# Invest — Top 15 report

_Generated: **2026-04-26 13:22 UTC** · Scores as of: **2026-04-26**_

🟢 last successful crawl: 0 min ago (at 2026-04-26T13:22:38Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.909 | 1.621 | 1.621 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.791 | 1.156 | 1.156 | 98.7% | +3.1% | 21 | 20 | 2 | 14 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.670 | 1.106 | 1.106 | 97.4% | -15.0% | 37 | 12 | 0 | 16 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.170 | 0.898 | 0.898 | 96.2% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ANET** | Arista Networks, Inc. | Technology | 1.088 | 0.448 | 0.448 | 94.9% | +1.6% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.988 | 0.407 | 0.407 | 93.6% | +24.1% | 23 | 8 | 0 | 12 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.972 | 0.400 | 0.400 | 92.3% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.948 | 0.390 | 0.390 | 91.0% | +7.5% | 63 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.880 | 0.362 | 0.362 | 89.7% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 10 | ★★ | **AAPL** | Apple Inc. | Technology | 0.768 | 0.315 | 0.315 | 88.5% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.756 | 0.310 | 0.310 | 87.2% | -1.6% | 29 | 5 | 1 | 16 | 0 |
| 12 |  | **APH** | Amphenol Corporation | Technology | 0.630 | 0.258 | 0.258 | 85.9% | +13.4% | 14 | 3 | 1 | 5 | 0 |
| 13 |  | **CLS** | Celestica Inc. | Technology | 0.604 | 0.247 | 0.247 | 84.6% | -2.4% | 18 | 2 | 0 | 7 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.574 | 0.234 | 0.234 | 83.3% | +12.5% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.524 | 0.214 | 0.214 | 82.1% | +21.1% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.639 | 0.982 | 0.982 | 100.0% | +9.6% | 41 | 12 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.723 | 0.639 | 0.639 | 98.7% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.392 | 0.515 | 0.515 | 97.4% | +36.7% | 45 | 3 | 1 | 20 | 0 |
| 4 | ★★ | **CRH** | CRH plc | Basic Materials | 1.373 | 0.508 | 0.508 | 96.2% | +21.1% | 19 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.370 | 0.507 | 0.507 | 94.9% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.083 | 0.399 | 0.399 | 93.6% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.071 | 0.395 | 0.395 | 92.3% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.054 | 0.389 | 0.389 | 91.0% | +3.1% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.987 | 0.363 | 0.363 | 89.7% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.969 | 0.357 | 0.357 | 88.5% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.955 | 0.352 | 0.352 | 87.2% | +14.2% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.931 | 0.343 | 0.343 | 85.9% | +9.8% | 31 | 14 | 2 | 12 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.882 | 0.324 | 0.324 | 84.6% | +18.2% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.877 | 0.322 | 0.322 | 83.3% | +7.3% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.833 | 0.306 | 0.306 | 82.1% | +22.7% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.902 | 0.814 | 0.814 | 100.0% | +56.8% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.582 | 0.676 | 0.676 | 98.7% | +41.1% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.436 | 0.612 | 0.612 | 97.4% | +38.4% | 32 | 1 | 0 | 19 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.428 | 0.609 | 0.609 | 96.2% | +49.8% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.375 | 0.586 | 0.586 | 94.9% | +50.9% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.277 | 0.543 | 0.543 | 93.6% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.274 | 0.542 | 0.542 | 92.3% | +50.6% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.263 | 0.538 | 0.538 | 91.0% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.243 | 0.529 | 0.529 | 89.7% | +36.7% | 45 | 3 | 1 | 20 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.160 | 0.493 | 0.493 | 88.5% | +22.7% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.154 | 0.490 | 0.490 | 87.2% | +30.2% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.088 | 0.462 | 0.462 | 85.9% | +42.3% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.992 | 0.420 | 0.420 | 84.6% | +20.7% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.988 | 0.418 | 0.418 | 83.3% | +25.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.973 | 0.412 | 0.412 | 82.1% | +40.5% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-26 13:22:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 13:22:32Z |  |
| stooq.prices | ok | 0 | 2026-04-26 11:58:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 11:58:45Z |  |
| stooq.prices | ok | 0 | 2026-04-26 11:07:21Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 11:07:14Z |  |
| stooq.prices | ok | 0 | 2026-04-26 10:10:18Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 10:10:12Z |  |
| stooq.prices | ok | 0 | 2026-04-26 09:03:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 09:03:08Z |  |
| stooq.prices | ok | 0 | 2026-04-26 07:56:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 07:56:47Z |  |
| stooq.prices | ok | 0 | 2026-04-26 06:12:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 06:12:34Z |  |
| stooq.prices | ok | 0 | 2026-04-26 03:58:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 03:58:38Z |  |
| stooq.prices | ok | 0 | 2026-04-26 00:08:19Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-26 00:08:12Z |  |
| edgar.13f | error | 0 | 2026-04-26 00:06:03Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-26 00:06:03Z |  |
