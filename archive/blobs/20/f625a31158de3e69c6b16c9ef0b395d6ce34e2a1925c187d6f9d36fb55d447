"""Audit external-profile replay frozen boundary or true-equivalence value-source cutset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset"
STATUS = (
    "MTT_SELECTED_EXTERNALPROFILEREPLAYFROZENBOUNDARY_OR_TRUEEQUIVALENCEVALUESOURCECUTSET_"
    "BUILT_THREE_LANES_ATTEMPTED_EXTERNAL_REPLAY_FROZEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    boundary = load(DATA / SLUG / "external_profile_replay_frozen_boundary.packet.json")
    lanes = load(DATA / SLUG / "three_lane_true_equivalence_value_source_attempt.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_three_lane_attempt.packet.json")
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

    if boundary.get("boundary_locks") is not True:
        errors.append("frozen boundary should lock")
    if boundary.get("closed_tiers", {}).get("external_profile_replay_under_declared_standard") is not True:
        errors.append("external profile replay should be frozen closed")
    if boundary.get("external_profile_coordinate_count") != 8:
        errors.append("external profile coordinate count must remain 8")
    guards = boundary.get("guardrails", {})
    for key in [
        "full_covariance_profile_likelihood_closed",
        "selected_Rtheta_source_rows_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        if guards.get(key) is not False:
            errors.append(f"boundary guardrail {key} must remain false")

    lane_a = lanes.get("lane_A_public_8x8_likelihood", {})
    if lane_a.get("attempted") is not True:
        errors.append("lane A not attempted")
    if lane_a.get("fixed_target_shape") != [8, 8]:
        errors.append("lane A target must be 8x8")
    if lane_a.get("fixed_target_symmetric_entries") != 36:
        errors.append("lane A must preserve 36 symmetric entries")
    if lane_a.get("missing_BCT_WZH_cross_covariance_entries") != 15:
        errors.append("lane A must preserve 15 missing cross entries")
    if lane_a.get("published_or_reconstructed_profile_likelihood_imported") is not False:
        errors.append("lane A must not import public likelihood")
    if len(lane_a.get("external_refs_checked", [])) < 2:
        errors.append("lane A should record external refs checked")

    lane_b = lanes.get("lane_B_routec_selected_source_rows", {})
    if lane_b.get("attempted") is not True:
        errors.append("lane B not attempted")
    if lane_b.get("minimal_internal_missing_object") != "SelectedRouteCStromingerGalerkinResidualSolve":
        errors.append("lane B missing object mismatch")
    if lane_b.get("selected_routec_galerkin_solve_closed") is not False:
        errors.append("lane B Route-C solve must remain open")
    if lane_b.get("accepted_selected_BCT_source_row_count") != 0:
        errors.append("lane B should promote zero selected source rows")
    if lane_b.get("formal_lift_lower_validators_all_pass") is not True:
        errors.append("lane B formal lift should still pass")
    if lane_b.get("basis_skeleton_closed") is not True:
        errors.append("lane B basis skeleton should be closed")
    if lane_b.get("rtheta_value_evaluator_readiness_present_count") != 5:
        errors.append("lane B Rtheta readiness should be 5")
    if lane_b.get("rtheta_value_evaluator_readiness_required_count") != 7:
        errors.append("lane B Rtheta readiness required should be 7")

    lane_c = lanes.get("lane_C_no_knob_value_source_rows", {})
    if lane_c.get("attempted") is not True:
        errors.append("lane C not attempted")
    if lane_c.get("obligation_kernel_closed") is not True:
        errors.append("lane C obligation kernel should be closed")
    if lane_c.get("import_manifest_closed") is not True:
        errors.append("lane C import manifest should be closed")
    for key in [
        "selected_dynamic_value_source_rows_emitted",
        "accepted_external_threshold_rows_imported",
        "no_knob_value_derivation_closed",
        "accepted_threshold_mass_scheme_source_layer_closed",
    ]:
        if lane_c.get(key) is not False:
            errors.append(f"lane C {key} must remain false")

    combined = lanes.get("combined_decision", {})
    if combined.get("external_profile_replay_frozen") is not True:
        errors.append("combined decision must freeze external replay")
    for key in [
        "true_SM_equivalence_closed",
        "full_covariance_profile_likelihood_closed",
        "selected_Rtheta_source_rows_closed",
        "no_knob_value_source_derivation_closed",
    ]:
        if combined.get(key) is not False:
            errors.append(f"combined {key} must remain false")

    closed = cutset.get("closed_now", {})
    for key in [
        "external_profile_replay_frozen_boundary",
        "lane_A_public_8x8_likelihood_attempted",
        "lane_B_routec_selected_source_rows_attempted",
        "lane_C_no_knob_value_source_rows_attempted",
        "three_lane_true_equivalence_cutset_sharpened",
    ]:
        if closed.get(key) is not True:
            errors.append(f"cutset did not close {key}")
    if cutset.get("recommended_next", {}).get("artifact") != (
        "MTT_Selected_Public8x8LikelihoodSearch_or_RouteCSourceEmissionExecution_v1"
    ):
        errors.append("wrong next artifact")

    if errors:
        print("selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_externalprofilereplayfrozenboundary_or_trueequivalencevaluesourcecutset audit: PASS")
    print(f"status: {STATUS}")
    print(f"external_replay_frozen: {boundary['boundary_locks']}")
    print("lanes_attempted: A/B/C")
    print(f"rtheta_readiness: {lane_b['rtheta_value_evaluator_readiness_present_count']}/{lane_b['rtheta_value_evaluator_readiness_required_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
