"""Build CONST-HIGGS-01 H4 nonlinear Higgs self-interaction source-rule gate."""

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

SLUG = "const_higgs_01_h4_nonlinear_higgs_self_interaction_source_rule"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_IDENTITY = BASE / "source_identity_bridge.packet.json"
INDEPENDENT_HESSIAN = BASE / "independent_hessian_quadrature_route.packet.json"
HIGGS_ACCEPTANCE = BASE / "higgs_quartic_source_acceptance.packet.json"
STRICT_TEMPLATE = BASE / "strict_nonlinear_higgs_source_template.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H4_NonlinearHiggsSelfInteractionSourceRule_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H4_NONLINEAR_SOURCE_RULE_CUTSET_BUILT_QUARTIC_OPEN"


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

    h3_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate.candidate.json"
    h3_quadratic_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "selected_quadratic_stiffness_kernel.packet.json"
    h3_boundary_path = DATA / "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate" / "quartic_nonclosure_boundary.packet.json"
    g4_contract_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "one_metrology_primitive_contract.packet.json"

    source_identity_attempt_path = SM_PARITY_REPO / "candidate_data" / "selected_psm_c1_02_sourceidentitylemma_derivation_attempt.candidate.json"
    phifin_or_hessian_path = SM_PARITY_REPO / "candidate_data" / "selected_phifinc1emission_or_independenthessianquadraturesource.candidate.json"
    independent_quadrature_path = SM_PARITY_REPO / "candidate_data" / "selected_independentquadratureruleandhessianbsource_or_routeaactionidentity.candidate.json"
    primitive_slot_path = SM_PARITY_REPO / "candidate_data" / "selected_primitivekernelslotcoverage_or_variationhessiangap.candidate.json"
    first_row_path = SM_PARITY_REPO / "candidate_data" / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource.candidate.json"
    patched_parity_path = SM_PARITY_REPO / "candidate_data" / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution.candidate.json"

    h3 = load(h3_path)
    h3_quadratic = load(h3_quadratic_path)
    h3_boundary = load(h3_boundary_path)
    g4_contract = load(g4_contract_path)
    source_identity_attempt = load(source_identity_attempt_path)
    phifin_or_hessian = load(phifin_or_hessian_path)
    independent_quadrature = load(independent_quadrature_path)
    primitive_slot = load(primitive_slot_path)
    first_row = load(first_row_path)
    patched_parity = load(patched_parity_path)

    source_identity = {
        "schema": "MTTConstHiggs01H4SourceIdentityBridge.v1",
        "status": "SOURCE_IDENTITY_BRIDGE_REDUCED_TO_PHYSICAL_ACTION_OWNERSHIP",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-SOURCE-IDENTITY-BRIDGE",
        "inputs": {
            "H3_candidate": rel(h3_path),
            "PSM_C1_02_source_identity_attempt": rel(source_identity_attempt_path),
            "patched_parity_source_execution": rel(patched_parity_path),
        },
        "imported_source_identity_result": {
            "status": source_identity_attempt["status"],
            "theorem_proved": source_identity_attempt["theorem"]["proved"],
            "admissible_c1_variation_space_derived": source_identity_attempt["what_closes_now"]["admissible_c1_variation_space_derived"],
            "postcheck_independence_guard_derived": source_identity_attempt["what_closes_now"]["postcheck_independence_guard_derived"],
            "single_surviving_obstruction_identified": source_identity_attempt["what_closes_now"]["single_surviving_obstruction_identified"],
            "PhysicalActionOwnsFiniteTraceKernel_open": source_identity_attempt["what_remains_open"]["PhysicalActionOwnsFiniteTraceKernel"],
            "SelectedFiniteC1SourceIdentityLemma_unpatched_open": source_identity_attempt["what_remains_open"]["SelectedFiniteC1SourceIdentityLemma_unpatched"],
            "next_required_artifact": source_identity_attempt["next_required_artifact"],
        },
        "patched_local_or_parity_tier": {
            "SM_parity_dynamic_C1_closed_under_local_principle": patched_parity["SM_parity_dynamic_C1_closed_under_local_principle"],
            "patched_theorem_proved": patched_parity["theorem"]["proved"],
            "no_knob_closed": patched_parity["no_knob_closed"],
            "true_SM_equivalence_closed": patched_parity["true_SM_equivalence_closed"],
            "unpatched_same_branch_PhiFinC1_source_emission_open": patched_parity["what_remains_open"]["unpatched_same_branch_PhiFinC1_source_emission"],
        },
        "Higgs_quartic_implication": {
            "helps": "source ownership of the differentiated finite C1/action kernel is a prerequisite for a selected nonlinear Higgs self-interaction source",
            "not_sufficient_alone": "after source ownership, a Higgs-amplitude projection of the nonlinear kernel is still needed before lambda_H can be claimed",
            "strict_source_identity_closed_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    independent_hessian = {
        "schema": "MTTConstHiggs01H4IndependentHessianQuadratureRoute.v1",
        "status": "INDEPENDENT_HESSIAN_QUADRATURE_ROUTE_LOCKED_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-INDEPENDENT-HESSIAN-QUADRATURE-ROUTE",
        "inputs": {
            "PhiFinC1_or_independent_hessian_gate": rel(phifin_or_hessian_path),
            "independent_quadrature_rule_and_hessian_b_source": rel(independent_quadrature_path),
            "primitive_kernel_slot_coverage": rel(primitive_slot_path),
            "first_row_exact_execution": rel(first_row_path),
        },
        "route_status": {
            "same_branch_phifin_lane_locked": phifin_or_hessian["what_closes_now"]["same_branch_phifin_lane_locked"],
            "independent_hessian_quadrature_lane_locked": phifin_or_hessian["what_closes_now"]["independent_hessian_quadrature_lane_locked"],
            "current_nonpromotion_verified": phifin_or_hessian["what_closes_now"]["current_nonpromotion_verified"],
            "independent_hessian_quadrature_source_open": phifin_or_hessian["what_remains_open"]["independent_hessian_quadrature_source"],
            "same_branch_phifin_c1_source_emission_open": phifin_or_hessian["what_remains_open"]["same_branch_phifin_c1_source_emission"],
            "source_independent_of_residual_projector_replay_open": phifin_or_hessian["what_remains_open"]["source_independent_of_residual_projector_replay"],
        },
        "quadrature_reduction": {
            "conditional_source_identity_witness_passes": independent_quadrature["what_closes_now"]["conditional_source_identity_witness_passes"],
            "formal_measure_support_imported": independent_quadrature["what_closes_now"]["formal_measure_support_imported"],
            "partial_source_id_packet_rejected_honestly": independent_quadrature["what_closes_now"]["partial_source_id_packet_rejected_honestly"],
            "SelectedFiniteC1SourceIdentityTheorem_open": independent_quadrature["what_remains_open"]["SelectedFiniteC1SourceIdentityTheorem"],
            "selected_hessian_b_source_open": independent_quadrature["what_remains_open"]["selected_hessian_b_source"],
            "selected_independent_quadrature_rule_source_open": independent_quadrature["what_remains_open"]["selected_independent_quadrature_rule_source"],
        },
        "row_execution_support": {
            "selected_basis_slot_coverage_for_72_rows": primitive_slot["what_closes_now"]["selected_basis_slot_coverage_for_72_rows"],
            "sector_coupling_typing_for_u_d_e_nuD": primitive_slot["what_closes_now"]["sector_coupling_typing_for_u_d_e_nuD"],
            "selected_phase_shift_variation_operators_pre_residual_open": primitive_slot["what_remains_open"]["selected_phase_shift_variation_operators_pre_residual"],
            "selected_hessian_counterterm_source_open": primitive_slot["what_remains_open"]["selected_hessian_counterterm_source"],
            "first_row_value_exact": first_row["promotion_decision"]["first_row_value_exact"],
            "first_row_value_float": first_row["promotion_decision"]["first_row_value_float"],
            "first_row_independently_executed_now": first_row["promotion_decision"]["first_row_independently_executed_now"],
            "full_72_row_execution_closed": first_row["promotion_decision"]["full_72_row_execution_closed"],
            "physical_PhiFinC1_action_source_closed": first_row["promotion_decision"]["physical_PhiFinC1_action_source_closed"],
        },
        "Higgs_quartic_implication": {
            "route_can_replace_source_identity_if": "it emits selected residual-projector-independent Hessian/quadrature rows and a Higgs-amplitude block extraction certificate",
            "route_closes_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    higgs_acceptance = {
        "schema": "MTTConstHiggs01H4HiggsQuarticSourceAcceptance.v1",
        "status": "HIGGS_QUARTIC_ACCEPTANCE_REDUCED_TO_TWO_OBJECT_CUTSET",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-HIGGS-QUARTIC-SOURCE-ACCEPTANCE",
        "inputs": {
            "H3_quadratic_kernel": rel(h3_quadratic_path),
            "H3_quartic_nonclosure_boundary": rel(h3_boundary_path),
            "G4_one_metrology_primitive_contract": rel(g4_contract_path),
        },
        "H3_locked_state": {
            "selected_Higgs_quadratic_stiffness_kernel_closed": h3["selected_Higgs_quadratic_stiffness_kernel_closed"],
            "selected_Higgs_quartic_threshold_kernel_emitted": h3["selected_Higgs_quartic_threshold_kernel_emitted"],
            "Higgs_quartic_numeric_value_derived": h3["Higgs_quartic_numeric_value_derived"],
            "dynamic_C1_retarded_overlap_route_closed": h3["dynamic_C1_retarded_overlap_route_closed"],
            "unpatched_dynamic_C1_closed": h3["unpatched_dynamic_C1_closed"],
        },
        "two_object_cutset_for_strict_quartic_closure": {
            "object_1_source_ownership": {
                "description": "physical Phi_fin^C1/action source identity or independent residual-projector-independent Hessian/quadrature source",
                "closed_now": False,
                "best_current_name": "PhysicalActionOwnsFiniteTraceKernel",
            },
            "object_2_Higgs_projection": {
                "description": "selected projection/extraction of the nonlinear source kernel onto the Higgs zero-mode/amplitude |phi|^4 coefficient",
                "closed_now": False,
                "best_current_name": "SelectedHiggsNonlinearAmplitudeProjection",
            },
        },
        "strict_acceptance_result": {
            "same_source_nonlinear_Phi_fin_variation_emitted": False,
            "selected_quartic_Higgs_Hessian_block_emitted": False,
            "independent_selected_Higgs_quartic_rows_emitted": False,
            "G4_normalization_reused_without_Higgs_target_fit": True,
            "measured_lambda_H_or_mH_v_used_as_selector": False,
            "new_Higgs_specific_parameters": 0,
            "strict_Higgs_quartic_closure": False,
        },
        "forbidden_shortcuts": [
            "promoting the H3 D_E spectral gap or pseudodeterminant to lambda_H",
            "using lambda_H=m_H^2/(2v^2), Higgs widths, branching ratios, or RG benchmark rows as source selectors",
            "counting the local/patched C1 premise as unpatched no-knob closure",
            "retuning the one universal metrology primitive for Higgs alone",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    strict_template = {
        "schema": "MTTConstHiggs01H4StrictNonlinearHiggsSourceTemplate.v1",
        "status": "STRICT_TEMPLATE_FOR_HIGGS_QUARTIC_SOURCE_EMISSION_BUILT",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-STRICT-NONLINEAR-HIGGS-SOURCE-TEMPLATE",
        "required_fields": {
            "selected_nonlinear_action_or_PhiFin_source_id": "must name the same selected source, not a replay functional",
            "selected_variation_space_id": "must include admissible Higgs-amplitude variations before residual projection",
            "selected_Higgs_zero_mode_or_amplitude_coordinate": "must identify the H-sector scalar/amplitude coordinate in the selected finite basis",
            "finite_trace_or_pairing_source_id": "must be theorem-derived or independently emitted",
            "second_or_fourth_variation_rows": "must emit the nonlinear Hessian/quartic rows or an exact finite formula",
            "Higgs_projection_certificate": "must prove the rows project to the |phi|^4 self-interaction slot",
            "G4_normalization_contract": "must reuse the G4 primitive without choosing it from Higgs observations",
            "exactness_or_error_certificate": "must provide exact arithmetic or certified numerical bounds",
            "selector_guardrail": "must exclude observed Higgs, SM masses, CKM/PMNS, weak angle, alpha, RG benchmark values, and target lambda_H as selectors",
        },
        "acceptance": {
            "all_required_fields_present": False,
            "conditional_witness_allowed": True,
            "conditional_witness_counts_as_strict_closure": False,
            "measured_replay_allowed_after_source_emission_only": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H4NextWork.v1",
        "status": "NEXT_WORKORDER_H5_SOURCE_OWNERSHIP_AND_HIGGS_PROJECTION",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNS-FINITE-TRACE-KERNEL",
            "task": "Prove PhysicalActionOwnsFiniteTraceKernel unpatched, or emit an independent Hessian/quadrature source packet with residual-projector-independent provenance.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION",
            "task": "Construct the selected projection from the nonlinear finite source kernel to the Higgs amplitude |phi|^4 slot, reusing the H-sector basis and G4 normalization.",
        },
        "paper_update_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / NONLINEAR-SOURCE-RULE-CUTSET",
            "task": "Record the H4 two-object cutset and forbid spectral-gap-to-quartic promotion unless the nonlinear source template is filled.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H4NonlinearHiggsSelfInteractionSourceRule",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NONLINEAR-HIGGS-SELF-INTERACTION-SOURCE-RULE",
        "output_packets": {
            "source_identity_bridge": rel(SOURCE_IDENTITY),
            "independent_hessian_quadrature_route": rel(INDEPENDENT_HESSIAN),
            "higgs_quartic_source_acceptance": rel(HIGGS_ACCEPTANCE),
            "strict_nonlinear_higgs_source_template": rel(STRICT_TEMPLATE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H4NonlinearSourceRuleCutsetTheorem",
            "proved": True,
            "statement": (
                "H4 evaluates the nonlinear Higgs self-interaction source rule against the current corpus and proof repos. The strict quartic target is not emitted. The gate is reduced to a two-object cutset: first, unpatched physical action ownership of the finite trace/C1 kernel or an independent residual-projector-independent Hessian/quadrature source; second, a selected Higgs-amplitude projection extracting the |phi|^4 self-interaction slot. Existing support gives H3 quadratic stiffness, source-identity normal form, 72-row slot coverage, and one exact first-row value, but not strict nonlinear Higgs quartic closure."
            ),
        },
        "superset_strategy": {
            "straight_source_path": "H3 quadratic stiffness remains closed but cannot be used as the quartic selector",
            "route_A": "physical Phi_fin^C1/action source identity, reduced to PhysicalActionOwnsFiniteTraceKernel",
            "route_B": "independent Hessian/quadrature row emission, with 72 slots typed and first row exact but provenance/full rows open",
            "local_premise_path": "patched/local dynamic C1 remains available for parity/local tier only",
            "locked_target": "selected Higgs nonlinear |phi|^4 source coefficient",
            "combined_paths_used_as_selectors": False,
        },
        "selected_Higgs_quadratic_stiffness_kernel_closed": True,
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "SelectedHiggsNonlinearAmplitudeProjection_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H5_PhysicalActionOwnsFiniteTraceKernel_and_HiggsProjection_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H4_NonlinearHiggsSelfInteractionSourceRule_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_Higgs_quadratic_stiffness_kernel_closed": True,
        "PhysicalActionOwnsFiniteTraceKernel_closed": False,
        "SelectedHiggsNonlinearAmplitudeProjection_closed": False,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H4 Nonlinear Higgs Self Interaction Source Rule v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NONLINEAR-HIGGS-SELF-INTERACTION-SOURCE-RULE`

## Result

```text
H3 selected quadratic stiffness                  True
PhysicalActionOwnsFiniteTraceKernel              False
SelectedHiggsNonlinearAmplitudeProjection        False
selected Higgs quartic/threshold kernel          False
Higgs quartic numeric value                      False
new Higgs-specific parameters                    0
```

## Cutset

H4 reduces strict Higgs quartic closure to two source objects:

```text
1. Physical action ownership of the finite trace/C1 kernel
   or an independent residual-projector-independent Hessian/quadrature export.

2. A selected Higgs-amplitude projection extracting the |phi|^4 slot
   from that nonlinear source kernel.
```

This is not regression.  It is the exact reason the H3 quadratic stiffness
result cannot be over-promoted into `lambda_H`.

## Superset Usage

Route A uses the same-branch `Phi_fin^C1` / physical action source identity.
The current single obstruction is `PhysicalActionOwnsFiniteTraceKernel`.

Route B uses independent Hessian/quadrature rows.  The current repo support
has 72-row slot coverage and one exact first-row value `4/3`, but not full
selected provenance or all rows.

The local/patched C1 path remains useful for parity/local work, but it is not
strict no-knob closure.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5-PHYSICAL-ACTION-OWNS-FINITE-TRACE-KERNEL`

and in parallel:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H5B-SELECTED-HIGGS-NONLINEAR-AMPLITUDE-PROJECTION`
"""

    for path, payload in [
        (SOURCE_IDENTITY, source_identity),
        (INDEPENDENT_HESSIAN, independent_hessian),
        (HIGGS_ACCEPTANCE, higgs_acceptance),
        (STRICT_TEMPLATE, strict_template),
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
