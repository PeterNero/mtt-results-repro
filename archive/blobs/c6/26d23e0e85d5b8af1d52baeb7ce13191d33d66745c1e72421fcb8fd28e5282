"""Audit CONST-HIGGS-01 H7B1K Phi_fin/projector/dotD import gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1k_phifin_minimizer_trace_or_end0_hsector_functor"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
STATIONARY_IMPORT = BASE / "stationary_phifin_projector_dotd_import.packet.json"
HSECTOR_BOUNDARY = BASE / "hsector_rank_one_boundary.packet.json"
DYNAMIC_HUV_VALIDATOR = BASE / "dynamic_huv_gate_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1K_PhiFinProjectorDotDImportGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1K_PHIFIN_PROJECTOR_DOTD_SLOT_IMPORTED_DYNAMIC_HUV_GATE_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def all_none(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is None, f"{name} emitted {key}")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    stationary = load(STATIONARY_IMPORT)
    hsector = load(HSECTOR_BOUNDARY)
    validator = load(DYNAMIC_HUV_VALIDATOR)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("stationary", stationary),
        ("hsector", hsector),
        ("validator", validator),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1J_gate_imported"] is True, "H7B1J import")
    require(candidate["stationary_phifin_projector_dotd_slot_imported"] is True, "stationary import")
    require(candidate["stationary_projector_rho_s_dotd_subgate_closed"] is True, "stationary subgate")
    require(candidate["physical_dotD_alpha1_removed_from_active_frontier"] is True, "dotD removed")
    require(candidate["H_sector_rank_one_boundary_proved"] is True, "H boundary")
    for key in [
        "strict_dynamic_Huv_gate_passes",
        "H_response_exported",
        "R_H_exported",
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"]
        == "MTT_CONST_HIGGS_01_H7B1L_DynamicPhiFinC1HuvResponseOrIndependentHuvHessian_v1",
        "candidate next",
    )

    require(stationary["status"] == "STATIONARY_PHIFIN_PROJECTOR_RHOS_DOTD_SLOT_IMPORTED", "stationary status")
    imported = stationary["imported_stationary_closures"]
    for key in [
        "raw_model_active_equivalence_rejected",
        "gauge_transported_trace_proved",
        "functional_selected_trace_proved",
        "rho_candidate_promoted_to_functional_selected_rho_s",
        "finite_projector_source_promotion_proved",
        "selected_projector_source_verified",
        "validator_ready_stationary_rho_s",
        "stationary_projector_source_verified",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
        "riesz_green_dotd_projector_retention_slot_closed",
        "physical_dotD_alpha1_removed_from_active_frontier",
    ]:
        require(imported[key] is True, f"stationary import missing {key}")
    h_slot = stationary["h_sector_imported_slot"]
    require(h_slot["sector"] == "H", "H sector")
    require(h_slot["rank"] == 1, "H rank")
    require(h_slot["selected_basis_labels"] == ["H:h0"], "H label")
    require(h_slot["model_basis_indices"] == [12], "H index")
    require(h_slot["transport"] == "identity on Higgs singlet", "H transport")
    require(h_slot["source_verified_by_transport_conjugation"] is True, "H source")
    require(h_slot["stationary_rho_s_promoted"] is True, "H rho_s")
    require(h_slot["green_operator_valid"] is True, "H Green")
    require(h_slot["riesz_projector_valid"] is True, "H Riesz")
    open_boundary = stationary["open_dynamic_boundary_imported"]
    for key in [
        "dynamic_PhiFin_C1_payload_emitted",
        "A_selected_emitted",
        "b_selected_emitted",
        "primitive_C1_contractions_emitted",
        "actual_dynamic_QaSU3_operator_packet_complete",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(open_boundary[key] is False, f"dynamic boundary overclosed {key}")
    require(stationary["superset_strategy"]["combining_paths"] is True, "stationary superset")
    require(stationary["superset_strategy"]["promotion_scope"] == "stationary sector source packet only", "scope")

    require(hsector["status"] == "HSECTOR_STATIONARY_RANK_ONE_BOUNDARY_PROVED_HUV_RESTRICTION_OPEN", "hsector status")
    require(hsector["boundary_theorem"]["proved"] is True, "hsector theorem")
    why = hsector["why_not_huv_response"]
    for key in [
        "H_rank_one_stationary_projector",
        "H_basis_is_single_label_H_h0",
        "transport_identity_on_higgs_singlet",
        "rank_one_projector_not_two_column_B_Huv",
        "stationary_projector_not_dynamic_response_restriction",
        "dynamic_PhiFin_C1_payload_open",
        "A_selected_and_b_selected_open",
        "primitive_C1_contractions_open",
        "selected_H_response_absent",
        "selected_R_H_absent",
        "selected_UV_two_Higgs_lift_absent",
    ]:
        require(why[key] is True, f"hsector reason {key}")
    emissions = hsector["emission_decision"]
    for key in [
        "H_response_exported",
        "R_H_exported",
        "B_Huv_exported",
        "M_source_exported",
        "Huv_exported",
        "s_beta_exported",
        "lambda_H_exported",
    ]:
        require(emissions[key] is False, f"hsector emitted {key}")

    require(validator["status"] == "DYNAMIC_HUV_MSOURCE_GATE_STILL_FAILS_AFTER_STATIONARY_IMPORT", "validator status")
    require(validator["passes"] is False, "validator pass")
    fields = validator["required_fields_after_stationary_import"]
    require(fields["stationary_projector_rho_s_dotD_imported"] is True, "validator stationary import")
    require(fields["no_observed_selector"] is True, "validator observed")
    require(fields["same_q79_F_m1_branch"] is True, "validator branch")
    for key in [
        "same_branch_selected_H_response",
        "same_branch_selected_R_H",
        "dynamic_PhiFin_C1_payload",
        "A_selected_and_b_selected",
        "primitive_C1_contractions",
        "UV_two_Higgs_lift_B_Huv",
        "finite_exactness_or_error_certificate_for_Huv",
    ]:
        require(fields[key] is False, f"validator overclosed {key}")
    all_none(validator["strict_outputs"], "strict output")
    route_a = validator["route_results"]["H7B1K_A_stationary_PhiFin_full_operator_promotion"]
    require(route_a["stationary_subgate_passes"] is True, "route A stationary")
    require(route_a["dynamic_Huv_gate_passes"] is False, "route A dynamic")
    route_b = validator["route_results"]["H7B1K_B_independent_Huv_Hessian_or_restriction_table"]
    require(route_b["table_emitted"] is False, "route B table")
    require(route_b["dynamic_Huv_gate_passes"] is False, "route B dynamic")
    require(validator["superset_strategy"]["combining_paths"] is True, "validator superset")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1L_DYNAMIC_PHIFIN_C1_HUV_RESPONSE_OR_INDEPENDENT_HUV_HESSIAN", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1L-DYNAMIC-PHIFIN-C1-HUV-RESPONSE-OR-INDEPENDENT-HUV-HESSIAN"), "next label")
    require(len(next_work["two_legal_exits"]) == 2, "next exits")
    require(len(next_work["do_not_repeat"]) == 4, "next guardrails")

    require(cert["status"] == STATUS, "cert status")
    require(cert["stationary_phifin_projector_dotd_slot_imported"] is True, "cert import")
    require(cert["stationary_projector_rho_s_dotd_subgate_closed"] is True, "cert subgate")
    require(cert["physical_dotD_alpha1_removed_from_active_frontier"] is True, "cert dotD")
    require(cert["H_sector_rank_one_boundary_proved"] is True, "cert H")
    require(cert["strict_dynamic_Huv_gate_passes"] is False, "cert dynamic")
    require(cert["H_response_exported"] is False, "cert H response")
    require(cert["R_H_exported"] is False, "cert R_H")
    require(cert["B_Huv_value_emitted"] is False, "cert B")
    require(cert["M_source_value_emitted"] is False, "cert M")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("stationary Phi_fin/projector/rho_s/dotD slot imported  True" in note, "note stationary")
    require("strict dynamic Huv/M_source gate passes                False" in note, "note dynamic")
    require("H7B1L-DYNAMIC-PHIFIN-C1-HUV-RESPONSE-OR-INDEPENDENT-HUV-HESSIAN" in note, "note next")

    print("CONST-HIGGS-01 H7B1K Phi_fin/projector/dotD import audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
