# Invest — Top 15 report

_Generated: **2026-04-22 15:44 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T15:44:13Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BAC**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.835 | 1.633 | 1.633 | 100.0% | +9.1% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.243 | 1.380 | 1.380 | 98.7% | +12.8% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.336 | 0.993 | 0.993 | 97.4% | +22.0% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.023 | 0.859 | 0.859 | 96.2% | +11.0% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.643 | 0.697 | 0.697 | 94.9% | +3.4% | 8 | 7 | 3 | 5 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.132 | 0.479 | 0.479 | 93.6% | +6.2% | 41 | 12 | 0 | 27 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.076 | 0.455 | 0.455 | 92.3% | +17.8% | 23 | 8 | 0 | 12 | 0 |
| 8 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.007 | 0.426 | 0.426 | 91.0% | -1.4% | 36 | 13 | 0 | 16 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.940 | 0.397 | 0.397 | 89.7% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ARM** | Arm Holdings plc | Technology | 0.875 | 0.369 | 0.369 | 88.5% | -11.3% | 27 | 10 | 2 | 18 | 0 |
| 11 |  | **ANET** | Arista Networks, Inc. | Technology | 0.783 | 0.330 | 0.330 | 87.2% | +1.7% | 27 | 3 | 0 | 11 | 0 |
| 12 |  | **CLS** | Celestica Inc. | Technology | 0.766 | 0.323 | 0.323 | 85.9% | -1.6% | 18 | 2 | 0 | 6 | 0 |
| 13 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.736 | 0.310 | 0.310 | 84.6% | +12.0% | 63 | 5 | 0 | 27 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.661 | 0.278 | 0.278 | 83.3% | +3.7% | 29 | 6 | 0 | 16 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.557 | 0.233 | 0.233 | 82.1% | +17.6% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.323 | 0.919 | 0.919 | 100.0% | +9.1% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.300 | 0.910 | 0.910 | 98.7% | +12.8% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.929 | 0.762 | 0.762 | 97.4% | +22.0% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.731 | 0.684 | 0.684 | 96.2% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.502 | 0.593 | 0.593 | 94.9% | +53.4% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.493 | 0.589 | 0.589 | 93.6% | +48.9% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.146 | 0.451 | 0.451 | 92.3% | +36.9% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.039 | 0.408 | 0.408 | 91.0% | +55.9% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.996 | 0.391 | 0.391 | 89.7% | +36.4% | 22 | 2 | 0 | 6 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.955 | 0.375 | 0.375 | 88.5% | +6.2% | 41 | 12 | 0 | 27 | 0 |
| 11 |  | **DE** | Deere & Company | Industrials | 0.954 | 0.375 | 0.375 | 87.2% | +13.7% | 13 | 11 | 0 | 13 | 0 |
| 12 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.945 | 0.371 | 0.371 | 85.9% | +22.2% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.919 | 0.360 | 0.360 | 84.6% | +39.4% | 35 | 10 | 0 | 20 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.869 | 0.341 | 0.341 | 83.3% | +11.0% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.780 | 0.305 | 0.305 | 82.1% | +21.6% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.878 | 0.830 | 0.830 | 100.0% | +49.2% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.773 | 0.783 | 0.783 | 98.7% | +53.4% | 21 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.726 | 0.762 | 0.762 | 97.4% | +55.9% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.548 | 0.683 | 0.683 | 96.2% | +48.9% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.518 | 0.670 | 0.670 | 94.9% | +36.4% | 22 | 2 | 0 | 6 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.303 | 0.574 | 0.574 | 93.6% | +36.9% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.302 | 0.573 | 0.573 | 92.3% | +22.2% | 10 | 1 | 0 | 2 | 0 |
| 8 |  | **ABT** | Abbott Laboratories | Healthcare | 1.277 | 0.562 | 0.562 | 91.0% | +29.4% | 22 | 6 | 0 | 13 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.250 | 0.550 | 0.550 | 89.7% | +22.6% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.176 | 0.517 | 0.517 | 88.5% | +41.0% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.085 | 0.477 | 0.477 | 87.2% | +21.6% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.074 | 0.471 | 0.471 | 85.9% | +39.4% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.023 | 0.449 | 0.449 | 84.6% | +22.0% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.904 | 0.396 | 0.396 | 83.3% | +22.9% | 23 | 9 | 0 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.857 | 0.375 | 0.375 | 82.1% | +17.6% | 21 | 3 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 15:44:12Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-22 15:44:01Z |  |
| stooq.prices | ok | 0 | 2026-04-22 14:13:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 14:13:25Z |  |
| stooq.prices | ok | 0 | 2026-04-22 12:11:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 12:11:19Z |  |
| stooq.prices | ok | 0 | 2026-04-22 11:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 11:05:00Z |  |
| stooq.prices | ok | 0 | 2026-04-22 09:55:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 09:55:54Z |  |
| stooq.prices | ok | 0 | 2026-04-22 08:03:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 08:03:07Z |  |
| stooq.prices | ok | 0 | 2026-04-22 05:59:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 05:59:51Z |  |
| stooq.prices | ok | 0 | 2026-04-22 03:44:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 03:44:42Z |  |
| stooq.prices | ok | 0 | 2026-04-22 00:06:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 00:06:30Z |  |
| edgar.13f | error | 0 | 2026-04-22 00:04:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-22 00:04:22Z |  |
