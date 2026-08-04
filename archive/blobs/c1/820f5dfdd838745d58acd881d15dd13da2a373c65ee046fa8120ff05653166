"""Audit Step 44 alpha1 universal source-anchor admission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ANCHOR = PACKET_DIR / "step44_alpha1_source_anchor_admission.packet.json"
FRONTIER = PACKET_DIR / "step44_rtheta_row_execution_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step44_Alpha1UniversalAnchorAdmission_or_RThetaRowExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP44_ALPHA1_UNIVERSAL_SOURCE_ANCHOR_ADMITTED_RTHETA_ROW_EXECUTION_OPEN"
NEXT = "MTT_Selected_RThetaRowsFromAlpha1Anchor_or_InternalCoefficientRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    anchor = load(ANCHOR)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "anchor admission theorem not proved")

    for packet in [data, anchor, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(anchor["status"] == "ALPHA1_ADMITTED_AS_ONE_UNIVERSAL_SOURCE_ANCHOR_FOR_OPERATOR_BRANCH", "anchor status mismatch")
    require(anchor["admitted_at_source_tier"] is True, "anchor not admitted")
    require(anchor["admitted_as_value_closure_anchor"] is False, "anchor overpromoted to value closure")
    alpha = anchor["anchor"]
    require(alpha["parameter_count"] == 1, "anchor count mismatch")
    require(alpha["lambda_alpha1"] == 1.0, "lambda_alpha1 mismatch")
    require(alpha["N_alpha1_h_ext"] == 1.0, "N_alpha1 mismatch")
    require(alpha["du_dalpha1_equals_h_ext"] is True, "du/dalpha mismatch")
    require(alpha["selected_dotD_source_verified"] is True, "dotD source missing")
    require(alpha["alpha1_driver_verified"] is True, "alpha1 driver missing")
    require(alpha["honest_dotD_alpha1_replay"] is True, "honest dotD replay missing")
    require(alpha["tangent_residual_l2"] == 0.0, "tangent residual not zero")
    for key, value in anchor["admission_checks"].items():
        require(value is True, f"admission check failed: {key}")

    readiness = frontier["readiness_after_step44"]
    require(readiness["one_anchor_source_tier_admitted"] is True, "frontier anchor missing")
    require(readiness["one_anchor_lane_readiness"] == "5/6", "readiness mismatch")
    require(readiness["selected_value_anchor_count"] == 0, "value anchor overselected")
    require(readiness["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(readiness["accepted_Rtheta_coefficient_value_count"] == 0, "coefficient rows overaccepted")
    require(frontier["remaining_single_missing_gate"]["name"] == "RthetaRowsFromAlpha1AnchorExecution", "missing gate mismatch")
    require(frontier["next_required_payload"] == NEXT, "frontier next mismatch")
    for key, value in frontier["still_open"].items():
        require(value is False, f"frontier overclosed: {key}")

    decision = data["closure_decision"]
    require(decision["alpha1_one_universal_source_anchor_admitted_at_source_tier"] is True, "decision anchor missing")
    require(decision["one_anchor_lane_readiness"] == "5/6", "decision readiness mismatch")
    require(decision["selected_universal_source_anchor_count_at_source_tier"] == 1, "source anchor count mismatch")
    require(decision["selected_value_anchor_count"] == 0, "value anchor count mismatch")
    require(decision["effective_fitted_parameter_count"] == 0, "fitted parameter count mismatch")
    require(decision["accepted_internal_scalar_row_count"] == 0, "decision scalar rows overaccepted")
    require(decision["accepted_Rtheta_coefficient_value_count"] == 0, "decision coefficient rows overaccepted")
    for key in [
        "Rtheta_rows_from_alpha1_anchor_executed",
        "selected_internal_Rtheta_coefficient_rows_closed",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "alpha1_source_strength_anchor",
        "lambda_alpha1 = 1",
        "5/6",
        NEXT,
        "without observed values selecting the map",
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
