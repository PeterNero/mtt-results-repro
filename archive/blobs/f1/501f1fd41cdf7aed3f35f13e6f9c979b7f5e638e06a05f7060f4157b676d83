from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_primitive_rows_execution_or_dynamic_dotd_trace_binding.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongPrimitiveRowsExecution_or_DynamicDotDTraceBinding_Import_v1.md"
)

STATUS = "POST_ALPHA_INDEPENDENT_LONG_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
PREV_STATUS = "POST_ALPHA_INDEPENDENT_LONG_TRACEMAP_AND_BASIS_VALUES_FILLED_INDEPENDENT_PRIMITIVE_ROWS_OPEN"
SOURCE_STATUS = "POST_ALPHA_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
THIS_ARTIFACT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["status"] == PREV_STATUS,
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_primitive_rows_execution_or_dynamic_dotD_trace_binding"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            prev["frontier_decision"]["stationary_trace_map_values_filled"] is True,
            prev["frontier_decision"]["stationary_basis_rows_filled"] is True,
            prev["frontier_decision"]["independent_primitive_row_ids_locked"] is True,
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
            source["unpatched_theorem_closure_claimed"] is False,
            source["frontier_decision"]["dynamic_dotD_trace_binding_accepted"] is True,
            source["frontier_decision"]["primitive_rows_executed"] is False,
            source["frontier_decision"]["conditional_replay_retained_without_promotion"] is True,
            source["frontier_decision"]["frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    binding = source_packet["dynamic_dotd_trace_binding"]
    primitive = source_packet["primitive_rows_execution_attempt"]
    cutset = source_packet["residual_completion_or_honest_galerkin_cutset"]

    flags = binding["binding_flags"]
    binding_ok = all(
        [
            binding["schema"] == "MTTDynamicDotDTraceBinding.v1",
            binding["status"] == "DYNAMIC_DOTD_TRACE_BINDING_ACCEPTED",
            binding["observed_data_used"] is False,
            binding["target_fitting_used"] is False,
            flags["stationary_trace_map_values_accepted"] is True,
            flags["selected_dotD_source_verified"] is True,
            flags["alpha1_driver_verified"] is True,
            flags["honest_dotD_alpha1_replay"] is True,
            flags["dU_dalpha_formula_closed"] is True,
            flags["dynamic_dotD_trace_binding_accepted"] is True,
            "primitive overlap contraction values" in binding["not_accepted_scope"],
            "A_selected" in binding["not_accepted_scope"],
            "b_selected" in binding["not_accepted_scope"],
            "deltaTheta_C1" in binding["not_accepted_scope"],
        ]
    )

    conditional = primitive["conditional_dynamic_values_retained"]
    primitive_ok = all(
        [
            primitive["schema"] == "MTTPrimitiveRowsExecutionAttempt.v1",
            primitive["status"] == "ATTEMPTED_NOT_EXECUTED_RESIDUAL_COMPLETION_OPEN",
            primitive["basis_stage_accepted"] is True,
            primitive["dynamic_trace_binding_accepted"] is True,
            primitive["row_count"] == 72,
            primitive["executed_row_count"] == 0,
            primitive["primitive_rows_executed"] is False,
            primitive["observed_data_used"] is False,
            primitive["target_fitting_used"] is False,
            len(primitive["rows"]) == 72,
            all(row["basis_stage_accepted"] is True for row in primitive["rows"]),
            all(row["dynamic_trace_binding_accepted"] is True for row in primitive["rows"]),
            all(row["executed_now"] is False for row in primitive["rows"]),
            primitive["span_obstruction_summary"]["pure_fixed_fiber_span_can_close"] is False,
            primitive["span_obstruction_summary"]["b_routed_residual_norm_sq"] == 12.0,
            conditional["A_conditional_shape"] == [72, 2],
            conditional["Gram_A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            conditional["A_transpose_b_conditional"] == [12.0, 12.0],
            conditional["deltaTheta_conditional_from_Gram_solve"] == [1.0, 1.0],
            conditional["rank"] == 2,
            conditional["condition_number"] == 1.0,
            conditional["relative_residual"] == 0.0,
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTResidualCompletionOrHonestGalerkinCutset.v1",
            cutset["status"] == "NEXT_CUTSET_SELECTED",
            cutset["recommended_next"]["artifact"] == NEXT,
            cutset["recommended_next"]["locked_conditional_target"]["A_transpose_A"]
            == [[12.0, 0.0], [0.0, 12.0]],
            cutset["recommended_next"]["locked_conditional_target"]["A_transpose_b"] == [12.0, 12.0],
            cutset["recommended_next"]["locked_conditional_target"]["deltaTheta_C1"] == [1.0, 1.0],
            "fixed-fiber primitive replay alone remains rejected"
            in cutset["recommended_next"]["superset_strategy"]["retained_guardrail"],
            "selected_residual_completion_source_theorem" in cutset["still_open"],
            "honest_Galerkin_C1_contractions" in cutset["still_open"],
        ]
    )

    what_closes_now = {
        "fresh_long_trace_basis_frontier_consumed": prev_ok,
        "audited_dynamic_dotD_trace_binding_reanchored": source_ok,
        "dynamic_dotD_trace_binding_accepted": binding_ok,
        "independent_primitive_rows_attempted_but_not_executed": primitive_ok,
        "residual_completion_or_honest_galerkin_cutset_selected": cutset_ok,
    }

    what_remains_open = {
        "independent_primitive_quadrature_rows_executed": True,
        "selected_residual_completion_source_theorem": True,
        "honest_Galerkin_C1_contractions": True,
        "hessian_source_rows": True,
        "sector_matrix_rows": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_promote_conditional_A_b_deltaTheta": True,
        "does_not_execute_primitive_rows": True,
        "does_not_claim_residual_completion_promoted": True,
        "does_not_claim_honest_galerkin_C1_emission": True,
        "does_not_claim_I10_proved": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaIndependentLongPrimitiveRowsExecutionOrDynamicDotDTraceBindingImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The fresh long-chain primitive branch imports acceptance of the dynamic "
            "dotD/Phi_fin^C1 trace binding. The 72 primitive rows are attempted but "
            "remain unexecuted because residual completion or honest Galerkin C1 "
            "emission is still required. Conditional A, b, and deltaTheta replay "
            "values are retained without promotion."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_dynamic_binding_certificate": source,
        "dynamic_dotd_trace_binding": binding,
        "independent_primitive_rows_execution_attempt": primitive,
        "residual_completion_or_honest_galerkin_cutset": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "dynamic_dotD_trace_binding_accepted": True,
            "independent_primitive_rows_executed": False,
            "conditional_replay_retained_without_promotion": True,
            "frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "fresh_previous_certificate": str(PREV),
            "source_dynamic_binding_certificate": str(SOURCE_CERT),
            "source_dynamic_binding_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha IndependentLong Primitive Rows Execution or Dynamic dotD Trace Binding Import v1

## Result

The fresh long-chain branch now accepts the dynamic trace binding.

Closed now:

```text
dynamic dotD / Phi_fin^C1 trace binding = true
selected dotD source verified           = true
alpha1 driver verified                  = true
basis stage accepted                    = true
```

Primitive rows remain attempted but unexecuted:

```text
primitive rows scheduled = 72
primitive rows executed  = 0
```

Conditional replay is retained but not promoted.

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
        "certificate": "post_alpha_independent_long_primitive_rows_execution_or_dynamic_dotd_trace_binding",
        "status": STATUS,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
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
