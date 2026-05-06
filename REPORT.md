# Invest — Top 15 report

_Generated: **2026-05-06 17:13 UTC** · Scores as of: **2026-05-06**_

🟢 last successful crawl: 0 min ago (at 2026-05-06T17:13:48Z)

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
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 4.259 | 1.541 | 1.541 | 100.0% | +7.6% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 4.145 | 1.500 | 1.500 | 98.7% | +4.2% | 14 | 8 | 0 | 9 | 0 |
| 3 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 1.697 | 0.610 | 0.610 | 97.4% | +6.7% | 22 | 18 | 2 | 14 | 0 |
| 4 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.433 | 0.514 | 0.514 | 96.2% | +9.0% | 17 | 1 | 0 | 8 | 0 |
| 5 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 1.104 | 0.395 | 0.395 | 94.9% | +12.0% | 61 | 5 | 0 | 32 | 0 |
| 6 |  | **AAPL** | Apple Inc. | Technology | 0.861 | 0.307 | 0.307 | 93.6% | +5.9% | 31 | 15 | 2 | 11 | 0 |
| 7 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 0.859 | 0.306 | 0.306 | 92.3% | -25.0% | 10 | 4 | 0 | 10 | 0 |
| 8 | ★★ | **DDOG** | Datadog, Inc. | Technology | 0.817 | 0.291 | 0.291 | 91.0% | +22.0% | 44 | 3 | 1 | 17 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.804 | 0.286 | 0.286 | 89.7% | +23.8% | 21 | 2 | 0 | 3 | 0 |
| 10 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.643 | 0.227 | 0.227 | 88.5% | -24.7% | 35 | 14 | 0 | 13 | 0 |
| 11 |  | **ADI** | Analog Devices, Inc. | Technology | 0.638 | 0.226 | 0.226 | 87.2% | -5.1% | 28 | 5 | 1 | 16 | 0 |
| 12 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.610 | 0.215 | 0.215 | 85.9% | +6.4% | 10 | 1 | 0 | 2 | 0 |
| 13 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.577 | 0.203 | 0.203 | 84.6% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 14 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.568 | 0.200 | 0.200 | 83.3% | +7.9% | 23 | 3 | 0 | 8 | 0 |
| 15 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.556 | 0.196 | 0.196 | 82.1% | +20.7% | 22 | 8 | 0 | 11 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CLS** | Celestica Inc. | Technology | 1.956 | 0.718 | 0.718 | 100.0% | +7.6% | 20 | 1 | 0 | 11 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.685 | 0.618 | 0.618 | 98.7% | +68.8% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 1.663 | 0.609 | 0.609 | 97.4% | +4.2% | 14 | 8 | 0 | 9 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.501 | 0.549 | 0.549 | 96.2% | +54.0% | 31 | 2 | 0 | 19 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.470 | 0.538 | 0.538 | 94.9% | +23.8% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.311 | 0.479 | 0.479 | 93.6% | +22.0% | 44 | 3 | 1 | 17 | 0 |
| 7 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 1.208 | 0.441 | 0.441 | 92.3% | +27.7% | 27 | 2 | 0 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.140 | 0.416 | 0.416 | 91.0% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.125 | 0.410 | 0.410 | 89.7% | +49.8% | 35 | 10 | 0 | 21 | 0 |
| 10 |  | **CVX** | Chevron Corporation | Energy | 0.996 | 0.362 | 0.362 | 88.5% | +16.0% | 18 | 6 | 1 | 11 | 0 |
| 11 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.968 | 0.352 | 0.352 | 87.2% | +4.8% | 42 | 11 | 0 | 27 | 0 |
| 12 | ★★ | **CRM** | Salesforce, Inc. | Technology | 0.967 | 0.351 | 0.351 | 85.9% | +46.9% | 33 | 8 | 1 | 24 | 0 |
| 13 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 0.872 | 0.316 | 0.316 | 84.6% | +6.7% | 22 | 18 | 2 | 14 | 0 |
| 14 | ★★ | **APH** | Amphenol Corporation | Technology | 0.865 | 0.313 | 0.313 | 83.3% | +32.3% | 15 | 3 | 0 | 7 | 0 |
| 15 | ★★ | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.841 | 0.305 | 0.305 | 82.1% | +12.0% | 61 | 5 | 0 | 32 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.196 | 0.996 | 0.996 | 100.0% | +68.8% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.056 | 0.932 | 0.932 | 98.7% | +54.0% | 31 | 2 | 0 | 19 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.581 | 0.714 | 0.714 | 97.4% | +43.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.328 | 0.599 | 0.599 | 96.2% | +49.8% | 35 | 10 | 0 | 21 | 0 |
| 5 |  | **ABT** | Abbott Laboratories | Healthcare | 1.320 | 0.595 | 0.595 | 94.9% | +37.5% | 21 | 7 | 0 | 11 | 0 |
| 6 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.251 | 0.563 | 0.563 | 93.6% | +46.9% | 33 | 8 | 1 | 24 | 0 |
| 7 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.088 | 0.488 | 0.488 | 92.3% | +23.8% | 21 | 2 | 0 | 3 | 0 |
| 8 |  | **CI** | The Cigna Group | Healthcare | 1.063 | 0.477 | 0.477 | 91.0% | +21.0% | 22 | 2 | 0 | 10 | 0 |
| 9 | ★★ | **APH** | Amphenol Corporation | Technology | 1.052 | 0.472 | 0.472 | 89.7% | +32.3% | 15 | 3 | 0 | 7 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.049 | 0.471 | 0.471 | 88.5% | +21.5% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **ACN** | Accenture plc | Technology | 1.005 | 0.450 | 0.450 | 87.2% | +41.0% | 18 | 10 | 0 | 12 | 0 |
| 12 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.982 | 0.440 | 0.440 | 85.9% | +32.8% | 30 | 7 | 0 | 25 | 0 |
| 13 | ★★ | **ANET** | Arista Networks, Inc. | Technology | 0.980 | 0.439 | 0.439 | 84.6% | +27.7% | 27 | 2 | 0 | 11 | 0 |
| 14 |  | **DKNG** | DraftKings Inc. | Consumer Cyclical | 0.964 | 0.431 | 0.431 | 83.3% | +43.5% | 28 | 7 | 0 | 22 | 0 |
| 15 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.925 | 0.414 | 0.414 | 82.1% | +23.9% | 24 | 8 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
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
| yfinance.fundamentals | ok | 80 | 2026-05-06 01:12:16Z |  |
| yfinance.prices | ok | 7110 | 2026-05-06 01:12:08Z |  |
