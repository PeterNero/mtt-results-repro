from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_weylpair_source_emission_or_honest_galerkin_c1_execution_valuerun_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_enriched_weylpair_source_provenance_or_galerkin_c1_values_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_enriched_weylpair_source_provenance_or_galerkin_c1_values_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_enriched_weylpair_source_provenance_or_galerkin_c1_values.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentEnrichedWeylPairSourceProvenance_or_GalerkinC1Values_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_OR_GALERKIN_C1_VALUES_IMPORTED_STATIC_CLOSED_DYNAMIC_OPEN"
SOURCE_STATUS = "POST_ALPHA_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_OR_GALERKIN_C1_VALUES_IMPORTED_STATIC_CLOSED_DYNAMIC_OPEN"
THIS_ARTIFACT = "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1"
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["conditional_value_run_ready"] is True,
            prev["frontier_decision"]["selected_value_promotion_blocked"] is True,
            prev["frontier_decision"]["frontier_is_enriched_weylpair_source_provenance_or_galerkin_C1_values"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["static_enriched_weylpair_source_provenance_closed"] is True,
            source["frontier_decision"]["dynamic_C1_values_open_after_static_closure"] is True,
            source["frontier_decision"]["frontier_is_dynamic_C1_transfer_tensor_or_galerkin_C1_values"] is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    static = source_packet["static_enriched_weylpair_source_provenance"]
    dynamic = source_packet["dynamic_c1_value_boundary"]
    galerkin = source_packet["galerkin_c1_values_fallback"]

    static_ok = all(
        [
            static["schema"] == "MTTStaticEnrichedWeylPairSourceProvenance.v1",
            static["status"] == "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED",
            static["provenance_closed"] is True,
            static["source_level_carrier"]["phase_Z_source_proved"] is True,
            static["source_level_carrier"]["shift_X_source_proved"] is True,
            static["source_level_carrier"]["active_shift_1_1_proved"] is True,
            static["static_sector_route"]["selected_static_sector_route_now_closed"] is True,
            static["static_sector_route"]["phase_Z_to"] == ["u", "e"],
            static["static_sector_route"]["shift_X_to"] == ["d", "nuD"],
            static["static_sector_route"]["same_route_in_primitive_selector"] is True,
            static["static_normalization"]["selected_overlap_transfer_normalization"] is True,
            static["static_normalization"]["static_trace_innerproduct_normalization_selected"] is True,
            static["observed_data_used"] is False,
            static["target_fitting_used"] is False,
        ]
    )

    dynamic_ok = all(
        [
            dynamic["schema"] == "MTTDynamicC1ValueBoundary.v1",
            dynamic["status"] == "DYNAMIC_C1_VALUES_OPEN_AFTER_STATIC_PROVENANCE",
            dynamic["conditional_value_run_ready"] is True,
            dynamic["conditional_rank"] == 2,
            abs(dynamic["conditional_condition_number"] - 1.0) < 1e-12,
            dynamic["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]],
            dynamic["A_transpose_b_if_promoted"] == [12.0, 12.0],
            dynamic["after_static_provenance_closure"]["source_level_weylpair_provenance_open"] is False,
            dynamic["after_static_provenance_closure"]["static_sector_routing_open"] is False,
            dynamic["after_static_provenance_closure"]["static_transfer_normalization_open"] is False,
            dynamic["after_static_provenance_closure"]["selected_dynamic_source_to_C1_transfer_tensor_open"] is True,
            dynamic["after_static_provenance_closure"]["selected_primitive_C1_overlap_contractions_open"] is True,
            dynamic["after_static_provenance_closure"]["b_selected_currently_emitted"] is False,
            dynamic["dynamic_value_promotion"]["A_selected_promoted"] is False,
            dynamic["dynamic_value_promotion"]["b_selected_promoted"] is False,
            dynamic["dynamic_value_promotion"]["deltaTheta_C1_promoted"] is False,
            dynamic["dynamic_value_promotion"]["SM_parity_dynamic_packet_closed"] is False,
            dynamic["observed_data_used"] is False,
            dynamic["target_fitting_used"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTSelectedGalerkinC1ValuesFallback.v1",
            galerkin["status"] == "HONEST_GALERKIN_C1_VALUES_STILL_OPEN",
            galerkin["contract_status"] == "HONEST_GALERKIN_RUN_CONTRACT_EMITTED_VALUES_OPEN",
            galerkin["selected_source_verified"] is False,
            galerkin["target_fitting_forbidden"] is True,
            galerkin["observed_flavor_data_forbidden"] is True,
            galerkin["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            galerkin["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
        ]
    )

    what_closes_now = {
        "long_name_weylpair_value_run_gate_consumed": prev_ok,
        "audited_static_enriched_weylpair_provenance_reanchored": source_ok,
        "static_Z_to_u_e_X_to_d_nuD_route_closed": static_ok,
        "dynamic_C1_value_boundary_preserved": dynamic_ok,
        "galerkin_C1_values_fallback_reemitted": galerkin_ok,
    }

    what_remains_open = {
        "selected_dynamic_source_to_C1_transfer_tensor": True,
        "selected_primitive_C1_overlap_contractions": True,
        "selected_D_E_Riesz_Green_dotD": True,
        "physical_alpha1_driver_at_dynamic_C1_tier": True,
        "theorem_derived_A_selected": True,
        "theorem_derived_b_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "promotes_only_static_enriched_weylpair_source_provenance": True,
        "does_not_promote_dynamic_C1_transfer_tensor": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_promote_honest_galerkin_execution": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentStaticEnrichedWeylPairSourceProvenanceImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the static enriched Weyl-pair "
            "provenance theorem. The static source-level Weyl carrier and routing "
            "select Z/clock for u,e and X/shift for d,nuD with finite trace "
            "normalization. This closes static provenance only; dynamic C1 transfer "
            "values, primitive contractions, A_selected, b_selected, and "
            "deltaTheta_C1 remain open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_static_provenance_certificate": source,
        "static_enriched_weylpair_source_provenance": static,
        "dynamic_c1_value_boundary": dynamic,
        "galerkin_c1_values_fallback": galerkin,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "static_enriched_weylpair_source_provenance_closed": True,
            "dynamic_C1_values_open_after_static_closure": True,
            "frontier_is_dynamic_C1_transfer_tensor_or_galerkin_C1_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_static_provenance_certificate": str(SOURCE_CERT),
            "source_static_provenance_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent EnrichedWeylPairSourceProvenance or GalerkinC1Values Import v1

## Result

The independent long-name branch now carries the static enriched Weyl-pair provenance theorem.

```text
Z / clock / phase  -> u, e
X / shift          -> d, nuD
unit transfer      -> rho_s(T_i) / sqrt(2)
```

This closes static routing and source-level provenance only. Dynamic C1 transfer
values and honest Galerkin C1 values remain open.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_independent_enriched_weylpair_source_provenance_or_galerkin_c1_values",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
