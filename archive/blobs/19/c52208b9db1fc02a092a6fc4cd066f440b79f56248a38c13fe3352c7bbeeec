"""Audit q79 selected visible bundle/direct HYM value-source search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_q79_selected_visible_bundle_or_direct_hym_value_source_search.py"
PACKET = ROOT / "candidate_data" / "q79_selected_visible_bundle_or_direct_hym_value_source_search.candidate.json"
CERT = ROOT / "certificates" / "q79_selected_visible_bundle_or_direct_hym_value_source_search_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_Visible_Bundle_or_Direct_HYM_Value_Source_Search_v1.md"

STATUS = "Q79_SELECTED_VISIBLE_BUNDLE_OR_DIRECT_HYM_VALUE_SOURCE_SEARCH_BUILT_PRIMARY_VALPHA_ROUTE_OPEN"
NEXT = "Q79_Selected_L2_Cochain_Ext_or_Direct_HYM_Value_Packet_Fill_v1"


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
    check("theorem proved as search", packet["theorem"]["proved"] is True, packet["theorem"])
    check("closure not claimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])
    check("all search checks pass", all(packet["search_checks"].values()), packet["search_checks"])

    results = packet["search_results"]
    check(
        "primary route is V_alpha L=(1,-2,0)",
        results["primary_route"]["id"] == "rank2_non_split_extension_preferred_L_1_-2_0"
        and results["primary_route"]["topological_target"]["l_vector_abc"] == [1, -2, 0],
        results["primary_route"],
    )
    check(
        "direct HYM preserved as fallback",
        results["direct_hym_routec_fallback"]["id"] == "direct_route_c_finite_hym_strominger_solve"
        and results["direct_hym_routec_fallback"]["open_fields"]["connection_or_residual"]["status"]
        == "OPEN",
        results["direct_hym_routec_fallback"],
    )
    check(
        "abelian shortcut retired",
        results["retired_as_final_source"]["id"] == "abelian_two_line_flux_row"
        and results["retired_as_final_source"]["role"] == "Chern_Bianchi_support_template_only",
        results["retired_as_final_source"],
    )
    check(
        "value fill target names cochain and direct HYM",
        packet["value_fill_target"]["name"] == NEXT
        and any("selected L^2 cochain" in item for item in packet["value_fill_target"]["primary_payload"])
        and any("selected finite HYM" in item for item in packet["value_fill_target"]["direct_hym_fallback_payload"]),
        packet["value_fill_target"],
    )
    check(
        "remaining open retained",
        packet["what_remains_open"]["selected_L2_cochain_packet"] is True
        and packet["what_remains_open"]["HYM_or_RouteC_residual_certificate"] is True
        and packet["what_remains_open"]["same_source_DE_Riesz_Green_dotD"] is True,
        packet["what_remains_open"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "search closed not value source",
        packet["verdict"]["source_search_closed"] is True
        and packet["verdict"]["value_source_closed"] is False
        and packet["verdict"]["next_required_artifact"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "non-split rank-two",
        "`L=(1,-2,0)`",
        "direct HYM/Route C remains the",
        "execution engine",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 selected visible bundle/direct HYM value-source search audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
