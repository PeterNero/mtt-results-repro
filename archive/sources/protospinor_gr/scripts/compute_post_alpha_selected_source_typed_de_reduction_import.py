from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_nonidentity_rhoe_bn_interface.packet.json"
RHOE = ROOT / "candidate_data" / "routec_nonidentity_rhoe_bn_construction_import.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json"
MONAD = QA / "candidate_data" / "monad_map_construction_or_source_augmentation.candidate.json"
AUTOMORPHY = QA / "candidate_data" / "iwasawa_automorphy_or_section_ring_construction.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_selected_source_typed_de_reduction_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_selected_source_typed_de_reduction.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SelectedSource_TypedDE_Reduction_v1.md"

STATUS = "POST_ALPHA_SELECTED_SOURCE_TYPED_DE_REDUCED_CONNECTION_WITNESS_OPEN"
NEXT = "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    rhoe = load(RHOE)
    source = load(SOURCE)
    monad = load(MONAD)
    automorphy = load(AUTOMORPHY)

    previous_interface_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["nonidentity_rhoE_BN_interface_built"] is True,
            prev["what_remains_open"]["selected_source_certificate"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1",
        ]
    )
    nonidentity_rhoe_numeric_available = all(
        [
            rhoe["theorem"]["proved"] is True,
            rhoe["verdict"]["nonidentity_rhoE_numeric_packet_built"] is True,
            rhoe["verdict"]["R2_metric_connection_numeric_gate_closed"] is True,
            rhoe["verdict"]["R2_source_promotion_closed"] is False,
            rhoe["verdict"]["R4_BN_payload_closed"] is False,
            rhoe["rho_E_candidate"]["selected_by_mtt"] is False,
        ]
    )
    source_reduction_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["decision"]["finite_prefix_has_nonidentity_rhoE_candidate"] is True,
            source["decision"]["finite_connection_prefix_values_present"] is True,
            source["decision"]["selected_routec_source_certificate_closed"] is False,
            source["decision"]["typed_DE_construction_closed"] is False,
            source["decision"]["selected_hym_connection_constructed"] is False,
            source["decision"]["selected_connection_witness_values_absent"] is True,
            source["decision"]["primitive_C1_values_computed"] is False,
            source["decision"]["A_selected_or_b_selected_emitted"] is False,
            source["decision"]["lambda_12_computable"] is False,
        ]
    )
    witness_contract_open = all(
        [
            source["reduction"]["q79_witness_search"]["selected_connection_witness_attempt"]["constructs_actual_selected_witness"]
            is False,
            source["reduction"]["q79_witness_search"]["selected_connection_witness_attempt"]["status"]
            == "OPEN_WITNESS_VALUES_ABSENT",
            all(
                value is None
                for value in source["reduction"]["q79_witness_search"]["selected_connection_witness_attempt"][
                    "candidate_values"
                ].values()
            ),
            source["reduction"]["q79_witness_search"]["routec_smoke_promotion_nogo"]["verdict"][
                "constructs_selected_connection_witness"
            ]
            is False,
            source["reduction"]["q79_witness_search"]["routec_smoke_promotion_nogo"]["selected_source_verified"]
            is False,
        ]
    )
    monad_section_ring_open = all(
        [
            monad["construction_result"]["charge_level_compatibility_passed"] is True,
            monad["construction_result"]["explicit_f_g_constructed"] is False,
            monad["construction_result"]["g_f_zero_checked"] is False,
            monad["construction_result"]["section_data_found"] is False,
            monad["construction_result"]["source_augmentation_required"] is True,
            automorphy["construction_result"]["symbolic_rank_one_relation_built"] is True,
            automorphy["construction_result"]["actual_automorphy_factors_found"] is False,
            automorphy["construction_result"]["explicit_f_g_constructed"] is False,
            automorphy["construction_result"]["g_f_zero_proved"] is False,
            automorphy["construction_result"]["qa_su3_closed"] is False,
        ]
    )
    guardrails_ok = all(
        [
            all(prev["guardrails"].values()),
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_selected_routec_source_certificate"] is False,
            source["guardrails"]["claims_typed_DE_construction"] is False,
            source["guardrails"]["claims_selected_HYM_connection_constructed"] is False,
            source["guardrails"]["claims_actual_selected_connection_witness_constructed"] is False,
            source["guardrails"]["claims_primitive_C1_values_computed"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_full_sm_closure"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
            monad["target_fitting_used"] is False,
            automorphy["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_interface_closed,
            nonidentity_rhoe_numeric_available,
            source_reduction_valid,
            witness_contract_open,
            monad_section_ring_open,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaSelectedSourceTypedDEReductionImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The non-identity rho_E/B_N fill attempt is reduced to an actual selected connection "
                "witness. The finite prefix contains useful nonidentity rho_E, D_E, dotD, C1-engine, "
                "and first HYM-correction values, but these are source-promotion open. Typed monad/Cech "
                "and automorphy routes currently provide charge compatibility and symbolic rank-one "
                "relations only; explicit f_i/g_i sections, automorphy factors, multiplication constants, "
                "g after f zero, exactness, selected HYM coefficients, and same-source residual certificates "
                "remain absent."
            ),
        },
        "status": STATUS,
        "finite_connection_prefix": source["reduction"]["finite_connection_prefix"],
        "witness_search": source["reduction"]["q79_witness_search"],
        "monad_construction": {
            "status": monad["status"],
            "charge_table": monad["charge_table"],
            "minimal_source_augmentation": monad["minimal_source_augmentation"],
            "gate_results": monad["gate_results"],
        },
        "automorphy_construction": {
            "status": automorphy["status"],
            "required_section_spaces": automorphy["required_section_spaces"],
            "symbolic_rank_one_relation": automorphy["symbolic_rank_one_relation"],
            "gate_results": automorphy["gate_results"],
        },
        "checks": {
            "previous_interface_closed": previous_interface_closed,
            "nonidentity_rhoe_numeric_available": nonidentity_rhoe_numeric_available,
            "source_reduction_valid": source_reduction_valid,
            "witness_contract_open": witness_contract_open,
            "monad_section_ring_open": monad_section_ring_open,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "selected_source_or_typed_DE_routes_classified": True,
            "finite_prefix_values_imported_as_nonclosing_support": True,
            "nonidentity_rhoE_numeric_candidate_carried_forward": True,
            "identity_rhoE_smoke_rejected_as_source": True,
            "typed_monad_charge_compatibility_imported": True,
            "automorphy_symbolic_rank_one_relation_imported": True,
            "selected_connection_witness_contract_localized": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_routec_source_certificate": True,
            "typed_f_i_sections": True,
            "typed_g_i_sections": True,
            "Cech_transitions_and_cocycle_data": True,
            "automorphy_factors": True,
            "section_bases_and_multiplication_constants": True,
            "g_after_f_zero_and_exactness_certificate": True,
            "selected_HYM_connection_coefficients": True,
            "selected_RouteC_residual_values": True,
            "honest_selected_DE_Riesz_Green_dotD": True,
            "selected_trace_equality_to_27mode_operator": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_promote_identity_rhoE_smoke": True,
            "does_not_promote_finite_prefix_values_to_selected_source": True,
            "does_not_claim_typed_monad_or_Cech_values": True,
            "does_not_claim_selected_HYM_connection": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "nonidentity_rhoe": str(RHOE),
            "source_reduction": str(SOURCE),
            "monad": str(MONAD),
            "automorphy": str(AUTOMORPHY),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_selected_source_typed_de_reduction",
        "status": STATUS,
        "closure_claimed": False,
        "selected_connection_witness_constructed": False,
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
    note = f"""# PostAlpha SelectedSource TypedDE Reduction v1

## Result

The non-identity `rho_E` / quotient-valid `B_N` fill attempt is reduced to an
actual selected connection witness.

Closed as support:

```text
nonidentity rho_E numeric candidate = true
finite 27-mode D_E/dotD prefix values = present
typed monad charge compatibility = true
automorphy symbolic rank-one relation = true
```

Still absent:

```text
typed f_i/g_i sections
Cech transition and cocycle data
automorphy factors and section bases
g after f = 0 exactness certificate
selected HYM/Route-C residual witness values
24 primitive C1 matrices
```

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
