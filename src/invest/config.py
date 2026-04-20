from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

Horizon = Literal["days", "weeks", "months"]
HORIZONS: tuple[Horizon, ...] = ("days", "weeks", "months")

FORWARD_WINDOW_DAYS: dict[Horizon, int] = {"days": 5, "weeks": 20, "months": 90}


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
    top_n: int = 20


# Weight matrix per horizon. Rows must sum to ~1 (negative entries allowed).
WEIGHTS: dict[Horizon, dict[str, float]] = {
    "days": {
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
    "weeks": {
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
    "months": {
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

FEATURE_NAMES: tuple[str, ...] = tuple(WEIGHTS["days"].keys())

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_settings() -> Settings:
    return Settings()
