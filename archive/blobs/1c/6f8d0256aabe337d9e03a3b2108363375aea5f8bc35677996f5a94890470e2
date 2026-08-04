"""Audit BCT selected-source repair or full-profile upgrade artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_bctselectedsourcerepair_or_fullprofileupgrade"
STATUS = (
    "MTT_SELECTED_BCTSELECTEDSOURCEREPAIR_OR_FULLPROFILEUPGRADE_"
    "BUILT_PROFILE_UPGRADED_SOURCE_REPAIR_BLOCKED"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    source_repair = load(DATA / SLUG / "selected_source_repair_retest.packet.json")
    profile = load(DATA / SLUG / "external_profile_upgrade.packet.json")
    frontier = load(DATA / SLUG / "nonlooping_frontier_decision.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_bct_source_repair_or_profile_upgrade.packet.json")
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

    if source_repair.get("minimal_internal_missing_object") != "SelectedRouteCStromingerGalerkinResidualSolve":
        errors.append("wrong selected-source missing object")
    if source_repair.get("honest_root_all_pass") is not False:
        errors.append("honest root must still fail")
    if source_repair.get("formal_lift_lower_validators_all_pass") is not True:
        errors.append("formal lift diagnostics should still pass")
    if source_repair.get("selected_Rtheta_mass_scheme_derivation_closed") is not False:
        errors.append("selected Rtheta derivation must remain open")
    if source_repair.get("accepted_BCT_selected_source_row_count") != 0:
        errors.append("no selected BCT source rows should be promoted")
    if "Do not spend another artifact" not in source_repair.get("nonlooping_rule", ""):
        errors.append("nonlooping selected-source rule missing")

    if profile.get("accepted_BCT_external_map_row_count") != 3:
        errors.append("expected three BCT external rows")
    if profile.get("accepted_WZH_external_coordinate_row_count") != 5:
        errors.append("expected five WZH external coordinate rows")
    if profile.get("accepted_external_profile_coordinate_count") != 8:
        errors.append("expected eight external profile coordinates")
    if profile.get("BCT_empirical_profile_95pct_closure_closed") is not True:
        errors.append("BCT empirical 95 percent profile must be imported closed")
    if profile.get("BCT_source_or_no_knob_profile_closure_closed") is not False:
        errors.append("BCT source/no-knob profile must remain open")
    if profile.get("W_Z_H_electroweak_matching_rows_closed_at_external_coordinate_layer") is not True:
        errors.append("WZH external coordinate layer must be imported closed")
    if profile.get("full_covariance_profile_likelihood_closed") is not False:
        errors.append("full covariance profile must remain open")
    if profile.get("true_SM_equivalence_closed") is not False:
        errors.append("true SM equivalence must remain open")

    progress = frontier.get("new_progress_since_dual_lane", {})
    if progress.get("external_profile_coordinate_count") != 8:
        errors.append("frontier must record eight external profile coordinates")
    retire = frontier.get("retire_for_now", {})
    if retire.get("repeat_BCT_selected_source_repair_without_new_routec_payload") is not True:
        errors.append("frontier must retire repeated selected-source repair")
    live = frontier.get("live_frontier", {})
    for key in [
        "full_covariance_profile_likelihood",
        "published_or_reconstructed_profile_likelihood",
        "selected_Rtheta_source_rows",
        "SelectedRouteCStromingerGalerkinResidualSolve",
        "no_knob_value_source_derivation",
        "true_SM_equivalence",
    ]:
        if live.get(key) is not True:
            errors.append(f"live frontier missing {key}")

    closed = cutset.get("closed_now", {})
    for key in [
        "BCT_selected_source_repair_retested",
        "BCT_empirical_profile_95pct_closure_imported",
        "WZH_external_coordinate_layer_imported",
        "external_profile_coordinate_layer_upgraded",
        "nonlooping_frontier_guard_added",
    ]:
        if closed.get(key) is not True:
            errors.append(f"cutset did not close {key}")
    if cutset.get("recommended_next", {}).get("artifact") != (
        "MTT_Selected_ExternalProfileToFullCovarianceBridge_or_SelectedSourceRows_v1"
    ):
        errors.append("wrong next artifact")

    if errors:
        print("selected_bctselectedsourcerepair_or_fullprofileupgrade audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_bctselectedsourcerepair_or_fullprofileupgrade audit: PASS")
    print(f"status: {STATUS}")
    print(f"external_profile_coordinates: {profile['accepted_external_profile_coordinate_count']}")
    print(f"selected_bct_source_rows: {source_repair['accepted_BCT_selected_source_row_count']}")
    print(f"next: {cutset['recommended_next']['artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
