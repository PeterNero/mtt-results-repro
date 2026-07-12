"""Audit public 8x8 likelihood search or Route-C source emission execution."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SLUG = "selected_public8x8likelihoodsearch_or_routecsourceemissionexecution"
STATUS = (
    "MTT_SELECTED_PUBLIC8X8LIKELIHOODSEARCH_OR_ROUTECSOURCEEMISSIONEXECUTION_"
    "BUILT_SUBGATES_CLOSED_TRUE_EQ_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    likelihood = load(DATA / SLUG / "public_8x8_likelihood_search_execution.packet.json")
    routec = load(DATA / SLUG / "routec_source_emission_execution.packet.json")
    noknob = load(DATA / SLUG / "noknob_value_source_execution.packet.json")
    cutset = load(DATA / SLUG / "next_cutset_after_public8x8_or_routec_execution.packet.json")
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

    if likelihood.get("target_shape") != [8, 8]:
        errors.append("public likelihood target should be 8x8")
    if likelihood.get("target_symmetric_entries") != 36:
        errors.append("public likelihood target should have 36 symmetric entries")
    if likelihood.get("missing_BCT_WZH_cross_covariance_entries") != 15:
        errors.append("missing cross entries should remain 15")
    if likelihood.get("subblock_provenance_found") is not True:
        errors.append("subblock provenance should be found")
    if likelihood.get("combined_8x8_likelihood_found") is not False:
        errors.append("combined 8x8 likelihood must remain absent")
    if likelihood.get("accepted_as_full_profile_likelihood") is not False:
        errors.append("full profile likelihood must not be accepted")

    if routec.get("selected_HYM_connection_subgate_closed") is not True:
        errors.append("Route-C HYM connection subgate should be closed")
    if routec.get("diagonal_End0_DE_Green_lane_closed") is not True:
        errors.append("Route-C diagonal End0 lane should be closed")
    if routec.get("Pi_Rtheta_closed") is not False:
        errors.append("Pi_Rtheta must remain open")
    if routec.get("selected_value_evaluator_closed") is not False:
        errors.append("selected value evaluator must remain open")
    if routec.get("value_evaluator_readiness_present_count") != 5:
        errors.append("Rtheta readiness should be 5")
    if routec.get("value_evaluator_readiness_required_count") != 7:
        errors.append("Rtheta readiness required should be 7")
    remaining = routec.get("remaining_readiness_items", {})
    for key in [
        "selected_sector_B_N_basis",
        "rank2_to_sector_transfer_values",
        "sector_ready_rhoE_DE_Riesz_Green_dotD_C1",
        "selected_quadrature_truncation_error_for_sector_payload",
    ]:
        if remaining.get(key) is not True:
            errors.append(f"Route-C remaining item missing: {key}")
    if routec.get("minimal_next_routec_object") != "SelectedRThetaSectorBNBasisAndTransferPayload":
        errors.append("wrong minimal next Route-C object")

    if noknob.get("first_value_source_row_numeric_payload_emitted") is not True:
        errors.append("first numeric value source row should be emitted")
    if noknob.get("primitive_exactness_backimported") is not True:
        errors.append("primitive exactness should be backimported")
    if noknob.get("primitive_seed", {}).get("exact_value") != "4/3":
        errors.append("primitive seed exact value should be 4/3")
    if noknob.get("accepted_as_selected_dynamic_value_source_row_now") is not False:
        errors.append("dynamic value-source row must not be promoted")
    if noknob.get("all_72_row_exactness_available") is not True:
        errors.append("72-row exactness should be available")
    if noknob.get("strict_vsd02_fill_attempt_closed") is not True:
        errors.append("VSD02 strict fill attempt should be closed")
    if noknob.get("accepted_source_row_count") != 0:
        errors.append("accepted source row count should remain zero")
    if noknob.get("minimal_next_noknob_object") != "PrimitiveToDynamicValueSourceAssemblyMap":
        errors.append("wrong minimal next no-knob object")

    closed = cutset.get("closed_now", {})
    for key in [
        "public_8x8_search_executed",
        "subblock_provenance_confirmed",
        "RouteC_HYM_connection_subgate_closed",
        "RouteC_diagonal_End0_DE_Green_lane_closed",
        "no_knob_first_exact_primitive_seed_backimported",
        "strict_VSD02_schema_and_fill_attempt_closed",
    ]:
        if closed.get(key) is not True:
            errors.append(f"cutset did not close {key}")
    still = cutset.get("still_open", {})
    for key in [
        "combined_public_8x8_likelihood",
        "selected_sector_B_N_basis",
        "rank2_to_sector_transfer_values",
        "PrimitiveToDynamicValueSourceAssemblyMap",
        "selected_dynamic_value_source_rows",
        "selected_Rtheta_source_rows",
        "true_SM_equivalence",
    ]:
        if still.get(key) is not True:
            errors.append(f"cutset must keep {key} open")
    if cutset.get("recommended_next", {}).get("artifact") != (
        "MTT_Selected_RThetaSectorTransferOrPrimitiveAssemblyMapExecution_v1"
    ):
        errors.append("wrong next artifact")

    if errors:
        print("selected_public8x8likelihoodsearch_or_routecsourceemissionexecution audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("selected_public8x8likelihoodsearch_or_routecsourceemissionexecution audit: PASS")
    print(f"status: {STATUS}")
    print(f"combined_8x8_found: {likelihood['combined_8x8_likelihood_found']}")
    print(f"rtheta_readiness: {routec['value_evaluator_readiness_present_count']}/{routec['value_evaluator_readiness_required_count']}")
    print(f"primitive_seed: {noknob['primitive_seed']['exact_value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
