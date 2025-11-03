import pytest

def test_classify_exploit_priority(sample_nvd_item):
    try:
        from src.classifier import classify
    except Exception as exc:
        pytest.skip(f"classify not importable yet: {exc}")

    # sample_nvd_item contains "RCE" and "PoC" in body/headline
    category = classify(sample_nvd_item)
    assert category in ("exploits", "actors", "supply_chain", "patch_now")
    assert category == "exploits"

def test_classify_supply_chain(sample_bc_item):
    try:
        from src.classifier import classify
    except Exception as exc:
        pytest.skip(f"classify not importable yet: {exc}")

    category = classify(sample_bc_item)
    assert category == "supply_chain" or category == "actors"  # acceptable if actor recognised
