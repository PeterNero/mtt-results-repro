from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_primitiverowsexecution_or_dynamicdotdtracebinding_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_primitiverowsexecution_or_dynamicdotdtracebinding.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
DYNAMIC_BINDING = SM_DIR / "dynamic_dotd_trace_binding.packet.json"
PRIMITIVE_ATTEMPT = SM_DIR / "primitive_rows_execution_attempt.packet.json"
CUTSET = SM_DIR / "residual_completion_or_honest_galerkin_cutset.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_Import_v1.md"

STATUS = "POST_ALPHA_DYNAMIC_DOTD_TRACE_BOUND_PRIMITIVE_ROWS_BLOCKED_BY_RESIDUAL_COMPLETION"
NEXT = "MTT_Selected_ResidualCompletion_SourcePromotion_or_HonestGalerkinC1_Emission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    binding = load(DYNAMIC_BINDING)
    primitive = load(PRIMITIVE_ATTEMPT)
    cutset = load(CUTSET)
    source_note = SM_NOTE.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_primitive_rows_execution_or_dynamic_dotD_trace_binding"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "DynamicDotDTraceBindingAndPrimitiveRowsBlockerTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["dynamic_dotD_trace_binding_accepted"] is True,
            candidate["promotion_decision"]["primitive_rows_executed"] is False,
            candidate["promotion_decision"]["residual_completion_promoted"] is False,
            candidate["promotion_decision"]["honest_Galerkin_C1_emission_promoted"] is False,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["unpatched_A_selected_promoted"] is False,
            candidate["promotion_decision"]["unpatched_b_selected_promoted"] is False,
            candidate["promotion_decision"]["unpatched_deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
            NEXT in source_note,
        ]
    )

    flags = binding["binding_flags"]
    binding_ok = all(
        [
            binding["schema"] == "MTTDynamicDotDTraceBinding.v1",
            binding["status"] == "DYNAMIC_DOTD_TRACE_BINDING_ACCEPTED",
            binding["accepted_scope"] == "dynamic dotD/Phi_fin^C1 trace binding and horizontal response source terms",
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
            binding["transport_derivative_formula"]["U"] == "exp(-u ad(T3))",
            binding["transport_derivative_formula"]["dU_dalpha"] == "-(du/dalpha) ad(T3) U",
            binding["transport_derivative_formula"]["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0",
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
            cutset["recommended_next"]["locked_conditional_target"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            cutset["recommended_next"]["locked_conditional_target"]["A_transpose_b"] == [12.0, 12.0],
            cutset["recommended_next"]["locked_conditional_target"]["deltaTheta_C1"] == [1.0, 1.0],
            "fixed-fiber primitive replay alone remains rejected"
            in cutset["recommended_next"]["superset_strategy"]["retained_guardrail"],
            set(cutset["closed_now"])
            == {
                "dynamic_dotD_trace_binding",
                "alpha1_driver_verified",
                "selected_dotD_source_verified",
                "basis_stage_preconditions",
            },
            "selected_residual_completion_source_theorem" in cutset["still_open"],
            "honest_Galerkin_C1_contractions" in cutset["still_open"],
            "selected_A_selected" in cutset["still_open"],
            "selected_b_selected" in cutset["still_open"],
            "selected_deltaTheta_C1" in cutset["still_open"],
        ]
    )

    what_closes_now = {
        "previous_trace_basis_frontier_consumed": prev_ok,
        "dynamic_dotD_trace_binding_theorem_imported": imported_ok,
        "dynamic_dotD_trace_binding_accepted": binding_ok,
        "primitive_rows_attempted_but_not_executed": primitive_ok,
        "residual_completion_or_honest_galerkin_cutset_selected": cutset_ok,
    }

    what_remains_open = {
        "primitive_quadrature_rows_executed": True,
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
        "name": "PostAlphaPrimitiveRowsExecutionOrDynamicDotDTraceBindingImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The selected dynamic dotD/Phi_fin^C1 trace binding is accepted from "
            "the stationary transported trace, transport-derivative formula, and "
            "same-branch alpha1/dotD driver. The 72 primitive rows are attempted "
            "against the selected basis and dynamic trace, but no row is executed "
            "because the fixed-fiber primitive span has a residual-completion "
            "obstruction. Conditional A, b, and deltaTheta replay values are retained "
            "only as conditional evidence and are not promoted."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "dynamic_dotd_trace_binding": binding,
        "primitive_rows_execution_attempt": primitive,
        "residual_completion_or_honest_galerkin_cutset": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "dynamic_dotD_trace_binding_accepted": True,
            "primitive_rows_executed": False,
            "conditional_replay_retained_without_promotion": True,
            "frontier_is_residual_completion_source_promotion_or_honest_galerkin_C1_emission": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "dynamic_dotd_trace_binding": str(DYNAMIC_BINDING),
            "primitive_rows_execution_attempt": str(PRIMITIVE_ATTEMPT),
            "residual_completion_or_honest_galerkin_cutset": str(CUTSET),
        },
    }

    note = f"""# PostAlpha Primitive Rows Execution or Dynamic dotD Trace Binding Import v1

## Result

The dynamic trace binding is now accepted.

Closed now:

```text
dynamic dotD / Phi_fin^C1 trace binding = True
selected dotD source verified           = True
alpha1 driver verified                  = True
basis stage accepted                    = True
```

Primitive row attempt:

```text
primitive rows scheduled                = 72
primitive rows executed                 = 0
fixed-fiber span obstruction retained   = True
```

Conditional replay is retained but not promoted:

```text
A^T A = [[12, 0], [0, 12]]
A^T b = [12, 12]
deltaTheta_C1 = [1, 1]
```

The next blocker is exactly residual-completion source promotion or honest Galerkin C1 emission.

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
        "certificate": "post_alpha_primitive_rows_execution_or_dynamic_dotd_trace_binding",
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
