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
    blend_composite_weight: float = 0.6
    blend_ml_weight: float = 0.4
    top_n: int = 10


# Weight matrix per horizon. Rows must sum to ~1 (negative entries allowed).
WEIGHTS: dict[Horizon, dict[str, float]] = {
    "hours": {
        # Fastest horizon — lean almost entirely on short-term momentum signals
        # and very-recent rating changes. Consensus & price-target upside have
        # almost no predictive value on hours-to-days; risk gets the biggest
        # penalty because intraday noise dominates.
        "consensus_z": 0.05,
        "upside_z": 0.00,
        "rating_mom_7d": 0.30,
        "rating_mom_30d": 0.05,
        "target_revision_30d": 0.05,
        "inst_flow_13f": 0.00,
        "insider_net_buy_90d": 0.05,
        "price_mom_21d": 0.30,
        "risk_penalty": 0.20,
    },
    "daily": {
        # ~5 trading days. Same flavour as "hours" but with a bit more weight on
        # the consensus snapshot and 30-day rating momentum.
        "consensus_z": 0.10,
        "upside_z": 0.05,
        "rating_mom_7d": 0.25,
        "rating_mom_30d": 0.10,
        "target_revision_30d": 0.05,
        "inst_flow_13f": 0.00,
        "insider_net_buy_90d": 0.05,
        "price_mom_21d": 0.25,
        "risk_penalty": 0.15,
    },
    "weekly": {
        "consensus_z": 0.20,
        "upside_z": 0.20,
        "rating_mom_7d": 0.10,
        "rating_mom_30d": 0.15,
        "target_revision_30d": 0.10,
        "inst_flow_13f": 0.05,
        "insider_net_buy_90d": 0.10,
        "price_mom_21d": 0.10,
        "risk_penalty": 0.10,
    },
    "monthly": {
        "consensus_z": 0.30,
        "upside_z": 0.25,
        "rating_mom_7d": 0.00,
        "rating_mom_30d": 0.05,
        "target_revision_30d": 0.10,
        "inst_flow_13f": 0.15,
        "insider_net_buy_90d": 0.10,
        "price_mom_21d": -0.05,
        "risk_penalty": 0.10,
    },
}

FEATURE_NAMES: tuple[str, ...] = tuple(WEIGHTS["daily"].keys())

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_settings() -> Settings:
    return Settings()
