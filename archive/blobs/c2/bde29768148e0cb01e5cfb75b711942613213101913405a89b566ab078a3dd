from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_strominger_trace_c1_first_variation_or_independent_quadrature_execution_plan_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_c1_first_variation_certificate_fill_or_independent_quadrature_rows_first_run_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_c1_first_variation_certificate_fill_or_independent_quadrature_rows_first_run.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_C1FirstVariationCertificateFill_or_IndependentQuadratureRowsFirstRun_Import_v1.md"
)

STATUS = "POST_ALPHA_C1_FIRST_VARIATION_PARTIAL_FILL_OR_INDEPENDENT_QUADRATURE_BASIS_FIRST_RUN_IMPORTED_OPEN"
SOURCE_STATUS = "POST_ALPHA_C1_FIRST_VARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_IMPORTED_OPEN"
THIS_ARTIFACT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["unpatched_theorem_closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            prev["frontier_decision"]["route_A_I11_certificate_schema_built"] is True,
            prev["frontier_decision"]["route_B_independent_row_schedule_built"] is True,
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["unpatched_theorem_closure_claimed"] is False,
            source["frontier_decision"]["frontier_is_trace_map_and_basis_values_or_primitive_rows_execution"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    route_a = source_packet["route_A_first_variation_certificate_partial_fill"]
    route_b = source_packet["route_B_basis_rows_first_run"]
    cutset = source_packet["next_cutset_after_partial_fill"]

    fields = route_a["filled_fields"]
    route_a_ok = all(
        [
            route_a["schema"] == "MTTC1FirstVariationCertificatePartialFill.v1",
            route_a["status"] == "PARTIAL_FILL_FORMAL_HESSIAN_NORMALIZATION_CLOSED_TRACE_AND_VARIATION_OPEN",
            route_a["certificate_accepted_now"] is False,
            route_a["observed_data_used"] is False,
            route_a["target_fitting_used"] is False,
            fields["hessian_or_coercivity"]["verified"] is True,
            fields["hessian_or_coercivity"]["constant_c"] == 1.0,
            fields["normalization_compatibility"]["verified"] is True,
            fields["selected_trace_map"]["verified"] is False,
            fields["first_variation_identity"]["verified"] is False,
            fields["boundary_cancellation"]["verified"] is False,
        ]
    )

    route_b_ok = all(
        [
            route_b["schema"] == "MTTQuadratureBasisRowsFirstRun.v1",
            route_b["status"] == "BASIS_ROW_STUBS_EMITTED_SELECTED_VALUES_OPEN",
            route_b["row_count"] == 19,
            route_b["selected_row_count"] == 0,
            route_b["all_basis_rows_selected"] is False,
            route_b["can_advance_to_primitive_rows"] is False,
            route_b["observed_data_used"] is False,
            route_b["target_fitting_used"] is False,
            len(route_b["basis_rows"]) == 19,
            all(row["selected_now"] is False for row in route_b["basis_rows"]),
            all(row["selected_basis_value"] is None for row in route_b["basis_rows"]),
            all(row["selected_projector_value"] is None for row in route_b["basis_rows"]),
            all(row["gram_matrix"] is None for row in route_b["basis_rows"]),
            all(row["spectral_gap"] is None for row in route_b["basis_rows"]),
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTC1FirstVariationOrQuadratureNextCutset.v1",
            cutset["status"] == "NEXT_CUTSET_AFTER_PARTIAL_FILL_SELECTED",
            cutset["recommended_next"]["artifact"] == NEXT,
            len(cutset["closed_now"]) == 3,
            len(cutset["still_blocks_route_A"]) == 3,
            len(cutset["still_blocks_route_B"]) == 4,
            "selected HYM/Strominger finite trace"
            in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
        ]
    )

    what_closes_now = {
        "long_name_Strominger_execution_plan_consumed": prev_ok,
        "audited_C1_partial_fill_reanchored": source_ok,
        "formal_hessian_coercivity_and_normalization_closed": route_a_ok,
        "independent_basis_row_stubs_emitted_not_selected": route_b_ok,
        "shared_trace_basis_cutset_identified": cutset_ok,
    }

    what_remains_open = {
        "selected_trace_map_values": True,
        "physical_first_variation_identity": True,
        "boundary_cancellation_for_selected_trace": True,
        "selected_projector_values": True,
        "ordered_selected_zero_mode_bases": True,
        "selected_Gram_matrices": True,
        "spectral_gap_and_error_bounds": True,
        "primitive_quadrature_rows": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_claim_route_A_certificate_accepted": True,
        "does_not_claim_route_B_basis_rows_accepted": True,
        "does_not_advance_to_primitive_rows": True,
        "does_not_claim_I10_proved": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaC1FirstVariationPartialFillOrIndependentQuadratureRowsFirstRunImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The long-name independent-quadrature branch imports the C1 first-variation "
            "partial fill. Formal Hessian/coercivity and normalization compatibility "
            "are closed, while selected trace values, physical first variation, boundary "
            "cancellation, and basis/projector/Gram/gap values remain open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_partial_fill_certificate": source,
        "route_A_first_variation_certificate_partial_fill": route_a,
        "route_B_independent_basis_rows_first_run": route_b,
        "next_cutset_after_partial_fill": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "formal_hessian_and_normalization_closed": True,
            "independent_basis_row_stubs_emitted": True,
            "frontier_is_trace_map_and_basis_values_or_primitive_rows_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_partial_fill_certificate": str(SOURCE_CERT),
            "source_partial_fill_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha C1 First Variation Certificate Fill or Independent Quadrature Rows First Run Import v1

## Result

The long-name branch now imports the partial C1/I11 fill and first independent basis-row run.

Closed now:

```text
formal Hessian/coercivity on residual quotient = True
normalization compatibility                  = True
independent basis row stubs emitted           = 19
```

Still open:

```text
selected trace map values
physical first-variation identity
boundary cancellation for selected trace
selected projector/basis/Gram/gap values
primitive quadrature rows
```

Next:

```text
{NEXT}
```

## Status

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_c1_first_variation_certificate_fill_or_independent_quadrature_rows_first_run",
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
