"""Import typed B_N retarded-derivative or primitive-response value emission."""

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

PREVIOUS = CERTS / "dynamic_overlap_or_c1primitive_source_emission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
SM_CERT = SM / "certificates" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission_certificate.json"

OUTPUT_PACKET = DATA / "typedbn_retarded_derivative_or_primitive_response_valueemission_import.candidate.json"
OUTPUT_CERT = CERTS / "typedbn_retarded_derivative_or_primitive_response_valueemission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_Import_v1.md"

STATUS = "TYPEDBN_OR_PRIMITIVE_RESPONSE_VALUEEMISSION_IMPORTED_SELECTOR_PROVENANCE_OPEN"
PREVIOUS_STATUS = "DYNAMIC_OVERLAP_OR_C1PRIMITIVE_REDUCTION_IMPORTED_TYPED_DERIVATIVE_VALUES_OPEN"
SM_STATUS = "MTT_SELECTED_TYPEDBN_RETARDEDDERIVATIVE_OR_PRIMITIVERESPONSE_VALUEEMISSION_BUILT_PRIMITIVE_CANDIDATES_UNSELECTED"
NEXT = "Selected_U1Y_RouteC_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    typed = sm_packet["typed_retarded_lane"]
    primitive = sm_packet["primitive_response_lane"]
    conditional = sm_packet["conditional_solver_packet"]
    remains = sm_packet["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_value_emission_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["primitive_response_candidate_values_emitted"] is True
        and sm_cert["selected_primitive_response_emitted"] is False
        and sm_cert["typed_retarded_derivative_emitted"] is False,
        "G2_typed_lane_tested_but_unselected": typed["attempted"] is True
        and typed["support_present"] is True
        and typed["selected_emitted"] is False
        and typed["partial_fill_closed"] is False,
        "G3_primitive_candidates_emitted_unselected": primitive["attempted"] is True
        and primitive["candidate_values_emitted"] is True
        and primitive["selected_emitted"] is False
        and primitive["active_shift_forced"] is True
        and primitive["fixed_fiber_candidate_count"] == 3
        and primitive["all_fixed_fiber_candidates_rank_three"] is True,
        "G4_all_fiber_candidates_unselected": all(
            item["selected_by_theorem"] is False
            and item["status"] == "STRUCTURAL_FINITE_CANDIDATE_UNSELECTED"
            and item["primitive_active_shift"] == [1, 1]
            for item in primitive["fixed_fiber_candidates"]
        ),
        "G5_conditional_solver_ready_not_selected": conditional["conditional_weylpair_A_exact"] is True
        and conditional["conditional_A_rank"] == 2
        and conditional["conditional_residual_norm"] < 1e-12
        and conditional["A_selected_claimed"] is False
        and conditional["b_selected_claimed"] is False,
        "G6_next_gate_is_selector_provenance": remains["selected_primitive_fiber_shift"] is True
        and remains["selected_retarded_source_selector"] is True
        and remains["selected_typed_BN_retarded_derivative"] is True
        and remains["selected_primitive_or_vertex_response"] is True,
        "G7_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_valueemission_packet": str(SM_PACKET),
            "sm_valueemission_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "TypedBNOrPrimitiveResponseValueEmissionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The typed B_N retarded-derivative lane was tested and remains "
                "support-only, while the primitive-response lane emits exact finite "
                "rank-3 candidates for fixed fiber shifts 0, 1, and 2 at active "
                "shift (1,1). These candidates are structural finite values, not "
                "selected values. The remaining proof gate is selector provenance: "
                "primitive fiber-shift source selector, typed retarded selector, "
                "or equivalent basis-transport/vertex theorem."
            ),
        },
        "checks": checks,
        "primitive_response_candidate_summary": {
            "active_shift": [1, 1],
            "fixed_fiber_shifts": [
                item["primitive_fiber_shift"] for item in primitive["fixed_fiber_candidates"]
            ],
            "rank_per_sector": 3,
            "sector_max_abs_entry": primitive["fixed_fiber_candidates"][0]["sector_max_abs_entry"],
            "selected_emitted": primitive["selected_emitted"],
            "why_not_promoted": primitive["why_not_promoted"],
        },
        "typed_retarded_lane_blockers": typed["blocking_fields"],
        "conditional_solver_packet": conditional,
        "selector_cutset": sm_packet["selector_cutset"],
        "what_remains_open": remains,
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Finite primitive values now exist as candidates. The next theorem "
                "must select a fiber shift or retarded selector without using the "
                "conditional Weyl solve as a selector."
            ),
        },
        "guardrails": {
            "primitive_response_candidate_values_emitted": True,
            "selected_primitive_response_emitted": False,
            "typed_retarded_derivative_emitted": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "TypedBNRetardedDerivativeOrPrimitiveResponseValueEmissionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "primitive_response_candidate_summary": packet["primitive_response_candidate_summary"],
        "frontier_update": packet["frontier_update"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    summary = packet["primitive_response_candidate_summary"]
    return f"""# TypedBN RetardedDerivative or PrimitiveResponse ValueEmission Import v1

Status: `{cert["status"]}`.

## Result

The primitive-response lane now has finite candidate values:

```json
{json.dumps(summary, indent=2, sort_keys=True)}
```

The typed `B_N` retarded-derivative lane remains support-only, and none of the
three primitive fiber shifts is selected by theorem.  `A_selected`,
`b_selected`, alpha1, and flavor data remain open.

Next artifact: `{packet["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
