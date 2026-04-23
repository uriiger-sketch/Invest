# Invest — Top 15 report

_Generated: **2026-04-23 14:05 UTC** · Scores as of: **2026-04-23**_

🟢 last successful crawl: 0 min ago (at 2026-04-23T14:05:13Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.898 | 1.609 | 1.609 | 100.0% | +8.7% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.288 | 1.356 | 1.356 | 98.7% | +13.2% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.194 | 0.903 | 0.903 | 97.4% | +11.8% | 16 | 1 | 0 | 7 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.901 | 0.781 | 0.781 | 96.2% | +10.2% | 41 | 12 | 0 | 27 | 0 |
| 5 |  | **ARM** | Arm Holdings plc | Technology | 1.191 | 0.487 | 0.487 | 94.9% | -14.9% | 27 | 10 | 2 | 18 | 0 |
| 6 |  | **ANET** | Arista Networks, Inc. | Technology | 1.079 | 0.441 | 0.441 | 93.6% | +1.0% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.991 | 0.404 | 0.404 | 92.3% | -3.6% | 36 | 13 | 0 | 16 | 0 |
| 8 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.976 | 0.398 | 0.398 | 91.0% | +3.2% | 20 | 21 | 2 | 14 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.972 | 0.397 | 0.397 | 89.7% | +23.1% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.961 | 0.392 | 0.392 | 88.5% | +23.2% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.864 | 0.352 | 0.352 | 87.2% | +10.8% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ADI** | Analog Devices, Inc. | Technology | 0.758 | 0.308 | 0.308 | 85.9% | -2.4% | 29 | 6 | 0 | 16 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.700 | 0.284 | 0.284 | 84.6% | +22.9% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.526 | 0.212 | 0.212 | 83.3% | -2.4% | 18 | 2 | 0 | 6 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.522 | 0.210 | 0.210 | 82.1% | +17.7% | 21 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.290 | 0.870 | 0.870 | 100.0% | +8.7% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.274 | 0.863 | 0.863 | 98.7% | +13.2% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.673 | 0.634 | 0.634 | 97.4% | +23.1% | 27 | 3 | 1 | 7 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.533 | 0.580 | 0.580 | 96.2% | +56.2% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.528 | 0.578 | 0.578 | 94.9% | +10.2% | 41 | 12 | 0 | 27 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.444 | 0.546 | 0.546 | 93.6% | +57.6% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.301 | 0.492 | 0.492 | 92.3% | +42.9% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.260 | 0.476 | 0.476 | 91.0% | +22.9% | 20 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.047 | 0.394 | 0.394 | 89.7% | +45.1% | 22 | 2 | 0 | 9 | 0 |
| 10 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.972 | 0.366 | 0.366 | 88.5% | +57.3% | 28 | 7 | 0 | 22 | 0 |
| 11 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.955 | 0.359 | 0.359 | 87.2% | +11.8% | 16 | 1 | 0 | 7 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.933 | 0.351 | 0.351 | 85.9% | +43.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.918 | 0.345 | 0.345 | 84.6% | +21.9% | 10 | 1 | 0 | 2 | 0 |
| 14 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.891 | 0.335 | 0.335 | 83.3% | +55.3% | 35 | 10 | 1 | 24 | 0 |
| 15 |  | **DE** | Deere & Company | Industrials | 0.827 | 0.310 | 0.310 | 82.1% | +13.6% | 13 | 11 | 0 | 13 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.754 | 0.752 | 0.752 | 100.0% | +57.6% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.706 | 0.731 | 0.731 | 98.7% | +45.1% | 22 | 2 | 0 | 9 | 0 |
| 3 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.671 | 0.715 | 0.715 | 97.4% | +56.2% | 20 | 1 | 0 | 9 | 0 |
| 4 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.572 | 0.673 | 0.673 | 96.2% | +45.5% | 32 | 1 | 0 | 19 | 0 |
| 5 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.569 | 0.672 | 0.672 | 94.9% | +57.3% | 28 | 7 | 0 | 22 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.468 | 0.628 | 0.628 | 93.6% | +55.3% | 35 | 10 | 1 | 24 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.376 | 0.588 | 0.588 | 92.3% | +42.9% | 44 | 3 | 1 | 19 | 0 |
| 8 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.259 | 0.537 | 0.537 | 91.0% | +21.9% | 10 | 1 | 0 | 2 | 0 |
| 9 |  | **ABT** | Abbott Laboratories | Healthcare | 1.210 | 0.516 | 0.516 | 89.7% | +29.9% | 22 | 6 | 0 | 13 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.189 | 0.507 | 0.507 | 88.5% | +23.1% | 27 | 3 | 1 | 7 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.092 | 0.465 | 0.465 | 87.2% | +22.1% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.056 | 0.449 | 0.449 | 85.9% | +43.1% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.046 | 0.445 | 0.445 | 84.6% | +22.9% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.975 | 0.415 | 0.415 | 83.3% | +42.1% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.874 | 0.371 | 0.371 | 82.1% | +23.6% | 23 | 9 | 0 | 11 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-23 14:05:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 14:05:06Z |  |
| stooq.prices | ok | 0 | 2026-04-23 11:59:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 11:59:16Z |  |
| stooq.prices | ok | 0 | 2026-04-23 10:51:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 10:50:57Z |  |
| stooq.prices | ok | 0 | 2026-04-23 09:07:15Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 09:07:09Z |  |
| stooq.prices | ok | 0 | 2026-04-23 07:12:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 07:11:59Z |  |
| stooq.prices | ok | 0 | 2026-04-23 05:17:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 05:17:45Z |  |
| stooq.prices | ok | 0 | 2026-04-23 02:33:16Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-23 02:33:09Z |  |
| edgar.13f | error | 0 | 2026-04-23 00:12:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-23 00:12:25Z |  |
| yfinance.actions | ok | 1040 | 2026-04-23 00:12:16Z |  |
| yfinance.consensus | ok | 79 | 2026-04-23 00:12:02Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-23 00:11:42Z |  |
| yfinance.prices | ok | 7110 | 2026-04-23 00:11:33Z |  |
