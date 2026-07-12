"""Audit selected Pi_CKM finite branch-retention weight rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pickmnumeratorbranchretentionprinciple_or_weightrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRINCIPLE = PACKET_DIR / "finite_branch_retention_principle.packet.json"
ROWS = PACKET_DIR / "selected_pickm_weight_rows.packet.json"
POSTCHECK = PACKET_DIR / "ckm_postcheck_after_selected_pickm_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PiCKMNumeratorBranchRetentionPrinciple_or_WeightRows_v1.md"

STATUS = "MTT_SELECTED_PICKM_NUMERATOR_BRANCH_RETENTION_PROVED_WEIGHT_ROWS_EMITTED_EXACT_CKM_OPEN"
NEXT = "MTT_Selected_PiCKMWeightRows_CKMResidualDecision_or_HigherOrderClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    principle = load(PRINCIPLE)
    rows = load(ROWS)
    postcheck = load(POSTCHECK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["name"] == "PiCKMFiniteBranchRetentionTheorem", "theorem name mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    require(principle["status"] == "FINITE_BRANCH_RETENTION_PRINCIPLE_PROVED_FOR_PICKM", "principle status mismatch")
    require(principle["all_three_branch_retention_clauses_closed"] is True, "branch clauses not closed")
    require(principle["new_empirical_parameters_introduced"] == 0, "new empirical parameter introduced")
    require(principle["observed_data_used_as_selector"] is False, "principle used observed selector")
    require(principle["target_fitting_used"] is False, "principle target fitting")
    census = principle["branch_census"]
    require(census["Pi_CKM^12"]["retained_dynamic_branches"] == 5, "Pi12 branch count")
    require(census["Pi_CKM^23"]["retained_dynamic_branches"] == 3, "Pi23 branch count")
    require(census["Pi_CKM^13"]["retained_dynamic_branches"] == 5, "Pi13 q branch count")
    require(census["Pi_CKM^13"]["retained_modulus_pulls"] == 3, "Pi13 modulus pull count")
    require(close(census["Pi_CKM^13"]["modulus_pull_value"], 7.0), "Pi13 modulus value")
    for row_id, clause in census.items():
        require(clause["proved"] is True, f"{row_id} branch clause not proved")

    require(rows["status"] == "SELECTED_PICKM_WEIGHT_ROWS_EMITTED", "rows status mismatch")
    require(rows["selected_Pi_CKM_row_certificates"] == 3, "row certificate count")
    require(rows["accepted_weight_rows"] == 3, "accepted weight row count")
    require(rows["accepted_exact_ckm_correction_rows"] == 0, "exact CKM corrections overaccepted")
    require(rows["accepted_no_knob_ckm_angle_rows"] == 0, "no-knob CKM rows overaccepted")
    require(rows["observed_data_used_as_selector"] is False, "rows used observed selector")
    require(rows["target_fitting_used"] is False, "rows used target fitting")

    row_map = rows["rows"]
    require(close(row_map["Pi_CKM^12"]["value"], 1.4123293778994717), "W12 value")
    require(close(row_map["Pi_CKM^23"]["value"], 6.829942647321135), "W23 value")
    require(close(row_map["Pi_CKM^13"]["value"], 23.11111111111111), "W13 value")
    require(close(row_map["Pi_CKM^12"]["correction_factor"], 1.0031525209328114), "C12")
    require(close(row_map["Pi_CKM^23"]["correction_factor"], 1.0152454076949133), "C23")
    require(close(row_map["Pi_CKM^13"]["correction_factor"], 1.0515873015873016), "C13")
    for row_id, row in row_map.items():
        require(row["accepted_as_selected_weight_row"] is True, f"{row_id} not accepted")
        require(row["row_certificate"].startswith(row_id), f"{row_id} certificate label")

    require(postcheck["status"] == "SELECTED_PICKM_ROWS_PREDICT_NEAR_REPLAY_EXACT_CLOSURE_OPEN", "postcheck status")
    require(postcheck["accepted_weight_rows"] == 3, "postcheck accepted weights")
    require(postcheck["accepted_exact_ckm_correction_rows"] == 0, "postcheck exact corrections overaccepted")
    require(postcheck["accepted_no_knob_ckm_angle_rows"] == 0, "postcheck no-knob rows overaccepted")
    require(postcheck["exact_ckm_angle_magnitudes_closed"] is False, "postcheck overclosed CKM")
    require(postcheck["true_SM_equivalence_closed"] is False, "postcheck overclosed true SM")
    require(postcheck["observed_data_used_as_selector"] is False, "postcheck observed selector")
    require(postcheck["observed_data_used_for_postcheck"] is True, "postcheck flag missing")
    require(postcheck["target_fitting_used"] is False, "postcheck target fitting")
    require(postcheck["max_relative_angle_residual_against_frozen_replay"] < 7e-6, "postcheck angle residual too high")
    require(postcheck["max_relative_weight_residual_against_frozen_replay"] > 0, "postcheck residual should be nonzero")
    require(postcheck["max_relative_weight_residual_against_frozen_replay"] < 1.4e-4, "postcheck weight residual too high")
    for angle, gain in postcheck["orders_of_improvement_over_leading_map"].items():
        require(gain > 7000, f"{angle} improvement too small")

    closure = data["closure_decision"]
    require(closure["branch_retention_principle_proved"] is True, "closure branch principle")
    require(closure["Pi_CKM_numerator_projector_rule_closed"] is True, "closure numerator")
    require(closure["selected_Pi_CKM_row_certificates"] == 3, "closure row certs")
    require(closure["accepted_weight_rows"] == 3, "closure weights")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "closure exact corrections")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "closure no-knob CKM")
    require(closure["exact_ckm_angle_magnitudes_closed"] is False, "closure exact CKM overclaimed")
    require(closure["Jarlskog_source_derived_without_measured_angles"] is False, "closure Jarlskog overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "closure true SM overclaimed")
    require(closure["full_no_knob_closure_closed"] is False, "closure no-knob overclaimed")

    nums = data["key_numbers"]
    require(nums["accepted_eckm_weight_rows"] == 3, "key accepted rows")
    require(nums["max_relative_angle_residual_against_frozen_replay"] < 7e-6, "key angle residual")
    require(nums["max_relative_weight_residual_against_frozen_replay"] > 0, "key nonzero residual")
    require(data["closure_claimed"] is False, "candidate closure claimed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["observed_data_used_for_postcheck"] is True, "candidate postcheck flag")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(cert["branch_retention_principle_proved"] is True, "cert branch principle")
    require(cert["selected_Pi_CKM_row_certificates"] == 3, "cert row certs")
    require(cert["accepted_weight_rows"] == 3, "cert weights")
    require(cert["accepted_exact_ckm_correction_rows"] == 0, "cert exact corrections")
    require(cert["exact_ckm_angle_magnitudes_closed"] is False, "cert exact CKM")
    require(cert["closure_claimed"] is False, "cert closure")

    for phrase in [
        "Accepted selected Pi_CKM weight rows are now `3/3`",
        "This is not exact CKM magnitude closure",
        "max relative angle residual",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
