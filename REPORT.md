# Invest — Top 15 report

_Generated: **2026-05-06 19:03 UTC** · Scores as of: **2026-05-06**_

🟢 last successful crawl: 0 min ago (at 2026-05-06T19:03:22Z)

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.257 | 1.541 | 1.541 | 100.0% | +7.2% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.172 | 1.510 | 1.510 | 98.7% | +3.0% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.700 | 0.611 | 0.611 | 97.4% | +6.5% | 22 | 18 | 2 | 14 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.429 | 0.513 | 0.513 | 96.2% | +8.3% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.096 | 0.392 | 0.392 | 94.9% | +11.8% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.925 | 0.330 | 0.330 | 93.6% | -26.4% | 10 | 4 | 0 | 10 | 0 |
| 7 |  | **AAPL** | Apple Inc. | Technology | 0.869 | 0.309 | 0.309 | 92.3% | +5.5% | 31 | 15 | 2 | 11 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.799 | 0.284 | 0.284 | 91.0% | +24.0% | 21 | 2 | 0 | 3 | 0 |
| 9 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.724 | 0.257 | 0.257 | 89.7% | +25.1% | 44 | 3 | 1 | 17 | 0 |
| 10 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.626 | 0.221 | 0.221 | 88.5% | -25.2% | 35 | 14 | 0 | 13 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.618 | 0.218 | 0.218 | 87.2% | -4.8% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.600 | 0.212 | 0.212 | 85.9% | +6.7% | 10 | 1 | 0 | 2 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.583 | 0.206 | 0.206 | 84.6% | +7.1% | 23 | 3 | 0 | 8 | 0 |
| 14 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.559 | 0.197 | 0.197 | 83.3% | +5.4% | 42 | 11 | 0 | 27 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.552 | 0.194 | 0.194 | 82.1% | +19.4% | 27 | 3 | 1 | 5 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.955 | 0.715 | 0.715 | 100.0% | +7.2% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.655 | 0.604 | 0.604 | 98.7% | +67.6% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.650 | 0.602 | 0.602 | 97.4% | +3.0% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.479 | 0.539 | 0.539 | 96.2% | +24.0% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.477 | 0.538 | 0.538 | 94.9% | +52.8% | 31 | 2 | 0 | 19 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.357 | 0.494 | 0.494 | 93.6% | +25.1% | 44 | 3 | 1 | 17 | 0 |
| 7 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.212 | 0.441 | 0.441 | 92.3% | +27.9% | 27 | 2 | 0 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.150 | 0.417 | 0.417 | 91.0% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.120 | 0.406 | 0.406 | 89.7% | +49.7% | 35 | 10 | 0 | 21 | 0 |
| 10 |  | **CVX** | Chevron Corporation | Energy | 1.005 | 0.364 | 0.364 | 88.5% | +16.1% | 18 | 6 | 1 | 11 | 0 |
| 11 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.001 | 0.362 | 0.362 | 87.2% | +48.8% | 33 | 8 | 1 | 24 | 0 |
| 12 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.982 | 0.356 | 0.356 | 85.9% | +5.4% | 42 | 11 | 0 | 27 | 0 |
| 13 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.875 | 0.316 | 0.316 | 84.6% | +6.5% | 22 | 18 | 2 | 14 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.861 | 0.311 | 0.311 | 83.3% | +32.1% | 15 | 3 | 0 | 7 | 0 |
| 15 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.839 | 0.303 | 0.303 | 82.1% | +11.8% | 61 | 5 | 0 | 32 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.148 | 0.972 | 0.972 | 100.0% | +67.6% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.013 | 0.910 | 0.910 | 98.7% | +52.8% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.590 | 0.717 | 0.717 | 97.4% | +43.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.321 | 0.594 | 0.594 | 96.2% | +49.7% | 35 | 10 | 0 | 21 | 0 |
| 5 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.309 | 0.588 | 0.588 | 94.9% | +48.8% | 33 | 8 | 1 | 24 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.297 | 0.583 | 0.583 | 93.6% | +36.9% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.098 | 0.492 | 0.492 | 92.3% | +24.0% | 21 | 2 | 0 | 3 | 0 |
| 8 | ★★ | **APH** | Amphenol Corporation | Technology | 1.045 | 0.467 | 0.467 | 91.0% | +32.1% | 15 | 3 | 0 | 7 | 0 |
| 9 |  | **ACN** | Accenture plc | Technology | 1.027 | 0.459 | 0.459 | 89.7% | +41.8% | 18 | 10 | 0 | 12 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.019 | 0.456 | 0.456 | 88.5% | +20.6% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **CI** | The Cigna Group | Healthcare | 1.014 | 0.453 | 0.453 | 87.2% | +19.6% | 22 | 2 | 0 | 10 | 0 |
| 12 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.988 | 0.441 | 0.441 | 85.9% | +27.9% | 27 | 2 | 0 | 11 | 0 |
| 13 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.977 | 0.436 | 0.436 | 84.6% | +43.9% | 28 | 7 | 0 | 22 | 0 |
| 14 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.956 | 0.427 | 0.427 | 83.3% | +32.0% | 30 | 7 | 0 | 25 | 0 |
| 15 |  | **BILL** | BILL Holdings, Inc. | Technology | 0.936 | 0.418 | 0.418 | 82.1% | +45.2% | 14 | 9 | 0 | 8 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| stooq.prices | ok | 0 | 2026-05-06 04:09:40Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-06 04:09:31Z |  |
| edgar.13f | error | 0 | 2026-05-06 01:12:53Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-06 01:12:52Z |  |
| yfinance.actions | ok | 1118 | 2026-05-06 01:12:45Z |  |
| yfinance.consensus | ok | 79 | 2026-05-06 01:12:33Z |  |
