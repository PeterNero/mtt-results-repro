from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_phifinc1_residual_projector_application_or_honest_galerkin_execution_valuefill_certificate.json"
)
STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_PHIFINC1_RESIDUAL_PROJECTOR_APPLICATION_OR_"
    "HONEST_GALERKIN_EXECUTION_IMPORTED_NOGO_OPEN"
)
NEXT = "MTT_Selected_DifferentiatedResidualProjectorSourceRule_or_HonestGalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "fresh long no-go theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    application = packet["phifinc1_projector_application_audit"]
    require(application["status"] == "PROJECTOR_APPLICATION_NOT_DERIVED_BY_EXISTING_PHIFINC1_ARTIFACTS", "application status drift")
    no_go = application["blocking_no_go"]
    require(no_go["proved"] is True, "transport-only no-go not proved")
    require(no_go["all_sector_matrices_verified_zero"] is True, "sector matrices are not all zero")
    require(no_go["canonical_all_zero"] is True, "canonical zero no-go drift")
    require(application["promotion_decision"]["PhiFinC1_projector_application_promoted"] is False, "application overclaimed")
    require(application["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False, "SM parity overclaimed")

    conditional = application["conditional_value_if_new_application_rule_is_proved"]
    require(conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "conditional A^T A drift")
    require(conditional["A_transpose_b"] == [12.0, 12.0], "conditional A^T b drift")
    require(conditional["deltaTheta_C1"] == [1.0, 1.0], "conditional deltaTheta drift")
    require(conditional["SM_parity_dynamic_packet_would_close"] is True, "conditional SM implication missing")
    require(conditional["no_knob_flavor_constants_would_close"] is False, "no-knob overclaim")

    route = packet["application_or_execution_decision"]
    require(route["status"] == "APPLICATION_NOGO_EXECUTION_VALUES_OPEN", "route decision drift")
    require("selected differentiated residual-projector source rule" in route["what_would_close_next"], "next source rule missing")

    contract = packet["honest_galerkin_execution_contract"]
    require(contract["status"] == "HONEST_GALERKIN_EXECUTION_VALUES_OPEN", "execution contract drift")
    require(contract["selected_source_verified_now"] is False, "execution source overclaimed")
    require(contract["target_fitting_forbidden"] is True, "target fitting guardrail missing")
    require(contract["observed_flavor_data_forbidden"] is True, "observed-data guardrail missing")

    require(STATUS in note and NEXT in note and "stationary-transport no-go" in note, "note missing essentials")
    print("AUDIT_PASS: fresh long PhiFinC1 transport-only no-go imported; differentiated source rule remains open")


if __name__ == "__main__":
    main()
