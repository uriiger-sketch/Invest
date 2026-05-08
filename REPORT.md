# Invest — Top 15 report

_Generated: **2026-05-08 00:10 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T00:10:48Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **AMZN**, **APH**, **BSX**, **CHWY**, **CI**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.589 | 1.461 | 1.461 | 100.0% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 2 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.122 | 0.669 | 0.669 | 98.7% | -6.2% | 44 | 3 | 1 | 16 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.064 | 0.650 | 0.650 | 97.4% | -23.5% | 35 | 14 | 0 | 22 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.688 | 0.529 | 0.529 | 96.2% | +11.0% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.189 | 0.369 | 0.369 | 94.9% | +14.1% | 61 | 5 | 0 | 29 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.135 | 0.352 | 0.352 | 93.6% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 1.111 | 0.344 | 0.344 | 92.3% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.851 | 0.260 | 0.260 | 91.0% | -22.1% | 10 | 4 | 0 | 11 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.798 | 0.243 | 0.243 | 89.7% | +4.3% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.752 | 0.228 | 0.228 | 88.5% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 11 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.730 | 0.222 | 0.222 | 87.2% | +17.4% | 22 | 8 | 0 | 6 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.728 | 0.221 | 0.221 | 85.9% | +6.3% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.656 | 0.198 | 0.198 | 84.6% | +18.0% | 27 | 3 | 1 | 5 | 0 |
| 14 | ★★ | **CVX** | Chevron Corporation | Energy | 0.652 | 0.197 | 0.197 | 83.3% | +17.7% | 18 | 6 | 1 | 11 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.580 | 0.173 | 0.173 | 82.1% | +11.8% | 10 | 1 | 0 | 2 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.972 | 0.683 | 0.683 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.955 | 0.677 | 0.677 | 98.7% | +6.1% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.634 | 0.564 | 0.564 | 97.4% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.555 | 0.536 | 0.536 | 96.2% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★ | **CVX** | Chevron Corporation | Energy | 1.258 | 0.432 | 0.432 | 94.9% | +17.7% | 18 | 6 | 1 | 11 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.205 | 0.413 | 0.413 | 93.6% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.116 | 0.382 | 0.382 | 92.3% | +45.0% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.075 | 0.367 | 0.367 | 91.0% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 9 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.057 | 0.361 | 0.361 | 89.7% | -2.8% | 42 | 11 | 0 | 27 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.962 | 0.328 | 0.328 | 88.5% | -6.2% | 44 | 3 | 1 | 16 | 0 |
| 11 | ★★ | **AAPL** | Apple Inc. | Technology | 0.913 | 0.310 | 0.310 | 87.2% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 12 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.903 | 0.307 | 0.307 | 85.9% | +14.1% | 61 | 5 | 0 | 29 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.900 | 0.306 | 0.306 | 84.6% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.844 | 0.286 | 0.286 | 83.3% | +19.9% | 22 | 2 | 0 | 10 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.831 | 0.282 | 0.282 | 82.1% | +14.6% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.477 | 1.099 | 1.099 | 100.0% | +73.4% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.033 | 0.899 | 0.899 | 98.7% | +50.6% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.634 | 0.721 | 0.721 | 97.4% | +42.4% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.337 | 0.588 | 0.588 | 96.2% | +36.4% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.270 | 0.558 | 0.558 | 94.9% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.235 | 0.542 | 0.542 | 93.6% | +45.0% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.175 | 0.515 | 0.515 | 92.3% | +44.0% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.139 | 0.499 | 0.499 | 91.0% | +33.0% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.120 | 0.491 | 0.491 | 89.7% | +22.6% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.042 | 0.456 | 0.456 | 88.5% | +19.9% | 22 | 2 | 0 | 10 | 0 |
| 11 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.976 | 0.426 | 0.426 | 87.2% | +24.5% | 24 | 8 | 0 | 9 | 0 |
| 12 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.975 | 0.426 | 0.426 | 85.9% | +31.0% | 30 | 7 | 0 | 24 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.966 | 0.422 | 0.422 | 84.6% | +19.3% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.941 | 0.411 | 0.411 | 83.3% | +38.3% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **ANET** | Arista Networks, Inc. | Technology | 0.925 | 0.403 | 0.403 | 82.1% | +28.4% | 27 | 2 | 0 | 13 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 00:10:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 00:10:38Z |  |
| stooq.prices | ok | 0 | 2026-05-07 23:02:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 23:02:46Z |  |
| stooq.prices | ok | 0 | 2026-05-07 21:57:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 21:57:38Z |  |
| stooq.prices | ok | 0 | 2026-05-07 20:42:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 20:42:28Z |  |
| stooq.prices | ok | 0 | 2026-05-07 19:18:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 19:18:07Z |  |
| stooq.prices | ok | 0 | 2026-05-07 17:25:53Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 17:25:47Z |  |
| stooq.prices | ok | 0 | 2026-05-07 15:40:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 15:40:14Z |  |
| stooq.prices | ok | 0 | 2026-05-07 13:05:49Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 13:05:44Z |  |
| stooq.prices | ok | 0 | 2026-05-07 11:10:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 11:10:04Z |  |
| stooq.prices | ok | 0 | 2026-05-07 08:49:50Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-07 08:49:44Z |  |
