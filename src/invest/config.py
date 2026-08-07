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
    # horizon's top list (0 = no cap). Prevents an all-semis top-13.
    max_per_sector: int = 5

    blend_composite_weight: float = 0.6
    blend_ml_weight: float = 0.4
    top_n: int = 13

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
    main_table_size: int = 30

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
    coverage_budget_seconds: float = 900.0

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


# Weight matrix per horizon. Every row sums to EXACTLY 1.0 (verified by
# test_scoring.py::test_weights_sum_to_one) so composite_score is on a
# comparable scale across horizons.
#
# Each horizon leans on a DIFFERENT momentum window (price_mom_5d /
# price_mom_21d / price_mom_63d) rather than sharing one window with only the
# weight vector to differentiate them. Sharing a single 21-day window across
# all four horizons made "hours" and "daily" rank near-identically (measured
# Spearman rho = 0.958, 11/13 top-13 overlap on live data) — there was no
# feature in the whole pipeline that actually varied on a sub-21-day or
# multi-month timescale. Now the dominant momentum window genuinely differs
# per horizon, in addition to the weights.
WEIGHTS: dict[Horizon, dict[str, float]] = {
    "hours": {
        # Fastest horizon — dominated by 5-day price momentum + very recent
        # rating changes, but still respects consensus/upside so a
        # high-quality name can plausibly top this list AND the longer ones.
        "consensus_z": 0.12,
        "upside_z": 0.08,
        "rating_mom_7d": 0.22,
        "rating_mom_30d": 0.03,
        "target_revision_30d": 0.05,
        "inst_flow_13f": 0.00,
        "insider_net_buy_90d": 0.05,
        "price_mom_5d": 0.30,
        "price_mom_21d": 0.05,
        "price_mom_63d": 0.00,
        "risk_penalty": 0.10,
    },
    "daily": {
        # ~5 trading days. Blends short (5d) and medium (21d) momentum.
        "consensus_z": 0.10,
        "upside_z": 0.05,
        "rating_mom_7d": 0.20,
        "rating_mom_30d": 0.08,
        "target_revision_30d": 0.05,
        "inst_flow_13f": 0.00,
        "insider_net_buy_90d": 0.05,
        "price_mom_5d": 0.15,
        "price_mom_21d": 0.17,
        "price_mom_63d": 0.00,
        "risk_penalty": 0.15,
    },
    "weekly": {
        # ~1 month. Medium momentum + a touch of the 63-day window; rating
        # momentum shifts to the slower 30-day window.
        "consensus_z": 0.18,
        "upside_z": 0.15,
        "rating_mom_7d": 0.05,
        "rating_mom_30d": 0.12,
        "target_revision_30d": 0.08,
        "inst_flow_13f": 0.05,
        "insider_net_buy_90d": 0.08,
        "price_mom_5d": 0.00,
        "price_mom_21d": 0.14,
        "price_mom_63d": 0.05,
        "risk_penalty": 0.10,
    },
    "monthly": {
        # ~1 quarter. Dominated by consensus/upside + 63-day momentum +
        # institutional flow; no weight on short-term (5d/7d) noise.
        "consensus_z": 0.25,
        "upside_z": 0.20,
        "rating_mom_7d": 0.00,
        "rating_mom_30d": 0.03,
        "target_revision_30d": 0.08,
        "inst_flow_13f": 0.12,
        "insider_net_buy_90d": 0.08,
        "price_mom_5d": 0.00,
        "price_mom_21d": 0.00,
        "price_mom_63d": 0.14,
        "risk_penalty": 0.10,
    },
}

FEATURE_NAMES: tuple[str, ...] = tuple(WEIGHTS["daily"].keys())

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_settings() -> Settings:
    return Settings()
