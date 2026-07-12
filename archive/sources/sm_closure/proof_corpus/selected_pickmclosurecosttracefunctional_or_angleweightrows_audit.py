"""Audit the Pi_CKM trace-law candidate and its non-promotion boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pickmclosurecosttracefunctional_or_angleweightrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_LAW = PACKET_DIR / "pickm_source_trace_law_candidate.packet.json"
PREDICTION = PACKET_DIR / "ckm_angle_prediction_from_trace_law_candidate.packet.json"
ACCEPTANCE = PACKET_DIR / "pickm_trace_law_acceptance_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1.md"

STATUS = "MTT_SELECTED_PICKM_TRACE_LAW_CANDIDATE_BUILT_SOURCE_DERIVATION_OPEN"
NEXT = "MTT_Selected_PiCKMSourceDerivationClauses_or_CKMPredictionUpgrade_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    trace_law = load(TRACE_LAW)
    prediction = load(PREDICTION)
    acceptance = load(ACCEPTANCE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "PiCKMTraceLawCandidateTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    require(trace_law["status"] == "PICKM_SOURCE_TRACE_LAW_CANDIDATE_BUILT_NOT_PROMOTED", "trace law status")
    require(trace_law["candidate_emits_three_numeric_weights"] is True, "candidate numeric rows")
    require(trace_law["accepted_as_selected_row_certificates"] is False, "trace law overpromoted")
    require(trace_law["accepted_weight_rows"] == 0, "trace law accepted weights")
    require(trace_law["diagnostic_postcheck_scan_used_for_discovery"] is True, "scan provenance")
    require(trace_law["target_fitting_used_to_accept_rows"] is False, "accepted by fitting")
    rows = trace_law["rows"]
    require(close(rows["Pi_CKM^12"]["value"], 1.4123293778994717), "W12 candidate")
    require(close(rows["Pi_CKM^23"]["value"], 6.829942647321135), "W23 candidate")
    require(close(rows["Pi_CKM^13"]["value"], 23.11111111111111), "W13 candidate")
    for row_id in ["Pi_CKM^12", "Pi_CKM^23", "Pi_CKM^13"]:
        require(rows[row_id]["derivation_clause_closed"] is False, f"{row_id} derivation overclosed")

    require(prediction["status"] == "CKM_ANGLE_PREDICTION_FROM_TRACE_LAW_CANDIDATE_EXECUTED", "prediction status")
    require(prediction["accepted_as_exact_ckm_closure"] is False, "prediction overclosed")
    require(prediction["max_relative_residual_against_frozen_replay"] < 7e-6, "prediction not strong")
    for angle in ["s12", "s23", "s13"]:
        require(prediction["orders_of_improvement_over_leading_map"][angle] > 1000, f"{angle} improvement")

    require(acceptance["status"] == "PICKM_TRACE_LAW_SOURCE_DERIVATION_CLAUSES_OPEN", "acceptance status")
    require(acceptance["candidate_is_numerically_strong"] is True, "candidate strength")
    require(acceptance["candidate_source_only_when_evaluated"] is True, "source-only evaluation")
    require(acceptance["candidate_selected_by_diagnostic_postcheck_scan"] is True, "diagnostic discovery")
    require(acceptance["accepted_weight_rows"] == 0, "acceptance weights")
    require(acceptance["accepted_exact_ckm_correction_rows"] == 0, "acceptance corrections")
    require(acceptance["accepted_no_knob_ckm_angle_rows"] == 0, "acceptance CKM rows")
    require(len(acceptance["remaining_derivation_clauses"]) == 3, "derivation clauses")
    require(acceptance["next_required_artifact"] == NEXT, "acceptance next")

    closure = data["closure_decision"]
    require(closure["Pi_CKM_trace_law_candidate_built"] is True, "closure candidate")
    require(closure["candidate_emits_three_numeric_weights"] is True, "closure numeric")
    require(closure["selected_Pi_CKM_row_certificates"] == 0, "closure Pi certs")
    require(closure["accepted_weight_rows"] == 0, "closure weights")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "closure corrections")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "closure CKM rows")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaim")
    require(closure["full_no_knob_closure_closed"] is False, "no-knob overclaim")

    nums = data["key_numbers"]
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted")
    require(nums["remaining_derivation_clauses"] == 3, "key clauses")
    require(nums["max_relative_residual_against_frozen_replay"] < 7e-6, "key residual")
    require(data["closure_claimed"] is False, "closure claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["diagnostic_postcheck_scan_used_for_discovery"] is True, "candidate discovery")
    require(data["target_fitting_used_to_accept_rows"] is False, "target fit acceptance")
    require(cert["Pi_CKM_trace_law_candidate_built"] is True, "cert candidate")
    require(cert["selected_Pi_CKM_row_certificates"] == 0, "cert Pi certs")
    require(cert["closure_claimed"] is False, "cert closure")
    require("accepted W rows = 0/3" in note, "note weights")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
