"""Audit differentiated PhiFinC1 residual-projector axiom / Galerkin C1 execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AXIOM_PACKET = PACKET_DIR / "residual_projector_axiom_patch_contract.packet.json"
GALERKIN_PACKET = PACKET_DIR / "honest_galerkin_execution_acceptance_contract.packet.json"
IMPLICATION_PACKET = PACKET_DIR / "closure_implication_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_RESIDUALPROJECTORAXIOM_OR_GALERKINC1EXECUTION_BUILT_CONTRACT_OPEN"
NEXT = "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    axiom = load(AXIOM_PACKET)
    galerkin = load(GALERKIN_PACKET)
    implication = load(IMPLICATION_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(axiom["status"] == "AXIOM_CONTRACT_READY_NOT_INSERTED", "axiom status mismatch")
    premises = axiom["premises_required"]
    for key in [
        "selected_qutrit_weyl_carrier",
        "selected_static_route_Z_clock_to_u_e",
        "selected_static_route_X_shift_to_d_nuD",
        "selected_trace_transfer_normalization",
        "canonical_Q_residual_available",
        "alpha1_dotD_driver_verified",
    ]:
        require(premises[key] is True, f"axiom premise missing: {key}")
    require(axiom["new_axiom_payload_if_accepted"]["selected_differentiated_PhiFinC1_applies_Q_residual"] is True, "axiom payload missing PhiFinC1 rule")
    require(axiom["new_axiom_payload_if_accepted"]["b_source_emitted"] is True, "axiom payload missing b source")
    require(axiom["exact_source_values_to_emit"]["routed_total_residual_norm_sq"] == 12.0, "residual norm mismatch")
    require(axiom["exact_source_values_to_emit"]["conditional_b_norm_sq"] == 24.0, "b norm mismatch")
    require(axiom["inserted_now"] is False, "axiom inserted overclaimed")
    require(axiom["selected_now"] is False, "axiom selected overclaimed")

    require(galerkin["status"] == "GALERKIN_EXECUTION_CONTRACT_READY_VALUES_MISSING", "Galerkin status mismatch")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "Galerkin coordinate mismatch")
    for key in [
        "selected_source_verified",
        "can_replace_source_map_now",
        "A_selected_emitted",
        "b_selected_emitted",
        "sector_response_matrices_emitted",
    ]:
        require(galerkin["current_values_available"][key] is False, f"Galerkin overclaimed: {key}")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_accepted"] is True, "Galerkin SM implication missing")
    require(galerkin["would_close_no_knob_flavor_constants_by_itself"] is False, "Galerkin no-knob overclaim")

    require(implication["status"] == "IMPLICATION_PROVED_ANTECEDENT_OPEN", "implication status mismatch")
    require(implication["proved_now"] is True, "implication theorem not proved")
    require(implication["antecedent_currently_met"] is False, "antecedent overclaimed")
    replay = implication["current_numeric_replay_if_axiom_accepted"]
    require(replay["rank"] == 2, "rank mismatch")
    require(replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(replay["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(replay["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(implication["if_axiom_contract_accepted_then"]["SM_parity_dynamic_packet_would_close"] is True, "axiom implication missing")
    require(implication["if_honest_galerkin_contract_filled_then"]["SM_parity_dynamic_packet_would_close"] is True, "Galerkin implication missing")
    require(implication["if_axiom_contract_accepted_then"]["no_knob_flavor_constants_would_close"] is False, "axiom no-knob overclaim")
    require(implication["if_honest_galerkin_contract_filled_then"]["no_knob_flavor_constants_would_close_by_default"] is False, "Galerkin no-knob overclaim")

    for key in [
        "residual_projector_axiom_contract_built",
        "honest_Galerkin_execution_contract_built",
        "closure_implication_replay_proved",
        "acceptance_tests_for_both_lanes_fixed",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "derive_or_insert_residual_projector_axiom",
        "prove_selected_differentiated_PhiFinC1_application_rule",
        "emit_selected_b_source_vector",
        "run_honest_selected_Galerkin_C1_execution",
        "promote_A_selected",
        "promote_b_selected",
        "promote_deltaTheta_C1",
        "emit_sector_response_matrices",
        "SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    for key in [
        "residual_projector_axiom_inserted_now",
        "differentiated_PhiFinC1_application_rule_proved_now",
        "honest_Galerkin_C1_execution_run_now",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "sector_response_matrices_promoted",
        "SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(data["promotion_decision"][key] is False, f"promotion overclaimed: {key}")
    for key in ["observed_data_used", "target_fitting_used", "closure_claimed"]:
        require(data[key] is False, f"guardrail overclaimed: {key}")

    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("neither lane" in note and "selected yet" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
