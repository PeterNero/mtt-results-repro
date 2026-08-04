"""Audit magnitude-bearing projection weights / threshold rows derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_magnitudebearingprojectionweights_or_thresholdrowsderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKSOLVE = PACKET_DIR / "diagnostic_magnitude_weight_backsolve.packet.json"
RANK_GAP = PACKET_DIR / "magnitude_weight_rank_gap.packet.json"
THRESHOLD = PACKET_DIR / "threshold_rows_derivation_attempt.packet.json"
SUPERSET = PACKET_DIR / "superset_search_targets_without_selection.packet.json"
DECISION = PACKET_DIR / "magnitude_weights_or_threshold_rows_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_magnitude_weight_backsolve.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_MagnitudeBearingProjectionWeights_or_ThresholdRowsDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_MAGNITUDEBEARINGPROJECTIONWEIGHTS_OR_THRESHOLDROWSDERIVATION_"
    "BUILT_DIAGNOSTIC_BACKSOLVE_RANK_GAP_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_GenerationResolvedThresholdSourceRows_or_ProfileConventionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    backsolve = load(BACKSOLVE)
    rank_gap = load(RANK_GAP)
    threshold = load(THRESHOLD)
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

    require(backsolve["status"] == "DIAGNOSTIC_MAGNITUDE_WEIGHTS_BACKSOLVED_NOT_SELECTED", "backsolve status mismatch")
    require(len(backsolve["diagnostic_weights"]) == 9, "wrong diagnostic row count")
    require(backsolve["accepted_as_selected_magnitude_weights"] is False, "diagnostic weights overaccepted")
    for row in backsolve["diagnostic_weights"]:
        require(row["source_normalized_weight"] == 1.0, f"source weight mismatch: {row}")
        require(row["used_as_selector"] is False, f"diagnostic row used as selector: {row}")
        require(row["diagnostic_magnitude_weight"] > 0, f"nonpositive diagnostic weight: {row}")
    require(backsolve["lambda_H_diagnostic_weight"] > 0, "lambda diagnostic missing")
    require(backsolve["closure_claimed"] is True, "backsolve should close locally")
    require(backsolve["observed_data_used_as_selector"] is False, "backsolve selector guard missing")
    require(backsolve["target_fitting_used"] is False, "backsolve target-fitting guard missing")

    require(rank_gap["status"] == "SOURCE_WEIGHT_RANK_INSUFFICIENT_FOR_MAGNITUDE_WEIGHTS", "rank-gap status mismatch")
    require(rank_gap["theorem"]["proved"] is True, "rank-gap theorem not proved")
    dims = rank_gap["dimension_evidence"]
    require(dims["source_column_count"] == 2, "source column count mismatch")
    require(dims["source_sector_slot_count"] == 4, "source slot count mismatch")
    require(dims["charged_generation_magnitude_rows"] == 9, "charged row count mismatch")
    require(dims["charged_plus_lambda_rows"] == 10, "lambda row count mismatch")
    require(dims["rank_gap_against_charged_rows"] == 7, "rank gap mismatch")
    require(dims["slot_gap_against_charged_rows"] == 5, "slot gap mismatch")
    hierarchy = rank_gap["hierarchy_evidence"]
    require(hierarchy["diag_abs_Y_u_ratio_max_min"] > 1000, "u hierarchy too small")
    require(hierarchy["diag_abs_Y_d_ratio_max_min"] > 100, "d hierarchy too small")
    require(hierarchy["diag_abs_Y_e_ratio_max_min"] > 100, "e hierarchy too small")
    require(rank_gap["closure_claimed"] is True, "rank-gap should close locally")

    require(
        threshold["status"] == "THRESHOLD_ROWS_DERIVATION_ATTEMPTED_NO_ACCEPTED_ROWS",
        "threshold status mismatch",
    )
    require(threshold["accepted_threshold_matching_source_rows"] == [], "threshold rows overfilled")
    require(threshold["accepted_mass_scheme_conversion_source_rows"] == [], "mass rows overfilled")
    require(threshold["residual_rows_finite"] is True, "finite residual support missing")
    for key in [
        "accepted_as_threshold_matching_values",
        "accepted_as_mass_scheme_conversion_values",
        "derivation_closed",
    ]:
        require(threshold[key] is False, f"threshold overclosed: {key}")
    require(threshold["closure_claimed"] is False, "threshold overclaimed")

    require(superset["status"] == "DIAGNOSTIC_TARGETS_AVAILABLE_FOR_DISCOVERY_ONLY", "superset status mismatch")
    require(superset["selected_next_lane"] == "internal_generation_resolved_threshold_rows", "wrong superset next lane")
    require("claim no-knob Yukawa closure from the backsolve" in superset["forbidden_use"], "superset guard missing")
    require(superset["closure_claimed"] is False, "superset overclaimed")

    require(decision["status"] == "DIAGNOSTIC_WEIGHTS_AND_RANK_GAP_CLOSED_SELECTED_ROWS_OPEN", "decision status mismatch")
    require(decision["source_normalized_sector_projection_weights_closed"] is True, "source weights missing")
    require(decision["diagnostic_magnitude_backsolve_emitted"] is True, "backsolve missing")
    require(decision["diagnostic_magnitude_backsolve_accepted_as_selection"] is False, "backsolve overaccepted")
    require(decision["rank_gap_theorem_proved"] is True, "rank gap missing")
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "generation_resolved_threshold_source_rows_closed",
        "same_branch_scale_scheme_loop_convention_closed",
        "mass_scheme_conversion_rows_closed",
        "profile_likelihood_or_diagonal_theorem_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["diagnostic_magnitude_weight_backsolve"] is True, "cutset backsolve missing")
    require(cutset["closed_now"]["rank_gap_theorem"] is True, "cutset rank gap missing")
    require(len(cutset["still_open"]) == 5, "cutset open count mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["diagnostic_magnitude_backsolve_emitted"] is True, "candidate final backsolve missing")
    require(final["rank_gap_theorem_proved"] is True, "candidate final rank gap missing")
    for key in [
        "magnitude_bearing_projection_weights_closed",
        "generation_resolved_threshold_source_rows_closed",
        "accepted_Yukawa_magnitudes_as_no_knob_predictions",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["diagnostic_magnitude_backsolve_emitted"] is True, "certificate backsolve missing")
    require(cert["diagnostic_magnitude_backsolve_accepted_as_selection"] is False, "certificate backsolve overaccepted")
    require(cert["rank_gap_theorem_proved"] is True, "certificate rank gap missing")
    require("diagnostic table accepted as selection    : false" in note, "note missing selector guard")
    require("rank gap theorem proved                   : true" in note, "note missing rank-gap line")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
