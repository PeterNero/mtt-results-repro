"""Audit Delta_v to CKM angle-magnitude map execution."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_deltav_to_ckm_anglemagnitudemap_or_honestflavorobservableexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEADING_MAP = PACKET_DIR / "leading_sqrt_flavor_angle_map.packet.json"
CKM_MATRIX = PACKET_DIR / "ckm_matrix_from_leading_map.packet.json"
CORRECTION = PACKET_DIR / "correction_functional_obligation.packet.json"
DECISION = PACKET_DIR / "angle_map_source_acceptance_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DeltaV_to_CKM_AngleMagnitudeMap_or_HonestFlavorObservableExecution_v1.md"

STATUS = "MTT_SELECTED_DELTAV_TO_CKM_ANGLEMAP_LEADING_POLICY_MAP_EXECUTED_CORRECTION_OPEN"
NEXT = "MTT_Selected_CKMAngleCorrectionFunctional_or_ExactFlavorObservableClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    leading = load(LEADING_MAP)
    matrix = load(CKM_MATRIX)
    correction = load(CORRECTION)
    decision_packet = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    closure = data["closure_decision"]
    require(closure["A_CKM_leading_candidate_executed"] is True, "leading candidate missing")
    require(closure["leading_policy_tier_angle_rows_emitted"] == 3, "leading row count")
    require(closure["leading_CKM_matrix_executed"] is True, "matrix not executed")
    require(closure["correction_functional_obligation_identified"] is True, "correction not identified")
    require(closure["accepted_exact_CKM_angle_rows"] == 0, "exact rows overaccepted")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob rows overaccepted")
    for key in [
        "CKM_angle_magnitudes_derived_exact",
        "Jarlskog_source_derived_without_measured_angles",
        "Yukawa_rows_derived_strict",
        "PMNS_orientation_source_values_derived",
        "true_SM_equivalence_closed",
        "full_no_knob_closure_closed",
    ]:
        require(closure[key] is False, f"overclaim: {key}")

    require(leading["status"] == "LEADING_POLICY_TIER_MAP_EXECUTED_NOT_EXACT", "leading status")
    require(leading["map_name"] == "A_CKM^0", "map name")
    require(leading["accepted_as_exact_A_CKM"] is False, "exact map overaccepted")
    require(leading["accepted_as_leading_policy_tier_map"] is True, "leading map not accepted")
    require(leading["observed_data_used_as_selector"] is False, "observed selector used")
    require(leading["target_fitting_used"] is False, "target fitting used")
    preds = leading["predicted_angles"]
    require(abs(preds["s12"] - 0.22430286152357248) < 1e-15, "s12 prediction")
    require(abs(preds["s23"] - 0.04119198745939121) < 1e-15, "s23 prediction")
    require(abs(preds["s13"] - 0.003548908297206734) < 1e-15, "s13 prediction")
    require(leading["residuals_against_measured_replay"]["s13"]["relative_residual"] > 0.04, "s13 residual should block exact closure")

    require(matrix["status"] == "LEADING_CKM_MATRIX_EXECUTED_POSTCHECK_ONLY", "matrix status")
    require(matrix["unitarity_max_residual"] < 1e-12, "matrix not unitary")
    require(abs(matrix["jarlskog"] - 2.856816219576763e-05) < 1e-18, "J prediction")
    require(abs(matrix["jarlskog_relative_residual"] - 0.08308025116477681) < 1e-12, "J residual")

    require(correction["status"] == "CORRECTION_FUNCTIONAL_REQUIRED_FOR_EXACT_ANGLE_CLOSURE", "correction status")
    require(correction["leading_map_residual_summary"]["max_relative_angle_residual"] > 0.04, "max residual")
    require("multiplicative corrections backsolved from measured CKM angles" in correction["forbidden_as_source"], "forbidden correction missing")

    require(decision_packet["status"] == "LEADING_POLICY_MAP_ACCEPTED_EXACT_SOURCE_MAP_REJECTED", "decision status")
    require(decision_packet["leading_policy_tier_angle_rows_emitted"] == 3, "decision row count")
    require(decision_packet["accepted_exact_CKM_angle_rows"] == 0, "decision exact rows")
    require(decision_packet["A_CKM_exact_source_map_closed"] is False, "decision exact closure")
    require(decision_packet["next_required_artifact"] == NEXT, "decision next")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["observed_data_used_for_postcheck"] is True, "postcheck flag missing")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["accepted_exact_CKM_angle_rows"] == 0, "cert exact rows")
    require("Accepted exact CKM angle rows: `0`" in note, "note boundary")
    require(NEXT in note, "note next")
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
