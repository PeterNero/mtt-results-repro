"""Audit published covariance likelihood import or Route-C selected-source emission."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission"
STATUS = (
    "MTT_SELECTED_PUBLISHEDCOVARIANCELIKELIHOODIMPORT_OR_ROUTECSELECTEDSOURCEEMISSION_"
    "BUILT_EXTERNAL_REPLAY_CLOSED_TRUE_EQ_SOURCE_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    likelihood = load(DATA / SLUG / "published_covariance_likelihood_import_attempt.packet.json")
    routec = load(DATA / SLUG / "routec_selected_source_emission_attempt.packet.json")
    replay = load(DATA / SLUG / "external_profile_replay_closure_under_declared_standard.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_likelihood_or_source_attempt.packet.json")
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

    if likelihood.get("published_or_reconstructed_profile_likelihood_imported") is not False:
        errors.append("published 8x8 likelihood should remain absent")
    if likelihood.get("accepted_as_full_profile_likelihood") is not False:
        errors.append("full profile likelihood must not be accepted")
    if likelihood.get("accepted_for_true_SM_equivalence") is not False:
        errors.append("likelihood import must not close true equivalence")
    if likelihood.get("fixed_target_shape") != [8, 8]:
        errors.append("likelihood target should be fixed at 8x8")
    if likelihood.get("fixed_target_symmetric_entries") != 36:
        errors.append("likelihood target should have 36 symmetric entries")
    if likelihood.get("missing_BCT_WZH_cross_covariance_entries") != 15:
        errors.append("missing cross block should be 15")

    if routec.get("minimal_internal_missing_object") != "SelectedRouteCStromingerGalerkinResidualSolve":
        errors.append("wrong Route-C missing object")
    if routec.get("accepted_selected_BCT_source_row_count") != 0:
        errors.append("Route-C should promote zero BCT source rows")
    if routec.get("honest_root_all_pass") is not False:
        errors.append("honest root must still fail")
    if routec.get("selected_routec_galerkin_solve_closed") is not False:
        errors.append("selected Route-C solve must remain open")
    if routec.get("selected_Rtheta_source_rows_closed") is not False:
        errors.append("selected Rtheta source rows must remain open")

    if replay.get("external_profile_coordinate_count") != 8:
        errors.append("external replay must admit 8 coordinates")
    if replay.get("external_profile_replay_closed_under_declared_standard") is not True:
        errors.append("external replay tier should close")
    if replay.get("SM_parity_closed") is not True:
        errors.append("SM parity should remain closed")
    if replay.get("BCT_empirical_profile_95pct_closure_imported") is not True:
        errors.append("BCT empirical profile must be imported")
    if replay.get("WZH_external_coordinate_layer_imported") is not True:
        errors.append("WZH external layer must be imported")
    if replay.get("full_covariance_profile_required_for_declared_replay") is not False:
        errors.append("full covariance must not be required for declared replay")
    if replay.get("full_covariance_profile_required_for_true_equivalence") is not True:
        errors.append("full covariance should remain required for true equivalence")
    for key in [
        "full_covariance_profile_likelihood_closed",
        "published_or_reconstructed_profile_likelihood_imported",
        "selected_Rtheta_source_rows_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        if replay.get(key) is not False:
            errors.append(f"{key} must remain false")

    closed = cutset.get("closed_now", {})
    for key in [
        "published_likelihood_import_attempt_executed",
        "routec_selected_source_emission_attempt_executed",
        "external_profile_replay_closed_under_declared_standard",
        "SM_parity_pattern_imported_without_reopening_SM_parity",
    ]:
        if closed.get(key) is not True:
            errors.append(f"cutset did not close {key}")
    still = cutset.get("still_open", {})
    for key in [
        "published_or_reconstructed_8x8_profile_likelihood",
        "BCT_WZH_cross_covariance_entries",
        "RouteC_selected_source_emission",
        "selected_Rtheta_source_rows",
        "no_knob_value_source_derivation",
        "true_SM_equivalence",
    ]:
        if still.get(key) is not True:
            errors.append(f"cutset must keep {key} open")
    if cutset.get("recommended_next", {}).get("artifact") != (
        "MTT_Selected_ExternalProfileReplayFrozenBoundary_or_TrueEquivalenceValueSourceCutset_v1"
    ):
        errors.append("wrong next artifact")

    if errors:
        print("selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_publishedcovariancelikelihoodimport_or_routecselectedsourceemission audit: PASS")
    print(f"status: {STATUS}")
    print(f"external_replay_closed: {replay['external_profile_replay_closed_under_declared_standard']}")
    print(f"published_likelihood_imported: {likelihood['published_or_reconstructed_profile_likelihood_imported']}")
    print(f"routec_source_rows: {routec['accepted_selected_BCT_source_row_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
