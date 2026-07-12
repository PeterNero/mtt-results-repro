"""Validate the two legal exits for the finite C1 row-kernel source proof."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROUTE_A_FIELDS = [
    "physical_action_restricts_to_finite_weyl_quotient",
    "zero_extra_boundary_or_source_term",
    "phase_R_Z_source_selection",
    "shift_R_X_source_selection",
    "same_source_b_selected_emission",
]

ROUTE_B_FIELDS = [
    "selected_basis_feeds_all_72_row_functionals",
    "pre_residual_phase_shift_variation_operators",
    "independent_hessian_counterterm_source_rows",
    "sector_rows_assembled_from_source_rows",
    "no_residual_projector_replay_or_locked_target_as_source",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_count(node: dict[str, Any]) -> int:
    evidence = node.get("attached_source_evidence", [])
    return len(evidence) if isinstance(evidence, list) else 0


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    route_a = payload.get("route_A_physical_action_restriction", {})
    route_b = payload.get("route_B_independent_rowkernel_source", {})

    missing_a = [field for field in ROUTE_A_FIELDS if route_a.get(field) is not True]
    missing_b = [field for field in ROUTE_B_FIELDS if route_b.get(field) is not True]
    route_a_ok = not missing_a and evidence_count(route_a) >= 5 and route_a.get("same_branch") is True
    route_b_ok = not missing_b and evidence_count(route_b) >= 5 and route_b.get("same_branch") is True

    if route_a.get("same_branch") is not True:
        errors.append("Route A same_branch must be true")
    if missing_a:
        errors.append("Route A missing: " + ", ".join(missing_a))
    if evidence_count(route_a) < 5:
        errors.append("Route A needs at least five same-branch source evidence entries")
    if route_b.get("same_branch") is not True:
        errors.append("Route B same_branch must be true")
    if missing_b:
        errors.append("Route B missing: " + ", ".join(missing_b))
    if evidence_count(route_b) < 5:
        errors.append("Route B needs at least five independent source evidence entries")
    if not (route_a_ok or route_b_ok):
        errors.append("neither Route A nor Route B validates")
    return route_a_ok or route_b_ok, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py <packet.json>", file=sys.stderr)
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
