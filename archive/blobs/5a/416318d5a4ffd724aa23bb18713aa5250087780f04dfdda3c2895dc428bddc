"""Audit Weyl coefficient source branch-filter reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_weylcoefficientsource_reduction_or_orientationtransfermap"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
FILTER = PACKET_DIR / "same_active_shift_orientation_branch_filter.packet.json"
GAP = PACKET_DIR / "coefficient_transfer_map_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_orientation_branch_filter.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_WeylCoefficientSource_Reduction_or_OrientationTransferMap_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_weylcoefficientsource_reduction_or_orientationtransfermap.py"

STATUS = "MTT_SELECTED_WEYLCOEFFICIENT_SOURCE_REDUCTION_BUILT_TWO_BRANCH_FILTER_TRANSFER_OPEN"
NEXT = "MTT_Selected_CoefficientTransferMap_or_CPOrientationSelection_v1"


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
    branch_filter = load(FILTER)
    gap = load(GAP)
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
        ("filter", branch_filter),
        ("gap", gap),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    static = branch_filter["static_source_evidence"]
    require(static["active_shift_selected"] is True, "active shift not selected")
    require(static["selected_active_shift"] == [1, 1], "active shift mismatch")
    require(static["source_level_weyl_carrier_proved"] is True, "source Weyl carrier missing")
    require(static["active_shift_1_1_provenance"] is True, "active shift provenance missing")
    require(static["static_matter_slot_readout_closed"] is True, "static matter readout missing")
    require(static["phase_route_static"] == ["u", "e"], "phase route mismatch")
    require(static["shift_route_static"] == ["d", "nuD"], "shift route mismatch")
    require(static["dynamic_transfer_map_emitted"] is False, "dynamic transfer overemitted")

    require(
        branch_filter["status"]
        == "FOUR_ALGEBRAIC_BRANCHES_REDUCED_TO_TWO_SAME_ORIENTATION_BRANCHES_CONDITIONALLY",
        "filter status mismatch",
    )
    require(branch_filter["algebraic_branch_count"] == 4, "algebraic branch count mismatch")
    require(branch_filter["same_active_shift_compatible_count"] == 2, "compatible count mismatch")
    require(branch_filter["mixed_orientation_count"] == 2, "mixed count mismatch")
    require(branch_filter["compatible_lambdas"] == ["1+omega", "1+omega2"], "compatible lambdas mismatch")
    require(branch_filter["compatible_cp_orientations"] == ["positive"], "compatible orientation mismatch")
    require(len(branch_filter["compatible_branch_ids"]) == 2, "compatible branch ids mismatch")
    require(len(branch_filter["mixed_branch_ids"]) == 2, "mixed branch ids mismatch")
    require(branch_filter["mixed_branches_rejected_as_selected_now"] is False, "mixed branches overrejected")
    require("transfer map is still open" in branch_filter["why_not_rejected_absolutely"], "open transfer caveat missing")

    require(gap["status"] == "SOURCE_BRANCH_FILTER_BUILT_TRANSFER_MAP_AND_ORIENTATION_OPEN", "gap status mismatch")
    require(gap["selected_lambda_emitted_now"] is False, "lambda overemitted")
    require(gap["selected_CP_orientation_emitted_now"] is False, "CP orientation overemitted")
    require(gap["physical_values_promoted_now"] is False, "physical values overpromoted")
    require("selected source-to-C1 coefficient transfer map" in gap["what_remains_open"], "transfer map gap missing")
    require("CP orientation selection or coexistence theorem" in gap["what_remains_open"], "orientation gap missing")

    closed = candidate["what_closes_now"]
    require(closed["active_shift_imported_into_coefficient_lift"] is True, "active shift not imported")
    require(closed["static_phase_shift_readout_imported"] is True, "readout not imported")
    require(closed["same_orientation_branch_filter_built"] is True, "filter not built")
    require(
        closed["natural_branch_count_reduced_four_to_two_conditionally"] is True,
        "branch count not conditionally reduced",
    )

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_coefficient_transfer_map",
        "absolute_rejection_of_mixed_orientation_branches",
        "CP_orientation_selection_or_coexistence",
        "selected_physical_matrix_promotion",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["same_orientation_filter_closed"] is True, "filter decision missing")
    require(decision["selected_lambda_emitted"] is False, "lambda overemitted")
    require(decision["selected_CP_orientation_emitted"] is False, "CP orientation overemitted")
    require(decision["physical_values_promoted"] is False, "physical values overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("same-active-shift compatible        : 2" in note, "note missing compatible count")
    require("mixed-orientation branches          : 2" in note, "note missing mixed count")
    require("selected lambda emitted             : false" in note, "note missing lambda guard")
    require("selected CP orientation emitted     : false" in note, "note missing CP guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
