"""Audit external-profile to full-covariance bridge or selected-source rows."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_externalprofiletofullcovariancebridge_or_selectedsourcerows"
STATUS = (
    "MTT_SELECTED_EXTERNALPROFILETOFULLCOVARIANCEBRIDGE_OR_SELECTEDSOURCEROWS_"
    "BUILT_8X8_COVARIANCE_TARGET_SELECTED_ROWS_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    bridge = load(DATA / SLUG / "external_profile_full_covariance_bridge.packet.json")
    fork = load(DATA / SLUG / "selected_source_rows_fork.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_external_profile_bridge.packet.json")
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

    target = bridge.get("full_covariance_target", {})
    if target.get("coordinate_count") != 8:
        errors.append("full covariance target must have 8 coordinates")
    if target.get("matrix_shape") != [8, 8]:
        errors.append("full covariance matrix shape must be 8x8")
    if target.get("symmetric_unique_entries") != 36:
        errors.append("8x8 symmetric matrix should have 36 unique entries")
    if target.get("hard_missing_entries_for_published_or_reconstructed_likelihood") != 15:
        errors.append("BCT-WZH cross block should have 15 missing entries")
    if target.get("strict_full_profile_entries_accepted") != 0:
        errors.append("strict full profile entries should not be accepted yet")
    if target.get("surrogate_or_empirical_entries_scaffolded") != 21:
        errors.append("expected 21 surrogate/empirical scaffold entries")

    blocks = bridge.get("external_coordinate_blocks", {})
    if blocks.get("BCT_empirical_block", {}).get("coordinate_count") != 3:
        errors.append("BCT block must have 3 coordinates")
    if blocks.get("BCT_empirical_block", {}).get("profile_95pct_closed") is not True:
        errors.append("BCT empirical profile should be closed")
    if blocks.get("WZH_weak_scale_block", {}).get("coordinate_count") != 5:
        errors.append("WZH block must have 5 coordinates")
    if blocks.get("WZH_weak_scale_block", {}).get("surrogate_matrix_available") is not True:
        errors.append("WZH surrogate matrix should be available")
    if blocks.get("WZH_weak_scale_block", {}).get("published_or_reconstructed_likelihood_available") is not False:
        errors.append("published/reconstructed likelihood must remain absent")
    if blocks.get("BCT_cross_WZH_block", {}).get("cross_covariance_entries") != 15:
        errors.append("BCT-WZH cross block must have 15 entries")

    gate = bridge.get("promotion_gate", {})
    for key in [
        "published_or_reconstructed_profile_likelihood_imported",
        "threshold_matching_values_emitted",
        "mass_scheme_conversion_values_emitted",
        "multi_loop_threshold_convention_values_emitted",
        "no_knob_MTT_source_derivation_of_values",
    ]:
        if gate.get(key) is not False:
            errors.append(f"{key} must remain false")
    if bridge.get("full_covariance_profile_likelihood_closed") is not False:
        errors.append("full covariance profile must remain open")

    if fork.get("minimal_internal_missing_object") != "SelectedRouteCStromingerGalerkinResidualSolve":
        errors.append("wrong source fork missing object")
    if fork.get("accepted_selected_BCT_source_row_count") != 0:
        errors.append("selected BCT source rows must remain zero")
    if fork.get("honest_root_all_pass") is not False:
        errors.append("honest root must still fail")
    if "surrogate covariance matrix as published likelihood" not in fork.get("must_not_promote", []):
        errors.append("must-not-promote guard missing")

    closed = cutset.get("closed_now", {})
    for key in [
        "external_profile_coordinate_count_fixed",
        "full_8x8_covariance_target_shape_fixed",
        "BCT_WZH_cross_covariance_gap_quantified",
        "selected_source_rows_fork_guarded",
    ]:
        if closed.get(key) is not True:
            errors.append(f"cutset did not close {key}")
    if cutset.get("recommended_next", {}).get("artifact") != (
        "MTT_Selected_PublishedCovarianceLikelihoodImport_or_RouteCSelectedSourceEmission_v1"
    ):
        errors.append("wrong next artifact")
    if cutset.get("still_open", {}).get("true_SM_equivalence") is not True:
        errors.append("true SM equivalence must remain open")

    if errors:
        print("selected_externalprofiletofullcovariancebridge_or_selectedsourcerows audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_externalprofiletofullcovariancebridge_or_selectedsourcerows audit: PASS")
    print(f"status: {STATUS}")
    print(f"covariance_shape: {target['matrix_shape']}")
    print(f"symmetric_entries: {target['symmetric_unique_entries']}")
    print(f"missing_cross_entries: {target['hard_missing_entries_for_published_or_reconstructed_likelihood']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
