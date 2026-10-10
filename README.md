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

1. **Crawls free data sources** on a schedule (every stage time-budgeted,
   rate-limit-governed, and skipping dormant/delisted symbols):
   - **Yahoo Finance** — one quoteSummary request per ticker returns:
     recommendation counts *and their 1–3-month trend*, price targets (mean,
     median, high/low), every firm's rating **and price-target change**, EPS
     estimate trend and up/down revisions, earnings surprises and the next
     report date, valuation, profitability, short interest, 52-week range.
     Plus OHLCV prices (a full year on the nightly deep run).
   - **News** — Yahoo Finance's stream for every ticker, Google News RSS for
     the names on (or near) the published table; each headline is scored
     with a finance-specific lexicon and deduplicated across feeds.
   - **SEC EDGAR** — 13F holdings of ~110 institutional filers (two report
     periods, so quarter-over-quarter flow is always computable), Form 4
     insider trades, and each issuer's filing stream (8-K red-flag items,
     late-filing notices, 13D activist stakes, offerings).
   - Finnhub / FMP when API keys are configured; stooq as a fail-fast price
     fallback for recently-live US names.
2. **Stores** everything in SQLite (`data/invest.db`, committed so state
   survives between runs; `invest maintain` prunes and VACUUMs it).
3. **Engineers ~25 features** per ticker across sell-side opinion, earnings
   revisions, news tone, smart money, events, fundamentals and price — with
   sanity checks (one-day price spikes dropped, mis-scaled targets discarded).
4. **Grades** every stock with a calibrated model (below) and blends in a
   LightGBM ranker only in proportion to its out-of-sample skill.
5. **Publishes** one table ordered by the integrated grade, with expected
   1-month excess return, probability of beating the universe, data
   confidence, news tone and 30-day opinion change, plus a per-row drawer
   with the evidence (drivers, analyst actions with target changes,
   headlines, estimates, SEC filings).

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

- `PRIOR_IC` — per-horizon prior information coefficient of every feature
  (the calibrated weights are derived from these plus measured history).
- `prior_ic_sd`, `corr_shrinkage`, `ic_haircut` — calibration strength.
- `blend_ml_weight` — cap on the ML ranker's share of the blend.
- `crawl_workers`, `coverage_budget_seconds`, `news_budget_seconds`,
  `sec_budget_seconds`, `focus_size`, `dormant_after_days` — crawl tuning.
- `*_retention_days` — history kept in the committed database.
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

## How the grade is built

The model follows standard cross-sectional alpha construction
(Grinold & Kahn):

1. **Standardise.** Each feature is rank-normalised to N(0,1) across the
   universe (robust to outliers by construction). Valuation, profitability,
   short interest and target upside are partially sector-neutralised.
   Unobserved data stays missing and contributes z = 0 — the prior mean —
   instead of a fabricated value.
2. **Prior information coefficients.** Each feature carries a literature
   prior IC per horizon (`PRIOR_IC` in `config.py`, with references): e.g.
   EPS revisions, consensus *changes* and target revisions positive; short
   interest, analyst disagreement and 1-week moves (short-term reversal)
   negative; value, profitability and 12-1 momentum mainly at long horizons.
3. **Bayesian calibration.** Daily cross-sectional Spearman ICs measured on
   our own stored feature snapshots vs realised forward returns update the
   priors by precision weighting (standard errors corrected for overlapping
   windows). Signals that do not work in this universe lose weight.
4. **Correlation-aware weights:** `w = C⁻¹ · IC` with C the (shrunk)
   cross-sectional correlation of the features, so correlated signals share
   weight instead of double-counting.
5. **ML blend.** The LightGBM ranker (target: cross-sectional rank of the
   forward return; purged walk-forward validation with an embargo) is
   weighted by its out-of-sample IC, capped at `blend_ml_weight`; zero until
   it has proven skill.
6. **Integrated grade.** The four horizon scores S_h are combined with
   weights equal to each horizon's estimated skill and their correlation R:

   ```
   G = Σ_h a_h S_h / √(aᵀ R a)        a_h = posterior IC of horizon h
   α_h = IC_h · σ_h · S_h             expected excess return (Grinold)
   P(beat) = Φ(IC_h · S_h)
   ```

   G is ≈ N(0,1) across the gated universe; the letter grade is its
   percentile (A+ ≥ 97th … D < 15th). Confidence = share of the model's
   weight backed by observed data for that stock.

Hard gates still apply first: liquidity, data quality (stale price, short
history, absurd or mis-scaled targets), net-bullish consensus, ≥ 4 % upside
and coverage floors. A small, explicit technology tilt remains as a
tiebreaker (`theme_tilt_*`).

Honest scale: realistic ICs are 0.02–0.08, so even an A+ implies only a
modestly-above-50 % chance of beating the universe over a month. The page
shows the calibration (ex-ante vs realised IC per horizon) under *Data
health & model calibration*.

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
make test            # unit tests: crawl reliability, intel parsing, features, grading model, report
make maintain        # prune expired history + VACUUM the database
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
│   ├── sentiment.py         # finance-lexicon headline tone
│   ├── sources/
│   │   ├── base.py          # retries, token bucket, rate governor, run_log
│   │   ├── yfinance_src.py  # prices + single-request company intel sweep
│   │   ├── news_src.py      # Yahoo + Google News headlines, dedupe
│   │   ├── edgar_src.py     # 13F, Form 4, issuer filing stream (SEC)
│   │   ├── stooq_src.py     # fail-fast price fallback
│   │   └── finnhub_src.py / fmp_src.py   # optional keyed feeds
│   ├── pipeline/
│   │   ├── ingest.py        # orchestrator: budgets, dormant skip, focus list
│   │   ├── features.py      # ~25 features + sanity filters + snapshots
│   │   ├── score.py         # rank-Gaussian standardisation, gates, composite
│   │   ├── grade.py         # IC calibration, weights, blend, integrated grade
│   │   ├── ml_rank.py       # LightGBM ranker, purged validation
│   │   ├── rank.py          # end-to-end ranking + persistence
│   │   └── maintenance.py   # retention pruning + VACUUM
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
