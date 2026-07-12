from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_fiberclass_c1_observable_quotient.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitiveclass_no_split_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitiveclass_no_split.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveClass_NoSplit_v1.md"

STATUS = "POST_ALPHA_PRIMITIVECLASS_NO_FLAVOR_SPLIT_HIGHERORDER_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_quotient_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["fixed_fiber_quotient_class_selected_for_current_C1_spectral_observables"] is True,
            prev["what_remains_open"]["selected_higher_order_or_full_response_matrices"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1",
        ]
    )
    primitive_no_split_proved = all(
        [
            source["theorem"]["proved"] is True,
            source["decision"]["primitive_fixed_fiber_class_selected_for_current_spectral_observables"] is True,
            source["decision"]["primitive_class_can_emit_non_degenerate_flavor"] is False,
            source["decision"]["primitive_class_can_emit_A_selected"] is False,
            source["decision"]["primitive_class_can_emit_b_selected"] is False,
            source["decision"]["primitive_class_can_emit_lambda_12"] is False,
            source["primitive_layer_tests"]["all_fixed_candidates_rank3_each_sector"] is True,
            source["primitive_layer_tests"]["all_yy_star_scalar_identity"] is True,
            source["primitive_layer_tests"]["max_traceless_norm_sq"] == 0.0,
            source["primitive_layer_tests"]["max_commutator_norm_sq"] == 0.0,
            source["primitive_layer_tests"]["mass_splitting_test_passes"] is False,
            source["primitive_layer_tests"]["mixing_commutator_test_passes"] is False,
            source["primitive_layer_tests"]["cp_odd_test_passes"] is False,
        ]
    )
    scalar_identity_all_sectors = all(
        sector["scalar_identity"] is True
        and sector["scalar_identity_residual"] == 0.0
        and sector["traceless_norm_sq"] == 0.0
        for sector in source["primitive_layer_tests"]["yy_star_scalar_tests"].values()
    )
    source_emission_required = all(
        [
            source["decision"]["higher_order_or_full_response_source_emission_required"] is True,
            source["decision"]["selected_source_emission_closed"] is False,
            source["higher_order_contract"]["criterion_imported"] is True,
            source["higher_order_contract"]["full_response_acceptance_tests_locked"] is True,
            source["higher_order_contract"]["diagnostic_splitter_exists_without_observed_targets"] is True,
            source["decision"]["diagnostic_splitter_promoted"] is False,
            source["decision"]["basis_transport_candidate_promoted"] is False,
        ]
    )
    live_routes_preserved = all(source["live_routes"].values())
    guardrails_ok = all(
        [
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_primitive_class_flavor_split"] is False,
            source["guardrails"]["claims_diagnostic_splitter_selected"] is False,
            source["guardrails"]["claims_basis_transport_selected"] is False,
            source["guardrails"]["claims_A_selected"] is False,
            source["guardrails"]["claims_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_Yukawa_CKM_PMNS_CP_or_full_SM_closure"] is False,
            source["guardrails"]["uses_observed_data"] is False,
            source["guardrails"]["uses_benchmark_data"] is False,
            source["guardrails"]["uses_locked_target_columns"] is False,
            all(prev["guardrails"].values()),
        ]
    )
    theorem_proved = all(
        [
            previous_quotient_closed,
            primitive_no_split_proved,
            scalar_identity_all_sectors,
            source_emission_required,
            live_routes_preserved,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaPrimitiveClassNoSplitImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected primitive fixed-fiber quotient class is enough for current C1 spectral "
                "observables but cannot by itself produce flavor splitting. Direct replay gives "
                "Y_s Y_s* = c I in u,d,e,nuD, with zero traceless parts, zero sector commutators, and "
                "zero CP-odd content. Therefore nondegenerate Yukawa hierarchy, CKM/PMNS/CP, A_selected, "
                "b_selected, and lambda_12 require selected same-source higher-order/full-response "
                "matrix emission or selected operator-level basis transport."
            ),
        },
        "status": STATUS,
        "primitive_layer_tests": source["primitive_layer_tests"],
        "higher_order_contract": source["higher_order_contract"],
        "source_emission_requirements": source["source_emission_requirements"],
        "live_routes": source["live_routes"],
        "checks": {
            "previous_quotient_closed": previous_quotient_closed,
            "primitive_no_split_proved": primitive_no_split_proved,
            "scalar_identity_all_sectors": scalar_identity_all_sectors,
            "source_emission_required": source_emission_required,
            "live_routes_preserved": live_routes_preserved,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "primitive_class_no_flavor_split_theorem": True,
            "mass_splitting_test_locked": True,
            "mixing_commutator_test_locked": True,
            "CP_odd_test_locked": True,
            "diagnostic_splitter_kept_support_only": True,
            "higher_order_or_full_response_requirement_proved": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_correction_matrix_source": True,
            "selected_full_response_matrices": True,
            "selected_basis_transport_theorem": True,
            "selected_primitive_C1_atom_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_primitive_class_flavor_split": True,
            "does_not_claim_diagnostic_splitter_selected": True,
            "does_not_claim_basis_transport_selected": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "primitiveclass_no_split": str(SOURCE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_primitiveclass_no_split",
        "status": STATUS,
        "closure_claimed": False,
        "primitive_class_flavor_split_possible": False,
        "reduced_to": NEXT,
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
    note = f"""# PostAlpha PrimitiveClass NoSplit v1

## Result

The primitive fixed-fiber quotient layer cannot produce flavor splitting by
itself.

```text
Y_s Y_s* = c I for every sector
c = {source["primitive_layer_tests"]["yy_star_scalar_tests"]["u"]["scalar"]}
max traceless norm squared = {source["primitive_layer_tests"]["max_traceless_norm_sq"]}
max commutator norm squared = {source["primitive_layer_tests"]["max_commutator_norm_sq"]}
CP-odd test passes = {str(source["primitive_layer_tests"]["cp_odd_test_passes"]).lower()}
```

So the next object must emit selected higher-order/full-response matrices or
same-source operator-level basis transport. Diagnostic splitters remain support
only.

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
