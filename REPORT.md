# Invest — Top 15 report

_Generated: **2026-04-22 14:13 UTC** · Scores as of: **2026-04-22**_

🟢 last successful crawl: 0 min ago (at 2026-04-22T14:13:31Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **BAC**, **BUD**, **CHWY**, **CI**, **CRDO**, **CRH**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DIS**, **DKNG**, **FROG**

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
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 3.792 | 1.612 | 1.612 | 100.0% | +10.2% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 3.217 | 1.367 | 1.367 | 98.7% | +12.4% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 2.355 | 1.000 | 1.000 | 97.4% | +21.3% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 2.063 | 0.875 | 0.875 | 96.2% | +11.9% | 16 | 1 | 0 | 7 | 0 |
| 5 |  | **BP** | BP p.l.c. | Energy | 1.628 | 0.690 | 0.690 | 94.9% | +3.4% | 8 | 7 | 3 | 5 | 0 |
| 6 |  | **AFRM** | Affirm Holdings, Inc. | Financial Services | 1.142 | 0.482 | 0.482 | 93.6% | +17.3% | 23 | 8 | 0 | 12 | 0 |
| 7 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.108 | 0.468 | 0.468 | 92.3% | +6.6% | 41 | 12 | 0 | 27 | 0 |
| 8 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 0.966 | 0.408 | 0.408 | 91.0% | +21.2% | 27 | 3 | 1 | 7 | 0 |
| 9 |  | **AMD** | Advanced Micro Devices, Inc. | Technology | 0.925 | 0.390 | 0.390 | 89.7% | +1.0% | 36 | 13 | 0 | 16 | 0 |
| 10 |  | **CLS** | Celestica Inc. | Technology | 0.835 | 0.352 | 0.352 | 88.5% | -2.3% | 18 | 2 | 0 | 6 | 0 |
| 11 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.757 | 0.318 | 0.318 | 87.2% | +11.6% | 63 | 5 | 0 | 27 | 0 |
| 12 |  | **ANET** | Arista Networks, Inc. | Technology | 0.734 | 0.309 | 0.309 | 85.9% | +3.1% | 27 | 3 | 0 | 11 | 0 |
| 13 |  | **ADI** | Analog Devices, Inc. | Technology | 0.695 | 0.292 | 0.292 | 84.6% | +3.0% | 29 | 6 | 0 | 16 | 0 |
| 14 |  | **ARM** | Arm Holdings plc | Technology | 0.693 | 0.291 | 0.291 | 83.3% | -7.1% | 27 | 10 | 2 | 18 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.580 | 0.243 | 0.243 | 82.1% | +16.7% | 21 | 3 | 0 | 10 | 0 |


## Weeks horizon — top 15

_20-day (~1 month) holding. Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **AAPL** | Apple Inc. | Technology | 2.328 | 0.928 | 0.928 | 100.0% | +10.2% | 31 | 14 | 2 | 12 | 0 |
| 2 | ★★ | **CVX** | Chevron Corporation | Energy | 2.272 | 0.905 | 0.905 | 98.7% | +12.4% | 18 | 6 | 1 | 9 | 0 |
| 3 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.921 | 0.765 | 0.765 | 97.4% | +21.3% | 20 | 2 | 0 | 3 | 0 |
| 4 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.709 | 0.680 | 0.680 | 96.2% | +21.2% | 27 | 3 | 1 | 7 | 0 |
| 5 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.516 | 0.602 | 0.602 | 94.9% | +52.4% | 21 | 5 | 0 | 12 | 0 |
| 6 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.501 | 0.597 | 0.597 | 93.6% | +47.9% | 20 | 1 | 0 | 9 | 0 |
| 7 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.154 | 0.457 | 0.457 | 92.3% | +36.6% | 44 | 3 | 1 | 20 | 0 |
| 8 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.044 | 0.413 | 0.413 | 91.0% | +54.9% | 28 | 7 | 0 | 22 | 0 |
| 9 | ★★ | **DHR** | Danaher Corporation | Healthcare | 0.985 | 0.390 | 0.390 | 89.7% | +34.9% | 22 | 2 | 0 | 6 | 0 |
| 10 | ★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 0.959 | 0.379 | 0.379 | 88.5% | +6.6% | 41 | 12 | 0 | 27 | 0 |
| 11 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 0.945 | 0.374 | 0.374 | 87.2% | +21.9% | 10 | 1 | 0 | 2 | 0 |
| 12 |  | **DE** | Deere & Company | Industrials | 0.937 | 0.371 | 0.371 | 85.9% | +12.7% | 13 | 11 | 0 | 13 | 0 |
| 13 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.917 | 0.362 | 0.362 | 84.6% | +11.9% | 16 | 1 | 0 | 7 | 0 |
| 14 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 0.913 | 0.361 | 0.361 | 83.3% | +37.6% | 35 | 10 | 0 | 20 | 0 |
| 15 | ★★ | **CI** | The Cigna Group | Healthcare | 0.773 | 0.305 | 0.305 | 82.1% | +20.8% | 22 | 2 | 0 | 8 | 0 |


## Months horizon — top 15

_90-day holding. Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | **BSX** | Boston Scientific Corporation | Healthcare | 1.914 | 0.849 | 0.849 | 100.0% | +48.9% | 32 | 1 | 0 | 18 | 0 |
| 2 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.778 | 0.788 | 0.788 | 98.7% | +52.4% | 21 | 5 | 0 | 12 | 0 |
| 3 | ★★ | **DKNG** | DraftKings Inc. | Consumer Cyclical | 1.741 | 0.772 | 0.772 | 97.4% | +54.9% | 28 | 7 | 0 | 22 | 0 |
| 4 | ★★ | **FROG** | JFrog Ltd. | Technology | 1.555 | 0.688 | 0.688 | 96.2% | +47.9% | 20 | 1 | 0 | 9 | 0 |
| 5 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.497 | 0.662 | 0.662 | 94.9% | +34.9% | 22 | 2 | 0 | 6 | 0 |
| 6 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.329 | 0.588 | 0.588 | 93.6% | +36.6% | 44 | 3 | 1 | 20 | 0 |
| 7 | ★★ | **BUD** | Anheuser-Busch InBev SA/NV | Consumer Defensive | 1.312 | 0.580 | 0.580 | 92.3% | +21.9% | 10 | 1 | 0 | 2 | 0 |
| 8 |  | **CRM** | Salesforce, Inc. | Technology | 1.251 | 0.552 | 0.552 | 91.0% | +41.8% | 35 | 10 | 1 | 24 | 0 |
| 9 |  | **ABT** | Abbott Laboratories | Healthcare | 1.250 | 0.552 | 0.552 | 89.7% | +27.9% | 22 | 6 | 0 | 13 | 0 |
| 10 | ★★★ | **DIS** | The Walt Disney Company | Communication Servic | 1.213 | 0.536 | 0.536 | 88.5% | +21.2% | 27 | 3 | 1 | 7 | 0 |
| 11 | ★★ | **CI** | The Cigna Group | Healthcare | 1.074 | 0.473 | 0.473 | 87.2% | +20.8% | 22 | 2 | 0 | 8 | 0 |
| 12 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.036 | 0.456 | 0.456 | 85.9% | +37.6% | 35 | 10 | 0 | 20 | 0 |
| 13 | ★★★ | **CRH** | CRH plc | Basic Materials | 1.014 | 0.446 | 0.446 | 84.6% | +21.3% | 20 | 2 | 0 | 3 | 0 |
| 14 |  | **ABBV** | AbbVie Inc. | Healthcare | 0.895 | 0.393 | 0.393 | 83.3% | +22.0% | 23 | 9 | 0 | 11 | 0 |
| 15 | ★★ | **BAC** | Bank of America Corporation | Financial Services | 0.837 | 0.367 | 0.367 | 82.1% | +16.7% | 21 | 3 | 0 | 10 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-04-22 14:13:30Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 14:13:25Z |  |
| stooq.prices | ok | 0 | 2026-04-22 12:11:25Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 12:11:19Z |  |
| stooq.prices | ok | 0 | 2026-04-22 11:05:05Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 11:05:00Z |  |
| stooq.prices | ok | 0 | 2026-04-22 09:55:59Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 09:55:54Z |  |
| stooq.prices | ok | 0 | 2026-04-22 08:03:12Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 08:03:07Z |  |
| stooq.prices | ok | 0 | 2026-04-22 05:59:55Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 05:59:51Z |  |
| stooq.prices | ok | 0 | 2026-04-22 03:44:47Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 03:44:42Z |  |
| stooq.prices | ok | 0 | 2026-04-22 00:06:38Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-04-22 00:06:30Z |  |
| edgar.13f | error | 0 | 2026-04-22 00:04:22Z | IntegrityError: (raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flus |
| stooq.prices | ok | 0 | 2026-04-22 00:04:22Z |  |
| yfinance.actions | ok | 1022 | 2026-04-22 00:04:10Z |  |
| yfinance.consensus | ok | 79 | 2026-04-22 00:04:01Z |  |
