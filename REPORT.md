# Invest — Top 15 report

_Generated: **2026-05-11 17:57 UTC** · Scores as of: **2026-05-11**_

🟢 last successful crawl: 0 min ago (at 2026-05-11T17:57:24Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **ABT**, **AMD**, **APH**, **BKNG**, **BSX**, **CHWY**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DHR**

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
| 1 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.247 | 1.983 | 1.983 | 100.0% | -4.7% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.010 | 1.514 | 1.514 | 98.7% | +10.7% | 22 | 18 | 2 | 19 | 0 |
| 3 |  | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.552 | 0.581 | 0.581 | 97.4% | +9.8% | 10 | 4 | 0 | 11 | 0 |
| 4 |  | **DDOG** | Datadog, Inc. | Technology | 1.551 | 0.580 | 0.580 | 96.2% | +7.0% | 44 | 3 | 1 | 22 | 0 |
| 5 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.486 | 0.556 | 0.556 | 94.9% | -8.8% | 42 | 11 | 0 | 27 | 0 |
| 6 | ★★ | **AAPL** | Apple Inc. | Technology | 0.873 | 0.323 | 0.323 | 93.6% | +4.5% | 31 | 15 | 2 | 11 | 0 |
| 7 |  | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.819 | 0.303 | 0.303 | 92.3% | +0.3% | 17 | 1 | 0 | 8 | 0 |
| 8 |  | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.707 | 0.260 | 0.260 | 91.0% | +4.4% | 22 | 3 | 0 | 8 | 0 |
| 9 |  | **ELV** | Elevance Health, Inc. | Healthcare | 0.657 | 0.241 | 0.241 | 89.7% | +2.2% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **CVX** | Chevron Corporation | Energy | 0.623 | 0.228 | 0.228 | 88.5% | +16.4% | 18 | 6 | 1 | 11 | 0 |
| 11 | ★★★ | **CRH** | CRH plc | Basic Materials | 0.513 | 0.187 | 0.187 | 87.2% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 12 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.497 | 0.180 | 0.180 | 85.9% | +15.0% | 62 | 4 | 0 | 29 | 0 |
| 13 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 0.444 | 0.160 | 0.160 | 84.6% | +22.7% | 23 | 8 | 0 | 9 | 0 |
| 14 |  | **FROG** | JFrog Ltd. | Technology | 0.400 | 0.143 | 0.143 | 83.3% | +17.5% | 20 | 1 | 0 | 12 | 0 |
| 15 |  | **CI** | The Cigna Group | Healthcare | 0.378 | 0.135 | 0.135 | 82.1% | +17.5% | 22 | 2 | 0 | 9 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.182 | 0.809 | 0.809 | 100.0% | +10.7% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.881 | 0.697 | 0.697 | 98.7% | -4.7% | 40 | 11 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.858 | 0.688 | 0.688 | 97.4% | +79.9% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.483 | 0.547 | 0.547 | 96.2% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.434 | 0.529 | 0.529 | 94.9% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 6 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.212 | 0.446 | 0.446 | 93.6% | -8.8% | 42 | 11 | 0 | 27 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.190 | 0.438 | 0.438 | 92.3% | +16.4% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.164 | 0.428 | 0.428 | 91.0% | +49.4% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.145 | 0.421 | 0.421 | 89.7% | +55.0% | 34 | 10 | 0 | 22 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.053 | 0.386 | 0.386 | 88.5% | +51.3% | 33 | 8 | 1 | 24 | 0 |
| 11 | ★★ | **APH** | Amphenol Corporation | Technology | 0.928 | 0.340 | 0.340 | 87.2% | +48.2% | 15 | 3 | 0 | 7 | 0 |
| 12 | ★★ | **AAPL** | Apple Inc. | Technology | 0.853 | 0.311 | 0.311 | 85.9% | +4.5% | 31 | 15 | 2 | 11 | 0 |
| 13 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 0.842 | 0.307 | 0.307 | 84.6% | +43.6% | 21 | 7 | 0 | 11 | 0 |
| 14 |  | **APP** | AppLovin Corporation | Communication Servic | 0.729 | 0.265 | 0.265 | 83.3% | +39.2% | 26 | 4 | 0 | 15 | 0 |
| 15 | ★★ | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 0.719 | 0.261 | 0.261 | 82.1% | +42.6% | 30 | 7 | 0 | 24 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.384 | 1.097 | 1.097 | 100.0% | +79.9% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 2.000 | 0.919 | 0.919 | 98.7% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.641 | 0.753 | 0.753 | 97.4% | +49.4% | 22 | 2 | 0 | 8 | 0 |
| 4 | ★★ | **APH** | Amphenol Corporation | Technology | 1.467 | 0.672 | 0.672 | 96.2% | +48.2% | 15 | 3 | 0 | 7 | 0 |
| 5 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.402 | 0.642 | 0.642 | 94.9% | +55.0% | 34 | 10 | 0 | 22 | 0 |
| 6 | ★★ | **ABT** | Abbott Laboratories | Healthcare | 1.376 | 0.629 | 0.629 | 93.6% | +43.6% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.227 | 0.560 | 0.560 | 92.3% | +51.3% | 33 | 8 | 1 | 24 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 1.205 | 0.550 | 0.550 | 91.0% | +38.2% | 28 | 1 | 0 | 13 | 0 |
| 9 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.189 | 0.543 | 0.543 | 89.7% | +26.4% | 21 | 2 | 0 | 3 | 0 |
| 10 | ★★ | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.179 | 0.538 | 0.538 | 88.5% | +42.6% | 30 | 7 | 0 | 24 | 0 |
| 11 |  | **BAC** | Bank of America Corporation | Financial Services | 1.026 | 0.467 | 0.467 | 87.2% | +24.2% | 22 | 3 | 0 | 9 | 0 |
| 12 |  | **AZN** | AstraZeneca PLC | Healthcare | 1.009 | 0.459 | 0.459 | 85.9% | +22.3% | 9 | 1 | 0 | 0 | 0 |
| 13 |  | **ACN** | Accenture plc | Technology | 0.927 | 0.421 | 0.421 | 84.6% | +43.2% | 18 | 10 | 0 | 12 | 0 |
| 14 |  | **DIS** | The Walt Disney Company | Communication Servic | 0.920 | 0.418 | 0.418 | 83.3% | +25.0% | 27 | 3 | 1 | 7 | 0 |
| 15 |  | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.903 | 0.410 | 0.410 | 82.1% | +15.7% | 10 | 1 | 0 | 3 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-11 17:57:23Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 17:57:18Z |  |
| stooq.prices | ok | 0 | 2026-05-11 15:47:33Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 15:47:22Z |  |
| stooq.prices | ok | 0 | 2026-05-11 12:31:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 12:31:42Z |  |
| stooq.prices | ok | 0 | 2026-05-11 09:37:48Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 09:37:39Z |  |
| stooq.prices | ok | 0 | 2026-05-11 05:43:06Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 05:43:01Z |  |
| stooq.prices | ok | 0 | 2026-05-11 01:29:46Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 01:29:39Z |  |
| edgar.13f | error | 0 | 2026-05-11 01:25:08Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-05-11 01:25:07Z |  |
| yfinance.actions | ok | 1153 | 2026-05-11 01:24:49Z |  |
| yfinance.consensus | ok | 79 | 2026-05-11 01:24:42Z |  |
| yfinance.fundamentals | ok | 80 | 2026-05-11 01:24:31Z |  |
| yfinance.prices | ok | 7110 | 2026-05-11 01:24:27Z |  |
| stooq.prices | ok | 0 | 2026-05-10 23:34:04Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-10 23:33:59Z |  |
