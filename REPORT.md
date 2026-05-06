# Invest — Top 15 report

_Generated: **2026-05-06 04:09 UTC** · Scores as of: **2026-05-06**_

🟢 last successful crawl: 0 min ago (at 2026-05-06T04:09:40Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AMZN**, **ANET**, **APH**, **BSX**, **CHWY**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.291 | 1.620 | 1.620 | 100.0% | +6.1% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.078 | 1.539 | 1.539 | 98.7% | +5.4% | 14 | 8 | 0 | 9 | 0 |
| 3 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.818 | 0.682 | 0.682 | 97.4% | +8.0% | 17 | 1 | 0 | 8 | 0 |
| 4 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.584 | 0.594 | 0.594 | 96.2% | +6.7% | 22 | 18 | 2 | 14 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.236 | 0.462 | 0.462 | 94.9% | +6.9% | 27 | 2 | 0 | 11 | 0 |
| 6 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.095 | 0.409 | 0.409 | 93.6% | +13.1% | 61 | 5 | 0 | 32 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.846 | 0.314 | 0.314 | 92.3% | +3.2% | 42 | 11 | 0 | 27 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.844 | 0.313 | 0.313 | 91.0% | +21.5% | 44 | 3 | 1 | 17 | 0 |
| 9 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.815 | 0.302 | 0.302 | 89.7% | -23.3% | 10 | 4 | 0 | 10 | 0 |
| 10 |  | **AAPL** | Apple Inc. | Technology | 0.735 | 0.272 | 0.272 | 88.5% | +6.8% | 31 | 15 | 2 | 11 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.712 | 0.263 | 0.263 | 87.2% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.607 | 0.223 | 0.223 | 85.9% | +7.3% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.582 | 0.214 | 0.214 | 84.6% | +18.4% | 22 | 8 | 0 | 11 | 0 |
| 14 |  | **ADI** | Analog Devices, Inc. | Technology | 0.577 | 0.212 | 0.212 | 83.3% | -2.9% | 28 | 5 | 1 | 16 | 0 |
| 15 |  | **AVGO** | Broadcom Inc. | Technology | 0.553 | 0.203 | 0.203 | 82.1% | +11.3% | 43 | 3 | 0 | 16 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.957 | 0.726 | 0.726 | 100.0% | +6.1% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.692 | 0.627 | 0.627 | 98.7% | +5.4% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.675 | 0.620 | 0.620 | 97.4% | +67.3% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.513 | 0.559 | 0.559 | 96.2% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.462 | 0.540 | 0.540 | 94.9% | +52.2% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.306 | 0.482 | 0.482 | 93.6% | +21.5% | 44 | 3 | 1 | 17 | 0 |
| 7 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.158 | 0.426 | 0.426 | 92.3% | +49.6% | 35 | 10 | 0 | 21 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.147 | 0.422 | 0.422 | 91.0% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.108 | 0.407 | 0.407 | 89.7% | +6.9% | 27 | 2 | 0 | 11 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.007 | 0.370 | 0.370 | 88.5% | +3.2% | 42 | 11 | 0 | 27 | 0 |
| 11 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.936 | 0.343 | 0.343 | 87.2% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 12 |  | **CVX** | Chevron Corporation | Energy | 0.915 | 0.335 | 0.335 | 85.9% | +11.5% | 18 | 6 | 1 | 11 | 0 |
| 13 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.905 | 0.331 | 0.331 | 84.6% | +43.5% | 33 | 8 | 1 | 24 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.889 | 0.325 | 0.325 | 83.3% | +32.9% | 15 | 3 | 0 | 7 | 0 |
| 15 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.867 | 0.317 | 0.317 | 82.1% | +13.1% | 61 | 5 | 0 | 32 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.251 | 1.008 | 1.008 | 100.0% | +67.3% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.077 | 0.929 | 0.929 | 98.7% | +52.2% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.648 | 0.735 | 0.735 | 97.4% | +43.2% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.372 | 0.610 | 0.610 | 96.2% | +49.6% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.322 | 0.587 | 0.587 | 94.9% | +36.1% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.209 | 0.536 | 0.536 | 93.6% | +26.5% | 21 | 2 | 0 | 3 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.192 | 0.528 | 0.528 | 92.3% | +43.5% | 33 | 8 | 1 | 24 | 0 |
| 8 |  | **CI** | The Cigna Group | Healthcare | 1.174 | 0.520 | 0.520 | 91.0% | +23.5% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.150 | 0.510 | 0.510 | 89.7% | +27.6% | 27 | 3 | 1 | 5 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.139 | 0.505 | 0.505 | 88.5% | +23.5% | 9 | 1 | 0 | 0 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 1.077 | 0.476 | 0.476 | 87.2% | +32.9% | 15 | 3 | 0 | 7 | 0 |
| 12 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.048 | 0.464 | 0.464 | 85.9% | +33.9% | 30 | 7 | 0 | 25 | 0 |
| 13 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.031 | 0.456 | 0.456 | 84.6% | +44.2% | 28 | 7 | 0 | 22 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 0.993 | 0.439 | 0.439 | 83.3% | +39.2% | 18 | 10 | 0 | 12 | 0 |
| 15 |  | **BAC** | Bank of America Corporation | Financial Services | 0.916 | 0.404 | 0.404 | 82.1% | +18.5% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-06 04:09:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 04:09:31Z |  |
| edgar.13f | error | 0 | 2026-05-06 01:12:53Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-06 01:12:52Z |  |
| yfinance.actions | ok | 1118 | 2026-05-06 01:12:45Z |  |
| yfinance.consensus | ok | 79 | 2026-05-06 01:12:33Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-06 01:12:16Z |  |
| yfinance.prices | ok | 7110 | 2026-05-06 01:12:08Z |  |
| stooq.prices | ok | 0 | 2026-05-06 00:07:39Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 00:07:34Z |  |
| stooq.prices | ok | 0 | 2026-05-05 23:15:00Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 23:14:48Z |  |
| stooq.prices | ok | 0 | 2026-05-05 22:16:31Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 22:16:25Z |  |
| stooq.prices | ok | 0 | 2026-05-05 21:18:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 21:18:03Z |  |
| stooq.prices | ok | 0 | 2026-05-05 20:09:35Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 20:09:30Z |  |
| stooq.prices | ok | 0 | 2026-05-05 18:57:08Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-05 18:56:58Z |  |
