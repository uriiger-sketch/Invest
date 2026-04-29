# Invest — Top 15 report

_Generated: **2026-04-29 16:57 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T16:57:37Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **APP**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.317 | 1.349 | 1.349 | 100.0% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.823 | 1.148 | 1.148 | 98.7% | -10.5% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.113 | 0.858 | 0.858 | 97.4% | +23.9% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.841 | 0.747 | 0.747 | 96.2% | +9.4% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.407 | 0.570 | 0.570 | 94.9% | +8.9% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.033 | 0.418 | 0.418 | 93.6% | +8.6% | 62 | 5 | 0 | 27 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.961 | 0.389 | 0.389 | 92.3% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.953 | 0.386 | 0.386 | 91.0% | +27.5% | 23 | 8 | 0 | 12 | 0 |
| 9 |  | **APH** | Amphenol Corporation | Technology | 0.875 | 0.354 | 0.354 | 89.7% | +12.3% | 14 | 3 | 1 | 5 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.843 | 0.341 | 0.341 | 88.5% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.806 | 0.326 | 0.326 | 87.2% | +1.0% | 29 | 5 | 1 | 16 | 0 |
| 12 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.763 | 0.308 | 0.308 | 85.9% | +4.1% | 13 | 9 | 0 | 9 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.761 | 0.307 | 0.307 | 84.6% | +9.9% | 31 | 14 | 2 | 13 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.683 | 0.276 | 0.276 | 83.3% | +11.2% | 18 | 2 | 0 | 7 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.613 | 0.247 | 0.247 | 82.1% | +19.6% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.803 | 0.668 | 0.668 | 100.0% | +9.4% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.708 | 0.633 | 0.633 | 98.7% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.448 | 0.536 | 0.536 | 97.4% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.441 | 0.533 | 0.533 | 96.2% | +34.9% | 45 | 3 | 1 | 19 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.427 | 0.528 | 0.528 | 94.9% | +57.8% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.351 | 0.499 | 0.499 | 93.6% | +6.2% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.239 | 0.458 | 0.458 | 92.3% | +23.9% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.236 | 0.457 | 0.457 | 91.0% | +50.8% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.113 | 0.411 | 0.411 | 89.7% | +8.9% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.072 | 0.395 | 0.395 | 88.5% | +40.0% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.944 | 0.347 | 0.347 | 87.2% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.914 | 0.336 | 0.336 | 85.9% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.865 | 0.318 | 0.318 | 84.6% | +46.7% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.824 | 0.303 | 0.303 | 83.3% | +9.9% | 31 | 14 | 2 | 13 | 0 |
| 15 | ★★ | **APP** | AppLovin Corporation | Communication Servic | 0.811 | 0.297 | 0.297 | 82.1% | +47.3% | 26 | 4 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.919 | 0.833 | 0.833 | 100.0% | +57.8% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.842 | 0.799 | 0.799 | 98.7% | +51.8% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.515 | 0.656 | 0.656 | 97.4% | +40.0% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.386 | 0.599 | 0.599 | 96.2% | +50.8% | 36 | 10 | 0 | 21 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.335 | 0.577 | 0.577 | 94.9% | +27.2% | 27 | 3 | 1 | 7 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.334 | 0.576 | 0.576 | 93.6% | +49.2% | 35 | 10 | 1 | 24 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.275 | 0.550 | 0.550 | 92.3% | +51.5% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.250 | 0.539 | 0.539 | 91.0% | +46.7% | 20 | 1 | 0 | 9 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.211 | 0.522 | 0.522 | 89.7% | +20.5% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.139 | 0.491 | 0.491 | 88.5% | +34.9% | 45 | 3 | 1 | 19 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.094 | 0.471 | 0.471 | 87.2% | +25.9% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ABT** | Abbott Laboratories | Healthcare | 1.053 | 0.453 | 0.453 | 85.9% | +28.6% | 21 | 7 | 0 | 12 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.003 | 0.431 | 0.431 | 84.6% | +41.0% | 18 | 10 | 0 | 12 | 0 |
| 14 | ★★ | **APP** | AppLovin Corporation | Communication Servic | 0.977 | 0.420 | 0.420 | 83.3% | +47.3% | 26 | 4 | 0 | 13 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.948 | 0.407 | 0.407 | 82.1% | +33.7% | 31 | 7 | 0 | 22 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-04-29 01:17:54Z |  |
| yfinance.prices | ok | 7110 | 2026-04-29 01:17:45Z |  |
