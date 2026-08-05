from invest.universe import chunks, static_universe


def test_static_universe_has_major_tickers():
    u = static_universe()
    assert "AAPL" in u
    assert "MSFT" in u
    assert len(u) >= 100


def test_chunks_preserves_order_and_size():
    xs = list("abcdefg")
    out = list(chunks(xs, 3))
    assert out == [["a", "b", "c"], ["d", "e", "f"], ["g"]]


def test_no_duplicate_tickers():
    """A duplicated ticker double-counts one company in the universe and can
    put the same name in the table twice."""
    from collections import Counter

    from invest.universe import static_universe

    dupes = {t for t, n in Counter(static_universe()).items() if n > 1}
    assert not dupes, f"duplicate tickers in universe: {dupes}"


def test_tase_lines_do_not_duplicate_us_listings():
    """Tel Aviv (.TA) entries must be TASE-ONLY names. A dual listing would
    count one company twice — once via its ADR and once via its home line —
    and the US line is the one that actually carries sell-side coverage."""
    from invest.universe import static_universe

    u = static_universe()
    us = {t for t in u if not t.endswith(".TA")}
    shadowed = [t for t in u if t.endswith(".TA") and t.split(".")[0] in us]
    assert not shadowed, f".TA lines shadowing a US listing: {shadowed}"


def test_israeli_and_tech_coverage_is_broad():
    """Guards the breadth this universe is supposed to provide, so a future
    edit can't quietly gut Israeli or quantum coverage."""
    from invest.universe import static_universe_entries

    entries = static_universe_entries()
    il = [t for t, _n, _s, r in entries if r == "IL"]
    tase = [t for t in il if t.endswith(".TA")]
    assert len(il) >= 80, f"Israeli coverage shrank to {len(il)}"
    assert len(tase) >= 25, f"Tel Aviv coverage shrank to {len(tase)}"

    tickers = {t for t, *_ in entries}
    for quantum in ("IONQ", "RGTI", "QBTS", "QUBT", "ARQQ", "LAES"):
        assert quantum in tickers, f"{quantum} missing from universe"


def test_frontier_tech_members_are_in_the_universe():
    """A FRONTIER_TECH ticker that isn't in the universe can never be
    crawled, scored, or tilted — it would be a silent no-op."""
    from invest.universe import FRONTIER_TECH, static_universe

    u = set(static_universe())
    missing = sorted(FRONTIER_TECH - u)
    assert not missing, f"FRONTIER_TECH tickers absent from universe: {missing}"
