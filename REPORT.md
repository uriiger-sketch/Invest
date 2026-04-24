# Invest — Top 15 report

_Generated: **2026-04-24 06:08 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T06:08:28Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.761 | 1.595 | 1.595 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.179 | 1.347 | 1.347 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.175 | 0.921 | 0.921 | 97.4% | +10.3% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.159 | 0.914 | 0.914 | 96.2% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.463 | 0.618 | 0.618 | 94.9% | +3.5% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **ARM** | Arm Holdings plc | Technology | 1.367 | 0.577 | 0.577 | 93.6% | -17.1% | 27 | 10 | 2 | 18 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.047 | 0.441 | 0.441 | 92.3% | +4.2% | 27 | 3 | 0 | 11 | 0 |
| 8 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.034 | 0.436 | 0.436 | 91.0% | -4.2% | 36 | 13 | 0 | 16 | 0 |
| 9 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.940 | 0.396 | 0.396 | 89.7% | +25.3% | 23 | 8 | 0 | 12 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.914 | 0.385 | 0.385 | 88.5% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.870 | 0.366 | 0.366 | 87.2% | +11.1% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.775 | 0.326 | 0.326 | 85.9% | -2.7% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.724 | 0.304 | 0.304 | 84.6% | +22.0% | 19 | 2 | 0 | 3 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.508 | 0.212 | 0.212 | 83.3% | +13.2% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.484 | 0.202 | 0.202 | 82.1% | +21.4% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.221 | 0.848 | 0.848 | 100.0% | +8.9% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.196 | 0.838 | 0.838 | 98.7% | +12.7% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.734 | 0.660 | 0.660 | 97.4% | +10.3% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.631 | 0.621 | 0.621 | 96.2% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.514 | 0.576 | 0.576 | 94.9% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.283 | 0.487 | 0.487 | 93.6% | +38.5% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.238 | 0.470 | 0.470 | 92.3% | +22.0% | 19 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.009 | 0.382 | 0.382 | 91.0% | +57.5% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.991 | 0.375 | 0.375 | 89.7% | +12.8% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.966 | 0.365 | 0.365 | 88.5% | +40.1% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.960 | 0.363 | 0.363 | 87.2% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.935 | 0.354 | 0.354 | 85.9% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.931 | 0.352 | 0.352 | 84.6% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.919 | 0.348 | 0.348 | 83.3% | +54.2% | 20 | 1 | 0 | 9 | 0 |
| 15 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.808 | 0.305 | 0.305 | 82.1% | +3.5% | 21 | 20 | 2 | 14 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.867 | 0.793 | 0.793 | 100.0% | +59.1% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.641 | 0.696 | 0.696 | 98.7% | +57.5% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.593 | 0.675 | 0.675 | 97.4% | +40.1% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.519 | 0.644 | 0.644 | 96.2% | +55.1% | 35 | 10 | 1 | 24 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.495 | 0.633 | 0.633 | 94.9% | +54.2% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.275 | 0.539 | 0.539 | 93.6% | +38.5% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.264 | 0.534 | 0.534 | 92.3% | +21.4% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.214 | 0.513 | 0.513 | 91.0% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.202 | 0.508 | 0.508 | 89.7% | +32.5% | 32 | 1 | 0 | 19 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.069 | 0.450 | 0.450 | 88.5% | +28.3% | 21 | 7 | 0 | 12 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.066 | 0.449 | 0.449 | 87.2% | +20.9% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.062 | 0.448 | 0.448 | 85.9% | +42.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.969 | 0.407 | 0.407 | 84.6% | +22.0% | 19 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.963 | 0.405 | 0.405 | 83.3% | +40.5% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.923 | 0.388 | 0.388 | 82.1% | +19.5% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 06:08:27Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-24 06:08:18Z |  |
| stooq.prices | ok | 0 | 2026-04-24 03:54:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 03:54:08Z |  |
| edgar.13f | error | 0 | 2026-04-24 00:11:13Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-24 00:11:12Z |  |
| yfinance.actions | ok | 1056 | 2026-04-24 00:10:57Z |  |
| yfinance.consensus | ok | 79 | 2026-04-24 00:10:49Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-24 00:10:38Z |  |
| yfinance.prices | ok | 7110 | 2026-04-24 00:10:32Z |  |
| stooq.prices | ok | 0 | 2026-04-24 00:05:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 00:05:49Z |  |
| stooq.prices | ok | 0 | 2026-04-23 23:09:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 23:09:49Z |  |
| stooq.prices | ok | 0 | 2026-04-23 22:04:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 22:04:12Z |  |
| stooq.prices | ok | 0 | 2026-04-23 21:10:49Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 21:10:43Z |  |
| stooq.prices | ok | 0 | 2026-04-23 20:15:01Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-23 20:14:56Z |  |
