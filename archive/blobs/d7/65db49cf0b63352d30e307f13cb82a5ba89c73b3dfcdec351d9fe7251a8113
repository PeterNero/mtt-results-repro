"""Audit selected Route-C operator-source and overlap-tensor packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_operator_source_and_overlap_tensor_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_OVERLAP_PACKET_AUDITED_SOURCE_LEVEL_CARRIER_CLOSED_SELECTED_C1_ROUTING_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    operator = data["selected_operator_source"]
    overlap = data["selected_overlap_transport"]
    best = data["best_current_statement"]
    route_matrix = {row["route"]: row for row in data["route_matrix"]}

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("packet not closed", data["packet_goal"]["closed_now"] is False and data["closure_claimed"] is False, data["packet_goal"]),
        check(
            "source-level carrier closed but selected operator not emitted",
            operator["same_branch_source_level_weyl_carrier_closed"] is True
            and operator["active_shift_1_1_provenance_closed"] is True
            and operator["A_selected_emitted"] is False
            and operator["b_selected_emitted"] is False,
            operator,
        ),
        check(
            "conditional overlap sufficient but unselected",
            overlap["enriched_weyl_pair_span_sufficient_conditionally"] is True
            and overlap["conditional_weylpair_solve_exact"] is True
            and overlap["conditional_source_to_C1_transfer_exact"] is True
            and overlap["selected_sector_routing_emitted"] is False
            and overlap["selected_transfer_normalization_emitted"] is False,
            overlap,
        ),
        check(
            "retired routes stay retired",
            route_matrix["canonical smooth B_N overlap path"]["status"] == "RETIRED_FOR_NONZERO_C1"
            and route_matrix["non-invariant primitive-only path"]["status"] == "COUNTEREXAMPLE",
            route_matrix,
        ),
        check(
            "best statement is sharp",
            best["source_level_ZX_carrier_closed"] is True
            and best["conditional_A_weylpair_exact"] is True
            and best["selected_A_selected_closed"] is False
            and best["selected_overlap_tensor_closed"] is False
            and best["selected_sector_routing_closed"] is False,
            best,
        ),
        check(
            "missing object named",
            data["missing_selected_object"]["name"] == NEXT
            and "selected source-to-C1 transfer functor or overlap tensor T_selected" in data["missing_selected_object"]["must_emit"],
            data["missing_selected_object"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False and data["superset_strategy"]["observed_data_used"] is False,
            data["superset_strategy"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records packet",
            "What Is Closed" in note
            and "What Is Not Closed" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C operator-source/overlap packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
