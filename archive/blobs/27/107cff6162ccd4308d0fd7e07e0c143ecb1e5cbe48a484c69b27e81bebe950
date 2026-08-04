"""Validate selected finite C1 row-kernel functional packet source clauses."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_SOURCE_CLAUSES = [
    "measure_action_binding",
    "boundary_source_null",
    "basis_to_row_functionals",
    "phase_shift_pre_residual_operators",
    "hessian_b_source",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    clauses = payload.get("source_clauses", {})
    for clause in REQUIRED_SOURCE_CLAUSES:
        node = clauses.get(clause, {})
        if node.get("source_emitted") is not True:
            errors.append(f"{clause}: source_emitted must be true")
        if node.get("same_branch") is not True:
            errors.append(f"{clause}: same_branch must be true")
        if node.get("theorem_derived") is not True:
            errors.append(f"{clause}: theorem_derived must be true")
        if node.get("uses_replay_as_source") is not False:
            errors.append(f"{clause}: uses_replay_as_source must be false")

    rows = payload.get("row_values", {})
    counts = rows.get("counts", {})
    if counts.get("primitive") != 72:
        errors.append("row_values.counts.primitive must be 72")
    if counts.get("hessian") != 2:
        errors.append("row_values.counts.hessian must be 2")
    if counts.get("sector") != 36:
        errors.append("row_values.counts.sector must be 36")
    if rows.get("values_filled") is not True:
        errors.append("row_values.values_filled must be true")
    if rows.get("values_promoted_as_source") is not True:
        errors.append("row_values.values_promoted_as_source must be true")

    evidence = payload.get("attached_source_evidence", [])
    if not isinstance(evidence, list) or len(evidence) < 5:
        errors.append("attached_source_evidence must contain at least five sources")
    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_finitec1_rowkernel_functional_packet.py <packet.json>", file=sys.stderr)
        return 2
    ok, errors = validate(load(Path(argv[1])))
    if ok:
        print(f"PASS {argv[1]}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
