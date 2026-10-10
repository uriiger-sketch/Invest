"""Headline tone scoring + news parsing / cross-feed deduplication."""
from __future__ import annotations

from datetime import UTC, datetime, timedelta

from invest.db import session_scope
from invest.models import NewsItem
from invest.sentiment import headline_relevance, score_headline
from invest.sources.news_src import (
    news_id,
    parse_google_news_rss,
    parse_yahoo_news,
    upsert_news,
)


def test_finance_phrases_and_words_score_with_the_right_sign():
    assert score_headline("Nvidia beats estimates, raises guidance") > 0.5
    assert score_headline("Apple misses estimates as iPhone sales fall") < -0.5
    assert score_headline("Analyst lowers price target on Nike") < 0
    assert score_headline("Goldman upgrades AMD to Buy") > 0


def test_neutral_and_generic_finance_words_are_not_negative():
    # Loughran & McDonald: "liability", "tax", "cost" are not negative in finance text.
    assert score_headline("Company reports quarterly results") == 0.0
    assert score_headline("Board approves tax and cost structure for liability unit") >= 0.0
    assert score_headline("") == 0.0
    assert score_headline(None) == 0.0


def test_negation_flips_polarity():
    assert score_headline("Microsoft not expected to miss targets") > 0
    assert score_headline("Deal fails to win approval") < 0


def test_relevance_rewards_headlines_that_name_the_company():
    assert headline_relevance("NVDA jumps after earnings", "NVDA", "NVIDIA Corporation") == 1.0
    assert headline_relevance("Nvidia jumps after earnings", "NVDA", "NVIDIA Corporation") == 1.0
    assert headline_relevance("Chip stocks rally", "NVDA", "NVIDIA Corporation") == 0.5
    # Short tickers must match as whole words only ("T" is not every 't').
    assert headline_relevance("Tech stocks rally into the close", "T", "AT&T Inc.") == 0.5


def _now() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


def test_parse_yahoo_news_handles_nested_and_flat_schemas_and_skips_video():
    recent = _now() - timedelta(hours=3)
    items = [
        {"id": "a", "content": {"title": "Acme beats estimates on record revenue",
                                "pubDate": recent.isoformat() + "Z",
                                "provider": {"displayName": "Reuters"},
                                "canonicalUrl": {"url": "https://example.com/a"},
                                "contentType": "STORY"}},
        {"id": "v", "content": {"title": "Watch: Acme CEO interview", "contentType": "VIDEO",
                                "pubDate": recent.isoformat() + "Z"}},
        {"uuid": "b", "title": "Acme shares tumble after recall", "publisher": "Barron's",
         "link": "https://example.com/b", "providerPublishTime": int(recent.replace(tzinfo=UTC).timestamp())},
        {"uuid": "old", "title": "Acme ancient news story here", "publisher": "X",
         "providerPublishTime": int((_now() - timedelta(days=90)).replace(tzinfo=UTC).timestamp())},
    ]
    rows = parse_yahoo_news("ACME", items, "Acme Corp.")
    titles = {r["title"] for r in rows}
    assert titles == {"Acme beats estimates on record revenue", "Acme shares tumble after recall"}
    by_title = {r["title"]: r for r in rows}
    assert by_title["Acme beats estimates on record revenue"]["sentiment"] > 0
    assert by_title["Acme shares tumble after recall"]["sentiment"] < 0
    assert by_title["Acme beats estimates on record revenue"]["publisher"] == "Reuters"
    assert all(r["relevance"] == 1.0 for r in rows)


_RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<item><title>Acme beats estimates on record revenue - Reuters</title>
<link>https://news.google.com/rss/articles/1</link>
<pubDate>{d1}</pubDate><source url="https://reuters.com">Reuters</source></item>
<item><title>Acme names new CFO - Bloomberg</title>
<link>https://news.google.com/rss/articles/2</link>
<pubDate>{d1}</pubDate><source url="https://bloomberg.com">Bloomberg</source></item>
<item><title>Ancient Acme story long ago - Old</title><link>x</link>
<pubDate>Mon, 01 Jan 2024 00:00:00 GMT</pubDate><source>Old</source></item>
</channel></rss>"""


def test_google_rss_strips_publisher_suffix_and_dedupes_with_yahoo():
    from email.utils import format_datetime

    d1 = format_datetime(datetime.now(UTC) - timedelta(hours=2))
    xml = _RSS.replace(b"{d1}", d1.encode())
    rows = parse_google_news_rss("ACME", xml, "Acme Corp.")
    assert {r["title"] for r in rows} == {"Acme beats estimates on record revenue",
                                          "Acme names new CFO"}
    assert {r["publisher"] for r in rows} == {"Reuters", "Bloomberg"}

    # The same story already stored from Yahoo must not be counted twice.
    yahoo = parse_yahoo_news("ACME", [{"title": "Acme beats estimates on record revenue",
                                       "publisher": "Reuters",
                                       "providerPublishTime": int(datetime.now(UTC).timestamp())}],
                             "Acme Corp.")
    assert yahoo[0]["id"] == news_id("ACME", "acme  beats estimates, on record revenue!")
    upsert_news(yahoo)
    upsert_news(rows)
    upsert_news(rows)  # re-crawl: idempotent
    with session_scope() as s:
        stored = s.query(NewsItem).filter(NewsItem.ticker == "ACME").all()
    assert len(stored) == 2
    assert {n.source for n in stored} == {"yahoo", "gnews"}


def test_garbage_rss_is_harmless():
    assert parse_google_news_rss("ACME", b"<not xml", "Acme") == []
    assert parse_google_news_rss("ACME", b"", "Acme") == []


def test_yahoo_search_news_keeps_only_stories_tagged_with_the_ticker():
    """Yahoo's search endpoint (used since the per-ticker news stream broke)
    returns loosely related stories. Live example: a Take-Two article filed
    under NVDA. Stories tagged with other symbols only are dropped; untagged
    ones are kept at headline-based relevance."""
    ts = int(datetime.now(UTC).timestamp()) - 3600
    items = [
        {"uuid": "1", "title": "Chipmakers rally as demand improves", "publisher": "Reuters",
         "link": "https://example.com/1", "providerPublishTime": ts, "type": "STORY",
         "relatedTickers": ["ACME", "NVDA"]},
        {"uuid": "2", "title": "Is now a good time to buy Take-Two stock?", "publisher": "Fool",
         "link": "https://example.com/2", "providerPublishTime": ts, "type": "STORY",
         "relatedTickers": ["TTWO"]},
        {"uuid": "3", "title": "Video: CEO interview about the quarter", "publisher": "Yahoo",
         "providerPublishTime": ts, "type": "VIDEO", "relatedTickers": ["ACME"]},
        {"uuid": "4", "title": "Market wrap: stocks drift higher today", "publisher": "AP",
         "link": "https://example.com/4", "providerPublishTime": ts, "type": "STORY"},
    ]
    rows = {r["title"]: r for r in parse_yahoo_news("ACME", items, "Acme Corp.")}
    assert set(rows) == {"Chipmakers rally as demand improves", "Market wrap: stocks drift higher today"}
    assert rows["Chipmakers rally as demand improves"]["relevance"] == 1.0
    assert rows["Market wrap: stocks drift higher today"]["relevance"] == 0.5
