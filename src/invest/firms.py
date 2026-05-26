"""Curated tier map for sell-side analyst firms.

Used by `pipeline/features.py` to weight rating-momentum signals by the
reputation of the firm that issued the upgrade/downgrade, and by the
report generator to display a "Tier" badge in the per-row drawer.

Tiers are deliberately broad — they reflect "how widely the market
follows this shop's calls", not investment-quality opinion.

`firm_tier()` is whitespace/case-insensitive and tolerates the common
suffix variants seen in yfinance / Finnhub data ("Goldman Sachs", "Goldman
Sachs Group", "Goldman Sachs & Co").
"""
from __future__ import annotations

# Tier 1: bulge-bracket banks + the largest equity-research independents.
TIER_1: frozenset[str] = frozenset({
    "goldman sachs", "morgan stanley", "jpmorgan", "jp morgan", "j p morgan",
    "bank of america", "bofa securities", "bofa", "merrill lynch",
    "citi", "citigroup", "citic",
    "barclays", "ubs", "wells fargo", "deutsche bank", "hsbc",
    "jefferies", "evercore isi", "evercore",
    "rbc capital markets", "rbc capital", "rbc",
    "bmo capital markets", "bmo capital", "bmo",
    "td cowen", "td securities", "td", "cowen",
    "piper sandler", "raymond james",
    "wedbush", "stifel", "truist securities", "truist",
    "oppenheimer", "keybanc capital markets", "keybanc",
    "mizuho securities", "mizuho",
    "macquarie", "bernstein", "redburn atlantic", "redburn",
    "cantor fitzgerald", "guggenheim securities", "guggenheim",
    "needham", "loop capital", "btig", "da davidson",
    "robert w baird", "baird",
    "susquehanna", "rosenblatt securities", "rosenblatt",
    "scotiabank", "nomura", "credit suisse", "bnp paribas exane",
    "bnp paribas", "societe generale",
})

# Tier 2: well-known specialist / mid-tier brokers.
TIER_2: frozenset[str] = frozenset({
    "argus research", "argus", "morningstar", "cfra",
    "benchmark", "roth capital partners", "roth capital", "roth mkm",
    "canaccord genuity", "canaccord",
    "william blair", "northland capital", "northland securities",
    "ubs financial", "atlantic equities",
    "compass point", "lake street capital markets", "lake street",
    "ladenburg thalmann", "telsey advisory group", "telsey",
    "tigress financial", "monness crespi", "monness",
    "hilliard lyons", "noble capital markets", "noble",
    "dougherty", "dawson james", "jmp securities", "jmp",
    "h c wainwright", "h.c. wainwright", "hc wainwright",
    "alembic global advisors", "alembic global",
    "tudor pickering", "tph", "wolfe research", "wolfe",
    "melius research", "melius",
})

# Tier 3: niche / regional / very small.
TIER_3: frozenset[str] = frozenset({
    "zacks", "zacks investment research",
    "mkm partners", "freedom finance", "freedom capital",
    "seaport global securities", "seaport global", "seaport research",
    "bryan garnier", "berenberg",
    "kepler cheuvreux", "kepler", "liberum",
    "investec", "panmure liberum", "panmure gordon",
    "shore capital", "peel hunt", "numis",
})


def _normalize(name: str) -> str:
    """Lowercase, strip common suffixes / ampersands so 'Goldman Sachs & Co.'
    matches 'Goldman Sachs'."""
    n = (name or "").lower().strip()
    n = n.replace(".", "").replace(",", "")
    # Strip trailing corporate suffixes.
    for suf in (
        " group", " securities", " capital markets", " capital", " markets",
        " & co", " and co", " llc", " ltd", " limited", " inc", " incorporated",
        " plc", " ag", " sa", " spa", " nv", " bv", " holdings", " holding",
    ):
        while n.endswith(suf):
            n = n[: -len(suf)].strip()
    n = " ".join(n.split())
    return n


def firm_tier(name: str | None) -> int:
    """Return 1/2/3 if `name` matches a known firm; 0 ("unknown") otherwise."""
    if not name:
        return 0
    key = _normalize(name)
    if not key:
        return 0
    if key in TIER_1:
        return 1
    if key in TIER_2:
        return 2
    if key in TIER_3:
        return 3
    # Partial-match: tier-1 firm names sometimes arrive prefixed by office
    # (e.g. "Goldman Sachs (US)"); try first three tokens.
    short = " ".join(key.split()[:3])
    if short in TIER_1:
        return 1
    if short in TIER_2:
        return 2
    if short in TIER_3:
        return 3
    return 0


# How much weight each tier contributes to rating-momentum signals.
TIER_WEIGHTS: dict[int, float] = {1: 1.0, 2: 0.5, 3: 0.25, 0: 0.25}


def firm_weight(name: str | None) -> float:
    """Tier-weighted action contribution; unknown firms still count a little."""
    return TIER_WEIGHTS[firm_tier(name)]
