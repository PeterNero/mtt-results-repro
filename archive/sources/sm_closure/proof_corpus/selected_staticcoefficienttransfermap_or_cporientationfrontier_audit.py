"""Audit selected static coefficient transfer map / CP frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_staticcoefficienttransfermap_or_cporientationfrontier"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
TRANSFER = PACKET_DIR / "selected_static_coefficient_transfer_map.packet.json"
BRANCHES = PACKET_DIR / "static_branch_promotion_decision.packet.json"
CP_FRONTIER = PACKET_DIR / "cp_orientation_frontier_after_static_transfer.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_static_coefficient_transfer.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StaticCoefficientTransferMap_or_CPOrientationFrontier_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_staticcoefficienttransfermap_or_cporientationfrontier.py"

STATUS = "MTT_SELECTED_STATIC_COEFFICIENT_TRANSFER_MAP_BUILT_MIXED_REJECTED_CP_ORIENTATION_FRONTIER_OPEN"
NEXT = "MTT_Selected_CPOrientation_or_DynamicPhysicalMatrixPromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    transfer = load(TRANSFER)
    branches = load(BRANCHES)
    cp_frontier = load(CP_FRONTIER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("transfer", transfer),
        ("branches", branches),
        ("cp_frontier", cp_frontier),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    evidence = transfer["source_evidence"]
    require(evidence["active_shift_selected"] is True, "active shift not selected")
    require(evidence["selected_active_shift"] == [1, 1], "active shift mismatch")
    require(evidence["conditional_routec_transfer_exact"] is True, "conditional routec transfer not exact")
    require(evidence["all_six_smslot_arrows_closed"] is True, "SM-slot arrows not closed")
    require(evidence["selected_same_source_consistency_map"] is True, "same-source consistency missing")
    require(evidence["selected_static_sector_route_now_closed"] is True, "static sector route missing")
    require(evidence["selected_static_phase_route"] == ["u", "e"], "phase route mismatch")
    require(evidence["selected_static_shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(evidence["selected_static_overlap_transfer_normalization"] is True, "static normalization missing")
    require(evidence["static_readout_status"] == "STATIC_SOURCE_TIER_READOUT_CLOSED", "readout status mismatch")
    require(evidence["dynamic_C1_promoted"] is False, "dynamic C1 overpromoted")

    require(
        transfer["status"] == "SELECTED_STATIC_COEFFICIENT_TRANSFER_MAP_EMITTED",
        "transfer status mismatch",
    )
    require(
        transfer["selected_static_coefficient_transfer_map_emitted"] is True,
        "selected static transfer not emitted",
    )
    require(transfer["rule"]["lambda_Z_equals_lambda_X"] is True, "lambda equality not enforced")
    require(transfer["mixed_branches_rejected_at_static_tier"] is True, "mixed branches not rejected")
    require(
        transfer["selected_specific_lambda_value_emitted"] is False,
        "specific lambda overemitted",
    )
    require(transfer["selected_dynamic_C1_transfer_promoted"] is False, "dynamic C1 overpromoted")
    require(transfer["selected_physical_matrices_promoted"] is False, "physical matrices overpromoted")

    require(
        branches["status"] == "FOUR_BRANCHES_REDUCED_TO_TWO_SELECTED_STATIC_COMPATIBLE_BRANCHES",
        "branch decision status mismatch",
    )
    require(branches["branch_count_before"] == 4, "branch count mismatch")
    require(branches["selected_static_compatible_count"] == 2, "compatible count mismatch")
    require(branches["rejected_mixed_count"] == 2, "rejected count mismatch")
    require(
        branches["selected_static_compatible_branch_ids"]
        == [
            "phase_lambda_1+omega__shift_lambda_1+omega",
            "phase_lambda_1+omega2__shift_lambda_1+omega2",
        ],
        "compatible branch ids mismatch",
    )
    require(
        branches["rejected_mixed_branch_ids"]
        == [
            "phase_lambda_1+omega__shift_lambda_1+omega2",
            "phase_lambda_1+omega2__shift_lambda_1+omega",
        ],
        "rejected branch ids mismatch",
    )
    require(branches["surviving_lambdas"] == ["1+omega", "1+omega2"], "surviving lambdas mismatch")
    require(branches["surviving_cp_odd_orientations"] == ["positive"], "surviving CP orientation mismatch")
    require(
        all(row["lambda_Z_equals_lambda_X"] is row["selected_static_coefficient_compatible"] for row in branches["branch_rows"]),
        "branch row compatibility mismatch",
    )

    require(
        cp_frontier["status"] == "STATIC_INVARIANT_CP_SIGN_FIXED_CONJUGATE_LAMBDA_AND_PHYSICAL_CP_OPEN",
        "CP frontier status mismatch",
    )
    require(
        cp_frontier["static_commutator_cp_orientation_sign_fixed"] is True,
        "static CP sign not fixed after rejection",
    )
    require(
        cp_frontier["surviving_cp_odd_orientations_in_current_finite_weyl_convention"] == ["positive"],
        "CP frontier orientation mismatch",
    )
    require(cp_frontier["selected_physical_CKM_or_PMNS_CP_orientation_emitted"] is False, "physical CP overemitted")
    require(
        cp_frontier["selected_complex_orientation_or_universe_branch_rule_emitted"] is False,
        "complex branch rule overemitted",
    )

    closed = candidate["what_closes_now"]
    require(closed["selected_static_coefficient_transfer_map"] is True, "static transfer not closed")
    require(closed["mixed_coefficient_branches_rejected_at_static_tier"] is True, "mixed rejection missing")
    require(closed["static_branch_count_reduced_four_to_two"] is True, "branch reduction missing")
    require(
        closed["static_finite_weyl_CP_sign_after_mixed_rejection_fixed_positive"] is True,
        "static CP sign closure missing",
    )

    remaining = candidate["what_remains_open"]
    for key in [
        "conjugate_lambda_branch_selection_or_coexistence",
        "selected_complex_orientation_or_time_arrow_rule",
        "selected_dynamic_C1_or_Aselected_matrix_promotion",
        "selected_b_selected_and_Hessian_normalization",
        "physical_CKM_PMNS_Yukawa_value_closure",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["mixed_branches_rejected"] is True, "mixed rejection decision missing")
    require(decision["selected_specific_lambda_value_emitted"] is False, "lambda value overemitted")
    require(decision["selected_physical_matrices_promoted"] is False, "physical matrices overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("lambda_Z = lambda_X = lambda_static" in note, "note missing transfer map")
    require("rejected mixed branch count         : 2" in note, "note missing rejected count")
    require("selected physical matrices promoted : false" in note, "note missing physical guard")
    require("full SM closure                     : false" in note, "note missing closure guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
