"""Validate selected independent C1 row-kernel source ids."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEDULE = (
    ROOT
    / "candidate_data"
    / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
    / "quadrature_row_schedule.packet.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def required_ids() -> dict[str, list[str]]:
    schedule = load(SCHEDULE)
    out: dict[str, list[str]] = {}
    for stage in schedule["execution_order"]:
        out[stage["stage"]] = stage["rows"]
    return out


def truthy_source(node: dict[str, Any], label: str, errors: list[str]) -> None:
    if node.get("selected_emitted") is not True:
        errors.append(f"{label}: selected_emitted must be true")
    if node.get("theorem_derived") is not True:
        errors.append(f"{label}: theorem_derived must be true")
    if node.get("independent_of_residual_replay") is not True:
        errors.append(f"{label}: independent_of_residual_replay must be true")
    if node.get("locked_target_dependency") is not False:
        errors.append(f"{label}: locked_target_dependency must be false")
    if not node.get("source_id"):
        errors.append(f"{label}: source_id is required")


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    ids = required_ids()
    global_sources = payload.get("global_sources", {})
    for key in ["selected_measure_pairing", "selected_quadrature_rule", "selected_variation_space"]:
        node = global_sources.get(key, {})
        truthy_source(node, f"global_sources.{key}", errors)

    primitive = payload.get("primitive_row_kernel_sources", [])
    hessian = payload.get("hessian_b_sources", [])
    sector = payload.get("sector_assembly_sources", [])
    if not isinstance(primitive, list):
        errors.append("primitive_row_kernel_sources must be a list")
        primitive = []
    if not isinstance(hessian, list):
        errors.append("hessian_b_sources must be a list")
        hessian = []
    if not isinstance(sector, list):
        errors.append("sector_assembly_sources must be a list")
        sector = []

    primitive_by_id = {row.get("row_id"): row for row in primitive if isinstance(row, dict)}
    hessian_by_id = {row.get("row_id"): row for row in hessian if isinstance(row, dict)}
    sector_by_id = {row.get("row_id"): row for row in sector if isinstance(row, dict)}

    for row_id in ids.get("primitive_contractions", []):
        row = primitive_by_id.get(row_id)
        if row is None:
            errors.append(f"{row_id}: missing primitive source")
            continue
        truthy_source(row, row_id, errors)
        if not row.get("integral_formula"):
            errors.append(f"{row_id}: integral_formula is required")
        if row.get("selected_measure_pairing_id") != global_sources.get("selected_measure_pairing", {}).get("source_id"):
            errors.append(f"{row_id}: selected_measure_pairing_id must match global measure")
        if row.get("selected_quadrature_rule_id") != global_sources.get("selected_quadrature_rule", {}).get("source_id"):
            errors.append(f"{row_id}: selected_quadrature_rule_id must match global quadrature rule")

    for row_id in ids.get("hessian_source", []):
        row = hessian_by_id.get(row_id)
        if row is None:
            errors.append(f"{row_id}: missing hessian source")
            continue
        truthy_source(row, row_id, errors)
        if row.get("selected_b_vector_source") is not True:
            errors.append(f"{row_id}: selected_b_vector_source must be true")
        if row.get("not_copied_from_A_transpose_b_target") is not True:
            errors.append(f"{row_id}: not_copied_from_A_transpose_b_target must be true")

    for row_id in ids.get("sector_matrices", []):
        row = sector_by_id.get(row_id)
        if row is None:
            errors.append(f"{row_id}: missing sector source")
            continue
        truthy_source(row, row_id, errors)
        if row.get("assembled_from_primitive_source_rows") is not True:
            errors.append(f"{row_id}: assembled_from_primitive_source_rows must be true")

    if len(primitive_by_id) != len(ids.get("primitive_contractions", [])):
        errors.append("primitive source count mismatch")
    if len(hessian_by_id) != len(ids.get("hessian_source", [])):
        errors.append("hessian source count mismatch")
    if len(sector_by_id) != len(ids.get("sector_matrices", [])):
        errors.append("sector source count mismatch")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_independentc1_rowkernel_source_ids.py <payload.json>", file=sys.stderr)
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
