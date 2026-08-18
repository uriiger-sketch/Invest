"""Contract tests for the find-a-stock search box on the live page.

The search itself is browser JS, which pytest can't execute. What pytest CAN
pin down is the HTML contract that JS depends on — the element ids it looks
up and the per-row data attributes it matches against. Those are what would
silently break if the table markup were refactored, leaving a search box
that renders fine and matches nothing.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from invest.config import get_settings


def _report():
    path = Path(__file__).resolve().parent.parent / "scripts" / "generate_report.py"
    spec = importlib.util.spec_from_file_location("generate_report_finder", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _rows(n: int = 3) -> list[dict]:
    return [
        {
            "rank": i + 1, "ticker": f"TK{i}", "name": f"Test Company {i} Inc.",
            "sector": "Technology", "upside_pct": 0.10, "last_close": 100.0,
            "mean_target": 110.0, "score": 3.0 - i, "horizons": ["hours"],
            "analysts": 20, "sources": 30,
        }
        for i in range(n)
    ]


def test_rows_expose_ticker_and_name_for_search():
    """Each row must carry lowercase data-ticker / data-name. The JS matches
    on these rather than scraping cell text, because the displayed name is
    truncated to 40 chars — searching the full company name would otherwise
    miss."""
    html = _report()._main_table_html(_rows(), {})
    assert "data-ticker='tk0'" in html
    assert "data-name='test company 0 inc.'" in html


def test_row_data_attributes_are_escaped():
    """A company name containing a quote or angle bracket must not be able to
    break out of the attribute and inject markup."""
    rows = _rows(1)
    rows[0]["name"] = "Evil <script>alert(1)</script> & \"Co\""
    rows[0]["ticker"] = "EVL"
    html = _report()._main_table_html(rows, {})
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;" in html


def test_finder_markup_and_script_are_wired_together():
    """The ids the JS looks up must actually exist in the page, and the search
    script must be present. A mismatch here is a silently dead search box."""
    src = (
        Path(__file__).resolve().parent.parent / "scripts" / "generate_report.py"
    ).read_text()
    # Element ids referenced by the script must be rendered in the markup.
    for element_id in ("finder-input", "finder-msg"):
        assert src.count(element_id) >= 2, f"{element_id} not both rendered and referenced"
    # The script must search both fields and both highlight and scroll.
    assert 'getAttribute("data-ticker")' in src
    assert 'getAttribute("data-name")' in src
    assert 'classList.add("hit")' in src
    assert "scrollIntoView" in src


def test_pool_is_deep_enough_to_actually_fill_the_table():
    """`main_table_size` is a cap on the UNION of the four horizons' lists,
    not a guarantee. If `top_n` is too small the union never reaches the cap
    and the "top N" table quietly renders fewer rows — exactly what happened
    at top_n=13, where the union was ~28 and the table advertised 30.

    Measured over five consecutive days of live scores the union lands at
    ~1.85x `top_n` and is stable day to day. This asserts the relationship
    holds even under a deliberately pessimistic 1.5x, so the table still
    fills on a day with heavier-than-usual cross-horizon overlap.
    """
    pessimistic_union_ratio = 1.5
    s = get_settings()
    assert s.top_n * pessimistic_union_ratio >= s.main_table_size, (
        f"top_n={s.top_n} unions to roughly {s.top_n * 1.85:.0f} distinct names "
        f"(pessimistically {s.top_n * pessimistic_union_ratio:.0f}), too thin to "
        f"reliably fill main_table_size={s.main_table_size}"
    )
