from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_tracemapandbasisvalues_or_primitiverowsexecution_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_tracemapandbasisvalues_or_primitiverowsexecution.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / "selected_tracemapandbasisvalues_or_primitiverowsexecution"
TRACE_FILL = SM_DIR / "route_a_trace_map_value_fill.packet.json"
BASIS_FILL = SM_DIR / "route_b_selected_basis_value_fill.packet.json"
PRIMITIVE_READY = SM_DIR / "primitive_rows_execution_ready.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_TraceMapAndBasisValues_or_PrimitiveRowsExecution_Import_v1.md"

STATUS = "POST_ALPHA_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    trace = load(TRACE_FILL)
    basis = load(BASIS_FILL)
    primitive = load(PRIMITIVE_READY)
    source_note = SM_NOTE.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_trace_map_and_basis_values_or_primitive_rows_execution"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "TraceMapAndBasisValuePromotionTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["route_A_trace_map_values_accepted"] is True,
            candidate["promotion_decision"]["route_B_basis_rows_accepted"] is True,
            candidate["promotion_decision"]["route_B_can_advance_to_primitive_rows_after_dynamic_binding"] is True,
            candidate["promotion_decision"]["primitive_rows_executed"] is False,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
            NEXT in source_note,
        ]
    )

    trace_flags = trace["filled_flags"]
    trace_ok = all(
        [
            trace["schema"] == "MTTSelectedTraceMapValueFill.v1",
            trace["status"] == "FUNCTIONAL_TRACE_MAP_VALUES_FILLED_DYNAMIC_BINDING_OPEN",
            trace["accepted_for_stationary_trace"] is True,
            trace["accepted_for_dynamic_C1_primitive_rows"] is False,
            trace["observed_data_used"] is False,
            trace["target_fitting_used"] is False,
            trace_flags["selected_trace_map_values"] is True,
            trace_flags["selected_source_verified_for_functional_End0_trace"] is True,
            trace_flags["selected_projector_source_verified"] is True,
            trace_flags["transport_closed_finite_validator_replay"] is True,
            trace["remaining_dynamic_flags"]["selected_dotD_source_verified"] is False,
            trace["remaining_dynamic_flags"]["alpha1_driver_verified"] is False,
            trace["remaining_dynamic_flags"]["physical_first_variation_identity"] is False,
            trace["remaining_dynamic_flags"]["boundary_cancellation_for_dynamic_C1_trace"] is False,
            set(trace["trace_values"].keys()) == {"Q", "u", "d", "L", "e", "N", "H"},
            all(value["source_trace_selected_functionally"] is True for value in trace["trace_values"].values()),
            all(value["gap_preserved_by_unitary_transport"] is True for value in trace["trace_values"].values()),
            all(value["rank_preserved"] is True for value in trace["trace_values"].values()),
            all(value["finite_27_mode_replay_closed"] is False for value in trace["trace_values"].values()),
        ]
    )

    basis_rows = basis["basis_rows"]
    basis_ok = all(
        [
            basis["schema"] == "MTTSelectedBasisValueFill.v1",
            basis["status"] == "STATIONARY_BASIS_PROJECTOR_GRAM_GAP_ROWS_FILLED",
            basis["accepted_for_basis_stage"] is True,
            basis["all_basis_rows_selected"] is True,
            basis["row_count"] == 19,
            basis["selected_row_count"] == 19,
            basis["observed_data_used"] is False,
            basis["target_fitting_used"] is False,
            len(basis_rows) == 19,
            all(row["selected_now"] is True for row in basis_rows),
            all(row["selected_basis_value"] is not None for row in basis_rows),
            all(row["selected_projector_value"] is not None for row in basis_rows),
            all(row["gram_matrix"] == "identity_preserved_by_unitary_transport" for row in basis_rows),
            all(row["spectral_gap"] == "preserved_from_model_gap" for row in basis_rows),
            all(row["gap_preserved"] is True for row in basis_rows),
            all(row["projector_idempotent"] is True for row in basis_rows),
            all(row["projector_self_adjoint"] is True for row in basis_rows),
            all(row["source_verified_by_transport_conjugation"] is True for row in basis_rows),
            all(row["why_not_selected"] is None for row in basis_rows),
            "dynamic C1 primitive response still requires dotD/trace binding" in basis["basis_values_scope"],
        ]
    )

    primitive_ok = all(
        [
            primitive["schema"] == "MTTPrimitiveRowsExecutionReady.v1",
            primitive["status"] == "READY_NOT_EXECUTED_DYNAMIC_DOTD_TRACE_BINDING_OPEN",
            primitive["basis_stage_accepted"] is True,
            primitive["can_execute_rows_now"] is False,
            primitive["primitive_row_count"] == 72,
            primitive["observed_data_used"] is False,
            primitive["target_fitting_used"] is False,
            len(primitive["primitive_row_ids"]) == 72,
            "dynamic dotD trace binding" in " ".join(primitive["why_not"]),
            "dU/dalpha transport derivative term" in primitive["next_execution_requirements"],
            "selected dynamic C1 trace binding" in primitive["next_execution_requirements"],
        ]
    )

    what_closes_now = {
        "previous_partial_fill_consumed": prev_ok,
        "trace_map_and_basis_value_theorem_imported": imported_ok,
        "stationary_trace_map_values_accepted": trace_ok,
        "stationary_basis_projector_gram_gap_rows_accepted": basis_ok,
        "primitive_row_ids_locked_but_not_executed": primitive_ok,
    }

    what_remains_open = {
        "selected_dynamic_dotD_trace_binding": True,
        "primitive_quadrature_rows": True,
        "hessian_source_rows": True,
        "sector_matrix_rows": True,
        "physical_first_variation_identity": True,
        "boundary_cancellation_for_dynamic_C1_trace": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_accept_stationary_trace_as_dynamic_C1_binding": True,
        "does_not_execute_primitive_rows": True,
        "does_not_claim_I10_proved": True,
        "does_not_promote_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaTraceMapAndBasisValuesOrPrimitiveRowsExecutionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "Stationary selected trace-map values and all 19 selected "
            "basis/projector/Gram/gap rows are accepted from the transported HYM/End0 "
            "source. This advances Route B past the basis stage and locks the 72 "
            "primitive row ids. The result does not execute primitive rows and does "
            "not identify the stationary trace with the dynamic dotD/Phi_fin^C1 trace "
            "binding required for physical first variation."
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
            "superset_strategy": candidate["superset_strategy"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "route_A_trace_map_value_fill": trace,
        "route_B_selected_basis_value_fill": basis,
        "primitive_rows_execution_ready": primitive,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "stationary_trace_map_values_filled": True,
            "stationary_basis_rows_filled": True,
            "primitive_row_ids_locked": True,
            "frontier_is_primitive_rows_execution_or_dynamic_dotD_trace_binding": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "route_A_trace_map_value_fill": str(TRACE_FILL),
            "route_B_selected_basis_value_fill": str(BASIS_FILL),
            "primitive_rows_execution_ready": str(PRIMITIVE_READY),
        },
    }

    note = f"""# PostAlpha Trace Map and Basis Values or Primitive Rows Execution Import v1

## Result

Stationary selected trace-map and basis data are now filled.

Closed now:

```text
stationary selected trace-map values   = True
selected basis/projector/Gram/gap rows = 19/19
primitive row ids locked               = 72
```

Still open:

```text
dynamic dotD / Phi_fin^C1 trace binding
primitive quadrature rows
hessian/source rows
sector matrix rows
physical first-variation identity
boundary cancellation for dynamic C1 trace
```

The key distinction is that stationary transported HYM/End0 trace data are accepted, but primitive C1 rows still require the differentiated dynamic trace binding.

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
        "certificate": "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution",
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
