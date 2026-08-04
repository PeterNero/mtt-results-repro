"""Audit threshold-row attempt / diagonal profile limitation theorem."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_thresholdrows_or_diagonalprofilelimitationtheorem"
STATUS = (
    "MTT_SELECTED_THRESHOLDROWS_OR_DIAGONALPROFILELIMITATIONTHEOREM_"
    "BUILT_PROVISIONAL_RTHETA1_DIAGONAL_TRUE_PRECISION_ROWS_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    limitation = load(DATA / SLUG / "firstpass_diagonal_profile_limitation_theorem.packet.json")
    rtheta1 = load(DATA / SLUG / "provisional_rtheta1_diagonal_instantiation.packet.json")
    rows = load(DATA / SLUG / "threshold_rows_after_diagonal_limitation.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_diagonal_limitation.packet.json")
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

    if limitation.get("closed_as_firstpass_diagonal_limitation") is not True:
        errors.append("first-pass diagonal limitation must be closed")
    if limitation.get("accepted_as_full_profile_likelihood") is not False:
        errors.append("full profile likelihood must remain open")
    if limitation.get("accepted_as_true_precision_equivalence") is not False:
        errors.append("true precision equivalence must remain open")
    if limitation.get("accepted_domain", {}).get("nonzero_coefficient_entries", 0) <= 0:
        errors.append("limitation must include nonzero coefficients")

    if rtheta1.get("provisional_firstpass_Rtheta_instantiated") is not True:
        errors.append("provisional Rtheta1 must be instantiated")
    if rtheta1.get("selected_threshold_response_functional_instantiated") is not False:
        errors.append("selected threshold response functional must remain open")
    if rtheta1.get("selected_Rtheta_source_rows_closed") is not False:
        errors.append("selected Rtheta source rows must remain open")
    if rtheta1.get("true_precision_profile_instantiated") is not False:
        errors.append("true precision profile must remain open")
    if rtheta1.get("source_owner_closed") is not True:
        errors.append("source owner should be closed")

    if rows.get("threshold_matching_source_row_count") != 0:
        errors.append("threshold matching source row count must remain zero")
    if rows.get("mass_scheme_conversion_source_row_count") != 0:
        errors.append("mass-scheme source row count must remain zero")
    if rows.get("precision_threshold_row_count") != 0:
        errors.append("precision threshold row count must remain zero")
    if rows.get("provisional_firstpass_evaluator_selects_future_rows") is not False:
        errors.append("provisional evaluator must not select future rows")

    closed = cutset.get("closed_now", {})
    if closed.get("firstpass_diagonal_profile_limitation_theorem") is not True:
        errors.append("cutset must close diagonal limitation theorem")
    if closed.get("provisional_Rtheta1_diagonal_instantiation") is not True:
        errors.append("cutset must close provisional Rtheta1")
    still_open = cutset.get("still_open", {})
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "selected_Rtheta_coefficient_values",
        "selected_Rtheta_source_rows",
        "selected_threshold_response_functional",
        "full_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_thresholdrows_or_diagonalprofilelimitationtheorem audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_thresholdrows_or_diagonalprofilelimitationtheorem audit: PASS")
    print(f"status: {STATUS}")
    print("provisional_Rtheta1_diagonal_instantiated: true")
    print(f"threshold_matching_source_row_count: {rows['threshold_matching_source_row_count']}")
    print(f"mass_scheme_conversion_source_row_count: {rows['mass_scheme_conversion_source_row_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
