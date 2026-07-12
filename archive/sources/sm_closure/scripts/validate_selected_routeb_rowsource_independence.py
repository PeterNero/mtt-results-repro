"""Validate Route B dynamic C1 row-source independence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "selected_basis_feeds_72_primitive_rows",
    "finite_weyl_trace_rule_feeds_all_rows",
    "sector_rows_assembled_from_primitive_rows",
    "hessian_source_rows_assembled_from_same_rows",
    "no_residual_projector_replay_used_as_source",
    "no_locked_target_values_used_as_source",
    "row_formula_source_theorem_derived",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    missing = [field for field in REQUIRED_FIELDS if payload.get(field) is not True]
    if missing:
        errors.append("missing row-source fields: " + ", ".join(missing))
    evidence = payload.get("attached_source_evidence", [])
    if not isinstance(evidence, list) or len(evidence) < 4:
        errors.append("attached_source_evidence must contain at least four sources")
    if payload.get("source_independent_of_residual_projector_replay") is not True:
        errors.append("source_independent_of_residual_projector_replay is not true")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_routeb_rowsource_independence.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    ok, errors = validate(load(path))
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
