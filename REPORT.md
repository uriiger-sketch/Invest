# Invest — Top 15 report

_Generated: **2026-05-05 18:57 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T18:57:09Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **APH**, **BSX**, **CHWY**, **CI**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.352 | 1.628 | 1.628 | 100.0% | +3.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.083 | 1.527 | 1.527 | 98.7% | +5.5% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.910 | 0.710 | 0.710 | 97.4% | +5.2% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.237 | 0.457 | 0.457 | 96.2% | +4.9% | 27 | 3 | 0 | 11 | 0 |
| 5 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.071 | 0.395 | 0.395 | 94.9% | +6.4% | 21 | 19 | 2 | 15 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.070 | 0.395 | 0.395 | 93.6% | +12.4% | 59 | 5 | 0 | 32 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.848 | 0.311 | 0.311 | 92.3% | +2.7% | 42 | 11 | 0 | 27 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.841 | 0.308 | 0.308 | 91.0% | +21.2% | 44 | 3 | 1 | 18 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.740 | 0.270 | 0.270 | 89.7% | +6.0% | 32 | 15 | 2 | 11 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.734 | 0.268 | 0.268 | 88.5% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 11 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.676 | 0.246 | 0.246 | 87.2% | -34.0% | 10 | 4 | 0 | 10 | 0 |
| 12 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.612 | 0.222 | 0.222 | 85.9% | -13.8% | 36 | 13 | 0 | 16 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.603 | 0.219 | 0.219 | 84.6% | +7.2% | 23 | 3 | 0 | 8 | 0 |
| 14 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.590 | 0.214 | 0.214 | 83.3% | +17.6% | 23 | 8 | 0 | 11 | 0 |
| 15 |  | **ADI** | Analog Devices, Inc. | Technology | 0.576 | 0.209 | 0.209 | 82.1% | -3.0% | 28 | 5 | 1 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.939 | 0.707 | 0.707 | 100.0% | +3.8% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.712 | 0.624 | 0.624 | 98.7% | +5.5% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.626 | 0.592 | 0.592 | 97.4% | +65.7% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.521 | 0.553 | 0.553 | 96.2% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.460 | 0.531 | 0.531 | 94.9% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.324 | 0.480 | 0.480 | 93.6% | +21.2% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.168 | 0.423 | 0.423 | 92.3% | +50.1% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.146 | 0.415 | 0.415 | 91.0% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.052 | 0.380 | 0.380 | 89.7% | +4.9% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.018 | 0.367 | 0.367 | 88.5% | +2.7% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.938 | 0.338 | 0.338 | 87.2% | +27.0% | 27 | 3 | 1 | 5 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.938 | 0.338 | 0.338 | 85.9% | +44.7% | 34 | 8 | 1 | 24 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.933 | 0.336 | 0.336 | 84.6% | +10.5% | 18 | 6 | 1 | 11 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.851 | 0.306 | 0.306 | 83.3% | +23.3% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.846 | 0.304 | 0.304 | 82.1% | +31.2% | 15 | 3 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.165 | 0.964 | 0.964 | 100.0% | +65.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.057 | 0.915 | 0.915 | 98.7% | +52.1% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.631 | 0.723 | 0.723 | 97.4% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.370 | 0.606 | 0.606 | 96.2% | +50.1% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.319 | 0.583 | 0.583 | 94.9% | +36.1% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.224 | 0.541 | 0.541 | 93.6% | +44.7% | 34 | 8 | 1 | 24 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.184 | 0.522 | 0.522 | 92.3% | +25.4% | 20 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **CI** | The Cigna Group | Healthcare | 1.176 | 0.519 | 0.519 | 91.0% | +23.3% | 22 | 2 | 0 | 10 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.140 | 0.503 | 0.503 | 89.7% | +23.2% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.136 | 0.501 | 0.501 | 88.5% | +27.0% | 27 | 3 | 1 | 5 | 0 |
| 11 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.099 | 0.484 | 0.484 | 87.2% | +46.4% | 28 | 7 | 0 | 22 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.051 | 0.463 | 0.463 | 85.9% | +41.2% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.048 | 0.461 | 0.461 | 84.6% | +34.0% | 30 | 7 | 0 | 27 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 1.022 | 0.450 | 0.450 | 83.3% | +31.2% | 15 | 3 | 0 | 7 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.921 | 0.404 | 0.404 | 82.1% | +18.2% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-05 18:57:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 18:56:58Z |  |
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
