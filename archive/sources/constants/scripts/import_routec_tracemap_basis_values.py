"""Import Route-C selected trace-map and basis-value promotion gate."""

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

PREVIOUS = CERTS / "routec_c1_partial_fill_basis_run_import_certificate.json"
UPSTREAM_SLUG = "selected_tracemapandbasisvalues_or_primitiverowsexecution"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
TRACE_FILL = UPSTREAM_DIR / "route_a_trace_map_value_fill.packet.json"
BASIS_FILL = UPSTREAM_DIR / "route_b_selected_basis_value_fill.packet.json"
PRIMITIVE_PLAN = UPSTREAM_DIR / "primitive_rows_execution_ready.packet.json"

OUTPUT_PACKET = DATA / "routec_tracemap_basis_values_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_tracemap_basis_values_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_TraceMapBasisValues_Import_v1.md"

STATUS = "ROUTEC_TRACEMAP_BASIS_VALUES_IMPORTED_DYNAMIC_DOTD_BINDING_OPEN"
PREVIOUS_STATUS = "ROUTEC_C1_PARTIAL_FILL_BASIS_RUN_IMPORTED_TRACE_BASIS_VALUES_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_TRACEMAP_AND_BASIS_VALUES_FILLED_PRIMITIVE_ROWS_OPEN"
NEXT = "MTT_Selected_PrimitiveRowsExecution_or_DynamicDotDTraceBinding_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    trace = load(TRACE_FILL)
    basis = load(BASIS_FILL)
    primitive = load(PRIMITIVE_PLAN)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")

    trace_flags = trace["filled_flags"]
    dynamic_flags = trace["remaining_dynamic_flags"]
    basis_rows = basis["basis_rows"]

    checks = {
        "T0_previous_partial_fill_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1",
        "T1_upstream_trace_basis_promotion_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "T2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["next_required_artifact"] == NEXT,
        "T3_stationary_trace_values_accepted_dynamic_trace_open": trace_flags["selected_trace_map_values"] is True
        and trace_flags["selected_source_verified_for_functional_End0_trace"] is True
        and trace_flags["selected_projector_source_verified"] is True
        and trace_flags["transport_closed_finite_validator_replay"] is True
        and trace["accepted_for_stationary_trace"] is True
        and trace["accepted_for_dynamic_C1_primitive_rows"] is False
        and dynamic_flags["selected_dotD_source_verified"] is False
        and dynamic_flags["alpha1_driver_verified"] is False,
        "T4_all_basis_projector_gram_gap_rows_selected": basis["row_count"] == 19
        and basis["selected_row_count"] == 19
        and basis["all_basis_rows_selected"] is True
        and basis["accepted_for_basis_stage"] is True
        and len(basis_rows) == 19
        and all(row["selected_now"] is True for row in basis_rows)
        and all(row["selected_basis_value"] is not None for row in basis_rows)
        and all(row["selected_projector_value"] is not None for row in basis_rows)
        and all(row["gram_matrix"] == "identity_preserved_by_unitary_transport" for row in basis_rows)
        and all(row["gap_preserved"] is True for row in basis_rows)
        and all(row["source_verified_by_transport_conjugation"] is True for row in basis_rows),
        "T5_primitive_rows_locked_not_executed": primitive["basis_stage_accepted"] is True
        and primitive["primitive_row_count"] == 72
        and primitive["can_execute_rows_now"] is False
        and "dynamic dotD trace binding" in " ".join(primitive["why_not"]),
        "T6_no_final_promotion_overclaim": upstream["promotion_decision"]["route_A_trace_map_values_accepted"] is True
        and upstream["promotion_decision"]["route_B_basis_rows_accepted"] is True
        and upstream["promotion_decision"]["route_B_can_advance_to_primitive_rows_after_dynamic_binding"] is True
        and upstream["promotion_decision"]["primitive_rows_executed"] is False
        and upstream["promotion_decision"]["I10_proved"] is False
        and upstream["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False
        and upstream["promotion_decision"]["true_SM_equivalence_closed"] is False
        and "stationary selected trace-map values" in note
        and "primitive row ids locked" in note,
    }

    trace_basis_summary = {
        "stationary_trace_map_values_accepted": trace["accepted_for_stationary_trace"],
        "dynamic_C1_trace_accepted": trace["accepted_for_dynamic_C1_primitive_rows"],
        "dynamic_flags": dynamic_flags,
        "basis_row_count": basis["row_count"],
        "selected_basis_row_count": basis["selected_row_count"],
        "basis_stage_accepted": basis["accepted_for_basis_stage"],
        "basis_ids": [row["basis_id"] for row in basis_rows],
        "primitive_row_count": primitive["primitive_row_count"],
        "primitive_rows_executed": primitive["can_execute_rows_now"],
        "primitive_blockers": primitive["why_not"],
    }

    return {
        "packet": "RouteC_TraceMapBasisValues_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_trace_fill": str(TRACE_FILL),
            "upstream_basis_fill": str(BASIS_FILL),
            "upstream_primitive_plan": str(PRIMITIVE_PLAN),
        },
        "theorem": {
            "name": "RouteCTraceMapBasisValuesImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Stationary selected trace-map values and all 19 selected "
                "basis/projector/Gram/gap rows are imported as accepted.  This "
                "advances Route B past the basis stage, but primitive C1 rows "
                "remain blocked by the selected dynamic dotD/Phi_fin^C1 trace "
                "binding."
            ),
        },
        "checks": checks,
        "trace_basis_summary": trace_basis_summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "route_a_trace_map_value_fill": trace,
            "route_b_selected_basis_value_fill": basis,
            "primitive_rows_execution_ready": primitive,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_primitive_rows_executed": False,
            "claims_physical_first_variation_identity": False,
            "claims_boundary_cancellation_for_dynamic_C1_trace": False,
            "claims_selected_A": False,
            "claims_selected_b": False,
            "claims_selected_deltaTheta_C1": False,
            "claims_I10_proved": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCTraceMapBasisValuesImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "trace_basis_summary": packet["trace_basis_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["trace_basis_summary"]
    return f"""# RouteC TraceMap Basis Values Import v1

Status: `{cert["status"]}`.

Accepted now:

```text
stationary trace-map values = {s["stationary_trace_map_values_accepted"]}
basis stage accepted        = {s["basis_stage_accepted"]}
selected basis rows         = {s["selected_basis_row_count"]}/{s["basis_row_count"]}
```

Primitive stage:

```text
primitive row ids locked = {s["primitive_row_count"]}
primitive rows executed  = {s["primitive_rows_executed"]}
blockers                 = {s["primitive_blockers"]}
```

Dynamic C1 status:

```text
dynamic C1 trace accepted = {s["dynamic_C1_trace_accepted"]}
dynamic flags             = {s["dynamic_flags"]}
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
