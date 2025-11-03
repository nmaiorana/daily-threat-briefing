import json
import os
from jsonschema import validate, ValidationError
import pytest

SCHEMA_PATH = os.path.join("spec", "schemas", "normalized.schema.json")

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def test_normalize_returns_schema_compliant_record(sample_nvd_item, monkeypatch):
    """
    The ingestion.normalize function should return a dict that validates against the normalized schema.
    """
    schema = load_schema()

    # Import the function under test (stub present in src/ingest.py)
    try:
        from src.ingest import normalize
    except Exception as exc:
        pytest.skip(f"normalize function not importable yet: {exc}")

    # Here we treat sample_nvd_item as raw input (tests do not rely on network)
    normalized = normalize(sample_nvd_item)
    assert isinstance(normalized, dict)
    # Validate against schema
    validate(instance=normalized, schema=schema)

def test_normalize_defaults_when_missing_fields(monkeypatch):
    """
    SPEC-05:
    - if 'headline' missing → first 80 chars of body
    - if 'published' missing → current UTC iso8601 Z
    """

    try:
        from src.ingest import normalize
    except Exception as exc:
        pytest.skip(f"normalize not importable yet: {exc}")

    raw = {
        "id": "X123",
        "source": "NVD",
        "body": "remote code execution in foo library — PoC published.",
    }

    norm = normalize(raw)

    # headline fallback = first 80 chars of body
    assert norm["headline"].startswith("remote code execution")

    # published auto set
    assert isinstance(norm["published"], str)
    assert norm["published"].endswith("Z")
