# Invest — Top 15 report

_Generated: **2026-05-04 14:34 UTC** · Scores as of: **2026-05-04**_

🟢 last successful crawl: 0 min ago (at 2026-05-04T14:34:23Z)

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.586 | 1.435 | 1.435 | 100.0% | +4.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 2.909 | 1.163 | 1.163 | 98.7% | +6.9% | 20 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.773 | 1.108 | 1.108 | 97.4% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.843 | 0.735 | 0.735 | 96.2% | +15.3% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.429 | 0.568 | 0.568 | 94.9% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.195 | 0.474 | 0.474 | 93.6% | +12.8% | 59 | 5 | 0 | 32 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.105 | 0.438 | 0.438 | 92.3% | +16.0% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.826 | 0.326 | 0.326 | 91.0% | +25.6% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.810 | 0.320 | 0.320 | 89.7% | +21.4% | 44 | 3 | 1 | 18 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.740 | 0.292 | 0.292 | 88.5% | +8.8% | 32 | 15 | 2 | 11 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.734 | 0.289 | 0.289 | 87.2% | -1.0% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.682 | 0.268 | 0.268 | 85.9% | +8.6% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AVGO** | Broadcom Inc. | Technology | 0.568 | 0.223 | 0.223 | 84.6% | +14.3% | 43 | 3 | 0 | 16 | 0 |
| 14 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.509 | 0.199 | 0.199 | 83.3% | +4.8% | 21 | 19 | 2 | 14 | 0 |
| 15 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.498 | 0.194 | 0.194 | 82.1% | +24.5% | 27 | 3 | 1 | 7 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.080 | 0.816 | 0.816 | 100.0% | +4.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.630 | 0.639 | 0.639 | 98.7% | +60.8% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.538 | 0.602 | 0.602 | 97.4% | +25.6% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.433 | 0.561 | 0.561 | 96.2% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★ | **CLS** | Celestica Inc. | Technology | 1.365 | 0.534 | 0.534 | 94.9% | +6.9% | 20 | 1 | 0 | 11 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.290 | 0.504 | 0.504 | 93.6% | +21.4% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.209 | 0.473 | 0.473 | 92.3% | +42.9% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.111 | 0.434 | 0.434 | 91.0% | +41.6% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.081 | 0.422 | 0.422 | 89.7% | +4.4% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.984 | 0.384 | 0.384 | 88.5% | +2.8% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.970 | 0.378 | 0.378 | 87.2% | +42.5% | 34 | 8 | 1 | 24 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.895 | 0.349 | 0.349 | 85.9% | +11.9% | 18 | 6 | 1 | 10 | 0 |
| 13 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.894 | 0.348 | 0.348 | 84.6% | +24.5% | 27 | 3 | 1 | 7 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.890 | 0.347 | 0.347 | 83.3% | +15.3% | 17 | 1 | 0 | 8 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.865 | 0.337 | 0.337 | 82.1% | +17.9% | 10 | 1 | 0 | 2 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.222 | 1.016 | 1.016 | 100.0% | +60.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.072 | 0.947 | 0.947 | 98.7% | +47.9% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.763 | 0.805 | 0.805 | 97.4% | +42.9% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.310 | 0.597 | 0.597 | 96.2% | +33.0% | 21 | 7 | 0 | 11 | 0 |
| 5 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.289 | 0.587 | 0.587 | 94.9% | +47.2% | 28 | 7 | 0 | 22 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.286 | 0.586 | 0.586 | 93.6% | +42.5% | 34 | 8 | 1 | 24 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.220 | 0.555 | 0.555 | 92.3% | +25.6% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.208 | 0.550 | 0.550 | 91.0% | +41.6% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.145 | 0.521 | 0.521 | 89.7% | +17.9% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.093 | 0.497 | 0.497 | 88.5% | +21.1% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.074 | 0.488 | 0.488 | 87.2% | +24.5% | 27 | 3 | 1 | 7 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 1.073 | 0.488 | 0.488 | 85.9% | +20.4% | 22 | 2 | 0 | 10 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.056 | 0.480 | 0.480 | 84.6% | +32.4% | 30 | 7 | 0 | 27 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.035 | 0.470 | 0.470 | 83.3% | +37.1% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.969 | 0.440 | 0.440 | 82.1% | +19.5% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-03 23:28:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-03 23:28:41Z |  |
