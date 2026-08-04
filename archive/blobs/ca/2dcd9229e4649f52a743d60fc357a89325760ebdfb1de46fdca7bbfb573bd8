"""Audit final SM-parity gap matrix / closure attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalsmparitygapmatrix_or_closureattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GAP = PACKET_DIR / "final_sm_parity_gap_matrix.packet.json"
DECISION = PACKET_DIR / "closure_attempt_decision.packet.json"
NEXT = PACKET_DIR / "minimal_next_gate_recommendation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalSMParityGapMatrix_or_ClosureAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FINALSMPARITYGAPMATRIX_OR_CLOSUREATTEMPT_BUILT_OPEN_GATES_SHARPENED"
NEXT_ARTIFACT = "MTT_Selected_CommonScaleYukawaHiggsTransport_or_FinalReplayAudit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    gap = load(GAP)
    decision = load(DECISION)
    recommendation = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(gap["status"] == "FINAL_GAP_MATRIX_BUILT_NOT_CLOSED", "gap status mismatch")
    require(len(gap["gap_rows"]) == 12, "gap row count mismatch")
    require(gap["closed_or_no_longer_blocking"]["patched_dynamic_C1_interface"] is True, "patched C1 regressed")
    require(gap["closed_or_no_longer_blocking"]["static_SM_slot_functor_source_arrows"] is True, "SM-slot closure regressed")

    expected_sm = {
        "common_scale_Yukawa_and_Higgs_transport",
        "covariance_profile_likelihood_or_tolerance_policy_execution",
        "final_integrated_empirical_replay_audit",
        "selected_SM_packet_certificate_integration",
    }
    expected_true_extra = {
        "GR_QM_measurement_interfaces",
        "local_QFT_observable_functor",
    }
    expected_no_knob = {
        "GR_QM_measurement_interfaces",
        "common_scale_Yukawa_and_Higgs_transport",
        "full_no_knob_constants",
        "local_QFT_observable_functor",
        "patched_dynamic_C1_interface",
        "selected_SM_packet_certificate_integration",
        "unpatched_no_knob_dynamic_C1_derivation",
    }
    require(set(gap["blocker_sets"]["SM_parity"]) == expected_sm, "SM parity blocker set mismatch")
    require(expected_true_extra.issubset(set(gap["blocker_sets"]["true_SM_equivalence"])), "true equivalence extras missing")
    require(set(gap["blocker_sets"]["no_knob"]) == expected_no_knob, "no-knob blocker set mismatch")

    require(decision["status"] == "CLOSURE_ATTEMPT_EVALUATED_NOT_YET_FULLY_CLOSED", "decision status mismatch")
    for key in ["patched_SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(decision[key] is False, f"closure overclaimed: {key}")
        require(data["closure_decision"][key] is False, f"candidate closure overclaimed: {key}")
    require(decision["no_regression_from_previous_work"]["patched_dynamic_C1_interface_ready"] is True, "patched C1 readiness regressed")
    require(decision["no_regression_from_previous_work"]["measured_constants_remain_downstream"] is True, "measured guardrail missing")
    require(decision["closure_guardrails"]["patched_dynamic_C1_is_patch_not_unpatched_derivation"] is True, "patch boundary missing")

    require(recommendation["status"] == "NEXT_GATE_RECOMMENDED", "recommendation status mismatch")
    require(recommendation["primary_next_gate"] == "common_scale_Yukawa_and_Higgs_transport", "wrong primary next gate")
    require(recommendation["parallel_gate"] == "selected_SM_packet_certificate_integration", "wrong parallel gate")
    require(recommendation["superset_strategy_use"]["mode"] == "combined_paths_with_locked_target", "superset strategy missing")

    for key in [
        "SM_parity_blockers_separated_from_true_equivalence_blockers",
        "closure_attempt_evaluated",
        "final_gap_matrix_built",
        "minimal_next_gate_selected",
        "no_knob_blockers_separated_from_SM_parity",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require("patched SM-parity closed = False" in note, "note missing closure guardrail")
    require("common-scale Yukawa/Higgs transport" in note, "note missing primary blocker")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
