# Invest — Top 15 report

_Generated: **2026-05-04 16:21 UTC** · Scores as of: **2026-05-04**_

🟢 last successful crawl: 0 min ago (at 2026-05-04T16:21:53Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.596 | 1.449 | 1.449 | 100.0% | +4.6% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 2.977 | 1.198 | 1.198 | 98.7% | +5.8% | 20 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.784 | 1.120 | 1.120 | 97.4% | +4.5% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.862 | 0.748 | 0.748 | 96.2% | +15.7% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.406 | 0.563 | 0.563 | 94.9% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.195 | 0.478 | 0.478 | 93.6% | +13.6% | 59 | 5 | 0 | 32 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.080 | 0.431 | 0.431 | 92.3% | +17.4% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.816 | 0.324 | 0.324 | 91.0% | +22.1% | 44 | 3 | 1 | 18 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.780 | 0.310 | 0.310 | 89.7% | +27.8% | 20 | 2 | 0 | 3 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.757 | 0.301 | 0.301 | 88.5% | +8.9% | 32 | 15 | 2 | 11 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.726 | 0.288 | 0.288 | 87.2% | -0.1% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.710 | 0.282 | 0.282 | 85.9% | +8.6% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AVGO** | Broadcom Inc. | Technology | 0.552 | 0.218 | 0.218 | 84.6% | +15.5% | 43 | 3 | 0 | 16 | 0 |
| 14 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.505 | 0.199 | 0.199 | 83.3% | +5.7% | 21 | 19 | 2 | 14 | 0 |
| 15 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.495 | 0.195 | 0.195 | 82.1% | +25.4% | 27 | 3 | 1 | 7 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.085 | 0.814 | 0.814 | 100.0% | +4.6% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.637 | 0.638 | 0.638 | 98.7% | +63.8% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.554 | 0.605 | 0.605 | 97.4% | +27.8% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.410 | 0.549 | 0.549 | 96.2% | +48.9% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★ | **CLS** | Celestica Inc. | Technology | 1.356 | 0.528 | 0.528 | 94.9% | +5.8% | 20 | 1 | 0 | 11 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.286 | 0.500 | 0.500 | 93.6% | +22.1% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.204 | 0.468 | 0.468 | 92.3% | +44.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.113 | 0.432 | 0.432 | 91.0% | +43.7% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.085 | 0.421 | 0.421 | 89.7% | +4.5% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.004 | 0.390 | 0.390 | 88.5% | +4.1% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.968 | 0.375 | 0.375 | 87.2% | +44.2% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.890 | 0.345 | 0.345 | 85.9% | +15.7% | 17 | 1 | 0 | 8 | 0 |
| 13 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.887 | 0.344 | 0.344 | 84.6% | +25.4% | 27 | 3 | 1 | 7 | 0 |
| 14 |  | **CVX** | Chevron Corporation | Energy | 0.872 | 0.338 | 0.338 | 83.3% | +11.2% | 18 | 6 | 1 | 10 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.866 | 0.335 | 0.335 | 82.1% | +19.0% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.257 | 1.026 | 1.026 | 100.0% | +63.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.049 | 0.931 | 0.931 | 98.7% | +48.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.770 | 0.803 | 0.803 | 97.4% | +44.7% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.322 | 0.598 | 0.598 | 96.2% | +34.6% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.296 | 0.587 | 0.587 | 94.9% | +44.2% | 34 | 8 | 1 | 24 | 0 |
| 6 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.284 | 0.581 | 0.581 | 93.6% | +48.7% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.260 | 0.570 | 0.570 | 92.3% | +27.8% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.230 | 0.556 | 0.556 | 91.0% | +43.7% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.152 | 0.521 | 0.521 | 89.7% | +19.0% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.113 | 0.503 | 0.503 | 88.5% | +35.2% | 30 | 7 | 0 | 27 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.084 | 0.490 | 0.490 | 87.2% | +21.9% | 9 | 1 | 0 | 0 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.079 | 0.487 | 0.487 | 85.9% | +21.5% | 22 | 2 | 0 | 10 | 0 |
| 13 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.066 | 0.481 | 0.481 | 84.6% | +25.4% | 27 | 3 | 1 | 7 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.054 | 0.476 | 0.476 | 83.3% | +39.1% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.958 | 0.432 | 0.432 | 82.1% | +20.2% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-04 16:21:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 16:21:37Z |  |
| stooq.prices | ok | 0 | 2026-05-04 14:34:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 14:34:16Z |  |
| stooq.prices | ok | 0 | 2026-05-04 12:07:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 12:07:23Z |  |
| stooq.prices | ok | 0 | 2026-05-04 10:13:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 10:13:35Z |  |
| stooq.prices | ok | 0 | 2026-05-04 07:47:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 07:47:19Z |  |
| stooq.prices | ok | 0 | 2026-05-04 04:52:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 04:52:38Z |  |
| stooq.prices | ok | 0 | 2026-05-04 01:19:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 01:19:18Z |  |
| edgar.13f | error | 0 | 2026-05-04 00:13:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-04 00:13:26Z |  |
| yfinance.actions | ok | 1123 | 2026-05-04 00:13:18Z |  |
| yfinance.consensus | ok | 79 | 2026-05-04 00:13:07Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-04 00:12:48Z |  |
| yfinance.prices | ok | 7110 | 2026-05-04 00:12:41Z |  |
