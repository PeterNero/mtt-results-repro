"""Import Route-C C1 partial fill and basis-row first-run gate."""

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

PREVIOUS = CERTS / "routec_strominger_execution_plan_import_certificate.json"
UPSTREAM_SLUG = "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
ROUTE_A_FILL = UPSTREAM_DIR / "route_a_first_variation_certificate_partial_fill.packet.json"
ROUTE_B_FIRST_RUN = UPSTREAM_DIR / "route_b_basis_rows_first_run.packet.json"
NEXT_CUTSET = UPSTREAM_DIR / "next_cutset_after_partial_fill.packet.json"

OUTPUT_PACKET = DATA / "routec_c1_partial_fill_basis_run_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_c1_partial_fill_basis_run_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_C1PartialFillBasisRun_Import_v1.md"

STATUS = "ROUTEC_C1_PARTIAL_FILL_BASIS_RUN_IMPORTED_TRACE_BASIS_VALUES_OPEN"
PREVIOUS_STATUS = "ROUTEC_STROMINGER_EXECUTION_PLAN_IMPORTED_C1_FILL_OR_QUADRATURE_ROWS_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_C1_FIRSTVARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_BUILT_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    route_a = load(ROUTE_A_FILL)
    route_b = load(ROUTE_B_FIRST_RUN)
    cutset = load(NEXT_CUTSET)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")

    fields = route_a["filled_fields"]
    basis_rows = route_b["basis_rows"]
    closed_fields = {
        "hessian_or_coercivity": fields["hessian_or_coercivity"],
        "normalization_compatibility": fields["normalization_compatibility"],
    }
    open_fields = {
        "selected_trace_map": fields["selected_trace_map"],
        "first_variation_identity": fields["first_variation_identity"],
        "boundary_cancellation": fields["boundary_cancellation"],
    }

    checks = {
        "C0_previous_execution_plan_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1",
        "C1_upstream_partial_fill_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "C2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["next_required_artifact"] == NEXT,
        "C3_formal_route_A_fields_closed_only": route_a["certificate_accepted_now"] is False
        and closed_fields["hessian_or_coercivity"]["verified"] is True
        and closed_fields["hessian_or_coercivity"]["constant_c"] == 1.0
        and closed_fields["normalization_compatibility"]["verified"] is True
        and all(field["verified"] is False for field in open_fields.values()),
        "C4_route_B_basis_rows_stubbed_not_selected": route_b["row_count"] == 19
        and route_b["selected_row_count"] == 0
        and route_b["all_basis_rows_selected"] is False
        and route_b["can_advance_to_primitive_rows"] is False
        and len(basis_rows) == 19
        and all(row["selected_now"] is False for row in basis_rows)
        and all(row["selected_basis_value"] is None for row in basis_rows)
        and all(row["selected_projector_value"] is None for row in basis_rows),
        "C5_next_cutset_sharpens_shared_missing_object": cutset["status"] == "NEXT_CUTSET_AFTER_PARTIAL_FILL_SELECTED"
        and cutset["recommended_next"]["artifact"] == NEXT
        and "selected HYM/Strominger finite trace" in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
        "C6_no_promotion_overclaim": all(upstream["promotion_decision"][key] is False for key in [
            "route_A_first_variation_certificate_accepted",
            "route_B_basis_rows_accepted",
            "route_B_can_advance_to_primitive_rows",
            "I10_proved",
            "unpatched_A_selected_promoted",
            "unpatched_b_selected_promoted",
            "unpatched_deltaTheta_C1_promoted",
            "unpatched_SM_parity_dynamic_packet_closed",
            "true_SM_equivalence_closed",
        ])
        and "formal Hessian/coercivity" in note
        and "basis row stubs emitted" in note,
    }

    partial_fill_summary = {
        "route_A_certificate_accepted": route_a["certificate_accepted_now"],
        "closed_formal_fields": {
            "hessian_or_coercivity": closed_fields["hessian_or_coercivity"]["verified"],
            "normalization_compatibility": closed_fields["normalization_compatibility"]["verified"],
        },
        "open_physical_fields": {key: value["verified"] for key, value in open_fields.items()},
        "basis_row_count": route_b["row_count"],
        "selected_basis_row_count": route_b["selected_row_count"],
        "can_advance_to_primitive_rows": route_b["can_advance_to_primitive_rows"],
        "basis_ids": [row["basis_id"] for row in basis_rows],
        "shared_missing_object": cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
    }

    return {
        "packet": "RouteC_C1PartialFillBasisRun_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_route_A_partial_fill": str(ROUTE_A_FILL),
            "upstream_route_B_basis_first_run": str(ROUTE_B_FIRST_RUN),
            "upstream_next_cutset": str(NEXT_CUTSET),
        },
        "theorem": {
            "name": "RouteCC1PartialFillBasisRunImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The formal residual-quotient Hessian/coercivity and normalization "
                "clauses are imported as closed, and the first quadrature basis run "
                "emits 19 row stubs.  Physical trace values, first variation, "
                "boundary cancellation, selected basis/projector/Gram/gap values, "
                "and primitive rows remain open."
            ),
        },
        "checks": checks,
        "partial_fill_summary": partial_fill_summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "route_a_first_variation_certificate_partial_fill": route_a,
            "route_b_basis_rows_first_run": route_b,
            "next_cutset_after_partial_fill": cutset,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_route_A_first_variation_certificate_accepted": False,
            "claims_route_B_basis_rows_accepted": False,
            "claims_route_B_can_advance_to_primitive_rows": False,
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
        "certificate": "RouteCC1PartialFillBasisRunImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "partial_fill_summary": packet["partial_fill_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["partial_fill_summary"]
    return f"""# RouteC C1 Partial Fill Basis Run Import v1

Status: `{cert["status"]}`.

Closed now:

```text
{s["closed_formal_fields"]}
```

Still open in Route A:

```text
{s["open_physical_fields"]}
```

Route B basis run:

```text
basis rows emitted = {s["basis_row_count"]}
selected rows      = {s["selected_basis_row_count"]}
advance primitive  = {s["can_advance_to_primitive_rows"]}
```

Shared missing object:

```text
{s["shared_missing_object"]}
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
