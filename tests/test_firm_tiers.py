"""Regression tests for `invest.firms`.

If the tier map ever regresses (e.g. someone renames a key, or the
normaliser stops stripping suffixes), the report's `rating_mom_*`
features lose their pedigree weighting and the Tier-1 column in the
coverage snapshot goes to zero. This test catches both.
"""
from __future__ import annotations

from invest.firms import TIER_WEIGHTS, firm_tier, firm_weight


def test_tier1_lookups():
    for name in [
        "Goldman Sachs",
        "GOLDMAN SACHS GROUP",
        "goldman sachs & co",
        "Morgan Stanley",
        "JPMorgan",
        "JP Morgan",
        "Bank of America",
        "BofA Securities",
        "Citi",
        "Citigroup",
        "Barclays",
        "UBS",
        "Wells Fargo",
        "Jefferies",
        "Evercore ISI",
        "RBC Capital Markets",
        "BMO Capital Markets",
        "Wedbush",
        "Stifel",
        "Mizuho Securities",
    ]:
        assert firm_tier(name) == 1, name


def test_tier2_lookups():
    assert firm_tier("Morningstar") == 2
    assert firm_tier("Argus Research") == 2
    assert firm_tier("Roth MKM") == 2


def test_tier3_lookups():
    assert firm_tier("Zacks") == 3
    assert firm_tier("Berenberg") == 3


def test_unknown_firm():
    assert firm_tier("Some Random Boutique") == 0
    assert firm_tier(None) == 0
    assert firm_tier("") == 0


def test_firm_weight_scales_by_tier():
    assert firm_weight("Goldman Sachs") == TIER_WEIGHTS[1]
    assert firm_weight("Morningstar") == TIER_WEIGHTS[2]
    assert firm_weight("Zacks") == TIER_WEIGHTS[3]
    assert firm_weight("nobody") == TIER_WEIGHTS[0]
    assert TIER_WEIGHTS[1] > TIER_WEIGHTS[2] > TIER_WEIGHTS[3] >= TIER_WEIGHTS[0]
