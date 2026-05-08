# Invest — Top 15 report

_Generated: **2026-05-08 17:16 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T17:16:55Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BSX**, **BUD**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.733 | 1.717 | 1.717 | 100.0% | -2.3% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.119 | 1.493 | 1.493 | 98.7% | +3.3% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.932 | 0.695 | 0.695 | 97.4% | -7.9% | 44 | 3 | 1 | 16 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.239 | 0.442 | 0.442 | 96.2% | -5.4% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.177 | 0.420 | 0.420 | 94.9% | +7.5% | 10 | 4 | 0 | 11 | 0 |
| 6 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.172 | 0.418 | 0.418 | 93.6% | +11.6% | 17 | 1 | 0 | 8 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.867 | 0.307 | 0.307 | 92.3% | +3.8% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.690 | 0.242 | 0.242 | 91.0% | +13.8% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.641 | 0.224 | 0.224 | 89.7% | +4.0% | 23 | 3 | 0 | 8 | 0 |
| 10 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.603 | 0.210 | 0.210 | 88.5% | +3.5% | 14 | 8 | 0 | 9 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.557 | 0.194 | 0.194 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.551 | 0.192 | 0.192 | 85.9% | +26.3% | 21 | 2 | 0 | 3 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.549 | 0.191 | 0.191 | 84.6% | -5.5% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.437 | 0.150 | 0.150 | 83.3% | +19.4% | 27 | 3 | 1 | 6 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.381 | 0.129 | 0.129 | 82.1% | +15.4% | 10 | 1 | 0 | 3 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.021 | 0.722 | 0.722 | 100.0% | +80.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.872 | 0.668 | 0.668 | 98.7% | +3.3% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.598 | 0.569 | 0.569 | 97.4% | -2.3% | 40 | 10 | 0 | 22 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.582 | 0.563 | 0.563 | 96.2% | +56.4% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.496 | 0.532 | 0.532 | 94.9% | +26.3% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.201 | 0.425 | 0.425 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.181 | 0.418 | 0.418 | 92.3% | +51.4% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.176 | 0.416 | 0.416 | 91.0% | +44.8% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.087 | 0.384 | 0.384 | 89.7% | +47.9% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.054 | 0.372 | 0.372 | 88.5% | -5.4% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.907 | 0.319 | 0.319 | 87.2% | -7.9% | 44 | 3 | 1 | 16 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 0.894 | 0.314 | 0.314 | 85.9% | +39.0% | 15 | 3 | 0 | 7 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.843 | 0.296 | 0.296 | 84.6% | +39.9% | 21 | 7 | 0 | 11 | 0 |
| 14 | ★★ | **AAPL** | Apple Inc. | Technology | 0.772 | 0.270 | 0.270 | 83.3% | +3.8% | 31 | 15 | 2 | 11 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.771 | 0.270 | 0.270 | 82.1% | +15.6% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.602 | 1.159 | 1.159 | 100.0% | +80.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.120 | 0.942 | 0.942 | 98.7% | +56.4% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.629 | 0.722 | 0.722 | 97.4% | +44.8% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.383 | 0.611 | 0.611 | 96.2% | +51.4% | 35 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.380 | 0.610 | 0.610 | 94.9% | +39.9% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **APH** | Amphenol Corporation | Technology | 1.290 | 0.570 | 0.570 | 93.6% | +39.0% | 15 | 3 | 0 | 7 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.246 | 0.549 | 0.549 | 92.3% | +47.9% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.222 | 0.539 | 0.539 | 91.0% | +26.3% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.091 | 0.480 | 0.480 | 89.7% | +22.5% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **ANET** | Arista Networks, Inc. | Technology | 1.070 | 0.471 | 0.471 | 88.5% | +34.1% | 26 | 2 | 0 | 13 | 0 |
| 11 |  | **BAC** | Bank of America Corporation | Financial Services | 1.049 | 0.461 | 0.461 | 87.2% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 12 |  | **CI** | The Cigna Group | Healthcare | 0.983 | 0.431 | 0.431 | 85.9% | +19.3% | 22 | 2 | 0 | 10 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.971 | 0.426 | 0.426 | 84.6% | +25.8% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.953 | 0.418 | 0.418 | 83.3% | +32.3% | 30 | 7 | 0 | 24 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.938 | 0.411 | 0.411 | 82.1% | +15.4% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 17:16:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 17:16:46Z |  |
| stooq.prices | ok | 0 | 2026-05-08 15:56:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 15:55:59Z |  |
| stooq.prices | ok | 0 | 2026-05-08 14:19:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 14:19:46Z |  |
| stooq.prices | ok | 0 | 2026-05-08 12:08:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 12:08:10Z |  |
| stooq.prices | ok | 0 | 2026-05-08 10:52:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 10:51:58Z |  |
| stooq.prices | ok | 0 | 2026-05-08 09:19:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 09:19:54Z |  |
| stooq.prices | ok | 0 | 2026-05-08 07:48:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 07:48:20Z |  |
| stooq.prices | ok | 0 | 2026-05-08 05:57:56Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 05:57:51Z |  |
| stooq.prices | ok | 0 | 2026-05-08 03:56:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 03:56:32Z |  |
| edgar.13f | error | 0 | 2026-05-08 01:20:06Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-08 01:20:05Z |  |
