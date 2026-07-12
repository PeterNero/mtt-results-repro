"""Audit CONST-HIGGS-01 H3 selected Higgs quadratic stiffness/quartic gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
QUADRATIC_KERNEL = BASE / "selected_quadratic_stiffness_kernel.packet.json"
DYNAMIC_ROUTE = BASE / "dynamic_c1_retarded_overlap_route.packet.json"
LOCAL_GATE = BASE / "local_premise_vs_strict_gate.packet.json"
QUARTIC_BOUNDARY = BASE / "quartic_nonclosure_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H3_SelectedHiggsQuadraticStiffnessAndQuarticGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H3_SELECTED_QUADRATIC_STIFFNESS_PROMOTED_QUARTIC_GATE_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


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
    quadratic_kernel = load(QUADRATIC_KERNEL)
    dynamic_route = load(DYNAMIC_ROUTE)
    local_gate = load(LOCAL_GATE)
    quartic_boundary = load(QUARTIC_BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("quadratic_kernel", quadratic_kernel),
        ("dynamic_route", dynamic_route),
        ("local_gate", local_gate),
        ("quartic_boundary", quartic_boundary),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["G4_one_metrology_primitive_reused"] is True, "G4 reuse")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "quadratic closure")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["dynamic_C1_retarded_overlap_route_closed"] is False, "dynamic overclosed")
    require(candidate["local_premise_dynamic_C1_available"] is True, "local premise missing")
    require(candidate["unpatched_dynamic_C1_closed"] is False, "unpatched overclosed")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")
    require(candidate["superset_strategy"]["combined_paths_used_as_selectors"] is False, "superset selector misuse")

    kernel = quadratic_kernel["selected_source_kernel"]
    require(quadratic_kernel["status"] == "SELECTED_FINITE_HIGGS_QUADRATIC_STIFFNESS_KERNEL_PROMOTED", "kernel status")
    require(kernel["finite_basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis")
    require(kernel["finite_basis_dimension"] == 27, "basis dimension")
    require(kernel["sector"] == "H", "sector")
    require(kernel["H_sector_kernel_dimension"] == 1, "H kernel")
    require(kernel["H_sector_positive_dimension"] == 26, "H positive")
    require(kernel["H_sector_positive_multiplicity_sum"] == 26, "H multiplicity")
    require(kernel["H_sector_min_positive_eigenvalue"] == 1.0, "min positive")
    require(kernel["H_sector_heat_trace_t1"] == 1.886949076994966, "heat")
    require(kernel["H_sector_reduced_heat_trace_t1"] == 0.8869490769949658, "reduced heat")
    require(kernel["H_sector_log_pseudodeterminant"] == 43.802475498298655, "pseudodet")
    require(kernel["selected_eta_N"] == 1.0, "eta")
    require(kernel["selected_Riesz_Green_gap_lower_bound"] == 2.386490844928603, "gap")
    require(kernel["selected_Green_norm_bound"] == 0.4190252822989217, "green")
    require(quadratic_kernel["normalization_tier"]["strict_no_knob_metrology_value_selected"] is False, "metrology overselected")
    require(quadratic_kernel["normalization_tier"]["new_Higgs_specific_parameters"] == 0, "kernel params")
    require(quadratic_kernel["what_this_closes"]["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "kernel close")
    require(quadratic_kernel["what_this_does_not_close"]["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "kernel quartic")

    imported_dynamic = dynamic_route["imported_dynamic_status"]
    require(imported_dynamic["postsource_frontier_built"] is True, "frontier")
    require(imported_dynamic["selected_C1_response_closed"] is False, "C1 overclosed")
    require(imported_dynamic["A_selected_promoted"] is False, "A overclosed")
    require(imported_dynamic["b_selected_promoted"] is False, "b overclosed")
    require(imported_dynamic["sector_response_matrices_promoted"] is False, "sector overclosed")
    require(imported_dynamic["proof_cycle_condensed"] is True, "cycle")
    require(imported_dynamic["shared_missing_object_identified"] is True, "missing object")
    require(imported_dynamic["straight_and_parallel_superset_paths_locked_to_same_target"] is True, "superset target lock")
    require(imported_dynamic["typed_retarded_derivative_emitted"] is False, "typed overemitted")
    require(imported_dynamic["selected_primitive_response_emitted"] is False, "primitive overemitted")
    require(imported_dynamic["primitive_response_candidate_values_emitted"] is True, "candidate values")
    require(dynamic_route["conditional_readiness_not_promotion"]["conditional_A_rank"] == 2, "rank")
    require(dynamic_route["conditional_readiness_not_promotion"]["conditional_b_norm"] == 4.898979485566356, "b norm")
    require(dynamic_route["strict_H3_dynamic_route_closed"] is False, "dynamic route")

    local = local_gate["local_premise_tier"]
    require(local["local_dynamic_C1_closed"] is True, "local C1")
    require(local["unpatched_dynamic_C1_closed"] is False, "unpatched C1")
    require(local["no_knob_closed"] is False, "local no-knob")
    require(local["independent_kernel_execution_supplied"] is False, "independent kernel")
    require(local["theorem_proved_under_local_premise"] is True, "local theorem")
    require(local_gate["strict_Higgs_quartic_promotion_allowed_now"] is False, "local strict misuse")

    accepted = quartic_boundary["accepted_subresult"]
    require(accepted["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "boundary quadratic")
    require(accepted["linearized_second_variation_of_quadratic_DE_energy_closed"] is True, "boundary second variation")
    require(quartic_boundary["separation_lemma"]["proved"] is True, "separation lemma")
    acceptance = quartic_boundary["strict_H3_acceptance_result"]
    require(acceptance["same_source_Phi_fin_second_variation_restricted_to_Higgs_amplitude"] is False, "Phi_fin overclosed")
    require(acceptance["selected_quartic_threshold_Hessian_block_normalized_by_G4"] is False, "Hessian overclosed")
    require(acceptance["dynamic_C1_retarded_overlap_response_to_quartic_kernel"] is False, "retarded overclosed")
    require(acceptance["reused_G4_primitive"] is True, "acceptance G4")
    require(acceptance["reused_H2_selected_DE_gap_layer"] is True, "acceptance H2")
    require(acceptance["forbade_measured_Higgs_values_as_selectors"] is True, "Higgs guard")
    locked = quartic_boundary["locked_boundary_after_H3"]
    require(locked["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "locked quartic")
    require(locked["Higgs_quartic_numeric_value_derived"] is False, "locked numeric")
    require(locked["new_Higgs_specific_parameters"] == 0, "locked params")
    require(locked["one_universal_primitive_tier_preserved"] is True, "primitive tier")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NONLINEAR-HIGGS-SELF-INTERACTION-SOURCE-RULE", "primary")
    require(next_work["parallel"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4B-INDEPENDENT-RETARDED-OVERLAP-OR-GALERKIN-HESSIAN-EXPORT", "parallel")
    require(next_work["paper_update_section"]["label"] == "CONST-HIGGS-01 / PAPER-INSERT / QUADRATIC-STIFFNESS-QUARTIC-SEPARATION", "paper insert")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "cert quadratic")
    require(cert["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "cert quartic")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require(cert["dynamic_C1_retarded_overlap_route_closed"] is False, "cert dynamic")
    require(cert["local_premise_dynamic_C1_available"] is True, "cert local")
    require("H3-SELECTED-HIGGS-QUADRATIC" in note and "H4-NONLINEAR-HIGGS" in note, "note")

    print("CONST-HIGGS-01 H3 selected Higgs quadratic stiffness/quartic gate audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
