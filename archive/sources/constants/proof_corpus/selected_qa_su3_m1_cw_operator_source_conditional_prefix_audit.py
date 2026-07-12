"""Audit the conditional prefix for Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_qa_su3_m1_cw_operator_source_conditional_prefix.py"
PACKET = ROOT / "candidate_data" / "selected_qa_su3_m1_cw_operator_source_conditional_prefix.candidate.json"
CERT = ROOT / "certificates" / "selected_qa_su3_m1_cw_operator_source_conditional_prefix_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Conditional_Prefix_v1.md"

STATUS = "QA_SU3_M1_CW_OPERATOR_SOURCE_CONDITIONAL_PREFIX_CLOSED_DOTD_C1_OPEN"
NEXT = "Selected_Qa_SU3_M1_CW_dotD_alpha1_and_C1_Primitive_Source_v1"


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
    check("all prefix checks pass", all(packet["prefix_checks"].values()), packet["prefix_checks"])
    check("theorem proved as conditional prefix", packet["theorem"]["proved"] is True, packet["theorem"])
    check("full closure not claimed", packet["theorem"]["closure_claimed"] is False, packet["theorem"])

    source = packet["selected_source_prefix"]
    check(
        "source is explicitly conditional",
        source["status"] == "CONDITIONAL_ON_TERMINAL_ADMISSIBLE_SECTION_SOURCE_PRINCIPLE"
        and source["principle_status"] == "EXPLICIT_PRINCIPLE_SYNTHESIZED_FROM_MTT_CORPUS"
        and source["unconditional_selector_proved"] is False,
        source,
    )
    check(
        "L3-K2 visible source selected under principle",
        source["selected_source_label"] == "g3 / L3-K2"
        and source["selected_L"] == [1, -2, 0]
        and source["selected_L2"] == [2, -4, 0]
        and source["selected_c2"] == [4, 0, 0],
        source,
    )
    check(
        "D_E gap layer imported but dotD still open",
        packet["what_closes_now"]["D_E_gap_Riesz_Green_source_identity_imported"] is True
        and packet["what_remains_open"]["selected_dotD_alpha1_first_variation"] is True
        and packet["same_source_operator_layer"]["dotD_alpha1_status"][
            "missing_source_identity"
        ],
        packet["same_source_operator_layer"],
    )
    check(
        "C1 and SM closure remain open",
        packet["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"] is True
        and packet["what_remains_open"]["nonzero_C1_response_matrices"] is True
        and packet["what_remains_open"]["selected_Yukawa_or_full_SM_closure"] is True,
        packet["what_remains_open"],
    )
    check(
        "guardrails all negative",
        all(v is False for v in packet["guardrails"].values()),
        packet["guardrails"],
    )
    check(
        "verdict names next gate",
        packet["verdict"]["conditional_prefix_closed"] is True
        and packet["verdict"]["full_CW_operator_source_closed"] is False
        and packet["verdict"]["selected_source_unconditional"] is False
        and packet["verdict"]["next_required_artifact"] == NEXT,
        packet["verdict"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "conditional prefix",
        "`TerminalAdmissibleSectionSourcePrinciple.v1`",
        "`g3 / L3-K2`",
        "`L=(1,-2,0)`",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nSelected Qa/SU3 M1 Chern-Weil operator source conditional prefix audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
