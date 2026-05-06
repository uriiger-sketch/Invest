# Invest — Top 15 report

_Generated: **2026-05-06 22:54 UTC** · Scores as of: **2026-05-06**_

🟢 last successful crawl: 0 min ago (at 2026-05-06T22:54:54Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **AMZN**, **APH**, **BSX**, **CHWY**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.255 | 1.532 | 1.532 | 100.0% | +7.0% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.157 | 1.496 | 1.496 | 98.7% | +3.8% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.698 | 0.607 | 0.607 | 97.4% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.515 | 0.541 | 0.541 | 96.2% | +5.4% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.058 | 0.376 | 0.376 | 94.9% | +12.6% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.924 | 0.328 | 0.328 | 93.6% | -27.2% | 10 | 4 | 0 | 10 | 0 |
| 7 |  | **AAPL** | Apple Inc. | Technology | 0.862 | 0.305 | 0.305 | 92.3% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.797 | 0.282 | 0.282 | 91.0% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.762 | 0.269 | 0.269 | 89.7% | +23.2% | 44 | 3 | 1 | 17 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.623 | 0.219 | 0.219 | 88.5% | -5.5% | 28 | 5 | 1 | 16 | 0 |
| 11 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.600 | 0.210 | 0.210 | 87.2% | -25.9% | 35 | 14 | 0 | 13 | 0 |
| 12 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.583 | 0.204 | 0.204 | 85.9% | +7.1% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.573 | 0.201 | 0.201 | 84.6% | +6.9% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.563 | 0.197 | 0.197 | 83.3% | +5.1% | 42 | 11 | 0 | 27 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.549 | 0.192 | 0.192 | 82.1% | +18.7% | 27 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.948 | 0.713 | 0.713 | 100.0% | +7.0% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.664 | 0.608 | 0.608 | 98.7% | +3.8% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.644 | 0.601 | 0.601 | 97.4% | +66.9% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.479 | 0.539 | 0.539 | 96.2% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.467 | 0.535 | 0.535 | 94.9% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.327 | 0.483 | 0.483 | 93.6% | +23.2% | 44 | 3 | 1 | 17 | 0 |
| 7 |  | **ANET** | Arista Networks, Inc. | Technology | 1.186 | 0.431 | 0.431 | 92.3% | +23.7% | 27 | 2 | 0 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.147 | 0.417 | 0.417 | 91.0% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.085 | 0.394 | 0.394 | 89.7% | +47.9% | 35 | 10 | 0 | 21 | 0 |
| 10 |  | **CVX** | Chevron Corporation | Energy | 1.012 | 0.367 | 0.367 | 88.5% | +16.0% | 18 | 6 | 1 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.990 | 0.359 | 0.359 | 87.2% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.981 | 0.355 | 0.355 | 85.9% | +5.1% | 42 | 11 | 0 | 27 | 0 |
| 13 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.878 | 0.317 | 0.317 | 84.6% | +6.6% | 22 | 18 | 2 | 14 | 0 |
| 14 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.848 | 0.306 | 0.306 | 83.3% | +12.6% | 61 | 5 | 0 | 32 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.847 | 0.306 | 0.306 | 82.1% | +31.2% | 15 | 3 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.125 | 0.964 | 0.964 | 100.0% | +66.9% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.990 | 0.902 | 0.902 | 98.7% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.577 | 0.713 | 0.713 | 97.4% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.318 | 0.594 | 0.594 | 96.2% | +37.5% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.286 | 0.579 | 0.579 | 94.9% | +48.1% | 33 | 8 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.264 | 0.569 | 0.569 | 93.6% | +47.9% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.099 | 0.494 | 0.494 | 92.3% | +23.9% | 21 | 2 | 0 | 3 | 0 |
| 8 |  | **CI** | The Cigna Group | Healthcare | 1.061 | 0.476 | 0.476 | 91.0% | +20.8% | 22 | 2 | 0 | 10 | 0 |
| 9 |  | **ACN** | Accenture plc | Technology | 1.060 | 0.476 | 0.476 | 89.7% | +42.7% | 18 | 10 | 0 | 12 | 0 |
| 10 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.041 | 0.467 | 0.467 | 88.5% | +45.7% | 28 | 7 | 0 | 22 | 0 |
| 11 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.037 | 0.465 | 0.465 | 87.2% | +21.0% | 9 | 1 | 0 | 0 | 0 |
| 12 | ★★ | **APH** | Amphenol Corporation | Technology | 1.021 | 0.458 | 0.458 | 85.9% | +31.2% | 15 | 3 | 0 | 7 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.003 | 0.450 | 0.450 | 84.6% | +33.3% | 30 | 7 | 0 | 25 | 0 |
| 14 |  | **BILL** | BILL Holdings, Inc. | Technology | 0.942 | 0.422 | 0.422 | 83.3% | +45.3% | 14 | 9 | 0 | 8 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.905 | 0.405 | 0.405 | 82.1% | +23.1% | 24 | 8 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-06 22:54:54Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 22:54:45Z |  |
| stooq.prices | ok | 0 | 2026-05-06 21:56:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 21:56:35Z |  |
| stooq.prices | ok | 0 | 2026-05-06 20:49:57Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 20:49:48Z |  |
| stooq.prices | ok | 0 | 2026-05-06 19:03:21Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 19:03:13Z |  |
| stooq.prices | ok | 0 | 2026-05-06 17:13:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 17:13:40Z |  |
| stooq.prices | ok | 0 | 2026-05-06 15:39:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 15:39:33Z |  |
| stooq.prices | ok | 0 | 2026-05-06 13:19:36Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 13:19:30Z |  |
| stooq.prices | ok | 0 | 2026-05-06 11:28:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 11:28:15Z |  |
| stooq.prices | ok | 0 | 2026-05-06 09:22:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 09:22:39Z |  |
| stooq.prices | ok | 0 | 2026-05-06 06:48:00Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 06:47:55Z |  |
