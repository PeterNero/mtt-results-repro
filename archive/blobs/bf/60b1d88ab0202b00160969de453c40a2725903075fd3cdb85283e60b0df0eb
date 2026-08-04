"""Audit q79 selected L2 cochain/Ext or direct HYM value-packet fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill.py"
PACKET = ROOT / "candidate_data" / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill.candidate.json"
CERT = ROOT / "certificates" / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1.md"

STATUS = "Q79_SELECTED_L2_COCHAIN_EXT_VALUE_PACKET_FILLED_CONDITIONALLY_SOURCE_PROMOTION_OPEN"
NEXT = "Q79_Base_Order_Breaking_Terminal_Lane_Source_or_Direct_HYM_Selected_Source_v1"


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
    check("all packet checks pass", all(packet["packet_checks"].values()), packet["packet_checks"])
    check("theorem proved only as conditional fill", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not claimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])

    value = packet["finite_value_packet"]
    check(
        "target is L=(1,-2,0), L2=(2,-4,0)",
        value["target"]["l_vector_abc"] == [1, -2, 0]
        and value["target"]["c1_L_squared_vector_abc"] == [2, -4, 0],
        value["target"],
    )
    check(
        "cochain validates h1 and d1d0",
        value["cohomology"]["h1"] == 8
        and value["cohomology"]["d1_d0_zero"] is True
        and value["cohomology"]["rank_d0"] == 0
        and value["cohomology"]["rank_d1"] == 0,
        value["cohomology"],
    )
    check(
        "Ext vector closed non-exact",
        value["extension_class"]["basis_label"] == "theta_plus_0_tensor_eta_minus_0"
        and value["extension_class"]["vector_C1"] == [1, 0, 0, 0, 0, 0, 0, 0]
        and value["extension_class"]["closed"] is True
        and value["extension_class"]["exact"] is False
        and value["extension_class"]["nonzero_ext_class"] is True,
        value["extension_class"],
    )
    check(
        "still unselected fixture",
        value["source_status"]["candidate_role"] == "UNSELECTED_FIXTURE"
        and value["source_status"]["selected_by_mtt"] is False
        and value["source_status"]["fixture_only"] is True
        and value["validator"]["promotes_to_non_split_V_alpha_input"] is False,
        value["source_status"],
    )
    check(
        "source promotion blocker retained",
        packet["selected_promotion_blocker"]["status"] == "SOURCE_PROMOTION_OPEN"
        and "source.selected_by_mtt is not true"
        in packet["selected_promotion_blocker"]["ordered_source_open_items"]
        and packet["selected_promotion_blocker"]["minimal_source_theorem"]["name"]
        == "Base_Order_Breaking_Terminal_Lane_Source_v1",
        packet["selected_promotion_blocker"],
    )
    check(
        "direct HYM fallback remains open",
        packet["direct_hym_fallback"]["status"] == "OPEN"
        and "selected connection coefficients" in packet["direct_hym_fallback"]["required_payload"],
        packet["direct_hym_fallback"],
    )
    check(
        "remaining gates retained",
        packet["what_remains_open"]["selected_source_promotion"] is True
        and packet["what_remains_open"]["direct_selected_HYM_or_RouteC_residual"] is True
        and packet["what_remains_open"]["same_source_DE_Riesz_Green_dotD"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "next artifact named",
        packet["verdict"]["conditional_value_packet_closed"] is True
        and packet["verdict"]["selected_value_source_closed"] is False
        and packet["verdict"]["best_next_artifact"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "`L=(1,-2,0)`",
        "`h1=8`",
        "`UNSELECTED_FIXTURE`",
        "promotes_to_non_split_V_alpha_input=false",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 selected L2 cochain/Ext or direct HYM value-packet fill audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
