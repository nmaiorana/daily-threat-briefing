# SPEC 04 — Test harness & stub contracts (DRAFT 0.1)

Purpose:
- Provide an automated test harness that validates ingestion normalization,
  classification, and daily briefing generation against the interface specs.

Scope:
- Unit tests for normalization (no network calls)
- Unit tests for classification rules (rules from SPEC 03)
- Integration-like test: daily briefing generator produces a JSON briefing
  matching SPEC 01 and does not exceed 800 words.

Acceptance:
- Tests express expected contracts (schemas) and failure modes.
- Tests run under `pytest` and are executed on PRs via GitHub Actions.
- Implementation code must import the defined functions:
  - `src.ingest.normalize(raw_item: dict) -> dict` (normalized record)
  - `src.classifier.classify(normalized_item: dict) -> str` (one of: exploits, actors, supply_chain, patch_now)
  - `src.generator.generate_briefing(date: str, items: List[dict]) -> dict`

Notes:
- Tests must NOT make any network requests (use static sample fixtures).
- Tests use JSON Schema validation (schemas in `spec/schemas/`).
