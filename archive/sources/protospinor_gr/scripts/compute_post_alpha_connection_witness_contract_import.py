from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_selected_source_typed_de_reduction.packet.json"
CONTRACT = QA / "candidate_data" / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json"
PAYLOAD = QA / "candidate_data" / "selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_connection_witness_contract_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_connection_witness_contract.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ConnectionWitness_Contract_Import_v1.md"

STATUS = "POST_ALPHA_CONNECTION_WITNESS_CONTRACT_IMPORTED_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def none_payload(payload: dict) -> bool:
    return all(value is None for value in payload.values())


def main() -> None:
    prev = load(PREV)
    contract = load(CONTRACT)
    payload = load(PAYLOAD)

    previous_reduced_to_contract = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_SELECTED_SOURCE_TYPED_DE_REDUCED_CONNECTION_WITNESS_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1",
            prev["what_closes_now"]["selected_connection_witness_contract_localized"] is True,
            prev["what_remains_open"]["selected_HYM_connection_coefficients"] is True,
            prev["what_remains_open"]["selected_RouteC_residual_values"] is True,
            prev["what_remains_open"]["all_24_primitive_C1_3x3_matrices"] is True,
            all(prev["guardrails"].values()),
        ]
    )
    contract_import_valid = all(
        [
            contract["theorem"]["proved"] is True,
            contract["closure_claimed"] is False,
            contract["status"] == "U1Y_ROUTEC_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_CONTRACT_BUILT_VALUES_OPEN",
            contract["decision"]["contract_built"] is True,
            contract["decision"]["accepts_three_equivalent_witness_routes"] is True,
            contract["decision"]["selected_connection_witness_constructed"] is False,
            contract["decision"]["typed_monad_cech_values_present"] is False,
            contract["decision"]["direct_hym_values_present"] is False,
            contract["decision"]["finite_routec_solve_values_present"] is False,
            contract["decision"]["same_source_certificate_present"] is False,
            contract["decision"]["primitive_C1_values_computed"] is False,
            contract["decision"]["A_selected_or_b_selected_emitted"] is False,
            contract["decision"]["lambda_12_computable"] is False,
            contract["decision"]["honest_replay_still_blocked"] is True,
            contract["decision"]["payload_missing_leaf_count"] == 29,
            contract["next_required_artifact"] == NEXT,
        ]
    )
    open_payload_empty = all(
        [
            payload["status"] == "OPEN_VALUES_REQUIRED",
            payload["branch"]["q"] == 79,
            payload["branch"]["orientation"] == "F",
            payload["branch"]["torsion_label_m"] == 1,
            payload["branch"]["antiunitary_partner_retained"] is True,
            none_payload(payload["typed_monad_cech_payload"]),
            none_payload(payload["direct_hym_payload"]),
            none_payload(payload["finite_routec_solve_payload"]),
            payload["same_source_requirements"]["no_lifted_selected_flags"] is True,
            payload["same_source_requirements"]["no_observed_or_benchmark_inputs"] is True,
            payload["same_source_requirements"]["source_certificate"] is None,
            payload["same_source_requirements"]["same_branch_derivative"] is None,
            payload["same_source_requirements"]["same_source_ChernWeil_GS_row"] is None,
            payload["same_source_requirements"]["orientation_selection"] is None,
        ]
    )
    blocked_attempts_are_honest = all(
        [
            contract["blocked_current_attempts"]["typed_monad_cech"]["constructed"] is False,
            contract["blocked_current_attempts"]["direct_selected_hym_connection"]["constructed"] is False,
            contract["blocked_current_attempts"]["routec_smoke_promotion"]["constructed"] is False,
            contract["blocked_current_attempts"]["typed_monad_cech"]["status"] == "REJECTED_AS_WITNESS",
            contract["blocked_current_attempts"]["direct_selected_hym_connection"]["status"] == "ABSTRACT_EXISTENCE_ONLY",
            contract["blocked_current_attempts"]["routec_smoke_promotion"]["status"] == "CANNOT_PROMOTE_SMOKE_TO_SELECTED_WITNESS",
        ]
    )
    finite_prefix_carried_only_as_support = all(
        [
            contract["finite_prefix_support"]["dimension"] == 27,
            contract["finite_prefix_support"]["DE_emitted"] is True,
            contract["finite_prefix_support"]["dotD_alpha1_emitted"] is True,
            contract["finite_prefix_support"]["primitive_C1_engine_built"] is True,
            contract["finite_prefix_support"]["selected_by_mtt"] is False,
            contract["decision"]["finite_prefix_may_seed_but_not_fill_payload"] is True,
            contract["guardrails"]["promotes_finite_prefix_values"] is False,
            contract["guardrails"]["promotes_lifted_selected_flags"] is False,
        ]
    )
    guardrails_ok = all(
        [
            contract["target_fitting_used"] is False,
            contract["guardrails"]["claims_selected_connection_witness_constructed"] is False,
            contract["guardrails"]["claims_typed_monad_cech_witness_constructed"] is False,
            contract["guardrails"]["claims_direct_hym_connection_constructed"] is False,
            contract["guardrails"]["claims_finite_routec_solve_constructed"] is False,
            contract["guardrails"]["claims_primitive_C1_values_computed"] is False,
            contract["guardrails"]["claims_A_selected_or_b_selected"] is False,
            contract["guardrails"]["claims_lambda12"] is False,
            contract["guardrails"]["claims_full_sm_closure"] is False,
            contract["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_reduced_to_contract,
            contract_import_valid,
            open_payload_empty,
            blocked_attempts_are_honest,
            finite_prefix_carried_only_as_support,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaConnectionWitnessContractImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The selected connection witness gate is reduced to a precise three-route payload "
                "contract. A proof may close by typed monad/Cech data, direct selected HYM/Strominger "
                "connection data, or finite Route-C solve data with same-source provenance. The current "
                "payload contains no values; all finite 27-mode data remain support only, not proof."
            ),
        },
        "status": STATUS,
        "branch": payload["branch"],
        "witness_routes": contract["witness_routes"],
        "payload_counts": contract["payload_counts"],
        "open_payload": payload,
        "blocked_current_attempts": contract["blocked_current_attempts"],
        "finite_prefix_support": contract["finite_prefix_support"],
        "checks": {
            "previous_reduced_to_contract": previous_reduced_to_contract,
            "contract_import_valid": contract_import_valid,
            "open_payload_empty": open_payload_empty,
            "blocked_attempts_are_honest": blocked_attempts_are_honest,
            "finite_prefix_carried_only_as_support": finite_prefix_carried_only_as_support,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "three_legal_connection_witness_routes_formalized": True,
            "twenty_nine_payload_leaves_made_machine_readable": True,
            "abstract_HYM_existence_rejected_as_value_witness": True,
            "typed_charge_compatibility_rejected_as_Cech_witness": True,
            "finite_smoke_rejected_as_selected_source": True,
            "same_source_requirements_made_explicit": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "fill_typed_monad_cech_payload": True,
            "fill_direct_hym_payload": True,
            "fill_finite_routec_solve_payload": True,
            "same_source_certificate": True,
            "same_branch_derivative": True,
            "same_source_ChernWeil_GS_row": True,
            "orientation_selection": True,
            "selected_connection_witness": True,
            "primitive_C1_values": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_any_payload_values": True,
            "does_not_promote_abstract_HYM_existence": True,
            "does_not_promote_typed_charge_compatibility": True,
            "does_not_promote_finite_prefix_or_smoke_values": True,
            "does_not_claim_primitive_C1_A_b_lambda_or_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "contract": str(CONTRACT),
            "payload": str(PAYLOAD),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_connection_witness_contract",
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
    note = f"""# PostAlpha ConnectionWitness Contract Import v1

## Result

The selected connection witness gate is now a precise payload contract with
three legal closing routes:

```text
typed monad/Cech payload
direct selected HYM/Strominger connection payload
finite Route-C solve with same-source provenance
```

The current payload is empty: 29 required leaves are still missing. This is a
useful closure of ambiguity, not a closure of values.

Rejected as proof sources:

```text
abstract HYM existence alone
typed charge compatibility without f_i/g_i and Cech data
finite 27-mode smoke/prefix values without selected source provenance
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
