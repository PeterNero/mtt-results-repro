"""Validate narrowed Phi_fin^C1 source emission or independent Hessian quadrature source."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROUTE_A_FIELDS = [
    "same_branch",
    "physical_phifin_c1_action_emitted",
    "finite_weyl_action_restriction_derived",
    "no_extra_boundary_or_source_term",
    "selected_phase_shift_variation_operators_pre_residual",
    "selected_hessian_counterterm_source",
    "same_source_b_selected_emitted",
    "row_formula_source_theorem_derived",
]

ROUTE_B_FIELDS = [
    "selected_basis_independent_of_residual_projector",
    "quadrature_rule_independent_of_locked_target",
    "all_72_primitive_rows_executed",
    "formal_110_rows_executed",
    "independent_hessian_quadrature_source_emitted",
    "selected_b_vector_source",
    "source_independent_of_residual_projector_replay",
    "exactness_or_error_certificates_attached",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence(node: dict[str, Any], key: str) -> list[Any]:
    value = node.get(key, [])
    return value if isinstance(value, list) else []


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    route_a = payload.get("route_A_phifinc1_source_emission", {})
    route_b = payload.get("route_B_independent_hessian_quadrature_source", {})

    missing_a = [field for field in ROUTE_A_FIELDS if route_a.get(field) is not True]
    missing_b = [field for field in ROUTE_B_FIELDS if route_b.get(field) is not True]
    evidence_a = evidence(route_a, "attached_same_branch_source_evidence")
    evidence_b = evidence(route_b, "attached_independent_quadrature_evidence")

    route_a_ok = not missing_a and len(evidence_a) >= 6
    route_b_ok = not missing_b and len(evidence_b) >= 5

    if missing_a:
        errors.append("Route A missing: " + ", ".join(missing_a))
    if len(evidence_a) < 6:
        errors.append("Route A needs at least six same-branch evidence sources")
    if missing_b:
        errors.append("Route B missing: " + ", ".join(missing_b))
    if len(evidence_b) < 5:
        errors.append("Route B needs at least five independent quadrature evidence sources")
    if not (route_a_ok or route_b_ok):
        errors.append("neither narrowed Route A nor narrowed Route B validates")
    return route_a_ok or route_b_ok, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_phifinc1emission_or_independenthessianquadraturesource.py <packet.json>", file=sys.stderr)
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
