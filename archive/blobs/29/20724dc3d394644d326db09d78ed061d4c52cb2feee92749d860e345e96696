"""Audit selected matter-slot charge and overlap-normalization theorem attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET"
NEXT = "MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    finite = data["finite_matter_slot"]
    charge = data["matter_slot_charge"]
    overlap = data["overlap_normalization"]
    obstruction = data["same_source_obstruction"]
    theorem = data["theorem_attempt"]
    verdict = data["selection_verdict"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("no closure claimed", data["closure_claimed"] is False and theorem["fully_proved"] is False, theorem),
        check(
            "finite SU5 transversality imported but unselected",
            finite["under_transversality_closed"] is True
            and finite["retarded_q79_orientation_closed"] is True
            and finite["selected_packet"]["U_10"] == "I_3"
            and finite["selected_packet"]["U_bar5"] == "F"
            and finite["selected_mtt_source_present"] is False,
            finite,
        ),
        check(
            "matter-slot charge still open",
            charge["routeA_matches_required_partition"] is True
            and charge["routeB_current_selected_block_uniform"] is True
            and charge["singlet_1M_rule_present"] is False
            and charge["selected_charge_table_closed"] is False,
            charge,
        ),
        check(
            "overlap normalization still open",
            overlap["conditional_residual_norm"] < 1e-12
            and overlap["selected_normalization_emitted"] is False
            and overlap["selected_overlap_functor_emitted"] is False,
            overlap,
        ),
        check(
            "same-source obstruction identified",
            obstruction["all_su5_source_routes_blocked"] is True
            and obstruction["visible_selected_operator_source_closed"] is False
            and obstruction["critical_overlap_obligation"] is True
            and obstruction["critical_de_dotd_obligation"] is True,
            obstruction,
        ),
        check(
            "verdict reduces to same-source packet",
            verdict["finite_algebra_is_not_blocker"] is True
            and verdict["conditional_routing_and_normalization_are_exact"] is True
            and verdict["same_source_operator_packet_required"] is True
            and verdict["selected_matter_slot_charge_closed"] is False
            and verdict["selected_overlap_normalization_closed"] is False,
            verdict,
        ),
        check(
            "superset strategy declared",
            data["superset_strategy"]["mode"] == "CONSTRAINED_SUPERSET_WITH_LOCKED_TARGET"
            and data["superset_strategy"]["observed_data_used"] is False
            and data["superset_strategy"]["using_one_straight_path"] is False,
            data["superset_strategy"],
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records reduction",
            "What Closes" in note and "Why This Is Still Not Selected Closure" in note and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected matter-slot charge and overlap-normalization theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
