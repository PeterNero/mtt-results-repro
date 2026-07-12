"""Audit BCT formula import and selected threshold-row derivation lanes."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_bctformulaimport_or_selectedthresholdrowderivation"
STATUS = (
    "MTT_SELECTED_BCTFORMULAIMPORT_OR_SELECTEDTHRESHOLDROWDERIVATION_"
    "BUILT_EXTERNAL_BCT_ROWS_ACCEPTED_SELECTED_DERIVATION_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    external = load(DATA / SLUG / "bct_external_formula_import_lane.packet.json")
    same_source = load(DATA / SLUG / "bct_selected_rtheta_derivation_lane.packet.json")
    updated = load(DATA / SLUG / "updated_threshold_readiness_after_bct_import.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_bct_dual_lane_attempt.packet.json")
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

    if external.get("accepted_external_bct_map_row_count") != 3:
        errors.append("expected 3 accepted external BCT map rows")
    if external.get("accepted_selected_Rtheta_source_row_count") != 0:
        errors.append("BCT selected Rtheta source rows must remain zero")
    if external.get("all_three_bct_external_mass_scheme_rows_available") is not True:
        errors.append("all BCT external rows should be available")
    for row_id in [
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
    ]:
        if row_id not in external.get("row_ids", []):
            errors.append(f"missing external BCT row {row_id}")

    if same_source.get("selected_Rtheta_mass_scheme_derivation_closed") is not False:
        errors.append("selected Rtheta mass-scheme derivation must remain open")
    if same_source.get("selected_routec_galerkin_solve_closed") is not False:
        errors.append("selected Route-C Galerkin solve must remain open")
    if same_source.get("honest_root_all_pass") is not False:
        errors.append("honest root should still fail")
    if same_source.get("formal_lift_lower_validators_all_pass") is not True:
        errors.append("formal lift lower validators should pass")
    if same_source.get("minimal_internal_missing_object") != "SelectedRouteCStromingerGalerkinResidualSolve":
        errors.append("wrong minimal missing object")
    if not same_source.get("failed_honest_root_slots"):
        errors.append("failed honest root slots must be listed")

    if updated.get("accepted_BCT_external_map_row_count") != 3:
        errors.append("updated readiness must include 3 BCT external rows")
    if updated.get("accepted_BCT_selected_source_row_count") != 0:
        errors.append("updated readiness must include 0 selected BCT source rows")
    if updated.get("BCT_residual_targets_replaced_by_external_map_rows") is not True:
        errors.append("BCT residual targets should be replaced by external map rows")
    if updated.get("rtheta1_harness_can_validate_all_BCT_external_rows") is not True:
        errors.append("Rtheta1 harness should validate BCT external rows")
    if updated.get("rtheta1_harness_selects_BCT_rows") is not False:
        errors.append("Rtheta1 harness must not select BCT rows")

    closed = cutset.get("closed_now", {})
    if closed.get("BCT_external_formula_or_table_import") is not True:
        errors.append("cutset must close external BCT import")
    if closed.get("selected_Rtheta_derivation_lane_tested") is not True:
        errors.append("same-source lane must be tested")
    still_open = cutset.get("still_open", {})
    for key in [
        "SelectedRouteCStromingerGalerkinResidualSolve",
        "selected_BCT_Rtheta_mass_scheme_derivation",
        "selected_BCT_source_rows",
        "BCT_profile_95pct_closure",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        if still_open.get(key) is not True:
            errors.append(f"{key} must remain open")

    if errors:
        print("selected_bctformulaimport_or_selectedthresholdrowderivation audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_bctformulaimport_or_selectedthresholdrowderivation audit: PASS")
    print(f"status: {STATUS}")
    print(f"accepted_external_bct_rows: {external['accepted_external_bct_map_row_count']}")
    print(f"selected_bct_source_rows: {external['accepted_selected_Rtheta_source_row_count']}")
    print(f"failed_honest_root_slots: {len(same_source['failed_honest_root_slots'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
