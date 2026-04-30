# Invest — Top 15 report

_Generated: **2026-04-30 04:07 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T04:07:46Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.817 | 1.153 | 1.153 | 100.0% | -10.8% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.176 | 0.890 | 0.890 | 98.7% | +19.1% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.957 | 0.800 | 0.800 | 97.4% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.473 | 0.601 | 0.601 | 96.2% | +6.6% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.360 | 0.555 | 0.555 | 94.9% | +13.6% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.278 | 0.521 | 0.521 | 93.6% | +3.3% | 14 | 8 | 0 | 10 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.028 | 0.419 | 0.419 | 92.3% | +8.0% | 62 | 5 | 0 | 27 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.026 | 0.418 | 0.418 | 91.0% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.997 | 0.406 | 0.406 | 89.7% | +24.6% | 23 | 8 | 0 | 12 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.889 | 0.361 | 0.361 | 88.5% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **APH** | Amphenol Corporation | Technology | 0.840 | 0.341 | 0.341 | 87.2% | +14.4% | 14 | 3 | 1 | 3 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.797 | 0.324 | 0.324 | 85.9% | +10.3% | 31 | 14 | 2 | 13 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.784 | 0.318 | 0.318 | 84.6% | +1.0% | 29 | 5 | 1 | 16 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.629 | 0.255 | 0.255 | 83.3% | +15.7% | 22 | 2 | 0 | 8 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.626 | 0.254 | 0.254 | 82.1% | +17.3% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.737 | 0.658 | 0.658 | 100.0% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.496 | 0.566 | 0.566 | 98.7% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.450 | 0.548 | 0.548 | 97.4% | +57.2% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.438 | 0.544 | 0.544 | 96.2% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.412 | 0.534 | 0.534 | 94.9% | +8.7% | 42 | 11 | 0 | 27 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.210 | 0.456 | 0.456 | 93.6% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.179 | 0.445 | 0.445 | 92.3% | +49.1% | 31 | 2 | 0 | 19 | 0 |
| 8 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.124 | 0.424 | 0.424 | 91.0% | +19.1% | 16 | 1 | 0 | 7 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.098 | 0.414 | 0.414 | 89.7% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.097 | 0.413 | 0.413 | 88.5% | +6.6% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.952 | 0.358 | 0.358 | 87.2% | +20.7% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.945 | 0.355 | 0.355 | 85.9% | +48.6% | 35 | 10 | 1 | 24 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.892 | 0.335 | 0.335 | 84.6% | +46.5% | 20 | 1 | 0 | 9 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.873 | 0.328 | 0.328 | 83.3% | +10.3% | 31 | 14 | 2 | 13 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.870 | 0.327 | 0.327 | 82.1% | +18.8% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.936 | 0.848 | 0.848 | 100.0% | +57.2% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.870 | 0.819 | 0.819 | 98.7% | +49.1% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.534 | 0.670 | 0.670 | 97.4% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.347 | 0.587 | 0.587 | 96.2% | +48.6% | 35 | 10 | 1 | 24 | 0 |
| 5 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.340 | 0.584 | 0.584 | 94.9% | +26.6% | 27 | 3 | 1 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.332 | 0.580 | 0.580 | 93.6% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.280 | 0.557 | 0.557 | 92.3% | +46.5% | 20 | 1 | 0 | 9 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.270 | 0.553 | 0.553 | 91.0% | +50.7% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.228 | 0.534 | 0.534 | 89.7% | +20.7% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.129 | 0.491 | 0.491 | 88.5% | +26.0% | 19 | 2 | 0 | 3 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.111 | 0.483 | 0.483 | 87.2% | +29.9% | 21 | 7 | 0 | 11 | 0 |
| 12 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.070 | 0.464 | 0.464 | 85.9% | +32.1% | 45 | 3 | 1 | 19 | 0 |
| 13 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.018 | 0.441 | 0.441 | 84.6% | +20.9% | 9 | 1 | 0 | 0 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.951 | 0.412 | 0.412 | 83.3% | +39.0% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **APP** | AppLovin Corporation | Communication Servic | 0.902 | 0.390 | 0.390 | 82.1% | +44.2% | 26 | 4 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 04:07:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 04:07:41Z |  |
| edgar.13f | error | 0 | 2026-04-30 01:18:07Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-30 01:18:07Z |  |
| yfinance.actions | ok | 1071 | 2026-04-30 01:17:53Z |  |
| yfinance.consensus | ok | 79 | 2026-04-30 01:17:44Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-30 01:17:31Z |  |
| yfinance.prices | ok | 7110 | 2026-04-30 01:17:27Z |  |
| stooq.prices | ok | 0 | 2026-04-30 00:10:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 00:10:48Z |  |
| stooq.prices | ok | 0 | 2026-04-29 23:13:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 23:13:33Z |  |
| stooq.prices | ok | 0 | 2026-04-29 22:13:28Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 22:13:20Z |  |
| stooq.prices | ok | 0 | 2026-04-29 21:07:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 21:07:12Z |  |
| stooq.prices | ok | 0 | 2026-04-29 19:56:36Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 19:56:30Z |  |
| stooq.prices | ok | 0 | 2026-04-29 18:14:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-29 18:14:45Z |  |
