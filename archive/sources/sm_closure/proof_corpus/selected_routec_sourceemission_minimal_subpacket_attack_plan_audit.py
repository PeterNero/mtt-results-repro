"""Audit source-emission minimal subpacket attack plan."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_sourceemission_minimal_subpacket_attack_plan.candidate.json"
CERT = REPO / "certificates" / "selected_routec_sourceemission_minimal_subpacket_attack_plan_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SOURCEEMISSION_MINIMAL_SUBPACKET_ATTACK_PLAN_BUILT"
NEXT = "MTT_Selected_RouteC_OperatorSourceIdentity_Subpacket_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    order = data["strategy"]["dependency_order"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False, data["closure_claimed"]),
        check("four ordered subpackets", [item["priority"] for item in order] == [1, 2, 3, 4], order),
        check("first subpacket selected", order[0]["next_artifact"] == NEXT and data["next_required_artifact"] == NEXT, order[0]),
        check("promotion condition present", "A_selected" in data["strategy"]["promotion_condition"], data["strategy"]),
        check("note records dependency order", "Dependency Order" in note and f"Next artifact: `{NEXT}`" in note, NOTE),
    ]
    print("\nMTT source-emission minimal subpacket attack plan audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
