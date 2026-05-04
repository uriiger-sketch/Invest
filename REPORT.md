# Invest — Top 15 report

_Generated: **2026-05-04 18:05 UTC** · Scores as of: **2026-05-04**_

🟢 last successful crawl: 0 min ago (at 2026-05-04T18:05:05Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ANET**, **BAC**, **BSX**, **BUD**, **CHWY**, **CLS**, **CRDO**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **DIS**, **ELV**

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
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 3.594 | 1.442 | 1.442 | 100.0% | +4.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CLS** | Celestica Inc. | Technology | 3.029 | 1.214 | 1.214 | 98.7% | +4.0% | 20 | 1 | 0 | 11 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 2.768 | 1.109 | 1.109 | 97.4% | +4.7% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.814 | 0.725 | 0.725 | 96.2% | +15.3% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.427 | 0.569 | 0.569 | 94.9% | +2.9% | 27 | 3 | 0 | 11 | 0 |
| 6 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.188 | 0.473 | 0.473 | 93.6% | +13.1% | 59 | 5 | 0 | 32 | 0 |
| 7 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.075 | 0.428 | 0.428 | 92.3% | +16.6% | 23 | 8 | 0 | 12 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.813 | 0.322 | 0.322 | 91.0% | +21.5% | 44 | 3 | 1 | 18 | 0 |
| 9 |  | **AAPL** | Apple Inc. | Technology | 0.768 | 0.304 | 0.304 | 89.7% | +8.5% | 32 | 15 | 2 | 11 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.760 | 0.301 | 0.301 | 88.5% | +28.4% | 20 | 2 | 0 | 3 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.746 | 0.295 | 0.295 | 87.2% | -1.0% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.683 | 0.270 | 0.270 | 85.9% | +8.8% | 23 | 3 | 0 | 8 | 0 |
| 13 |  | **AVGO** | Broadcom Inc. | Technology | 0.535 | 0.210 | 0.210 | 84.6% | +15.2% | 43 | 3 | 0 | 16 | 0 |
| 14 |  | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.493 | 0.193 | 0.193 | 83.3% | +5.8% | 21 | 19 | 2 | 14 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.480 | 0.188 | 0.188 | 82.1% | +19.9% | 22 | 3 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 2.097 | 0.815 | 0.815 | 100.0% | +4.7% | 42 | 11 | 0 | 27 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.673 | 0.649 | 0.649 | 98.7% | +65.6% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.566 | 0.608 | 0.608 | 97.4% | +28.4% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.416 | 0.549 | 0.549 | 96.2% | +49.1% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★ | **CLS** | Celestica Inc. | Technology | 1.334 | 0.517 | 0.517 | 94.9% | +4.0% | 20 | 1 | 0 | 11 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.276 | 0.494 | 0.494 | 93.6% | +21.5% | 44 | 3 | 1 | 18 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.185 | 0.459 | 0.459 | 92.3% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.097 | 0.424 | 0.424 | 91.0% | +43.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.092 | 0.422 | 0.422 | 89.7% | +4.7% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.989 | 0.382 | 0.382 | 88.5% | +2.9% | 27 | 3 | 0 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.975 | 0.376 | 0.376 | 87.2% | +44.6% | 34 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.898 | 0.346 | 0.346 | 85.9% | +25.9% | 27 | 3 | 1 | 7 | 0 |
| 13 |  | **CVX** | Chevron Corporation | Energy | 0.879 | 0.339 | 0.339 | 84.6% | +11.0% | 18 | 6 | 1 | 10 | 0 |
| 14 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.872 | 0.336 | 0.336 | 83.3% | +19.0% | 10 | 1 | 0 | 2 | 0 |
| 15 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.864 | 0.333 | 0.333 | 82.1% | +15.3% | 17 | 1 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.309 | 1.049 | 1.049 | 100.0% | +65.6% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.048 | 0.930 | 0.930 | 98.7% | +49.1% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.726 | 0.782 | 0.782 | 97.4% | +43.7% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **ABT** | Abbott Laboratories | Healthcare | 1.319 | 0.597 | 0.597 | 96.2% | +34.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.306 | 0.590 | 0.590 | 94.9% | +44.6% | 34 | 8 | 1 | 24 | 0 |
| 6 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.282 | 0.580 | 0.580 | 93.6% | +28.4% | 20 | 2 | 0 | 3 | 0 |
| 7 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.266 | 0.572 | 0.572 | 92.3% | +48.4% | 28 | 7 | 0 | 22 | 0 |
| 8 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.205 | 0.544 | 0.544 | 91.0% | +43.2% | 35 | 10 | 0 | 21 | 0 |
| 9 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.157 | 0.522 | 0.522 | 89.7% | +19.0% | 10 | 1 | 0 | 2 | 0 |
| 10 |  | **CI** | The Cigna Group | Healthcare | 1.107 | 0.499 | 0.499 | 88.5% | +22.1% | 22 | 2 | 0 | 10 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.104 | 0.498 | 0.498 | 87.2% | +35.0% | 30 | 7 | 0 | 27 | 0 |
| 12 | ★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.087 | 0.490 | 0.490 | 85.9% | +25.9% | 27 | 3 | 1 | 7 | 0 |
| 13 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.085 | 0.489 | 0.489 | 84.6% | +21.8% | 9 | 1 | 0 | 0 | 0 |
| 14 |  | **ACN** | Accenture plc | Technology | 1.066 | 0.481 | 0.481 | 83.3% | +39.5% | 18 | 10 | 0 | 12 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.954 | 0.429 | 0.429 | 82.1% | +19.9% | 22 | 3 | 0 | 9 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-04 18:05:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 18:04:59Z |  |
| stooq.prices | ok | 0 | 2026-05-04 16:21:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 16:21:37Z |  |
| stooq.prices | ok | 0 | 2026-05-04 14:34:22Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 14:34:16Z |  |
| stooq.prices | ok | 0 | 2026-05-04 12:07:29Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 12:07:23Z |  |
| stooq.prices | ok | 0 | 2026-05-04 10:13:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 10:13:35Z |  |
| stooq.prices | ok | 0 | 2026-05-04 07:47:24Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 07:47:19Z |  |
| stooq.prices | ok | 0 | 2026-05-04 04:52:45Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 04:52:38Z |  |
| stooq.prices | ok | 0 | 2026-05-04 01:19:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-04 01:19:18Z |  |
| edgar.13f | error | 0 | 2026-05-04 00:13:26Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-04 00:13:26Z |  |
| yfinance.actions | ok | 1123 | 2026-05-04 00:13:18Z |  |
| yfinance.consensus | ok | 79 | 2026-05-04 00:13:07Z |  |
