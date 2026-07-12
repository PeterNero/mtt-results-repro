"""Audit R_theta sector-transfer or primitive assembly-map execution artifact."""

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
BUILDER = ROOT / "scripts" / "build_selected_rthetasectortransfer_or_primitiveassemblymapexecution.py"

SLUG = "selected_rthetasectortransfer_or_primitiveassemblymapexecution"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaSectorTransfer_or_PrimitiveAssemblyMapExecution_v1.md"

SECTOR = PACKET_DIR / "rtheta_sector_transfer_execution.packet.json"
ASSEMBLY = PACKET_DIR / "primitive_assembly_map_execution.packet.json"
PI_VALUE = PACKET_DIR / "pi_closure_value_evaluator_domain.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_sector_transfer_or_assembly_execution.packet.json"

STATUS = (
    "MTT_SELECTED_RTHETASECTORTRANSFER_OR_PRIMITIVEASSEMBLYMAPEXECUTION_"
    "BUILT_PI_AND_SOURCE_ASSEMBLY_CLOSED_THRESHOLD_ROWS_OPEN"
)
NEXT = "MTT_Selected_RThetaThresholdRows_or_ProfileConventionSourceClosure_CurrentFrontier_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    sector = load(SECTOR)
    assembly = load(ASSEMBLY)
    pi_value = load(PI_VALUE)
    cutset = load(CUTSET)
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
    for key in ["closure_claimed", "observed_data_used_as_selector", "target_fitting_used"]:
        expect(cert.get(key) is False, f"certificate guardrail overclaimed: {key}", errors)

    expect(
        sector.get("status") == "STATIONARY_SECTOR_TRANSFER_AND_DOTD_TRANSPORT_CLOSED",
        "sector packet status mismatch",
        errors,
    )
    for key in [
        "selected_HYM_connection_subgate_closed",
        "diagonal_End0_DE_Green_lane_closed",
        "stationary_sector_transfer_closed",
        "selected_stationary_rho_s_closed",
        "selected_sector_basis_projector_contract_closed",
        "selected_Riesz_Green_stationary_closed",
        "dotD_alpha1_transport_subgate_closed",
        "alpha1_driver_normalization_closed",
        "closure_claimed",
    ]:
        expect(sector.get(key) is True, f"sector field should be true: {key}", errors)
    expect(
        "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership"
        in sector.get("still_missing_before_primitive_import", []),
        "sector packet should preserve pre-import matter-slot blocker",
        errors,
    )
    expect(
        "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta"
        in sector.get("still_missing_before_primitive_import", []),
        "sector packet should preserve pre-import primitive-C1 blocker",
        errors,
    )

    expect(
        assembly.get("status") == "VSD01_SOURCE_ASSEMBLY_AND_DYNAMIC_OVERLAP_PACKET_CLOSED_VALUES_OPEN",
        "assembly packet status mismatch",
        errors,
    )
    expect(assembly.get("primitive_seed", {}).get("exact_value") == "4/3", "primitive seed should be 4/3", errors)
    for key in [
        "all_72_primitive_rows_exact",
        "formal_110_row_assembly",
        "A_selected_promoted",
        "b_selected_promoted",
        "deltaTheta_C1_promoted",
        "physical_PhiFinC1_action_source",
        "VSD01_source_assembly_subgate_closed",
        "dynamic_matter_overlap_operator_packet_closed",
        "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed",
        "closure_claimed",
    ]:
        expect(assembly.get(key) is True, f"assembly field should be true: {key}", errors)
    expect(assembly.get("Yukawa_mass_mixing_value_closure") is False, "assembly overclosed Yukawa", errors)
    expect(assembly.get("observed_data_used_as_selector") is False, "assembly observed selector", errors)
    expect(assembly.get("target_fitting_used") is False, "assembly target fitting", errors)

    expect(
        pi_value.get("status") == "PI_RTHETA_AND_VALUE_EVALUATOR_DOMAIN_CLOSED_NUMERIC_VALUES_OPEN",
        "Pi/value packet status mismatch",
        errors,
    )
    for key in [
        "Pi_Rtheta_closed",
        "primitive_C1_overlap_contractions_closed",
        "matter_slot_routing_closed",
        "coefficient_functional_domain_closed",
        "selected_dynamic_operator_source_owner_closed",
        "source_normalized_projection_weights_closed",
        "ordered_dependency_graph_closed",
        "generation_structure_support_closed",
    ]:
        expect(pi_value.get(key) is True, f"Pi/value field should be true: {key}", errors)
    for key in [
        "selected_threshold_response_functional_instantiated",
        "accepted_lambda_H_value",
        "closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        expect(pi_value.get(key) is False, f"Pi/value field overclaimed: {key}", errors)
    expect(pi_value.get("accepted_coefficient_value_count") == 0, "accepted coefficient count should be zero", errors)
    expect(pi_value.get("value_execution_readiness_present_count") == 4, "readiness present count mismatch", errors)
    expect(pi_value.get("value_execution_readiness_requirement_count") == 9, "readiness required count mismatch", errors)
    expected_blockers = [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ]
    expect(pi_value.get("blocking_failures") == expected_blockers, "blocking failures mismatch", errors)

    component_tests = pi_value.get("component_tests_after_primitive_c1_import", {})
    for key in [
        "selected_matter_slot_routing_available",
        "primitive_C1_overlap_or_no_need_available",
        "selected_primitive_C1_overlap_contractions_available",
        "selected_dynamic_matter_overlap_packet_validates",
    ]:
        expect(component_tests.get(key) is True, f"Pi component test missing: {key}", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "stationary_sector_transfer",
        "selected_stationary_rho_s",
        "dotD_alpha1_transport_subgate",
        "VSD01_source_assembly_subgate",
        "dynamic_matter_overlap_operator_packet_first_response",
        "Pi_Rtheta",
        "coefficient_functional_domain",
        "selected_dynamic_operator_source_owner",
        "ordered_value_frontier_dependency_graph",
    ]:
        expect(closed.get(key) is True, f"cutset did not close {key}", errors)
    still = cutset.get("still_open", {})
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
    ]:
        expect(still.get(key) is True, f"cutset overclosed or omitted {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)
    expect(cutset.get("closure_claimed") is False, "cutset overclaimed", errors)

    closure = candidate.get("closure_decision", {})
    for key in [
        "Pi_Rtheta_closed",
        "VSD01_source_assembly_subgate_closed",
        "dynamic_matter_overlap_operator_packet_first_response_closed",
        "coefficient_functional_domain_closed",
    ]:
        expect(closure.get(key) is True, f"candidate closure should be true: {key}", errors)
    for key in [
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
    ]:
        expect(closure.get(key) is False, f"candidate closure overclosed: {key}", errors)
    expect(closure.get("accepted_coefficient_value_count") == 0, "candidate accepted coefficient count", errors)
    expect(candidate.get("theorem", {}).get("proved") is True, "candidate theorem not proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem missing", errors)

    expect("Pi_Rtheta closed                        : true" in note, "note missing Pi closure", errors)
    expect("Rtheta coefficient values accepted      : 0" in note, "note missing zero-value guard", errors)
    expect("true SM equivalence                     : false" in note, "note missing true-equivalence guard", errors)

    if errors:
        print("RTheta sector-transfer/primitive-assembly audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("RTheta sector-transfer/primitive-assembly audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
