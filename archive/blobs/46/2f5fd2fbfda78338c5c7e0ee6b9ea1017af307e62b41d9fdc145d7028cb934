"""Audit Step 25 threshold external replay / no-knob kernel cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step25_thresholdexternalreplay_noknobkernel_or_fulls2cutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXTERNAL_KERNEL = PACKET_DIR / "step25_external_replay_and_noknob_kernel.packet.json"
INTERNAL_BLOCKER = PACKET_DIR / "step25_internal_scalar_emission_blocker.packet.json"
NEXT_CUTSET = PACKET_DIR / "step25_to_step26_fulls2_payload_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step25_ThresholdExternalReplay_NoKnobKernel_or_FullS2Cutset_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP25_THRESHOLDEXTERNALREPLAY_NOKNOBKERNEL_OR_FULLS2CUTSET_BUILT_EXTERNAL_REPLAY_AND_KERNEL_CLOSED_FULLS2_INTERNAL_ROWS_OPEN"
NEXT = "MTT_Selected_PhiFinMinimizerTraceSectorPayload_or_InternalScalarRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    external_kernel = load(EXTERNAL_KERNEL)
    internal_blocker = load(INTERNAL_BLOCKER)
    cutset = load(NEXT_CUTSET)
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

    threshold = external_kernel["threshold_external_replay"]
    require(threshold["accepted_external_source_row_imported"] is True, "external source row not imported")
    require(threshold["accepted_external_threshold_row_count"] == 7, "threshold row count mismatch")
    require(threshold["accepted_external_mass_scheme_row_count"] == 3, "mass row count mismatch")
    require(threshold["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile not closed")
    require(threshold["external_import_lane_closed_at_admitted_replay_tier"] is True, "external lane not closed")
    require(threshold["external_rows_used_as_branch_selector"] is False, "external rows used as selector")
    require(threshold["closure_tier"] == "admitted external replay", "wrong external closure tier")
    require(threshold["internal_selected_Rtheta_value_row_emitted"] is False, "internal row overemitted")
    require(threshold["selected_threshold_response_functional_instantiated"] is False, "internal threshold functional overclosed")

    readiness = external_kernel["readiness"]
    require(readiness["readiness_fraction"] == "8/9", "readiness mismatch")
    require(readiness["present_count"] == 8, "present count mismatch")
    require(readiness["requirement_count"] == 9, "requirement count mismatch")
    require(readiness["only_remaining_readiness_blocker"] == "no_knob_value_derivation", "wrong readiness blocker")
    require(readiness["closed_value_obligation_rows_at_admitted_external_tier"] == 4, "external obligation count mismatch")
    require(readiness["closed_value_obligation_rows_at_internal_no_knob_tier"] == 0, "internal obligation overclosed")

    kernel = external_kernel["no_knob_kernel"]
    require(kernel["final_no_knob_kernel_typed"] is True, "no-knob kernel not typed")
    require(kernel["selected_internal_value_emission_count"] == 0, "kernel emitted internal values")
    require(kernel["selected_universal_parameter_count"] == 0, "universal parameter selected")
    require(kernel["true_SM_equivalence_closed"] is False, "kernel overclosed true SM")
    require(kernel["full_no_knob_closed"] is False, "kernel overclosed no-knob")

    internal = internal_blocker["internal_attempt"]
    require(internal["kernel_readiness"] == "8/9", "internal readiness mismatch")
    require(internal["value_source_obligation_closed_row_count"] == 0, "value obligation overclosed")
    require(internal["accepted_internal_scalar_row_count"] == 0, "internal scalar rows emitted")
    require(internal["fullS2_payload_ready"] is False, "fullS2 overready")
    require(internal["universal_anchor_selected"] is False, "anchor selected")
    require(internal["lambda_H_row_emitted"] is False, "lambda_H row overemitted")
    require(internal["true_SM_equivalence_closed"] is False, "internal overclosed true SM")
    require(internal["full_no_knob_closed"] is False, "internal overclosed no-knob")
    require(internal_blocker["closure_claimed"] is False, "internal blocker overclaimed")

    decision = data["closure_decision"]
    require(decision["step24_next_artifact_executed"] is True, "Step24 next not executed")
    require(decision["admitted_external_threshold_rows_closed"] is True, "threshold rows not closed")
    require(decision["admitted_external_threshold_row_count"] == 7, "candidate threshold count mismatch")
    require(decision["admitted_external_mass_scheme_rows_closed"] is True, "mass rows not closed")
    require(decision["admitted_external_mass_scheme_row_count"] == 3, "candidate mass count mismatch")
    require(decision["accepted_diagonal_profile_theorem_closed_at_replay_tier"] is True, "diagonal theorem missing")
    require(decision["final_no_knob_kernel_typed"] is True, "kernel not typed")
    require(decision["Rtheta_readiness_8_of_9"] is True, "Rtheta readiness not preserved")
    require(decision["direct_internal_scalar_attempt_executed"] is True, "internal attempt not executed")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate internal rows overemitted")
    require(decision["selected_internal_value_emission_count"] == 0, "candidate values overemitted")
    require(decision["selected_universal_parameter_count"] == 0, "candidate universal parameter selected")
    require(decision["selected_fullS2_payload_ready"] is False, "candidate fullS2 overready")
    require(decision["candidate_specific_universal_source_anchor_selected"] is False, "candidate anchor selected")
    require(decision["lambda_H_row_emitted"] is False, "candidate lambda_H overemitted")
    require(decision["true_SM_equivalence_closed"] is False, "candidate true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "candidate no-knob overclosed")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    for key in [
        "admitted_external_threshold_rows",
        "admitted_external_mass_scheme_rows",
        "accepted_diagonal_profile_theorem_at_replay_tier",
        "final_no_knob_kernel_typed",
        "direct_internal_scalar_attempt_executed",
    ]:
        require(cutset["closed_do_not_reopen"][key] is True, f"cutset close flag missing: {key}")
    for key in [
        "selected_fullS2_rhoE_D_E_operator_payload",
        "Phi_fin_selected_minimizer_trace",
        "candidate_specific_universal_source_anchor",
        "internal_Rtheta_scalar_value_rows",
        "lambda_H_value_execution",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")

    for phrase in [
        "admitted external threshold rows                            7",
        "accepted internal scalar rows                               0",
        "selected full-S2 rhoE/D_E/operator payload                  open",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
