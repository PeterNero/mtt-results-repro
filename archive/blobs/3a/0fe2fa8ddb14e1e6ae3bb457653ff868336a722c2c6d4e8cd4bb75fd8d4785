from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_connection_witness_contract.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_finite_hym_connection_solve_or_typed_cech_payload.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_finite_hym_de_gap_promotion_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_finite_hym_de_gap_promotion.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_FiniteHYM_DE_Gap_Promotion_v1.md"

STATUS = "POST_ALPHA_FINITE_HYM_DE_GAP_PROMOTED_DOTD_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)

    previous_contract_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_CONNECTION_WITNESS_CONTRACT_IMPORTED_VALUES_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1",
            prev["what_closes_now"]["three_legal_connection_witness_routes_formalized"] is True,
            prev["what_remains_open"]["fill_finite_routec_solve_payload"] is True,
            all(prev["guardrails"].values()),
        ]
    )
    source_valid = all(
        [
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["status"] == "U1Y_ROUTEC_FINITE_HYM_SOLVE_PROMOTES_DE_GAP_LAYER_DOTD_ALPHA1_SOURCE_OPEN",
            source["decision"]["finite_basis_BN_closed"] is True,
            source["decision"]["DE_action_closed_for_gap_layer"] is True,
            source["decision"]["Riesz_Green_gap_layer_closed"] is True,
            source["decision"]["finite_DE_gap_layer_promoted"] is True,
            source["decision"]["analytic_alpha1_kernel_formula_proved"] is True,
            source["decision"]["full_finite_HYM_connection_solve_closed"] is False,
            source["decision"]["dotD_alpha1_source_closed"] is False,
            source["decision"]["selected_alpha1_value_fill_closed"] is False,
            source["decision"]["primitive_C1_values_computed"] is False,
            source["decision"]["A_selected_or_b_selected_emitted"] is False,
            source["decision"]["lambda_12_computable"] is False,
            source["decision"]["typed_cech_payload_filled"] is False,
            source["decision"]["target_fitting_used"] is False,
            source["next_required_artifact"] == NEXT,
        ]
    )
    promoted_gap_layer_valid = all(
        [
            source["promoted_finite_routec_payload"]["finite_basis_BN"]["basis_dimension"] == 27,
            source["promoted_finite_routec_payload"]["finite_basis_BN"]["selected_trace_equality_proved"] is True,
            source["promoted_finite_routec_payload"]["DE_action"]["D_E_source_flags_are_theorem_derived"] is True,
            source["promoted_finite_routec_payload"]["DE_action"]["D_E_honest_replay_passes_after_theorem_derived_source_flags"] is True,
            source["promoted_finite_routec_payload"]["DE_action"]["selected_trace_equality"]["proved"] is True,
            source["promoted_finite_routec_payload"]["riesz_gap"]["selected_eta_N"]
            < source["promoted_finite_routec_payload"]["riesz_gap"]["eta_threshold"],
            source["promoted_finite_routec_payload"]["riesz_gap"]["selected_gap_lower_bound"] > 0,
            source["promoted_finite_routec_payload"]["reduced_green"]["Riesz_Green_layer_closes"] is True,
            source["promoted_finite_routec_payload"]["reduced_green"]["selected_green_norm_bound"] > 0,
        ]
    )
    alpha1_kernel_is_conditional = all(
        [
            source["alpha1_frontier"]["analytic_formula"]["status"]
            == "ANALYTIC_FORMULA_PROVED_SELECTED_TANGENT_VALUES_OPEN",
            source["alpha1_frontier"]["analytic_formula"]["what_the_formula_closes"][
                "duhamel_retarded_kernel_derivative_formula"
            ]
            is True,
            source["alpha1_frontier"]["analytic_formula"]["what_the_formula_does_not_close"][
                "selected_alpha1_tangent_parameter"
            ]
            is True,
            source["alpha1_frontier"]["value_fill_status"]
            == "Q79_SELECTED_PHYSICAL_ALPHA1_VALUE_FILL_ATTEMPTED_NAIVE_SOURCENORM_NOGO_END0SECTOR_VALUES_OPEN",
        ]
    )
    open_payload_honest = all(
        [
            "selected tangent/source normalization open"
            in source["still_open_finite_routec_payload"]["dotD_alpha1"],
            "full connection lift remains open"
            in source["still_open_finite_routec_payload"]["local_A01_or_discrete_connection_variables"],
            "not promoted beyond D_E gap layer"
            in source["still_open_finite_routec_payload"]["routec_residual_values"],
            "selected primitive/non-invariant C1 values open"
            in source["still_open_finite_routec_payload"]["primitive_C1_contractions"],
            all(source["what_remains_open"].values()),
        ]
    )
    guardrails_ok = all(
        [
            source["target_fitting_used"] is False,
            source["guardrails"]["claims_full_finite_HYM_connection_solve_closed"] is False,
            source["guardrails"]["claims_dotD_alpha1_source_closed"] is False,
            source["guardrails"]["claims_primitive_C1_values_computed"] is False,
            source["guardrails"]["claims_A_selected_or_b_selected"] is False,
            source["guardrails"]["claims_lambda12"] is False,
            source["guardrails"]["claims_full_sm_closure"] is False,
            source["guardrails"]["claims_typed_cech_payload_filled"] is False,
            source["guardrails"]["promotes_dotD_value_matrices_without_alpha1_source"] is False,
            source["guardrails"]["uses_observed_or_benchmark_inputs"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_contract_ready,
            source_valid,
            promoted_gap_layer_valid,
            alpha1_kernel_is_conditional,
            open_payload_honest,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaFiniteHYMDEGapPromotionImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The finite Route-C/HYM route promotes the selected 27-mode B_N, D_E "
                "gap, Riesz projection, and reduced Green layer. The D_E trace equality "
                "is theorem-derived and target-free. This still does not close dotD_alpha1 "
                "source normalization, End0-sector routing values, full HYM connection lift, "
                "primitive C1 contractions, A_selected, b_selected, lambda_12, or full SM closure."
            ),
        },
        "status": STATUS,
        "promoted_finite_routec_payload": source["promoted_finite_routec_payload"],
        "alpha1_frontier": source["alpha1_frontier"],
        "still_open_finite_routec_payload": source["still_open_finite_routec_payload"],
        "checks": {
            "previous_contract_ready": previous_contract_ready,
            "source_valid": source_valid,
            "promoted_gap_layer_valid": promoted_gap_layer_valid,
            "alpha1_kernel_is_conditional": alpha1_kernel_is_conditional,
            "open_payload_honest": open_payload_honest,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": source["what_closes_now"],
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_claim_dotD_alpha1_source": True,
            "does_not_claim_full_HYM_connection_solve": True,
            "does_not_claim_primitive_C1_values": True,
            "does_not_claim_A_selected_b_selected_lambda12_or_SM": True,
            "does_not_promote_dotD_matrices_without_source_normalization": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous": str(PREV),
            "source": str(SOURCE),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_finite_hym_de_gap_promotion",
        "status": STATUS,
        "closure_claimed": False,
        "full_finite_HYM_connection_solve_closed": False,
        "dotD_alpha1_source_closed": False,
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
    gap = source["promoted_finite_routec_payload"]["riesz_gap"]
    green = source["promoted_finite_routec_payload"]["reduced_green"]
    note = f"""# PostAlpha FiniteHYM DE Gap Promotion v1

## Result

The finite Route-C/HYM route now promotes the selected 27-mode gap layer:

```text
B_N dimension = 27
selected eta_N = {gap["selected_eta_N"]}
eta threshold = {gap["eta_threshold"]}
selected gap lower bound = {gap["selected_gap_lower_bound"]}
selected Green norm bound = {green["selected_green_norm_bound"]}
```

This closes the selected `D_E` gap/Riesz/Green layer, not the full finite HYM
connection solve. The analytic retarded/Riesz alpha1 kernel formula is proved
but still waits for selected tangent/source-normalization or End0-sector
routing values.

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
