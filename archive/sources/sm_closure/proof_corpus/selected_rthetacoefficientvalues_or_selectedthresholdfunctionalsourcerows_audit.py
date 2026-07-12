"""Audit first-pass R_theta coefficients and selected source-row gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows"
STATUS = (
    "MTT_SELECTED_RTHETACOEFFICIENTVALUES_OR_SELECTEDTHRESHOLDFUNCTIONALSOURCEROWS_"
    "BUILT_FIRSTPASS_COEFFICIENTS_SELECTED_SOURCE_ROWS_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    coeffs = load(DATA / SLUG / "firstpass_rtheta_coefficient_values.packet.json")
    composed = load(DATA / SLUG / "firstpass_composed_bct_to_mt_response.packet.json")
    promotion = load(DATA / SLUG / "selected_rtheta_source_row_promotion_audit.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_rtheta_coefficient_values.packet.json")
    cert = load(CERTS / f"{SLUG}_certificate.json")

    errors: list[str] = []

    if candidate.get("status") != STATUS:
        errors.append("candidate status mismatch")
    if cert.get("status") != STATUS:
        errors.append("certificate status mismatch")
    if candidate.get("closure_claimed") is not False:
        errors.append("candidate must not claim full closure")
    if candidate.get("observed_data_used_as_selector") is not False:
        errors.append("observed values must not be selectors")
    if candidate.get("target_fitting_used") is not False:
        errors.append("target fitting must remain false")

    if coeffs.get("accepted_as_firstpass_Rtheta_coefficient_values") is not True:
        errors.append("first-pass Rtheta coefficients must be accepted")
    if coeffs.get("accepted_as_selected_Rtheta_coefficient_values") is not False:
        errors.append("selected Rtheta coefficients must remain open")
    if coeffs.get("accepted_as_selected_threshold_response_functional") is not False:
        errors.append("selected threshold functional must remain open")
    if coeffs.get("total_dense_coefficient_entries") != 82:
        errors.append("expected 82 dense coefficient entries")
    if coeffs.get("total_nonzero_coefficient_entries", 0) <= 0:
        errors.append("expected nonzero coefficient entries")
    if coeffs.get("inverse_residual_max_abs", 1.0) >= 1e-8:
        errors.append("inverse residual is too large")

    blocks = coeffs.get("coefficient_blocks", {})
    for name in [
        "RG_Mt_to_MZ_forward",
        "RG_MZ_to_Mt_inverse",
        "BCT_mass_to_MZ_yukawa",
        "composed_BCT_to_Mt_native",
    ]:
        if name not in blocks:
            errors.append(f"missing coefficient block {name}")
    if composed.get("accepted_as_firstpass_response_values") is not True:
        errors.append("composed BCT-to-Mt response must be accepted at first-pass tier")
    if composed.get("accepted_as_selected_threshold_response_covariance") is not False:
        errors.append("selected threshold response covariance must remain open")
    if composed.get("inserted_crossblock_entry_count") != 8:
        errors.append("expected 8 imported cross-block entries")

    if promotion.get("firstpass_Rtheta_coefficient_values_closed") is not True:
        errors.append("promotion audit must close first-pass coefficient values")
    if promotion.get("selected_Rtheta_source_rows_closed") is not False:
        errors.append("selected Rtheta source rows must remain open")
    if promotion.get("selected_Rtheta_coefficient_values_closed") is not False:
        errors.append("selected Rtheta coefficient values must remain open")
    if promotion.get("promoted_selected_Rtheta_source_row_count") != 0:
        errors.append("no selected source rows should be promoted")
    if not promotion.get("promotion_blockers"):
        errors.append("promotion blockers must be listed")

    closed = cutset.get("closed_now", {})
    if closed.get("firstpass_Rtheta_coefficient_values") is not True:
        errors.append("cutset must close first-pass coefficient values")
    if closed.get("firstpass_composed_BCT_to_Mt_response") is not True:
        errors.append("cutset must close composed BCT-to-Mt response")
    still_open = cutset.get("still_open", {})
    for key in [
        "selected_dynamic_operator_source_owner",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "selected_Rtheta_coefficient_values",
        "selected_threshold_response_functional",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_rthetacoefficientvalues_or_selectedthresholdfunctionalsourcerows audit: PASS")
    print(f"status: {STATUS}")
    print(f"dense_coefficient_entries: {coeffs['total_dense_coefficient_entries']}")
    print(f"nonzero_coefficient_entries: {coeffs['total_nonzero_coefficient_entries']}")
    print(f"promoted_selected_source_rows: {promotion['promoted_selected_Rtheta_source_row_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
