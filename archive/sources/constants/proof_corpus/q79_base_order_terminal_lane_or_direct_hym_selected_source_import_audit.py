"""Audit q79 base-order terminal-lane/direct HYM selected-source import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_q79_base_order_terminal_lane_or_direct_hym_selected_source.py"
PACKET = ROOT / "candidate_data" / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import.candidate.json"
CERT = ROOT / "certificates" / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Base_Order_Terminal_Lane_or_Direct_HYM_Selected_Source_Import_v1.md"

STATUS = "Q79_BASE_ORDER_TERMINAL_LANE_SELECTED_UNDER_EXPLICIT_PRINCIPLE_STABILITY_OPERATOR_OPEN"
NEXT = "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and cert match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("all import checks pass", all(packet["import_checks"].values()), packet["import_checks"])
    check("theorem proved as import", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not overclaimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])

    selected = packet["selected_terminal_source_under_principle"]
    check(
        "terminal source selects g3 L3-K2",
        selected["selection_derivation"]["selected_source_label"] == "g3 / L3-K2"
        and selected["selection_derivation"]["selected_L"] == [1, -2, 0]
        and selected["selection_derivation"]["selected_L2"] == [2, -4, 0],
        selected["selection_derivation"],
    )
    check(
        "principle explicit not unconditional",
        selected["source_principle"]["status"] == "EXPLICIT_PRINCIPLE_SYNTHESIZED_FROM_MTT_CORPUS"
        and "promoted into the main MTT axiomatic spine"
        in selected["source_principle"]["credibility_status"],
        selected["source_principle"],
    )
    check(
        "selected validators pass under principle",
        selected["validator_results"]["ordered_source"]["exit_code"] == 0
        and selected["validator_results"]["cohomology"]["exit_code"] == 0
        and selected["validator_results"]["cohomology"]["promotes_rank_two_route"] is True,
        selected["validator_results"],
    )
    check(
        "sign and base order closed for terminal g3",
        packet["sign_and_base_order"]["terminal_map_duality"][
            "physical_L_is_dual_of_printed_g3_terminal_map_type"
        ]
        is True
        and packet["sign_and_base_order"]["ordered_base_matrix_binding"][
            "appell_humbert_matrix_matches"
        ]
        is True,
        packet["sign_and_base_order"],
    )
    check(
        "only reduced AH stability imported",
        packet["stability_or_hym_status"]["reduced_AH_stability_proved"]["proved"] is True
        and packet["stability_or_hym_status"]["promotion_gap"]["full_stability_proved"] is False
        and packet["stability_or_hym_status"]["promotion_gap"]["hym_existence_proved"] is False,
        packet["stability_or_hym_status"]["promotion_gap"],
    )
    check(
        "remaining operator gates retained",
        packet["what_remains_open"]["same_source_DE_Riesz_Green_dotD"] is True
        and packet["what_remains_open"]["operator_layer_Pic0_recheck"] is True
        and packet["what_remains_open"]["primitive_C1_contractions"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "next artifact named",
        packet["verdict"]["base_order_gate_closed_under_explicit_principle"] is True
        and packet["verdict"]["selected_value_source_unconditional"] is False
        and packet["verdict"]["best_next_artifact"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "terminal admissible-section principle",
        "`g3 / L3-K2`",
        "`L=(1,-2,0)`",
        "`h1=8`",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 base-order terminal-lane/direct HYM selected-source import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
