from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun"
ROUTE_A = SM_DIR / "route_a_first_variation_certificate_partial_fill.packet.json"
ROUTE_B = SM_DIR / "route_b_basis_rows_first_run.packet.json"
CUTSET = SM_DIR / "next_cutset_after_partial_fill.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_Import_v1.md"

STATUS = "POST_ALPHA_C1_FIRST_VARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_IMPORTED_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    cutset = load(CUTSET)
    source_note = SM_NOTE.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "C1FirstVariationPartialFillAndBasisRowsFirstRunTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["route_A_first_variation_certificate_accepted"] is False,
            candidate["promotion_decision"]["route_B_basis_rows_accepted"] is False,
            candidate["promotion_decision"]["route_B_can_advance_to_primitive_rows"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
            NEXT in source_note,
        ]
    )

    fields = route_a["filled_fields"]
    route_a_ok = all(
        [
            route_a["schema"] == "MTTC1FirstVariationCertificatePartialFill.v1",
            route_a["status"] == "PARTIAL_FILL_FORMAL_HESSIAN_NORMALIZATION_CLOSED_TRACE_AND_VARIATION_OPEN",
            route_a["certificate_accepted_now"] is False,
            route_a["observed_data_used"] is False,
            route_a["target_fitting_used"] is False,
            route_a["functional_source_status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE",
            fields["hessian_or_coercivity"]["verified"] is True,
            fields["hessian_or_coercivity"]["constant_c"] == 1.0,
            fields["hessian_or_coercivity"]["scope"] == "formal C1 defect functional on the residual quotient span",
            fields["normalization_compatibility"]["verified"] is True,
            fields["selected_trace_map"]["verified"] is False,
            fields["first_variation_identity"]["verified"] is False,
            fields["boundary_cancellation"]["verified"] is False,
        ]
    )

    basis_rows = route_b["basis_rows"]
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
            route_b["zero_mode_bridge_status"] == "MTT_SELECTED_ZEROMODE_BASIS_HYM_PROJECTOR_THEOREM_REDUCED_VALUES_OPEN",
            len(basis_rows) == 19,
            all(row["selected_now"] is False for row in basis_rows),
            all(row["selected_basis_value"] is None for row in basis_rows),
            all(row["selected_projector_value"] is None for row in basis_rows),
            all(row["gram_matrix"] is None for row in basis_rows),
            all(row["spectral_gap"] is None for row in basis_rows),
            route_b["zero_mode_current_blockers"]["selected_zero_mode_bases_emitted"] is False,
            route_b["zero_mode_current_blockers"]["zero_mode_slot_values_filled"] is False,
        ]
    )

    cutset_ok = all(
        [
            cutset["schema"] == "MTTC1FirstVariationOrQuadratureNextCutset.v1",
            cutset["status"] == "NEXT_CUTSET_AFTER_PARTIAL_FILL_SELECTED",
            cutset["recommended_next"]["artifact"] == NEXT,
            cutset["closed_now"]
            == [
                "formal_hessian_coercivity_on_residual_quotient",
                "finite_trace_frobenius_normalization_scale_independence",
                "basis_row_id_schedule_materialized",
            ],
            cutset["still_blocks_route_A"]
            == [
                "selected_trace_map_values",
                "physical_first_variation_identity",
                "boundary_cancellation_for_selected_trace",
            ],
            cutset["still_blocks_route_B"]
            == [
                "selected_projector_values",
                "ordered_selected_zero_mode_bases",
                "selected_Gram_matrices",
                "spectral_gap_and_error_bounds",
            ],
            "selected HYM/Strominger finite trace"
            in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
        ]
    )

    what_closes_now = {
        "previous_execution_plan_consumed": prev_ok,
        "C1_first_variation_partial_fill_imported": imported_ok,
        "formal_hessian_coercivity_and_normalization_closed": route_a_ok,
        "basis_row_stubs_emitted_not_selected": route_b_ok,
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
        "name": "PostAlphaC1FirstVariationPartialFillOrQuadratureRowsFirstRunImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The I11 route is partially filled: formal Hessian/coercivity on the "
            "residual quotient and finite trace/Frobenius normalization scale "
            "independence are closed. Physical selected trace values, first variation, "
            "and boundary cancellation remain open. The quadrature route emits the "
            "19 basis row stubs but accepts none because selected projector, ordered "
            "basis, Gram, and gap values are not yet emitted."
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
        "route_A_first_variation_certificate_partial_fill": route_a,
        "route_B_basis_rows_first_run": route_b,
        "next_cutset_after_partial_fill": cutset,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "formal_hessian_and_normalization_closed": True,
            "basis_row_stubs_emitted": True,
            "frontier_is_trace_map_and_basis_values_or_primitive_rows_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "route_A_partial_fill": str(ROUTE_A),
            "route_B_basis_rows_first_run": str(ROUTE_B),
            "next_cutset": str(CUTSET),
        },
    }

    note = f"""# PostAlpha C1 First Variation Certificate Fill or Quadrature Rows First Run Import v1

## Result

The I11 certificate is partially filled, but not accepted.

Closed now:

```text
formal Hessian/coercivity on residual quotient = True
normalization scale-independence              = True
basis row stubs emitted                       = 19
```

Still open:

```text
selected trace map values
physical first-variation identity
boundary cancellation for selected trace
selected projector/basis/Gram/gap values
primitive quadrature rows
```

The shared missing object is now:

```text
selected HYM/Strominger finite trace plus sector projector/basis/Gram/gap values
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
        "certificate": "post_alpha_c1_first_variation_certificate_fill_or_quadrature_rows_first_run",
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
