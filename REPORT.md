# Invest — Top 15 report

_Generated: **2026-04-28 17:46 UTC** · Scores as of: **2026-04-28**_

🟢 last successful crawl: 0 min ago (at 2026-04-28T17:46:31Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ANET**, **BUD**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **FROG**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 4.126 | 1.728 | 1.728 | 100.0% | +7.5% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.736 | 1.145 | 1.145 | 98.7% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 3 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 2.659 | 1.113 | 1.113 | 97.4% | -8.8% | 36 | 13 | 0 | 15 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.756 | 0.734 | 0.734 | 96.2% | +25.6% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.274 | 0.532 | 0.532 | 94.9% | +23.8% | 23 | 8 | 0 | 12 | 0 |
| 6 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.232 | 0.514 | 0.514 | 93.6% | +10.0% | 27 | 3 | 0 | 11 | 0 |
| 7 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.068 | 0.445 | 0.445 | 92.3% | +9.8% | 62 | 5 | 0 | 26 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.964 | 0.401 | 0.401 | 91.0% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.858 | 0.357 | 0.357 | 89.7% | +24.6% | 19 | 2 | 0 | 3 | 0 |
| 10 |  | **ADI** | Analog Devices, Inc. | Technology | 0.740 | 0.307 | 0.307 | 88.5% | +2.0% | 29 | 5 | 1 | 16 | 0 |
| 11 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.729 | 0.303 | 0.303 | 87.2% | +5.6% | 13 | 9 | 0 | 9 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.673 | 0.279 | 0.279 | 85.9% | +10.2% | 31 | 14 | 2 | 12 | 0 |
| 13 |  | **C** | Citigroup Inc. | Financial Services | 0.637 | 0.264 | 0.264 | 84.6% | +10.1% | 19 | 4 | 0 | 12 | 0 |
| 14 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.615 | 0.255 | 0.255 | 83.3% | +17.7% | 10 | 1 | 0 | 2 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.601 | 0.249 | 0.249 | 82.1% | +18.8% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.674 | 1.020 | 1.020 | 100.0% | +7.5% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.658 | 0.630 | 0.630 | 98.7% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.431 | 0.543 | 0.543 | 97.4% | +59.3% | 21 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.430 | 0.543 | 0.543 | 96.2% | +33.5% | 45 | 3 | 1 | 19 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.407 | 0.534 | 0.534 | 94.9% | +24.6% | 19 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.182 | 0.447 | 0.447 | 93.6% | +46.1% | 36 | 10 | 0 | 21 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.131 | 0.428 | 0.428 | 92.3% | +25.6% | 16 | 1 | 0 | 7 | 0 |
| 8 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.057 | 0.399 | 0.399 | 91.0% | +5.3% | 21 | 20 | 2 | 14 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.055 | 0.399 | 0.399 | 89.7% | +39.7% | 22 | 2 | 0 | 10 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.041 | 0.393 | 0.393 | 88.5% | +10.0% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.903 | 0.340 | 0.340 | 87.2% | +46.7% | 35 | 10 | 1 | 24 | 0 |
| 12 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.890 | 0.335 | 0.335 | 85.9% | +17.7% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **FROG** | JFrog Ltd. | Technology | 0.874 | 0.329 | 0.329 | 84.6% | +48.2% | 20 | 1 | 0 | 9 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.811 | 0.305 | 0.305 | 83.3% | +17.8% | 14 | 3 | 1 | 5 | 0 |
| 15 | ★★ | **AAPL** | Apple Inc. | Technology | 0.789 | 0.297 | 0.297 | 82.1% | +10.2% | 31 | 14 | 2 | 12 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.058 | 0.887 | 0.887 | 100.0% | +59.3% | 21 | 5 | 0 | 12 | 0 |
| 2 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.791 | 0.771 | 0.771 | 98.7% | +47.0% | 32 | 1 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.541 | 0.662 | 0.662 | 97.4% | +39.7% | 22 | 2 | 0 | 10 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.367 | 0.586 | 0.586 | 96.2% | +48.2% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.275 | 0.546 | 0.546 | 94.9% | +46.7% | 35 | 10 | 1 | 24 | 0 |
| 6 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.259 | 0.539 | 0.539 | 93.6% | +26.1% | 27 | 3 | 1 | 7 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.243 | 0.532 | 0.532 | 92.3% | +46.1% | 36 | 10 | 0 | 21 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.180 | 0.505 | 0.505 | 91.0% | +47.7% | 28 | 7 | 0 | 23 | 0 |
| 9 | ★★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.104 | 0.472 | 0.472 | 89.7% | +17.7% | 10 | 1 | 0 | 2 | 0 |
| 10 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.097 | 0.469 | 0.469 | 88.5% | +33.5% | 45 | 3 | 1 | 19 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.056 | 0.451 | 0.451 | 87.2% | +24.6% | 19 | 2 | 0 | 3 | 0 |
| 12 |  | **ABBV** | AbbVie Inc. | Healthcare | 1.038 | 0.443 | 0.443 | 85.9% | +26.4% | 23 | 9 | 0 | 10 | 0 |
| 13 |  | **ABT** | Abbott Laboratories | Healthcare | 1.018 | 0.434 | 0.434 | 84.6% | +26.4% | 21 | 7 | 0 | 12 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.990 | 0.422 | 0.422 | 83.3% | +39.8% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.943 | 0.401 | 0.401 | 82.1% | +18.4% | 22 | 2 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-28 17:46:31Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 17:46:25Z |  |
| stooq.prices | ok | 0 | 2026-04-28 15:42:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 15:42:01Z |  |
| stooq.prices | ok | 0 | 2026-04-28 13:18:26Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 13:18:21Z |  |
| stooq.prices | ok | 0 | 2026-04-28 11:24:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 11:24:40Z |  |
| stooq.prices | ok | 0 | 2026-04-28 09:21:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 09:21:05Z |  |
| stooq.prices | ok | 0 | 2026-04-28 06:47:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 06:47:39Z |  |
| stooq.prices | ok | 0 | 2026-04-28 04:09:44Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-28 04:09:39Z |  |
| edgar.13f | error | 0 | 2026-04-28 01:16:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-28 01:16:32Z |  |
| yfinance.actions | ok | 1053 | 2026-04-28 01:16:25Z |  |
| yfinance.consensus | ok | 79 | 2026-04-28 01:16:15Z |  |
| yfinance.fundamentals | ok | 80 | 2026-04-28 01:15:58Z |  |
| yfinance.prices | ok | 7110 | 2026-04-28 01:15:52Z |  |
