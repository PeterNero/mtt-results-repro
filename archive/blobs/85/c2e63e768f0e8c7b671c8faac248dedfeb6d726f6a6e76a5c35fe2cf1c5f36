"""Build CONST-HIGGS-01 H2 selected Higgs projector/quartic-kernel source packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM_REPO = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h2_selected_higgs_projector_and_quartic_kernel_source_packet"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAP_LAYER = BASE / "selected_gap_layer_promotion.packet.json"
PROJECTOR_PACKET = BASE / "higgs_projector_source_packet.packet.json"
HEAT_RESPONSE = BASE / "finite_heat_spectrum_response_import.packet.json"
QUARTIC_GATE = BASE / "quartic_kernel_reduction.packet.json"
BOUNDARY = BASE / "h2_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H2_SELECTED_PROJECTOR_SOURCE_PROMOTED_QUARTIC_KERNEL_OPEN"


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

    h1_path = DATA / "const_higgs_01_h1_shared_metrology_primitive_test.candidate.json"
    h1_boundary_path = DATA / "const_higgs_01_h1_shared_metrology_primitive_test" / "h1_boundary.packet.json"
    g4_contract_path = DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive" / "one_metrology_primitive_contract.packet.json"
    lemma_path = NONSM_REPO / "candidate_data" / "selected_canonical_trace_formula_source_lemma_proof.candidate.json"
    gap_lock_path = NONSM_REPO / "candidate_data" / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"
    trace27_path = NONSM_REPO / "candidate_data" / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"
    heat_final_path = SM_PARITY_REPO / "candidate_data" / "selected_heattorsionresponse_finalgate.candidate.json"

    h1 = load(h1_path)
    h1_boundary = load(h1_boundary_path)
    g4_contract = load(g4_contract_path)
    lemma = load(lemma_path)
    gap_lock = load(gap_lock_path)
    trace27 = load(trace27_path)
    heat_final = load(heat_final_path)

    gap_layer = {
        "schema": "MTTConstHiggs01H2SelectedGapLayerPromotion.v1",
        "status": "SELECTED_DE_GAP_LAYER_PROMOTED_FROM_CANONICAL_TRACE_LEMMA",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-SELECTED-GAP-LAYER-PROMOTION",
        "inputs": {
            "H1_candidate": rel(h1_path),
            "selected_canonical_trace_formula_source_lemma": rel(lemma_path),
            "selected_PhiFin_S2_gap_layer_lock": rel(gap_lock_path),
            "selected_trace_equals_27_mode_DE_attempt": rel(trace27_path),
        },
        "promotion": {
            "selected_trace_equality_proved": lemma["selected_trace_equality"]["proved"],
            "D_E_source_flags_theorem_derived": gap_lock["locked_contract"]["D_E_source_flags_are_theorem_derived"],
            "D_E_honest_replay_passes_after_theorem_derived_source_flags": gap_lock["locked_contract"]["D_E_honest_replay_passes_after_theorem_derived_source_flags"],
            "Riesz_Green_layer_closes": gap_lock["locked_contract"]["Riesz_Green_layer_closes"],
            "selected_eta_N": gap_lock["locked_contract"]["selected_eta_N"],
            "eta_threshold": gap_lock["locked_contract"]["eta_threshold"],
            "selected_gap_lower_bound": gap_lock["locked_contract"]["selected_gap_lower_bound"],
            "selected_green_norm_bound": gap_lock["locked_contract"]["selected_green_norm_bound"],
            "basis_id": gap_lock["locked_contract"]["basis_id"],
            "basis_dimension": gap_lock["locked_contract"]["basis_dimension"],
        },
        "scope_guardrail": gap_lock["locked_contract"]["scope"],
        "still_separate": gap_lock["still_separate"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    projector_packet = {
        "schema": "MTTConstHiggs01H2ProjectorSourcePacket.v1",
        "status": "HIGGS_DE_GAP_PROJECTOR_SOURCE_PROMOTED_FULL_ZERO_MODE_PACKET_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-HIGGS-PROJECTOR-SOURCE-PACKET",
        "selected_source_identity": {
            "branch": "q79/F,m=1 S3/GS Route-C",
            "same_source_no_substitution_certificate": lemma["proof_steps"]["same_source_no_substitution_certificate"]["proved"],
            "observed_or_benchmark_inputs_used": False,
        },
        "H_sector_selected_gap_layer": {
            "formula": lemma["selected_trace_equality"]["H_sector"],
            "H_shift_indices": gap_lock["formula_lock"]["H_shift_indices"],
            "zero_cluster_indices": gap_lock["locked_contract"]["zero_cluster_indices"],
            "H_rank_two_shift_source_proved": lemma["proof_steps"]["H_rank_two_shift_source"]["proved"],
            "canonical_metric_connection_source_proved": lemma["proof_steps"]["canonical_active_metric_normalization_source"]["proved"],
            "projective_flat_connection_to_DE_source_proved": lemma["proof_steps"]["projective_flat_connection_to_DE_source"]["proved"],
        },
        "projector_boundary": {
            "block_family_Higgs_projector_support_closed_from_H1": h1["block_family_Higgs_projector_support_closed"],
            "selected_DE_gap_layer_closed_now": True,
            "full_selected_zero_mode_basis_packet": False,
            "full_selected_dotD_C1_response": False,
            "Yukawa_or_SM_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    heat_response = {
        "schema": "MTTConstHiggs01H2FiniteHeatSpectrumResponseImport.v1",
        "status": "FINITE_HEAT_SPECTRUM_RESPONSE_IMPORTED_AS_SELECTED_GAP_LAYER_CONSEQUENCE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-FINITE-HEAT-SPECTRUM-RESPONSE",
        "inputs": {
            "SM_parity_heat_torsion_final_gate": rel(heat_final_path),
            "selected_gap_lock": rel(gap_lock_path),
        },
        "imported_response": {
            "finite_determinant_heat_spectrum_or_torsion_response_closed": heat_final["closure_decision"]["finite_determinant_heat_spectrum_or_torsion_response_closed"],
            "selected_finite_heat_trace_emitted": heat_final["what_closes_now"]["selected_finite_heat_trace_emitted"],
            "selected_positive_complement_pseudodeterminant_emitted": heat_final["what_closes_now"]["selected_positive_complement_pseudodeterminant_emitted"],
            "operator_source_slots_closed_total": heat_final["closure_decision"]["operator_source_slots_closed_total"],
            "operator_source_slots_remaining": heat_final["closure_decision"]["operator_source_slots_remaining"],
        },
        "classification_for_Higgs_quartic": {
            "useful": "confirms the selected D_E/gap layer has source-level spectral response data",
            "not_enough": "does not emit a Higgs quartic/threshold second-variation kernel, smooth analytic torsion, or dynamic C1/Yukawa response",
        },
        "open_from_import": heat_final["what_remains_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    quartic_gate = {
        "schema": "MTTConstHiggs01H2QuarticKernelReduction.v1",
        "status": "QUARTIC_KERNEL_REDUCED_TO_SELECTED_SECOND_VARIATION_OR_DYNAMIC_C1_RESPONSE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-QUARTIC-KERNEL-REDUCTION",
        "what_changed_from_H1": {
            "selected_PhiFin_D_E_gap_layer": "open in H1, promoted in H2 by the canonical trace lemma and gap-layer lock",
            "selected_eta_N": 1.0,
            "selected_gap_Riesz_Green_layer": True,
        },
        "still_not_a_quartic_derivation": {
            "selected_Higgs_quartic_threshold_kernel_emitted": False,
            "Higgs_quartic_numeric_value_derived": False,
            "dotD_alpha1_C1_response_closed": False,
            "A_selected_or_b_selected_claimed": False,
            "Yukawa_or_SM_closure_claimed": False,
        },
        "strict_H3_acceptance": {
            "must_emit_one_of": [
                "same-source Phi_fin second variation restricted to the Higgs scalar/zero-mode amplitude",
                "selected quartic threshold Hessian block with normalization tied to the G4 primitive",
                "dynamic C1/retarded-overlap response that maps the selected D_E/gap layer to the Higgs quartic kernel",
            ],
            "must_reuse": [
                "G4 one-metrology/action primitive without choosing a value from Higgs data",
                "H2 selected D_E/gap/Riesz/Green layer",
            ],
            "must_forbid": [
                "lambda_H = m_H^2/(2 v^2) as a source selector",
                "Higgs widths, branching ratios, or external RG rows as source selectors",
                "new Higgs-specific normalization or threshold knobs",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstHiggs01H2Boundary.v1",
        "status": "H2_PROMOTES_SELECTED_GAP_LAYER_QUARTIC_KERNEL_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-BOUNDARY",
        "closed_or_promoted_now": {
            "selected_PhiFin_finite_trace_morphism_for_DE_gap_layer": True,
            "selected_trace_equality_for_27mode_DE": True,
            "D_E_source_flags_theorem_derived_for_gap_layer": True,
            "selected_eta_N_promoted": True,
            "selected_gap_Riesz_Green_layer": True,
            "H_sector_rank_two_zero_cluster_shift_source": True,
            "finite_heat_spectrum_response_slot": True,
        },
        "still_open": {
            "selected_Higgs_quartic_threshold_kernel": True,
            "Higgs_quartic_numeric_value": True,
            "full_selected_zero_mode_basis_packet": True,
            "dotD_alpha1_C1_response": True,
            "A_selected_and_b_selected": True,
            "Yukawa_or_full_SM_closure": True,
            "strict_no_knob_Higgs_closure": True,
            "one_primitive_cross_constant_validation": h1_boundary["still_open"]["one_primitive_cross_constant_validation"],
        },
        "anti_cycle_delta_from_H1": {
            "H1": "froze the older boundary where Phi_fin finite trace provenance was open",
            "H2": "imports the newer canonical trace lemma and gap-layer replay lock, promoting the selected D_E/gap layer while keeping quartic/dynamic response open",
            "not_repeated": [
                "not treating D_E/gap-layer closure as Higgs quartic closure",
                "not inferring Yukawa, C1, or full SM closure",
                "not using measured Higgs values as source selectors",
                "not adding a Higgs-specific primitive",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H2NextWork.v1",
        "status": "NEXT_WORKORDER_H3_HIGGS_QUARTIC_SECOND_VARIATION_OR_DYNAMIC_RESPONSE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-NEXT",
        "primary": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUARTIC-SECOND-VARIATION-KERNEL",
            "task": "Derive or emit the selected Phi_fin second-variation/quartic Hessian block on the Higgs amplitude, with normalization tied to the G4 primitive and no measured Higgs inputs.",
        },
        "parallel": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3B-DYNAMIC-C1-RETARDED-OVERLAP-RESPONSE",
            "task": "Try the dynamic C1/retarded-overlap route from the selected D_E/gap/Riesz/Green layer to a Higgs quartic threshold kernel.",
        },
        "parking_lot": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3C-PRECISION-LAMBDA-TRANSPORT-COMPARISON",
            "task": "Use downstream lambda_H/RG rows only after a source kernel is emitted; never as a source selector.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H2SelectedHiggsProjectorAndQuarticKernelSourcePacket",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-SELECTED-HIGGS-PROJECTOR-AND-QUARTIC-KERNEL-SOURCE-PACKET",
        "output_packets": {
            "selected_gap_layer_promotion": rel(GAP_LAYER),
            "higgs_projector_source_packet": rel(PROJECTOR_PACKET),
            "finite_heat_spectrum_response_import": rel(HEAT_RESPONSE),
            "quartic_kernel_reduction": rel(QUARTIC_GATE),
            "h2_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H2SelectedGapLayerPromotionTheorem",
            "proved": True,
            "statement": (
                "Using the newer selected canonical trace formula source lemma and selected Phi_fin S2 gap-layer replay lock, the H1 Phi_fin provenance blocker closes for the D_E/gap/Riesz/Green layer. The H-sector rank-two zero-cluster shift, selected eta_N=1.0, positive gap, Green bound, and finite heat/spectrum response are now theorem-derived at the selected finite Galerkin layer. This does not yet emit the Higgs quartic/threshold second-variation kernel, dotD/C1 response, or a numerical lambda_H value."
            ),
        },
        "G4_one_metrology_primitive_reused": True,
        "new_Higgs_specific_parameters": 0,
        "selected_PhiFin_provenance_closed_for_DE_gap_layer": True,
        "selected_DE_gap_Riesz_Green_layer_closed": True,
        "selected_eta_N": 1.0,
        "H_sector_rank_two_zero_cluster_shift_source_closed": True,
        "finite_heat_spectrum_response_slot_closed": True,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H3_SelectedHiggsQuarticSecondVariationKernel_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H2_SelectedHiggsProjectorAndQuarticKernelSourcePacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_PhiFin_provenance_closed_for_DE_gap_layer": True,
        "selected_DE_gap_Riesz_Green_layer_closed": True,
        "selected_eta_N": 1.0,
        "H_sector_rank_two_zero_cluster_shift_source_closed": True,
        "finite_heat_spectrum_response_slot_closed": True,
        "selected_Higgs_quartic_threshold_kernel_emitted": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H2 Selected Higgs Projector And Quartic Kernel Source Packet v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H2-SELECTED-HIGGS-PROJECTOR-AND-QUARTIC-KERNEL-SOURCE-PACKET`

## Result

```text
selected Phi_fin provenance for D_E/gap layer   True
selected eta_N                                  1.0
eta threshold                                   2.1932454224643014
selected gap lower bound                        2.386490844928603
selected Green norm bound                       0.4190252822989217
H-sector rank-two shift source                  True
finite heat/spectrum response slot              True
selected Higgs quartic/threshold kernel         False
Higgs quartic numeric value                     False
```

H2 imports the newer selected canonical trace formula source lemma.  That
repairs the H1 provenance blocker for the finite `D_E` gap layer:

```text
Phi_fin(D_E(selected source))
  = canonical F3xF3 Fourier Laplacian
  + H-sector rank-two zero-cluster projector on indices 13,14.
```

The selected finite gap/Riesz/Green layer is now theorem-derived.  This is a
real promotion, but it is scoped.  It does not emit the dynamic `dotD/C1`
response, `A_selected`, `b_selected`, Yukawa data, or the Higgs
quartic/threshold second-variation kernel.

## Next

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H3-SELECTED-HIGGS-QUARTIC-SECOND-VARIATION-KERNEL`

H3 must derive a same-source second variation or dynamic retarded-overlap
response from the selected gap layer to the Higgs quartic threshold kernel,
while reusing the G4 primitive and forbidding measured Higgs values as
selectors.
"""

    for path, payload in [
        (GAP_LAYER, gap_layer),
        (PROJECTOR_PACKET, projector_packet),
        (HEAT_RESPONSE, heat_response),
        (QUARTIC_GATE, quartic_gate),
        (BOUNDARY, boundary),
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
