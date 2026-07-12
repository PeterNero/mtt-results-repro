"""Audit threshold/mass-scheme row readiness and precision-profile gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_thresholdmassschemerows_or_precisionprofileupgrade"
STATUS = (
    "MTT_SELECTED_THRESHOLDMASSSCHEMEROWS_OR_PRECISIONPROFILEUPGRADE_"
    "BUILT_ROW_READINESS_EXTERNAL_COORDINATES_ACCEPTED_SOURCE_ROWS_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    readiness = load(DATA / SLUG / "threshold_mass_scheme_row_readiness_matrix.packet.json")
    profile = load(DATA / SLUG / "precision_profile_upgrade_gate.packet.json")
    harness = load(DATA / SLUG / "rtheta1_validation_harness_row_attachment.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_threshold_row_readiness.packet.json")
    cert = load(CERTS / f"{SLUG}_certificate.json")

    errors: list[str] = []

    if candidate.get("status") != STATUS:
        errors.append("candidate status mismatch")
    if cert.get("status") != STATUS:
        errors.append("certificate status mismatch")
    if candidate.get("closure_claimed") is not False:
        errors.append("candidate must not claim full closure")
    if candidate.get("observed_data_used_as_selector") is not False:
        errors.append("observed data must not select")
    if candidate.get("target_fitting_used") is not False:
        errors.append("target fitting must remain false")

    if readiness.get("row_count") != 10:
        errors.append("expected 10 readiness rows")
    if readiness.get("accepted_external_coordinate_or_map_row_count") != 7:
        errors.append("expected 7 accepted external coordinate/map rows")
    if readiness.get("accepted_selected_Rtheta_source_row_count") != 0:
        errors.append("selected Rtheta source rows must remain zero")
    if readiness.get("accepted_full_profile_row_count") != 0:
        errors.append("full profile rows must remain zero")
    if readiness.get("sector_summary", {}).get("bct_finite_residual_rows") != 3:
        errors.append("expected 3 BCT finite residual rows")
    if readiness.get("sector_summary", {}).get("bct_accepted_map_rows") != 0:
        errors.append("BCT accepted map rows must remain zero")

    if profile.get("accepted_as_precision_profile_upgrade") is not False:
        errors.append("precision profile upgrade must remain open")
    if profile.get("wzh_interim_sidecars_present") is not True:
        errors.append("WZH interim sidecars should be present")
    if profile.get("weak_bct_crossblock_entries_present") is not True:
        errors.append("weak/BCT crossblock entries should be present")
    if profile.get("full_covariance_profile_likelihood_closed") is not False:
        errors.append("full covariance profile must remain open")

    if harness.get("provisional_Rtheta1_diagonal_instantiated") is not True:
        errors.append("provisional Rtheta1 must be attached")
    if harness.get("validates_external_top_higgs_rows") is not True:
        errors.append("top/Higgs validation attachment missing")
    if harness.get("validates_wzh_coordinate_rows") is not True:
        errors.append("WZH validation attachment missing")
    if harness.get("validates_bct_residual_inventory") is not True:
        errors.append("BCT residual validation attachment missing")
    if harness.get("selects_threshold_rows") is not False:
        errors.append("harness must not select threshold rows")
    if harness.get("threshold_response_rows_closed") is not False:
        errors.append("threshold response rows must remain open")
    if harness.get("mass_scheme_conversion_rows_closed") is not False:
        errors.append("mass-scheme rows must remain open")

    closed = cutset.get("closed_now", {})
    if closed.get("threshold_mass_scheme_row_readiness_matrix") is not True:
        errors.append("cutset must close row readiness")
    if closed.get("BCT_residual_rows_attached_as_validation_targets") is not True:
        errors.append("cutset must attach BCT residual rows")
    still_open = cutset.get("still_open", {})
    for key in [
        "BCT_formula_or_table_import",
        "selected_threshold_matching_source_rows",
        "selected_mass_scheme_conversion_source_rows",
        "selected_Rtheta_source_rows",
        "selected_threshold_response_functional",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_thresholdmassschemerows_or_precisionprofileupgrade audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_thresholdmassschemerows_or_precisionprofileupgrade audit: PASS")
    print(f"status: {STATUS}")
    print(f"readiness_rows: {readiness['row_count']}")
    print(f"accepted_external_rows: {readiness['accepted_external_coordinate_or_map_row_count']}")
    print(f"selected_source_rows: {readiness['accepted_selected_Rtheta_source_row_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
