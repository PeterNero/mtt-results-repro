"""Audit the selected HYM operator-values gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_routec_hym_operator_values_gate.candidate.json"
CERT = ROOT / "certificates" / "selected_routec_hym_operator_values_gate_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_RouteC_HYM_OperatorValues_or_DERieszGreenDotD_Source_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_ROUTEC_HYM_OPERATOR_VALUES_GATE_BUILT_VALUES_NOT_EMITTED", "unexpected status")
    require(data["closure_claimed"] is False, "must not claim closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    require(data["abstract_HYM_import"]["selected_equalradius_HYM_existence"] is True, "HYM bridge import missing")
    require(data["selected_operator_values_closed"] is False, "operator values must remain open")
    require(data["shape_support"]["honest_smoke_has_zero_residuals"] is True, "expected zero residual support")
    require(data["shape_support"]["lifted_flag_matrices_pass_lower_validators"] is True, "expected lifted validator support")
    require(data["source_flags_on_honest_smoke"]["route_c_residual_selected_source_verified"] is False, "honest residual source flag should be false")
    require(data["source_flags_on_honest_smoke"]["de_action_all_selected_source_verified"] is False, "honest D_E flags should be false")
    require(data["source_flags_on_honest_smoke"]["selected_dotD_source_verified"] is False, "honest dotD flags should be false")
    require(data["source_flags_on_honest_smoke"]["alpha1_driver_verified"] is False, "honest alpha1 driver flags should be false")
    require(data["what_closes_now"]["abstract_HYM_no_longer_blocker"] is True, "abstract HYM blocker should close")
    require(data["what_closes_now"]["exact_missing_extraction_theorem_identified"] is True, "extraction theorem should be identified")
    require(data["what_remains_open"]["selected_D_E_Riesz_Green_dotD"] is True, "D_E/Riesz/Green/dotD must remain open")
    require(
        data["next_required_artifact"] == "MTT_Selected_HYM_Connection_to_Finite_Operator_Extraction_v1",
        "wrong next artifact",
    )
    require(cert["selected_operator_values_closed"] is False, "certificate must keep values open")
    normalized_proof = " ".join(proof.split())
    require("concrete finite operator values are not emitted yet" in normalized_proof, "proof must state non-emission")
    require("selected-source flags are false" in proof, "proof must state source-flag guardrail")

    print("PASS selected Route-C HYM operator-values gate audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
