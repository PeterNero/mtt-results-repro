from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_differentiated_phifinc1_residual_projector_axiom_or_galerkin_c1_execution_certificate.json"
STATUS = "POST_ALPHA_DIFFERENTIATED_PHIFINC1_RESIDUAL_PROJECTOR_AXIOM_OR_GALERKIN_C1_EXECUTION_IMPORTED_CONTRACT_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "two-lane implication import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "differentiated_PhiFinC1_application_rule_proved_now",
        "residual_projector_axiom_inserted_now",
        "honest_Galerkin_C1_execution_run_now",
        "sector_response_matrices_promoted",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    implication = packet["closure_implication_replay"]
    require(implication["status"] == "IMPLICATION_PROVED_ANTECEDENT_OPEN", "implication status drift")
    require(implication["proved_now"] is True, "implication not proved")
    require(implication["antecedent_currently_met"] is False, "antecedent overclaimed")
    require(implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(implication["current_numeric_replay_if_axiom_accepted"]["A_transpose_b"] == [12.0, 12.0], "A^T b drift")
    require(implication["current_numeric_replay_if_axiom_accepted"]["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")
    require(implication["if_axiom_contract_accepted_then"]["SM_parity_dynamic_packet_would_close"] is True, "axiom implication missing")
    require(implication["if_honest_galerkin_contract_filled_then"]["SM_parity_dynamic_packet_would_close"] is True, "Galerkin implication missing")

    axiom = packet["residual_projector_axiom_patch_contract"]
    require(axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED", "axiom status drift")
    require(axiom["selected_now"] is False, "axiom selected overclaimed")
    require(axiom["inserted_now"] is False, "axiom insertion overclaimed")
    require(axiom["exact_source_values_to_emit"]["phase_R_Z"]["residual_norm_sq"] == 4.0, "phase residual drift")
    require(axiom["exact_source_values_to_emit"]["shift_R_X"]["residual_norm_sq"] == 2.0, "shift residual drift")
    require(axiom["exact_source_values_to_emit"]["conditional_b_norm_sq"] == 24.0, "conditional b norm drift")
    require(axiom["new_axiom_payload_if_accepted"]["b_source_emitted"] is True, "b source payload missing")

    galerkin = packet["honest_galerkin_execution_acceptance_contract"]
    require(galerkin["status"] == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING", "Galerkin status drift")
    require(galerkin["current_values_available"]["selected_source_verified"] is False, "Galerkin source overclaimed")
    require(galerkin["current_values_available"]["sector_response_matrices_emitted"] is False, "sector matrices overemitted")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_accepted"] is True, "Galerkin closure implication missing")
    require(galerkin["would_close_no_knob_flavor_constants_by_itself"] is False, "Galerkin no-knob overclaim")

    require(STATUS in note and NEXT in note and "axiom not inserted" in note, "note missing essentials")
    print("AUDIT_PASS: differentiated PhiFinC1 axiom/Galerkin contracts imported; insertion/execution remains open")


if __name__ == "__main__":
    main()
