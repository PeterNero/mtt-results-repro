"""Import Route-C I10 payload / quadrature fill cutset attempt."""

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

PREVIOUS = CERTS / "routec_i10_payload_contract_import_certificate.json"
UPSTREAM_SLUG = "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
ROUTE_A = UPSTREAM_DIR / "route_a_i10_payload_certificate_fill_attempt.packet.json"
ROUTE_B = UPSTREAM_DIR / "route_b_independent_quadrature_values_fill_attempt.packet.json"
CUTSET = UPSTREAM_DIR / "minimal_next_cutset.packet.json"

OUTPUT_PACKET = DATA / "routec_i10_fill_cutset_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_i10_fill_cutset_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_I10FillCutset_Import_v1.md"

STATUS = "ROUTEC_I10_FILL_CUTSET_IMPORTED_STROMINGER_TRACE_OR_QUADRATURE_PLAN_OPEN"
PREVIOUS_STATUS = "ROUTEC_I10_PAYLOAD_CONTRACT_IMPORTED_VALUES_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_I10_PAYLOAD_OR_QUADRATURE_VALUES_FILL_ATTEMPT_BUILT_CUTSET_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    cutset = load(CUTSET)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    replay = upstream["replay_if_route_A_or_B_accepted"]

    payload_checks = route_a["payload_checks"]
    route_b_checks = route_b["acceptance_checks"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1",
        "F1_upstream_fill_attempt_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["route_A_accepted"] is False
        and cert["route_B_accepted"] is False
        and cert["next_required_artifact"] == NEXT,
        "F3_route_A_payloads_evaluated_not_accepted": route_a["status"] == "ATTEMPTED_NOT_ACCEPTED_SELECTED_PAYLOADS_OPEN"
        and route_a["accepted_now"] is False
        and payload_checks["selected_minimizer_trace_payload_verified"]["value"] is False
        and payload_checks["selected_c1_response_payload_verified"]["value"] is False
        and payload_checks["defect_functional_minimizer_payload_verified"]["value"] is False
        and payload_checks["no_observed_data_as_selector"]["value"] is True,
        "F4_route_B_tables_evaluated_empty_not_accepted": route_b["status"] == "ATTEMPTED_VALUES_EMPTY_NOT_ACCEPTED"
        and route_b["accepted_now"] is False
        and route_b["table_counts"] == {
            "zero_mode_basis_rows": 0,
            "primitive_contraction_rows": 0,
            "hessian_source_rows": 0,
            "sector_matrix_rows": 0,
        }
        and route_b_checks["no_patched_replay_copying"] is True
        and all(value is False for key, value in route_b_checks.items() if key != "no_patched_replay_copying")
        and len(route_b["why_values_not_filled"]) == 4,
        "F5_minimal_cutset_selected": cutset["status"] == "NEXT_CUTSET_SELECTED"
        and cutset["recommended_next"]["artifact"] == NEXT
        and cutset["route_A_minimal_cutset"] == [
            "selected_minimizer_trace_payload_verified",
            "selected_c1_response_payload_verified",
            "defect_functional_minimizer_payload_verified",
        ]
        and cutset["route_B_minimal_cutset"] == [
            "zero_mode_basis_rows",
            "primitive_contraction_rows",
            "hessian_source_rows",
            "sector_matrix_rows",
        ]
        and "straight_route" in cutset["recommended_next"]["superset_strategy"]
        and "parallel_route" in cutset["recommended_next"]["superset_strategy"],
        "F6_replay_and_remaining_gates_preserved": replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and all(upstream["what_remains_open"][key] is True for key in [
            "selected_minimizer_trace_payload_verified",
            "selected_c1_response_payload_verified",
            "defect_functional_minimizer_payload_verified",
            "independent_quadrature_values_filled",
            "unpatched_SM_parity_dynamic_packet_closure",
            "true_SM_equivalence_closure",
        ]),
        "F7_no_promotion_overclaim": all(upstream["promotion_decision"][key] is False for key in [
            "route_A_i10_payload_certificate_accepted",
            "route_B_independent_quadrature_values_accepted",
            "I10_proved",
            "unpatched_A_selected_promoted",
            "unpatched_b_selected_promoted",
            "unpatched_deltaTheta_C1_promoted",
            "unpatched_SM_parity_dynamic_packet_closed",
            "true_SM_equivalence_closed",
        ])
        and "Route A result" in note
        and "Route B result" in note,
    }

    summary = {
        "route_A_accepted": False,
        "route_B_accepted": False,
        "route_A_minimal_cutset": cutset["route_A_minimal_cutset"],
        "route_B_minimal_cutset": cutset["route_B_minimal_cutset"],
        "route_B_table_counts": route_b["table_counts"],
        "no_observed_data_as_selector": payload_checks["no_observed_data_as_selector"]["value"],
        "no_patched_replay_copying": route_b_checks["no_patched_replay_copying"],
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
    }

    return {
        "packet": "RouteC_I10FillCutset_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_route_A_attempt": str(ROUTE_A),
            "upstream_route_B_attempt": str(ROUTE_B),
            "upstream_cutset": str(CUTSET),
        },
        "theorem": {
            "name": "RouteCI10FillCutsetImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "Both I10 payload and independent quadrature fill routes are "
                "evaluated against current corpus packets.  Neither is accepted; "
                "the next exact blocker is selected trace/C1/first-variation payloads "
                "or independent quadrature rows."
            ),
        },
        "checks": checks,
        "i10_fill_cutset_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "route_a_i10_payload_certificate_fill_attempt": route_a,
            "route_b_independent_quadrature_values_fill_attempt": route_b,
            "minimal_next_cutset": cutset,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_route_A_accepted": False,
            "claims_route_B_accepted": False,
            "claims_I10_proved": False,
            "claims_unpatched_A_selected": False,
            "claims_unpatched_b_selected": False,
            "claims_unpatched_deltaTheta_C1": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCI10FillCutsetImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "i10_fill_cutset_summary": packet["i10_fill_cutset_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["i10_fill_cutset_summary"]
    return f"""# RouteC I10 Fill Cutset Import v1

Status: `{cert["status"]}`.

The I10 payload and independent quadrature fill attempts have been evaluated.
Neither route is accepted yet.

Route A cutset:

```text
{s["route_A_minimal_cutset"]}
```

Route B cutset:

```text
{s["route_B_minimal_cutset"]}
```

Current Route B table counts:

```text
{s["route_B_table_counts"]}
```

Replay remains fixed if either route later closes:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
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
