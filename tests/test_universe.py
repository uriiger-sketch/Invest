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
