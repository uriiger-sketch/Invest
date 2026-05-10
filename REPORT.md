# Invest — Top 15 report

_Generated: **2026-05-10 10:02 UTC** · Scores as of: **2026-05-10**_

🟢 last successful crawl: 0 min ago (at 2026-05-10T10:02:04Z)

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.327 | 2.050 | 2.050 | 100.0% | -2.2% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 3.965 | 1.524 | 1.524 | 98.7% | +8.9% | 22 | 18 | 2 | 19 | 0 |
| 3 |  | **DDOG** | Datadog, Inc. | Technology | 1.531 | 0.583 | 0.583 | 97.4% | +6.7% | 44 | 3 | 1 | 22 | 0 |
| 4 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.284 | 0.488 | 0.488 | 96.2% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 5 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 1.066 | 0.404 | 0.404 | 94.9% | +10.9% | 17 | 1 | 0 | 8 | 0 |
| 6 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.048 | 0.397 | 0.397 | 93.6% | +7.2% | 10 | 4 | 0 | 11 | 0 |
| 7 | ★★ | **AAPL** | Apple Inc. | Technology | 0.856 | 0.323 | 0.323 | 92.3% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 8 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.615 | 0.230 | 0.230 | 91.0% | +14.3% | 62 | 4 | 0 | 29 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.606 | 0.226 | 0.226 | 89.7% | +2.9% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.578 | 0.215 | 0.215 | 88.5% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 11 | ★★ | **CVX** | Chevron Corporation | Energy | 0.568 | 0.211 | 0.211 | 87.2% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 12 |  | **FROG** | JFrog Ltd. | Technology | 0.561 | 0.209 | 0.209 | 85.9% | +12.6% | 20 | 1 | 0 | 12 | 0 |
| 13 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.545 | 0.203 | 0.203 | 84.6% | +4.6% | 22 | 3 | 0 | 8 | 0 |
| 14 |  | **AVGO** | Broadcom Inc. | Technology | 0.457 | 0.168 | 0.168 | 83.3% | +10.6% | 43 | 3 | 0 | 16 | 0 |
| 15 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.387 | 0.142 | 0.142 | 82.1% | +21.0% | 27 | 3 | 1 | 7 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.096 | 0.778 | 0.778 | 100.0% | +8.9% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.944 | 0.722 | 0.722 | 98.7% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.933 | 0.717 | 0.717 | 97.4% | -2.2% | 40 | 11 | 0 | 22 | 0 |
| 4 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.539 | 0.570 | 0.570 | 96.2% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 5 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.501 | 0.555 | 0.555 | 94.9% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 6 | ★★ | **CVX** | Chevron Corporation | Energy | 1.226 | 0.452 | 0.452 | 93.6% | +18.4% | 18 | 6 | 1 | 11 | 0 |
| 7 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.166 | 0.429 | 0.429 | 92.3% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 8 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.117 | 0.411 | 0.411 | 91.0% | -6.8% | 42 | 11 | 0 | 27 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.113 | 0.409 | 0.409 | 89.7% | +50.3% | 34 | 10 | 0 | 22 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.044 | 0.384 | 0.384 | 88.5% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.912 | 0.334 | 0.334 | 87.2% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.830 | 0.303 | 0.303 | 85.9% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 13 | ★★ | **AAPL** | Apple Inc. | Technology | 0.805 | 0.294 | 0.294 | 84.6% | +4.1% | 31 | 15 | 2 | 11 | 0 |
| 14 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.679 | 0.247 | 0.247 | 83.3% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 15 |  | **APP** | AppLovin Corporation | Communication Servic | 0.676 | 0.246 | 0.246 | 82.1% | +37.7% | 26 | 4 | 0 | 15 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.541 | 1.153 | 1.153 | 100.0% | +78.7% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.114 | 0.957 | 0.957 | 98.7% | +58.0% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.656 | 0.748 | 0.748 | 97.4% | +46.1% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.387 | 0.625 | 0.625 | 96.2% | +40.7% | 21 | 7 | 0 | 11 | 0 |
| 5 | ★★ | **APH** | Amphenol Corporation | Technology | 1.366 | 0.615 | 0.615 | 94.9% | +41.9% | 15 | 3 | 0 | 7 | 0 |
| 6 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.344 | 0.605 | 0.605 | 93.6% | +50.3% | 34 | 10 | 0 | 22 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.229 | 0.552 | 0.552 | 92.3% | +47.5% | 33 | 8 | 1 | 24 | 0 |
| 8 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.189 | 0.534 | 0.534 | 91.0% | +25.5% | 21 | 2 | 0 | 3 | 0 |
| 9 |  | **ANET** | Arista Networks, Inc. | Technology | 1.109 | 0.497 | 0.497 | 89.7% | +33.0% | 28 | 1 | 0 | 13 | 0 |
| 10 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.057 | 0.474 | 0.474 | 88.5% | +22.4% | 9 | 1 | 0 | 0 | 0 |
| 11 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.035 | 0.464 | 0.464 | 87.2% | +35.2% | 30 | 7 | 0 | 24 | 0 |
| 12 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 1.022 | 0.458 | 0.458 | 85.9% | +22.7% | 22 | 3 | 0 | 9 | 0 |
| 13 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.925 | 0.413 | 0.413 | 84.6% | +25.1% | 24 | 8 | 0 | 9 | 0 |
| 14 |  | **CI** | The Cigna Group | Healthcare | 0.912 | 0.407 | 0.407 | 83.3% | +18.2% | 22 | 2 | 0 | 10 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.908 | 0.405 | 0.405 | 82.1% | +15.5% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-10 10:02:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 10:01:57Z |  |
| stooq.prices | ok | 0 | 2026-05-10 08:23:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 08:23:33Z |  |
| stooq.prices | ok | 0 | 2026-05-10 06:12:03Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 06:11:56Z |  |
| stooq.prices | ok | 0 | 2026-05-10 02:50:52Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 02:50:47Z |  |
| edgar.13f | error | 0 | 2026-05-10 01:22:32Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-10 01:22:31Z |  |
| yfinance.actions | ok | 1172 | 2026-05-10 01:22:20Z |  |
| yfinance.consensus | ok | 79 | 2026-05-10 01:22:10Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-10 01:21:56Z |  |
| yfinance.prices | ok | 7110 | 2026-05-10 01:21:51Z |  |
| stooq.prices | ok | 0 | 2026-05-09 23:47:09Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 23:47:04Z |  |
| stooq.prices | ok | 0 | 2026-05-09 22:42:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 22:42:32Z |  |
| stooq.prices | ok | 0 | 2026-05-09 21:42:37Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-09 21:42:30Z |  |
