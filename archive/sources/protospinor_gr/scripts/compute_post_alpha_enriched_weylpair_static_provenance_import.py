from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_weylpair_source_emission_valuerun_certificate.json"

SM_CERT = SM_ROOT / "certificates" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
STATIC_PROVENANCE = SM_DIR / "static_enriched_weylpair_source_provenance.packet.json"
DYNAMIC_BOUNDARY = SM_DIR / "dynamic_c1_value_boundary.packet.json"
GALERKIN_FALLBACK = SM_DIR / "galerkin_c1_values_fallback.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_enriched_weylpair_static_provenance_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_enriched_weylpair_static_provenance.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_EnrichedWeylPair_StaticProvenance_Import_v1.md"

STATUS = "POST_ALPHA_ENRICHED_WEYLPAIR_STATIC_PROVENANCE_CLOSED_DYNAMIC_C1_VALUES_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferTensor_or_GalerkinC1Values_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    sm_cert = load(SM_CERT)
    sm_candidate = load(SM_CANDIDATE)
    static = load(STATIC_PROVENANCE)
    dynamic = load(DYNAMIC_BOUNDARY)
    fallback = load(GALERKIN_FALLBACK)

    previous_gate_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["conditional_value_run_ready"] is True,
            prev["frontier_decision"]["conditional_value_run_promoted"] is False,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_EnrichedWeylPairSourceProvenance_or_GalerkinC1Values_v1",
        ]
    )

    imported_theorem_ok = all(
        [
            sm_cert["theorem_proved"] is True,
            sm_cert["closure_claimed"] is False,
            sm_cert["SM_parity_dynamic_packet_closure_claimed"] is False,
            sm_cert["no_knob_closure_claimed"] is False,
            sm_cert["true_SM_equivalence_claimed"] is False,
            sm_cert["observed_data_used"] is False,
            sm_cert["target_fitting_used"] is False,
            sm_cert["next_required_artifact"] == NEXT,
            all(sm_cert["what_closes"].values()),
            all(sm_cert["what_remains_open"].values()),
            sm_candidate["theorem"]["proved"] is True,
            sm_candidate["closure_claimed"] is False,
            sm_candidate["promotion_decision"]["static_enriched_weylpair_source_provenance_promoted"] is True,
            sm_candidate["promotion_decision"]["dynamic_C1_transfer_tensor_promoted"] is False,
            sm_candidate["promotion_decision"]["A_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["b_selected_promoted"] is False,
            sm_candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            all(sm_candidate["what_closes_now"].values()),
            all(sm_candidate["what_remains_open"].values()),
        ]
    )

    static_provenance_ok = all(
        [
            static["schema"] == "MTTStaticEnrichedWeylPairSourceProvenance.v1",
            static["status"] == "STATIC_ENRICHED_WEYLPAIR_SOURCE_PROVENANCE_CLOSED",
            static["provenance_closed"] is True,
            static["observed_data_used"] is False,
            static["target_fitting_used"] is False,
            static["source_level_carrier"]["phase_Z_source_proved"] is True,
            static["source_level_carrier"]["shift_X_source_proved"] is True,
            static["source_level_carrier"]["active_shift_1_1_proved"] is True,
            static["static_sector_route"]["phase_Z_to"] == ["u", "e"],
            static["static_sector_route"]["shift_X_to"] == ["d", "nuD"],
            static["static_sector_route"]["selected_static_sector_route_now_closed"] is True,
            static["static_sector_route"]["same_route_in_primitive_selector"] is True,
            static["static_normalization"]["selected_overlap_transfer_normalization"] is True,
            static["static_normalization"]["static_trace_innerproduct_normalization_selected"] is True,
        ]
    )

    dynamic_boundary_ok = all(
        [
            dynamic["schema"] == "MTTDynamicC1ValueBoundary.v1",
            dynamic["status"] == "DYNAMIC_C1_VALUES_OPEN_AFTER_STATIC_PROVENANCE",
            dynamic["observed_data_used"] is False,
            dynamic["target_fitting_used"] is False,
            dynamic["conditional_value_run_ready"] is True,
            dynamic["conditional_rank"] == 2,
            dynamic["A_transpose_A_if_promoted"] == [[12.0, 0.0], [0.0, 12.0]],
            dynamic["A_transpose_b_if_promoted"] == [12.0, 12.0],
            dynamic["after_static_provenance_closure"]["source_level_weylpair_provenance_open"] is False,
            dynamic["after_static_provenance_closure"]["static_sector_routing_open"] is False,
            dynamic["after_static_provenance_closure"]["static_transfer_normalization_open"] is False,
            dynamic["after_static_provenance_closure"]["A_selected_currently_emitted"] is False,
            dynamic["after_static_provenance_closure"]["b_selected_currently_emitted"] is False,
            dynamic["after_static_provenance_closure"]["selected_dynamic_source_to_C1_transfer_tensor_open"] is True,
            dynamic["after_static_provenance_closure"]["selected_primitive_C1_overlap_contractions_open"] is True,
            dynamic["dynamic_value_promotion"]["A_selected_promoted"] is False,
            dynamic["dynamic_value_promotion"]["b_selected_promoted"] is False,
            dynamic["dynamic_value_promotion"]["deltaTheta_C1_promoted"] is False,
        ]
    )

    fallback_ok = all(
        [
            fallback["schema"] == "MTTSelectedGalerkinC1ValuesFallback.v1",
            fallback["status"] == "HONEST_GALERKIN_C1_VALUES_STILL_OPEN",
            fallback["selected_source_verified"] is False,
            fallback["current_manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            fallback["observed_flavor_data_forbidden"] is True,
            fallback["target_fitting_forbidden"] is True,
            fallback["would_close_SM_parity_dynamic_packet_if_values_emitted"] is True,
            fallback["would_close_no_knob_flavor_constants_if_values_emitted"] is False,
        ]
    )

    what_closes_now = {
        "previous_weylpair_value_run_gate_consumed": previous_gate_ok,
        "static_enriched_weylpair_source_provenance_imported": imported_theorem_ok,
        "source_level_Z_and_X_carrier_closed": static_provenance_ok,
        "dynamic_boundary_after_static_closure_imported": dynamic_boundary_ok,
        "honest_Galerkin_fallback_reemitted": fallback_ok,
    }

    what_remains_open = {
        "selected_dynamic_source_to_C1_transfer_tensor": True,
        "selected_primitive_C1_overlap_contractions": True,
        "selected_Hessian_or_b_source_vector": True,
        "theorem_derived_A_selected": True,
        "theorem_derived_b_selected": True,
        "selected_deltaTheta_C1": True,
        "selected_D_E_Riesz_Green_dotD_at_dynamic_tier": True,
        "physical_alpha1_driver_at_dynamic_C1_tier": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_promote_static_provenance_to_dynamic_C1_values": True,
        "does_not_promote_A_selected_or_b_selected": True,
        "does_not_promote_deltaTheta_C1": True,
        "does_not_claim_honest_Galerkin_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaEnrichedWeylPairStaticProvenanceImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The selected static enriched Weyl-pair provenance imports as closed: "
            "the source-level qutrit carrier supplies Z/clock to u,e and X/shift "
            "to d,nuD with selected finite trace normalization and no observed-data "
            "selector. This removes the static sector-route ambiguity but does not "
            "promote A_selected, b_selected, DeltaTheta_C1, or dynamic C1 values; "
            "the live frontier is the selected dynamic source-to-C1 transfer tensor, "
            "primitive C1 contractions, Hessian/source normalization, or honest "
            "Galerkin C1 values."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "static_source_provenance": {
            "phase_Z_to": static["static_sector_route"]["phase_Z_to"],
            "shift_X_to": static["static_sector_route"]["shift_X_to"],
            "active_shift_1_1_proved": static["source_level_carrier"]["active_shift_1_1_proved"],
            "source_level_carrier": static["source_level_carrier"]["carrier_statement"],
            "normalization": static["static_normalization"],
        },
        "dynamic_boundary": {
            "conditional_value_run_ready": dynamic["conditional_value_run_ready"],
            "conditional_rank": dynamic["conditional_rank"],
            "conditional_condition_number": dynamic["conditional_condition_number"],
            "conditional_deltaTheta": dynamic["conditional_deltaTheta"],
            "A_transpose_A_if_promoted": dynamic["A_transpose_A_if_promoted"],
            "A_transpose_b_if_promoted": dynamic["A_transpose_b_if_promoted"],
            "why_not_A_selected": dynamic["why_not_A_selected"],
            "open_dynamic_requirements": dynamic["open_dynamic_requirements"],
        },
        "honest_galerkin_required_outputs": fallback["required_outputs"],
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "static_enriched_weylpair_provenance_closed": True,
            "dynamic_C1_values_promoted": False,
            "frontier_is_dynamic_C1_transfer_tensor_or_galerkin_values": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_weylpair_value_run": str(PREV),
            "sm_static_provenance_certificate": str(SM_CERT),
            "sm_static_provenance_candidate": str(SM_CANDIDATE),
            "static_enriched_weylpair_source_provenance": str(STATIC_PROVENANCE),
            "dynamic_c1_value_boundary": str(DYNAMIC_BOUNDARY),
            "galerkin_c1_values_fallback": str(GALERKIN_FALLBACK),
        },
    }

    note = f"""# PostAlpha Enriched WeylPair Static Provenance Import v1

## Result

Static enriched Weyl-pair provenance is now closed locally:

```text
Z / clock / phase -> u,e
X / shift         -> d,nuD
active shift      -> (1,1)
finite trace transfer normalization selected
```

This is source-tier data, not a target fit. It closes the static sector-route
ambiguity.

Dynamic C1 values remain open:

```text
A_selected not emitted
b_selected not emitted
DeltaTheta_C1 not promoted
dynamic source-to-C1 transfer tensor open
primitive C1 overlap contractions open
honest selected Galerkin C1 values open
```

The conditional value run remains ready, but still unpromoted:

```text
rank = 2
condition number = 1.0000000000000002
DeltaTheta = [1.0, 1.0000000000000002]
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
```

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
        "certificate": "post_alpha_enriched_weylpair_static_provenance",
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
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
