"""Validate a selected Route B independent quadrature/Hessian payload."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEDULE = ROOT / "candidate_data" / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan" / "quadrature_row_schedule.packet.json"
REQUIRED_STAGES = ["primitive_contractions", "hessian_source", "sector_matrices"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def required_row_ids() -> list[str]:
    schedule = load(SCHEDULE)
    ids: list[str] = []
    for stage in schedule["execution_order"]:
        if stage["stage"] in REQUIRED_STAGES:
            ids.extend(stage["rows"])
    return ids


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    rows = payload.get("rows", [])
    if not isinstance(rows, list):
        return False, errors + ["rows must be a list"]

    required_ids = required_row_ids()
    by_id = {row.get("row_id"): row for row in rows if isinstance(row, dict)}
    missing = [row_id for row_id in required_ids if row_id not in by_id]
    extra = [row_id for row_id in by_id if row_id not in required_ids]
    if missing:
        errors.append(f"missing required rows: {len(missing)}")
    if extra:
        errors.append(f"unexpected rows: {len(extra)}")

    for row_id in required_ids:
        row = by_id.get(row_id)
        if not row:
            continue
        prefix = f"{row_id}: "
        if row.get("independent_source_emitted") is not True:
            errors.append(prefix + "independent_source_emitted must be true")
        if row.get("locked_target_dependency") is not False:
            errors.append(prefix + "locked_target_dependency must be false")
        if row.get("residual_replay_dependency") is not False:
            errors.append(prefix + "residual_replay_dependency must be false")
        if not row.get("quadrature_rule_id"):
            errors.append(prefix + "quadrature_rule_id is required")
        if not row.get("kernel_source_id"):
            errors.append(prefix + "kernel_source_id is required")
        if row.get("value") is None:
            errors.append(prefix + "value is required")
        if not (row.get("exactness_certificate") or row.get("error_bound")):
            errors.append(prefix + "exactness_certificate or error_bound is required")

    hessian_rows = [by_id.get("theta_phase"), by_id.get("theta_shift")]
    if any(row and row.get("selected_b_vector_source") is not True for row in hessian_rows):
        errors.append("hessian rows must emit selected_b_vector_source")

    return not errors, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_routeb_independent_quadrature_payload.py <payload.json>", file=sys.stderr)
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
