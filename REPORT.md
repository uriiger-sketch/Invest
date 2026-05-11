# Invest — Top 10 report

_Generated: **2026-05-11 17:59 UTC** · Scores as of: **2026-05-11**_

🟢 last successful crawl: 0 min ago (at 2026-05-11T17:59:29Z)

> Not investment advice. Ranks publicly available analyst consensus, price-target upside, rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended composite + ML score per horizon.

**High-conviction cross-horizon picks:** **AAPL**, **ABNB**, **AMD**, **BSX**, **CDNS**, **CHWY**, **CRDO**, **CRH**, **CRM**, **CRWD**, **CVX**, **DASH**, **DDOG**, **DHR**, **DOCN**, **ELV**

## How to read this

| Column | What it means |
|---|---|
| **#** | Rank (1 = highest blended score in this horizon). |
| **★★ / ★★★ / ★★★★** | Cross-horizon highlight. ★★ = this ticker ranks in two of the four top-10 lists; ★★★ = three of four; ★★★★ (very rare) = all four horizons agree. High-conviction names. |
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

## Next few hours — top 10

_Next few hours / next session. Fastest signal — leans almost entirely on short-term price momentum and very-recent rating changes. Heaviest risk penalty (intraday noise is large)._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.697 | 2.335 | 2.335 | 100.0% | -4.5% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.101 | 1.678 | 1.678 | 98.7% | +10.8% | 22 | 18 | 2 | 19 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.601 | 0.650 | 0.650 | 97.4% | +7.2% | 44 | 3 | 1 | 22 | 0 |
| 4 | ★★ | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.570 | 0.637 | 0.637 | 96.2% | +10.2% | 10 | 4 | 0 | 11 | 0 |
| 5 | ★★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.098 | 0.443 | 0.443 | 94.9% | -8.6% | 42 | 11 | 0 | 27 | 0 |
| 6 | ★★ | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.773 | 0.309 | 0.309 | 93.6% | +4.4% | 22 | 3 | 0 | 8 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.756 | 0.302 | 0.302 | 92.3% | +1.1% | 17 | 1 | 0 | 8 | 0 |
| 8 | ★★ | **AAPL** | Apple Inc. | Technology | 0.699 | 0.278 | 0.278 | 91.0% | +4.5% | 31 | 15 | 2 | 11 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 0.653 | 0.260 | 0.260 | 89.7% | +2.1% | 14 | 8 | 0 | 9 | 0 |
| 10 |  | **AMZN** | Amazon.com, Inc. | Consumer Cyclical | 0.457 | 0.179 | 0.179 | 88.5% | +15.0% | 62 | 4 | 0 | 29 | 0 |


## Daily (~5 trading days) — top 10

_About a week of holding (5 trading days). Same flavour as 'hours' but with more weight on 30-day rating momentum and the consensus snapshot._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 5.250 | 1.986 | 1.986 | 100.0% | -4.5% | 40 | 11 | 0 | 22 | 0 |
| 2 | ★★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 4.005 | 1.513 | 1.513 | 98.7% | +10.8% | 22 | 18 | 2 | 19 | 0 |
| 3 | ★★ | **DDOG** | Datadog, Inc. | Technology | 1.558 | 0.584 | 0.584 | 97.4% | +7.2% | 44 | 3 | 1 | 22 | 0 |
| 4 | ★★ | **DOCN** | DigitalOcean Holdings, Inc. | Technology | 1.551 | 0.581 | 0.581 | 96.2% | +10.2% | 10 | 4 | 0 | 11 | 0 |
| 5 | ★★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.487 | 0.556 | 0.556 | 94.9% | -8.6% | 42 | 11 | 0 | 27 | 0 |
| 6 | ★★ | **AAPL** | Apple Inc. | Technology | 0.873 | 0.323 | 0.323 | 93.6% | +4.5% | 31 | 15 | 2 | 11 | 0 |
| 7 | ★★ | **CRDO** | Credo Technology Group Holding Ltd | Technology | 0.808 | 0.299 | 0.299 | 92.3% | +1.1% | 17 | 1 | 0 | 8 | 0 |
| 8 | ★★ | **CDNS** | Cadence Design Systems, Inc. | Technology | 0.713 | 0.262 | 0.262 | 91.0% | +4.4% | 22 | 3 | 0 | 8 | 0 |
| 9 | ★★ | **ELV** | Elevance Health, Inc. | Healthcare | 0.664 | 0.244 | 0.244 | 89.7% | +2.1% | 14 | 8 | 0 | 9 | 0 |
| 10 | ★★ | **CVX** | Chevron Corporation | Energy | 0.622 | 0.228 | 0.228 | 88.5% | +16.4% | 18 | 6 | 1 | 11 | 0 |


## Weekly (~1 month) — top 10

_About a month of holding (20 trading days). Balanced mix of consensus, price-target upside, rating momentum and price trend._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★★ | **ABNB** | Airbnb, Inc. | Consumer Cyclical | 2.182 | 0.809 | 0.809 | 100.0% | +10.8% | 22 | 18 | 2 | 19 | 0 |
| 2 | ★★★ | **AMD** | Advanced Micro Devices, Inc. | Technology | 1.889 | 0.699 | 0.699 | 98.7% | -4.5% | 40 | 11 | 0 | 22 | 0 |
| 3 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 1.856 | 0.687 | 0.687 | 97.4% | +80.0% | 20 | 5 | 0 | 12 | 0 |
| 4 | ★★ | **CRH** | CRH plc | Basic Materials | 1.479 | 0.546 | 0.546 | 96.2% | +26.3% | 21 | 2 | 0 | 3 | 0 |
| 5 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.430 | 0.527 | 0.527 | 94.9% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 6 | ★★★ | **CRWD** | CrowdStrike Holdings, Inc. | Technology | 1.216 | 0.447 | 0.447 | 93.6% | -8.6% | 42 | 11 | 0 | 27 | 0 |
| 7 | ★★ | **CVX** | Chevron Corporation | Energy | 1.188 | 0.437 | 0.437 | 92.3% | +16.4% | 18 | 6 | 1 | 11 | 0 |
| 8 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.163 | 0.428 | 0.428 | 91.0% | +49.5% | 22 | 2 | 0 | 8 | 0 |
| 9 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.142 | 0.420 | 0.420 | 89.7% | +54.9% | 34 | 10 | 0 | 22 | 0 |
| 10 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.053 | 0.386 | 0.386 | 88.5% | +51.4% | 33 | 8 | 1 | 24 | 0 |


## Month and above (~90 days) — top 10

_A quarter or more (90+ trading days). Leans on analyst consensus, price-target upside, and institutional (13F) flow; actively de-weights short-term price chase._

| # | ★ | Ticker | Name | Sector | Blended | Composite | ML | Pctile | Upside | Buy | Hold | Sell | Firms | Insts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ★★ | **CHWY** | Chewy, Inc. | Consumer Cyclical | 2.385 | 1.097 | 1.097 | 100.0% | +80.0% | 20 | 5 | 0 | 12 | 0 |
| 2 | ★★ | **BSX** | Boston Scientific Corporation | Healthcare | 1.999 | 0.918 | 0.918 | 98.7% | +58.8% | 31 | 2 | 0 | 16 | 0 |
| 3 | ★★ | **DHR** | Danaher Corporation | Healthcare | 1.645 | 0.754 | 0.754 | 97.4% | +49.5% | 22 | 2 | 0 | 8 | 0 |
| 4 |  | **APH** | Amphenol Corporation | Technology | 1.472 | 0.673 | 0.673 | 96.2% | +48.4% | 15 | 3 | 0 | 7 | 0 |
| 5 | ★★ | **DASH** | DoorDash, Inc. | Consumer Cyclical | 1.399 | 0.640 | 0.640 | 94.9% | +54.9% | 34 | 10 | 0 | 22 | 0 |
| 6 |  | **ABT** | Abbott Laboratories | Healthcare | 1.374 | 0.628 | 0.628 | 93.6% | +43.6% | 21 | 7 | 0 | 11 | 0 |
| 7 | ★★ | **CRM** | Salesforce, Inc. | Technology | 1.229 | 0.561 | 0.561 | 92.3% | +51.4% | 33 | 8 | 1 | 24 | 0 |
| 8 |  | **ANET** | Arista Networks, Inc. | Technology | 1.207 | 0.551 | 0.551 | 91.0% | +38.3% | 28 | 1 | 0 | 13 | 0 |
| 9 | ★★ | **CRH** | CRH plc | Basic Materials | 1.186 | 0.541 | 0.541 | 89.7% | +26.3% | 21 | 2 | 0 | 3 | 0 |
| 10 |  | **BKNG** | Booking Holdings Inc. | Consumer Cyclical | 1.178 | 0.537 | 0.537 | 88.5% | +42.6% | 30 | 7 | 0 | 24 | 0 |


## Recent pipeline runs

| Job | Status | Rows | Started | Error |
|---|---|---:|---|---|
| stooq.prices | ok | 0 | 2026-05-11 17:59:28Z |  |
| yfinance.prices_fast | ok | 7110 | 2026-05-11 17:59:19Z |  |
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
