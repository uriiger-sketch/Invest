# <img src="docs/favicon.svg" width="28" alt="Invest icon" align="top"> Invest — autonomous stock ranking crawler

**📈 Live report (permanent link — same address every deployment):**
**<https://uriiger-sketch.github.io/Invest/>**

The Markdown snapshot lives at [`REPORT.md`](REPORT.md); both refresh
automatically every 2 hours via GitHub Actions.

A small, always-on crawler that ingests what the world's top investment
houses, funds, and sell-side analysts are publicly saying about the stock
market, then distils it into a ranked **top-13** list of stocks across four
horizons — **next few hours / daily / weekly / month and above** — with a
transparent, testable score and an optional ML re-ranker layered on top.

> **Not investment advice.** This tool summarises publicly available data to
> help you build a shortlist for further research. Paywalled analyst reports
> are never scraped; only the publicly aggregated buy/hold/sell counts and
> price-target numbers. Past signal does not predict future return.

---

## What it does

1. **Crawls free data sources** on a schedule:
   - `yfinance` — OHLCV prices, fundamentals, analyst consensus, price targets,
     rating actions.
   - Finnhub (free tier, 60 req/min — optional key) — same signals with firm +
     analyst names on rating actions.
   - SEC EDGAR — 13F-HR holdings from ~20 tracked institutional filers
     (Berkshire, BlackRock, Vanguard, Bridgewater, Renaissance, Citadel,
     Point72, Tiger Global, ARK, …) and Form 4 insider-trade activity.
2. **Stores** everything in a local SQLite DB (`data/invest.db`), idempotently.
3. **Engineers features** per ticker: consensus score, upside to target, rating
   momentum (7 d / 30 d), target revision, institutional flow, insider flow,
   price momentum, realised-volatility risk penalty, liquidity filter.
4. **Scores** each ticker with a horizon-specific weighted composite, and
   blends that with an **ML ranker** (LightGBM regressor trained on realised
   forward returns). Cold-start safe — until enough snapshots exist, the ML
   score falls back to the composite so the blended number is always defined.
5. **Serves** a **Streamlit dashboard** on `http://localhost:8501` with:
   - Top 20 per horizon
   - Ticker drill-down (price, consensus over time, rating actions, 13F flow,
     insider trades)
   - Sources & freshness (last successful run per job, error log)
   - Methodology (live weight matrix and blend ratio from `config.py`)

---

## Quick start

```bash
# 1. install
make install           # pip install -e ".[dev]"
cp .env.example .env   # fill FINNHUB_API_KEY (optional) + SEC_USER_AGENT

# 2. first-run ingest + rank (run once, then let the scheduler take over)
make migrate           # alembic upgrade head
make ingest            # pulls data; takes a while for full universe
make rank              # scores + persists top-20 per horizon

# 3. dashboard (also starts the background scheduler)
make serve             # starts Streamlit + APScheduler on :8501
```

Or with Docker:

```bash
make docker-build
make docker-up         # runs `serve` inside the container
# then open http://localhost:8501
```

---

## Configuration

All knobs live in [`src/invest/config.py`](src/invest/config.py):

- `WEIGHTS` — per-horizon weights for each of the 9 scoring features. Editable.
- `blend_composite_weight` / `blend_ml_weight` — mix of composite and ML.
- `top_n` — number of stocks shown per horizon (default **20**).
- `liquidity_min_dollar_volume` — stocks below this 20-day dollar volume are
  excluded from the ranking.
- `universe_max` (env `UNIVERSE_MAX`) — cap the number of tickers ingested
  (0 = no cap; use the full S&P 500 ∪ NDX 100 union).

Env vars (in `.env`):

| Var | Purpose |
|---|---|
| `FINNHUB_API_KEY` | Optional free-tier key for richer analyst coverage. |
| `SEC_USER_AGENT` | Required by SEC — must include a contact email. |
| `SCRAPE_OK` | Enable ToS-gray scrapers (off by default). |
| `INVEST_DB_URL` | SQLite path (default `sqlite:///data/invest.db`). |
| `STREAMLIT_PORT` | Dashboard port (default `8501`). |
| `RUN_SCHEDULER` | `true` / `false` — run APScheduler inside `serve`. |

---

## How the score is built

Each feature is z-scored across the universe (clipped to ±5) and combined with
weights that depend on the horizon:

| Feature | Days | Weeks | Months |
|---|---:|---:|---:|
| consensus_z (weighted buy/hold/sell) | 0.10 | 0.20 | 0.30 |
| upside_z (mean target / last close − 1) | 0.05 | 0.20 | 0.25 |
| rating_mom_7d | 0.25 | 0.10 | 0.00 |
| rating_mom_30d | 0.10 | 0.15 | 0.05 |
| target_revision_30d | 0.05 | 0.10 | 0.10 |
| inst_flow_13f | 0.00 | 0.05 | 0.15 |
| insider_net_buy_90d | 0.05 | 0.10 | 0.10 |
| price_mom_21d | 0.25 | 0.10 | −0.05 |
| risk_penalty (−60 d realised vol) | 0.15 | 0.10 | 0.10 |

Blended score:
```
blended = 0.6 · z(composite) + 0.4 · z(ml)
```

The ML component is a LightGBM regressor per horizon trained on your own stored
feature snapshots against realised 5-day / 20-day / 90-day forward returns.
Until ≥ 60 daily snapshots exist, `ml_score := composite_score`.

---

## Scheduler

APScheduler runs inside the `serve` process (toggle via `RUN_SCHEDULER`):

| Job | Cadence |
|---|---|
| `ingest_prices` | every 30 min, Mon–Fri 09:30–16:00 ET |
| `ingest_all` (ratings, fundamentals, EDGAR) | every 6 h |
| `compute_scores` | daily 18:30 ET |
| `train_ml` | daily 19:00 ET |
| `refresh_universe` | Sunday 03:00 ET |

All jobs write a row to the `run_log` table. The **Sources & freshness** page
in the dashboard surfaces last-success time, row counts, and recent errors.

---

## Verification

```bash
make test            # unit tests: scoring, features, run-log, universe, rate-limiter
make ingest          # end-to-end: populates SQLite
make rank            # produces top-20 per horizon in the terminal + DB
make dashboard       # opens http://localhost:8501
python scripts/backtest.py   # sanity check: Spearman IC per horizon
```

Sanity thresholds to watch:
- Sum of (strong_buy + buy + hold + sell + strong_sell) ≈ `num_analysts`.
- `upside_z` mean across the universe is near 0; no single z > ~8.
- `scripts/backtest.py` reports Spearman IC > 0.03 across horizons on average.

---

## Project layout

```
Invest/
├── pyproject.toml           # uv / pip; deps pinned by major
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── alembic/                 # initial schema migration
├── src/invest/
│   ├── config.py            # weights, blend ratio, env
│   ├── db.py                # engine + session helper
│   ├── models.py            # SQLAlchemy ORM
│   ├── universe.py          # S&P500 ∪ NDX100 with static fallback
│   ├── sources/
│   │   ├── base.py          # retries, token bucket, run_log
│   │   ├── yfinance_src.py  # primary free source
│   │   ├── finnhub_src.py   # optional free-tier rating feed
│   │   └── edgar_src.py     # 13F + Form 4 from SEC
│   ├── pipeline/
│   │   ├── ingest.py        # orchestrator
│   │   ├── features.py      # per-ticker feature engineering
│   │   ├── score.py         # composite scoring
│   │   ├── ml_rank.py       # LightGBM + cold-start fallback
│   │   └── rank.py          # blend + persist + top-N
│   ├── scheduler.py         # APScheduler cadences
│   ├── dashboard.py         # Streamlit (4 pages)
│   └── cli.py               # `invest ingest | rank | train | serve`
├── scripts/backtest.py
└── tests/                   # pytest with in-memory SQLite
```

---

## Legal & ToS

- We only ingest publicly aggregated / free-tier data per each provider's ToS.
  **Paywalled analyst research is never scraped.**
- SEC EDGAR access includes the `User-Agent` header required by
  <https://www.sec.gov/os/accessing-edgar-data>.
- yfinance uses unofficial Yahoo endpoints — requests are batched and throttled
  to be polite; the source is optional and easy to swap.
- ToS-gray scrapers (Finviz) are stubbed and disabled by default behind the
  `SCRAPE_OK` flag.
