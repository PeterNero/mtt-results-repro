"""Audit CONST-HIGGS-01 H7B1J dynamic Hessian or H-sector restriction export."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
DYNAMIC = BASE / "dynamic_hessian_edge_export_attempt.packet.json"
HSECTOR = BASE / "hsector_restriction_edge_export_attempt.packet.json"
WITNESS = BASE / "rejected_compact_h_dotd_numeric_witness.packet.json"
VALIDATOR = BASE / "strict_msource_gate_validator.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1J_DynamicHessianOrHSectorRestrictionExport_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1J_DYNAMIC_HESSIAN_OR_HSECTOR_RESTRICTION_GATE_BUILT_STRICT_EXPORT_OPEN"


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
    dynamic = load(DYNAMIC)
    hsector = load(HSECTOR)
    witness = load(WITNESS)
    validator = load(VALIDATOR)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("dynamic", dynamic),
        ("hsector", hsector),
        ("witness", witness),
        ("validator", validator),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1I_gate_imported"] is True, "H7B1I gate")
    require(candidate["dynamic_hessian_edge_attempted"] is True, "dynamic attempted")
    require(candidate["hsector_restriction_edge_attempted"] is True, "hsector attempted")
    require(candidate["compact_H_numeric_witness_emitted_support_only"] is True, "compact witness")
    require(candidate["conditional_RouteB_validator_passes_support_only"] is True, "conditional RouteB")
    require(candidate["selected_HYM_rank2_first_solve_imported"] is True, "HYM first solve")
    for key in [
        "strict_msource_gate_passes",
        "H_response_exported",
        "R_H_exported",
        "M_source_value_emitted",
        "B_Huv_value_emitted",
        "selected_finite_Huv_reduction_found",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1K_PhiFinMinimizerTraceOrEnd0HSectorFunctor_v1",
        "candidate next",
    )

    require(dynamic["status"] == "DYNAMIC_HESSIAN_EDGE_ATTEMPT_SUPPORT_STRONG_STRICT_EXPORT_OPEN", "dynamic status")
    support = dynamic["support_imported"]
    require(support["conditional_RouteB_validator_passes"] is True, "conditional RouteB support")
    require(support["unpatched_RouteB_validator_passes"] is False, "unpatched RouteB support")
    require(support["hessian_source_rows_assembled_from_same_rows_support"] is True, "hessian row support")
    require(support["unpatched_actual_row_fill_source_independent"] is False, "row independence")
    require(support["unpatched_source_independent_of_residual_projector_replay"] is False, "residual replay")
    require(support["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^TA")
    require(support["A_transpose_b"] == [12.0, 12.0], "A^Tb")
    require(support["b_norm_sq"] == 24.0, "b norm")
    require(support["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta")
    require(support["b_selected_emitted_by_independent_hessian"] is False, "b independent")
    require(support["dynamic_transfer_conditional_gram_exact"] is True, "conditional gram")
    require(support["five_clause_values_filled"] is True, "five clause filled")
    require(support["five_clause_values_promoted_as_source"] is False, "five clause promoted")
    why_dynamic = dynamic["why_current_support_is_not_H_response"]
    require(why_dynamic["conditional_validator_not_unpatched_export"] is True, "dynamic conditional reason")
    require(why_dynamic["hessian_vector_is_replay_from_residual_projector_contract"] is True, "dynamic replay reason")
    require(why_dynamic["five_clause_hessian_b_source_emitted"] is False, "dynamic source emitted")
    require(why_dynamic["five_clause_hessian_b_theorem_derived"] is False, "dynamic theorem")
    require(why_dynamic["five_clause_hessian_b_uses_replay_as_source"] is True, "dynamic uses replay")
    require(why_dynamic["c1_rows_live_in_flavor_response_coordinate_system_not_Huv_mass_strain"] is True, "dynamic coordinate")
    require(dynamic["export_decision"]["H_response_exported"] is False, "dynamic H_response")
    require(dynamic["export_decision"]["strict_gate_passes"] is False, "dynamic gate")

    require(hsector["status"] == "HSECTOR_RESTRICTION_EDGE_ATTEMPT_RANK2_SUPPORT_STRICT_EXPORT_OPEN", "hsector status")
    rank2 = hsector["rank2_and_projector_support_imported"]
    require(rank2["selected_diagonal_HYM_first_solve_closed"] is True, "HYM solve")
    require(rank2["rank2_End0_payload_closed"] is True, "End0 payload")
    require(rank2["rank2_to_sector_transfer_closed"] is False, "rank2 transfer")
    require(rank2["A_HYM_formula_emitted"] is True, "A_HYM")
    require(rank2["full_diagonal_End0_Green_closed"] is True, "End0 Green")
    require(rank2["rank2_to_sector_functor_closed"] is False, "sector functor")
    require(rank2["physical_dotD_alpha1_emitted"] is False, "physical dotD")
    require(rank2["sector_routing_values_emitted"] is False, "sector values")
    require(rank2["finite_model_active_projector_values_emitted"] is True, "projector values")
    require(rank2["selected_HYM_projector_values_promoted"] is False, "projector promoted")
    require(rank2["PhiFin_selected_trace_emitted"] is False, "PhiFin")
    require(rank2["selected_End0_to_sector_functor_values_extracted"] is False, "End0 functor values")
    require(rank2["scalar_normalization_no_go_closed"] is True, "scalar no-go")
    compact = hsector["compact_H_slot_support"]
    require(compact["dimension"] == 2, "compact dim")
    require(compact["expected_kernel_dimension"] == 1, "compact kernel")
    require(compact["kind"] == "single_higgs_carrier", "compact kind")
    require(compact["selected_dotD_source_verified"] is False, "compact dotD flag")
    require(compact["alpha1_driver_verified"] is False, "compact alpha1 flag")
    require(compact["selected_by_mtt"] is False, "compact selected")
    zero = hsector["zero_cluster_and_H_projector_support"]
    require(zero["zero_cluster_indices"] == [12, 13, 14], "zero cluster")
    require(zero["H_basis_count"] == 1, "H basis")
    require(zero["H_selected_source_verified"] is False, "H source flag")
    why_h = hsector["why_current_support_is_not_R_H"]
    for key in [
        "rank2_End0_lane_not_yet_sector_functor",
        "finite_projector_values_not_promoted_to_selected",
        "End0_to_sector_values_not_extracted",
        "compact_H_slot_is_single_higgs_carrier",
        "compact_H_slot_flags_are_unselected",
        "H_projector_is_rank_one_not_two_Higgs_lift",
        "rank_two_zero_cluster_support_is_not_a_restriction_map",
    ]:
        require(why_h[key] is True, f"hsector reason {key}")
    require(hsector["export_decision"]["R_H_exported"] is False, "R_H")
    require(hsector["export_decision"]["B_Huv_or_two_column_lift_exported"] is False, "B_Huv")

    require(witness["status"] == "COMPACT_H_DOTD_NUMERIC_WITNESS_REJECTED_AS_MSOURCE_OR_RH", "witness status")
    values = witness["witness_values"]
    require(values["lower_left_complex_entry_z"] == [0.22323835599578146, 0.44739762673968303], "witness z")
    require(values["would_be_Delta_if_promoted"] == 0.0, "witness Delta")
    require(values["would_be_abs_Omega_sq_if_promoted"] == 0.0625, "witness Omega")
    require(values["would_be_s_beta_if_promoted"] == 0.0, "witness s_beta")
    checks = witness["rejection_checks"]
    require(checks["selected_by_mtt"] is False, "witness selected")
    require(checks["selected_dotD_source_verified"] is False, "witness dotD flag")
    require(checks["alpha1_driver_verified"] is False, "witness alpha1 flag")
    require(checks["is_dotD_response_not_mass_strain_Hessian"] is True, "witness not Hessian")
    require(checks["is_single_higgs_carrier_not_UV_two_Higgs_lift"] is True, "witness single H")
    for key, value in witness["promotion_decision"].items():
        if key.startswith("promote_to_"):
            require(value is False, f"witness promoted {key}")

    require(validator["status"] == "STRICT_MSOURCE_GATE_VALIDATOR_FAILS_CURRENT_EXPORT_ATTEMPT", "validator status")
    require(validator["passes"] is False, "validator pass")
    fields = validator["required_fields"]
    require(fields["dynamic_hessian_or_mass_strain_source_owned"] is False, "validator dynamic")
    require(fields["H_sector_restriction_map_source_owned"] is False, "validator hsector")
    require(fields["finite_exactness_or_error_certificate"] is False, "validator exactness")
    require(fields["not_residual_replay_or_conditional_witness"] is False, "validator replay")
    require(fields["no_observed_selector"] is True, "validator observed")
    require(fields["same_q79_F_m1_branch"] is True, "validator branch")
    all_none(validator["strict_outputs"], "strict output")
    require(validator["superset_strategy"]["combining_paths"] is True, "superset")
    require(len(validator["superset_strategy"]["straight_paths_tested"]) == 2, "straight paths")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1K_PHIFIN_TRACE_OR_END0_HSECTOR_FUNCTOR", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR"), "next label")
    require(len(next_work["two_legal_exits"]) == 2, "next exits")
    require(len(next_work["do_not_repeat"]) == 4, "next guardrails")

    require(cert["status"] == STATUS, "cert status")
    require(cert["dynamic_hessian_edge_attempted"] is True, "cert dynamic")
    require(cert["hsector_restriction_edge_attempted"] is True, "cert hsector")
    require(cert["compact_H_numeric_witness_emitted_support_only"] is True, "cert witness")
    require(cert["strict_msource_gate_passes"] is False, "cert gate")
    require(cert["H_response_exported"] is False, "cert H_response")
    require(cert["R_H_exported"] is False, "cert R_H")
    require(cert["M_source_value_emitted"] is False, "cert M")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")
    require("strict M_source gate passes               False" in note, "note gate")
    require("compact H numeric witness retained        support only" in note, "note witness")
    require("H7B1K-PHIFIN-MINIMIZER-TRACE-OR-END0-HSECTOR-FUNCTOR" in note, "note next")

    print("CONST-HIGGS-01 H7B1J dynamic Hessian/H-sector restriction audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
