"""Audit same-source matter-slot/overlap operator packet contract."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
CERT = REPO / "certificates" / "selected_routec_samesource_matter_slot_overlap_operator_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    fields = data["required_fields"]
    counts = data["field_counts"]
    status = data["same_source_status"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False and status["packet_closed"] is False, status),
        check(
            "field contract broad enough",
            counts["required"] == 7 and counts["support_present"] >= 5 and counts["selected_emitted"] < counts["required"],
            counts,
        ),
        check(
            "critical selected fields open",
            fields["matter_slot_charge"]["selected_emitted"] is False
            and fields["singlet_neutrino_rule"]["selected_emitted"] is False
            and fields["operator_values"]["selected_emitted"] is False
            and fields["overlap_transfer"]["selected_emitted"] is False
            and fields["normalization"]["selected_emitted"] is False
            and fields["primitive_contractions"]["selected_emitted"] is False,
            fields,
        ),
        check(
            "validator contract forbids shortcuts",
            "lifted selected-source flags" in data["validator_contract"]["must_reject"]
            and "unselected SU(5) fixture promotion" in data["validator_contract"]["must_reject"]
            and "observed masses, CKM, PMNS, CP phase, or benchmark matrices" in data["validator_contract"]["must_reject"],
            data["validator_contract"],
        ),
        check(
            "route decision sharp",
            data["route_decision"]["finite_algebra_route"] == "closed as conditional support"
            and data["route_decision"]["best_next_route"] == "fill or reject one same-source operator packet against the validator contract",
            data["route_decision"],
        ),
        check(
            "no target fitting",
            data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["target_fitting_used"] is False,
            data["superset_strategy"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records packet contract",
            "Required Fields" in note and "Current Status" in note and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT same-source matter-slot/overlap operator packet audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
