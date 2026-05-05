# Invest — Top 15 report

_Generated: **2026-05-05 17:23 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T17:23:46Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AMZN**, **ANET**, **BSX**, **CHWY**, **CI**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.332 | 1.633 | 1.633 | 100.0% | +4.0% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.080 | 1.538 | 1.538 | 98.7% | +5.1% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.885 | 0.706 | 0.706 | 97.4% | +6.4% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.288 | 0.480 | 0.480 | 96.2% | +3.9% | 27 | 3 | 0 | 11 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.073 | 0.398 | 0.398 | 94.9% | +12.6% | 59 | 5 | 0 | 32 | 0 |
| 6 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.062 | 0.394 | 0.394 | 93.6% | +6.7% | 21 | 19 | 2 | 15 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.848 | 0.313 | 0.313 | 92.3% | +2.9% | 42 | 11 | 0 | 27 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.842 | 0.311 | 0.311 | 91.0% | +21.4% | 44 | 3 | 1 | 18 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.741 | 0.273 | 0.273 | 89.7% | +25.0% | 20 | 2 | 0 | 3 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.739 | 0.272 | 0.272 | 88.5% | +6.1% | 32 | 15 | 2 | 11 | 0 |
| 11 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.633 | 0.232 | 0.232 | 87.2% | -32.4% | 10 | 4 | 0 | 10 | 0 |
| 12 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.608 | 0.222 | 0.222 | 85.9% | -13.2% | 36 | 13 | 0 | 16 | 0 |
| 13 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.605 | 0.221 | 0.221 | 84.6% | +17.6% | 23 | 8 | 0 | 11 | 0 |
| 14 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.605 | 0.221 | 0.221 | 83.3% | +7.4% | 23 | 3 | 0 | 8 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.577 | 0.210 | 0.210 | 82.1% | -2.7% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.944 | 0.709 | 0.709 | 100.0% | +4.0% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.707 | 0.621 | 0.621 | 98.7% | +5.1% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.638 | 0.596 | 0.596 | 97.4% | +66.5% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.510 | 0.549 | 0.549 | 96.2% | +25.0% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.455 | 0.528 | 0.528 | 94.9% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.326 | 0.481 | 0.481 | 93.6% | +21.4% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.156 | 0.418 | 0.418 | 92.3% | +49.6% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.144 | 0.414 | 0.414 | 91.0% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.042 | 0.376 | 0.376 | 89.7% | +3.9% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.018 | 0.367 | 0.367 | 88.5% | +2.9% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.944 | 0.340 | 0.340 | 87.2% | +45.2% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.940 | 0.338 | 0.338 | 85.9% | +27.3% | 27 | 3 | 1 | 5 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.933 | 0.336 | 0.336 | 84.6% | +10.8% | 18 | 6 | 1 | 11 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.847 | 0.304 | 0.304 | 83.3% | +23.2% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.838 | 0.301 | 0.301 | 82.1% | +12.6% | 59 | 5 | 0 | 32 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.197 | 0.974 | 0.974 | 100.0% | +66.5% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.061 | 0.913 | 0.913 | 98.7% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.638 | 0.724 | 0.724 | 97.4% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.352 | 0.595 | 0.595 | 96.2% | +49.6% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.318 | 0.580 | 0.580 | 94.9% | +36.1% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.240 | 0.545 | 0.545 | 93.6% | +45.2% | 34 | 8 | 1 | 24 | 0 |
| 7 | ★★ | **CI** | The Cigna Group | Healthcare | 1.173 | 0.515 | 0.515 | 92.3% | +23.2% | 22 | 2 | 0 | 10 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.166 | 0.512 | 0.512 | 91.0% | +25.0% | 20 | 2 | 0 | 3 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.158 | 0.509 | 0.509 | 89.7% | +23.8% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.142 | 0.501 | 0.501 | 88.5% | +27.3% | 27 | 3 | 1 | 5 | 0 |
| 11 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.083 | 0.475 | 0.475 | 87.2% | +46.0% | 28 | 7 | 0 | 22 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.066 | 0.467 | 0.467 | 85.9% | +41.7% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.058 | 0.464 | 0.464 | 84.6% | +34.3% | 30 | 7 | 0 | 27 | 0 |
| 14 |  | **APH** | Amphenol Corporation | Technology | 0.949 | 0.415 | 0.415 | 83.3% | +29.2% | 15 | 3 | 0 | 7 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.921 | 0.402 | 0.402 | 82.1% | +18.3% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-05 17:23:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 17:23:39Z |  |
| stooq.prices | ok | 0 | 2026-05-05 15:53:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 15:53:16Z |  |
| stooq.prices | ok | 0 | 2026-05-05 13:52:58Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 13:52:51Z |  |
| stooq.prices | ok | 0 | 2026-05-05 11:51:13Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 11:51:08Z |  |
| stooq.prices | ok | 0 | 2026-05-05 10:23:43Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 10:23:38Z |  |
| stooq.prices | ok | 0 | 2026-05-05 08:30:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 08:30:25Z |  |
| stooq.prices | ok | 0 | 2026-05-05 06:15:20Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 06:15:15Z |  |
| stooq.prices | ok | 0 | 2026-05-05 03:53:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 03:53:24Z |  |
| edgar.13f | error | 0 | 2026-05-05 01:13:33Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-05 01:13:32Z |  |
| yfinance.actions | ok | 1126 | 2026-05-05 01:13:19Z |  |
| yfinance.consensus | ok | 79 | 2026-05-05 01:13:10Z |  |
