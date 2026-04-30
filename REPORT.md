# Invest — Top 15 report

_Generated: **2026-04-30 16:50 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T16:50:55Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **APH**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.061 | 1.277 | 1.277 | 100.0% | -14.0% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.086 | 0.869 | 0.869 | 98.7% | +19.4% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.884 | 0.784 | 0.784 | 97.4% | +10.7% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.453 | 0.604 | 0.604 | 96.2% | +5.0% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.300 | 0.539 | 0.539 | 94.9% | +3.6% | 14 | 8 | 0 | 10 | 0 |
| 6 |  | **CLS** | Celestica Inc. | Technology | 1.269 | 0.527 | 0.527 | 93.6% | +9.3% | 19 | 1 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.054 | 0.436 | 0.436 | 92.3% | +24.6% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.975 | 0.403 | 0.403 | 91.0% | +9.4% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.943 | 0.390 | 0.390 | 89.7% | +22.0% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.881 | 0.364 | 0.364 | 88.5% | +24.6% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.832 | 0.343 | 0.343 | 87.2% | -1.8% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.802 | 0.331 | 0.331 | 85.9% | +9.3% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.679 | 0.279 | 0.279 | 84.6% | +15.9% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.665 | 0.273 | 0.273 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.642 | 0.264 | 0.264 | 82.1% | +15.1% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.714 | 0.643 | 0.643 | 100.0% | +24.6% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.492 | 0.559 | 0.559 | 98.7% | +10.7% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.488 | 0.557 | 0.557 | 97.4% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.467 | 0.549 | 0.549 | 96.2% | +63.2% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.426 | 0.534 | 0.534 | 94.9% | +22.0% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.178 | 0.440 | 0.440 | 93.6% | +47.7% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.134 | 0.423 | 0.423 | 92.3% | +19.4% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.129 | 0.421 | 0.421 | 91.0% | +48.4% | 31 | 2 | 0 | 19 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.102 | 0.411 | 0.411 | 89.7% | +5.0% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.035 | 0.386 | 0.386 | 88.5% | +38.9% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.020 | 0.380 | 0.380 | 87.2% | +53.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.899 | 0.334 | 0.334 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.889 | 0.331 | 0.331 | 84.6% | +9.3% | 31 | 14 | 2 | 13 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.864 | 0.321 | 0.321 | 83.3% | +15.9% | 14 | 3 | 1 | 3 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.853 | 0.317 | 0.317 | 82.1% | +9.5% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.085 | 0.912 | 0.912 | 100.0% | +63.2% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.774 | 0.775 | 0.775 | 98.7% | +48.4% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.476 | 0.643 | 0.643 | 97.4% | +38.9% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.474 | 0.642 | 0.642 | 96.2% | +53.6% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **FROG** | JFrog Ltd. | Technology | 1.282 | 0.557 | 0.557 | 94.9% | +46.7% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.257 | 0.547 | 0.547 | 93.6% | +24.6% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.242 | 0.540 | 0.540 | 92.3% | +47.7% | 36 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.239 | 0.538 | 0.538 | 91.0% | +51.5% | 28 | 7 | 0 | 22 | 0 |
| 9 |  | **ABT** | Abbott Laboratories | Healthcare | 1.128 | 0.489 | 0.489 | 89.7% | +30.8% | 21 | 7 | 0 | 11 | 0 |
| 10 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.108 | 0.481 | 0.481 | 88.5% | +63.0% | 16 | 20 | 0 | 14 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.107 | 0.480 | 0.480 | 87.2% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.057 | 0.458 | 0.458 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.025 | 0.444 | 0.444 | 84.6% | +41.0% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.003 | 0.434 | 0.434 | 83.3% | +33.7% | 31 | 7 | 0 | 26 | 0 |
| 15 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.972 | 0.420 | 0.420 | 82.1% | +22.0% | 19 | 2 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 16:50:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 16:50:49Z |  |
| stooq.prices | ok | 0 | 2026-04-30 15:14:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 15:14:04Z |  |
| stooq.prices | ok | 0 | 2026-04-30 12:58:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-30 11:10:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 11:10:54Z |  |
| stooq.prices | ok | 0 | 2026-04-30 09:11:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 09:10:56Z |  |
| stooq.prices | ok | 0 | 2026-04-30 06:44:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 06:44:48Z |  |
| stooq.prices | ok | 0 | 2026-04-30 04:07:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 04:07:41Z |  |
| edgar.13f | error | 0 | 2026-04-30 01:18:07Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-30 01:18:07Z |  |
| yfinance.actions | ok | 1071 | 2026-04-30 01:17:53Z |  |
| yfinance.consensus | ok | 79 | 2026-04-30 01:17:44Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-30 01:17:31Z |  |
| yfinance.prices | ok | 7110 | 2026-04-30 01:17:27Z |  |
