# Invest — Top 15 report

_Generated: **2026-05-01 14:55 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T14:55:10Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AMD**, **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.385 | 1.409 | 1.409 | 100.0% | -14.6% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.747 | 1.143 | 1.143 | 98.7% | +9.1% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CLS** | Celestica Inc. | Technology | 2.012 | 0.838 | 0.838 | 97.4% | +3.0% | 19 | 1 | 0 | 10 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.906 | 0.793 | 0.793 | 96.2% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.807 | 0.752 | 0.752 | 94.9% | +4.1% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.423 | 0.592 | 0.592 | 93.6% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.004 | 0.417 | 0.417 | 92.3% | +5.2% | 62 | 5 | 0 | 32 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.999 | 0.415 | 0.415 | 91.0% | +19.6% | 23 | 8 | 0 | 12 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.994 | 0.413 | 0.413 | 89.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.822 | 0.342 | 0.342 | 88.5% | +21.6% | 18 | 2 | 0 | 3 | 0 |
| 11 |  | **AAPL** | Apple Inc. | Technology | 0.801 | 0.333 | 0.333 | 87.2% | +5.3% | 32 | 14 | 2 | 7 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.682 | 0.283 | 0.283 | 85.9% | -1.0% | 29 | 5 | 1 | 16 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.620 | 0.257 | 0.257 | 84.6% | +28.1% | 45 | 3 | 1 | 19 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.582 | 0.242 | 0.242 | 83.3% | +13.2% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.526 | 0.218 | 0.218 | 82.1% | +15.6% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.945 | 0.711 | 0.711 | 100.0% | +9.1% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.748 | 0.638 | 0.638 | 98.7% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.494 | 0.545 | 0.545 | 97.4% | +60.0% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.441 | 0.525 | 0.525 | 96.2% | +21.6% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.436 | 0.524 | 0.524 | 94.9% | +28.1% | 45 | 3 | 1 | 19 | 0 |
| 6 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.391 | 0.507 | 0.507 | 93.6% | +48.3% | 31 | 2 | 0 | 19 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.148 | 0.418 | 0.418 | 92.3% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.135 | 0.413 | 0.413 | 91.0% | +42.3% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.131 | 0.412 | 0.412 | 89.7% | +42.9% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.090 | 0.396 | 0.396 | 88.5% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.984 | 0.358 | 0.358 | 87.2% | +49.3% | 35 | 10 | 1 | 24 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.953 | 0.346 | 0.346 | 85.9% | +10.7% | 18 | 6 | 1 | 10 | 0 |
| 13 | ★★ | **CLS** | Celestica Inc. | Technology | 0.918 | 0.333 | 0.333 | 84.6% | +3.0% | 19 | 1 | 0 | 10 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.869 | 0.315 | 0.315 | 83.3% | +15.6% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.837 | 0.304 | 0.304 | 82.1% | -14.6% | 36 | 13 | 0 | 15 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.036 | 0.890 | 0.890 | 100.0% | +60.0% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.990 | 0.869 | 0.869 | 98.7% | +48.3% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.661 | 0.724 | 0.724 | 97.4% | +42.3% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.382 | 0.601 | 0.601 | 96.2% | +49.3% | 35 | 10 | 1 | 24 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.266 | 0.550 | 0.550 | 94.9% | +23.7% | 27 | 3 | 1 | 7 | 0 |
| 6 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.251 | 0.543 | 0.543 | 93.6% | +67.1% | 16 | 20 | 0 | 14 | 0 |
| 7 |  | **ABT** | Abbott Laboratories | Healthcare | 1.250 | 0.543 | 0.543 | 92.3% | +32.9% | 21 | 7 | 0 | 11 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.241 | 0.539 | 0.539 | 91.0% | +49.7% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.116 | 0.484 | 0.484 | 89.7% | +42.9% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.072 | 0.465 | 0.465 | 88.5% | +15.6% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **ACN** | Accenture plc | Technology | 1.068 | 0.463 | 0.463 | 87.2% | +40.9% | 18 | 10 | 0 | 12 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.064 | 0.461 | 0.461 | 85.9% | +20.6% | 9 | 1 | 0 | 0 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.009 | 0.437 | 0.437 | 84.6% | +19.1% | 22 | 2 | 0 | 8 | 0 |
| 14 |  | **FROG** | JFrog Ltd. | Technology | 1.009 | 0.437 | 0.437 | 83.3% | +37.8% | 20 | 1 | 0 | 9 | 0 |
| 15 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.998 | 0.432 | 0.432 | 82.1% | +21.6% | 18 | 2 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 14:55:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 14:55:01Z |  |
| stooq.prices | ok | 0 | 2026-05-01 13:47:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 13:47:50Z |  |
| stooq.prices | ok | 0 | 2026-05-01 11:59:27Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 11:59:21Z |  |
| stooq.prices | ok | 0 | 2026-05-01 10:46:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 10:46:30Z |  |
| stooq.prices | ok | 0 | 2026-05-01 09:14:02Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-05-01 09:13:57Z |  |
| stooq.prices | ok | 0 | 2026-05-01 07:16:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 07:16:31Z |  |
| stooq.prices | ok | 0 | 2026-05-01 04:32:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 04:32:36Z |  |
| edgar.13f | error | 0 | 2026-05-01 01:22:52Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-01 01:22:51Z |  |
| yfinance.actions | ok | 1106 | 2026-05-01 01:22:40Z |  |
| yfinance.consensus | ok | 79 | 2026-05-01 01:22:31Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-01 01:22:17Z |  |
| yfinance.prices | ok | 7110 | 2026-05-01 01:22:11Z |  |
