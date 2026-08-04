"""Audit central-value tolerance policy execution / full covariance profile gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_centralvaluetolerancepolicyexecution_or_fullcovarianceprofile"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
POLICY = PACKET_DIR / "central_value_tolerance_execution.packet.json"
UPDATED = PACKET_DIR / "updated_sm_parity_blocker_matrix.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CentralValueTolerancePolicyExecution_or_FullCovarianceProfile_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_CENTRALVALUETOLERANCEPOLICYEXECUTION_OR_FULLCOVARIANCEPROFILE_BUILT_SM_PARITY_TIER_CLOSED"
NEXT_ARTIFACT = "MTT_Selected_AcceptedRGTransportValues_or_QaSU3SourcePacket_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    policy = load(POLICY)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")
    require(NEXT_ARTIFACT in note, "note missing next artifact")

    require(policy["status"] == "CENTRAL_VALUE_TOLERANCE_POLICY_EXECUTED_FOR_SM_PARITY_TIER", "policy status mismatch")
    require(policy["accepted_tiers_now"]["tier_0_central_replay"] is True, "tier 0 not closed")
    require(policy["accepted_tiers_now"]["tier_1_uncertainty_sidecar"] is True, "tier 1 not closed")
    require(policy["accepted_tiers_now"]["tier_2_profile_likelihood"] is False, "tier 2 overclaimed")
    require(policy["what_this_closes"]["covariance_profile_likelihood_or_tolerance_policy_execution_for_SM_parity"] is True, "SM parity tolerance not closed")
    require(policy["what_this_closes"]["full_covariance_profile_likelihood"] is False, "full covariance overclaimed")
    require(policy["guardrails"]["central_value_tier_not_precision_global_fit"] is True, "central tier guard missing")
    require(policy["guardrails"]["observed_values_downstream_only"] is True, "downstream guard missing")
    for row in ["gauge_MZ", "CKM", "PMNS", "charged_masses_native", "higgs_tree_native"]:
        require(policy["central_value_rows"][row]["central_tier_ready"] is True, f"central row not ready: {row}")

    require(updated["status"] == "SM_PARITY_BLOCKER_MATRIX_UPDATED_COVARIANCE_TOLERANCE_TIER_CLOSED", "updated matrix status mismatch")
    require("covariance_profile_likelihood_or_tolerance_policy_execution" in updated["previous_SM_parity_blockers"], "previous blocker missing")
    require("covariance_profile_likelihood_or_tolerance_policy_execution" not in updated["current_SM_parity_blockers"], "blocker not removed")
    require(set(updated["current_SM_parity_blockers"]) == {
        "common_scale_Yukawa_and_Higgs_transport",
        "final_integrated_empirical_replay_audit",
        "selected_SM_packet_certificate_integration",
    }, "current SM parity blockers mismatch")
    for key in ["PDG_CKM_global_fit", "NuFIT_PMNS_profile", "electroweak_fit_correlations"]:
        require(key in updated["still_open_for_precision_true_equivalence"], f"precision gate missing: {key}")

    for key in [
        "central_value_tolerance_policy_executed",
        "SM_parity_covariance_tolerance_blocker_closed",
        "uncertainty_sidecar_policy_attached",
        "full_covariance_profile_kept_open",
        "blocker_matrix_updated",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "common_scale_Yukawa_and_Higgs_transport",
        "final_integrated_empirical_replay_audit",
        "selected_SM_packet_certificate_integration",
        "accepted_RG_transport_values",
        "QaSU3_color_operator_packet",
        "full_covariance_profile_likelihood_for_precision_equivalence",
        "SM_parity_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key in ["patched_SM_parity_closed", "true_SM_equivalence_closed", "no_knob_closed"]:
        require(data["closure_decision"][key] is False, f"closure overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "guardrail violated")
    require("tier 2 profile likelihood      = open" in note, "note missing full covariance guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
