# Invest — Top 15 report

_Generated: **2026-05-08 22:17 UTC** · Scores as of: **2026-05-08**_

🟢 last successful crawl: 0 min ago (at 2026-05-08T22:17:04Z)

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 4.803 | 1.734 | 1.734 | 100.0% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.085 | 1.473 | 1.473 | 98.7% | +5.4% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 2.071 | 0.742 | 0.742 | 97.4% | -11.6% | 44 | 3 | 1 | 16 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.268 | 0.451 | 0.451 | 96.2% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.158 | 0.411 | 0.411 | 94.9% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.140 | 0.404 | 0.404 | 93.6% | +7.2% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.867 | 0.305 | 0.305 | 92.3% | +3.4% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.675 | 0.235 | 0.235 | 91.0% | +14.0% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.608 | 0.211 | 0.211 | 89.7% | +2.9% | 14 | 8 | 0 | 9 | 0 |
| 10 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.604 | 0.210 | 0.210 | 88.5% | +4.6% | 23 | 3 | 0 | 8 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.568 | 0.197 | 0.197 | 87.2% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 12 | ★★ | **CVX** | Chevron Corporation | Energy | 0.561 | 0.194 | 0.194 | 85.9% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 13 |  | **FROG** | JFrog Ltd. | Technology | 0.490 | 0.168 | 0.168 | 84.6% | -4.6% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.423 | 0.144 | 0.144 | 83.3% | +19.7% | 27 | 3 | 1 | 6 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.374 | 0.126 | 0.126 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.967 | 0.708 | 0.708 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.906 | 0.686 | 0.686 | 98.7% | +5.4% | 22 | 18 | 2 | 14 | 0 |
| 3 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.612 | 0.578 | 0.578 | 97.4% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 4 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.542 | 0.553 | 0.553 | 96.2% | -4.9% | 40 | 10 | 0 | 22 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.473 | 0.528 | 0.528 | 94.9% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.204 | 0.430 | 0.430 | 93.6% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.202 | 0.429 | 0.429 | 92.3% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.173 | 0.418 | 0.418 | 91.0% | +51.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.077 | 0.384 | 0.384 | 89.7% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.026 | 0.365 | 0.365 | 88.5% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.948 | 0.337 | 0.337 | 87.2% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.865 | 0.306 | 0.306 | 85.9% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 13 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.863 | 0.306 | 0.306 | 84.6% | -11.6% | 44 | 3 | 1 | 16 | 0 |
| 14 |  | **DE** | Deere & Company | Industrials | 0.780 | 0.275 | 0.275 | 83.3% | +15.7% | 13 | 11 | 0 | 13 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.766 | 0.270 | 0.270 | 82.1% | +3.4% | 31 | 15 | 2 | 11 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.507 | 1.133 | 1.133 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.147 | 0.968 | 0.968 | 98.7% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.657 | 0.745 | 0.745 | 97.4% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.394 | 0.625 | 0.625 | 96.2% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.370 | 0.614 | 0.614 | 94.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.366 | 0.613 | 0.613 | 93.6% | +51.2% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.227 | 0.549 | 0.549 | 92.3% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.182 | 0.529 | 0.529 | 91.0% | +25.3% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.084 | 0.484 | 0.484 | 89.7% | +22.4% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **BAC** | Bank of America Corporation | Financial Services | 1.048 | 0.468 | 0.468 | 88.5% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.047 | 0.467 | 0.467 | 87.2% | +35.2% | 30 | 7 | 0 | 24 | 0 |
| 12 |  | **ANET** | Arista Networks, Inc. | Technology | 1.004 | 0.447 | 0.447 | 85.9% | +32.2% | 26 | 2 | 0 | 13 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.948 | 0.422 | 0.422 | 84.6% | +25.1% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.943 | 0.420 | 0.420 | 83.3% | +18.2% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.942 | 0.419 | 0.419 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-08 22:17:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 22:16:13Z |  |
| stooq.prices | ok | 0 | 2026-05-08 21:19:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 21:19:04Z |  |
| stooq.prices | ok | 0 | 2026-05-08 20:07:19Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 20:07:13Z |  |
| stooq.prices | ok | 0 | 2026-05-08 18:48:11Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-08 18:48:02Z |  |
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
