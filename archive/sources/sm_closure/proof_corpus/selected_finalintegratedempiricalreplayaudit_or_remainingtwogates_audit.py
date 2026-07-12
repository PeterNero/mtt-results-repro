"""Audit final integrated empirical replay audit / remaining two-gate matrix."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalintegratedempiricalreplayaudit_or_remainingtwogates"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AUDIT = PACKET_DIR / "final_integrated_empirical_replay_audit.packet.json"
BLOCKERS = PACKET_DIR / "remaining_two_gate_sm_parity_matrix.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalIntegratedEmpiricalReplayAudit_or_RemainingTwoGates_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FINALINTEGRATEDEMPIRICALREPLAYAUDIT_OR_REMAININGTWOGATES_BUILT_AUDIT_EXECUTED_TWO_GATES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    audit = load(AUDIT)
    blockers = load(BLOCKERS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(audit["status"] == "FINAL_INTEGRATED_AUDIT_EXECUTED_NOT_CLOSED", "audit status mismatch")
    require(audit["audit_machinery_executed"] is True, "audit machinery not executed")
    require(audit["SM_parity_passed"] is False, "SM parity overclaimed")
    require(set(audit["blocks"]) == {
        "common_scale_Yukawa_and_Higgs_transport",
        "selected_SM_packet_certificate_integration",
    }, "audit blockers mismatch")
    for required_pass in [
        "measured_replay_admission_policy",
        "static_SM_slot_functor_source_arrows",
        "patched_dynamic_C1_interface",
        "MZ_gauge_triplet_common_scale",
        "central_value_tolerance_policy",
    ]:
        require(required_pass in audit["passes"], f"pass row missing: {required_pass}")
    require(audit["observed_data_used"] is False and audit["target_fitting_used"] is False, "audit guardrail violated")

    require(blockers["status"] == "SM_PARITY_REDUCED_TO_TWO_GATES", "blocker matrix status mismatch")
    require("final_integrated_empirical_replay_audit" in blockers["previous_SM_parity_blockers"], "previous audit blocker missing")
    require(set(blockers["current_SM_parity_blockers"]) == {
        "common_scale_Yukawa_and_Higgs_transport",
        "selected_SM_packet_certificate_integration",
    }, "current blocker matrix mismatch")
    require(blockers["closed_now"] == ["final_integrated_empirical_replay_audit"], "closed-now mismatch")
    require(blockers["full_covariance_profile_likelihood"] == "OPEN_FOR_PRECISION_TRUE_EQUIVALENCE_NOT_SM_PARITY_BLOCKER", "covariance guardrail mismatch")
    require(blockers["true_equivalence_and_no_knob_guardrail"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(blockers["true_equivalence_and_no_knob_guardrail"]["no_knob_closed"] is False, "no-knob overclaimed")

    for key in [
        "final_integrated_empirical_replay_audit_executed",
        "available_replay_tiers_passed",
        "SM_parity_blocker_matrix_reduced_to_two_gates",
        "full_covariance_kept_as_precision_true_equivalence_gate",
        "guardrails_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "common_scale_Yukawa_and_Higgs_transport",
        "selected_SM_packet_certificate_integration",
        "accepted_RG_transport_values",
        "QaSU3_color_operator_packet",
        "SM_parity_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "candidate guardrail violated")
    require("fails closure only on two remaining gates" in note, "note missing two-gate reduction")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
