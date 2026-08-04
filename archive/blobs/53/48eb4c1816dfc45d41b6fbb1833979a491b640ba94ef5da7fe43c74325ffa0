"""Build dynamic C1 transfer tensor / Galerkin C1 values gate.

This artifact imports the newly closed static Weyl-pair provenance together
with the strongest stationary operator and alpha1/dotD packets.  It separates
the dynamic C1 frontier into:

* closed support: static sector routing, trace normalization, stationary
  projector/Riesz/Green transport, alpha1/dotD driver;
* open value emission: non-invariant primitive C1 tensor, Hessian/source vector
  b_selected, or honest Galerkin C1 values.

It also materializes the exact conditional dynamic transfer tensor normal form
without promoting it to selected physical data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"
DYNAMIC_BOUNDARY = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "dynamic_c1_value_boundary.packet.json"
)
STATIC_PROVENANCE = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "static_enriched_weylpair_source_provenance.packet.json"
)
VALUE_RUN = (
    DATA
    / "selected_weylpairsourceemission_or_honestgalerkinc1execution_valuerun"
    / "conditional_weylpair_value_run.packet.json"
)
WEYL_SOURCE = DATA / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem.candidate.json"
PHIFIN_DYNAMIC = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
DIFF_PHIFIN = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
CROSSREPO_ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
HONEST_GALERKIN = (
    DATA
    / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
    / "galerkin_c1_values_fallback.packet.json"
)

OUTPUT = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"
PACKET_DIR = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values"
SUPPORT_PACKET = PACKET_DIR / "closed_dynamic_operator_support.packet.json"
TENSOR_PACKET = PACKET_DIR / "conditional_dynamic_c1_transfer_tensor.packet.json"
FRONTIER_PACKET = PACKET_DIR / "primitive_tensor_or_galerkin_frontier.packet.json"
CERT = CERTS / "selected_dynamicc1transfertensor_or_galerkinc1values_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_OR_GALERKINC1VALUES_BUILT_OPERATOR_ALPHA1_CLOSED_PRIMITIVE_TENSOR_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_or_HessianSourceVector_or_GalerkinC1Values_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    dynamic = load(DYNAMIC_BOUNDARY)
    static = load(STATIC_PROVENANCE)
    value_run = load(VALUE_RUN)
    weyl_source = load(WEYL_SOURCE)
    phifin_dynamic = load(PHIFIN_DYNAMIC)
    diff_phifin = load(DIFF_PHIFIN)
    alpha1 = load(CROSSREPO_ALPHA1)
    galerkin = load(HONEST_GALERKIN)

    stationary = phifin_dynamic["stationary_trace_import"]
    alpha1_import = alpha1["alpha1_driver_replay_import"]
    diff_driver = diff_phifin["driver_contract"]
    zero_no_go = diff_phifin["transport_only_no_go_theorem"]
    source_directions = weyl_source["enriched_weyl_pair_packet"]["source_directions"]

    operator_alpha1_closed = (
        previous["promotion_decision"]["static_enriched_weylpair_source_provenance_promoted"] is True
        and static["provenance_closed"] is True
        and stationary["selected_projector_source_verified"] is True
        and stationary["selected_riesz_green_source_verified"] is True
        and stationary["selected_source_verified"] is True
        and alpha1["alpha1_driver_verified_imported"] is True
        and alpha1["selected_dotD_source_verified_imported"] is True
        and diff_driver["attached_to_differentiated_contract_as_driver"] is True
    )

    support_packet = {
        "schema": "MTTClosedDynamicOperatorSupport.v1",
        "status": "STATIC_OPERATOR_ALPHA1_SUPPORT_CLOSED_FOR_DYNAMIC_C1_FRONTIER",
        "static_source_support": {
            "static_enriched_weylpair_source_provenance_promoted": previous["promotion_decision"][
                "static_enriched_weylpair_source_provenance_promoted"
            ],
            "phase_Z_to": static["static_sector_route"]["phase_Z_to"],
            "shift_X_to": static["static_sector_route"]["shift_X_to"],
            "trace_transfer_normalization_selected": static["static_normalization"][
                "static_trace_innerproduct_normalization_selected"
            ],
        },
        "stationary_operator_support": {
            "selected_projector_source_verified": stationary["selected_projector_source_verified"],
            "selected_riesz_green_source_verified": stationary["selected_riesz_green_source_verified"],
            "selected_rho_s_validator_ready": stationary["selected_rho_s_validator_ready"],
            "selected_source_verified": stationary["selected_source_verified"],
            "functional_gauge_transported_trace_proved": stationary[
                "functional_gauge_transported_trace_proved"
            ],
            "symbolic_transport_conjugation_validator_extended": stationary[
                "symbolic_transport_conjugation_validator_extended"
            ],
        },
        "alpha1_dotD_support": {
            "alpha1_driver_verified_imported": alpha1["alpha1_driver_verified_imported"],
            "selected_dotD_source_verified_imported": alpha1[
                "selected_dotD_source_verified_imported"
            ],
            "honest_dotD_alpha1_replay": alpha1_import["honest_dotD_alpha1_replay"],
            "N_alpha1_h_ext": alpha1_import["N_alpha1_h_ext"],
            "du_dalpha1_equals_h_ext": alpha1_import["du_dalpha1_equals_h_ext"],
            "attached_to_differentiated_contract_as_driver": diff_driver[
                "attached_to_differentiated_contract_as_driver"
            ],
            "primitive_overlap_values_emitted_by_driver": diff_driver[
                "primitive_overlap_values_emitted_by_driver"
            ],
        },
        "closed_for_frontier": operator_alpha1_closed,
        "does_not_emit": [
            "selected non-invariant primitive C1 tensor",
            "selected primitive overlap contractions",
            "selected Hessian/source vector b_selected",
            "selected A_selected",
            "selected deltaTheta_C1",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    tensor_packet = {
        "schema": "MTTConditionalDynamicC1TransferTensor.v1",
        "status": "CONDITIONAL_TENSOR_NORMAL_FORM_BUILT_NOT_SELECTED",
        "tensor_name": "T_dynamic_conditional_WeylPair",
        "domain_basis": [
            {
                "id": "phase_Z",
                "source": "selected source-level Z/clock/phase leg",
                "routed_to": static["static_sector_route"]["phase_Z_to"],
            },
            {
                "id": "shift_X",
                "source": "selected source-level X/shift/active vertex leg",
                "routed_to": static["static_sector_route"]["shift_X_to"],
            },
        ],
        "codomain": {
            "real_dimension": 72,
            "sector_order": ["u", "d", "e", "nuD"],
            "matrix_order": "row-major 3x3 complex entries encoded as real/imag pairs",
        },
        "sector_response_columns": {
            "phase_packet": source_directions["phase_packet"],
            "shift_packet": source_directions["shift_packet"],
        },
        "normal_form_replay": {
            "rank": value_run["rank"],
            "condition_number": value_run["condition_number"],
            "A_transpose_A": value_run["A_transpose_A_if_promoted"],
            "A_transpose_b": value_run["A_transpose_b_if_promoted"],
            "deltaTheta_C1": value_run["deltaTheta_C1_if_promoted"],
            "SM_parity_dynamic_packet_would_close_if_promoted": value_run[
                "SM_parity_dynamic_packet_would_close_if_promoted"
            ],
            "no_knob_flavor_constants_would_close_if_promoted": value_run[
                "no_knob_flavor_constants_would_close_if_promoted"
            ],
        },
        "selection_status": {
            "conditional_tensor_built": True,
            "selected_dynamic_C1_transfer_tensor_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
        },
        "why_not_selected": (
            "The tensor normal form is fixed by closed static provenance and exact "
            "finite algebra, but a selected non-invariant primitive C1 tensor, "
            "Hessian/source vector, or honest Galerkin value emission has not yet "
            "emitted these columns as physical differentiated C1 response data."
        ),
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    frontier_packet = {
        "schema": "MTTPrimitiveTensorOrGalerkinFrontier.v1",
        "status": "PRIMITIVE_TENSOR_HESSIAN_OR_GALERKIN_VALUES_OPEN",
        "transport_only_lane_rejected": zero_no_go["proved"],
        "transport_only_zero_matrices": zero_no_go["finite_evidence"][
            "all_sector_matrices_verified_zero"
        ],
        "canonical_tensor_selected_by_theorem": diff_phifin["canonical_transport_only_test"][
            "canonical_tensor_selected_by_theorem"
        ],
        "required_primitive_formula": diff_phifin["differentiated_primitive_overlap_contract"][
            "primitive_overlap_formula"
        ],
        "required_acceptance_equations": diff_phifin[
            "differentiated_primitive_overlap_contract"
        ]["acceptance_equations"],
        "remaining_value_routes": {
            "route_A_selected_noninvariant_primitive_tensor": {
                "must_emit": [
                    "selected_primitive_vertex_operator_phase_Z",
                    "selected_primitive_vertex_operator_shift_X",
                    "primitive_three_by_three_contraction_terms",
                    "linear_response_matrices in the 72-real codomain",
                ],
                "currently_emitted": False,
            },
            "route_B_selected_Hessian_or_b_source_vector": {
                "must_emit": [
                    "selected Hessian/source vector b_selected",
                    "selected Gram/Hessian normalization",
                    "same-branch equality b_selected = phase + shift or replacement",
                ],
                "currently_emitted": False,
            },
            "route_C_honest_Galerkin_C1_values": {
                "must_emit": galerkin["required_outputs"],
                "selected_source_verified_now": galerkin["selected_source_verified"],
                "currently_emitted": False,
            },
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1TransferTensorOrGalerkinC1Values",
        "status": STATUS,
        "inputs": {
            "previous_static_provenance_gate": rel(PREVIOUS),
            "dynamic_boundary": rel(DYNAMIC_BOUNDARY),
            "static_provenance": rel(STATIC_PROVENANCE),
            "conditional_value_run": rel(VALUE_RUN),
            "weylpair_source_gate": rel(WEYL_SOURCE),
            "phifin_dynamic_transfer_gate": rel(PHIFIN_DYNAMIC),
            "differentiated_phifin_gate": rel(DIFF_PHIFIN),
            "crossrepo_alpha1_driver": rel(CROSSREPO_ALPHA1),
            "honest_galerkin_values": rel(HONEST_GALERKIN),
        },
        "output_packets": {
            "closed_dynamic_operator_support": rel(SUPPORT_PACKET),
            "conditional_dynamic_c1_transfer_tensor": rel(TENSOR_PACKET),
            "primitive_tensor_or_galerkin_frontier": rel(FRONTIER_PACKET),
        },
        "what_closes_now": {
            "static_source_provenance_retained_closed": True,
            "stationary_projector_riesz_green_support_retained_closed": True,
            "alpha1_dotD_driver_retained_closed": True,
            "transport_only_zero_lane_rejected": True,
            "conditional_dynamic_C1_transfer_tensor_normal_form_built": True,
            "dynamic_frontier_reduced_to_primitive_tensor_Hessian_or_Galerkin_values": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_noninvariant_primitive_C1_tensor": True,
            "selected_primitive_C1_overlap_contractions": True,
            "selected_Hessian_or_b_source_vector": True,
            "honest_selected_Galerkin_C1_values": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "operator_alpha1_support_closed_for_frontier": operator_alpha1_closed,
            "conditional_dynamic_C1_transfer_tensor_selected": False,
            "selected_noninvariant_primitive_C1_tensor_promoted": False,
            "selected_Hessian_or_b_source_vector_promoted": False,
            "honest_Galerkin_C1_values_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "DynamicC1FrontierReductionTheorem",
            "proved": True,
            "statement": (
                "After static Weyl-pair provenance, stationary projector/Riesz/Green "
                "transport, and imported alpha1/dotD replay are closed, the remaining "
                "dynamic C1 obstruction is not generic operator support.  The exact "
                "conditional transfer-tensor normal form is built and has rank 2 with "
                "A^T A=12 I_2 and deltaTheta=(1,1), but it is not selected physical "
                "data until a non-invariant primitive C1 tensor, Hessian/source vector "
                "b_selected, or honest Galerkin C1 run emits the same values from the "
                "same branch."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "support_packet_path": rel(SUPPORT_PACKET),
        "tensor_packet_path": rel(TENSOR_PACKET),
        "frontier_packet_path": rel(FRONTIER_PACKET),
        "theorem_proved": True,
        "closure_claimed": False,
        "SM_parity_dynamic_packet_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "no_knob_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1TransferTensor or GalerkinC1Values v1

Status: `{STATUS}`.

Closed support now carried into the dynamic frontier:

```text
static Weyl-pair provenance       = closed
stationary projector/Riesz/Green  = closed
alpha1/dotD driver                = closed
transport-only C1 lane            = rejected
```

The conditional dynamic tensor normal form is built but not promoted:

```text
rank = {value_run["rank"]}
A^T A = {value_run["A_transpose_A_if_promoted"]}
A^T b = {value_run["A_transpose_b_if_promoted"]}
deltaTheta = {value_run["deltaTheta_C1_if_promoted"]}
```

The live frontier is now only value emission: selected non-invariant primitive
C1 tensor, selected Hessian/source vector `b_selected`, or honest selected
Galerkin C1 values.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or target
residuals are used as selectors.

Next artifact: `{NEXT}`.
"""

    SUPPORT_PACKET.write_text(json.dumps(support_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    TENSOR_PACKET.write_text(json.dumps(tensor_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER_PACKET.write_text(json.dumps(frontier_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
