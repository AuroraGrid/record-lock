from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "example-record-lock.json"
SCHEMA_PATH = ROOT / "schema" / "record-lock.schema.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
    if schema_errors:
        for error in schema_errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"SCHEMA ERROR at {location}: {error.message}")
        raise SystemExit(1)

    source_ids = {source["source_id"] for source in data["sources"]}
    claim_ids = {claim["claim_id"] for claim in data["claims"]}
    if len(source_ids) != len(data["sources"]):
        fail("source identifiers must be unique")
    if len(claim_ids) != len(data["claims"]):
        fail("claim identifiers must be unique")

    for claim in data["claims"]:
        missing_sources = set(claim["source_ids"]) - source_ids
        if missing_sources:
            fail(f"{claim['claim_id']} references missing sources: {sorted(missing_sources)}")
        if claim["type"] == "fact" and any(
            source["source_class"].endswith("unverified")
            for source in data["sources"]
            if source["source_id"] in claim["source_ids"]
        ):
            fail(f"{claim['claim_id']} labels an unverified source as fact")
        if claim["state"] == "verified" and not any(
            source["source_class"] in {"official_record", "controlling_record"}
            for source in data["sources"]
            if source["source_id"] in claim["source_ids"]
        ):
            fail(f"{claim['claim_id']} is verified without a controlling record")
        if claim["privacy_status"] in {"restricted", "withhold"}:
            fail(f"{claim['claim_id']} is not eligible for a public export")

    for hypothesis in data["hypotheses"]:
        referenced = set(hypothesis["supporting_claim_ids"]) | set(
            hypothesis["contradicting_claim_ids"]
        )
        missing_claims = referenced - claim_ids
        if missing_claims:
            fail(
                f"{hypothesis['hypothesis_id']} references missing claims: "
                f"{sorted(missing_claims)}"
            )

    assessment = data["assessment"]
    if not assessment["strongest_counterargument"].strip():
        fail("assessment lacks a strongest counterargument")
    if not assessment["falsifier"].strip():
        fail("assessment lacks a falsifier")
    if any(claim["type"] == "forecast" for claim in data["claims"]) and not data["horizon"]:
        fail("forecast records require a horizon")
    if assessment["confidence"] == "verified" and any(
        claim["state"] != "verified" for claim in data["claims"]
    ):
        fail("record confidence cannot be verified while claims remain unresolved")

    print(
        f"Validated {len(data['claims'])} claims, {len(data['sources'])} sources, "
        f"{len(data['hypotheses'])} hypotheses, and {len(data['constraints'])} constraints."
    )


if __name__ == "__main__":
    main()
