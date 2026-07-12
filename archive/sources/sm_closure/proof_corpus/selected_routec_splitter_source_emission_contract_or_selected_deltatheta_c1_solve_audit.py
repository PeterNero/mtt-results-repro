"""Audit selected DeltaTheta_C1 solve gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"
CERT = REPO / "certificates" / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_DELTATHETA_C1_SOLVE_GATE_BUILT_SELECTED_HESSIAN_RESPONSE_OPERATOR_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    gate = data["selected_deltatheta_c1_solve_gate"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "target vector built",
            gate["target_real_dimension"] == 72
            and gate["target_vector_norm_sq"] > 0
            and all(value > 0 for value in gate["sector_target_norm_sq"].values()),
            gate,
        ),
        check(
            "selected operator not available",
            gate["selected_operator_available"] is False
            and gate["rank_test_computable"] is False
            and gate["least_squares_solution_computable"] is False,
            gate,
        ),
        check(
            "diagnostic identity lift rejected",
            gate["diagnostic_identity_lift_exists"] is True
            and gate["diagnostic_identity_lift_norm_sq"] == gate["target_vector_norm_sq"]
            and gate["diagnostic_identity_lift_promotable"] is False,
            gate,
        ),
        check(
            "remaining selected response operator",
            data["what_remains_open"]["selected_C1_response_operator_A_selected"] is True
            and data["what_remains_open"]["selected_source_vector_b_selected"] is True
            and data["what_remains_open"]["selected_deltaTheta_C1_solution"] is True,
            data["what_remains_open"],
        ),
        check(
            "no target fitting or closure",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records selected response operator gate",
            "A_selected * deltaTheta_C1 = b_splitter" in note
            and "selected response operator is not" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C DeltaTheta C1 solve gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
