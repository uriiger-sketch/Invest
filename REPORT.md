# Invest — Top 15 report

_Generated: **2026-05-05 13:53 UTC** · Scores as of: **2026-05-05**_

🟢 last successful crawl: 0 min ago (at 2026-05-05T13:52:59Z)

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.438 | 1.686 | 1.686 | 100.0% | +1.4% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.074 | 1.548 | 1.548 | 98.7% | +4.9% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.755 | 0.663 | 0.663 | 97.4% | +9.8% | 17 | 1 | 0 | 8 | 0 |
| 4 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.318 | 0.496 | 0.496 | 96.2% | +3.5% | 27 | 3 | 0 | 11 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.148 | 0.431 | 0.431 | 94.9% | +10.6% | 59 | 5 | 0 | 32 | 0 |
| 6 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.059 | 0.397 | 0.397 | 93.6% | +6.9% | 21 | 19 | 2 | 15 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.859 | 0.321 | 0.321 | 92.3% | +21.2% | 44 | 3 | 1 | 18 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.810 | 0.302 | 0.302 | 91.0% | +4.4% | 42 | 11 | 0 | 27 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.713 | 0.265 | 0.265 | 89.7% | +7.6% | 32 | 15 | 2 | 11 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.712 | 0.265 | 0.265 | 88.5% | +26.8% | 20 | 2 | 0 | 3 | 0 |
| 11 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.650 | 0.241 | 0.241 | 87.2% | -32.0% | 10 | 4 | 0 | 10 | 0 |
| 12 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.620 | 0.230 | 0.230 | 85.9% | +17.8% | 23 | 8 | 0 | 11 | 0 |
| 13 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.595 | 0.220 | 0.220 | 84.6% | -12.3% | 36 | 13 | 0 | 16 | 0 |
| 14 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.574 | 0.212 | 0.212 | 83.3% | +8.8% | 23 | 3 | 0 | 8 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.549 | 0.203 | 0.203 | 82.1% | +11.8% | 43 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.918 | 0.699 | 0.699 | 100.0% | +1.4% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.704 | 0.620 | 0.620 | 98.7% | +4.9% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.628 | 0.592 | 0.592 | 97.4% | +67.0% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.538 | 0.558 | 0.558 | 96.2% | +26.8% | 20 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.425 | 0.517 | 0.517 | 94.9% | +51.5% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.318 | 0.477 | 0.477 | 93.6% | +21.2% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.151 | 0.416 | 0.416 | 92.3% | +44.3% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.087 | 0.392 | 0.392 | 91.0% | +46.6% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.038 | 0.374 | 0.374 | 89.7% | +3.5% | 27 | 3 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.038 | 0.374 | 0.374 | 88.5% | +4.4% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.977 | 0.352 | 0.352 | 87.2% | +47.6% | 34 | 8 | 1 | 24 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.936 | 0.336 | 0.336 | 85.9% | +11.4% | 18 | 6 | 1 | 11 | 0 |
| 13 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.922 | 0.331 | 0.331 | 84.6% | +26.8% | 27 | 3 | 1 | 5 | 0 |
| 14 | ★★ | **CI** | The Cigna Group | Healthcare | 0.816 | 0.292 | 0.292 | 83.3% | +22.0% | 22 | 2 | 0 | 10 | 0 |
| 15 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.805 | 0.288 | 0.288 | 82.1% | +10.6% | 59 | 5 | 0 | 32 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.189 | 0.968 | 0.968 | 100.0% | +67.0% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.021 | 0.893 | 0.893 | 98.7% | +51.5% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.657 | 0.730 | 0.730 | 97.4% | +44.3% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.352 | 0.594 | 0.594 | 96.2% | +37.6% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.303 | 0.572 | 0.572 | 94.9% | +47.6% | 34 | 8 | 1 | 24 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.226 | 0.537 | 0.537 | 93.6% | +46.6% | 35 | 10 | 0 | 21 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.218 | 0.534 | 0.534 | 92.3% | +26.8% | 20 | 2 | 0 | 3 | 0 |
| 8 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.209 | 0.530 | 0.530 | 91.0% | +50.3% | 28 | 7 | 0 | 22 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.141 | 0.499 | 0.499 | 89.7% | +23.7% | 9 | 1 | 0 | 0 | 0 |
| 10 | ★★ | **CI** | The Cigna Group | Healthcare | 1.116 | 0.488 | 0.488 | 88.5% | +22.0% | 22 | 2 | 0 | 10 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.109 | 0.485 | 0.485 | 87.2% | +26.8% | 27 | 3 | 1 | 5 | 0 |
| 12 |  | **ACN** | Accenture plc | Technology | 1.082 | 0.473 | 0.473 | 85.9% | +42.8% | 18 | 10 | 0 | 12 | 0 |
| 13 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.074 | 0.469 | 0.469 | 84.6% | +35.3% | 30 | 7 | 0 | 27 | 0 |
| 14 |  | **BAC** | Bank of America Corporation | Financial Services | 0.944 | 0.411 | 0.411 | 83.3% | +19.3% | 22 | 3 | 0 | 9 | 0 |
| 15 |  | **APH** | Amphenol Corporation | Technology | 0.877 | 0.381 | 0.381 | 82.1% | +27.7% | 15 | 3 | 0 | 7 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-05-05 01:12:57Z |  |
| yfinance.prices | ok | 7110 | 2026-05-05 01:12:52Z |  |
| stooq.prices | ok | 0 | 2026-05-05 00:11:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 00:11:33Z |  |
