"""Audit R_theta source-owner reconciliation and precision convention gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem"
STATUS = (
    "MTT_SELECTED_RTHETASOURCEOWNER_OR_PRECISIONTHRESHOLDCONVENTIONTHEOREM_"
    "CLOSED_SOURCE_OWNER_FIRSTPASS_VALUES_PRECISION_ROWS_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    source_owner = load(DATA / SLUG / "rtheta_source_owner_reconciliation.packet.json")
    coeff_update = load(DATA / SLUG / "coefficient_promotion_after_source_owner.packet.json")
    precision = load(DATA / SLUG / "precision_threshold_convention_obstruction.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_source_owner_reconciliation.packet.json")
    cert = load(CERTS / f"{SLUG}_certificate.json")

    errors: list[str] = []

    if candidate.get("status") != STATUS:
        errors.append("candidate status mismatch")
    if cert.get("status") != STATUS:
        errors.append("certificate status mismatch")
    if candidate.get("closure_claimed") is not False:
        errors.append("candidate must not claim full closure")
    if candidate.get("observed_data_used_as_selector") is not False:
        errors.append("observed values must not select")
    if candidate.get("target_fitting_used") is not False:
        errors.append("target fitting must remain false")

    if source_owner.get("selected_dynamic_operator_source_owner_closed") is not True:
        errors.append("source owner must be closed")
    if source_owner.get("Pi_Rtheta_closed") is not True:
        errors.append("Pi_Rtheta must be closed")
    if source_owner.get("coefficient_functional_domain_closed") is not True:
        errors.append("coefficient functional domain must be closed")
    if source_owner.get("firstpass_Rtheta_coefficient_values_present") is not True:
        errors.append("first-pass coefficient values must be present")
    if source_owner.get("firstpass_nonzero_coefficient_entries", 0) <= 0:
        errors.append("first-pass coefficient entries must be nonzero")

    if coeff_update.get("firstpass_Rtheta_coefficient_values_closed") is not True:
        errors.append("first-pass coefficient values must remain closed")
    if coeff_update.get("selected_dynamic_operator_source_owner_closed") is not True:
        errors.append("source owner must remain closed in coefficient update")
    if coeff_update.get("selected_Rtheta_coefficient_values_closed") is not False:
        errors.append("selected Rtheta coefficients must remain open")
    if coeff_update.get("selected_Rtheta_source_rows_closed") is not False:
        errors.append("selected Rtheta source rows must remain open")
    if "selected_dynamic_operator_source_owner" in coeff_update.get("remaining_blockers_after_source_owner_reconciliation", []):
        errors.append("source-owner blocker must be retired")

    if precision.get("target_identified") is not True:
        errors.append("precision target must be identified")
    if precision.get("selected_same_branch_source_closed") is not False:
        errors.append("same-branch precision source must remain open")
    if precision.get("accepted_precision_threshold_row_count") != 0:
        errors.append("precision threshold rows must remain zero")
    if precision.get("precision_convention_closed") is not False:
        errors.append("precision convention must remain open")
    if precision.get("threshold_matching_required", {}).get("top") is None:
        errors.append("top threshold requirement missing")
    if precision.get("mass_scheme_conversion_required", {}).get("direct_top_mass") is not True:
        errors.append("direct top mass conversion requirement missing")

    closed = cutset.get("closed_now", {})
    if closed.get("selected_dynamic_operator_source_owner") is not True:
        errors.append("cutset must close source owner")
    if closed.get("stale_source_owner_blocker_retired_from_promotion_audit") is not True:
        errors.append("cutset must retire stale source-owner blocker")
    still_open = cutset.get("still_open", {})
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "selected_Rtheta_coefficient_values",
        "selected_Rtheta_source_rows",
        "selected_threshold_response_functional",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_rtheta_sourceowner_or_precisionthresholdconventiontheorem audit: PASS")
    print(f"status: {STATUS}")
    print("source_owner_closed: true")
    print(f"firstpass_nonzero_coefficients: {source_owner['firstpass_nonzero_coefficient_entries']}")
    print(f"accepted_precision_threshold_row_count: {precision['accepted_precision_threshold_row_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
