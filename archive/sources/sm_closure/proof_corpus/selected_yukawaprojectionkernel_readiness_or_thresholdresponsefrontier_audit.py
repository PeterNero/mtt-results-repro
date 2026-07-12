"""Audit Yukawa projection-kernel readiness / threshold-response frontier gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_OWNER = PACKET_DIR / "updated_source_owner_readiness.packet.json"
SKELETON = PACKET_DIR / "sector_aware_projection_kernel_skeleton.packet.json"
FRONTIER = PACKET_DIR / "threshold_response_frontier_contraction.packet.json"
SUPERSET = PACKET_DIR / "superset_strategy_execution_matrix.packet.json"
DECISION = PACKET_DIR / "yukawa_projection_kernel_readiness_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_projection_readiness.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_YukawaProjectionKernelReadiness_or_ThresholdResponseFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_YUKAWAPROJECTIONKERNEL_READINESS_OR_THRESHOLDRESPONSEFRONTIER_"
    "BUILT_SOURCE_OWNER_PROMOTED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source_owner = load(SOURCE_OWNER)
    skeleton = load(SKELETON)
    frontier = load(FRONTIER)
    superset = load(SUPERSET)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(source_owner["status"] == "SOURCE_OWNER_AND_FIRST_RESPONSE_ROWS_PROMOTED", "source-owner status mismatch")
    require(source_owner["previous_audit_present_count"] == 1, "previous readiness count mismatch")
    require(source_owner["present_count"] == 3, "updated readiness count mismatch")
    require(source_owner["requirement_count"] == 7, "requirement count mismatch")
    for key in [
        "selected_dynamic_operator_source_owner",
        "finite_normalization_transport_same_branch",
        "sector_response_source_rows",
    ]:
        require(source_owner["closed_now"][key] is True, f"source-owner closure missing: {key}")
    require(
        source_owner["still_open"]
        == [
            "same_branch_scale_scheme_loop_convention",
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
            "full_profile_likelihood_or_accepted_diagonal_theorem",
        ],
        "source-owner frontier did not contract as expected",
    )
    require(source_owner["closure_claimed"] is True, "source-owner packet should close locally")

    require(
        skeleton["status"] == "SECTOR_AWARE_PROJECTION_SKELETON_EMITTED_WEIGHTS_OPEN",
        "skeleton status mismatch",
    )
    require(skeleton["skeleton_closed"] is True, "skeleton not closed")
    require(skeleton["full_projection_kernel_closed"] is False, "full kernel overclosed")
    require(skeleton["accepted_Yukawa_magnitudes_as_no_knob_predictions"] is False, "magnitudes overclosed")
    require(len(skeleton["sector_slots"]) == 4, "sector slot count mismatch")
    slots = {row["sector"]: row for row in skeleton["sector_slots"]}
    require(slots["u"]["source_direction"] == "phase_packet_I_plus_Z", "u source direction mismatch")
    require(slots["e"]["source_direction"] == "phase_packet_I_plus_Z", "e source direction mismatch")
    require(slots["d"]["source_direction"] == "shift_packet_I_plus_X", "d source direction mismatch")
    require(slots["nuD"]["source_direction"] == "shift_packet_I_plus_X", "nuD source direction mismatch")
    for row in skeleton["sector_slots"]:
        require(row["accepted_magnitude_source"] == "open", f"slot magnitude overclosed: {row['sector']}")
    require(skeleton["observed_data_used_as_selector"] is False, "skeleton selector guard missing")
    require(skeleton["target_fitting_used"] is False, "skeleton target-fitting guard missing")

    require(
        frontier["status"] == "FRONTIER_CONTRACTED_FROM_SOURCE_OWNER_TO_THRESHOLD_RESPONSE_ROWS",
        "frontier status mismatch",
    )
    require("selected_dynamic_operator_source_owner" in frontier["retired_blockers"], "source-owner blocker not retired")
    require(
        frontier["remaining_blockers"]
        == [
            "same_branch_scale_scheme_loop_convention",
            "threshold_matching_source_rows",
            "mass_scheme_conversion_source_rows",
            "full_profile_likelihood_or_accepted_diagonal_theorem",
        ],
        "frontier remaining blockers mismatch",
    )
    require(frontier["rtheta_projection_state"]["Pi_Rtheta_closed"] is False, "Pi_Rtheta overclosed")
    require(frontier["value_profile_state"]["accepted_common_scale_values_for_true_precision"] is False, "precision overaccepted")
    require(frontier["closure_claimed"] is False, "frontier overclaimed")

    require(superset["status"] == "SUPERSET_STRATEGY_LOCKED_TO_COMPLEMENTARY_ROWS", "superset status mismatch")
    require(superset["selected_next_lane"] == "lane_A_internal_selected_projection", "wrong selected superset lane")
    require(len(superset["lanes"]) == 3, "superset lane count mismatch")
    require(superset["observed_data_used_as_selector"] is False, "superset selector guard missing")
    require(superset["target_fitting_used"] is False, "superset target-fitting guard missing")

    require(decision["status"] == "SOURCE_OWNER_AND_SKELETON_CLOSED_FULL_KERNEL_OPEN", "decision status mismatch")
    require(decision["updated_readiness_present_count"] == 3, "decision readiness count mismatch")
    require(decision["source_owner_promoted"] is True, "decision source owner not promoted")
    require(decision["sector_aware_projection_skeleton_closed"] is True, "decision skeleton not closed")
    for key in [
        "selected_projection_weights_closed",
        "selected_threshold_response_rows_closed",
        "mass_scheme_conversion_rows_closed",
        "profile_likelihood_or_diagonal_theorem_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["source_owner_promoted"] is True, "cutset source owner missing")
    require(cutset["closed_now"]["sector_aware_projection_skeleton"] is True, "cutset skeleton missing")
    require(len(cutset["still_open"]) == 5, "cutset open count mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["source_owner_promoted"] is True, "candidate final source owner missing")
    require(final["sector_aware_projection_skeleton_closed"] is True, "candidate final skeleton missing")
    for key in [
        "full_projection_kernel_closed",
        "selected_threshold_response_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["source_owner_promoted"] is True, "certificate source owner missing")
    require(cert["updated_readiness_present_count"] == 3, "certificate readiness count mismatch")
    require(cert["full_projection_kernel_closed"] is False, "certificate full kernel overclosed")
    require("readiness rows present             : 3/7" in note, "note missing readiness contraction")
    require("full projection kernel closed      : false" in note, "note missing kernel guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
