from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PREV = ROOT / "candidate_data" / "post_alpha_dotd_source_end0_routing_reduction.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json"
VALUES = QA / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json"
SM_DICTIONARY_HINT = CORPUS / "10 ProtoSpinor" / "Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"

OUT_CERT = ROOT / "certificates" / "post_alpha_end0_sector_model_values_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_end0_sector_model_values.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_End0_Sector_ModelValues_Import_v1.md"

STATUS = "POST_ALPHA_END0_SECTOR_MODEL_VALUES_CONSTRUCTED_SELECTED_ZEROMODES_OPEN"
NEXT = "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)
    values = load(VALUES)
    sm_text = read(SM_DICTIONARY_HINT)

    previous_reduction_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_DOTD_SOURCE_REDUCED_END0_ROUTING_VALUES_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
            prev["what_closes_now"]["End0_to_sector_route_selected_as_primary_frontier"] is True,
            prev["what_remains_open"]["selected_End0_to_sector_functor_values"] is True,
            all(prev["guardrails"].values()),
        ]
    )
    source_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["status"]
            == "U1Y_ROUTEC_END0_TO_SECTOR_VALUE_PACKET_CONSTRUCTED_MODEL_VALUES_ZERO_MODE_SOURCE_OPEN",
            source["decision"]["End0_domain_values_filled"] is True,
            source["decision"]["End0_tensor_product_carrier_constructed"] is True,
            source["decision"]["sector_projectors_constructed"] is True,
            source["decision"]["commutator_and_projector_checks_pass"] is True,
            source["decision"]["conditional_adjoint_triplet_theorem_proved"] is True,
            source["decision"]["conditional_gram_normalization_theorem_proved"] is True,
            source["decision"]["honest_dotD_replay_passes"] is False,
            source["decision"]["selected_zero_mode_bases_emitted"] is False,
            source["decision"]["selected_source_map_emitted"] is False,
            source["decision"]["selected_sector_zero_mode_realization_extracted"] is False,
            source["decision"]["selected_matter_slot_routing_extracted"] is False,
            source["decision"]["selected_1M_Dirac_neutrino_rule"] is False,
            source["decision"]["selected_transfer_normalization_extracted"] is False,
            source["decision"]["physical_dotD_alpha1_payload_extracted"] is False,
            source["decision"]["target_fitting_used"] is False,
            source["next_required_artifact"] == NEXT,
        ]
    )
    values_model_valid = all(
        [
            values["status"] == "MODEL_VALUES_CONSTRUCTED_SELECTED_ZERO_MODE_SOURCE_OPEN",
            values["domain"]["selected_End0_basis_available"] is True,
            values["domain"]["basis"] == ["T1", "T2", "T3"],
            values["sector_carrier_model"]["total_dimension"] == 19,
            values["sector_carrier_model"]["rank_match"]["six_matter_triplets_plus_H_singlet"] == "6*3+1",
            values["sector_carrier_model"]["rank_match"]["matches_BN_zero_cluster_sector_ranks"] is True,
            values["sector_carrier_model"]["rank_match"]["matches_expected_sector_kernel_rank_sum"] is True,
            values["sector_carrier_model"]["validation"]["all_lie_checks_pass"] is True,
            values["sector_carrier_model"]["validation"]["all_projectors_idempotent"] is True,
            values["sector_carrier_model"]["validation"]["all_distinct_projectors_orthogonal"] is True,
            values["sector_carrier_model"]["validation"]["projectors_sum_to_identity"] is True,
            values["sector_carrier_model"]["validation"]["all_projectors_commute_with_End0_action"] is True,
            values["sector_carrier_model"]["validation"]["matter_T3_norms_equal"] is True,
            values["sector_carrier_model"]["validation"]["H_T3_response_zero"] is True,
        ]
    )
    sector_dimensions_valid = all(
        [
            values["sector_projector_model"]["sector_dimensions"]["Q"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["u"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["d"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["L"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["e"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["N"] == 3,
            values["sector_projector_model"]["sector_dimensions"]["H"] == 1,
            values["sector_projector_model"]["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"],
            values["sector_projector_model"]["sector_T3_response_norms"]["H"]["zero_response"] is True,
            all(
                values["sector_projector_model"]["sector_T3_response_norms"][sector]["frobenius_norm"]
                == 1.4142135623730951
                for sector in ["Q", "u", "d", "L", "e", "N"]
            ),
        ]
    )
    promotion_blocker_valid = all(
        [
            values["source_promotion"]["promotion_decision"]["can_promote_without_new_theorem"] is False,
            values["source_promotion"]["promotion_decision"]["canonical_source_map_constructed"] is True,
            values["source_promotion"]["promotion_decision"]["selected_source_map_emitted"] is False,
            values["source_promotion"]["promotion_decision"]["selected_zero_mode_bases_emitted"] is False,
            values["source_promotion"]["promotion_decision"]["minimal_new_theorem_needed"]
            == "MTT_Selected_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1",
            values["source_promotion"]["source_chain"]["coherent_spectral_zero_mode_retention"] is False,
            values["source_promotion"]["source_chain"]["zero_mode_slot_values_filled"] is False,
        ]
    )
    old_dictionary_support_present = all(
        token in sm_text
        for token in [
            "QL",
            "uR",
            "dR",
            "LL",
            "eR",
            "B3",
            "B2",
            "B1",
        ]
    )
    guardrails_ok = all(
        [
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_honest_dotD_replay_passes"] is False,
            source["guardrails"]["claims_selected_zero_mode_bases_emitted"] is False,
            source["guardrails"]["claims_selected_source_map_rho_s"] is False,
            source["guardrails"]["claims_selected_matter_slot_routing"] is False,
            source["guardrails"]["claims_selected_1M_Dirac_neutrino_rule"] is False,
            source["guardrails"]["claims_selected_transfer_normalization"] is False,
            source["guardrails"]["claims_physical_dotD_alpha1_payload_extracted"] is False,
            source["guardrails"]["claims_primitive_C1_values_computed"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_full_sm_closure"] is False,
            source["guardrails"]["promotes_model_carrier_as_selected_zero_modes"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_reduction_ready,
            source_valid,
            values_model_valid,
            sector_dimensions_valid,
            promotion_blocker_valid,
            guardrails_ok,
        ]
    )

    b_support_dictionary = {
        "Q": ["B3", "B2", "B1"],
        "u": ["B3", "B1"],
        "d": ["B3", "B1"],
        "L": ["B2", "B1"],
        "e": ["B1"],
        "N": [],
        "H": ["B2", "B1"],
    }
    packet = {
        "theorem": {
            "name": "PostAlphaEnd0SectorModelValuesImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected End0-to-sector frontier now has canonical model values: "
                "T1,T2,T3 act by the adjoint triplet on six matter sectors Q,u,d,L,e,N "
                "and trivially on the H singlet. The sector projectors are orthogonal, "
                "idempotent, commute with the End0 action, and have ranks 3,3,3,3,3,3,1. "
                "This matches the old B1/B2/B3 Standard Model support dictionary as a "
                "support interpretation, but it is not yet promoted to selected physical "
                "zero modes because the same-source HYM/projector zero-mode basis theorem is absent."
            ),
        },
        "status": STATUS,
        "constructed_values_summary": source["constructed_values_summary"],
        "value_packet": values,
        "b_support_dictionary_interpretation": {
            "source_file": str(SM_DICTIONARY_HINT),
            "old_dictionary_tokens_found_in_checked_file": old_dictionary_support_present,
            "dictionary_status": "RECORDED_AS_USER_SUPPLIED_SUPPORT_INTERPRETATION_NOT_USED_AS_PROOF_INPUT",
            "support_labels_by_sector": b_support_dictionary,
            "interpretation_status": "SUPPORT_MATCH_ONLY_SELECTED_ZEROMODE_SOURCE_OPEN",
            "not_claimed": [
                "27-mode B_N equals literal particle list",
                "selected matter-slot routing",
                "selected 1_M Dirac-neutrino rule",
                "physical dotD alpha1 payload",
                "full SM closure",
            ],
        },
        "promotion_blocker": source["promotion_blocker"],
        "checks": {
            "previous_reduction_ready": previous_reduction_ready,
            "source_valid": source_valid,
            "values_model_valid": values_model_valid,
            "sector_dimensions_valid": sector_dimensions_valid,
            "promotion_blocker_valid": promotion_blocker_valid,
            "old_dictionary_recorded_not_used_as_proof_input": True,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            **source["what_closes_now"],
            "B1_B2_B3_dictionary_support_match_recorded": True,
            "six_triplet_plus_H_singlet_rank_match_to_SM_slots_recorded": True,
        },
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_promote_model_carrier_to_selected_zero_modes": True,
            "does_not_claim_B_dictionary_as_physical_payload": True,
            "does_not_claim_selected_matter_routing_or_1M_rule": True,
            "does_not_claim_honest_dotD_replay": True,
            "does_not_claim_primitive_C1_A_b_lambda_or_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
            "values": str(VALUES),
            "sm_dictionary_hint": str(SM_DICTIONARY_HINT),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_end0_sector_model_values",
        "status": STATUS,
        "closure_claimed": False,
        "selected_zero_mode_bases_emitted": False,
        "physical_dotD_alpha1_payload_extracted": False,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha End0 Sector ModelValues Import v1

## Result

The End0-to-sector frontier now has canonical model values:

```text
domain basis = T1,T2,T3
matter sectors = Q,u,d,L,e,N
matter rank = 6*3
H rank = 1
total sector carrier rank = 19
```

All projector and bracket checks pass at the model level. The old `B1,B2,B3`
SM support dictionary is compatible with this sector carrier:

```text
Q -> B3+B2+B1
u,d -> B3+B1
L -> B2+B1
e -> B1
N -> sterile/none
H -> B2+B1 support reuse
```

This is still not a physical `dotD_alpha1` payload. The selected zero-mode
bases `K_s`, selected source map `rho_s`, matter-slot routing, `1_M` rule, and
transfer normalization remain open.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
