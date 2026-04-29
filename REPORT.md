# Invest — Top 15 report

_Generated: **2026-04-29 19:56 UTC** · Scores as of: **2026-04-29**_

🟢 last successful crawl: 0 min ago (at 2026-04-29T19:56:36Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.332 | 1.350 | 1.350 | 100.0% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 2 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.797 | 1.133 | 1.133 | 98.7% | -12.0% | 36 | 13 | 0 | 15 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.151 | 0.871 | 0.871 | 97.4% | +19.7% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.837 | 0.743 | 0.743 | 96.2% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.416 | 0.572 | 0.572 | 94.9% | +6.8% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.998 | 0.402 | 0.402 | 93.6% | +8.1% | 62 | 5 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.985 | 0.397 | 0.397 | 92.3% | +24.3% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.965 | 0.389 | 0.389 | 91.0% | +26.7% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.837 | 0.337 | 0.337 | 89.7% | +25.6% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **APH** | Amphenol Corporation | Technology | 0.777 | 0.313 | 0.313 | 88.5% | +14.6% | 14 | 3 | 1 | 5 | 0 |
| 11 |  | **CLS** | Celestica Inc. | Technology | 0.765 | 0.308 | 0.308 | 87.2% | +7.0% | 18 | 2 | 0 | 7 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.754 | 0.303 | 0.303 | 85.9% | +1.1% | 29 | 5 | 1 | 16 | 0 |
| 13 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.748 | 0.301 | 0.301 | 84.6% | +2.9% | 13 | 9 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.736 | 0.296 | 0.296 | 83.3% | +10.3% | 31 | 14 | 2 | 13 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.621 | 0.249 | 0.249 | 82.1% | +17.5% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.799 | 0.666 | 0.666 | 100.0% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.721 | 0.637 | 0.637 | 98.7% | +26.7% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.460 | 0.540 | 0.540 | 97.4% | +25.6% | 19 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.453 | 0.537 | 0.537 | 96.2% | +57.1% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.408 | 0.520 | 0.520 | 94.9% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.343 | 0.496 | 0.496 | 93.6% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.213 | 0.447 | 0.447 | 92.3% | +48.0% | 36 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.158 | 0.427 | 0.427 | 91.0% | +19.7% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.110 | 0.409 | 0.409 | 89.7% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.075 | 0.396 | 0.396 | 88.5% | +6.8% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.965 | 0.355 | 0.355 | 87.2% | +20.6% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.931 | 0.342 | 0.342 | 85.9% | +48.2% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.887 | 0.325 | 0.325 | 84.6% | +46.3% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.843 | 0.309 | 0.309 | 83.3% | +10.3% | 31 | 14 | 2 | 13 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.834 | 0.306 | 0.306 | 82.1% | +18.7% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.931 | 0.842 | 0.842 | 100.0% | +57.1% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.824 | 0.794 | 0.794 | 98.7% | +50.4% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.552 | 0.674 | 0.674 | 97.4% | +40.2% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.344 | 0.583 | 0.583 | 96.2% | +26.7% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.333 | 0.578 | 0.578 | 94.9% | +48.2% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.327 | 0.575 | 0.575 | 93.6% | +48.0% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.310 | 0.568 | 0.568 | 92.3% | +51.3% | 28 | 7 | 0 | 23 | 0 |
| 8 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.274 | 0.552 | 0.552 | 91.0% | +46.3% | 20 | 1 | 0 | 9 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.241 | 0.538 | 0.538 | 89.7% | +20.6% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.109 | 0.479 | 0.479 | 88.5% | +25.6% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.109 | 0.479 | 0.479 | 87.2% | +29.5% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.065 | 0.460 | 0.460 | 85.9% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.959 | 0.413 | 0.413 | 84.6% | +39.0% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.956 | 0.412 | 0.412 | 83.3% | +33.1% | 31 | 7 | 0 | 22 | 0 |
| 15 |  | **APP** | AppLovin Corporation | Communication Servic | 0.916 | 0.394 | 0.394 | 82.1% | +44.5% | 26 | 4 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-29 19:56:36Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 19:56:30Z |  |
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
