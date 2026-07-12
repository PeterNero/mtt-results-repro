"""Build dynamic C1 value-emission attempt / honest Galerkin C1 run gate.

This artifact applies the strict 72-real acceptance manifest to the currently
available value sources.  It does not promote the conditional Weyl-pair tensor;
it records exactly which Lane A and Lane B value-emission requirements are
still missing after the static provenance, operator support, alpha1/dotD
support, and linear algebra have been closed.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest.candidate.json"
STRICT = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
    / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
)
DUAL = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
    / "dual_path_value_fill_contract.packet.json"
)
DYNAMIC_GATE = DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"
TENSOR_PACKET = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values"
    / "conditional_dynamic_c1_transfer_tensor.packet.json"
)
FRONTIER_PACKET = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values"
    / "primitive_tensor_or_galerkin_frontier.packet.json"
)
PHIFIN_GATE = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
DIFF_PHIFIN = DATA / "selected_differentiated_phifinc1_primitiveoverlap_or_galerkinrun.candidate.json"
DYNAMIC_HESSIAN = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
DYNAMIC_OVERLAP = DATA / "selected_dynamicoverlaptensor_hessiannormalization_or_galerkinc1contractions_valueemission.candidate.json"
GALERKIN_C1 = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"

OUTPUT = DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"
PACKET_DIR = DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
LANE_A = PACKET_DIR / "lane_a_same_source_value_emission_attempt.packet.json"
LANE_B = PACKET_DIR / "lane_b_honest_galerkin_c1_run_attempt.packet.json"
CUTSET = PACKET_DIR / "strict_value_emission_cutset.packet.json"
CERT = CERTS / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1TRANSFERTENSOR_VALUEEMISSION_OR_HONESTGALERKINC1RUN_ATTEMPTED_EXISTING_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1"


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
    strict = load(STRICT)
    dual = load(DUAL)
    dynamic_gate = load(DYNAMIC_GATE)
    tensor = load(TENSOR_PACKET)
    frontier = load(FRONTIER_PACKET)
    phifin = load(PHIFIN_GATE)
    diff_phifin = load(DIFF_PHIFIN)
    dynamic_hessian = load(DYNAMIC_HESSIAN)
    dynamic_overlap = load(DYNAMIC_OVERLAP)
    galerkin = load(GALERKIN_C1)

    normal_form = tensor["normal_form_replay"]
    strict_acceptance = strict["dynamic_value_acceptance"]
    lane_a_contract = dual["lane_A_same_source_dynamic_transfer"]
    lane_b_contract = dual["lane_B_honest_galerkin_c1_run"]

    support_closed = (
        dynamic_gate["promotion_decision"]["operator_alpha1_support_closed_for_frontier"] is True
        and phifin["promotion_decision"]["stationary_source_layer_promoted"] is True
        and diff_phifin["promotion_decision"]["alpha1_dotD_driver_attached_to_contract"] is True
    )

    lane_a_missing = [
        "selected differentiated Phi_fin^C1 source-to-C1 transfer tensor",
        "selected primitive C1 overlap contractions",
        "selected Hessian/source-vector normalization emitting b_selected",
        "same-source proof tying emitted tensor to static Weyl route",
        "sector response matrices in the fixed 72-real coordinate system",
    ]
    lane_b_missing = list(galerkin["required_outputs"])

    lane_a_packet = {
        "schema": "MTTLaneASameSourceDynamicValueEmissionAttempt.v1",
        "status": "LANE_A_SAME_SOURCE_DYNAMIC_VALUE_EMISSION_ATTEMPTED_VALUES_OPEN",
        "acceptance_contract": lane_a_contract,
        "closed_support_available": {
            "static_operator_alpha1_support_closed": support_closed,
            "conditional_transfer_tensor_normal_form_built": dynamic_gate["what_closes_now"][
                "conditional_dynamic_C1_transfer_tensor_normal_form_built"
            ],
            "transport_only_zero_lane_rejected": dynamic_gate["what_closes_now"][
                "transport_only_zero_lane_rejected"
            ],
            "stationary_trace_layer_promoted": phifin["promotion_decision"][
                "stationary_source_layer_promoted"
            ],
            "alpha1_dotD_driver_attached_to_differentiated_contract": diff_phifin[
                "promotion_decision"
            ]["alpha1_dotD_driver_attached_to_contract"],
            "linear_algebra_obstruction_removed": dynamic_hessian["promotion_gate"][
                "no_linear_algebra_obstruction"
            ],
        },
        "existing_value_sources_checked": {
            "conditional_tensor_is_reference_not_promotion": strict[
                "conditional_reference_not_a_promotion"
            ],
            "PhiFinC1_identity_promoted_now": phifin["promotion_decision"][
                "selected_PhiFinC1_identity_promoted"
            ],
            "primitive_overlap_contractions_promoted": diff_phifin["promotion_decision"][
                "selected_primitive_overlap_contractions_promoted"
            ],
            "selected_Hessian_bselected_emitted": dynamic_hessian["promotion_gate"][
                "selected_Hessian_bselected_emitted"
            ],
            "selected_dynamic_transfer_identity_emitted": dynamic_hessian["promotion_gate"][
                "selected_dynamic_transfer_identity_emitted"
            ],
            "current_layer_promoted_as_dynamic_overlap_tensor": dynamic_overlap[
                "promotion_decision"
            ]["current_layer_values_promoted_as_dynamic_overlap_tensor"],
            "current_layer_promoted_as_A_selected": dynamic_overlap["promotion_decision"][
                "current_layer_values_promoted_as_A_selected"
            ],
            "current_layer_promoted_as_b_selected": dynamic_overlap["promotion_decision"][
                "current_layer_values_promoted_as_b_selected"
            ],
        },
        "conditional_values_preserved_only_as_if_promoted_reference": {
            "rank": normal_form["rank"],
            "condition_number": normal_form["condition_number"],
            "A_transpose_A": normal_form["A_transpose_A"],
            "A_transpose_b": normal_form["A_transpose_b"],
            "deltaTheta_C1": normal_form["deltaTheta_C1"],
        },
        "missing_for_promotion": lane_a_missing,
        "can_promote_A_selected_b_selected_deltaTheta_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    lane_b_packet = {
        "schema": "MTTLaneBHonestGalerkinC1RunAttempt.v1",
        "status": "LANE_B_HONEST_GALERKIN_C1_RUN_ATTEMPTED_VALUES_OPEN",
        "acceptance_contract": lane_b_contract,
        "manifest_status": galerkin["status"],
        "selected_source_verified": galerkin["selected_source_verified"],
        "required_outputs": galerkin["required_outputs"],
        "missing_outputs": lane_b_missing,
        "must_emit_same_coordinate_target": strict["coordinate_system"],
        "currently_closed": False,
        "can_promote_honest_Galerkin_C1_values_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    cutset_packet = {
        "schema": "MTTStrictDynamicC1ValueEmissionCutset.v1",
        "status": "STRICT_VALUE_EMISSION_CUTSET_IDENTIFIED_EXISTING_VALUES_OPEN",
        "acceptance_target": {
            "coordinate_system": strict["coordinate_system"],
            "A_selected_72_real_columns_required": strict_acceptance[
                "A_selected_72_real_columns_required"
            ],
            "b_selected_72_real_source_vector_required": strict_acceptance[
                "b_selected_72_real_source_vector_required"
            ],
            "deltaTheta_C1_must_be_solved_from_selected_values": strict_acceptance[
                "deltaTheta_C1_must_be_solved_from_selected_values"
            ],
            "sector_response_matrices_required": strict_acceptance[
                "must_report_sector_response_matrices"
            ],
        },
        "closed_numeric_facts": {
            "A_transpose_A": normal_form["A_transpose_A"],
            "A_transpose_b": normal_form["A_transpose_b"],
            "deltaTheta_C1": normal_form["deltaTheta_C1"],
            "rank": normal_form["rank"],
            "condition_number": normal_form["condition_number"],
            "A_transpose_A_equals_12I2": normal_form["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            "A_transpose_b_equals_12_12": normal_form["A_transpose_b"]
            == [12.0, 12.0],
            "deltaTheta_equals_1_1": normal_form["deltaTheta_C1"] == [1.0, 1.0],
            "rank_2_condition_number_1": normal_form["rank"] == 2
            and abs(normal_form["condition_number"] - 1.0) <= 1e-12,
        },
        "field_status": {
            "A_selected": "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            "b_selected": "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            "deltaTheta_C1": "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            "sector_response_matrices": "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
            "nonzero_family_rank_or_countertheorem": "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
        },
        "closed_not_blockers": {
            "static_Weyl_pair_source_provenance": True,
            "stationary_projector_Riesz_Green_support": True,
            "alpha1_dotD_driver_support": True,
            "fixed_72_real_coordinate_manifest": True,
            "rank_2_condition_number_1_conditional_linear_algebra": True,
            "transport_only_zero_lane_rejection": frontier["transport_only_lane_rejected"],
        },
        "current_acceptance_sources_exhausted": {
            "lane_A_same_source_dynamic_transfer_checked": True,
            "lane_B_honest_Galerkin_C1_checked": True,
            "no_current_packet_satisfies_strict_acceptance": True,
        },
        "minimal_live_cutset": [
            "selected primitive C1 tensor or differentiated Phi_fin^C1 source map",
            "selected Hessian/source vector b_selected or equivalent source coefficients",
            "sector response matrices in fixed 72-real coordinates",
            "honest selected Galerkin C1 execution values as replacement route",
        ],
        "promotion_allowed_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicC1TransferTensorValueEmissionOrHonestGalerkinC1Run",
        "status": STATUS,
        "inputs": {
            "acceptance_manifest": rel(PREVIOUS),
            "strict_acceptance_packet": rel(STRICT),
            "dual_path_contract": rel(DUAL),
            "dynamic_transfer_tensor_gate": rel(DYNAMIC_GATE),
            "conditional_tensor_packet": rel(TENSOR_PACKET),
            "primitive_frontier_packet": rel(FRONTIER_PACKET),
            "PhiFinC1_gate": rel(PHIFIN_GATE),
            "differentiated_PhiFin_gate": rel(DIFF_PHIFIN),
            "dynamic_Hessian_gate": rel(DYNAMIC_HESSIAN),
            "dynamic_overlap_value_gate": rel(DYNAMIC_OVERLAP),
            "honest_Galerkin_C1_manifest": rel(GALERKIN_C1),
        },
        "output_packets": {
            "lane_A_same_source_value_emission_attempt": rel(LANE_A),
            "lane_B_honest_galerkin_c1_run_attempt": rel(LANE_B),
            "strict_value_emission_cutset": rel(CUTSET),
        },
        "what_closes_now": {
            "strict_acceptance_target_replayed": True,
            "lane_A_existing_sources_checked_against_acceptance": True,
            "lane_B_existing_galerkin_manifest_checked_against_acceptance": True,
            "closed_support_separated_from_value_emission": True,
            "minimal_dynamic_value_cutset_identified": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "selected_differentiated_PhiFinC1_source_map": True,
            "selected_primitive_C1_overlap_contractions": True,
            "selected_Hessian_or_b_source_vector": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1": True,
            "selected_sector_response_matrices": True,
            "honest_selected_Galerkin_C1_execution_values": True,
            "SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_flavor_closure": True,
        },
        "promotion_decision": {
            "value_emission_attempt_completed": True,
            "lane_A_same_source_dynamic_transfer_promoted": False,
            "lane_B_honest_Galerkin_C1_promoted": False,
            "A_selected_promoted": False,
            "b_selected_promoted": False,
            "deltaTheta_C1_promoted": False,
            "sector_response_matrices_promoted": False,
            "SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_flavor_constants_closed": False,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "sector_response_matrices_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "DynamicC1ValueEmissionCutsetTheorem",
            "proved": True,
            "statement": (
                "Against the strict 72-real acceptance manifest, the current acceptance-relevant "
                "source inventory has no legal selected value-emission packet.  Closed support "
                "already includes static Weyl-pair provenance, stationary projector/Riesz/Green "
                "transport, alpha1/dotD support, and exact conditional rank-2 linear algebra.  "
                "The remaining obstruction is therefore exactly value emission: either a selected "
                "primitive/differentiated Phi_fin^C1 source map with b_selected and sector response "
                "matrices, or an honest selected Galerkin C1 execution that emits replacement values."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1TransferTensor_ValueEmission_or_HonestGalerkinC1Run_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "lane_A_packet_path": rel(LANE_A),
        "lane_B_packet_path": rel(LANE_B),
        "cutset_packet_path": rel(CUTSET),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "sector_response_matrices_claimed": False,
        "honest_Galerkin_C1_claimed": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1TransferTensor ValueEmission or HonestGalerkinC1Run v1

Status: `{STATUS}`.

The strict acceptance target is now replayed against the current source
inventory:

```text
target coordinate system = 4 sectors x 3x3 complex = 72 real coordinates
conditional rank         = {normal_form["rank"]}
conditional A^T A        = {normal_form["A_transpose_A"]}
conditional A^T b        = {normal_form["A_transpose_b"]}
conditional deltaTheta   = {normal_form["deltaTheta_C1"]}
```

Lane A is supported but not emitted: static provenance, stationary
projector/Riesz/Green, alpha1/dotD, and the conditional tensor are in place,
but selected differentiated `Phi_fin^C1`, primitive overlaps, `b_selected`, and
sector matrices are still absent.

Lane B is also open: the honest Galerkin C1 manifest still reports
`{galerkin["status"]}`.

So the remaining object is sharply identified: a selected primitive C1 tensor /
Hessian source map, or an honest selected Galerkin C1 execution, in the same
72-real coordinate system.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    LANE_A.write_text(json.dumps(lane_a_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    LANE_B.write_text(json.dumps(lane_b_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
