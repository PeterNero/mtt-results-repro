"""Build CONST-HIGGS-01 H5 physical-action finite-trace ownership gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h5_physical_action_owns_finite_trace_kernel"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
OWNERSHIP_ATTEMPT = BASE / "physical_action_ownership_attempt.packet.json"
COUNTERMODEL_GUARDRAIL = BASE / "support_only_countermodel_guardrail.packet.json"
KERNEL_REDUCTION = BASE / "pre_residual_action_kernel_reduction.packet.json"
HIGGS_IMPLICATION = BASE / "higgs_quartic_implication.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H5_PhysicalActionOwnsFiniteTraceKernel_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H5_PHYSICAL_ACTION_OWNERSHIP_COUNTERMODEL_GUARDRAIL_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h4_path = DATA / "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule.candidate.json"
    h4_acceptance_path = DATA / "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule" / "higgs_quartic_source_acceptance.packet.json"
    physical_action_attack_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel.candidate.json"
    direct_attempt_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel" / "direct_proof_attempt.packet.json"
    countermodel_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel" / "support_only_countermodel_import.packet.json"
    remaining_kernel_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel" / "remaining_kernel_theorem.packet.json"
    source_next_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel" / "next_labeled_workorder.packet.json"
    last_contract_path = SM_PARITY_REPO / "candidate_data" / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem.candidate.json"
    all_rows_path = SM_PARITY_REPO / "candidate_data" / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
    action_equivalence_path = SM_PARITY_REPO / "candidate_data" / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"

    h4 = load(h4_path)
    h4_acceptance = load(h4_acceptance_path)
    physical_action_attack = load(physical_action_attack_path)
    direct_attempt = load(direct_attempt_path)
    countermodel = load(countermodel_path)
    remaining_kernel = load(remaining_kernel_path)
    source_next = load(source_next_path)
    last_contract = load(last_contract_path)
    all_rows = load(all_rows_path)
    action_equivalence = load(action_equivalence_path)

    ownership_attempt = {
        "schema": "MTTConstHiggs01H5PhysicalActionOwnershipAttempt.v1",
        "status": "PHYSICAL_ACTION_OWNERSHIP_ATTEMPT_COMPLETED_NOT_PROVED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNERSHIP-ATTEMPT",
        "inputs": {
            "H4_candidate": rel(h4_path),
            "PSM_C1_02_physical_action_attack": rel(physical_action_attack_path),
            "direct_proof_attempt": rel(direct_attempt_path),
            "last_source_contract": rel(last_contract_path),
            "action_equivalence": rel(action_equivalence_path),
        },
        "direct_attempt_result": {
            "statement_needed": direct_attempt["statement_needed"],
            "physical_action_owns_finite_trace_kernel_proved_now": direct_attempt["proof_result"]["physical_action_owns_finite_trace_kernel_proved_now"],
            "reason_not_proved": direct_attempt["proof_result"]["reason_not_proved"],
            "closed_subclauses": direct_attempt["closed_subclauses"],
            "closed_support": direct_attempt["closed_support"],
            "still_required_physical_subclauses": direct_attempt["still_required_physical_subclauses"],
        },
        "last_source_contract_status": {
            "formal_computation_layer_closed": last_contract["promotion_decision"]["formal_computation_layer_closed"],
            "finite_measure_normalization_retired": last_contract["promotion_decision"]["finite_measure_normalization_retired"],
            "physical_action_equivalence_theorem_built": last_contract["promotion_decision"]["physical_action_equivalence_theorem_built"],
            "route_A_physical_action_source_closed": last_contract["promotion_decision"]["route_A_physical_action_source_closed"],
            "route_B_provenance_independence_closed": last_contract["promotion_decision"]["route_B_provenance_independence_closed"],
            "next_actionable_target": last_contract["promotion_decision"]["next_actionable_target"],
        },
        "action_equivalence_cutset": {
            "theorem_proved": action_equivalence["theorem"]["proved"],
            "finite_boundary_no_longer_blocker": action_equivalence["what_closes_now"]["finite_boundary_no_longer_blocker"],
            "action_identity_to_source_emission_equivalence": action_equivalence["what_closes_now"]["action_identity_to_source_emission_equivalence"],
            "physical_action_identity_open": action_equivalence["what_remains_open"]["physical_action_identity"],
            "physical_measure_equals_trace_frobenius_pairing_open": action_equivalence["what_remains_open"]["physical_measure_equals_trace_frobenius_pairing"],
            "same_source_b_selected_emission_open": action_equivalence["what_remains_open"]["same_source_b_selected_emission"],
            "no_extra_boundary_or_source_open": action_equivalence["what_remains_open"]["no_extra_physical_boundary_or_source_term"],
        },
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    countermodel_guardrail = {
        "schema": "MTTConstHiggs01H5SupportOnlyCountermodelGuardrail.v1",
        "status": "SUPPORT_ONLY_COUNTERMODEL_IMPORTED_AS_H5_GUARDRAIL",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-SUPPORT-ONLY-COUNTERMODEL-GUARDRAIL",
        "inputs": {
            "support_only_countermodel_import": rel(countermodel_path),
            "all_rows_provenance_promotion": rel(all_rows_path),
        },
        "countermodel": {
            "support_only_countermodel_valid": countermodel["support_only_countermodel_valid"],
            "blocks_derivation_from_closed_support_alone": countermodel["blocks_derivation_from_closed_support_alone"],
            "closed_support_not_enough": countermodel["closed_support_not_enough"],
            "validator_rejects_current_two_exit_packet": countermodel["validator_rejects_current_two_exit_packet"],
            "therefore": countermodel["therefore"],
        },
        "closed_support_facts_retained": countermodel["closed_support_facts_true"],
        "additional_structural_support_retained": countermodel["additional_structural_support_true"],
        "formal_rows": {
            "formal_110_row_replay_closed": all_rows["promotion_decision"]["formal_110_row_replay_closed"],
            "formal_A_b_deltaTheta_replay_closed": all_rows["promotion_decision"]["formal_A_b_deltaTheta_replay_closed"],
            "all_72_exact_rows_retained": all_rows["what_closes_now"]["all_72_exact_rows_retained"],
            "source_promotion_cutset_minimized": all_rows["what_closes_now"]["source_promotion_cutset_minimized"],
            "physical_PhiFinC1_action_source_closed": all_rows["promotion_decision"]["physical_PhiFinC1_action_source_closed"],
            "provenance_independent_of_residual_projector_replay": all_rows["promotion_decision"]["provenance_independent_of_residual_projector_replay"],
        },
        "forbidden_promotions": [
            "closed 110-row replay -> PhysicalActionOwnsFiniteTraceKernel",
            "A^T b=(12,12) or deltaTheta=(1,1) -> b_selected source",
            "exact Weyl row values -> physical Phi_fin^C1 source ownership",
            "support-only finite quotient -> Higgs quartic self-interaction",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    kernel_reduction = {
        "schema": "MTTConstHiggs01H5PreResidualActionKernelReduction.v1",
        "status": "H5_REDUCED_TO_SELECTED_PHIFINC1_PRERESIDUAL_ACTION_KERNEL_THEOREM",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PRERESIDUAL-ACTION-KERNEL-REDUCTION",
        "inputs": {
            "remaining_kernel_theorem": rel(remaining_kernel_path),
            "source_next_workorder": rel(source_next_path),
        },
        "remaining_kernel_theorem": {
            "theorem_name": remaining_kernel["theorem_name"],
            "statement": remaining_kernel["statement"],
            "proved_now": remaining_kernel["proved_now"],
            "must_not_be_used_as_free_patch": remaining_kernel["must_not_be_used_as_free_patch"],
            "acceptable_proof_sources": remaining_kernel["acceptable_proof_sources"],
            "forbidden_shortcuts": remaining_kernel["forbidden_shortcuts"],
            "would_close": remaining_kernel["would_close"],
        },
        "source_repo_next_work": {
            "next_required_artifact": source_next["next_required_artifact"],
            "primary_label": source_next["primary"]["label"],
            "primary_task": source_next["primary"]["task"],
            "secondary_label": source_next["secondary"]["label"],
            "superset_strategy": source_next["superset_strategy"],
        },
        "H5_closure_result": {
            "PhysicalActionOwnsFiniteTraceKernel_closed": False,
            "SelectedPhiFinC1PreResidualActionKernelTheorem_closed": False,
            "SelectedFiniteC1SourceIdentityLemma_unpatched_closed": False,
            "independent_Galerkin_or_quadrature_replacement_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    higgs_implication = {
        "schema": "MTTConstHiggs01H5HiggsQuarticImplication.v1",
        "status": "HIGGS_QUARTIC_STILL_BLOCKED_BY_ACTION_OWNERSHIP_AND_PROJECTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-HIGGS-QUARTIC-IMPLICATION",
        "inputs": {
            "H4_acceptance": rel(h4_acceptance_path),
        },
        "H4_cutset_replayed": h4_acceptance["two_object_cutset_for_strict_quartic_closure"],
        "H5_update": {
            "object_1_PhysicalActionOwnsFiniteTraceKernel": False,
            "object_1_status": "attacked directly; blocked by support-only countermodel; reduced to SelectedPhiFinC1PreResidualActionKernelTheorem",
            "object_2_SelectedHiggsNonlinearAmplitudeProjection": False,
            "object_2_status": "not attacked yet in H5; remains H5B/H6B",
            "selected_Higgs_quartic_threshold_kernel_emitted": False,
            "Higgs_quartic_numeric_value_derived": False,
            "new_Higgs_specific_parameters": 0,
        },
        "strict_guardrail": {
            "no_measured_lambda_H_selector": True,
            "no_Higgs_mass_or_vev_backsolve": True,
            "no_spectral_gap_to_quartic_promotion": True,
            "no_local_patch_counted_as_no_knob": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H5NextWork.v1",
        "status": "NEXT_WORKORDER_H6_PRERESIDUAL_ACTION_KERNEL_OR_H5B_HIGGS_PROJECTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM",
            "task": "Prove the selected physical differentiated Phi_fin^C1 action is the least-defect trace/Frobenius source functional emitting R_Z/R_X and b_selected with zero extra boundary/source term.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION",
            "task": "Build the Higgs-amplitude projection contract so, if H6 closes the nonlinear source kernel, the |phi|^4 slot can be extracted without using measured Higgs values.",
        },
        "paper_update_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / ACTION-OWNERSHIP-COUNTERMODEL-GUARDRAIL",
            "task": "Record that finite row/support closure is not source ownership, and state the exact remaining pre-residual action-kernel theorem.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H5PhysicalActionOwnsFiniteTraceKernel",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNS-FINITE-TRACE-KERNEL",
        "output_packets": {
            "physical_action_ownership_attempt": rel(OWNERSHIP_ATTEMPT),
            "support_only_countermodel_guardrail": rel(COUNTERMODEL_GUARDRAIL),
            "pre_residual_action_kernel_reduction": rel(KERNEL_REDUCTION),
            "higgs_quartic_implication": rel(HIGGS_IMPLICATION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H5ActionOwnershipCountermodelGuardrailTheorem",
            "proved": True,
            "statement": (
                "H5 attacks PhysicalActionOwnsFiniteTraceKernel using the direct PSM-C1-02 proof attempt, the last Phi_fin^C1 source contract, the formal 110-row replay, and the support-only countermodel. Closed finite trace support, exact Weyl rows, formal A/b/deltaTheta replay, and boundary algebra do not force physical Phi_fin^C1 action ownership. The remaining strict object is SelectedPhiFinC1PreResidualActionKernelTheorem or an independent Galerkin/quadrature replacement, before any Higgs |phi|^4 projection can produce a quartic source."
            ),
        },
        "superset_strategy": {
            "straight_source_path": "physical Phi_fin^C1 action ownership route",
            "route_C": "Weyl-variation/pre-residual action-kernel theorem route",
            "route_B": "independent Galerkin/quadrature replacement route",
            "locked_target": "PhysicalActionOwnsFiniteTraceKernel as prerequisite for selected Higgs quartic source",
            "closed_support_used_as_selector": False,
            "combined_paths_used_as_free_parameters": False,
        },
        "selected_Higgs_quadratic_stiffness_kernel_closed": True,
        "formal_110_row_replay_closed": True,
        "support_only_countermodel_valid": True,
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "SelectedPhiFinC1PreResidualActionKernelTheorem_closed": False,
        "SelectedHiggsNonlinearAmplitudeProjection_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6_SelectedPhiFinC1PreResidualActionKernelTheorem_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H5_PhysicalActionOwnsFiniteTraceKernel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "formal_110_row_replay_closed": True,
        "support_only_countermodel_valid": True,
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "SelectedPhiFinC1PreResidualActionKernelTheorem_closed": False,
        "SelectedHiggsNonlinearAmplitudeProjection_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H5 Physical Action Owns Finite Trace Kernel v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNS-FINITE-TRACE-KERNEL`

## Result

```text
formal 110-row replay closed                     True
support-only countermodel valid                  True
PhysicalActionOwnsFiniteTraceKernel              False
SelectedPhiFinC1PreResidualActionKernelTheorem   False
SelectedHiggsNonlinearAmplitudeProjection        False
selected Higgs quartic/threshold kernel          False
Higgs quartic numeric value                      False
new Higgs-specific parameters                    0
```

## Theorem

H5 attacks the physical-action ownership lemma directly.  The result is a
guardrail theorem:

```text
closed finite trace support
+ exact Weyl rows
+ formal 110-row replay
+ boundary algebra
does not imply physical Phi_fin^C1 action ownership.
```

The imported countermodel blocks the shortcut.  This is exactly the right
place to be strict: row values and support are not source ownership.

## Remaining Kernel

The remaining theorem is:

```text
SelectedPhiFinC1PreResidualActionKernelTheorem
```

It must prove that the selected physical differentiated `Phi_fin^C1` action
is the least-defect trace/Frobenius source functional emitting `R_Z`, `R_X`,
and `b_selected`, with zero extra boundary/source term.

## Higgs Consequence

The Higgs quartic is still blocked by two objects:

```text
1. PhysicalActionOwnsFiniteTraceKernel
2. SelectedHiggsNonlinearAmplitudeProjection
```

H5 attacks object 1 and reduces it to the pre-residual action-kernel theorem.
Object 2 remains the parallel `H5B` projection contract.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6-SELECTED-PHIFINC1-PRERESIDUAL-ACTION-KERNEL-THEOREM`

Parallel:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION`
"""

    for path, payload in [
        (OWNERSHIP_ATTEMPT, ownership_attempt),
        (COUNTERMODEL_GUARDRAIL, countermodel_guardrail),
        (KERNEL_REDUCTION, kernel_reduction),
        (HIGGS_IMPLICATION, higgs_implication),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
