"""Decide the explicit Qa/SU3 HYM-matrix route after repair no-go tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPAIR_B_NO_GO = ROOT / "certificates" / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json"
REPAIR_A_STRESS = ROOT / "certificates" / "selected_qa_su3_repair_retirement_stress_test_certificate.json"
SOURCE_HUNT = ROOT / "certificates" / "selected_qa_su3_alternative_operator_or_projector_source_hunt_certificate.json"
TEMPLATE = ROOT / "certificates" / "selected_qa_su3_color_connection_template_fill_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    repair_b = load(REPAIR_B_NO_GO)
    repair_a = load(REPAIR_A_STRESS)
    source_hunt = load(SOURCE_HUNT)
    template = load(TEMPLATE)
    routes = source_hunt["candidate_routes"]
    route_by_id = {route["id"]: route for route in routes}
    output = {
        "certificate": "SelectedQaSU3ExplicitHYMRouteRetirement",
        "status": "QA_SU3_EXPLICIT_HYM_MATRIX_ROUTE_RETIRED_CURRENT_SOURCE_RECORD",
        "input_status": {
            "repair_A_stress_test": repair_a["status"],
            "repair_B_current_source_no_go": repair_b["status"],
            "alternative_source_hunt": source_hunt["status"],
            "color_connection_template": template["status"],
        },
        "retirement_basis": [
            {
                "branch": "printed matrix",
                "status": "blocked",
                "reason": "The printed matrix fails the standard integrability check against the printed Iwasawa structure equation.",
            },
            {
                "branch": "Repair A diagonal B3",
                "status": "retired_under_selected_branch",
                "reason": "It has an extra noncentral unitary stabilizer and direct split, incompatible with the selected indecomposable rank-3 SU3 HYM branch.",
            },
            {
                "branch": "Repair B moved B2",
                "status": "current_source_no_go",
                "reason": "It requires the unsourced primitive correction -(w1*mu+w3*mu^2) diag(1,-1,0).",
            },
        ],
        "retirement_scope": {
            "explicit_hym_matrix_route_retired_for_current_proof": True,
            "future_erratum_can_reopen": True,
            "future_source_certified_full_curvature_can_reopen": True,
            "mathematical_hym_bundle_existence_retired": False,
        },
        "selected_next_routes": [
            {
                "rank": 1,
                "route": "nontrivial_su3_color_bundle_connection_endomorphism",
                "source_status": route_by_id[
                    "nontrivial_su3_color_bundle_connection_endomorphism"
                ]["status"],
                "reason": "This keeps the selected SU3 color-bundle idea but demands a real sourced threshold operator or Weitzenbock/endomorphism_E rather than the blocked displayed matrix.",
                "next_test": "fill or no-go the selected endomorphism_E / color threshold operator template",
            },
            {
                "rank": 2,
                "route": "ray_singer_or_reidemeister_torsion_local_system",
                "source_status": route_by_id[
                    "ray_singer_or_reidemeister_torsion_local_system"
                ]["status"],
                "reason": "The p!=0 Nil Hodge complex is acyclic, making analytic/Reidemeister torsion the natural determinant invariant if the local system and color character are selected.",
                "next_test": "construct selected local-system torsion input or prove the corpus does not select it",
            },
            {
                "rank": 3,
                "route": "global_section_gribov_or_fundamental_domain_measure",
                "source_status": route_by_id[
                    "global_section_gribov_or_fundamental_domain_measure"
                ]["status"],
                "reason": "A finite global quotient measure could be legal, but only after avoiding double-counting the already closed local BRST/FP rules.",
                "next_test": "source-certify a global section/fundamental-domain measure independent of target residuals",
            },
        ],
        "do_not_use": [
            "printed HYM matrix or A/B repairs as final proof sources under the current corpus",
            "local FP/BRST quotient Jacobian as an extra correction because it was already counted",
            "soft gauge tube widths or regulator widths as physical constants",
            "complex nesting/shared-circle rotations as direct Qa corrections without a source link",
            "observed electroweak or Qa residuals to choose determinant factors",
        ],
        "verdict": {
            "explicit_hym_matrix_route_currently_retired": True,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
            "next_required_artifact": "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
