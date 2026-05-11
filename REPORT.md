# Invest — Top 15 report

_Generated: **2026-05-11 01:25 UTC** · Scores as of: **2026-05-11**_

🟢 last successful crawl: 0 min ago (at 2026-05-11T01:25:08Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BAC**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.354 | 2.066 | 2.066 | 100.0% | -2.2% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.986 | 1.536 | 1.536 | 98.7% | +8.9% | 22 | 18 | 2 | 19 | 0 |
| 3 |  | **DDOG** | Datadog, Inc. | Technology | 1.517 | 0.580 | 0.580 | 97.4% | +6.7% | 44 | 3 | 1 | 22 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.307 | 0.499 | 0.499 | 96.2% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.054 | 0.400 | 0.400 | 94.9% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.035 | 0.393 | 0.393 | 93.6% | +7.2% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.858 | 0.325 | 0.325 | 92.3% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.616 | 0.231 | 0.231 | 91.0% | +2.9% | 14 | 8 | 0 | 9 | 0 |
| 9 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.604 | 0.226 | 0.226 | 89.7% | +14.3% | 62 | 4 | 0 | 29 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.582 | 0.218 | 0.218 | 88.5% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.571 | 0.214 | 0.214 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 |  | **FROG** | JFrog Ltd. | Technology | 0.551 | 0.205 | 0.205 | 85.9% | +12.6% | 20 | 1 | 0 | 12 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.535 | 0.199 | 0.199 | 84.6% | +4.6% | 22 | 3 | 0 | 8 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.446 | 0.165 | 0.165 | 83.3% | +10.6% | 43 | 3 | 0 | 16 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.377 | 0.138 | 0.138 | 82.1% | +21.0% | 27 | 3 | 1 | 7 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.146 | 0.797 | 0.797 | 100.0% | +8.9% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.998 | 0.742 | 0.742 | 98.7% | -2.2% | 40 | 11 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.931 | 0.716 | 0.716 | 97.4% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.526 | 0.564 | 0.564 | 96.2% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.512 | 0.559 | 0.559 | 94.9% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.234 | 0.455 | 0.455 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.160 | 0.427 | 0.427 | 92.3% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.152 | 0.424 | 0.424 | 91.0% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.099 | 0.404 | 0.404 | 89.7% | +50.3% | 34 | 10 | 0 | 22 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.030 | 0.378 | 0.378 | 88.5% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.898 | 0.329 | 0.329 | 87.2% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.816 | 0.298 | 0.298 | 85.9% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.813 | 0.297 | 0.297 | 84.6% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 14 |  | **CLS** | Celestica Inc. | Technology | 0.688 | 0.250 | 0.250 | 83.3% | +18.0% | 20 | 1 | 0 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.665 | 0.242 | 0.242 | 82.1% | +22.7% | 22 | 3 | 0 | 9 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.540 | 1.151 | 1.151 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.113 | 0.956 | 0.956 | 98.7% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.654 | 0.746 | 0.746 | 97.4% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.385 | 0.623 | 0.623 | 96.2% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.364 | 0.613 | 0.613 | 94.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.341 | 0.603 | 0.603 | 93.6% | +50.3% | 34 | 10 | 0 | 22 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.227 | 0.551 | 0.551 | 92.3% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.193 | 0.535 | 0.535 | 91.0% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **ANET** | Arista Networks, Inc. | Technology | 1.106 | 0.496 | 0.496 | 89.7% | +33.0% | 28 | 1 | 0 | 13 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.055 | 0.472 | 0.472 | 88.5% | +22.4% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.033 | 0.462 | 0.462 | 87.2% | +35.2% | 30 | 7 | 0 | 24 | 0 |
| 12 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 1.019 | 0.456 | 0.456 | 85.9% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.922 | 0.411 | 0.411 | 84.6% | +25.1% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.909 | 0.406 | 0.406 | 83.3% | +18.2% | 22 | 2 | 0 | 9 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.905 | 0.404 | 0.404 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| edgar.13f | error | 0 | 2026-05-11 01:25:08Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-11 01:25:07Z |  |
| yfinance.actions | ok | 1153 | 2026-05-11 01:24:49Z |  |
| yfinance.consensus | ok | 79 | 2026-05-11 01:24:42Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-11 01:24:31Z |  |
| yfinance.prices | ok | 7110 | 2026-05-11 01:24:27Z |  |
| stooq.prices | ok | 0 | 2026-05-10 23:34:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 23:33:59Z |  |
| stooq.prices | ok | 0 | 2026-05-10 22:28:32Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 22:28:26Z |  |
| stooq.prices | ok | 0 | 2026-05-10 21:31:17Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 21:31:13Z |  |
| stooq.prices | ok | 0 | 2026-05-10 20:26:36Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 20:26:28Z |  |
| stooq.prices | ok | 0 | 2026-05-10 19:36:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 19:36:17Z |  |
| stooq.prices | ok | 0 | 2026-05-10 18:09:34Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 18:09:29Z |  |
| stooq.prices | ok | 0 | 2026-05-10 17:05:39Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 17:05:34Z |  |
