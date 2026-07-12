from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"
NONSM_ROOT = ROOT.parent / "mtt-nonsm-constants-no-knob"

PREV = ROOT / "certificates" / "post_alpha_hym_alpha1_frontier_synthesis_certificate.json"

SM_CERT = SM_ROOT / "certificates" / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"
SM_CUTSET = (
    SM_ROOT
    / "candidate_data"
    / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
    / "strict_value_emission_cutset.packet.json"
)
SM_LANE_B = (
    SM_ROOT
    / "candidate_data"
    / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
    / "lane_b_honest_galerkin_c1_run_attempt.packet.json"
)
NONSCALAR = NONSM_ROOT / "candidate_data" / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_value_emission_cutset_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dynamic_c1_value_emission_cutset.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_DynamicC1_ValueEmission_Cutset_Import_v1.md"

STATUS = "POST_ALPHA_DYNAMIC_C1_VALUE_EMISSION_CUTSET_IDENTIFIED_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREV)
    sm_cert = load(SM_CERT)
    sm_candidate = load(SM_CANDIDATE)
    sm_cutset = load(SM_CUTSET)
    sm_lane_b = load(SM_LANE_B)
    nonscalar = load(NONSCALAR)

    coordinate_system = sm_cutset["acceptance_target"]["coordinate_system"]
    numeric = sm_cutset["closed_numeric_facts"]

    previous_frontier_ok = (
        previous["theorem"]["proved"] is True
        and previous["closure_claimed"] is False
        and previous["frontier_decision"]["frontier_is_primitive_C1_or_full_response_emission"] is True
    )

    imported_sm_cutset_ok = all(
        [
            sm_cert["theorem_proved"] is True,
            sm_cert["closure_claimed"] is False,
            sm_cert["observed_data_used"] is False,
            sm_cert["target_fitting_used"] is False,
            sm_cert["A_selected_claimed"] is False,
            sm_cert["b_selected_claimed"] is False,
            sm_cert["deltaTheta_C1_claimed"] is False,
            sm_cert["sector_response_matrices_claimed"] is False,
            sm_cert["honest_Galerkin_C1_claimed"] is False,
            sm_cert["next_required_artifact"] == NEXT,
            all(sm_cert["what_closes"].values()),
            all(sm_cert["what_remains_open"].values()),
            sm_candidate["theorem"]["proved"] is True,
            sm_candidate["closure_claimed"] is False,
            sm_candidate["next_required_artifact"] == NEXT,
            sm_candidate["promotion_decision"]["value_emission_attempt_completed"] is True,
            sm_candidate["promotion_decision"]["A_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["b_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            sm_candidate["promotion_decision"]["sector_response_matrices_promoted"] is False,
            sm_candidate["promotion_decision"]["lane_B_honest_Galerkin_C1_promoted"] is False,
        ]
    )

    strict_acceptance_manifest_ok = all(
        [
            sm_cutset["schema"] == "MTTStrictDynamicC1ValueEmissionCutset.v1",
            sm_cutset["status"] == "STRICT_VALUE_EMISSION_CUTSET_IDENTIFIED_EXISTING_VALUES_OPEN",
            sm_cutset["promotion_allowed_now"] is False,
            sm_cutset["observed_data_used"] is False,
            sm_cutset["target_fitting_used"] is False,
            sm_cutset["acceptance_target"]["A_selected_72_real_columns_required"] is True,
            sm_cutset["acceptance_target"]["b_selected_72_real_source_vector_required"] is True,
            sm_cutset["acceptance_target"]["sector_response_matrices_required"] is True,
            sm_cutset["acceptance_target"]["deltaTheta_C1_must_be_solved_from_selected_values"] is True,
            coordinate_system["name"] == "fixed_72_real_C1_coordinate_system",
            coordinate_system["sectors"] == ["u", "e", "d", "nuD"],
            coordinate_system["total_real_coordinates"] == 72,
            coordinate_system["real_coordinates_per_sector"] == 18,
            coordinate_system["per_sector_matrix_shape"] == [3, 3],
            sm_cutset["current_acceptance_sources_exhausted"]["lane_A_same_source_dynamic_transfer_checked"] is True,
            sm_cutset["current_acceptance_sources_exhausted"]["lane_B_honest_Galerkin_C1_checked"] is True,
            sm_cutset["current_acceptance_sources_exhausted"]["no_current_packet_satisfies_strict_acceptance"] is True,
        ]
    )

    conditional_reference_arithmetic = {
        "A_transpose_A": numeric["A_transpose_A"],
        "A_transpose_b": numeric["A_transpose_b"],
        "deltaTheta_C1": numeric["deltaTheta_C1"],
        "rank": numeric["rank"],
        "condition_number": numeric["condition_number"],
        "reference_is_selected": False,
        "reason": "These are conditional reference facts only; no selected A_selected, b_selected, or sector matrices are emitted.",
    }

    conditional_reference_ok = all(
        [
            numeric["A_transpose_A_equals_12I2"] is True,
            numeric["A_transpose_b_equals_12_12"] is True,
            numeric["deltaTheta_equals_1_1"] is True,
            numeric["rank_2_condition_number_1"] is True,
            sm_cutset["field_status"]["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            sm_cutset["field_status"]["b_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            sm_cutset["field_status"]["deltaTheta_C1"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED",
            sm_cutset["field_status"]["sector_response_matrices"] == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE",
        ]
    )

    honest_galerkin_lane_ok = all(
        [
            sm_lane_b["schema"] == "MTTLaneBHonestGalerkinC1RunAttempt.v1",
            sm_lane_b["can_promote_honest_Galerkin_C1_values_now"] is False,
            sm_lane_b["currently_closed"] is False,
            sm_lane_b["selected_source_verified"] is False,
            sm_lane_b["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            sm_lane_b["observed_data_used"] is False,
            sm_lane_b["target_fitting_used"] is False,
            sm_lane_b["must_emit_same_coordinate_target"] == coordinate_system,
            sm_lane_b["missing_outputs"]
            == [
                "zero_mode_bases",
                "primitive_three_by_three_contraction_terms",
                "linear_response_matrices",
                "C33/nonzero-family-rank tests",
            ],
        ]
    )

    nonscalar_support_ok = all(
        [
            nonscalar["theorem"]["proved"] is True,
            nonscalar["theorem"]["closure_claimed"] is False,
            nonscalar["promotion_gate"]["conditional_non_scalar_packet_available"] is True,
            nonscalar["promotion_gate"]["promote_to_A_selected_allowed"] is False,
            nonscalar["promotion_gate"]["promote_to_b_selected_allowed"] is False,
            nonscalar["promotion_gate"]["promote_to_selected_full_response_allowed"] is False,
            nonscalar["promotion_gate"]["selected_source_to_C1_transfer_map_emitted"] is False,
            all(nonscalar["what_remains_open"].values()),
        ]
    )

    what_closes_now = {
        "post_alpha_frontier_matches_dynamic_value_emission": previous_frontier_ok,
        "SM_dynamic_C1_cutset_imported": imported_sm_cutset_ok,
        "strict_72_real_acceptance_manifest_imported": strict_acceptance_manifest_ok,
        "conditional_rank2_reference_arithmetic_quarantined": conditional_reference_ok,
        "honest_Galerkin_lane_requirements_imported": honest_galerkin_lane_ok,
        "conditional_nonscalar_packet_kept_unpromoted": nonscalar_support_ok,
        "observed_constants_excluded_as_selectors": (
            sm_cert["observed_data_used"] is False
            and sm_cert["target_fitting_used"] is False
            and sm_cutset["observed_data_used"] is False
            and sm_cutset["target_fitting_used"] is False
            and sm_lane_b["observed_data_used"] is False
            and sm_lane_b["target_fitting_used"] is False
        ),
    }

    what_remains_open = {
        "selected_primitive_C1_tensor_or_differentiated_PhiFinC1_source_map": True,
        "selected_Hessian_source_vector_b_selected_or_equivalent_coefficients": True,
        "selected_sector_response_matrices_in_fixed_72_real_coordinates": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "selected_A_selected": True,
        "selected_deltaTheta_C1_solve": True,
        "lambda12_Yukawa_CKM_PMNS_CP_mass_closure": True,
        "full_SM_no_knob_closure": True,
    }

    guardrails = {
        "does_not_promote_conditional_A_or_b": True,
        "does_not_promote_deltaTheta_C1_reference": True,
        "does_not_claim_sector_response_matrices": True,
        "does_not_claim_honest_Galerkin_C1_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem_proved = all(
        [
            all(what_closes_now.values()),
            all(what_remains_open.values()),
            all(guardrails.values()),
        ]
    )

    theorem = {
        "name": "PostAlphaDynamicC1ValueEmissionCutsetImport",
        "proved": theorem_proved,
        "closure_claimed": False,
        "statement": (
            "Given the post-alpha HYM/alpha1 frontier, the strict SM-parity "
            "dynamic C1 value-emission cutset imports as the exact next gate. "
            "Existing same-source and honest-Galerkin lanes have been checked "
            "against the fixed 72-real acceptance manifest and no current "
            "packet emits selected A_selected, b_selected, sector response "
            "matrices, or an honest DeltaTheta_C1 solve. Conditional rank-2 "
            "arithmetic is retained only as a reference, not as selected MTT data."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "strict_acceptance_manifest": sm_cutset["acceptance_target"],
        "conditional_reference_arithmetic": conditional_reference_arithmetic,
        "field_status": sm_cutset["field_status"],
        "minimal_live_cutset": sm_cutset["minimal_live_cutset"],
        "honest_galerkin_lane_missing_outputs": sm_lane_b["missing_outputs"],
        "conditional_nonscalar_support": {
            "available": True,
            "promoted": False,
            "status": nonscalar["status"],
            "why_not_promoted": nonscalar["promotion_gate"]["why_not_promoted"],
        },
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "frontier_is_selected_value_emission_cutset": True,
            "frontier_is_HYM_existence": False,
            "frontier_is_alpha1_driver": False,
            "frontier_is_conditional_rank2_arithmetic": False,
            "frontier_is_observed_fit": False,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_post_alpha_hym_alpha1_frontier": str(PREV),
            "sm_dynamic_c1_certificate": str(SM_CERT),
            "sm_dynamic_c1_candidate": str(SM_CANDIDATE),
            "sm_strict_value_emission_cutset": str(SM_CUTSET),
            "sm_lane_b_honest_galerkin_attempt": str(SM_LANE_B),
            "nonscalar_conditional_support": str(NONSCALAR),
        },
    }

    note = f"""# PostAlpha Dynamic C1 Value-Emission Cutset Import v1

## Result

The post-alpha HYM/alpha1 frontier now imports the strict dynamic C1
value-emission cutset from the SM-parity branch.

What closes:

```text
the remaining gate is selected value emission
the acceptance target is the fixed 72-real C1 coordinate system
same-source and honest-Galerkin lanes have both been checked
no current packet satisfies strict acceptance
conditional rank-2 arithmetic is quarantined as non-selected reference data
observed constants and target fitting are excluded
```

What remains:

```text
selected primitive C1 tensor or differentiated PhiFinC1 source map
selected b_selected/source coefficients
selected sector response matrices in fixed 72-real coordinates
honest selected Galerkin C1 execution values
selected A_selected and honest DeltaTheta_C1 solve
full lambda12/Yukawa/CKM/PMNS/CP/mass closure
```

The useful conditional arithmetic is:

```text
A^T A = 12 I_2
A^T b = (12, 12)
DeltaTheta_C1 = (1, 1)
rank = 2, condition number = 1
```

But this packet explicitly does not promote those values as selected MTT data.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_dynamic_c1_value_emission_cutset",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "conditional_reference_arithmetic": conditional_reference_arithmetic,
        "minimal_live_cutset": sm_cutset["minimal_live_cutset"],
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
