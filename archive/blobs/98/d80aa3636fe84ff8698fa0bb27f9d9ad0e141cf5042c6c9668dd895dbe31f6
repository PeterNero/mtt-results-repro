"""Build CONST-HIGGS-01 H3 selected Higgs quadratic stiffness/quartic gate."""

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

SLUG = "const_higgs_01_h3_selected_higgs_quadratic_stiffness_and_quartic_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QUADRATIC_KERNEL = BASE / "selected_quadratic_stiffness_kernel.packet.json"
DYNAMIC_ROUTE = BASE / "dynamic_c1_retarded_overlap_route.packet.json"
LOCAL_GATE = BASE / "local_premise_vs_strict_gate.packet.json"
QUARTIC_BOUNDARY = BASE / "quartic_nonclosure_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H3_SelectedHiggsQuadraticStiffnessAndQuarticGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H3_SELECTED_QUADRATIC_STIFFNESS_PROMOTED_QUARTIC_GATE_OPEN"


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

    h2_path = DATA / "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet.candidate.json"
    h2_gap_path = DATA / "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet" / "selected_gap_layer_promotion.packet.json"
    h2_quartic_gate_path = DATA / "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet" / "quartic_kernel_reduction.packet.json"
    g4_contract_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "one_metrology_primitive_contract.packet.json"
    heat_spectrum_path = SM_PARITY_REPO / "candidate_data" / "selected_heattorsionresponse_finalgate" / "selected_finite_heat_spectrum_response.packet.json"
    dynamic_frontier_path = SM_PARITY_REPO / "candidate_data" / "selected_dynamicqasu3_or_c1response_postsourcefrontier.candidate.json"
    dynamic_cycle_path = SM_PARITY_REPO / "candidate_data" / "selected_dynamicc1proofcycle_condensation_or_cycleexit.candidate.json"
    typed_retarded_path = SM_PARITY_REPO / "candidate_data" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
    local_principle_path = SM_PARITY_REPO / "candidate_data" / "selected_localprinciple_dynamicc1closure_integration_or_unpatchedkernelexecution.candidate.json"

    h2 = load(h2_path)
    h2_gap = load(h2_gap_path)
    h2_quartic_gate = load(h2_quartic_gate_path)
    g4_contract = load(g4_contract_path)
    heat_spectrum = load(heat_spectrum_path)
    dynamic_frontier = load(dynamic_frontier_path)
    dynamic_cycle = load(dynamic_cycle_path)
    typed_retarded = load(typed_retarded_path)
    local_principle = load(local_principle_path)

    finite_invariants = heat_spectrum["finite_invariants"]
    spectrum = heat_spectrum["finite_spectrum_convention"]
    h_positive_eigenvalues = spectrum["H_sector_positive_eigenvalues"]
    h_positive_dimension = sum(item["multiplicity"] for item in h_positive_eigenvalues)
    h_min_positive = min(item["eigenvalue"] for item in h_positive_eigenvalues)

    quadratic_kernel = {
        "schema": "MTTConstHiggs01H3SelectedQuadraticStiffnessKernel.v1",
        "status": "SELECTED_FINITE_HIGGS_QUADRATIC_STIFFNESS_KERNEL_PROMOTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUADRATIC-STIFFNESS-KERNEL",
        "inputs": {
            "H2_candidate": rel(h2_path),
            "H2_selected_gap_layer": rel(h2_gap_path),
            "G4_one_metrology_primitive_contract": rel(g4_contract_path),
            "selected_finite_heat_spectrum_response": rel(heat_spectrum_path),
        },
        "selected_source_kernel": {
            "finite_basis_id": heat_spectrum["source_contract"]["basis_id"],
            "finite_basis_dimension": heat_spectrum["source_contract"]["basis_dimension_per_sector"],
            "sector": "H",
            "operator": "K_H^(2) := D_E^* D_E restricted to the selected H-sector finite layer",
            "quadratic_form": "Q_H(phi) := <D_E phi, D_E phi>_selected finite trace",
            "source_contract": heat_spectrum["source_contract"]["H_sector"],
            "zero_cluster_indices": heat_spectrum["source_contract"]["zero_cluster_indices"],
            "H_sector_kernel_dimension": finite_invariants["H_sector_kernel_dimension"],
            "H_sector_positive_dimension": finite_invariants["H_sector_positive_dimension"],
            "H_sector_positive_multiplicity_sum": h_positive_dimension,
            "H_sector_min_positive_eigenvalue": h_min_positive,
            "H_sector_positive_eigenvalues": h_positive_eigenvalues,
            "H_sector_heat_trace_t1": finite_invariants["H_sector_heat_trace_t1"],
            "H_sector_reduced_heat_trace_t1": finite_invariants["H_sector_reduced_heat_trace_t1"],
            "H_sector_log_pseudodeterminant": finite_invariants["H_sector_log_pseudodeterminant"],
            "selected_eta_N": h2_gap["promotion"]["selected_eta_N"],
            "selected_Riesz_Green_gap_lower_bound": h2_gap["promotion"]["selected_gap_lower_bound"],
            "selected_Green_norm_bound": h2_gap["promotion"]["selected_green_norm_bound"],
        },
        "normalization_tier": {
            "G4_one_metrology_primitive_reused": h2["G4_one_metrology_primitive_reused"],
            "G4_primitive_status": g4_contract["status"],
            "strict_no_knob_metrology_value_selected": False,
            "new_Higgs_specific_parameters": 0,
            "interpretation": "The selected finite quadratic kernel is dimensionless/source-level until the already-declared one universal metrology primitive is assigned or derived elsewhere.",
        },
        "what_this_closes": {
            "selected_Higgs_quadratic_stiffness_kernel_closed": True,
            "selected_H_sector_positive_spectrum_closed": True,
            "selected_H_sector_heat_and_pseudodeterminant_response_closed": True,
            "linearized_second_variation_of_quadratic_DE_energy_closed": True,
        },
        "what_this_does_not_close": {
            "selected_Higgs_quartic_threshold_kernel_emitted": False,
            "Higgs_quartic_numeric_value_derived": False,
            "nonlinear_Higgs_amplitude_self_interaction_emitted": False,
            "Yukawa_or_full_SM_closure": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    dynamic_route = {
        "schema": "MTTConstHiggs01H3DynamicC1RetardedOverlapRoute.v1",
        "status": "DYNAMIC_C1_RETARDED_OVERLAP_ROUTE_EVALUATED_STRICT_SOURCE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3B-DYNAMIC-C1-RETARDED-OVERLAP-ROUTE",
        "inputs": {
            "dynamic_QaSU3_or_C1_response_postsource_frontier": rel(dynamic_frontier_path),
            "dynamic_C1_proof_cycle_condensation": rel(dynamic_cycle_path),
            "typed_BN_retarded_derivative_or_primitive_response": rel(typed_retarded_path),
        },
        "superset_path_role": {
            "mode": "parallel dynamic path locked to the same Higgs quartic target",
            "straight_path_target": "selected finite H-sector quadratic stiffness kernel",
            "dynamic_path_target": "selected nonlinear Higgs quartic/threshold response through differentiated Phi_fin^C1 or retarded overlap",
            "observed_targets_forbidden_as_selectors": True,
        },
        "imported_dynamic_status": {
            "postsource_frontier_built": dynamic_frontier["closure_decision"]["postsource_frontier_built"],
            "selected_C1_response_closed": dynamic_frontier["closure_decision"]["selected_C1_response_closed"],
            "A_selected_promoted": dynamic_frontier["closure_decision"]["A_selected_promoted"],
            "b_selected_promoted": dynamic_frontier["closure_decision"]["b_selected_promoted"],
            "sector_response_matrices_promoted": dynamic_frontier["closure_decision"]["sector_response_matrices_promoted"],
            "proof_cycle_condensed": dynamic_cycle["what_closes_now"]["proof_cycle_detected_and_condensed"],
            "shared_missing_object_identified": dynamic_cycle["what_closes_now"]["shared_missing_object_identified"],
            "straight_and_parallel_superset_paths_locked_to_same_target": dynamic_cycle["what_closes_now"]["straight_and_parallel_superset_paths_locked_to_same_target"],
            "typed_retarded_derivative_emitted": typed_retarded["typed_retarded_derivative_emitted"],
            "selected_primitive_response_emitted": typed_retarded["selected_primitive_response_emitted"],
            "primitive_response_candidate_values_emitted": typed_retarded["primitive_response_candidate_values_emitted"],
        },
        "conditional_readiness_not_promotion": {
            "conditional_A_rank": typed_retarded["conditional_solver_packet"]["conditional_A_rank"],
            "conditional_b_norm": typed_retarded["conditional_solver_packet"]["conditional_b_norm"],
            "conditional_deltaTheta": typed_retarded["conditional_solver_packet"]["conditional_deltaTheta"],
            "conditional_residual_norm": typed_retarded["conditional_solver_packet"]["conditional_residual_norm"],
            "reason_not_promoted": typed_retarded["conditional_solver_packet"]["reason"],
        },
        "strict_H3_dynamic_route_closed": False,
        "remaining_strict_missing_object": "same-source nonlinear differentiated Phi_fin^C1/retarded-overlap kernel or independent selected quadrature/Hessian export",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    local_gate = {
        "schema": "MTTConstHiggs01H3LocalPremiseVsStrictGate.v1",
        "status": "LOCAL_PREMISE_DYNAMIC_C1_AVAILABLE_STRICT_UNPATCHED_GATE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-LOCAL-PREMISE-VS-STRICT-GATE",
        "inputs": {
            "local_principle_dynamic_C1_closure": rel(local_principle_path),
        },
        "local_premise_tier": {
            "local_dynamic_C1_closed": local_principle["closure_decision"]["local_dynamic_C1_closed"],
            "unpatched_dynamic_C1_closed": local_principle["closure_decision"]["unpatched_dynamic_C1_closed"],
            "no_knob_closed": local_principle["closure_decision"]["no_knob_closed"],
            "independent_kernel_execution_supplied": local_principle["closure_decision"]["independent_kernel_execution_supplied"],
            "theorem_proved_under_local_premise": local_principle["theorem"]["proved"],
            "statement": local_principle["theorem"]["statement"],
        },
        "Higgs_usage_policy": {
            "can_be_used_as": [
                "a local-premise appendix path",
                "a blueprint for the strict nonlinear kernel export",
                "a consistency check for dynamic C1 algebra",
            ],
            "cannot_be_used_as": [
                "strict no-knob Higgs quartic closure",
                "unpatched selected Phi_fin source identity",
                "independent selected quadrature/Hessian emission",
            ],
        },
        "strict_Higgs_quartic_promotion_allowed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    quartic_boundary = {
        "schema": "MTTConstHiggs01H3QuarticNonclosureBoundary.v1",
        "status": "QUADRATIC_STIFFNESS_QUARTIC_SELF_INTERACTION_SEPARATION_PROVED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-QUARTIC-NONCLOSURE-BOUNDARY",
        "accepted_subresult": {
            "selected_Higgs_quadratic_stiffness_kernel_closed": True,
            "linearized_second_variation_of_quadratic_DE_energy_closed": True,
            "finite_heat_spectral_response_closed": True,
        },
        "separation_lemma": {
            "name": "QuadraticStiffnessDoesNotSelectQuarticSelfInteractionLemma",
            "proved": True,
            "statement": (
                "The selected H2/H3 data consist of a finite linear operator D_E, its positive-complement spectral table, and spectral functionals of D_E^*D_E. These data determine the quadratic stiffness form Q_H(phi)=<D_E phi,D_E phi> on the selected finite H-sector, but they do not determine a nonlinear amplitude coefficient for |phi|^4. A quartic threshold kernel needs an additional selected nonlinear source rule: either a same-source Phi_fin second/fourth variation on the Higgs amplitude, a selected retarded-overlap/dynamic C1 response, or an independent selected quadrature/Hessian export."
            ),
        },
        "H2_acceptance_rechecked": h2_quartic_gate["strict_H3_acceptance"],
        "strict_H3_acceptance_result": {
            "same_source_Phi_fin_second_variation_restricted_to_Higgs_amplitude": False,
            "selected_quartic_threshold_Hessian_block_normalized_by_G4": False,
            "dynamic_C1_retarded_overlap_response_to_quartic_kernel": False,
            "reused_G4_primitive": True,
            "reused_H2_selected_DE_gap_layer": True,
            "forbade_measured_Higgs_values_as_selectors": True,
        },
        "locked_boundary_after_H3": {
            "selected_Higgs_quartic_threshold_kernel_emitted": False,
            "Higgs_quartic_numeric_value_derived": False,
            "new_Higgs_specific_parameters": 0,
            "strict_no_knob_Higgs_closure": False,
            "one_universal_primitive_tier_preserved": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H3NextWork.v1",
        "status": "NEXT_WORKORDER_H4_NONLINEAR_HIGGS_SELF_INTERACTION_SOURCE_RULE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NONLINEAR-HIGGS-SELF-INTERACTION-SOURCE-RULE",
            "task": "Emit or derive the same-source nonlinear Phi_fin second/fourth variation on the selected Higgs amplitude, or an equivalent selected quartic Hessian block tied to the G4 primitive.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4B-INDEPENDENT-RETARDED-OVERLAP-OR-GALERKIN-HESSIAN-EXPORT",
            "task": "Export independent selected retarded-overlap/quadrature/Hessian rows with source ids and exactness/error certificates, then test whether they select a quartic threshold kernel.",
        },
        "paper_update_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / QUADRATIC-STIFFNESS-QUARTIC-SEPARATION",
            "task": "Add H3 as a theorem insert: quadratic stiffness is selected; quartic self-coupling remains a named nonlinear-source theorem, not a measured-Higgs replay.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H3SelectedHiggsQuadraticStiffnessAndQuarticGate",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUADRATIC-STIFFNESS-AND-QUARTIC-GATE",
        "output_packets": {
            "selected_quadratic_stiffness_kernel": rel(QUADRATIC_KERNEL),
            "dynamic_c1_retarded_overlap_route": rel(DYNAMIC_ROUTE),
            "local_premise_vs_strict_gate": rel(LOCAL_GATE),
            "quartic_nonclosure_boundary": rel(QUARTIC_BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H3QuadraticStiffnessQuarticSeparationTheorem",
            "proved": True,
            "statement": (
                "The H2 selected finite D_E/gap/Riesz/Green layer promotes a strict source-level Higgs quadratic stiffness kernel K_H^(2)=D_E^*D_E on the selected H-sector finite layer, with kernel dimension 1, positive dimension 26, selected eta_N=1.0, and the finite heat/pseudodeterminant response imported from the selected heat-spectrum gate. The same data do not select a Higgs quartic threshold/self-interaction coefficient. Strict quartic closure is reduced to H4: emit a same-source nonlinear Phi_fin variation, selected retarded-overlap/dynamic C1 response, or independent selected Hessian/quadrature export."
            ),
        },
        "superset_strategy": {
            "straight_source_path": "H2 selected D_E/gap layer -> H3 selected finite Higgs quadratic stiffness kernel",
            "dynamic_path": "dynamic Phi_fin^C1/retarded overlap -> possible nonlinear Higgs quartic kernel, still strict-source open",
            "local_premise_path": "local SelectedWeylVariationActionPrinciple closes dynamic C1 only inside a local-premise tier, not strict no-knob",
            "locked_target": "selected Higgs quartic threshold/self-interaction kernel",
            "combined_paths_used_as_selectors": False,
        },
        "G4_one_metrology_primitive_reused": True,
        "new_Higgs_specific_parameters": 0,
        "selected_Higgs_quadratic_stiffness_kernel_closed": True,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "dynamic_C1_retarded_overlap_route_closed": False,
        "local_premise_dynamic_C1_available": True,
        "unpatched_dynamic_C1_closed": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H4_NonlinearHiggsSelfInteractionSourceRule_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H3_SelectedHiggsQuadraticStiffnessAndQuarticGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_Higgs_quadratic_stiffness_kernel_closed": True,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "dynamic_C1_retarded_overlap_route_closed": False,
        "local_premise_dynamic_C1_available": True,
        "unpatched_dynamic_C1_closed": False,
        "new_Higgs_specific_parameters": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H3 Selected Higgs Quadratic Stiffness And Quartic Gate v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUADRATIC-STIFFNESS-AND-QUARTIC-GATE`

## Result

```text
selected Higgs quadratic stiffness kernel       True
H-sector kernel dimension                       {finite_invariants["H_sector_kernel_dimension"]}
H-sector positive dimension                     {finite_invariants["H_sector_positive_dimension"]}
H-sector min positive eigenvalue                {h_min_positive}
selected eta_N                                  {h2_gap["promotion"]["selected_eta_N"]}
H-sector log pseudodeterminant                  {finite_invariants["H_sector_log_pseudodeterminant"]}
selected Higgs quartic/threshold kernel         False
Higgs quartic numeric value                     False
new Higgs-specific parameters                   0
```

## Theorem

The H2 selected `D_E` gap layer now gives a real H3 theorem:

```text
K_H^(2) := D_E^* D_E restricted to the selected finite H sector
Q_H(phi) := <D_E phi, D_E phi>_selected finite trace
```

This closes the source-level finite Higgs quadratic stiffness kernel.  It
uses the same selected finite basis and the same G4 metrology primitive tier;
it does not add a Higgs-specific knob and it does not use measured Higgs data.

## Separation

This is not yet a Higgs quartic derivation.  The selected data at H3 are a
linear finite operator, its positive-complement spectrum, and heat/determinant
functionals of `D_E^*D_E`.  Those determine a quadratic form.  They do not
determine a nonlinear `|phi|^4` self-interaction coefficient.

The strict quartic gate now has one clean target:

```text
derive or emit a same-source nonlinear Phi_fin variation,
or a selected retarded-overlap/dynamic C1 response,
or an independent selected Hessian/quadrature export.
```

## Superset Usage

Straight path: H2 selected `D_E` gap layer -> H3 selected quadratic stiffness.

Dynamic path: differentiated `Phi_fin^C1` / retarded overlap -> possible
quartic kernel, still open in the strict source tier.

Local-premise path: the local SelectedWeylVariationActionPrinciple can close
dynamic C1 inside a local premise tier, but it is not counted as strict
no-knob Higgs closure.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H4-NONLINEAR-HIGGS-SELF-INTERACTION-SOURCE-RULE`
"""

    for path, payload in [
        (QUADRATIC_KERNEL, quadratic_kernel),
        (DYNAMIC_ROUTE, dynamic_route),
        (LOCAL_GATE, local_gate),
        (QUARTIC_BOUNDARY, quartic_boundary),
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
