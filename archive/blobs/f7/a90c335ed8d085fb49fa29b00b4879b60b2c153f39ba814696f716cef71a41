"""Audit selected C1 response-operator emission."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_c1_response_operator_emission.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_c1_response_operator_emission_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_RESPONSE_OPERATOR_EMISSION_AUDITED_A_SELECTED_NOT_EMITTED"
NEXT = "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    emission = data["emission_audit"]
    lanes = data["response_lanes"]
    contract = data["operator_emission_contract"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "selected operator not emitted",
            emission["selected_operator_A_selected_emitted"] is False
            and emission["selected_source_vector_b_selected_emitted"] is False
            and emission["rank_test_now_computable"] is False
            and emission["least_squares_now_computable"] is False,
            emission,
        ),
        check(
            "schema support imported",
            emission["template_schema_present"] is True
            and emission["template_status"] == "OPEN"
            and emission["template_driver_row_present"] is True
            and emission["template_principal_hessian_blocks_present"] is True
            and all(emission["template_response_matrices_null"].values()),
            emission,
        ),
        check(
            "extraction attempt blocked by missing values",
            emission["extraction_attempt_present"] is True
            and emission["extraction_attempt_status"] == "C1_RESPONSE_EXTRACTION_BLOCKED_MISSING_SELECTED_OPERATOR_DATA"
            and emission["extraction_attempt_result"]["alpha1_driver_row_computed"] is True
            and emission["extraction_attempt_result"]["M_C1_alpha1_entries_computed"] is False
            and all(emission["extraction_attempt_missing_nulls"].values()),
            emission,
        ),
        check(
            "lanes separated",
            lanes["straight_selected_c1_response"]["usable_as_proof"] is False
            and lanes["canonical_smooth_bn_response"]["nonzero_response_found"] is False
            and lanes["canonical_smooth_bn_response"]["usable_as_proof"] is False
            and lanes["noninvariant_candidate_response"]["nonzero_unselected_candidates_found"] > 0
            and lanes["noninvariant_candidate_response"]["can_close_selected_C1_now"] is False,
            lanes,
        ),
        check(
            "contract targets A selected",
            contract["name"] == "SelectedC1ResponseOperatorEmissionContract"
            and contract["codomain_real_dimension"] == 72
            and "selected C1 deformation coordinates after gauge fixing" in contract["domain_must_include"]
            and len(contract["validators_after_emission"]) >= 6,
            contract,
        ),
        check(
            "no target fitting or closure",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check(
            "remaining rebuild gate",
            data["what_remains_open"]["emit_selected_A_selected"] is True
            and data["what_remains_open"]["emit_selected_b_selected"] is True
            and data["what_remains_open"]["selected_sector_response_matrices"] is True,
            data["what_remains_open"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records not emitted",
            "It is not emitted yet" in note
            and "canonical smooth B_N C1 response is computed but zero" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C C1 response-operator emission audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
