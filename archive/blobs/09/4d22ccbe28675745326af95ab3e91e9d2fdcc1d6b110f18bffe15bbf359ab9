"""Audit threshold-response rows / sector projection weights execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
WEIGHTS = PACKET_DIR / "source_normalized_sector_projection_weights.packet.json"
FIRST_ROW = PACKET_DIR / "first_dynamic_row_repromotion.packet.json"
THRESHOLD = PACKET_DIR / "threshold_response_rows_recheck.packet.json"
DECISION = PACKET_DIR / "threshold_rows_or_projection_weights_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_source_projection_weights.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_THRESHOLDRESPONSEROWS_OR_SECTORPROJECTIONWEIGHTSEXECUTION_"
    "BUILT_SOURCE_WEIGHTS_CLOSED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_MagnitudeBearingProjectionWeights_or_ThresholdRowsDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    weights = load(WEIGHTS)
    first_row = load(FIRST_ROW)
    threshold = load(THRESHOLD)
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

    require(
        weights["status"] == "SOURCE_NORMALIZED_SECTOR_PROJECTION_WEIGHTS_SELECTED",
        "weights status mismatch",
    )
    require(weights["source_projection_weights_closed"] is True, "source weights not closed")
    require(weights["magnitude_bearing_projection_weights_closed"] is False, "magnitude weights overclosed")
    normal = weights["normal_form"]
    require(normal["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(normal["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(normal["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(normal["rank"] == 2, "rank mismatch")
    require(len(weights["sector_weights"]) == 4, "sector weight count mismatch")
    by_sector = {row["sector"]: row for row in weights["sector_weights"]}
    for sector in ["u", "e", "d", "nuD"]:
        require(by_sector[sector]["source_normalized_weight"] == 1.0, f"source weight mismatch: {sector}")
        require(by_sector[sector]["magnitude_bearing_weight"] is None, f"magnitude weight overfilled: {sector}")
    require(by_sector["u"]["source_column"] == "phase_Z", "u source column mismatch")
    require(by_sector["e"]["source_column"] == "phase_Z", "e source column mismatch")
    require(by_sector["d"]["source_column"] == "shift_X", "d source column mismatch")
    require(by_sector["nuD"]["source_column"] == "shift_X", "nuD source column mismatch")
    require(weights["closure_claimed"] is True, "weights should close locally")
    require(weights["observed_data_used_as_selector"] is False, "weights selector guard missing")
    require(weights["target_fitting_used"] is False, "weights target-fitting guard missing")

    require(
        first_row["status"] == "FIRST_DYNAMIC_ROW_REPROMOTED_AS_SOURCE_NORMALIZED_ROW",
        "first row status mismatch",
    )
    require(
        first_row["accepted_as_selected_source_normalized_projection_row_now"] is True,
        "first row not repromoted",
    )
    require(first_row["accepted_as_magnitude_or_threshold_source_row"] is False, "first row overpromoted")
    require(first_row["old_accepted_as_selected_dynamic_value_source_row"] is False, "old row unexpectedly accepted")
    require(first_row["closure_claimed"] is True, "first row should close locally")

    require(
        threshold["status"] == "THRESHOLD_AND_MASS_SCHEME_ROWS_STILL_OPEN_AFTER_SOURCE_WEIGHTS",
        "threshold status mismatch",
    )
    require(threshold["residual_rows_finite"] is True, "finite residual support missing")
    require(threshold["accepted_threshold_matching_source_rows"] == [], "threshold rows overfilled")
    require(threshold["accepted_mass_scheme_conversion_source_rows"] == [], "mass-scheme rows overfilled")
    for key in [
        "accepted_as_threshold_matching_values",
        "accepted_as_mass_scheme_conversion_values",
        "threshold_response_rows_closed",
        "mass_scheme_conversion_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
    ]:
        require(threshold[key] is False, f"threshold overclosed: {key}")
    require(threshold["closure_claimed"] is False, "threshold packet overclaimed")

    require(decision["status"] == "SOURCE_PROJECTION_WEIGHTS_CLOSED_THRESHOLD_RESPONSE_OPEN", "decision status mismatch")
    require(decision["source_owner_promoted"] is True, "source owner missing")
    require(decision["sector_aware_projection_skeleton_closed"] is True, "skeleton missing")
    require(decision["source_normalized_sector_projection_weights_closed"] is True, "source weights missing")
    require(decision["first_dynamic_row_repromoted_as_source_normalized"] is True, "first row missing")
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "selected_threshold_response_rows_closed",
        "mass_scheme_conversion_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "profile_likelihood_or_diagonal_theorem_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["source_normalized_sector_projection_weights"] is True, "cutset source weights missing")
    require(cutset["closed_now"]["first_dynamic_row_source_normalized_repromotion"] is True, "cutset first row missing")
    require(len(cutset["still_open"]) == 5, "cutset open count mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["source_normalized_sector_projection_weights_closed"] is True, "candidate final source weights missing")
    require(final["first_dynamic_row_repromoted_as_source_normalized"] is True, "candidate final first row missing")
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "selected_threshold_response_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["source_normalized_sector_projection_weights_closed"] is True, "certificate source weights missing")
    require(cert["magnitude_bearing_projection_weights_closed"] is False, "certificate magnitude weights overclosed")
    require("source projection weights closed      : true" in note, "note missing source weights")
    require("magnitude-bearing weights closed      : false" in note, "note missing magnitude guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
