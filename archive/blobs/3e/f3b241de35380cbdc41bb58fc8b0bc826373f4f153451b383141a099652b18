"""Audit same-source operator packet fill/no-go attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
CERT = REPO / "certificates" / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY"
NEXT = "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    summary = data["fill_summary"]
    fields = data["attempted_selected_packet"]["fields"]
    validator = data["validator_report"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False, data["closure_claimed"]),
        check(
            "fill attempted but no selected emissions",
            summary["required_fields"] == 7
            and summary["support_present"] >= 6
            and summary["selected_emitted"] == 0
            and summary["nogo_for_current_scaffolds"] is True,
            summary,
        ),
        check(
            "critical absent or conditional fields identified",
            fields["singlet_neutrino_rule"]["support_present"] is False
            and fields["overlap_transfer"]["provenance"] == "locked_target_selection"
            and fields["normalization"]["provenance"] == "locked_target_selection"
            and fields["operator_values"]["selected_emitted"] is False,
            fields,
        ),
        check(
            "validator rejects attempted packet",
            validator["exit_code"] == 1
            and validator["ok"] is False
            and len(validator["errors"]) >= 7,
            validator,
        ),
        check(
            "A and b not promoted",
            data["attempted_selected_packet"]["packet_flags"]["promote_to_A_selected"] is False
            and data["attempted_selected_packet"]["packet_flags"]["promote_to_b_selected"] is False,
            data["attempted_selected_packet"]["packet_flags"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records no-go",
            "does not validate" in note and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT same-source operator packet fill/no-go audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
