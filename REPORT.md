# Invest — Top 15 report

_Generated: **2026-04-24 19:15 UTC** · Scores as of: **2026-04-24**_

🟢 last successful crawl: 0 min ago (at 2026-04-24T19:15:46Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.752 | 1.575 | 1.575 | 100.0% | +10.1% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.242 | 1.361 | 1.361 | 98.7% | +15.0% | 18 | 6 | 1 | 10 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.308 | 0.968 | 0.968 | 97.4% | +9.0% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.120 | 0.888 | 0.888 | 96.2% | +5.9% | 16 | 1 | 0 | 7 | 0 |
| 5 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.437 | 0.601 | 0.601 | 94.9% | +3.2% | 21 | 20 | 2 | 14 | 0 |
| 6 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.083 | 0.452 | 0.452 | 93.6% | -15.4% | 36 | 13 | 0 | 16 | 0 |
| 7 |  | **ARM** | Arm Holdings plc | Technology | 1.027 | 0.429 | 0.429 | 92.3% | -27.4% | 27 | 10 | 2 | 18 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 0.994 | 0.415 | 0.415 | 91.0% | +0.3% | 27 | 3 | 0 | 11 | 0 |
| 9 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.921 | 0.384 | 0.384 | 89.7% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 10 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.917 | 0.382 | 0.382 | 88.5% | +23.2% | 23 | 8 | 0 | 12 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.867 | 0.361 | 0.361 | 87.2% | +7.3% | 63 | 5 | 0 | 27 | 0 |
| 12 | ★★ | **CRH** | CRH plc | Basic Materials | 0.779 | 0.324 | 0.324 | 85.9% | +21.0% | 19 | 2 | 0 | 3 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.732 | 0.304 | 0.304 | 84.6% | -2.2% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.548 | 0.227 | 0.227 | 83.3% | -4.4% | 18 | 2 | 0 | 6 | 0 |
| 15 |  | **APH** | Amphenol Corporation | Technology | 0.542 | 0.224 | 0.224 | 82.1% | +12.9% | 14 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CVX** | Chevron Corporation | Energy | 2.292 | 0.872 | 0.872 | 100.0% | +15.0% | 18 | 6 | 1 | 10 | 0 |
| 2 | ★★ | **AAPL** | Apple Inc. | Technology | 2.259 | 0.859 | 0.859 | 98.7% | +10.1% | 31 | 14 | 2 | 12 | 0 |
| 3 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.774 | 0.674 | 0.674 | 97.4% | +9.0% | 41 | 12 | 0 | 27 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.687 | 0.640 | 0.640 | 96.2% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.286 | 0.487 | 0.487 | 94.9% | +37.0% | 44 | 3 | 1 | 20 | 0 |
| 6 | ★★ | **CRH** | CRH plc | Basic Materials | 1.257 | 0.476 | 0.476 | 93.6% | +21.0% | 19 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.255 | 0.475 | 0.475 | 92.3% | +54.7% | 21 | 5 | 0 | 12 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.065 | 0.402 | 0.402 | 91.0% | +40.7% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.042 | 0.393 | 0.393 | 89.7% | +49.8% | 28 | 7 | 0 | 22 | 0 |
| 10 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.004 | 0.379 | 0.379 | 88.5% | +42.2% | 35 | 10 | 0 | 20 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.928 | 0.350 | 0.350 | 87.2% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.906 | 0.341 | 0.341 | 85.9% | +50.8% | 35 | 10 | 1 | 24 | 0 |
| 13 |  | **DE** | Deere & Company | Industrials | 0.865 | 0.325 | 0.325 | 84.6% | +17.7% | 13 | 11 | 0 | 13 | 0 |
| 14 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.806 | 0.303 | 0.303 | 83.3% | +5.9% | 16 | 1 | 0 | 7 | 0 |
| 15 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.805 | 0.303 | 0.303 | 82.1% | +3.2% | 21 | 20 | 2 | 14 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.819 | 0.774 | 0.774 | 100.0% | +54.7% | 21 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.634 | 0.695 | 0.695 | 98.7% | +40.7% | 22 | 2 | 0 | 10 | 0 |
| 3 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.464 | 0.622 | 0.622 | 97.4% | +39.0% | 32 | 1 | 0 | 19 | 0 |
| 4 |  | **FROG** | JFrog Ltd. | Technology | 1.452 | 0.616 | 0.616 | 96.2% | +50.5% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.369 | 0.581 | 0.581 | 94.9% | +50.8% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.305 | 0.553 | 0.553 | 93.6% | +49.8% | 28 | 7 | 0 | 22 | 0 |
| 7 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.285 | 0.544 | 0.544 | 92.3% | +21.1% | 10 | 1 | 0 | 2 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.278 | 0.541 | 0.541 | 91.0% | +24.9% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.247 | 0.528 | 0.528 | 89.7% | +37.0% | 44 | 3 | 1 | 20 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.191 | 0.504 | 0.504 | 88.5% | +23.5% | 22 | 2 | 0 | 8 | 0 |
| 11 |  | **ABT** | Abbott Laboratories | Healthcare | 1.138 | 0.481 | 0.481 | 87.2% | +29.7% | 21 | 7 | 0 | 12 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.083 | 0.458 | 0.458 | 85.9% | +42.2% | 35 | 10 | 0 | 20 | 0 |
| 13 |  | **BAC** | Bank of America Corporation | Financial Services | 0.996 | 0.420 | 0.420 | 84.6% | +20.6% | 22 | 3 | 0 | 9 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.992 | 0.418 | 0.418 | 83.3% | +25.5% | 23 | 9 | 0 | 11 | 0 |
| 15 |  | **ACN** | Accenture plc | Technology | 0.958 | 0.404 | 0.404 | 82.1% | +40.1% | 18 | 10 | 0 | 12 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-24 19:15:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 19:15:40Z |  |
| stooq.prices | ok | 0 | 2026-04-24 18:03:41Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 18:03:34Z |  |
| stooq.prices | ok | 0 | 2026-04-24 17:16:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 17:16:36Z |  |
| stooq.prices | ok | 0 | 2026-04-24 16:04:51Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 16:04:44Z |  |
| stooq.prices | ok | 0 | 2026-04-24 14:45:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 14:45:06Z |  |
| stooq.prices | ok | 0 | 2026-04-24 12:42:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 12:42:38Z |  |
| stooq.prices | ok | 0 | 2026-04-24 11:37:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 11:37:32Z |  |
| stooq.prices | ok | 0 | 2026-04-24 10:13:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 10:13:04Z |  |
| stooq.prices | ok | 0 | 2026-04-24 08:25:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-24 08:25:41Z |  |
| stooq.prices | ok | 0 | 2026-04-24 06:08:27Z |  |
| yfinance.prices_fast | ok | 7020 | 2026-04-24 06:08:18Z |  |
