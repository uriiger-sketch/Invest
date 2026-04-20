"""Typer CLI: `invest ingest`, `invest rank`, `invest train`, `invest serve`."""
from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from .config import HORIZONS, get_settings

app = typer.Typer(help="Invest — autonomous stock ranking crawler.", no_args_is_help=True)
console = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-5s %(name)s :: %(message)s",
    datefmt="%H:%M:%S",
)


def _ensure_schema() -> None:
    """Create tables on first run if they don't exist yet, then seed Stock
    rows from the static universe so 13F ticker matching works on first run."""
    from sqlalchemy import inspect

    from .db import get_engine, init_db
    from .universe import seed_stocks_table

    insp = inspect(get_engine())
    if "stocks" not in insp.get_table_names():
        init_db()
    seed_stocks_table()


@app.command()
def ingest() -> None:
    """Pull fresh data from all configured sources."""
    _ensure_schema()
    from .pipeline.ingest import ingest_all

    total = ingest_all()
    console.print(f"[green]ingest done[/] — {total} rows written")


@app.command("ingest-fast")
def ingest_fast() -> None:
    """Quick refresh: yfinance prices + consensus only. Used by the 20-min loop."""
    _ensure_schema()
    from .pipeline.ingest import ingest_fast as _ingest_fast

    total = _ingest_fast()
    console.print(f"[green]fast ingest done[/] — {total} rows written")


@app.command()
def rank(n: int = typer.Option(20, help="Top-N per horizon")) -> None:
    """Compute features, score, blend, and print top-N per horizon."""
    _ensure_schema()
    from .pipeline.rank import rank_all, top_n
    from .universe import current_universe

    rank_all(current_universe())
    tops = top_n(n=n)
    for h in HORIZONS:
        df = tops.get(h)
        if df is None or df.empty:
            console.print(f"[yellow]no scores for horizon {h}[/]")
            continue
        table = Table(title=f"Top {n} — {h}")
        table.add_column("#", justify="right")
        table.add_column("Ticker")
        table.add_column("Blended", justify="right")
        table.add_column("Composite", justify="right")
        table.add_column("ML", justify="right")
        table.add_column("Pctile", justify="right")
        for _, r in df.iterrows():
            table.add_row(
                str(int(r["rank"])),
                str(r["ticker"]),
                f"{r['blended_score']:.3f}",
                f"{r['composite_score']:.3f}",
                f"{r['ml_score']:.3f}",
                f"{(r['percentile'] or 0)*100:.1f}%",
            )
        console.print(table)


@app.command()
def train() -> None:
    """Train LightGBM models (no-op if cold-start thresholds not met)."""
    _ensure_schema()
    from .pipeline.ml_rank import train_all

    result = train_all()
    for h, p in result.items():
        console.print(f"{h}: {'saved ' + str(p) if p else '[yellow]cold-start, no model[/]'}")


@app.command()
def serve() -> None:
    """Launch Streamlit dashboard and (optionally) the APScheduler in the background."""
    _ensure_schema()
    settings = get_settings()

    if settings.run_scheduler:
        from .scheduler import start_scheduler

        start_scheduler()  # background thread

    dashboard_path = Path(__file__).parent / "dashboard.py"
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(dashboard_path),
        "--server.port",
        str(settings.streamlit_port),
        "--server.address",
        "0.0.0.0",
        "--server.headless",
        "true",
        "--browser.gatherUsageStats",
        "false",
    ]
    console.print(f"[green]starting dashboard[/] on :{settings.streamlit_port}")
    subprocess.run(cmd, check=False)


@app.command("refresh-universe")
def refresh_universe_cmd() -> None:
    """Pull current S&P500 + NDX100 tickers and print the list size."""
    from .universe import refresh_universe

    tickers = refresh_universe()
    console.print(f"universe size: {len(tickers)}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
