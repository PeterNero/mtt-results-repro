"""Audit the selected Qa/SU3 Strominger/HYM source packet search."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_strominger_hym_source_packet_search_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_Strominger_HYM_Source_Packet_Search_v1.md"
SCRIPT = REPO / "scripts" / "search_selected_qa_su3_strominger_hym_source_packet.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")
    result = cert["search_result"]
    levels = {item["level"]: item for item in cert["levels"]}

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_STROMINGER_HYM_SOURCE_PACKET_SEARCH_DONE_SAME_BRANCH_SOURCE_NOT_FOUND",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["search_result"] == cert["search_result"]
            and computed["constructive_spec"] == cert["constructive_spec"],
            computed["search_result"],
        ),
        check(
            "templates found",
            result["general_strominger_hym_template_found"] is True
            and result["visible_source_packet_template_found"] is True,
            result,
        ),
        check(
            "same-branch source not found",
            result["same_branch_qa_su3_source_packet_found"] is False
            and levels["same_branch_qa_su3_source_packet"]["status"] == "NOT_FOUND",
            levels["same_branch_qa_su3_source_packet"],
        ),
        check(
            "template scope guarded",
            levels["general_strominger_hym_fixed_sector_template"]["usable_for_qa_su3_determinant"] is False
            and levels["visible_sector_source_packet_analogue"]["usable_for_qa_su3_determinant"] is False,
            levels,
        ),
        check(
            "no closure overclaimed",
            result["selected_endomorphism_E_found"] is False
            and result["determinant_computable_now"] is False
            and result["qa_su3_closed"] is False
            and result["full_sm_closure_achieved"] is False
            and result["target_fitting_used"] is False,
            result,
        ),
        check(
            "constructive next artifact named",
            cert["next_required_artifact"]["name"] == "Selected_Qa_SU3_Chern_Bianchi_Source_Packet_Candidates_v1"
            and "Chern/Bianchi packet for a candidate SU3 source"
            in cert["constructive_spec"]["minimal_next_computable_subpacket"],
            cert["next_required_artifact"],
        ),
        check(
            "note records search result",
            "same-branch Qa/SU3 source packet: not found" in note
            and "Selected_Qa_SU3_Chern_Bianchi_Source_Packet_Candidates_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 Strominger HYM source packet search audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
