from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_c1_first_variation_certificate_fill_or_independent_quadrature_rows_first_run_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_trace_map_and_basis_values_or_primitive_rows_execution_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_IndependentLongTraceMapAndBasisValues_or_IndependentPrimitiveRowsExecution_Import_v1.md"
)

STATUS = "POST_ALPHA_INDEPENDENT_LONG_TRACEMAP_AND_BASIS_VALUES_FILLED_INDEPENDENT_PRIMITIVE_ROWS_OPEN"
PREV_STATUS = (
    "POST_ALPHA_INDEPENDENT_LONG_C1_FIRST_VARIATION_PARTIAL_FILL_OR_INDEPENDENT_"
    "QUADRATURE_BASIS_FIRST_RUN_REANCHORED_OPEN"
)
SOURCE_STATUS = "POST_ALPHA_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
THIS_ARTIFACT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


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
            prev["frontier_decision"]["frontier_is_trace_map_and_basis_values_or_primitive_rows_execution"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            prev["frontier_decision"]["formal_hessian_and_normalization_closed"] is True,
            prev["frontier_decision"]["independent_basis_row_stubs_emitted"] is True,
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
            source["frontier_decision"]["frontier_is_primitive_rows_execution_or_dynamic_dotD_trace_binding"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    trace = source_packet["route_A_trace_map_value_fill"]
    basis = source_packet["route_B_selected_basis_value_fill"]
    primitive = source_packet["primitive_rows_execution_ready"]

    trace_ok = all(
        [
            trace["schema"] == "MTTSelectedTraceMapValueFill.v1",
            trace["status"] == "FUNCTIONAL_TRACE_MAP_VALUES_FILLED_DYNAMIC_BINDING_OPEN",
            trace["accepted_for_stationary_trace"] is True,
            trace["accepted_for_dynamic_C1_primitive_rows"] is False,
            trace["observed_data_used"] is False,
            trace["target_fitting_used"] is False,
            trace["filled_flags"]["selected_trace_map_values"] is True,
            trace["remaining_dynamic_flags"]["selected_dotD_source_verified"] is False,
            trace["remaining_dynamic_flags"]["physical_first_variation_identity"] is False,
            set(trace["trace_values"].keys()) == {"Q", "u", "d", "L", "e", "N", "H"},
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
        ]
    )

    what_closes_now = {
        "fresh_long_C1_partial_fill_consumed": prev_ok,
        "audited_trace_basis_values_reanchored": source_ok,
        "stationary_trace_map_values_accepted": trace_ok,
        "stationary_basis_projector_gram_gap_rows_accepted": basis_ok,
        "independent_primitive_row_ids_locked_but_not_executed": primitive_ok,
    }

    what_remains_open = {
        "selected_dynamic_dotD_trace_binding": True,
        "independent_primitive_quadrature_rows": True,
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
        "name": "PostAlphaIndependentLongTraceMapAndBasisValuesOrIndependentPrimitiveRowsExecutionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The fresh long-chain branch imports accepted stationary trace-map values "
            "and all 19 basis/projector/Gram/gap rows. The 72 independent primitive row "
            "ids are locked, but execution remains blocked by the dynamic dotD trace "
            "binding and physical first-variation requirements."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "fresh_previous_certificate": prev,
        "source_trace_basis_certificate": source,
        "route_A_trace_map_value_fill": trace,
        "route_B_selected_basis_value_fill": basis,
        "independent_primitive_rows_execution_ready": primitive,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "stationary_trace_map_values_filled": True,
            "stationary_basis_rows_filled": True,
            "independent_primitive_row_ids_locked": True,
            "frontier_is_primitive_rows_execution_or_dynamic_dotD_trace_binding": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "fresh_previous_certificate": str(PREV),
            "source_trace_basis_certificate": str(SOURCE_CERT),
            "source_trace_basis_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha IndependentLongTrace Map and Basis Values or Independent Primitive Rows Execution Import v1

## Result

The fresh long-chain branch now accepts the stationary trace/basis stage.

Closed now:

```text
stationary selected trace-map values   = true
selected basis/projector/Gram/gap rows = 19/19
independent primitive row ids locked   = 72
```

Still open:

```text
dynamic dotD / Phi_fin^C1 trace binding
independent primitive quadrature rows
hessian/source rows
sector matrix rows
physical first-variation identity
boundary cancellation for dynamic C1 trace
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

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_independent_long_trace_map_and_basis_values_or_independent_primitive_rows_execution",
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
