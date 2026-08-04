from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_differentiated_phifinc1_residual_projector_contract_certificate.json"
STATUS = "POST_ALPHA_DIFFERENTIATED_PHIFINC1_RESIDUAL_PROJECTOR_CONTRACT_IMPORTED_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "contract theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["two_lane_acceptance_target_fixed"] is True, "two-lane target missing")
    require(decision["closure_implication_proved"] is True, "closure implication missing")
    require(decision["residual_projector_axiom_inserted_now"] is False, "axiom insertion overclaimed")
    require(decision["honest_Galerkin_C1_execution_run_now"] is False, "Galerkin execution overclaimed")
    require(decision["frontier_is_axiom_insertion_or_first_Galerkin_execution"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    axiom = packet["axiom_contract"]
    require(axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED", "wrong axiom contract status")
    require(axiom["inserted_now"] is False, "axiom inserted")
    require(axiom["selected_now"] is False, "axiom selected")
    require(axiom["exact_source_values_to_emit"]["phase_R_Z"]["residual_norm_sq"] == 4.0, "phase residual drift")
    require(axiom["exact_source_values_to_emit"]["shift_R_X"]["residual_norm_sq"] == 2.0, "shift residual drift")
    require(axiom["exact_source_values_to_emit"]["conditional_b_norm_sq"] == 24.0, "b norm drift")

    replay = packet["closure_implication_replay"]
    require(replay["status"] == "IMPLICATION_PROVED_ANTECEDENT_OPEN", "wrong replay status")
    require(replay["antecedent_currently_met"] is False, "antecedent overclaimed")
    require(replay["current_numeric_replay_if_axiom_accepted"]["rank"] == 2, "rank drift")
    require(replay["current_numeric_replay_if_axiom_accepted"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(replay["current_numeric_replay_if_axiom_accepted"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(replay["current_numeric_replay_if_axiom_accepted"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")

    galerkin = packet["honest_galerkin_execution_acceptance_contract"]
    require(galerkin["status"] == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING", "wrong Galerkin contract status")
    require(galerkin["current_values_available"]["A_selected_emitted"] is False, "A emitted")
    require(galerkin["current_values_available"]["b_selected_emitted"] is False, "b emitted")
    require(galerkin["current_values_available"]["sector_response_matrices_emitted"] is False, "sector matrices emitted")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "coordinate target drift")
    require(STATUS in note and NEXT in note and "antecedent is open" in note, "note missing essentials")
    print("AUDIT_PASS: differentiated PhiFin C1 residual-projector contract imported; axiom insertion/Galerkin execution remain open")


if __name__ == "__main__":
    main()
