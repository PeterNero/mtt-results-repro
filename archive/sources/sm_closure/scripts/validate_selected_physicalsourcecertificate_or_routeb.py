"""Validate selected Phi_fin^C1 physical source certificate or Route B independent run."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROUTE_A_FIELDS = [
    "physical_action_restricts_to_selected_finite_Weyl_quotient",
    "no_extra_physical_boundary_or_source_term",
    "phase_R_Z_source_selection",
    "shift_R_X_source_selection",
    "same_source_b_selected_emission",
]

ROUTE_B_FIELDS = [
    "selected_basis_independent_of_residual_projector",
    "quadrature_rule_independent_of_locked_target",
    "all_72_primitive_rows_executed",
    "formal_110_rows_executed",
    "source_independent_of_residual_projector_replay",
    "exactness_or_error_certificates_attached",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def truth(payload: dict[str, Any], path: list[str]) -> bool:
    node: Any = payload
    for key in path:
        if not isinstance(node, dict) or key not in node:
            return False
        node = node[key]
    return node is True


def evidence_list(payload: dict[str, Any], path: list[str]) -> list[Any]:
    node: Any = payload
    for key in path:
        if not isinstance(node, dict) or key not in node:
            return []
        node = node[key]
    return node if isinstance(node, list) else []


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")

    route_a = payload.get("route_A_physical_source_certificate", {})
    route_b = payload.get("route_B_independent_execution", {})

    route_a_missing = [key for key in ROUTE_A_FIELDS if route_a.get(key) is not True]
    route_b_missing = [key for key in ROUTE_B_FIELDS if route_b.get(key) is not True]

    route_a_evidence = evidence_list(route_a, ["attached_same_branch_sources"])
    route_b_evidence = evidence_list(route_b, ["attached_independent_provenance_sources"])

    route_a_ok = not route_a_missing and len(route_a_evidence) >= 5 and route_a.get("same_branch") is True
    route_b_ok = not route_b_missing and len(route_b_evidence) >= 3

    if route_a_missing:
        errors.append("Route A missing: " + ", ".join(route_a_missing))
    if not route_a_evidence:
        errors.append("Route A has no attached same-branch source evidence")
    if route_a.get("same_branch") is not True:
        errors.append("Route A same_branch is not true")

    if route_b_missing:
        errors.append("Route B missing: " + ", ".join(route_b_missing))
    if not route_b_evidence:
        errors.append("Route B has no attached independent provenance evidence")

    if not (route_a_ok or route_b_ok):
        errors.append("neither Route A nor Route B validates")
    return route_a_ok or route_b_ok, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_physicalsourcecertificate_or_routeb.py <packet.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    payload = load(path)
    ok, errors = validate(payload)
    if ok:
        print(f"PASS {path}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
