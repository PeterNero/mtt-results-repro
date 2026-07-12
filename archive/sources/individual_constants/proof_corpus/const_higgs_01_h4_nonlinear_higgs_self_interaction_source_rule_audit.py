"""Audit CONST-HIGGS-01 H4 nonlinear Higgs self-interaction source-rule gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
SOURCE_IDENTITY = BASE / "source_identity_bridge.packet.json"
INDEPENDENT_HESSIAN = BASE / "independent_hessian_quadrature_route.packet.json"
HIGGS_ACCEPTANCE = BASE / "higgs_quartic_source_acceptance.packet.json"
STRICT_TEMPLATE = BASE / "strict_nonlinear_higgs_source_template.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H4_NonlinearHiggsSelfInteractionSourceRule_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H4_NONLINEAR_SOURCE_RULE_CUTSET_BUILT_QUARTIC_OPEN"


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
    source_identity = load(SOURCE_IDENTITY)
    independent_hessian = load(INDEPENDENT_HESSIAN)
    higgs_acceptance = load(HIGGS_ACCEPTANCE)
    strict_template = load(STRICT_TEMPLATE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, item in [
        ("candidate", candidate),
        ("source_identity", source_identity),
        ("independent_hessian", independent_hessian),
        ("higgs_acceptance", higgs_acceptance),
        ("strict_template", strict_template),
    ]:
        clean(item, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "H3 quadratic")
    require(candidate["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "action ownership overclosed")
    require(candidate["SelectedHiggsNonlinearAmplitudeProjection_closed"] is False, "Higgs projection overclosed")
    require(candidate["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "quartic overemitted")
    require(candidate["Higgs_quartic_numeric_value_derived"] is False, "lambda overderived")
    require(candidate["strict_no_knob_Higgs_closure"] is False, "strict overclosed")
    require(candidate["new_Higgs_specific_parameters"] == 0, "Higgs params")
    require(candidate["superset_strategy"]["combined_paths_used_as_selectors"] is False, "superset selector misuse")

    imported = source_identity["imported_source_identity_result"]
    require(imported["theorem_proved"] is True, "source identity theorem")
    require(imported["admissible_c1_variation_space_derived"] is True, "admissible variation")
    require(imported["postcheck_independence_guard_derived"] is True, "independence guard")
    require(imported["single_surviving_obstruction_identified"] is True, "single obstruction")
    require(imported["PhysicalActionOwnsFiniteTraceKernel_open"] is True, "PhysicalActionOwnsFiniteTraceKernel")
    require(imported["SelectedFiniteC1SourceIdentityLemma_unpatched_open"] is True, "unpatched source identity")
    patched = source_identity["patched_local_or_parity_tier"]
    require(patched["SM_parity_dynamic_C1_closed_under_local_principle"] is True, "patched parity")
    require(patched["patched_theorem_proved"] is True, "patched theorem")
    require(patched["no_knob_closed"] is False, "patched no-knob")
    require(patched["true_SM_equivalence_closed"] is False, "patched true eq")
    require(source_identity["Higgs_quartic_implication"]["strict_source_identity_closed_now"] is False, "strict source identity")

    route = independent_hessian["route_status"]
    require(route["same_branch_phifin_lane_locked"] is True, "same branch lane")
    require(route["independent_hessian_quadrature_lane_locked"] is True, "independent lane")
    require(route["current_nonpromotion_verified"] is True, "nonpromotion")
    require(route["independent_hessian_quadrature_source_open"] is True, "independent source")
    require(route["same_branch_phifin_c1_source_emission_open"] is True, "phifin source")
    require(route["source_independent_of_residual_projector_replay_open"] is True, "residual independence")
    reduction = independent_hessian["quadrature_reduction"]
    require(reduction["conditional_source_identity_witness_passes"] is True, "conditional witness")
    require(reduction["formal_measure_support_imported"] is True, "formal measure")
    require(reduction["partial_source_id_packet_rejected_honestly"] is True, "partial reject")
    require(reduction["SelectedFiniteC1SourceIdentityTheorem_open"] is True, "source theorem open")
    require(reduction["selected_hessian_b_source_open"] is True, "hessian b")
    row = independent_hessian["row_execution_support"]
    require(row["selected_basis_slot_coverage_for_72_rows"] is True, "72 slots")
    require(row["sector_coupling_typing_for_u_d_e_nuD"] is True, "sector typing")
    require(row["selected_phase_shift_variation_operators_pre_residual_open"] is True, "phase/shift open")
    require(row["selected_hessian_counterterm_source_open"] is True, "hessian counterterm")
    require(row["first_row_value_exact"] == "4/3", "first row exact")
    require(row["first_row_value_float"] == 1.3333333333333333, "first row float")
    require(row["first_row_independently_executed_now"] is False, "first row provenance")
    require(row["full_72_row_execution_closed"] is False, "72 rows overclosed")
    require(row["physical_PhiFinC1_action_source_closed"] is False, "physical source overclosed")
    require(independent_hessian["Higgs_quartic_implication"]["route_closes_now"] is False, "independent route overclosed")

    h3_locked = higgs_acceptance["H3_locked_state"]
    require(h3_locked["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "acceptance H3")
    require(h3_locked["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "acceptance quartic")
    cutset = higgs_acceptance["two_object_cutset_for_strict_quartic_closure"]
    require(cutset["object_1_source_ownership"]["best_current_name"] == "PhysicalActionOwnsFiniteTraceKernel", "object 1")
    require(cutset["object_1_source_ownership"]["closed_now"] is False, "object 1 closed")
    require(cutset["object_2_Higgs_projection"]["best_current_name"] == "SelectedHiggsNonlinearAmplitudeProjection", "object 2")
    require(cutset["object_2_Higgs_projection"]["closed_now"] is False, "object 2 closed")
    strict = higgs_acceptance["strict_acceptance_result"]
    require(strict["same_source_nonlinear_Phi_fin_variation_emitted"] is False, "nonlinear variation")
    require(strict["selected_quartic_Higgs_Hessian_block_emitted"] is False, "Higgs Hessian")
    require(strict["independent_selected_Higgs_quartic_rows_emitted"] is False, "Higgs rows")
    require(strict["G4_normalization_reused_without_Higgs_target_fit"] is True, "G4 acceptance")
    require(strict["measured_lambda_H_or_mH_v_used_as_selector"] is False, "measured selector")
    require(strict["new_Higgs_specific_parameters"] == 0, "strict params")
    require(strict["strict_Higgs_quartic_closure"] is False, "strict quartic")
    require("promoting the H3 D_E spectral gap or pseudodeterminant to lambda_H" in higgs_acceptance["forbidden_shortcuts"], "shortcut guard")

    fields = strict_template["required_fields"]
    require("selected_nonlinear_action_or_PhiFin_source_id" in fields, "template source")
    require("selected_Higgs_zero_mode_or_amplitude_coordinate" in fields, "template Higgs coordinate")
    require("second_or_fourth_variation_rows" in fields, "template variation rows")
    require("Higgs_projection_certificate" in fields, "template projection")
    require("selector_guardrail" in fields, "template guard")
    require(strict_template["acceptance"]["all_required_fields_present"] is False, "template all fields")
    require(strict_template["acceptance"]["conditional_witness_counts_as_strict_closure"] is False, "conditional closure")
    require(strict_template["acceptance"]["measured_replay_allowed_after_source_emission_only"] is True, "replay policy")

    require(next_work["primary"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNS-FINITE-TRACE-KERNEL", "primary")
    require(next_work["parallel"]["label"] == "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION", "parallel")
    require(next_work["paper_update_section"]["label"] == "CONST-HIGGS-01 / PAPER-INSERT / NONLINEAR-SOURCE-RULE-CUTSET", "paper insert")

    require(cert["status"] == STATUS, "cert status")
    require(cert["selected_Higgs_quadratic_stiffness_kernel_closed"] is True, "cert quadratic")
    require(cert["PhysicalActionOwnsFiniteTraceKernel_closed"] is False, "cert action")
    require(cert["SelectedHiggsNonlinearAmplitudeProjection_closed"] is False, "cert projection")
    require(cert["selected_Higgs_quartic_threshold_kernel_emitted"] is False, "cert quartic")
    require(cert["Higgs_quartic_numeric_value_derived"] is False, "cert numeric")
    require("H4-NONLINEAR-HIGGS" in note and "H5-PHYSICAL-ACTION" in note, "note")

    print("CONST-HIGGS-01 H4 nonlinear Higgs self-interaction source-rule audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
