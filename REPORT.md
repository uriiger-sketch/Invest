# Invest — Top 15 report

_Generated: **2026-05-06 15:39 UTC** · Scores as of: **2026-05-06**_

🟢 last successful crawl: 0 min ago (at 2026-05-06T15:39:44Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **ABNB**, **AMZN**, **ANET**, **APH**, **BSX**, **CHWY**, **CLS**, **CRH**, **CRM**, **CRWD**, **DASH**, **DDOG**, **DHR**, **ELV**

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.229 | 1.538 | 1.538 | 100.0% | +8.5% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.160 | 1.513 | 1.513 | 98.7% | +3.5% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.685 | 0.609 | 0.609 | 97.4% | +7.2% | 22 | 18 | 2 | 14 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.421 | 0.512 | 0.512 | 96.2% | +10.3% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.081 | 0.388 | 0.388 | 94.9% | +13.2% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 0.859 | 0.307 | 0.307 | 93.6% | +6.2% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.812 | 0.290 | 0.290 | 92.3% | +23.5% | 21 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.783 | 0.279 | 0.279 | 91.0% | +23.7% | 44 | 3 | 1 | 17 | 0 |
| 9 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.755 | 0.269 | 0.269 | 89.7% | -22.9% | 10 | 4 | 0 | 10 | 0 |
| 10 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.715 | 0.255 | 0.255 | 88.5% | -24.9% | 35 | 14 | 0 | 13 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.663 | 0.236 | 0.236 | 87.2% | -5.3% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.623 | 0.221 | 0.221 | 85.9% | +6.3% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.580 | 0.206 | 0.206 | 84.6% | +8.0% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.569 | 0.201 | 0.201 | 83.3% | +5.3% | 42 | 11 | 0 | 27 | 0 |
| 15 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.561 | 0.198 | 0.198 | 82.1% | +21.3% | 22 | 8 | 0 | 11 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.973 | 0.724 | 0.724 | 100.0% | +8.5% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.698 | 0.622 | 0.622 | 98.7% | +69.6% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.653 | 0.605 | 0.605 | 97.4% | +3.5% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.501 | 0.549 | 0.549 | 96.2% | +54.2% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.463 | 0.535 | 0.535 | 94.9% | +23.5% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.339 | 0.489 | 0.489 | 93.6% | +23.7% | 44 | 3 | 1 | 17 | 0 |
| 7 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.205 | 0.439 | 0.439 | 92.3% | +27.5% | 27 | 2 | 0 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.133 | 0.412 | 0.412 | 91.0% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.108 | 0.403 | 0.403 | 89.7% | +49.0% | 35 | 10 | 0 | 21 | 0 |
| 10 |  | **CVX** | Chevron Corporation | Energy | 0.997 | 0.362 | 0.362 | 88.5% | +16.7% | 18 | 6 | 1 | 11 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.972 | 0.353 | 0.353 | 87.2% | +5.3% | 42 | 11 | 0 | 27 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.957 | 0.347 | 0.347 | 85.9% | +46.5% | 33 | 8 | 1 | 24 | 0 |
| 13 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.877 | 0.317 | 0.317 | 84.6% | +7.2% | 22 | 18 | 2 | 14 | 0 |
| 14 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.863 | 0.312 | 0.312 | 83.3% | +13.2% | 61 | 5 | 0 | 32 | 0 |
| 15 | ★★ | **APH** | Amphenol Corporation | Technology | 0.832 | 0.301 | 0.301 | 82.1% | +30.7% | 15 | 3 | 0 | 7 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.229 | 1.006 | 1.006 | 100.0% | +69.6% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.071 | 0.934 | 0.934 | 98.7% | +54.2% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.581 | 0.711 | 0.711 | 97.4% | +43.0% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.302 | 0.584 | 0.584 | 96.2% | +49.0% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.290 | 0.578 | 0.578 | 94.9% | +36.5% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.240 | 0.555 | 0.555 | 93.6% | +46.5% | 33 | 8 | 1 | 24 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.075 | 0.480 | 0.480 | 92.3% | +23.5% | 21 | 2 | 0 | 3 | 0 |
| 8 |  | **CI** | The Cigna Group | Healthcare | 1.073 | 0.479 | 0.479 | 91.0% | +21.3% | 22 | 2 | 0 | 10 | 0 |
| 9 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.045 | 0.466 | 0.466 | 89.7% | +21.4% | 9 | 1 | 0 | 0 | 0 |
| 10 |  | **ACN** | Accenture plc | Technology | 1.020 | 0.455 | 0.455 | 88.5% | +41.4% | 18 | 10 | 0 | 12 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.994 | 0.443 | 0.443 | 87.2% | +30.7% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.974 | 0.434 | 0.434 | 85.9% | +27.5% | 27 | 2 | 0 | 11 | 0 |
| 13 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.969 | 0.432 | 0.432 | 84.6% | +43.7% | 28 | 7 | 0 | 22 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.958 | 0.427 | 0.427 | 83.3% | +32.1% | 30 | 7 | 0 | 25 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.909 | 0.404 | 0.404 | 82.1% | +23.5% | 24 | 8 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
