#!/usr/bin/env python3
"""Level 1 — structural validation for the assessment instrument.

Checks: required fields, dimension weight total, question-id uniqueness,
maturity_target reference shape, and version consistency with VERSION.
Schema validation against the umbrella instrument schema stays in
scripts/validate.py (run after this in CI).
"""
import re
import sys
from pathlib import Path

import yaml

INSTRUMENT_PATH = "assessments/v1-alpha/instrument.yaml"


def main() -> int:
    instrument = yaml.safe_load(Path(INSTRUMENT_PATH).read_text())
    manifest = yaml.safe_load(Path("model.yaml").read_text())

    errors = []
    for required in ("id", "name", "domain", "version", "dimensions", "maturity_target"):
        if required not in instrument:
            errors.append(f"missing required field '{required}'")

    if not re.match(r"^dea:assessment-[a-z-]+$", instrument.get("id", "")):
        errors.append(f"id '{instrument.get('id')}' does not match 'dea:assessment-<domain>'")
    if not re.match(r"^dea:maturity-[a-z-]+$", instrument.get("maturity_target", "")):
        errors.append(
            f"maturity_target '{instrument.get('maturity_target')}' does not match 'dea:maturity-<domain>'"
        )

    dims = instrument.get("dimensions", [])
    if not 4 <= len(dims) <= 6:
        errors.append(f"expected 4-6 dimensions, found {len(dims)}")
    weight_total = sum(float(d.get("weight", 0)) for d in dims)
    if abs(weight_total - 1.0) > 1e-9:
        errors.append(f"dimension weights sum to {weight_total}, expected 1.0")

    qids = []
    for d in dims:
        dim_qids = [q["id"] for q in d.get("questions", [])]
        if len(dim_qids) != len(set(dim_qids)):
            errors.append(f"duplicate question ids within dimension '{d.get('id')}'")
        qids.extend(dim_qids)

    if "total_questions" in instrument and instrument["total_questions"] != len(qids):
        errors.append(
            f"total_questions={instrument['total_questions']} but counted {len(qids)}"
        )

    version = instrument.get("version", "")
    version_file = Path("VERSION").read_text().strip()
    if version != version_file:
        errors.append(f"instrument version {version} != VERSION file {version_file}")

    manifest_version = manifest.get("version", "")
    if manifest_version != version:
        errors.append(f"model.yaml version {manifest_version} != instrument version {version}")

    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1

    print(f"OK — {instrument['name']}")
    print(f"  Dimensions: {len(dims)} (weights sum to {weight_total})")
    print(f"  Total questions: {len(qids)}")
    print(f"  Maturity target: {instrument['maturity_target']}")
    print(f"  Version: {version} (instrument = VERSION = model.yaml)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
