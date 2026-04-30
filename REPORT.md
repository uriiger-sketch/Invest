# Invest — Top 15 report

_Generated: **2026-04-30 19:52 UTC** · Scores as of: **2026-04-30**_

🟢 last successful crawl: 0 min ago (at 2026-04-30T19:52:42Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ANET**, **APH**, **BSX**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**

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
| 1 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 3.079 | 1.285 | 1.285 | 100.0% | -15.0% | 36 | 13 | 0 | 16 | 0 |
| 2 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.949 | 0.811 | 0.811 | 98.7% | +21.4% | 16 | 1 | 0 | 7 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.880 | 0.783 | 0.783 | 97.4% | +10.5% | 42 | 11 | 0 | 27 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.468 | 0.610 | 0.610 | 96.2% | +4.0% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **CLS** | Celestica Inc. | Technology | 1.413 | 0.586 | 0.586 | 94.9% | +4.5% | 19 | 1 | 0 | 10 | 0 |
| 6 |  | **ELV** | Elevance Health, Inc. | Healthcare | 1.283 | 0.532 | 0.532 | 93.6% | +3.6% | 14 | 8 | 0 | 10 | 0 |
| 7 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.070 | 0.443 | 0.443 | 92.3% | +23.3% | 27 | 3 | 1 | 7 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.039 | 0.430 | 0.430 | 91.0% | +7.1% | 62 | 5 | 0 | 27 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 0.959 | 0.396 | 0.396 | 89.7% | +20.6% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.912 | 0.377 | 0.377 | 88.5% | +23.0% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.817 | 0.337 | 0.337 | 87.2% | -1.9% | 29 | 5 | 1 | 16 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.803 | 0.331 | 0.331 | 85.9% | +8.9% | 31 | 14 | 2 | 13 | 0 |
| 13 | ★★ | **APH** | Amphenol Corporation | Technology | 0.673 | 0.277 | 0.277 | 84.6% | +15.7% | 14 | 3 | 1 | 3 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.656 | 0.270 | 0.270 | 83.3% | +16.2% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.643 | 0.264 | 0.264 | 82.1% | +14.4% | 44 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.698 | 0.635 | 0.635 | 100.0% | +23.3% | 27 | 3 | 1 | 7 | 0 |
| 2 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.502 | 0.560 | 0.560 | 98.7% | +10.5% | 42 | 11 | 0 | 27 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.495 | 0.558 | 0.558 | 97.4% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 4 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.418 | 0.529 | 0.529 | 96.2% | +60.3% | 21 | 5 | 0 | 12 | 0 |
| 5 | ★★ | **CRH** | CRH plc | Basic Materials | 1.408 | 0.525 | 0.525 | 94.9% | +20.6% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.191 | 0.443 | 0.443 | 93.6% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.137 | 0.423 | 0.423 | 92.3% | +21.4% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.135 | 0.422 | 0.422 | 91.0% | +48.3% | 31 | 2 | 0 | 19 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.099 | 0.408 | 0.408 | 89.7% | +4.0% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.060 | 0.394 | 0.394 | 88.5% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.011 | 0.375 | 0.375 | 87.2% | +52.7% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.905 | 0.335 | 0.335 | 85.9% | +16.2% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.894 | 0.331 | 0.331 | 84.6% | +8.9% | 31 | 14 | 2 | 13 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.869 | 0.322 | 0.322 | 83.3% | +15.7% | 14 | 3 | 1 | 3 | 0 |
| 15 |  | **CVX** | Chevron Corporation | Energy | 0.867 | 0.321 | 0.321 | 82.1% | +9.5% | 18 | 6 | 1 | 10 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.998 | 0.871 | 0.871 | 100.0% | +60.3% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.785 | 0.777 | 0.777 | 98.7% | +48.3% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.524 | 0.662 | 0.662 | 97.4% | +39.9% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.458 | 0.633 | 0.633 | 96.2% | +52.7% | 35 | 10 | 1 | 24 | 0 |
| 5 |  | **CHKP** | Check Point Software Technologies Ltd. | Technology | 1.292 | 0.560 | 0.560 | 94.9% | +70.0% | 16 | 20 | 0 | 14 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.277 | 0.553 | 0.553 | 93.6% | +48.2% | 36 | 10 | 0 | 21 | 0 |
| 7 |  | **FROG** | JFrog Ltd. | Technology | 1.256 | 0.544 | 0.544 | 92.3% | +45.6% | 20 | 1 | 0 | 9 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.221 | 0.529 | 0.529 | 91.0% | +23.3% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.194 | 0.517 | 0.517 | 89.7% | +49.9% | 28 | 7 | 0 | 22 | 0 |
| 10 |  | **ABT** | Abbott Laboratories | Healthcare | 1.144 | 0.495 | 0.495 | 88.5% | +30.8% | 21 | 7 | 0 | 11 | 0 |
| 11 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.123 | 0.485 | 0.485 | 87.2% | +33.4% | 45 | 3 | 1 | 19 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.072 | 0.463 | 0.463 | 85.9% | +16.2% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 1.045 | 0.451 | 0.451 | 84.6% | +41.2% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.993 | 0.428 | 0.428 | 83.3% | +33.0% | 31 | 7 | 0 | 26 | 0 |
| 15 |  | **AZN** | AstraZeneca PLC | Healthcare | 0.977 | 0.421 | 0.421 | 82.1% | +19.0% | 9 | 1 | 0 | 0 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-30 19:52:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 19:52:35Z |  |
| stooq.prices | ok | 0 | 2026-04-30 18:09:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 18:09:46Z |  |
| stooq.prices | ok | 0 | 2026-04-30 16:50:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 16:50:49Z |  |
| stooq.prices | ok | 0 | 2026-04-30 15:14:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 15:14:04Z |  |
| stooq.prices | ok | 0 | 2026-04-30 12:58:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 12:57:58Z |  |
| stooq.prices | ok | 0 | 2026-04-30 11:10:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 11:10:54Z |  |
| stooq.prices | ok | 0 | 2026-04-30 09:11:02Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 09:10:56Z |  |
| stooq.prices | ok | 0 | 2026-04-30 06:44:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 06:44:48Z |  |
| stooq.prices | ok | 0 | 2026-04-30 04:07:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-30 04:07:41Z |  |
| edgar.13f | error | 0 | 2026-04-30 01:18:07Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-30 01:18:07Z |  |
