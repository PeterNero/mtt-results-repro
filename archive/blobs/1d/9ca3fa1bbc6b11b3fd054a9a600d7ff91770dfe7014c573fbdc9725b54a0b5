from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = (
    ROOT
    / "certificates"
    / "post_alpha_i10_payload_certificate_or_independent_quadrature_values_fill_certificate.json"
)
SOURCE_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "post_alpha_strominger_trace_c1_first_variation_or_independent_quadrature_execution_plan_certificate.json"
)
OUT_PACKET = (
    ROOT
    / "candidate_data"
    / "post_alpha_strominger_trace_c1_first_variation_or_independent_quadrature_execution_plan.packet.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "PostAlpha_StromingerTraceC1FirstVariation_or_IndependentQuadratureExecutionPlan_Import_v1.md"
)

STATUS = "POST_ALPHA_STROMINGER_TRACE_C1_FIRST_VARIATION_OR_INDEPENDENT_QUADRATURE_EXECUTION_PLAN_IMPORTED_OPEN"
SOURCE_STATUS = "POST_ALPHA_STROMINGER_TRACE_C1_FIRST_VARIATION_OR_QUADRATURE_EXECUTION_PLAN_IMPORTED_OPEN"
THIS_ARTIFACT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


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
            prev["frontier_decision"]["frontier_is_strominger_trace_c1_first_variation_or_quadrature_execution_plan"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            prev["frontier_decision"]["route_A_rejected_at_this_gate"] is True,
            prev["frontier_decision"]["route_B_rejected_at_this_gate"] is True,
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["unpatched_theorem_closure_claimed"] is False,
            source["frontier_decision"]["frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    first = source_packet["route_A_first_variation_certificate_plan"]
    quad = source_packet["route_B_quadrature_execution_manifest"]
    schedule = source_packet["quadrature_row_schedule"]

    route_a_ok = all(
        [
            first["schema"] == "MTTStromingerTraceC1FirstVariationCertificatePlan.v1",
            first["status"] == "CERTIFICATE_PLAN_BUILT_VALUES_OPEN",
            first["verified_now"] is False,
            first["observed_data_used"] is False,
            first["target_fitting_used"] is False,
            set(first["certificate_fields"].keys())
            == {
                "selected_trace_map",
                "first_variation_identity",
                "hessian_or_coercivity",
                "boundary_cancellation",
                "normalization_compatibility",
            },
            all(field["required"] is True for field in first["certificate_fields"].values()),
            all(field["verified_now"] is False for field in first["certificate_fields"].values()),
        ]
    )

    route_b_ok = all(
        [
            quad["schema"] == "MTTQuadratureExecutionManifest.v1",
            quad["status"] == "EXECUTION_PLAN_BUILT_VALUES_OPEN",
            quad["accepted_now"] is False,
            quad["observed_data_used"] is False,
            quad["target_fitting_used"] is False,
            quad["row_requirements"]["zero_mode_basis_rows"]["count"] == 19,
            quad["row_requirements"]["primitive_contraction_rows"]["count"] == 72,
            quad["row_requirements"]["hessian_source_rows"]["count"] == 2,
            quad["row_requirements"]["sector_matrix_rows"]["count"] == 36,
            all(req["filled_now"] is False for req in quad["row_requirements"].values()),
            quad["acceptance_equations"]["A_transpose_A_target"] == [[12.0, 0.0], [0.0, 12.0]],
            quad["acceptance_equations"]["A_transpose_b_target"] == [12.0, 12.0],
            quad["acceptance_equations"]["deltaTheta_C1_target"] == [1.0, 1.0],
        ]
    )

    schedule_ok = all(
        [
            schedule["schema"] == "MTTQuadratureRowSchedule.v1",
            schedule["status"] == "ROW_SCHEDULE_BUILT_NOT_EXECUTED",
            schedule["executed_now"] is False,
            schedule["next_executable_stage"] == "basis",
            [stage["stage"] for stage in schedule["execution_order"]]
            == ["basis", "primitive_contractions", "hessian_source", "sector_matrices"],
            [len(stage["rows"]) for stage in schedule["execution_order"]] == [19, 72, 2, 36],
        ]
    )

    what_closes_now = {
        "long_name_I10_independent_quadrature_cutset_consumed": prev_ok,
        "audited_Strominger_C1_execution_plan_reanchored": source_ok,
        "route_A_I11_certificate_fields_fixed": route_a_ok,
        "route_B_independent_quadrature_execution_manifest_fixed": route_b_ok,
        "independent_quadrature_row_schedule_fixed": schedule_ok,
    }

    what_remains_open = {
        "selected_trace_map_values": True,
        "first_variation_identity_verified": True,
        "hessian_or_coercivity_verified": True,
        "boundary_cancellation_verified": True,
        "normalization_compatibility_verified": True,
        "independent_quadrature_basis_rows_executed": True,
        "independent_quadrature_primitive_rows_executed": True,
        "independent_quadrature_hessian_source_rows_executed": True,
        "independent_quadrature_sector_matrix_rows_executed": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_proved": True,
        "does_not_claim_I11_certificate_verified": True,
        "does_not_claim_independent_quadrature_rows_executed": True,
        "does_not_promote_replay_A_b_or_deltaTheta_as_selected_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaStromingerTraceC1FirstVariationOrIndependentQuadratureExecutionPlanImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The long-name I10 independent-quadrature cutset is reanchored to the "
            "audited Strominger trace/C1 first-variation or quadrature execution plan. "
            "This fixes the next executable frontier without claiming the I11 "
            "certificate or independent quadrature rows have been filled."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_execution_plan_certificate": source,
        "route_A_first_variation_certificate_plan": first,
        "route_B_independent_quadrature_execution_manifest": quad,
        "independent_quadrature_row_schedule": schedule,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_I11_certificate_schema_built": True,
            "route_B_independent_row_schedule_built": True,
            "frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_execution_plan_certificate": str(SOURCE_CERT),
            "source_execution_plan_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Strominger Trace C1 First Variation or Independent Quadrature Execution Plan Import v1

## Result

The long-name I10 fill branch now reaches the same audited execution frontier:

```text
{NEXT}
```

Route A still requires the I11 first-variation certificate fields to be verified.
Route B still requires independent quadrature execution:

```text
zero-mode basis rows       = 19
primitive contraction rows = 72
hessian/source rows        = 2
sector matrix rows         = 36
```

No replay values are promoted as selected values.

## Status

```text
{STATUS}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_strominger_trace_c1_first_variation_or_independent_quadrature_execution_plan",
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
