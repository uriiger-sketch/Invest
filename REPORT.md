# Invest — Top 15 report

_Generated: **2026-04-24 16:04 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T16:04:52Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.765 | 1.581 | 1.581 | 100.0% | +9.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.244 | 1.362 | 1.362 | 98.7% | +15.2% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.242 | 0.940 | 0.940 | 97.4% | +11.2% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.050 | 0.859 | 0.859 | 96.2% | +7.1% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.437 | 0.601 | 0.601 | 94.9% | +3.5% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.159 | 0.484 | 0.484 | 93.6% | -16.9% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.053 | 0.440 | 0.440 | 92.3% | -27.7% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 1.000 | 0.417 | 0.417 | 91.0% | +0.3% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.927 | 0.386 | 0.386 | 89.7% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.886 | 0.369 | 0.369 | 88.5% | +24.1% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.854 | 0.356 | 0.356 | 87.2% | +7.9% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★ | **CRH** | CRH plc | Basic Materials | 0.790 | 0.329 | 0.329 | 85.9% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.733 | 0.305 | 0.305 | 84.6% | -2.1% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.582 | 0.242 | 0.242 | 83.3% | -5.1% | 18 | 2 | 0 | 6 | 0 |
| 15 |  | **APH** | Amphenol Corporation | Technology | 0.568 | 0.235 | 0.235 | 82.1% | +12.2% | 14 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.303 | 0.871 | 0.871 | 100.0% | +15.2% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.270 | 0.858 | 0.858 | 98.7% | +9.9% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.811 | 0.684 | 0.684 | 97.4% | +11.2% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.679 | 0.634 | 0.634 | 96.2% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.300 | 0.489 | 0.489 | 94.9% | +39.2% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **CRH** | CRH plc | Basic Materials | 1.248 | 0.470 | 0.470 | 93.6% | +20.7% | 19 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.239 | 0.466 | 0.466 | 92.3% | +55.9% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.074 | 0.404 | 0.404 | 91.0% | +53.5% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.034 | 0.388 | 0.388 | 89.7% | +40.4% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.970 | 0.364 | 0.364 | 88.5% | +41.8% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.922 | 0.345 | 0.345 | 87.2% | +53.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.913 | 0.342 | 0.342 | 85.9% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.842 | 0.315 | 0.315 | 84.6% | +15.7% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.820 | 0.307 | 0.307 | 83.3% | +3.5% | 21 | 20 | 2 | 14 | 0 |
| 15 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.812 | 0.304 | 0.304 | 82.1% | +7.1% | 16 | 1 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.812 | 0.769 | 0.769 | 100.0% | +55.9% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.587 | 0.673 | 0.673 | 98.7% | +40.4% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **FROG** | JFrog Ltd. | Technology | 1.463 | 0.619 | 0.619 | 97.4% | +52.2% | 20 | 1 | 0 | 9 | 0 |
| 4 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.438 | 0.609 | 0.609 | 96.2% | +39.2% | 32 | 1 | 0 | 19 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.421 | 0.601 | 0.601 | 94.9% | +53.6% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.395 | 0.590 | 0.590 | 93.6% | +53.5% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.293 | 0.546 | 0.546 | 92.3% | +39.2% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.254 | 0.530 | 0.530 | 91.0% | +24.8% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.246 | 0.526 | 0.526 | 89.7% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.176 | 0.496 | 0.496 | 88.5% | +23.6% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.092 | 0.460 | 0.460 | 87.2% | +29.1% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.030 | 0.434 | 0.434 | 85.9% | +41.8% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.016 | 0.428 | 0.428 | 84.6% | +42.8% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.967 | 0.406 | 0.406 | 83.3% | +25.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **APP** | AppLovin Corporation | Communication Servic | 0.961 | 0.404 | 0.404 | 82.1% | +47.2% | 26 | 4 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 16:04:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 16:04:44Z |  |
| stooq.prices | ok | 0 | 2026-04-24 14:45:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 14:45:06Z |  |
| stooq.prices | ok | 0 | 2026-04-24 12:42:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 12:42:38Z |  |
| stooq.prices | ok | 0 | 2026-04-24 11:37:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 11:37:32Z |  |
| stooq.prices | ok | 0 | 2026-04-24 10:13:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 10:13:04Z |  |
| stooq.prices | ok | 0 | 2026-04-24 08:25:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 08:25:41Z |  |
| stooq.prices | ok | 0 | 2026-04-24 06:08:27Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-24 06:08:18Z |  |
| stooq.prices | ok | 0 | 2026-04-24 03:54:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 03:54:08Z |  |
| edgar.13f | error | 0 | 2026-04-24 00:11:13Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-24 00:11:12Z |  |
| yfinance.actions | ok | 1056 | 2026-04-24 00:10:57Z |  |
| yfinance.consensus | ok | 79 | 2026-04-24 00:10:49Z |  |
