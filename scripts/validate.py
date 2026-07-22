#!/usr/bin/env python3
"""Validate assessment instrument against the DEA umbrella schema."""
import sys
import json
import yaml
import urllib.request
from jsonschema import validate, ValidationError

SCHEMA_URL = (
    "https://raw.githubusercontent.com/Assessment-Models/"
    "dea-catalog-assessment-tools/main/schemas/instrument.schema.json"
)

INSTRUMENT_PATH = "assessments/v1-alpha/instrument.yaml"


def main() -> int:
    with open(INSTRUMENT_PATH) as fh:
        instrument = yaml.safe_load(fh)

    try:
        schema = json.loads(
            urllib.request.urlopen(SCHEMA_URL, timeout=10).read()
        )
    except Exception as exc:
        print(f"WARN: could not fetch remote schema ({exc}); using local fallback")
        schema = None

    if schema is None:
        for required in ("id", "name", "domain", "dimensions"):
            if required not in instrument:
                print(f"FAIL: missing required field '{required}'")
                return 1
    else:
        try:
            validate(instance=instrument, schema=schema)
        except ValidationError as exc:
            print(f"VALIDATION FAILED: {exc.message}")
            return 1

    n_dims = len(instrument.get("dimensions", []))
    n_q = sum(len(d.get("questions", [])) for d in instrument.get("dimensions", []))
    name = instrument.get("name", "unknown")

    print(f"OK — {name}")
    print(f"  Dimensions: {n_dims}")
    print(f"  Total questions: {n_q}")
    print(f"  Duration: ~{instrument.get('duration_minutes', 60)} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())