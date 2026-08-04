"""Audit current direct H K threshold row exit test."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_directhkthresholdrow_currentexit_or_radialsource"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLAR_PACKET = PACKET_DIR / "direct_hk_polar_prerequisite_recheck.packet.json"
RADIAL_PACKET = PACKET_DIR / "direct_hk_radial_value_source_gate.packet.json"
DIRECT_PACKET = PACKET_DIR / "direct_kthreshold_omega_h_lambda_execution_attempt.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_radial_source_or_direct_NH_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DirectHKThresholdRow_CurrentExit_or_RadialSource_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIRECTHKTHRESHOLDROW_CURRENTEXIT_PHASE_CLOSED_RADIAL_SOURCE_OPEN"
NEXT = "MTT_Selected_HRadialSourceValue_or_DirectNHExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    polar = load(POLAR_PACKET)
    radial = load(RADIAL_PACKET)
    direct = load(DIRECT_PACKET)
    contract = load(NEXT_CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("polar", polar),
        ("radial", radial),
        ("direct", direct),
        ("contract", contract),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    for key in [
        "m0_tracefree_quotient_promoted",
        "sigma_D_orientation_promoted",
        "phase_axis_promoted",
        "phi_sign_promoted",
        "strict_phi_Omega_promoted",
        "radial_norm_law_promoted",
    ]:
        require(polar[key] is True, f"polar missing {key}")
    require(polar["strict_r_H_promoted"] is False, "r_H overpromoted")
    require(polar["strict_Herm2_rows_promoted"] is False, "Herm2 overpromoted")

    require(radial["controlled_r_H_postcheck_only"] > 0, "controlled r_H")
    require(radial["accepted_radial_action_norm_value_rows"] == 0, "radial rows overaccepted")
    require(radial["accepted_H_lambda_bridge_value_rows"] == 0, "H lambda bridge overaccepted")
    require(radial["accepted_numeric_radial_value_sources"] == 0, "numeric radial overaccepted")
    require(radial["direct_N_H_value_emitted"] is False, "N_H overemitted")
    require(radial["selected_L_rowlocal_Omega_H_lambda_emitted"] is False, "L overemitted")
    require(radial["selected_T_scheme_Omega_H_lambda_emitted"] is False, "T overemitted")
    require(radial["lambda_H_source_value_payload_emitted"] is False, "lambda payload overemitted")

    require(direct["required_output"] == "K_threshold.Omega_H.lambda", "direct output")
    require(direct["direct_exit_from_current_frontier"] == "K_threshold.Omega_H.lambda", "frontier exit")
    latest = direct["latest_row_certificate_payload"]
    require(latest["B_Huv_support_imported"] is True, "B_Huv support")
    require(latest["payload_manifest_fixed"] is True, "manifest")
    require(latest["support_slots_available"] == 4, "support slots")
    require(latest["payload_slots_required"] == 8, "payload slots")
    require(latest["accepted_payload_slot_count"] == 0, "payload overaccepted")
    require(latest["accepted_value_row_count"] == 0, "value rows overaccepted")
    require(latest["accepted_final_certificate_count"] == 0, "certs overaccepted")
    current = direct["current_decision"]
    require(current["phase_and_direction_prerequisites_closed"] is True, "phase prereqs")
    require(current["radial_norm_law_closed"] is True, "norm law")
    require(current["numeric_radial_source_value_emitted"] is False, "radial overemitted")
    require(current["direct_N_H_value_emitted"] is False, "N_H direct overemitted")
    require(current["direct_K_threshold_Omega_H_lambda_emitted"] is False, "direct K overemitted")
    require(current["strict_H_K_threshold_row_emitted"] is False, "H K overemitted")
    require(current["accepted_selected_K_source_row_count"] == 9, "K accepted")
    require(current["selected_K_threshold_row_count_required"] == 10, "K required")

    require(contract["status"] == "RADIAL_SOURCE_VALUE_OR_DIRECT_NH_REQUIRED", "contract status")
    require(contract["strict_K_threshold_count"] == {"accepted": 9, "required": 10}, "contract K")
    for phrase in [
        "trace-free m0=0",
        "ordered T3/sigma_D=+1 orientation",
        "q79/F,m=1 +i phase sign",
        "radial norm law on the selected Herm(2) ray",
        "formal RO.q79F1.Omega_H.lambda operator domain readiness",
    ]:
        require(phrase in contract["already_closed_for_direct_exit"], f"closed phrase {phrase}")
    for phrase in [
        "controlled HRG radial value as strict source",
        "near miss z448*sqrt2/phi as exact source identity",
        "B_Huv support slots as final Herm(2) value certificates",
        "model-active HYM/Galerkin values as selected H K row",
    ]:
        require(phrase in contract["must_not_use"], f"must-not-use {phrase}")

    decision = data["closure_decision"]
    for key in [
        "direct_exit_executed_current_frontier",
        "m0_tracefree_quotient_promoted",
        "sigma_D_orientation_promoted",
        "strict_phi_Omega_promoted",
        "radial_norm_law_promoted",
    ]:
        require(decision[key] is True, f"decision missing {key}")
    for key in [
        "strict_r_H_promoted",
        "numeric_radial_source_value_emitted",
        "direct_N_H_value_emitted",
        "selected_L_rowlocal_Omega_H_lambda_emitted",
        "selected_T_scheme_Omega_H_lambda_emitted",
        "direct_K_threshold_Omega_H_lambda_emitted",
        "strict_H_K_threshold_row_emitted",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "decision K")
    require(decision["selected_K_threshold_row_count_required"] == 10, "decision K required")

    for phrase in [
        "DirectHKThresholdCurrentExitReductionTheorem",
        "The direct `K_threshold.Omega_H.lambda` exit has been re-executed",
        "Accepted numeric radial source values: `0`",
        "Direct `N_H` values emitted: `false`",
        "Direct `K_threshold.Omega_H.lambda` emitted: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: direct H K exit reduced to radial source value or direct N_H.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
