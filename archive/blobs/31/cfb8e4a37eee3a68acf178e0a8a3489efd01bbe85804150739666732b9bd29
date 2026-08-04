"""Import the selected C1 response-operator emission audit."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure"

FIBER_REDUCTION = CERTS / "noninvariant_c1_fiberclass_reduction_certificate.json"
SM_CERT = SM / "certificates" / "selected_routec_selected_c1_response_operator_emission_certificate.json"
SM_CANDIDATE = SM / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json"

OUTPUT = CERTS / "selected_c1_response_operator_emission_audit_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    fiber = load(FIBER_REDUCTION)
    sm_cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)

    audit = candidate["emission_audit"]
    lanes = candidate["response_lanes"]
    contract = candidate["operator_emission_contract"]

    output = {
        "certificate": "SelectedC1ResponseOperatorEmissionAuditImport",
        "status": "SELECTED_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED",
        "inputs": {
            "local_noninvariant_c1_fiberclass_reduction": str(FIBER_REDUCTION.relative_to(ROOT)),
            "sm_selected_c1_response_operator_emission": str(SM_CERT),
            "sm_selected_c1_response_operator_candidate": str(SM_CANDIDATE),
        },
        "closed_now": {
            "selected_response_operator_schema_audited": sm_cert["what_closes"][
                "selected_response_operator_schema_audited"
            ],
            "canonical_zero_response_separated_from_nonzero_unselected_candidates": sm_cert[
                "what_closes"
            ]["canonical_zero_response_separated_from_nonzero_unselected_candidates"],
            "A_selected_emission_blocker_identified": sm_cert["what_closes"][
                "A_selected_emission_blocker_identified"
            ],
            "q79_template_and_extraction_attempt_imported": sm_cert["what_closes"][
                "q79_template_and_extraction_attempt_imported"
            ],
            "target_fitting_excluded": sm_cert["what_closes"]["target_fitting_excluded"],
        },
        "operator_contract": {
            "name": contract["name"],
            "operator_equation": contract["operator_equation"],
            "codomain_real_dimension": contract["codomain_real_dimension"],
            "domain_must_include": contract["domain_must_include"],
            "validators_after_emission": contract["validators_after_emission"],
            "forbidden_shortcuts": contract["forbidden_shortcuts"],
        },
        "audit_result": {
            "selected_operator_A_selected_emitted": audit["selected_operator_A_selected_emitted"],
            "selected_source_vector_b_selected_emitted": audit["selected_source_vector_b_selected_emitted"],
            "least_squares_now_computable": audit["least_squares_now_computable"],
            "rank_test_now_computable": audit["rank_test_now_computable"],
            "template_principal_hessian_blocks_present": audit[
                "template_principal_hessian_blocks_present"
            ],
            "template_driver_row_present": audit["template_driver_row_present"],
            "template_response_matrices_null": audit["template_response_matrices_null"],
            "extraction_attempt_status": audit["extraction_attempt_status"],
            "extraction_attempt_result": audit["extraction_attempt_result"],
        },
        "response_lanes": {
            "canonical_smooth_bn_response": lanes["canonical_smooth_bn_response"],
            "noninvariant_candidate_response": lanes["noninvariant_candidate_response"],
            "straight_selected_c1_response": lanes["straight_selected_c1_response"],
        },
        "not_closed": {
            "emit_selected_A_selected": sm_cert["what_remains_open"]["emit_selected_A_selected"],
            "emit_selected_b_selected": sm_cert["what_remains_open"]["emit_selected_b_selected"],
            "selected_Hess_Xi_finite_blocks": sm_cert["what_remains_open"][
                "selected_Hess_Xi_finite_blocks"
            ],
            "selected_dotD_Q_u_d_L_e_N_H": sm_cert["what_remains_open"][
                "selected_dotD_Q_u_d_L_e_N_H"
            ],
            "selected_zero_mode_bases_and_Gram_Schmidt": sm_cert["what_remains_open"][
                "selected_zero_mode_bases_and_Gram_Schmidt"
            ],
            "selected_primitive_C1_contractions": sm_cert["what_remains_open"][
                "selected_primitive_C1_contractions"
            ],
            "selected_sector_response_matrices": sm_cert["what_remains_open"][
                "selected_sector_response_matrices"
            ],
            "solve_or_reject_splitter_equation": sm_cert["what_remains_open"][
                "solve_or_reject_splitter_equation"
            ],
            "full_SM_closure": sm_cert["what_remains_open"]["full_SM_or_no_knob_closure"],
        },
        "next_closing_object": {
            "name": "Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1",
            "must_emit": [
                "selected finite Hess_Xi lower-order blocks",
                "selected alpha1 source vector b_selected",
                "selected dotD operators for Q,u,d,L,e,N,H",
                "selected zero-mode bases and L2 Gram-Schmidt rule",
                "selected primitive C1 contractions",
                "sector response matrices M_u, M_d, M_e, M_nuD",
            ],
        },
        "guardrails": {
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_deltaTheta_C1_solved": False,
            "claims_flavor_closure": False,
            "uses_observed_flavor_data": False,
        },
        "honest_answer": (
            "The selected C1 response equation is now structurally specified but not "
            "computable: A_selected and b_selected are absent. The next proof step is "
            "not a numerical solve; it is rebuilding the selected Galerkin/source "
            "packet that emits those finite blocks."
        ),
        "previous_reduction_status": fiber["status"],
    }

    if "--write-certificate" in sys.argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
