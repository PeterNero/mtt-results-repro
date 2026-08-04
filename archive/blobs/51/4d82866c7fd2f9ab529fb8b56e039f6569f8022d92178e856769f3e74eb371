"""Audit Step 26 Phi_fin trace / matter-slot reconciliation cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step26_phifintrace_matterslot_reconciliation_or_fulls2payloadcutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_PACKET = PACKET_DIR / "step26_phifin_trace_and_transport_replay.packet.json"
MATTER_PACKET = PACKET_DIR / "step26_static_matter_slot_reconciliation.packet.json"
FULLS2_CUTSET = PACKET_DIR / "step26_fulls2_operator_payload_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step26_PhiFinTraceMatterSlotReconciliation_or_FullS2PayloadCutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP26_PHIFINTRACE_MATTERSLOT_RECONCILIATION_OR_FULLS2PAYLOADCUTSET_BUILT_TRACE_AND_STATIC_MATTER_CLOSED_FULLS2_PAYLOAD_OPEN"
NEXT = "MTT_Selected_RhoEDEFullS2OperatorPayload_or_InternalScalarRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    trace = load(TRACE_PACKET)
    matter = load(MATTER_PACKET)
    cutset = load(FULLS2_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    require(trace["functional_PhiFin_trace_closed"] is True, "Phi_fin trace not closed")
    require(trace["symbolic_transport_finite_morphism_valid"] is True, "symbolic transport not valid")
    require(trace["transport_closed_validator_replay_closed"] is True, "transport validator not closed")
    require(trace["validator_ready_sector_rho_s_packet"] is True, "rho_s packet not ready")
    require(trace["same_branch_alpha1_derivative_closed"] is True, "alpha1 derivative not closed")
    require(trace["gauge_trace"]["functional_selected_trace_proved"] is True, "gauge trace not proved")
    require(trace["gauge_trace"]["selected_source_verified_for_functional_End0_trace"] is True, "functional End0 source not verified")
    require(trace["symbolic_transport"]["closure_claimed"] is True, "symbolic finite replay not closed")
    require(trace["symbolic_transport"]["symbolic_transport_quotient_used"] is True, "symbolic quotient not used")
    require(trace["symbolic_transport"]["raw_27mode_finite_replay_closed"] is False, "raw 27-mode overclosed")
    require(trace["symbolic_transport"]["selected_rho_s_validator_ready"] is True, "rho_s validator not ready")
    require(trace["symbolic_transport"]["selected_dotD_source_verified"] is False, "dotD overclosed by transport")

    outputs = matter["selected_static_tier_outputs"]
    for key in [
        "selected_matter_slot_transversality_readout",
        "selected_U10_clock_source",
        "selected_Ubar5_shift_source",
        "selected_1M_Dirac_neutrino_shift_source",
        "selected_ordered_matter_slot_packet",
        "selected_overlap_transfer_normalization_static_tier",
    ]:
        require(outputs[key] is True, f"static matter output missing: {key}")
    require(matter["static_matter_slot_readout_closed"] is True, "static readout not closed")
    require(matter["static_U10_Ubar5_1M_source_closed"] is True, "static source not closed")
    require(matter["internal_scalar_gate_after_static_readout"]["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(matter["internal_scalar_gate_after_static_readout"]["dynamic_overlap_kernel_layer"] is False, "dynamic overlap overclosed")
    require(matter["internal_scalar_gate_after_static_readout"]["dynamic_PhiFin_C1_payload_layer"] is False, "dynamic PhiFin C1 overclosed")

    state = cutset["current_fullS2_payload_state"]
    require(state["diagonal_End0_operator_payload_closed"] is True, "diagonal End0 support missing")
    require(state["rhoE_DE_fullS2_execution_closed"] is False, "rhoE/DE fullS2 overclosed")
    require(state["selected_HYM_sector_payload_closed"] is False, "HYM sector payload overclosed")
    require(state["rank2_to_sector_transfer_closed"] is False, "rank2-sector overclosed")
    require(state["physical_dotD_alpha1_closed"] is False, "physical dotD overclosed")
    require(state["phi_fin_dynamic_c1_payload_closed"] is False, "PhiFin dynamic C1 overclosed")
    require(state["typed_bn_retarded_derivative_closed"] is False, "typed BN overclosed")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for key in [
        "functional_PhiFin_trace",
        "symbolic_transport_finite_morphism",
        "transport_closed_validator_replay",
        "validator_ready_sector_rho_s_packet",
        "same_branch_alpha1_derivative",
        "static_U10_Ubar5_1M_matter_slot_source_tier",
    ]:
        require(cutset["closed_do_not_reopen"][key] is True, f"cutset close flag missing: {key}")
    for key in [
        "selected_fullS2_rhoE_D_E_operator_payload",
        "selected_D_E_Riesz_Green_dotD_dynamic_payload",
        "dynamic_PhiFin_C1_payload",
        "typed_BN_retarded_derivative",
        "candidate_specific_universal_source_anchor",
        "internal_Rtheta_scalar_rows",
        "lambda_H_row_emission",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")

    decision = data["closure_decision"]
    for key in [
        "functional_PhiFin_trace_closed",
        "symbolic_transport_finite_morphism_closed",
        "transport_closed_validator_replay_closed",
        "validator_ready_sector_rho_s_packet_closed",
        "same_branch_alpha1_derivative_closed",
        "static_U10_Ubar5_1M_source_closed",
        "static_matter_slot_readout_closed",
        "selected_ordered_matter_slot_packet_static_tier",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
    for key in [
        "selected_fullS2_rhoE_D_E_operator_payload_closed",
        "selected_D_E_Riesz_Green_dotD_dynamic_payload_closed",
        "dynamic_PhiFin_C1_payload_closed",
        "typed_BN_retarded_derivative_closed",
        "candidate_specific_universal_source_anchor_selected",
        "lambda_H_row_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["selected_fullS2_rhoE_D_E_operator_payload_closed"] is False, "certificate overclosed fullS2")

    for phrase in [
        "functional Phi_fin trace                                  closed",
        "static U10/Ubar5/1M matter-slot source tier                 closed",
        "selected full-S2 rhoE/D_E operator payload                 open",
        "accepted internal Rtheta scalar rows                       0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
