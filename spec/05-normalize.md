# SPEC 05 — normalize

normalize(raw_item: dict) must return a normalized record that validates against the schema in `spec/schemas/normalized.schema.json`.

rules:
- if `headline` not present in raw_item, use first 80 chars of body
- if `published` not present, default = current UTC datetime in ISO8601 with Z
- source is string from raw_item["source"]
- id must be string from raw_item["id"]
