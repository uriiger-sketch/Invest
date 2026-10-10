from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Four horizons.
#   hours   — "next few hours": fastest signal, heavy on price + rating momentum.
#             Approximated with a 1-day forward window since the free price feeds
#             are daily.
#   daily   — 5 trading days (~ a week of holding).
#   weekly  — 20 trading days (~ a month of holding).
#   monthly — 90 trading days (~ a quarter; "month and above" investments).
Horizon = Literal["hours", "daily", "weekly", "monthly"]
HORIZONS: tuple[Horizon, ...] = ("hours", "daily", "weekly", "monthly")

FORWARD_WINDOW_DAYS: dict[Horizon, int] = {
    "hours": 1,
    "daily": 5,
    "weekly": 20,
    "monthly": 90,
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    finnhub_api_key: str = Field(default="", alias="FINNHUB_API_KEY")
    sec_user_agent: str = Field(
        default="Invest Research Client <you@example.com>", alias="SEC_USER_AGENT"
    )
    scrape_ok: bool = Field(default=False, alias="SCRAPE_OK")

    db_url: str = Field(default="sqlite:///data/invest.db", alias="INVEST_DB_URL")
    universe_max: int = Field(default=0, alias="UNIVERSE_MAX")
    streamlit_port: int = Field(default=8501, alias="STREAMLIT_PORT")
    run_scheduler: bool = Field(default=True, alias="RUN_SCHEDULER")

    liquidity_min_dollar_volume: float = 5_000_000.0
    # Quality gates: a stock is excluded from the top-N if its analyst outlook
    # is meaningfully negative on any of these axes. Tunable here so users can
    # be stricter or looser without code changes.
    min_consensus_z: float = 0.0     # require strictly net-bullish consensus
    min_upside: float = 0.04         # require ≥ 4 % upside to consensus target
    min_firms: int = 5               # require at least 5 covering firms IF the ticker has any consensus
    # Distinct contributors required, as computed in features.build_features:
    #   max(covering analysts, named rating-changers in 90 d) + 13F filers + insider filers
    #
    # CALIBRATION NOTE — two separate miscalibrations have killed this gate:
    #   1. The threshold was 50 while the metric could not exceed ~28.
    #   2. The metric itself counted only *named* firms from the 90-day
    #      upgrade/downgrade feed, so a database restored from empty scored
    #      every ticker at 0 regardless of how many analysts actually covered
    #      it. Both rejected 100 % of the universe, which meant no Score rows
    #      were persisted at all.
    # 12 covering desks is a real bar that well-followed US names clear
    # comfortably while still admitting the better-covered Israeli and
    # European listings. Raising it above ~20 will start excluding those.
    # `invest rank` now fails loudly if any gate wipes out the whole universe.
    min_total_sources: int = 12
    consensus_max_age_days: int = 14 # ignore Consensus rows older than this

    # Data-quality gates — reliability hardening. A ticker is excluded when its
    # underlying market data can't be trusted, regardless of how bullish the
    # analyst signal looks:
    stale_price_max_days: int = 7      # last close older than this → excluded
    min_price_history_days: int = 60   # need this much history for vol/momentum to mean anything
    max_upside_sane: float = 2.0       # upside > 200 % almost always means stale/wrong target data → excluded
    upside_cap: float = 0.75           # cap upside used in SCORING at 75 % so one outlier can't dominate

    # Analyst-reliability shrinkage: consensus_z is multiplied by n/(n+k) so a
    # 3-analyst unanimous "buy" doesn't outrank a 30-analyst 80 %-buy.
    consensus_shrinkage_k: float = 10.0

    # Diversification: cap how many names from one sector can occupy a single
    # horizon's top list (0 = no cap). Prevents an all-semis top list.
    # Scaled with `top_n` below: 8 of 30 keeps any one sector under ~27 % of a
    # horizon while leaving room for the technology emphasis the theme tilt
    # applies. (Counter-intuitively a TIGHTER cap yields a LARGER cross-horizon
    # union — it forces each horizon deeper into other sectors — but at the
    # cost of pushing out genuinely strong same-sector names.)
    max_per_sector: int = 8

    # Composite vs ML blend. These are no longer fixed weights: the blend is
    # the information-coefficient-optimal combination of the two signals
    # (see pipeline/grade.py), and the ML model only gets weight once its
    # purged out-of-sample IC is credibly positive. `blend_ml_weight` is the
    # CAP on the ML share, so an over-fitted model can never dominate.
    blend_composite_weight: float = 0.6
    blend_ml_weight: float = 0.4

    # ---------------------------- crawl ----------------------------
    # Concurrent Yahoo workers. Each ticker costs ONE quoteSummary request
    # (all analyst / estimate / fundamental modules at once) plus one news
    # request, so 4 workers keep a ~600-name sweep to a few minutes while
    # staying far below Yahoo's rate limits.
    crawl_workers: int = 4
    # Wall-clock budgets per crawl stage. Every stage is ordered so a
    # truncated run still makes progress (stalest-first / focus-first), and
    # the sum stays well inside the workflow's 25-minute fast-ingest limit —
    # the old unbounded stooq fallback alone burned 26 minutes on dead
    # tickers and killed whole runs.
    news_budget_seconds: float = 180.0
    sec_budget_seconds: float = 150.0
    stooq_budget_seconds: float = 45.0
    form4_budget_seconds: float = 720.0
    # "Focus list": the names currently on (or just below) the published
    # table get the expensive per-company intel (Google News, SEC filing
    # stream) on EVERY run, not just the nightly deep run.
    focus_size: int = 90
    # A ticker with no price for this many days is dormant (delisted,
    # acquired, renamed). Dormant names are skipped by the per-ticker sweeps
    # instead of costing retries on every run.
    dormant_after_days: int = 10
    # Union the live S&P 500 + NASDAQ-100 membership into the universe.
    include_index_constituents: bool = Field(default=True, alias="INCLUDE_INDEX_CONSTITUENTS")
    # Price history window: the nightly deep run re-downloads a full year so
    # split adjustments propagate to every stored row and 12-month momentum
    # is computable; the fast loop only needs the recent quarter.
    deep_price_period: str = "1y"
    fast_price_period: str = "3mo"

    # ------------------------- data sanity -------------------------
    # Yahoo's own quote vs our stored close. A gap this large means the
    # target is in a different currency/ADR ratio than the price (observed:
    # ENLV target 80 vs price 0.30, UMC target in the wrong unit).
    target_price_mismatch_tol: float = 0.35
    # Price must sit inside [low_target / k, high_target * k]; outside it the
    # target set is stale or mis-scaled.
    target_band_factor: float = 3.0

    # --------------------------- news ---------------------------
    news_half_life_days: float = 2.0     # recency decay of headline tone
    news_shrinkage_k: float = 1.5        # pseudo-count shrinking sparse news to neutral
    news_lookback_days: int = 10

    # ------------------------- retention -------------------------
    # The SQLite file is committed to git on every run; GitHub rejects files
    # over 100 MB. These keep it bounded (see `invest maintain`).
    feature_retention_days: int = 365
    score_retention_days: int = 365
    daily_history_days: int = 60     # older daily history is thinned to weekly
    news_retention_days: int = 14
    run_log_retention_days: int = 45
    filing_retention_days: int = 400
    db_size_warn_mb: float = 70.0

    # -------------------------- grading --------------------------
    # Prior uncertainty (SD) of every factor IC in PRIOR_IC below. Measured
    # ICs from our own snapshot history update these priors by precision
    # weighting; with little history the posterior stays at the prior.
    prior_ic_sd: float = 0.02
    # Shrinkage of the cross-sectional factor correlation matrix toward the
    # identity before inverting it for the IC-optimal weights.
    corr_shrinkage: float = 0.5
    # Haircut on the ex-ante composite IC implied by the priors (estimation
    # error, crowding, publication decay — McLean & Pontiff 2016).
    ic_haircut: float = 0.5
    # Minimum number of dated cross-sections before measured ICs are used.
    min_ic_dates: int = 5
    # Per-horizon depth. This is the real driver of how many distinct names
    # reach the merged table, because that table is the UNION of the four
    # horizons' lists, and the union is what `main_table_size` caps.
    #
    # Measured against five consecutive days of live scores (229 tickers
    # clearing the gates per horizon), union size is very stable and lands
    # around 1.85x top_n:
    #     top_n=13 -> ~28   (why the "top 30" table never actually hit 30)
    #     top_n=30 -> 56-59 (only ~14 % over a 50-row table)
    #     top_n=35 -> 65-67 (~30 % headroom — what we use)
    # Keep enough margin that a day with heavier cross-horizon overlap still
    # fills the table from real selections rather than scraping its tail.
    top_n: int = 35

    # Theme tilt — a deliberate, small thumb on the scale toward technology,
    # applied to `blended_score` (which is in z-score units, so typical spread
    # across the ranked pool is roughly ±2). These values are intentionally
    # tiny: they act as a TIEBREAKER between names of comparable quality, and
    # are far too small to drag a gate-failing or negative-outlook stock into
    # the table — the quality gates run first and are untouched by this.
    #   theme_tilt_tech     — any Technology-sector name
    #   theme_tilt_frontier — quantum / AI-infrastructure pure plays
    #                         (universe.FRONTIER_TECH); replaces, not adds to,
    #                         the tech tilt so it can't compound.
    # Set both to 0.0 to disable the tilt entirely.
    theme_tilt_tech: float = 0.10
    theme_tilt_frontier: float = 0.20

    # The report's single merged table unions each horizon's own top `top_n`
    # diversified picks, so its row count is however many DISTINCT tickers
    # that union produces — not `top_n` itself, and not fixed run to run
    # (observed live: 27 rows on one run). This caps the FINAL merged table
    # to a fixed, predictable size, independent of `top_n` (which still
    # controls each horizon's own candidate pool).
    #
    # This must stay comfortably BELOW the union `top_n` produces, otherwise
    # the tail of the table is whatever happened to be left rather than a
    # real selection. See the `top_n` note above for the measured union size.
    main_table_size: int = 50

    # Hourly coverage sweep: consensus + price targets + named rating actions,
    # walked stalest-first over the whole universe.
    #
    # `coverage_sweep_max` = 0 means "no cap — every ticker every run", which is
    # what we want: an earlier fixed 60-ticker cap left a restored-from-empty
    # database with analyst coverage for only 20 % of the universe, so nothing
    # could clear the coverage gate and the run produced no rankings at all.
    # `coverage_budget_seconds` is the real safety valve: the sweep stops when
    # it runs out of time, and because it is ordered stalest-first the leftover
    # names are simply first in line next run.
    coverage_sweep_max: int = 0
    # Worst-case stage budgets on the fast path sum to ~19 min (prices ~1,
    # stooq ≤0.75, sweep ≤12, Google News ≤3, SEC ≤2.5) inside the 30-minute
    # step limit; a healthy sweep of ~600 names takes ~4 min with 4 workers.
    coverage_budget_seconds: float = 720.0

    # Report staleness: if the newest persisted Score is older than this many
    # days, the report shows a loud warning instead of presenting old
    # rankings as if they were current.
    max_score_age_days: int = 2

    # Sustained-picks + history (used by the report generator).
    history_path: str = "docs/history.jsonl"
    sustained_days: int = 7          # how many days back to look
    sustained_min_runs_pct: float = 0.6   # must appear on ≥60 % of those runs
    sustained_min_stars: int = 2     # require horizon_count ≥ 2 on a majority of runs
    history_show_days: int = 14      # render the last N days in the by-date section


# ---------------------------------------------------------------------------
# Signal model.
#
# The grade is built the way cross-sectional equity research builds alpha
# forecasts (Grinold & Kahn, "Active Portfolio Management"):
#
#   1. every feature is rank-normalised to N(0,1) across the universe;
#   2. each feature carries a PRIOR information coefficient (IC = expected
#      cross-sectional Spearman correlation with the forward return over
#      that horizon), set from the published literature below;
#   3. the priors are updated with ICs MEASURED on our own stored feature
#      snapshots vs realised forward returns (precision-weighted Bayes), so
#      a signal that does not work in this universe loses its weight;
#   4. weights are Σ⁻¹·IC (Σ = shrunk factor correlation), which stops
#      correlated signals (consensus level vs target upside) double-counting;
#   5. expected excess return  α = IC · σ · z  (Grinold's formula).
#
# Signs matter: a negative prior IC means the signal predicts UNDER-
# performance (short interest, analyst disagreement, short-term reversal).
#
# Priors are deliberately modest — single-signal monthly ICs in the
# literature are typically 0.02–0.05 and decay after publication
# (McLean & Pontiff 2016). Horizons: hours≈1d, daily≈5d, weekly≈20d,
# monthly≈90d forward windows.
#
# References (short form):
#   Barber, Lehavy, McNichols & Trueman 2001; Jegadeesh, Kim, Krische &
#   Lee 2004 (consensus level vs change); Womack 1996 (rating changes);
#   Brav & Lehavy 2003, Da & Schaumburg 2011 (target prices);
#   Diether, Malloy & Scherbina 2002 (dispersion); Chan, Jegadeesh &
#   Lakonishok 1996 (earnings revisions); Bernard & Thomas 1989 (PEAD);
#   Tetlock 2007, Tetlock, Saar-Tsechansky & Macskassy 2008 (news tone);
#   Lakonishok & Lee 2001, Cohen, Malloy & Pomorski 2012 (insiders);
#   Asquith, Pathak & Ritter 2005, Rapach, Ringgenberg & Zhou 2016 (short
#   interest); Brav, Jiang, Partnoy & Thomas 2008 (13D activism);
#   Palmrose, Richardson & Scholz 2004 (restatements / red-flag 8-Ks);
#   Fama & French 1992 (value); Novy-Marx 2013 (profitability);
#   Jegadeesh 1990, Lehmann 1990 (short-term reversal); Jegadeesh &
#   Titman 1993 (12-1 momentum); Novy-Marx 2012 (intermediate momentum);
#   George & Hwang 2004 (52-week high); Ang, Hodrick, Xing & Zhang 2006,
#   Frazzini & Pedersen 2014 (low volatility).
# ---------------------------------------------------------------------------
#                                 hours   daily  weekly  monthly
_PRIOR_IC_TABLE: dict[str, tuple[float, float, float, float]] = {
    # --- sell-side opinion -------------------------------------------------
    "consensus_z":           (0.004, 0.008, 0.015, 0.020),
    "consensus_delta":       (0.008, 0.015, 0.020, 0.020),
    "upside_z":              (0.004, 0.008, 0.015, 0.025),
    "target_dispersion":     (0.000, -0.004, -0.008, -0.015),
    "target_revision_30d":   (0.008, 0.015, 0.020, 0.015),
    "firm_target_revision":  (0.012, 0.018, 0.020, 0.015),
    "rating_mom_7d":         (0.015, 0.015, 0.008, 0.000),
    "rating_mom_30d":        (0.004, 0.008, 0.015, 0.012),
    # --- earnings ----------------------------------------------------------
    "eps_revision":          (0.008, 0.015, 0.025, 0.025),
    "eps_revision_breadth":  (0.006, 0.012, 0.020, 0.020),
    "earnings_surprise":     (0.004, 0.008, 0.015, 0.015),
    # --- news --------------------------------------------------------------
    "news_sentiment":        (0.015, 0.012, 0.008, 0.004),
    # --- smart money / events ---------------------------------------------
    "inst_flow_13f":         (0.000, 0.000, 0.005, 0.010),
    "insider_signal":        (0.000, 0.004, 0.008, 0.015),
    "short_interest":        (0.000, -0.004, -0.010, -0.015),
    "activist_13d":          (0.000, 0.004, 0.008, 0.012),
    "sec_red_flags":         (-0.004, -0.008, -0.010, -0.012),
    # --- fundamentals (sector-neutral) ------------------------------------
    "value":                 (0.000, 0.000, 0.005, 0.015),
    "quality":               (0.000, 0.000, 0.005, 0.015),
    # --- price -------------------------------------------------------------
    "price_mom_5d":          (-0.008, -0.010, -0.004, 0.000),
    "price_mom_21d":         (0.000, -0.006, -0.010, -0.004),
    "price_mom_63d":         (0.004, 0.008, 0.010, 0.010),
    "mom_12_1":              (0.000, 0.004, 0.012, 0.025),
    "high_52w":              (0.000, 0.004, 0.008, 0.015),
    "risk_penalty":          (0.004, 0.008, 0.012, 0.015),
}

FEATURE_NAMES: tuple[str, ...] = tuple(_PRIOR_IC_TABLE)

PRIOR_IC: dict[Horizon, dict[str, float]] = {
    h: {f: v[i] for f, v in _PRIOR_IC_TABLE.items()} for i, h in enumerate(HORIZONS)
}

# Normalised prior weights (Σ|w| = 1 per horizon). Display / explainability
# only — the live weights are the calibrated Σ⁻¹·IC from pipeline/grade.py.
WEIGHTS: dict[Horizon, dict[str, float]] = {
    h: {f: v / (sum(abs(x) for x in ics.values()) or 1.0) for f, v in ics.items()}
    for h, ics in PRIOR_IC.items()
}

# Partial sector neutralisation (λ ∈ [0, 1]): z ← z − λ·mean_sector(z).
# Valuation and profitability are only comparable within an industry, and
# sell-side upside / disagreement / shorting levels differ structurally by
# sector (biotech targets are always "far away"). Da & Schaumburg (2011)
# show target upside predicts returns WITHIN industries, not across them.
SECTOR_NEUTRAL: dict[str, float] = {
    "value": 1.0,
    "quality": 1.0,
    "upside_z": 0.5,
    "target_dispersion": 0.5,
    "short_interest": 0.5,
}

# Features whose raw value 0 is a genuine observation ("no rating changes",
# "no red-flag filings") rather than missing data. Everything else stays NaN
# when unobserved and contributes z = 0 (the Bayesian prior mean), instead of
# being scored as if the true value were 0.
ZERO_IS_OBSERVATION: frozenset[str] = frozenset({"rating_mom_7d", "rating_mom_30d"})

# Yahoo / static-list sector labels → one taxonomy, so the diversification
# cap and sector neutralisation don't treat "Consumer Cyclical" and
# "Consumer Discretionary" as different sectors.
SECTOR_ALIASES: dict[str, str] = {
    "consumer cyclical": "Consumer Discretionary",
    "consumer defensive": "Consumer Staples",
    "financial services": "Financials",
    "financial": "Financials",
    "healthcare": "Health Care",
    "basic materials": "Materials",
    "communication": "Communication Services",
}


def normalize_sector(sector: str | None) -> str:
    s = (sector or "").strip()
    if not s:
        return ""
    return SECTOR_ALIASES.get(s.lower(), s)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_settings() -> Settings:
    return Settings()
