"""Audit CKM residual profile-admission / higher-order closure reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CKM_PROFILE = PACKET_DIR / "ckm_diagonal_profile_admission.packet.json"
HIGHER_ORDER = PACKET_DIR / "higher_order_residual_row_decision.packet.json"
DECISION = PACKET_DIR / "post_ckm_profile_remaining_rows_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_CKMCovarianceProfileOrHigherOrderResidualClosure_or_PMNSHiggsPEWRows_v1.md"
)

STATUS = (
    "MTT_SELECTED_CKMCOVARIANCEPROFILEORHIGHERORDERRESIDUALCLOSURE_OR_PMNSHIGGSPEWROWS_"
    "BUILT_CKM_DIAGONAL_PROFILE_ADMITTED_FULLCOV_PMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_PMNSRunningMassRows_or_HiggsThresholdStrictPEWExit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    profile = load(CKM_PROFILE)
    higher = load(HIGHER_ORDER)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")
    require(data["observed_data_used_for_postcheck"] is True, "candidate postcheck")

    require(
        profile["status"] == "CKM_RESIDUAL_ADMITTED_BY_CURRENT_DIAGONAL_PROFILE_FULL_COVARIANCE_OPEN",
        "profile status",
    )
    require(profile["observed_data_used_as_selector"] is False, "profile observed selector")
    require(profile["target_fitting_used"] is False, "profile target fitting")
    require(profile["observed_data_used_for_postcheck"] is True, "profile postcheck")
    require(profile["ckm_diagonal_profile_degrees_of_freedom"] == 3, "CKM dof")
    require(profile["admission_threshold_sigma"] == 1.0, "threshold")
    require(profile["max_abs_sigma_score_no_covariance"] < 0.001, "sigma score too high")
    require(profile["chi2_ckm_diagonal"] < 1e-6, "chi2 too high")
    require(profile["ckm_residual_admitted_by_current_diagonal_profile"] is True, "not admitted")
    require(profile["full_ckm_fit_covariance_encoded"] is False, "covariance overencoded")
    require(profile["full_covariance_ready"] is False, "full covariance ready unexpectedly")
    require(profile["full_covariance_profile_likelihood_closed"] is False, "full covariance overclosed")
    require("not encoded yet" in profile["why_not_full_covariance"], "missing covariance guard")

    require(
        higher["status"] == "HIGHER_ORDER_RESIDUAL_ROW_NOT_REQUIRED_FOR_CURRENT_DIAGONAL_ADMISSION",
        "higher status",
    )
    require(higher["observed_data_used_as_selector"] is False, "higher observed selector")
    require(higher["target_fitting_used"] is False, "higher target fitting")
    require(higher["accepted_residual_correction_rows"] == 0, "higher rows overaccepted")
    require(higher["higher_order_residual_rows_required_for_exact_frozen_central_replay"] is True, "central replay")
    require(
        higher["higher_order_residual_rows_required_for_current_diagonal_profile_admission"] is False,
        "profile admission should not need higher-order rows",
    )
    require(higher["exact_central_ckm_closure"] is False, "exact CKM overclosed")
    require(higher["current_diagonal_ckm_profile_admission_closed"] is True, "profile not closed")

    require(
        decision["status"] == "CKM_RESIDUAL_PROFILE_ADMITTED_PMNS_RUNNING_HIGGS_PEW_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 3, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_selected_Pi_CKM_weight_rows"] == 3, "Pi rows")
    require(counts["accepted_exact_ckm_correction_rows"] == 0, "exact CKM rows")
    require(counts["accepted_no_knob_CKM_angle_rows"] == 0, "no-knob CKM rows")
    require(counts["accepted_ckm_diagonal_profile_admission_rows"] == 3, "profile rows")
    require(counts["PMNS_angle_phase_rows"] == 0, "PMNS rows")
    require(counts["running_mass_ratio_rows"] == 0, "running rows")
    acceptance = decision["acceptance"]
    require(acceptance["ckm_Pi_weight_rows_closed"] is True, "accept Pi")
    require(acceptance["ckm_diagonal_profile_admission_closed"] is True, "accept profile")
    require(acceptance["ckm_exact_central_residual_closed"] is False, "central overclosed")
    require(acceptance["ckm_full_covariance_profile_closed"] is False, "covariance overclosed")
    require(
        acceptance["higher_order_residual_rows_required_for_current_profile_tier"] is False,
        "higher-order requirement",
    )
    require(acceptance["PMNS_rows_closed"] is False, "PMNS overclosed")
    require(acceptance["running_mass_ratio_rows_closed"] is False, "running overclosed")
    require(acceptance["higgs_threshold_rows_closed"] is False, "Higgs overclosed")
    require(acceptance["strict_PEW_directK_values_closed"] is False, "PEW overclosed")
    require(acceptance["fullS2_no_proxy_rows_closed"] is False, "fullS2 overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(
        data["theorem"]["name"] == "CKMDiagonalProfileAdmissionAfterSelectedPiCKMRowsTheorem",
        "theorem",
    )
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_selected_Pi_CKM_weight_rows"] == 3, "key Pi")
    require(key["accepted_ckm_diagonal_profile_admission_rows"] == 3, "key profile")
    require(key["max_abs_sigma_score_no_covariance"] < 0.001, "key sigma")
    require(key["accepted_exact_ckm_correction_rows"] == 0, "key exact")
    require(key["PMNS_angle_phase_rows"] == 0, "key PMNS")
    require(key["running_mass_ratio_rows"] == 0, "key running")

    require(cert["ckm_Pi_weight_rows_closed"] is True, "cert Pi")
    require(cert["ckm_diagonal_profile_admission_closed"] is True, "cert profile")
    require(cert["accepted_ckm_diagonal_profile_admission_rows"] == 3, "cert rows")
    require(cert["ckm_exact_central_residual_closed"] is False, "cert central")
    require(cert["ckm_full_covariance_profile_closed"] is False, "cert covariance")
    require(cert["PMNS_rows_closed"] is False, "cert PMNS")
    require(cert["running_mass_ratio_rows_closed"] is False, "cert running")
    require(cert["higgs_threshold_rows_closed"] is False, "cert Higgs")
    require(cert["strict_PEW_directK_values_closed"] is False, "cert PEW")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "diagonal CKM admission rows: `3/3`",
        "exact central CKM equality: open",
        "full CKM covariance/profile likelihood: open",
        "PMNS rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
