"""Audit selected C1 routing, normalization, and overlap source packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_C1_ROUTING_NORMALIZATION_OVERLAP_SOURCE_ATTEMPT_BUILT_SELECTION_STILL_OPEN"
NEXT = "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    attempts = data["attempts"]
    verdict = data["selection_verdict"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False, data["closure_claimed"]),
        check(
            "conditional routing exact",
            attempts["c1_routing"]["conditional_route"]["matches_locked_columns"] is True
            and attempts["c1_routing"]["conditional_route"]["phase_residual"] == 0.0
            and attempts["c1_routing"]["conditional_route"]["shift_residual"] == 0.0,
            attempts["c1_routing"],
        ),
        check(
            "routing not selected independently",
            attempts["c1_routing"]["selected_source_independently_derives_route"] is False
            and attempts["c1_routing"]["selected_sector_routing_emitted"] is False,
            attempts["c1_routing"],
        ),
        check(
            "normalization not selected",
            attempts["normalization"]["conditional_residual_norm"] < 1e-12
            and attempts["normalization"]["selected_normalization_emitted"] is False
            and attempts["normalization"]["b_selected_emitted"] is False,
            attempts["normalization"],
        ),
        check(
            "overlap source open",
            attempts["overlap_source"]["selected_overlap_tensor_or_functor_emitted"] is False
            and attempts["overlap_source"]["enriched_weyl_pair_conditionally_sufficient"] is True,
            attempts["overlap_source"],
        ),
        check(
            "matter clues not promoted",
            attempts["matter_slot_evidence"]["su5_fixture_selected"] is False
            and attempts["matter_slot_evidence"]["honest_routec_uniformity_blocks_selected_split"] is True
            and attempts["matter_slot_evidence"]["singlet_1M_rule_present"] is False,
            attempts["matter_slot_evidence"],
        ),
        check(
            "verdict sharp",
            verdict["conditional_algebra_closed"] is True
            and verdict["selected_c1_routing_closed"] is False
            and verdict["selected_transfer_normalization_closed"] is False
            and verdict["selected_overlap_source_closed"] is False,
            verdict,
        ),
        check(
            "superset strategy declared",
            data["superset_strategy"]["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and data["superset_strategy"]["using_one_straight_path"] is False
            and data["superset_strategy"]["observed_data_used"] is False,
            data["superset_strategy"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records routes",
            "Live Routes" in note and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected C1 routing/normalization/overlap packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
