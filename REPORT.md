# Invest — Top 15 report

_Generated: **2026-04-22 22:47 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T22:47:07Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.860 | 1.631 | 1.631 | 100.0% | +9.0% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.268 | 1.380 | 1.380 | 98.7% | +13.5% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.309 | 0.974 | 0.974 | 97.4% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.007 | 0.846 | 0.846 | 96.2% | +9.5% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.651 | 0.695 | 0.695 | 94.9% | +3.4% | 8 | 7 | 3 | 5 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.167 | 0.490 | 0.490 | 93.6% | +5.0% | 41 | 12 | 0 | 27 | 0 |
| 7 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.059 | 0.444 | 0.444 | 92.3% | -3.6% | 36 | 13 | 0 | 16 | 0 |
| 8 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.034 | 0.434 | 0.434 | 91.0% | +17.5% | 23 | 8 | 0 | 12 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.945 | 0.396 | 0.396 | 89.7% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **ARM** | Arm Holdings plc | Technology | 0.938 | 0.393 | 0.393 | 88.5% | -13.7% | 27 | 10 | 2 | 18 | 0 |
| 11 |  | **ANET** | Arista Networks, Inc. | Technology | 0.830 | 0.347 | 0.347 | 87.2% | -0.2% | 27 | 3 | 0 | 11 | 0 |
| 12 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.759 | 0.318 | 0.318 | 85.9% | +10.7% | 63 | 5 | 0 | 27 | 0 |
| 13 |  | **CLS** | Celestica Inc. | Technology | 0.709 | 0.296 | 0.296 | 84.6% | -1.5% | 18 | 2 | 0 | 6 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.665 | 0.278 | 0.278 | 83.3% | +3.0% | 29 | 6 | 0 | 16 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.536 | 0.223 | 0.223 | 82.1% | +17.9% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.330 | 0.921 | 0.921 | 100.0% | +13.5% | 18 | 6 | 1 | 9 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.329 | 0.920 | 0.920 | 98.7% | +9.0% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.945 | 0.767 | 0.767 | 97.4% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.733 | 0.683 | 0.683 | 96.2% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.468 | 0.578 | 0.578 | 94.9% | +47.7% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.453 | 0.572 | 0.572 | 93.6% | +50.9% | 21 | 5 | 0 | 12 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.114 | 0.438 | 0.438 | 92.3% | +35.0% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.057 | 0.415 | 0.415 | 91.0% | +56.7% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.037 | 0.407 | 0.407 | 89.7% | +39.1% | 22 | 2 | 0 | 6 | 0 |
| 10 |  | **DE** | Deere & Company | Industrials | 0.978 | 0.383 | 0.383 | 88.5% | +14.7% | 13 | 11 | 0 | 13 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.961 | 0.377 | 0.377 | 87.2% | +23.1% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.943 | 0.369 | 0.369 | 85.9% | +5.0% | 41 | 12 | 0 | 27 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.890 | 0.349 | 0.349 | 84.6% | +38.0% | 35 | 10 | 0 | 20 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.826 | 0.323 | 0.323 | 83.3% | +9.5% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.808 | 0.316 | 0.316 | 82.1% | +23.1% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.852 | 0.824 | 0.824 | 100.0% | +49.0% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.739 | 0.773 | 0.773 | 98.7% | +56.7% | 28 | 7 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.667 | 0.741 | 0.741 | 97.4% | +50.9% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.604 | 0.712 | 0.712 | 96.2% | +39.1% | 22 | 2 | 0 | 6 | 0 |
| 5 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.494 | 0.663 | 0.663 | 94.9% | +47.7% | 20 | 1 | 0 | 9 | 0 |
| 6 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.335 | 0.592 | 0.592 | 93.6% | +23.1% | 10 | 1 | 0 | 2 | 0 |
| 7 |  | **ABT** | Abbott Laboratories | Healthcare | 1.304 | 0.578 | 0.578 | 92.3% | +30.3% | 22 | 6 | 0 | 13 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.243 | 0.550 | 0.550 | 91.0% | +22.4% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.221 | 0.541 | 0.541 | 89.7% | +35.0% | 44 | 3 | 1 | 20 | 0 |
| 10 |  | **CRM** | Salesforce, Inc. | Technology | 1.194 | 0.528 | 0.528 | 88.5% | +41.7% | 35 | 10 | 1 | 24 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.151 | 0.509 | 0.509 | 87.2% | +23.1% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.066 | 0.471 | 0.471 | 85.9% | +23.0% | 20 | 2 | 0 | 3 | 0 |
| 13 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.016 | 0.448 | 0.448 | 84.6% | +38.0% | 35 | 10 | 0 | 20 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.961 | 0.423 | 0.423 | 83.3% | +24.4% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.880 | 0.387 | 0.387 | 82.1% | +29.3% | 31 | 7 | 0 | 21 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 22:47:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 22:47:02Z |  |
| stooq.prices | ok | 0 | 2026-04-22 21:50:56Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 21:50:51Z |  |
| stooq.prices | ok | 0 | 2026-04-22 20:54:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 20:54:38Z |  |
| stooq.prices | ok | 0 | 2026-04-22 19:42:14Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 19:42:09Z |  |
| stooq.prices | ok | 0 | 2026-04-22 18:06:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 18:06:02Z |  |
| stooq.prices | ok | 0 | 2026-04-22 16:59:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 16:59:04Z |  |
| stooq.prices | ok | 0 | 2026-04-22 15:44:12Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-22 15:44:01Z |  |
| stooq.prices | ok | 0 | 2026-04-22 14:13:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 14:13:25Z |  |
| stooq.prices | ok | 0 | 2026-04-22 12:11:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 12:11:19Z |  |
| stooq.prices | ok | 0 | 2026-04-22 11:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 11:05:00Z |  |
