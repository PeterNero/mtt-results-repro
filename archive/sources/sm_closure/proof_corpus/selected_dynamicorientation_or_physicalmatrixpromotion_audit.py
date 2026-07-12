"""Audit dynamic orientation / physical matrix promotion reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicorientation_or_physicalmatrixpromotion"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
DYNAMIC_SEARCH = PACKET_DIR / "dynamic_orientation_selector_search.packet.json"
PROMOTION_BOUNDARY = PACKET_DIR / "physical_matrix_promotion_boundary.packet.json"
VALUE_ALIGNMENT = PACKET_DIR / "value_frontier_alignment_after_lambda_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_orientation_reconciliation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicOrientation_or_PhysicalMatrixPromotion_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicorientation_or_physicalmatrixpromotion.py"

STATUS = "MTT_SELECTED_DYNAMICORIENTATION_OR_PHYSICALMATRIXPROMOTION_BUILT_FIRST_RESPONSE_RECONCILED_LAMBDA_REPRESENTATIVE_OPEN"
NEXT = "MTT_Selected_SecondOrderDynamicCoefficientEmission_or_LambdaRepresentativeSelection_v1"


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
    dynamic_search = load(DYNAMIC_SEARCH)
    promotion_boundary = load(PROMOTION_BOUNDARY)
    value_alignment = load(VALUE_ALIGNMENT)
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
        ("dynamic_search", dynamic_search),
        ("promotion_boundary", promotion_boundary),
        ("value_alignment", value_alignment),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(
        dynamic_search["status"]
        == "NO_DYNAMIC_LAMBDA_REPRESENTATIVE_SELECTOR_IN_CURRENT_FIRST_RESPONSE_PACKETS",
        "dynamic search status mismatch",
    )
    require(dynamic_search["static_lambda_orbit"] == ["1+omega", "1+omega2"], "lambda orbit mismatch")
    require(dynamic_search["dynamic_first_response_closed"] is True, "dynamic first response not closed")
    require(
        dynamic_search["dynamic_lambda_representative_selector_found"] is False,
        "dynamic selector unexpectedly found",
    )
    for payload_name, hits in dynamic_search["selector_hits"].items():
        require(all(value is False for value in hits.values()), f"selector hit in {payload_name}: {hits}")

    require(
        promotion_boundary["status"]
        == "FIRST_RESPONSE_DYNAMIC_PROMOTION_DOES_NOT_PROMOTE_SECOND_ORDER_LAMBDA_MATRICES",
        "promotion boundary status mismatch",
    )
    require(promotion_boundary["static_lambda_orbit_selected"] is True, "static orbit not selected")
    require(promotion_boundary["dynamic_first_response_layer_closed"] is True, "dynamic first response missing")
    require(
        promotion_boundary["second_order_lambda_coefficient_matrices_present_in_dynamic_packets"] is False,
        "second-order matrices unexpectedly present",
    )
    require(
        promotion_boundary["selected_second_order_physical_matrices_promoted"] is False,
        "second-order physical matrices overpromoted",
    )
    require(promotion_boundary["individual_lambda_value_selected"] is False, "lambda representative overselected")
    require(
        promotion_boundary["physical_coexistence_or_equivalence_proved"] is False,
        "coexistence/equivalence overclaimed",
    )

    require(
        value_alignment["status"]
        == "VALUE_FRONTIER_ALIGNED_LAMBDA_REPRESENTATIVE_AND_ACCEPTED_VALUES_OPEN",
        "value alignment status mismatch",
    )
    require(
        value_alignment["VSD01_legacy_dynamic_absence_blocker_retired"] is True,
        "VSD01 legacy blocker not retired",
    )
    require(value_alignment["VSD01_full_obligation_closed"] is False, "VSD01 full obligation overclosed")
    require(value_alignment["accepted_Yukawa_magnitudes_closed"] is False, "Yukawa magnitudes overclosed")
    require(value_alignment["CKM_PMNS_measured_value_closure"] is False, "CKM/PMNS overclosed")
    require(value_alignment["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(value_alignment["full_SM_no_knob_closed"] is False, "no-knob overclosed")

    closed = candidate["what_closes_now"]
    require(
        closed["dynamic_first_response_reconciled_with_static_lambda_orbit"] is True,
        "reconciliation missing",
    )
    require(
        closed["old_VSD01_dynamic_absence_track_retired_for_this_frontier"] is True,
        "old VSD01 track not retired",
    )
    require(
        closed["no_current_dynamic_lambda_representative_selector_found"] is True,
        "no-selector result missing",
    )
    require(
        closed["second_order_lambda_physical_promotion_boundary_built"] is True,
        "promotion boundary missing",
    )

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_second_order_dynamic_coefficient_emission",
        "individual_lambda_representative_selection_or_coexistence",
        "selected_second_order_physical_matrix_promotion",
        "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["dynamic_first_response_layer_closed"] is True, "dynamic closure not recorded")
    require(decision["individual_lambda_value_selected"] is False, "individual lambda overselected")
    require(
        decision["selected_second_order_physical_matrices_promoted"] is False,
        "second-order matrices overpromoted",
    )
    require(decision["accepted_value_layer_closed"] is False, "accepted value layer overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("dynamic lambda selector found       : false" in note, "note missing selector guard")
    require("second-order physical matrices promoted : false" in note, "note missing matrix guard")
    require("full SM closure                     : false" in note, "note missing closure guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
