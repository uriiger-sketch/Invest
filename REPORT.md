# Invest — Top 15 report

_Generated: **2026-05-01 07:16 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T07:16:38Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.383 | 1.393 | 1.393 | 100.0% | -15.2% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.769 | 1.140 | 1.140 | 98.7% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CLS** | Celestica Inc. | Technology | 2.039 | 0.840 | 0.840 | 97.4% | +4.5% | 19 | 1 | 0 | 10 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.921 | 0.791 | 0.791 | 96.2% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.920 | 0.790 | 0.790 | 94.9% | +3.3% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.402 | 0.577 | 0.577 | 93.6% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.994 | 0.409 | 0.409 | 92.3% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.962 | 0.396 | 0.396 | 91.0% | +7.1% | 62 | 5 | 0 | 32 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.890 | 0.366 | 0.366 | 89.7% | +20.6% | 18 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.827 | 0.340 | 0.340 | 88.5% | +23.0% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.749 | 0.308 | 0.308 | 87.2% | -2.3% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.710 | 0.292 | 0.292 | 85.9% | +10.0% | 32 | 14 | 2 | 7 | 0 |
| 13 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.578 | 0.237 | 0.237 | 84.6% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.572 | 0.235 | 0.235 | 83.3% | +13.9% | 44 | 3 | 0 | 16 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.535 | 0.220 | 0.220 | 82.1% | +17.7% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.000 | 0.722 | 0.722 | 100.0% | +10.3% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.736 | 0.626 | 0.626 | 98.7% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.535 | 0.553 | 0.553 | 97.4% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.443 | 0.520 | 0.520 | 96.2% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **CRH** | CRH plc | Basic Materials | 1.439 | 0.519 | 0.519 | 94.9% | +20.6% | 18 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.210 | 0.435 | 0.435 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.136 | 0.408 | 0.408 | 92.3% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.131 | 0.406 | 0.406 | 91.0% | +20.3% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.121 | 0.403 | 0.403 | 89.7% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.066 | 0.383 | 0.383 | 88.5% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.013 | 0.364 | 0.364 | 87.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★ | **CLS** | Celestica Inc. | Technology | 0.973 | 0.349 | 0.349 | 85.9% | +4.5% | 19 | 1 | 0 | 10 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.922 | 0.331 | 0.331 | 84.6% | +10.0% | 32 | 14 | 2 | 7 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.910 | 0.326 | 0.326 | 83.3% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.875 | 0.313 | 0.313 | 82.1% | +9.8% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.999 | 0.873 | 0.873 | 100.0% | +60.5% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.764 | 0.769 | 0.769 | 98.7% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.517 | 0.660 | 0.660 | 97.4% | +39.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.448 | 0.629 | 0.629 | 96.2% | +52.6% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.327 | 0.576 | 0.576 | 94.9% | +71.8% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.294 | 0.562 | 0.562 | 93.6% | +48.8% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **FROG** | JFrog Ltd. | Technology | 1.267 | 0.550 | 0.550 | 92.3% | +46.0% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.234 | 0.535 | 0.535 | 91.0% | +23.6% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.166 | 0.505 | 0.505 | 89.7% | +49.5% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.141 | 0.494 | 0.494 | 88.5% | +33.9% | 45 | 3 | 1 | 19 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.135 | 0.492 | 0.492 | 87.2% | +30.7% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.078 | 0.466 | 0.466 | 85.9% | +16.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.014 | 0.438 | 0.438 | 84.6% | +33.6% | 31 | 7 | 0 | 27 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.005 | 0.434 | 0.434 | 83.3% | +40.2% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.994 | 0.429 | 0.429 | 82.1% | +19.5% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-01 00:10:18Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 00:10:13Z |  |
| stooq.prices | ok | 0 | 2026-04-30 23:14:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 23:14:11Z |  |
| stooq.prices | ok | 0 | 2026-04-30 22:04:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 22:04:24Z |  |
| stooq.prices | ok | 0 | 2026-04-30 21:00:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 21:00:00Z |  |
| stooq.prices | ok | 0 | 2026-04-30 19:52:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 19:52:35Z |  |
