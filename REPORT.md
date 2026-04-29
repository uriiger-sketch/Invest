# Invest — Top 15 report

_Generated: **2026-04-29 18:14 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T18:14:52Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **APH**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.309 | 1.344 | 1.344 | 100.0% | +6.6% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.852 | 1.158 | 1.158 | 98.7% | -11.5% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.078 | 0.843 | 0.843 | 97.4% | +23.8% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.832 | 0.743 | 0.743 | 96.2% | +9.7% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.415 | 0.573 | 0.573 | 94.9% | +8.3% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.048 | 0.424 | 0.424 | 93.6% | +7.8% | 62 | 5 | 0 | 27 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.961 | 0.388 | 0.388 | 92.3% | +27.3% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.943 | 0.381 | 0.381 | 91.0% | +27.3% | 23 | 8 | 0 | 12 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.844 | 0.341 | 0.341 | 89.7% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 10 | ★★ | **APH** | Amphenol Corporation | Technology | 0.818 | 0.330 | 0.330 | 88.5% | +14.2% | 14 | 3 | 1 | 5 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.795 | 0.321 | 0.321 | 87.2% | +1.0% | 29 | 5 | 1 | 16 | 0 |
| 12 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.757 | 0.305 | 0.305 | 85.9% | +4.0% | 13 | 9 | 0 | 9 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.752 | 0.303 | 0.303 | 84.6% | +10.2% | 31 | 14 | 2 | 13 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.732 | 0.295 | 0.295 | 83.3% | +9.4% | 18 | 2 | 0 | 7 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.606 | 0.244 | 0.244 | 82.1% | +19.4% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.807 | 0.669 | 0.669 | 100.0% | +9.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.710 | 0.633 | 0.633 | 98.7% | +27.3% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.447 | 0.535 | 0.535 | 97.4% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.431 | 0.529 | 0.529 | 96.2% | +58.1% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.422 | 0.525 | 0.525 | 94.9% | +34.0% | 45 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.358 | 0.502 | 0.502 | 93.6% | +6.6% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.219 | 0.450 | 0.450 | 92.3% | +23.8% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.218 | 0.449 | 0.449 | 91.0% | +50.0% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.102 | 0.406 | 0.406 | 89.7% | +8.3% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.101 | 0.405 | 0.405 | 88.5% | +41.4% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.950 | 0.349 | 0.349 | 87.2% | +20.9% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.914 | 0.336 | 0.336 | 85.9% | +49.3% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.861 | 0.316 | 0.316 | 84.6% | +46.7% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.832 | 0.305 | 0.305 | 83.3% | +10.2% | 31 | 14 | 2 | 13 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.822 | 0.301 | 0.301 | 82.1% | +14.2% | 14 | 3 | 1 | 5 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.919 | 0.835 | 0.835 | 100.0% | +58.1% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.854 | 0.807 | 0.807 | 98.7% | +52.5% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.558 | 0.677 | 0.677 | 97.4% | +41.4% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.350 | 0.585 | 0.585 | 96.2% | +50.0% | 36 | 10 | 0 | 21 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.333 | 0.577 | 0.577 | 94.9% | +27.3% | 27 | 3 | 1 | 7 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.328 | 0.575 | 0.575 | 93.6% | +49.3% | 35 | 10 | 1 | 24 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.303 | 0.564 | 0.564 | 92.3% | +52.5% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.241 | 0.537 | 0.537 | 91.0% | +46.7% | 20 | 1 | 0 | 9 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.222 | 0.528 | 0.528 | 89.7% | +20.9% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.099 | 0.474 | 0.474 | 88.5% | +34.0% | 45 | 3 | 1 | 19 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.089 | 0.470 | 0.470 | 87.2% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ABT** | Abbott Laboratories | Healthcare | 1.057 | 0.456 | 0.456 | 85.9% | +28.9% | 21 | 7 | 0 | 12 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.975 | 0.420 | 0.420 | 84.6% | +40.5% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **APP** | AppLovin Corporation | Communication Servic | 0.950 | 0.409 | 0.409 | 83.3% | +46.7% | 26 | 4 | 0 | 13 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.940 | 0.404 | 0.404 | 82.1% | +33.7% | 31 | 7 | 0 | 22 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-29 18:14:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 18:14:45Z |  |
| stooq.prices | ok | 0 | 2026-04-29 16:57:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 16:57:30Z |  |
| stooq.prices | ok | 0 | 2026-04-29 15:20:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 15:20:11Z |  |
| stooq.prices | ok | 0 | 2026-04-29 12:58:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-29 11:09:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 11:09:50Z |  |
| stooq.prices | ok | 0 | 2026-04-29 09:09:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 09:09:27Z |  |
| stooq.prices | ok | 0 | 2026-04-29 06:40:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 06:40:50Z |  |
| stooq.prices | ok | 0 | 2026-04-29 04:05:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 04:05:50Z |  |
| edgar.13f | error | 0 | 2026-04-29 01:18:49Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-29 01:18:48Z |  |
| yfinance.actions | ok | 1063 | 2026-04-29 01:18:37Z |  |
| yfinance.consensus | ok | 79 | 2026-04-29 01:18:19Z |  |
