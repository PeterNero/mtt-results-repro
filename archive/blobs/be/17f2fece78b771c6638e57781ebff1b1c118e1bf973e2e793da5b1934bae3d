"""Import Route-C Strominger trace C1 first-variation / quadrature plan."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_i10_fill_cutset_import_certificate.json"
UPSTREAM_SLUG = "selected_stromingertracec1firstvariation_or_quadratureexecutionplan"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
ROUTE_A = UPSTREAM_DIR / "route_a_first_variation_certificate_plan.packet.json"
ROUTE_B = UPSTREAM_DIR / "route_b_quadrature_execution_manifest.packet.json"
ROW_SCHEDULE = UPSTREAM_DIR / "quadrature_row_schedule.packet.json"

OUTPUT_PACKET = DATA / "routec_strominger_execution_plan_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_strominger_execution_plan_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_StromingerExecutionPlan_Import_v1.md"

STATUS = "ROUTEC_STROMINGER_EXECUTION_PLAN_IMPORTED_C1_FILL_OR_QUADRATURE_ROWS_OPEN"
PREVIOUS_STATUS = "ROUTEC_I10_FILL_CUTSET_IMPORTED_STROMINGER_TRACE_OR_QUADRATURE_PLAN_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_STROMINGERTRACE_C1_FIRSTVARIATION_OR_QUADRATURE_EXECUTION_PLAN_BUILT_OPEN"
NEXT = "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    schedule = load(ROW_SCHEDULE)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")

    fields = route_a["certificate_fields"]
    rows = route_b["row_requirements"]
    locked = upstream["superset_strategy"]["locked_target"]

    required_first_variation_fields = [
        "selected_trace_map",
        "first_variation_identity",
        "hessian_or_coercivity",
        "boundary_cancellation",
        "normalization_compatibility",
    ]
    expected_rows = {
        "zero_mode_basis_rows": 19,
        "primitive_contraction_rows": 72,
        "hessian_source_rows": 2,
        "sector_matrix_rows": 36,
    }

    checks = {
        "P0_previous_cutset_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1",
        "P1_upstream_plan_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "P2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["next_required_artifact"] == NEXT,
        "P3_route_A_first_variation_schema_is_required_not_verified": route_a["theorem_slot"] == "I11_strominger_trace_c1_first_variation"
        and route_a["verified_now"] is False
        and route_a["observed_data_used"] is False
        and route_a["target_fitting_used"] is False
        and all(fields[key]["required"] is True for key in required_first_variation_fields)
        and all(fields[key]["verified_now"] is False for key in required_first_variation_fields),
        "P4_route_B_row_manifest_is_executable_not_filled": route_b["accepted_now"] is False
        and route_b["acceptance_equations"]["rank_minimum"] == 2
        and all(rows[key]["count"] == expected_rows[key] for key in expected_rows)
        and all(rows[key]["filled_now"] is False for key in expected_rows)
        and "using measured masses, mixings, or CP phase as row targets" in route_b["acceptance_equations"]["forbidden_shortcuts"],
        "P5_schedule_order_and_counts_preserved": schedule["status"] == "ROW_SCHEDULE_BUILT_NOT_EXECUTED"
        and schedule["executed_now"] is False
        and schedule["next_executable_stage"] == "basis"
        and [stage["stage"] for stage in schedule["execution_order"]] == [
            "basis",
            "primitive_contractions",
            "hessian_source",
            "sector_matrices",
        ],
        "P6_locked_replay_target_preserved": locked["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and locked["A_transpose_b"] == [12.0, 12.0]
        and locked["deltaTheta_C1"] == [1.0, 1.0],
        "P7_no_promotion_overclaim": all(upstream["promotion_decision"][key] is False for key in [
            "route_A_first_variation_certificate_accepted",
            "route_B_quadrature_execution_accepted",
            "I10_proved",
            "unpatched_A_selected_promoted",
            "unpatched_b_selected_promoted",
            "unpatched_deltaTheta_C1_promoted",
            "unpatched_SM_parity_dynamic_packet_closed",
            "true_SM_equivalence_closed",
        ])
        and "Route A now requires" in note
        and "Route B now has" in note,
    }

    execution_plan = {
        "route_A_required_first_variation_fields": required_first_variation_fields,
        "route_A_verified_now": route_a["verified_now"],
        "route_B_expected_row_counts": expected_rows,
        "route_B_accepted_now": route_b["accepted_now"],
        "row_execution_order": [stage["stage"] for stage in schedule["execution_order"]],
        "next_executable_stage": schedule["next_executable_stage"],
        "locked_target": locked,
    }

    return {
        "packet": "RouteC_StromingerExecutionPlan_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_route_A_plan": str(ROUTE_A),
            "upstream_route_B_manifest": str(ROUTE_B),
            "upstream_row_schedule": str(ROW_SCHEDULE),
        },
        "theorem": {
            "name": "RouteCStromingerExecutionPlanImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected Strominger/HYM trace C1 gate is reduced to an "
                "executable first-variation certificate fill or an independent "
                "quadrature row run.  No C1 values, selected A, selected b, or "
                "SM closure are promoted by this import."
            ),
        },
        "checks": checks,
        "execution_plan": execution_plan,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "route_a_first_variation_certificate_plan": route_a,
            "route_b_quadrature_execution_manifest": route_b,
            "quadrature_row_schedule": schedule,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_route_A_first_variation_certificate_accepted": False,
            "claims_route_B_quadrature_execution_accepted": False,
            "claims_I10_proved": False,
            "claims_selected_A": False,
            "claims_selected_b": False,
            "claims_selected_deltaTheta_C1": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCStromingerExecutionPlanImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "execution_plan": packet["execution_plan"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    plan = cert["execution_plan"]
    return f"""# RouteC Strominger Execution Plan Import v1

Status: `{cert["status"]}`.

The Strominger/HYM C1 gate is now executable, but not closed.

Route A first-variation fields still required:

```text
{plan["route_A_required_first_variation_fields"]}
```

Route B quadrature rows still required:

```text
{plan["route_B_expected_row_counts"]}
```

Execution order:

```text
{plan["row_execution_order"]}
```

Locked replay target remains:

```text
A^T A = {plan["locked_target"]["A_transpose_A"]}
A^T b = {plan["locked_target"]["A_transpose_b"]}
deltaTheta_C1 = {plan["locked_target"]["deltaTheta_C1"]}
```

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
