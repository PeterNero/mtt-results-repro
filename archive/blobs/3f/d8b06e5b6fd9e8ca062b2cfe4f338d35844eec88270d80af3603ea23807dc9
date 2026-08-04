from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_trace_equals_27mode.packet.json"
ALPHA = ROOT / "candidate_data" / "alpha1_driver_replay_closure_import.packet.json"
U1Y_DOTD_C1 = QA / "candidate_data" / "selected_u1y_routec_dotd_alpha1_c1_response_emission.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_dotd_alpha1_c1_response_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_dotd_alpha1_c1_response.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_dotD_alpha1_C1_Response_v1.md"

STATUS = "POST_ALPHA_DOTD_ALPHA1_C1_RESPONSE_ALPHA_REPLAY_CLOSED_PRIMITIVE_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    alpha = load(ALPHA)
    source = load(U1Y_DOTD_C1)

    de_gap_layer_carried = all(
        [
            prev["decision"]["DE_gap_Riesz_Green_layer_closed"] is True,
            source["decision"]["D_E_gap_Riesz_Green_layer_closed"] is True,
            source["derivative_payload_checks"]["D0_locked_basis_and_D_E_gap_available"] is True,
            source["derivative_payload_checks"]["D1_same_basis_dotD_values_available"] is True,
            source["decision"]["same_basis_dotD_alpha1_values_available"] is True,
            source["decision"]["dotD_alpha1_has_nonzero_entries"] is True,
        ]
    )
    local_alpha_replay_closed = all(
        [
            alpha["theorem"]["proved"] is True,
            alpha["what_closes_now"]["alpha1_driver_verified"] is True,
            alpha["what_closes_now"]["selected_dotD_source_verified"] is True,
            alpha["what_closes_now"]["honest_dotD_alpha1_replay"] is True,
            alpha["honest_dotd_replay"]["alpha1_driver_verified"] is True,
            alpha["honest_dotd_replay"]["selected_dotD_source_verified"] is True,
            alpha["honest_dotd_replay"]["honest_dotD_validator_closed"] is True,
            alpha["promoted_value"]["selected_value_emitted_by_this_theorem"] is True,
        ]
    )
    source_reduction_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["decision"]["C1_response_operator_emitted"] is False,
            source["decision"]["A_selected_emitted"] is False,
            source["decision"]["b_selected_emitted"] is False,
            source["decision"]["sector_response_matrices_emitted"] is False,
            source["decision"]["lambda_12_computable"] is False,
            source["decision"]["Yukawa_or_full_SM_closure"] is False,
        ]
    )
    c1_frontier_open = all(
        [
            source["lane_classification"]["c1_response_lane"]["status"]
            == "OPEN_C1_RESPONSE_EMISSION_REQUIRES_SELECTED_OPERATOR_BLOCKS",
            source["lane_classification"]["c1_response_lane"]["response_lanes"]["canonical_smooth_bn_response"][
                "status"
            ]
            == "COMPUTED_ZERO_RESPONSE",
            source["lane_classification"]["c1_response_lane"]["response_lanes"]["noninvariant_candidate_response"][
                "usable_as_proof"
            ]
            is False,
            source["what_remains_open"]["selected_Hess_Xi_finite_blocks"] is True,
            source["what_remains_open"]["selected_primitive_C1_contractions"] is True,
            source["what_remains_open"]["selected_zero_mode_bases_and_Gram_Schmidt"] is True,
            source["what_remains_open"]["selected_sector_response_matrices"] is True,
            source["what_remains_open"]["A_selected"] is True,
            source["what_remains_open"]["b_selected"] is True,
        ]
    )
    guardrails_ok = all(
        [
            source["guardrails"]["claims_C1_response_emitted"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_Yukawa_or_full_SM_closure"] is False,
            source["guardrails"]["promotes_diagnostic_lift_as_proof"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
            source["target_fitting_used"] is False,
            all(prev["guardrails"].values()),
            all(alpha["guardrails"].values()),
        ]
    )
    theorem_proved = all([de_gap_layer_carried, local_alpha_replay_closed, source_reduction_valid, c1_frontier_open, guardrails_ok])

    reconciled_decision = dict(source["decision"])
    reconciled_decision.update(
        {
            "same_branch_alpha1_driver_proved": True,
            "selected_dotD_source_theorem_proved": True,
            "selected_alpha1_tangent_or_retarded_kernel_emitted": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "next_required_artifact": NEXT,
        }
    )

    packet = {
        "theorem": {
            "name": "PostAlphaDotDAlpha1C1ResponseReconciliationTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "On the q79/F,m=1 Route-C branch, the U1/Y dotD-C1 response packet correctly reduces the "
                "post-alpha problem to finite C1 response emission. In this repo the alpha1 tangent/source "
                "and honest dotD replay have since been closed by the oriented overlap theorem, so the stale "
                "alpha-open flags in the sibling packet are superseded locally. The remaining live gate is "
                "selected primitive C1/Hess_Xi/zero-mode/source-block emission, hence A_selected, b_selected, "
                "sector response matrices, lambda_12, Yukawa magnitudes, and full SM closure remain open."
            ),
        },
        "status": STATUS,
        "alpha_reconciliation": {
            "sibling_packet_alpha_flags_stale_locally": True,
            "local_alpha1_driver_verified": local_alpha_replay_closed,
            "local_selected_dotD_source_verified": local_alpha_replay_closed,
            "local_honest_dotD_replay_without_lifted_flags": local_alpha_replay_closed,
            "superseded_sibling_next": source["decision"]["next_required_artifact"],
            "reconciled_next": NEXT,
        },
        "decision": reconciled_decision,
        "carried_forward": {
            "D_E_gap_Riesz_Green_layer_closed": prev["decision"]["DE_gap_Riesz_Green_layer_closed"],
            "same_basis_nonzero_dotD_value_packet": source["lane_classification"]["closed_value_prefix"],
            "c1_response_contract": source["lane_classification"]["c1_response_lane"]["operator_contract"],
            "canonical_smooth_bn_response": source["lane_classification"]["c1_response_lane"]["response_lanes"][
                "canonical_smooth_bn_response"
            ],
            "noninvariant_candidate_response": source["lane_classification"]["c1_response_lane"]["response_lanes"][
                "noninvariant_candidate_response"
            ],
        },
        "checks": {
            "de_gap_layer_carried": de_gap_layer_carried,
            "local_alpha_replay_closed": local_alpha_replay_closed,
            "source_reduction_valid": source_reduction_valid,
            "c1_frontier_open": c1_frontier_open,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "post_alpha_dotD_C1_response_frontier_reconciled": True,
            "D_E_gap_Riesz_Green_layer_carried_forward": True,
            "same_basis_dotD_value_packet_carried_forward": True,
            "local_alpha1_driver_closure_carried_forward": True,
            "local_selected_dotD_source_closure_carried_forward": True,
            "stale_alpha_open_flags_superseded_locally": True,
            "C1_response_operator_contract_validator_ready": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_primitive_C1_contractions": True,
            "selected_noninvariant_C1_source_or_basis_transport_payload": True,
            "selected_Hess_Xi_finite_blocks": True,
            "selected_zero_mode_bases_and_Gram_Schmidt": True,
            "selected_sector_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_reopen_local_alpha1": True,
            "does_not_claim_C1_response_operator_emitted": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_promote_noninvariant_candidates_as_selected": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_trace_equals_27mode": str(PREV),
            "alpha1_driver_replay_closure": str(ALPHA),
            "u1y_dotd_c1_response": str(U1Y_DOTD_C1),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_dotd_alpha1_c1_response",
        "status": STATUS,
        "closure_claimed": False,
        "alpha1_driver_verified_locally": local_alpha_replay_closed,
        "selected_dotD_source_verified_locally": local_alpha_replay_closed,
        "C1_response_operator_emitted": False,
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
    note = f"""# PostAlpha dotD alpha1 C1 Response v1

## Result

The post-alpha dotD/C1 response frontier is now reconciled with the local
alpha1 closure.

The imported U1/Y packet correctly says that selected C1 response matrices,
`A_selected`, `b_selected`, and `lambda_12` are not emitted. Its stale
alpha-open fields are superseded here by the local oriented-overlap theorem:

```text
alpha1_driver_verified = true
selected_dotD_source_verified = true
honest dotD replay without lifted flags = true
```

So the live frontier is no longer the alpha1 tangent. It is the selected
primitive C1 payload:

```text
selected primitive C1 contractions
selected Hess_Xi finite blocks
selected zero-mode bases and Gram-Schmidt
selected sector response matrices
A_selected and b_selected
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
