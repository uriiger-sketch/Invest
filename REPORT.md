# Invest — Top 15 report

_Generated: **2026-05-01 17:00 UTC** · Scores as of: **2026-05-01**_

🟢 last successful crawl: 0 min ago (at 2026-05-01T17:00:27Z)

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.435 | 1.419 | 1.419 | 100.0% | -16.2% | 36 | 13 | 0 | 15 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.782 | 1.149 | 1.149 | 98.7% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.018 | 0.833 | 0.833 | 97.4% | +16.3% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CLS** | Celestica Inc. | Technology | 1.994 | 0.823 | 0.823 | 96.2% | +2.7% | 19 | 1 | 0 | 10 | 0 |
| 5 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.796 | 0.742 | 0.742 | 94.9% | +4.1% | 14 | 8 | 0 | 9 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.404 | 0.579 | 0.579 | 93.6% | +2.4% | 27 | 3 | 0 | 11 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.998 | 0.411 | 0.411 | 92.3% | +23.8% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.979 | 0.403 | 0.403 | 91.0% | +19.0% | 23 | 8 | 0 | 12 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.965 | 0.398 | 0.398 | 89.7% | +5.8% | 62 | 5 | 0 | 32 | 0 |
| 10 | ★★ | **AAPL** | Apple Inc. | Technology | 0.798 | 0.329 | 0.329 | 88.5% | +5.4% | 32 | 14 | 2 | 7 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.787 | 0.324 | 0.324 | 87.2% | +22.9% | 18 | 2 | 0 | 3 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.655 | 0.270 | 0.270 | 85.9% | +26.0% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.653 | 0.269 | 0.269 | 84.6% | -0.7% | 29 | 5 | 1 | 16 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.552 | 0.227 | 0.227 | 83.3% | +13.1% | 44 | 3 | 0 | 16 | 0 |
| 15 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.512 | 0.211 | 0.211 | 82.1% | +16.1% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.927 | 0.706 | 0.706 | 100.0% | +8.1% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.749 | 0.640 | 0.640 | 98.7% | +23.8% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.531 | 0.560 | 0.560 | 97.4% | +61.2% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.460 | 0.534 | 0.534 | 96.2% | +22.9% | 18 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.410 | 0.516 | 0.516 | 94.9% | +48.7% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.392 | 0.509 | 0.509 | 93.6% | +26.0% | 45 | 3 | 1 | 19 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.159 | 0.423 | 0.423 | 92.3% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.134 | 0.414 | 0.414 | 91.0% | +43.1% | 36 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.084 | 0.396 | 0.396 | 89.7% | +16.3% | 16 | 1 | 0 | 7 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.070 | 0.390 | 0.390 | 88.5% | +2.4% | 27 | 3 | 0 | 11 | 0 |
| 11 |  | **CVX** | Chevron Corporation | Energy | 0.972 | 0.355 | 0.355 | 87.2% | +11.6% | 18 | 6 | 1 | 10 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.951 | 0.347 | 0.347 | 85.9% | +47.4% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **CLS** | Celestica Inc. | Technology | 0.897 | 0.327 | 0.327 | 84.6% | +2.7% | 19 | 1 | 0 | 10 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.880 | 0.321 | 0.321 | 83.3% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.825 | 0.300 | 0.300 | 82.1% | +5.4% | 32 | 14 | 2 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.069 | 0.914 | 0.914 | 100.0% | +61.2% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.991 | 0.879 | 0.879 | 98.7% | +48.7% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.675 | 0.739 | 0.739 | 97.4% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.303 | 0.573 | 0.573 | 96.2% | +47.4% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.265 | 0.556 | 0.556 | 94.9% | +50.5% | 28 | 7 | 0 | 22 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.262 | 0.555 | 0.555 | 93.6% | +23.8% | 27 | 3 | 1 | 7 | 0 |
| 7 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.253 | 0.551 | 0.551 | 92.3% | +67.4% | 16 | 20 | 0 | 14 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.207 | 0.530 | 0.530 | 91.0% | +32.0% | 21 | 7 | 0 | 11 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.123 | 0.493 | 0.493 | 89.7% | +43.1% | 36 | 10 | 0 | 21 | 0 |
| 10 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.091 | 0.479 | 0.479 | 88.5% | +16.1% | 10 | 1 | 0 | 2 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.082 | 0.475 | 0.475 | 87.2% | +21.3% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.044 | 0.458 | 0.458 | 85.9% | +22.9% | 18 | 2 | 0 | 3 | 0 |
| 13 |  | **CI** | The Cigna Group | Healthcare | 1.019 | 0.447 | 0.447 | 84.6% | +19.5% | 22 | 2 | 0 | 8 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.015 | 0.445 | 0.445 | 83.3% | +39.6% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.988 | 0.433 | 0.433 | 82.1% | +32.4% | 31 | 7 | 0 | 27 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-01 17:00:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 17:00:20Z |  |
| stooq.prices | ok | 0 | 2026-05-01 15:57:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-01 15:57:17Z |  |
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
