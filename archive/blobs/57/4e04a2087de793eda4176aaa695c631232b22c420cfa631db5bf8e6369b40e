from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_i10_payload_certificate_or_quadrature_values_fill_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan.candidate.json"
SM_NOTE = SM_ROOT / "proof_corpus" / "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1.md"
SM_DIR = SM_ROOT / "candidate_data" / "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
FIRST_VARIATION = SM_DIR / "route_a_first_variation_certificate_plan.packet.json"
QUADRATURE_PLAN = SM_DIR / "route_b_quadrature_execution_manifest.packet.json"
ROW_SCHEDULE = SM_DIR / "quadrature_row_schedule.packet.json"
PAPER_DRAFT = SM_ROOT / "proof_corpus" / "paper_appendix_drafts" / "selected_source" / "theta_execution_flavor__i11_strominger_trace_c1_first_variation.md"

OUT_CERT = ROOT / "certificates" / "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_Import_v1.md"

STATUS = "POST_ALPHA_STROMINGER_TRACE_C1_FIRST_VARIATION_OR_QUADRATURE_EXECUTION_PLAN_IMPORTED_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    first = load(FIRST_VARIATION)
    quadrature = load(QUADRATURE_PLAN)
    schedule = load(ROW_SCHEDULE)
    source_note = SM_NOTE.read_text(encoding="utf-8")
    draft = PAPER_DRAFT.read_text(encoding="utf-8")

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_strominger_trace_c1_first_variation_or_quadrature_execution_plan"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["unpatched_theorem_closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "StromingerTraceC1FirstVariationOrQuadratureExecutionPlanTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["I10_proved"] is False,
            candidate["promotion_decision"]["route_A_first_variation_certificate_accepted"] is False,
            candidate["promotion_decision"]["route_B_quadrature_execution_accepted"] is False,
            candidate["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False,
            candidate["promotion_decision"]["true_SM_equivalence_closed"] is False,
            candidate["superset_strategy"]["locked_target"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            candidate["superset_strategy"]["locked_target"]["A_transpose_b"] == [12.0, 12.0],
            candidate["superset_strategy"]["locked_target"]["deltaTheta_C1"] == [1.0, 1.0],
            NEXT in source_note,
            "Theorem Slot I11" in draft,
        ]
    )

    first_variation_ok = all(
        [
            first["schema"] == "MTTStromingerTraceC1FirstVariationCertificatePlan.v1",
            first["status"] == "CERTIFICATE_PLAN_BUILT_VALUES_OPEN",
            first["route"] == "A",
            first["theorem_slot"] == "I11_strominger_trace_c1_first_variation",
            first["verified_now"] is False,
            first["observed_data_used"] is False,
            first["target_fitting_used"] is False,
            first["inputs_from_previous_attempt"]["no_observed_data_as_selector"] is True,
            first["inputs_from_previous_attempt"]["missing_payloads"]
            == [
                "defect_functional_minimizer_payload_verified",
                "selected_c1_response_payload_verified",
                "selected_minimizer_trace_payload_verified",
            ],
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
            first["would_close_if_all_verified"]["I10_proved"] is True,
            first["would_close_if_all_verified"]["unpatched_dynamic_packet_closed"] is True,
        ]
    )

    row_requirements = quadrature["row_requirements"]
    quadrature_ok = all(
        [
            quadrature["schema"] == "MTTQuadratureExecutionManifest.v1",
            quadrature["status"] == "EXECUTION_PLAN_BUILT_VALUES_OPEN",
            quadrature["route"] == "B",
            quadrature["accepted_now"] is False,
            quadrature["observed_data_used"] is False,
            quadrature["target_fitting_used"] is False,
            quadrature["previous_table_counts"]
            == {
                "hessian_source_rows": 0,
                "primitive_contraction_rows": 0,
                "sector_matrix_rows": 0,
                "zero_mode_basis_rows": 0,
            },
            row_requirements["zero_mode_basis_rows"]["count"] == 19,
            row_requirements["primitive_contraction_rows"]["count"] == 72,
            row_requirements["hessian_source_rows"]["count"] == 2,
            row_requirements["sector_matrix_rows"]["count"] == 36,
            all(req["filled_now"] is False for req in row_requirements.values()),
            quadrature["acceptance_equations"]["A_transpose_A_target"] == [[12.0, 0.0], [0.0, 12.0]],
            quadrature["acceptance_equations"]["A_transpose_b_target"] == [12.0, 12.0],
            quadrature["acceptance_equations"]["deltaTheta_C1_target"] == [1.0, 1.0],
            quadrature["acceptance_equations"]["rank_minimum"] == 2,
            "using measured masses, mixings, or CP phase as row targets"
            in quadrature["acceptance_equations"]["forbidden_shortcuts"],
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
            len(schedule["execution_order"][0]["rows"]) == 19,
            len(schedule["execution_order"][1]["rows"]) == 72,
            len(schedule["execution_order"][2]["rows"]) == 2,
            len(schedule["execution_order"][3]["rows"]) == 36,
        ]
    )

    what_closes_now = {
        "previous_I10_fill_cutset_consumed": prev_ok,
        "Strominger_C1_first_variation_plan_imported": imported_ok,
        "route_A_I11_certificate_fields_fixed": first_variation_ok,
        "route_B_quadrature_execution_manifest_fixed": quadrature_ok,
        "quadrature_row_schedule_fixed": schedule_ok,
    }

    what_remains_open = {
        "selected_trace_map_values": True,
        "first_variation_identity_verified": True,
        "hessian_or_coercivity_verified": True,
        "boundary_cancellation_verified": True,
        "normalization_compatibility_verified": True,
        "quadrature_basis_rows_executed": True,
        "quadrature_primitive_rows_executed": True,
        "quadrature_hessian_source_rows_executed": True,
        "quadrature_sector_matrix_rows_executed": True,
        "unpatched_SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_claim_I10_proved": True,
        "does_not_claim_I11_certificate_verified": True,
        "does_not_claim_quadrature_rows_executed": True,
        "does_not_promote_replay_A_b_or_deltaTheta_as_selected_values": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_unpatched_SM_closure": True,
        "does_not_claim_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaStromingerTraceC1FirstVariationOrQuadratureExecutionPlanImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "statement": (
            "The I10 blocker is converted into an executable two-route plan. Route A "
            "requires an I11 selected Strominger/HYM finite C1 trace first-variation "
            "certificate with selected trace map, first-variation identity, coercivity, "
            "boundary cancellation, and normalization compatibility. Route B requires "
            "executing the scheduled independent quadrature rows: 19 basis, 72 primitive, "
            "2 Hessian/source, and 36 sector rows. Neither route is accepted yet."
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
        "route_A_first_variation_certificate_plan": first,
        "route_B_quadrature_execution_manifest": quadrature,
        "quadrature_row_schedule": schedule,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_I11_certificate_schema_built": True,
            "route_B_row_schedule_built": True,
            "frontier_is_C1_first_variation_certificate_fill_or_quadrature_rows_first_run": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "route_A_first_variation_certificate_plan": str(FIRST_VARIATION),
            "route_B_quadrature_execution_manifest": str(QUADRATURE_PLAN),
            "quadrature_row_schedule": str(ROW_SCHEDULE),
            "paper_draft_I11": str(PAPER_DRAFT),
        },
    }

    note = f"""# PostAlpha Strominger Trace C1 First Variation or Quadrature Execution Plan Import v1

## Result

The next proof step is now executable.

Route A requires an I11 certificate with five unverified fields:

```text
selected trace map values
first-variation identity
Hessian/coercivity clause
boundary cancellation
normalization compatibility
```

Route B requires a first quadrature run:

```text
zero-mode basis rows       = 19
primitive contraction rows = 72
hessian/source rows        = 2
sector matrix rows         = 36
```

The locked replay target remains a target for acceptance, not selected data:

```text
A^T A = [[12, 0], [0, 12]]
A^T b = [12, 12]
deltaTheta_C1 = [1, 1]
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
        "certificate": "post_alpha_strominger_trace_c1_first_variation_or_quadrature_execution_plan",
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
