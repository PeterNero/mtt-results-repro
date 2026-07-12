"""Build the Phi_q ansatz solver / gerbe obstruction gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
OUTPUT_CERT = CERTS / "phiq_ansatz_solver_or_gerbe_obstruction_certificate.json"
OUTPUT_DATA = DATA / "phiq_ansatz_solver_or_gerbe_obstruction.candidate.json"


REQUIRED_SPACES = [
    ("F1", [-3, 0, 1]),
    ("F2", [-2, 1, -1]),
    ("F3", [0, -1, 0]),
    ("F4", [0, 0, -1]),
    ("F5", [1, 1, 1]),
    ("G1", [2, 1, -1]),
    ("G2", [1, 0, 1]),
    ("G3", [-1, 2, 0]),
    ("G4", [-1, 1, 1]),
    ("G5", [-2, 0, -1]),
    ("P", [-1, 1, 0]),
]


def has_c(charge: list[int]) -> bool:
    return charge[2] != 0


def main() -> None:
    form_differentials = {
        "omega1": "0",
        "omega2": "0",
        "omega3": "omega1 wedge omega2",
        "a=(i/2)omega1 wedge baromega1": "0",
        "b=(i/2)omega2 wedge baromega2": "0",
        "c=(i/2)omega3 wedge baromega3": "(i/2)(omega1 wedge omega2 wedge baromega3 - omega3 wedge baromega1 wedge baromega2)",
    }
    space_results = []
    for sid, charge in REQUIRED_SPACES:
        c_axis = has_c(charge)
        space_results.append(
            {
                "id": sid,
                "charge": charge,
                "ordinary_de_rham_line_bundle_c1_admissible_under_literal_abc": not c_axis,
                "c_axis_used": c_axis,
                "status": "OBSTRUCTED_LITERAL_C_AXIS_NOT_CLOSED" if c_axis else "PASS_AB_BASE_ONLY",
            }
        )
    c_obstructed = [item for item in space_results if item["c_axis_used"]]
    ansatz_tests = [
        {
            "id": "ordinary_line_bundle_factor_literal_abc",
            "status": "OBSTRUCTED",
            "reason": "Eight required spaces use the literal c direction, but c=(i/2)omega3 wedge baromega3 is not closed on the Iwasawa structure equations.",
            "can_supply_all_required_spaces": False,
        },
        {
            "id": "ordinary_line_bundle_factor_ab_only",
            "status": "PARTIAL_ONLY",
            "reason": "Can only address F3, G3, and P-like c=0 charges; the monad needs eight c-bearing spaces.",
            "can_supply_all_required_spaces": False,
        },
        {
            "id": "reinterpret_c_as_closed_bott_chern_or_integral_class",
            "status": "SOURCE_AMENDMENT_REQUIRED",
            "reason": "If c is a cohomology label rather than the literal invariant form, the source must provide the closed representative and transition/factor data.",
            "can_supply_all_required_spaces": "UNKNOWN_PENDING_SOURCE_AMENDMENT",
        },
        {
            "id": "twisted_gerbe_module",
            "status": "LIVE_PRIMARY_AFTER_OBSTRUCTION",
            "reason": "A gerbe/B-field/twisted module can carry nonclosed local curvature data while preserving a global twisted cocycle, if selected independently.",
            "can_supply_all_required_spaces": "POSSIBLE_NOT_CLOSED",
        },
        {
            "id": "source_certified_a01_operator_exit",
            "status": "LIVE_ALTERNATIVE",
            "reason": "Bypass individual line-bundle factors and derive D_E directly from a corrected, source-certified Dolbeault operator.",
            "can_supply_all_required_spaces": "NOT_APPLICABLE_OPERATOR_EXIT",
        },
    ]
    candidate = {
        "candidate": "SelectedQaSU3PhiQAnsatzSolverOrGerbeObstruction",
        "status": "PHIQ_LITERAL_ABC_LINE_BUNDLE_ROUTE_OBSTRUCTED_GERBE_OR_SOURCE_AMENDMENT_REQUIRED",
        "structure_equations": {
            "domega1": "0",
            "domega2": "0",
            "domega3": "omega1 wedge omega2",
        },
        "form_differentials": form_differentials,
        "required_spaces": space_results,
        "counts": {
            "required_spaces": len(REQUIRED_SPACES),
            "c_axis_obstructed_spaces": len(c_obstructed),
            "ordinary_ab_only_spaces": len(REQUIRED_SPACES) - len(c_obstructed),
        },
        "ansatz_tests": ansatz_tests,
        "interpretation": [
            "This does not prove the monad idea false.",
            "It proves that the literal invariant-form reading of c cannot be used as an ordinary de Rham first Chern direction for all required line bundles.",
            "Closure now requires either a source amendment giving closed c-class/factors, a twisted gerbe module, or a direct operator exit.",
        ],
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3PhiQAnsatzSolverOrGerbeObstruction",
        "status": "QA_SU3_PHIQ_LITERAL_C_AXIS_OBSTRUCTION_GERBE_OR_SOURCE_AMENDMENT_REQUIRED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "literal_c_nonclosed_check": True,
            "ordinary_ab_only_route_insufficient": True,
            "ordinary_full_nil_theta_line_bundle_route_obstructed_under_literal_abc": True,
        },
        "what_remains_open": {
            "closed_c_representative_or_source_amendment": True,
            "twisted_gerbe_packet": True,
            "source_certified_a01_operator_exit": True,
            "section_basis_solver": True,
            "operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "route_update": {
            "ordinary_full_nil_theta_route": "OBSTRUCTED_UNDER_LITERAL_ABC_C_AXIS",
            "primary_next_route": "projective_gerbe_twisted_module_or_source_amended_closed_c",
            "fast_alternative": "source_certified_A01_operator_exit",
            "next_required_artifact": "Selected_Qa_SU3_Gerbe_Twist_or_Closed_C_Source_Amendment_Gate_v1",
        },
        "counts": candidate["counts"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    text_data = json.dumps(candidate, indent=2, sort_keys=True)
    text_cert = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(text_data + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(text_cert + "\n", encoding="utf-8")
    print(text_cert)


if __name__ == "__main__":
    main()
