"""Audit CONST-HIGGS-01 H5 physical-action finite-trace ownership gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h5_physical_action_owns_finite_trace_kernel"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
OWNERSHIP_ATTEMPT = BASE / "physical_action_ownership_attempt.packet.json"
COUNTERMODEL_GUARDRAIL = BASE / "support_only_countermodel_guardrail.packet.json"
KERNEL_REDUCTION = BASE / "pre_residual_action_kernel_reduction.packet.json"
HIGGS_IMPLICATION = BASE / "higgs_quartic_implication.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H5_PhysicalActionOwnsFiniteTraceKernel_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H5_PHYSICAL_ACTION_OWNERSHIP_COUNTERMODEL_GUARDRAIL_BUILT"


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
    ownership_attempt = load(OWNERSHIP_ATTEMPT)
    countermodel_guardrail = load(COUNTERMODEL_GUARDRAIL)
    kernel_reduction = load(KERNEL_REDUCTION)
    higgs_implication = load(HIGGS_IMPLICATION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("ownership_attempt", ownership_attempt),
        ("countermodel_guardrail", countermodel_guardrail),
        ("kernel_reduction", kernel_reduction),
        ("higgs_implication", higgs_implication),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "quadratic")
    require(candidate["formal_110_row_replay_closed"] is True, "formal rows")
    require(candidate["support_only_countermodel_valid"] is True, "countermodel")
    require(candidate["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "action overclosed")
    require(candidate["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"] is False, "kernel theorem overclosed")
    require(candidate["SelectedHiggsNonlinearAmplitudeProjection_closed"] is False, "projection overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["superset_strategy"]["closed_support_used_as_selector"] is False, "support selector misuse")
    require(candidate["superset_strategy"]["combined_paths_used_as_free_parameters"] is False, "superset free parameter")

    direct = ownership_attempt["direct_attempt_result"]
    require(direct["physical_action_owns_finite_trace_kernel_proved_now"] is False, "direct proof overclosed")
    require(direct["closed_subclauses"]["finite_selected_C1_quotient"] is True, "finite C1")
    require(direct["closed_subclauses"]["finite_measure_normalization_trace_Frobenius"] is True, "trace Frobenius")
    require(direct["closed_subclauses"]["algebraic_finite_boundary_cancellation"] is True, "boundary")
    require(direct["closed_support"]["formal_110_rows_executed"] is True, "110 rows")
    require(direct["closed_support"]["formal_110_row_counts"]["total_rows"] == 110, "110 count")
    require(direct["closed_support"]["formal_110_row_counts"]["primitive_rows"] == 72, "primitive count")
    require(direct["closed_support"]["formal_110_row_counts"]["sector_matrix_rows"] == 36, "sector count")
    require(direct["closed_support"]["formal_110_row_counts"]["hessian_source_rows"] == 2, "hessian count")
    require(direct["still_required_physical_subclauses"]["physical_PhiFinC1_action_restriction"] is True, "action restriction")
    require(direct["still_required_physical_subclauses"]["same_source_b_selected_emission"] is True, "b selected")
    require(ownership_attempt["last_source_contract_status"]["formal_computation_layer_closed"] is True, "last formal")
    require(ownership_attempt["last_source_contract_status"]["route_A_physical_action_source_closed"] is False, "route A overclosed")
    require(ownership_attempt["last_source_contract_status"]["route_B_provenance_independence_closed"] is False, "route B overclosed")
    require(ownership_attempt["action_equivalence_cutset"]["theorem_proved"] is True, "equivalence theorem")
    require(ownership_attempt["action_equivalence_cutset"]["finite_boundary_no_longer_blocker"] is True, "finite boundary retired")
    require(ownership_attempt["action_equivalence_cutset"]["physical_action_identity_open"] is True, "physical identity open")
    require(ownership_attempt["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "ownership packet")

    counter = countermodel_guardrail["countermodel"]
    require(counter["support_only_countermodel_valid"] is True, "guard countermodel")
    require(counter["blocks_derivation_from_closed_support_alone"] is True, "blocks support")
    require(counter["closed_support_not_enough"] is True, "not enough")
    require(counter["validator_rejects_current_two_exit_packet"] is True, "validator")
    formal = countermodel_guardrail["formal_rows"]
    require(formal["formal_110_row_replay_closed"] is True, "formal replay")
    require(formal["formal_A_b_deltaTheta_replay_closed"] is True, "A/b/delta")
    require(formal["all_72_exact_rows_retained"] is True, "72 exact")
    require(formal["physical_PhiFinC1_action_source_closed"] is False, "physical source closed")
    require(formal["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require("closed 110-row replay -> PhysicalActionOwnsFiniteTraceKernel" in countermodel_guardrail["forbidden_promotions"], "forbidden")

    kernel = kernel_reduction["remaining_kernel_theorem"]
    require(kernel["theorem_name"] == "SelectedPhiFinC1PreResidualActionKernelTheorem", "kernel name")
    require(kernel["proved_now"] is False, "kernel overproved")
    require(kernel["must_not_be_used_as_free_patch"] is True, "free patch")
    require("reuse exact R_Z/R_X decomposition as source selection" in kernel["forbidden_shortcuts"], "R_Z shortcut")
    require(kernel["would_close"]["selected_variation_functional"] is True, "would close variation")
    require(kernel["would_close"]["same_source_hessian"] is True, "would close Hessian")
    closure = kernel_reduction["H5_closure_result"]
    require(closure["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "closure action")
    require(closure["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"] is False, "closure kernel")
    require(closure["SelectedFiniteC1SourceIdentityLemma_unpatched_closed"] is False, "closure source identity")
    require(closure["independent_Galerkin_or_quadrature_replacement_closed"] is False, "closure independent")

    update = higgs_implication["H5_update"]
    require(update["object_1_PhysicalActionOwnsFiniteTraceKernel"] is False, "Higgs object 1")
    require(update["object_2_SelectedHiggsNonlinearAmplitudeProjection"] is False, "Higgs object 2")
    require(update["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "Higgs quartic")
    require(update["Higgs_quartic_numeric_value_derived"] is False, "Higgs numeric")
    require(update["new_Higgs_specific_parameters"] == 0, "Higgs params update")
    guard = higgs_implication["strict_guardrail"]
    require(guard["no_measured_lambda_H_selector"] is True, "lambda guard")
    require(guard["no_Higgs_mass_or_vev_backsolve"] is True, "Higgs backsolve")
    require(guard["no_spectral_gap_to_quartic_promotion"] is True, "gap guard")
    require(guard["no_local_patch_counted_as_no_knob"] is True, "local guard")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM", "primary")
    require(next_work["parallel"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION", "parallel")
    require(next_work["paper_update_section"]["label"] == "CONST-HIGGS-01 / PAPER-INSERT / ACTION-OWNERSHIP-COUNTERMODEL-GUARDRAIL", "paper insert")

    require(cert["status"] == STATUS, "cert status")
    require(cert["formal_110_row_replay_closed"] is True, "cert formal")
    require(cert["support_only_countermodel_valid"] is True, "cert countermodel")
    require(cert["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "cert action")
    require(cert["SelectedPhiFinC1PreResidualActionKernelTheorem_closed"] is False, "cert kernel")
    require(cert["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "cert quartic")
    require("H5-PHYSICAL-ACTION" in note and "H6-SELECTED-PHIFINC1" in note, "note")

    print("CONST-HIGGS-01 H5 physical-action finite-trace ownership audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
