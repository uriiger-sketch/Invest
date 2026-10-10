"""Finance-specific headline tone scoring.

Why a domain lexicon and not a general-purpose one: Loughran & McDonald
(2011) showed that ~3/4 of the words a general sentiment dictionary flags as
negative are NOT negative in financial text ("liability", "tax", "cost",
"capital", "vice" president …). Headlines are short, so a small curated
lexicon of finance-specific polarity words plus a few multi-word phrases
("raises guidance", "misses estimates", "price target cut") captures most of
the signal, deterministically and with no model download.

Scoring:
    s = (P − N) / (P + N + 1)  ∈ (−1, 1)
with phrase hits counted double, and polarity flipped when a negator
("not", "no", "fails to", …) precedes the word within three tokens.
Headlines with no polarity words score exactly 0.

This is a noisy measurement; the pipeline shrinks the per-ticker average
toward 0 when there are few headlines (see features._news_features), and the
grading model learns from our own history how much weight the signal earns.
"""
from __future__ import annotations

import re

_POSITIVE_WORDS: frozenset[str] = frozenset({
    "beat", "beats", "tops", "topped", "surpass", "surpasses", "surpassed", "exceed",
    "exceeds", "exceeded", "record", "upgrade", "upgraded", "upgrades", "outperform",
    "outperforms", "overweight", "bullish", "rally", "rallies", "rallied", "surge",
    "surges", "surged", "soar", "soars", "soared", "jump", "jumps", "jumped", "gain",
    "gains", "gained", "climb", "climbs", "climbed", "rise", "rises", "rose", "strong",
    "stronger", "strongest", "robust", "expand", "expands", "expanded", "expansion",
    "win", "wins", "won", "award", "awarded", "approval", "approved", "approves",
    "breakthrough", "partnership", "buyback", "repurchase", "profit", "profitable",
    "upbeat", "optimistic", "accelerate", "accelerates", "accelerating", "boost",
    "boosts", "boosted", "lift", "lifts", "lifted", "upside", "rebound", "rebounds",
    "rebounded", "recovery", "milestone", "outpace", "outpaces", "momentum", "raise",
    "raises", "raised", "hike", "hikes", "hiked", "positive", "tailwind", "tailwinds",
    "best", "highs", "growth", "grows", "grew", "secures", "secured", "clinches",
})

_NEGATIVE_WORDS: frozenset[str] = frozenset({
    "miss", "misses", "missed", "downgrade", "downgraded", "downgrades", "underperform",
    "underperforms", "underweight", "bearish", "plunge", "plunges", "plunged",
    "plummet", "plummets", "plummeted", "tumble", "tumbles", "tumbled", "slump",
    "slumps", "slumped", "sink", "sinks", "sank", "drop", "drops", "dropped", "fall",
    "falls", "fell", "decline", "declines", "declined", "slide", "slides", "slid",
    "weak", "weaker", "weakest", "weakness", "warn", "warns", "warning", "loss",
    "losses", "lawsuit", "lawsuits", "sue", "sues", "sued", "probe", "probes",
    "investigation", "subpoena", "fraud", "recall", "recalls", "layoff", "layoffs",
    "restructuring", "bankruptcy", "bankrupt", "default", "defaults", "delist",
    "delisting", "halt", "halted", "fined", "penalty", "antitrust", "dilution",
    "dilutive", "resign", "resigns", "resigned", "resignation", "concern", "concerns",
    "headwind", "headwinds", "disappoint", "disappoints", "disappointing",
    "disappointed", "slowdown", "shortfall", "delay", "delays", "delayed", "suspend",
    "suspends", "suspended", "breach", "hack", "hacked", "outage", "scandal", "cut",
    "cuts", "slash", "slashes", "slashed", "lowers", "lowered", "lows",
    "selloff", "sell-off", "crash", "crashes", "crashed",
    "negative", "lose", "loses", "lost", "plunging", "sinking", "falling", "worst",
    "downside", "turmoil", "uncertainty", "violation",
    "violations", "charges", "charged", "indicted", "guilty",
})

# Multi-word phrases, matched on the lowercased headline before tokenising.
# Each phrase hit counts DOUBLE and its words are removed so they are not
# double-scored as single words too ("price target cut" is not also "cut").
_POSITIVE_PHRASES: tuple[str, ...] = (
    "raises guidance", "raised guidance", "raises outlook", "raised outlook",
    "boosts outlook", "lifts outlook", "raises forecast", "raised forecast",
    "beats estimates", "beat estimates", "tops estimates", "above estimates",
    "better than expected", "better-than-expected", "record revenue", "record quarter",
    "record high", "all-time high", "upgraded to buy", "upgrade to buy",
    "upgraded to outperform", "upgraded to overweight", "raises price target",
    "raised price target", "price target raised", "price target hike",
    "price target increased", "boosts price target", "dividend increase",
    "raises dividend", "share buyback", "stock buyback", "fda approval",
    "beat and raise", "strong demand",
)
_NEGATIVE_PHRASES: tuple[str, ...] = (
    "cuts guidance", "cut guidance", "lowers guidance", "lowered guidance",
    "cuts outlook", "lowers outlook", "lowered outlook", "cuts forecast",
    "misses estimates", "missed estimates", "below estimates", "worse than expected",
    "worse-than-expected", "downgraded to sell", "downgrade to sell",
    "downgraded to underperform", "downgraded to underweight", "downgraded to neutral",
    "downgraded to hold", "lowers price target", "lowered price target",
    "price target cut", "price target lowered", "cuts price target",
    "price target reduced", "secondary offering", "stock offering", "public offering",
    "going concern", "sec investigation", "class action", "short seller",
    "short report", "chapter 11", "job cuts", "profit warning", "guidance cut",
    "52-week low", "data breach",
)

_NEGATORS: frozenset[str] = frozenset({
    "not", "no", "never", "without", "fails", "failed", "fail", "nor", "neither",
    "hardly", "unable", "didn't", "doesn't", "isn't", "wasn't", "won't", "can't",
})

_TOKEN = re.compile(r"[a-z][a-z'\-]*")


def score_headline(text: str | None) -> float:
    """Tone of one headline in (−1, 1); 0.0 when it carries no polarity."""
    if not text:
        return 0.0
    t = " " + text.lower().replace("’", "'") + " "
    pos = neg = 0.0
    for phrase in _POSITIVE_PHRASES:
        if f" {phrase} " in t or f" {phrase}," in t or f" {phrase}." in t:
            pos += 2.0
            t = t.replace(phrase, " ")
    for phrase in _NEGATIVE_PHRASES:
        if f" {phrase} " in t or f" {phrase}," in t or f" {phrase}." in t:
            neg += 2.0
            t = t.replace(phrase, " ")
    tokens = _TOKEN.findall(t)
    for i, tok in enumerate(tokens):
        polarity = 1.0 if tok in _POSITIVE_WORDS else -1.0 if tok in _NEGATIVE_WORDS else 0.0
        if polarity == 0.0:
            continue
        if any(w in _NEGATORS for w in tokens[max(0, i - 3):i]):
            polarity = -polarity
        if polarity > 0:
            pos += 1.0
        else:
            neg += 1.0
    if pos == 0.0 and neg == 0.0:
        return 0.0
    return (pos - neg) / (pos + neg + 1.0)


def headline_relevance(title: str, ticker: str, company_name: str | None) -> float:
    """1.0 when the headline names the company (ticker or leading name token),
    else 0.5 — a broad-query hit that may be about a peer or the market."""
    if not title:
        return 0.5
    low = title.lower()
    base = ticker.split(".")[0].lower()
    if len(base) >= 2 and re.search(rf"(?<![a-z0-9]){re.escape(base)}(?![a-z0-9])", low):
        return 1.0
    if company_name:
        first = _company_stem(company_name)
        if first and first in low:
            return 1.0
    return 0.5


_NAME_SUFFIX = re.compile(
    r"\b(inc|incorporated|corp|corporation|co|company|ltd|limited|plc|holdings?|group|"
    r"n\.?v|s\.?a|s\.?e|ag|a/s|asa|se|technologies|technology|the)\b\.?",
    re.I,
)


def _company_stem(name: str) -> str:
    """'Apple Inc.' -> 'apple'; 'The TJX Companies, Inc.' -> 'tjx companies'."""
    n = _NAME_SUFFIX.sub(" ", name.replace(",", " ")).strip().lower()
    n = " ".join(n.split())
    return n if len(n) >= 3 else ""


def company_query_name(name: str | None) -> str:
    """Name used to query news feeds (suffixes stripped, original casing)."""
    if not name:
        return ""
    n = _NAME_SUFFIX.sub(" ", name.replace(",", " "))
    return " ".join(n.split())
