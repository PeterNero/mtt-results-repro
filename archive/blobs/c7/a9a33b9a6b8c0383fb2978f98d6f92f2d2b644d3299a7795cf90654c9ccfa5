"""Audit physical dotD/sector-transfer import for the K-row frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicaldotdalpha1sectortransferretardedoverlapkernel_or_empiricalkparityimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECONCILIATION = PACKET_DIR / "physical_dotd_sector_transfer_import_reconciliation.packet.json"
READINESS = PACKET_DIR / "retarded_overlap_kernel_readiness_after_stationary_transfer.packet.json"
EMISSION = PACKET_DIR / "krow_emission_after_physical_transfer_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_physical_transfer_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalDotDAlpha1SectorTransferRetardedOverlapKernel_or_EmpiricalKParityImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PHYSICALDOTDALPHA1SECTORTRANSFERRETARDEDOVERLAPKERNEL_OR_EMPIRICALKPARITYIMPORT_"
    "BUILT_DOTD_SECTOR_IMPORTED_DYNAMIC_ROWS_OPEN"
)
NEXT = "MTT_Selected_DynamicRetardedOverlapDerivativeRows_or_TSchemeLambdaHSourceExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its local theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    reconciliation = load(RECONCILIATION)
    readiness = load(READINESS)
    emission = load(EMISSION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("reconciliation", reconciliation),
        ("readiness", readiness),
        ("emission", emission),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(cert["true_SM_equivalence_claimed"] is False, "certificate true SM overclaim")
    require(cert["full_no_knob_closure_claimed"] is False, "certificate full no-knob overclaim")

    decision = data["closure_decision"]
    require(decision["physical_dotD_alpha1_imported"] is True, "dotD not imported")
    require(decision["stationary_sector_transfer_imported"] is True, "sector transfer not imported")
    require(decision["dynamic_first_response_support_imported"] is True, "dynamic support not imported")
    require(decision["retarded_overlap_kernel_readiness_built"] is True, "readiness not built")
    require(decision["selected_retarded_overlap_derivative_rows_emitted"] is False, "retarded rows overemitted")
    require(decision["selected_T_scheme_rows_emitted"] is False, "T_scheme overemitted")
    require(decision["selected_lambda_H_payload_emitted"] is False, "lambda_H overemitted")
    require(decision["accepted_selected_K_source_row_count"] == 0, "K rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["controlled_empirical_K_import_available"] is True, "empirical K unavailable")
    require(
        decision["controlled_empirical_K_import_selected_for_no_knob"] is False,
        "empirical K promoted to no-knob",
    )
    require(decision["true_SM_equivalence_closed"] is False, "true SM closure overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclaimed")

    require(
        reconciliation["status"] == "PHYSICAL_DOTD_AND_STATIONARY_SECTOR_TRANSFER_IMPORTED_FOR_K_ATTEMPT",
        "reconciliation status mismatch",
    )
    require(
        reconciliation["direct_hym_firstsolve_branch"]["physical_dotD_alpha1_closed_in_direct_firstsolve_packet"]
        is False,
        "direct firstsolve dotD unexpectedly closed",
    )
    require(
        reconciliation["direct_hym_firstsolve_branch"]["finite_projector_values_emitted"] is True,
        "direct firstsolve projector progress missing",
    )
    require(
        reconciliation["direct_hym_firstsolve_branch"]["finite_projector_values_promoted_to_selected"] is False,
        "direct firstsolve projector overpromoted",
    )
    later = reconciliation["later_dotd_import"]
    for key in [
        "selected_dotD_transport_derivative_formula_closed",
        "selected_alpha1_driver_normalization_closed",
        "same_branch_dotD_alpha1_values_closed",
        "honest_dotD_alpha1_replay_closed",
    ]:
        require(later[key] is True, f"later dotD import missing {key}")
    stationary = reconciliation["stationary_sector_import"]
    for key in [
        "stationary_projector_source_verified",
        "validator_ready_stationary_rho_s",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "physical_dotD_alpha1_available_by_import",
        "all_stationary_rho_s_promoted",
        "all_source_verified",
    ]:
        require(stationary[key] is True, f"stationary import missing {key}")
    dynamic = reconciliation["dynamic_first_response_import"]
    require(dynamic["dynamic_matter_overlap_operator_packet_closed"] is True, "dynamic matter packet not closed")
    require(
        dynamic["selected_dynamic_QaSU3_operator_packet_first_response_layer_closed"] is True,
        "dynamic first response not closed",
    )
    require(
        dynamic["primitive_C1_contractions_selected_emitted_first_response_layer"] is True,
        "primitive first-response support missing",
    )
    require(dynamic["Yukawa_magnitudes_predicted"] is False, "Yukawa magnitudes overpredicted")
    require(dynamic["full_mass_spectrum_predicted"] is False, "mass spectrum overpredicted")
    closed = reconciliation["closed_for_this_k_attempt"]
    for key in [
        "physical_dotD_alpha1_available",
        "stationary_sector_projectors_available",
        "stationary_rho_s_available",
        "dynamic_first_response_support_available",
        "direct_hym_firstsolve_dotd_gap_superseded_by_later_import",
    ]:
        require(closed[key] is True, f"K attempt import not closed: {key}")
    still_not = reconciliation["still_not_emitted"]
    for key in [
        "selected_retarded_overlap_derivative_row_values",
        "selected_threshold_scheme_rows_T_scheme",
        "selected_lambda_H_H_sector_payload",
        "ten_selected_K_threshold_rows",
    ]:
        require(still_not[key] is False, f"reconciliation overemits {key}")

    require(readiness["status"] == "DOTD_SECTOR_TRANSFER_READY_RETARDED_ROW_VALUES_OPEN", "readiness status mismatch")
    require(readiness["row_count"] == 10, "readiness row count mismatch")
    require(readiness["required_selected_K_row_count"] == 10, "required K count mismatch")
    require(readiness["active_scalar_sector_classes"] == ["H", "d", "e", "u"], "sector classes changed")
    require(readiness["active_scalar_sector_class_upper_bound"] == 4, "sector upper bound changed")
    require(readiness["sector_class_bound_sufficient_for_ten_K_rows"] is False, "sector bound overclaimed")
    require(
        readiness["generation_basis_rank_typed_but_no_derivative_matrix_elements_emitted"] is True,
        "basis/derivative distinction missing",
    )
    require(
        readiness["functional_contract_imported"]["requires_selected_retarded_overlap_kernel"] is True,
        "functional retarded requirement missing",
    )
    require(
        readiness["functional_contract_imported"]["requires_selected_threshold_scheme_values"] is True,
        "functional threshold requirement missing",
    )
    require(
        readiness["threshold_scheme_gate"]["selected_threshold_response_functional_instantiated"] is False,
        "threshold response overinstantiated",
    )
    require(readiness["threshold_scheme_gate"]["accepted_T_scheme_source_row_count"] == 0, "T_scheme rows overaccepted")
    require(
        readiness["threshold_scheme_gate"]["generation_resolved_threshold_source_rows_closed"] is False,
        "generation threshold rows overclosed",
    )

    for row in readiness["row_readiness"]:
        require(row["stationary_sector_projector_available"] is True, f"{row['omega_id']} projector unavailable")
        require(row["stationary_rho_s_available"] is True, f"{row['omega_id']} rho_s unavailable")
        require(row["green_operator_valid"] is True, f"{row['omega_id']} Green invalid")
        require(row["physical_dotD_alpha1_available"] is True, f"{row['omega_id']} dotD unavailable")
        require(
            row["same_source_dynamic_matter_first_response_available"] is True,
            f"{row['omega_id']} dynamic support unavailable",
        )
        require(
            row["dynamic_first_response_is_scalar_K_value_source"] is False,
            f"{row['omega_id']} dynamic first response promoted to scalar source",
        )
        require(
            row["selected_retarded_overlap_derivative_row_emitted"] is False,
            f"{row['omega_id']} retarded row overemitted",
        )
        require(row["selected_threshold_scheme_row_emitted"] is False, f"{row['omega_id']} T_scheme overemitted")
        require(row["selected_K_threshold_row_emitted"] is False, f"{row['omega_id']} K row overemitted")
        require(row["emitted_K_threshold_value"] is None, f"{row['omega_id']} K value emitted")
        require(row["accepted_as_no_knob_source_row"] is False, f"{row['omega_id']} no-knob overaccepted")
        require(row["empirical_K_import_available"] is True, f"{row['omega_id']} empirical K unavailable")
        require(
            row["accepted_as_controlled_empirical_row"] is True,
            f"{row['omega_id']} empirical boundary missing",
        )
        require(row["observed_data_used_as_selector"] is False, f"{row['omega_id']} observed selector")
        require(row["target_fitting_used"] is False, f"{row['omega_id']} target fitting")
        require(
            "stationary sector projector/rho_s and physical dotD_alpha1 are available by import"
            in row["blocking_reasons"],
            f"{row['omega_id']} missing dotD import reason",
        )
        require(
            "same-source dynamic matter overlap is first-response/non-scalar support, not a scalar K_threshold value functional"
            in row["blocking_reasons"],
            f"{row['omega_id']} missing non-scalar guard",
        )
        if row["sector"] == "H":
            require(row["selected_lambda_H_payload_emitted"] is False, "H lambda overemitted")
            require("selected lambda_H H-sector payload is not emitted" in row["blocking_reasons"], "H lambda reason missing")
        else:
            require(row["selected_lambda_H_payload_emitted"] is None, f"{row['omega_id']} lambda marker mismatch")

    require(emission["status"] == "PHYSICAL_TRANSFER_IMPORTED_NO_SELECTED_K_ROWS_EMITTED", "emission status mismatch")
    require(emission["closed_K_grammar_rows"] is True, "K grammar not closed")
    require(emission["conditional_K_to_Omega_theorem"] is True, "conditional K theorem not imported")
    require(emission["physical_dotD_alpha1_available"] is True, "emission dotD missing")
    require(emission["stationary_sector_transfer_available"] is True, "emission sector transfer missing")
    require(emission["same_source_dynamic_first_response_support_available"] is True, "emission dynamic support missing")
    require(emission["selected_retarded_overlap_derivative_rows_emitted"] is False, "emission retarded rows overclaimed")
    require(emission["selected_T_scheme_rows_emitted"] is False, "emission T_scheme overclaimed")
    require(emission["selected_lambda_H_payload_emitted"] is False, "emission lambda overclaimed")
    require(emission["accepted_selected_K_source_row_count"] == 0, "emission K rows overaccepted")
    require(emission["accepted_internal_scalar_value_row_count"] == 0, "emission scalar rows overaccepted")
    require(emission["lambda_H_value_row_emitted"] is False, "emission lambda value overemitted")
    require(emission["controlled_empirical_K_rows_available"] == 10, "empirical K count mismatch")
    require(
        emission["controlled_empirical_K_import_selected_for_no_knob"] is False,
        "emission empirical K promoted",
    )
    require(len(emission["row_decisions"]) == 10, "emission row decisions mismatch")
    require(
        all(row["accepted_as_controlled_empirical_row"] is True for row in emission["row_decisions"]),
        "controlled empirical row boundary missing",
    )
    require(
        all(row["accepted_as_no_knob_source_row"] is False for row in emission["row_decisions"]),
        "some K row overaccepted",
    )

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "physical dotD_alpha1 imported into the K-row frontier",
        "stationary sector projector/rho_s/Green transfer imported into every K slot",
        "same-source dynamic matter overlap first-response layer imported as support",
        "direct HYM-firstsolve dotD wording superseded by later stationary/dotD import",
        "empirical K parity import retained as non-no-knob boundary",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected rowwise retarded-overlap derivative values",
        "selected threshold-scheme rows T_scheme.*",
        "selected lambda_H H-sector value/quartic payload",
        "ten selected K_threshold rows",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")
    for phrase in [
        "reopen physical dotD_alpha1 or stationary projectors as active blockers without a failed import audit",
        "use first-response dynamic matter matrices as scalar K_threshold rows",
        "use empirical K import as F_K",
        "use observed Yukawa/Higgs values to select T_scheme or retarded rows",
    ]:
        require(phrase in cutset["forbidden_routes"], f"cutset forbidden route missing {phrase}")

    for phrase in [
        "physical dotD_alpha1 imported into K frontier      : true",
        "stationary sector transfer imported into K slots   : true",
        "same-source dynamic first-response support imported: true",
        "selected retarded-overlap derivative rows : false",
        "selected T_scheme rows                    : false",
        "selected lambda_H payload                 : false",
        "accepted selected K rows                  : 0",
        "empirical K selected for no-knob           : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
