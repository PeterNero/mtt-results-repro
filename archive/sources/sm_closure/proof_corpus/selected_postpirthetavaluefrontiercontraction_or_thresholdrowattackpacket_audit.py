"""Audit post-Pi Rtheta value-frontier contraction or threshold-row attack packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket.py"

SLUG = "selected_postpirthetavaluefrontiercontraction_or_thresholdrowattackpacket"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostPiRThetaValueFrontierContraction_or_ThresholdRowAttackPacket_v1.md"

RETIREMENT = PACKET_DIR / "post_pi_stale_blocker_retirement.packet.json"
RECLASSIFICATION = PACKET_DIR / "vsd_obligation_reclassification_after_pi.packet.json"
CUTSET = PACKET_DIR / "minimal_threshold_row_cutset_after_post_pi.packet.json"
ROUTE_ORDER = PACKET_DIR / "threshold_row_attack_order_after_post_pi.packet.json"

STATUS = (
    "MTT_SELECTED_POSTPIRTHETAVALUEFRONTIERCONTRACTION_OR_THRESHOLDROWATTACKPACKET_"
    "BUILT_STALE_BLOCKERS_RETIRED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_PostPi_v1"
BLOCKERS = [
    "same_branch_scale_scheme_loop_convention",
    "threshold_matching_source_rows",
    "mass_scheme_conversion_source_rows",
    "no_knob_value_derivation",
    "full_profile_likelihood_or_accepted_diagonal_theorem",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    retirement = load(RETIREMENT)
    reclassification = load(RECLASSIFICATION)
    cutset = load(CUTSET)
    route_order = load(ROUTE_ORDER)
    note = NOTE.read_text(encoding="utf-8")

    errors: list[str] = []

    expect(candidate.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(candidate.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(candidate.get(key) is False, f"candidate guardrail overclaimed: {key}", errors)
        expect(cert.get(key) is False, f"certificate guardrail overclaimed: {key}", errors)

    expect(
        retirement.get("status") == "POST_PI_SOURCE_OWNER_AND_ASSEMBLY_BLOCKERS_RETIRED",
        "retirement status mismatch",
        errors,
    )
    retired = retirement.get("retired_from_old_first_row_open_set", {})
    for key in [
        "assembly_map_from_primitive_rows_to_dynamic_value_source_row",
        "physical_PhiFinC1_action_source_or_independent_provenance",
        "selected_A_b_deltaTheta_promotion",
        "honest_primitive_row_exactness_seed",
        "selected_dynamic_operator_source_owner",
        "Pi_Rtheta",
        "coefficient_functional_domain",
    ]:
        expect(retired.get(key) is True, f"stale blocker not retired: {key}", errors)
    still = retirement.get("still_not_retired", {})
    for key in [
        "selected_dynamic_overlap_threshold_tensor_T_selected",
        "same_branch_linking_tensor_rows_to_versioned_value_packet",
        "magnitude_bearing_projection_weights",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
    ]:
        expect(still.get(key) is True, f"value blocker over-retired: {key}", errors)
    expect(retirement.get("closure_claimed") is False, "retirement overclaimed full closure", errors)

    expect(
        reclassification.get("status") == "VSD_SOURCE_PROVENANCE_RECLASSIFIED_VALUES_STILL_OPEN",
        "reclassification status mismatch",
        errors,
    )
    expect(reclassification.get("required_row_count") == 5, "VSD required row count mismatch", errors)
    expect(
        reclassification.get("closed_row_count_after_reclassification") == 0,
        "VSD value rows overclosed",
        errors,
    )
    expect(
        reclassification.get("selected_dynamic_value_source_rows_emitted") is False,
        "dynamic value source rows overemitted",
        errors,
    )
    vsd01 = next(
        row for row in reclassification.get("reclassified_rows", [])
        if row.get("id") == "VSD-01-selected-overlap-value-kernel"
    )
    for key in [
        "all_72_primitive_rows_exact",
        "formal_110_row_assembly",
        "A_b_deltaTheta_promoted",
        "physical_PhiFinC1_action_source",
        "dynamic_matter_overlap_first_response_layer",
        "Pi_Rtheta",
    ]:
        expect(
            vsd01.get("post_pi_source_subrequirements_closed", {}).get(key) is True,
            f"VSD01 source subrequirement missing: {key}",
            errors,
        )
    for key in [
        "selected_dynamic_overlap_threshold_tensor_T_selected",
        "sector_rows_for_charged_fermions_and_lambda_H",
        "same_branch_link_to_versioned_value_packet",
    ]:
        expect(
            vsd01.get("post_pi_value_subrequirements_still_open", {}).get(key) is True,
            f"VSD01 value subrequirement overclosed: {key}",
            errors,
        )
    expect(vsd01.get("post_pi_closed") is False, "VSD01 overclosed", errors)

    expect(
        cutset.get("status") == "MINIMAL_VALUE_CUTSET_CONTRACTED_TO_THRESHOLD_PROFILE_ROWS",
        "cutset status mismatch",
        errors,
    )
    closed_support = cutset.get("closed_support_now", {})
    for key in [
        "Pi_Rtheta",
        "VSD01_source_assembly_subgate",
        "dynamic_matter_overlap_operator_packet_first_response",
        "coefficient_functional_domain",
        "source_normalized_projection_weights",
    ]:
        expect(closed_support.get(key) is True, f"cutset support not closed: {key}", errors)
    expect(cutset.get("minimal_remaining_blockers") == BLOCKERS, "minimal blocker list mismatch", errors)
    expect(cutset.get("minimal_remaining_blocker_count") == len(BLOCKERS), "minimal blocker count mismatch", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "closure_claimed",
    ]:
        expect(cutset.get(key) is False, f"cutset overclaimed: {key}", errors)
    expect(cutset.get("accepted_coefficient_value_count") == 0, "cutset accepted coefficients", errors)

    expect(
        route_order.get("status") == "ATTACK_ORDER_FIXED_CONVENTION_SOURCE_FIRST",
        "route order status mismatch",
        errors,
    )
    routes = route_order.get("ordered_routes", [])
    expect([route["target"] for route in routes[:5]] == [
        "same_branch_scale_scheme_loop_convention",
        "selected_threshold_response_functional_instantiated",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ], "route order mismatch", errors)
    expect(routes[0]["current_closed"] is False, "same-branch convention overclosed", errors)
    expect(route_order.get("recommended_next", {}).get("artifact") == NEXT, "route next mismatch", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "post_pi_frontier_synchronized",
        "stale_source_owner_and_assembly_blockers_retired",
        "VSD_01_source_provenance_subrequirements_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure missing: {key}", errors)
    for key in [
        "VSD_01_magnitude_value_row_closed",
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "selected_value_evaluator_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(closure.get(key) is False, f"candidate overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficients", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    expect("stale source-owner/assembly blockers retired      : true" in note, "note missing stale blocker retirement", errors)
    expect("VSD01 magnitude-bearing value row closed          : false" in note, "note missing VSD01 value guard", errors)
    expect("accepted Rtheta coefficient values                : 0" in note, "note missing coefficient guard", errors)

    if errors:
        print("Post-Pi Rtheta value-frontier contraction audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Post-Pi Rtheta value-frontier contraction audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
