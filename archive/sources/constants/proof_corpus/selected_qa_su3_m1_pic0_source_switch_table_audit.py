"""Audit the Qa/SU3 m=1 Pic0/source switch table."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qa_su3_m1_pic0_source_switch_table_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_SU3_M1_Pic0_Source_Switch_Table_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qa_su3_m1_pic0_source_switch_table.py"


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

    table = {case["case"]: case for case in cert["switch_table"]}
    closes = cert["what_this_closes"]
    not_closed = cert["what_this_does_not_close"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "QA_SU3_M1_PIC0_SOURCE_SWITCH_TABLE_BUILT_BOTH_SWITCHES_REQUIRED",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["switch_table"] == cert["switch_table"]
            and computed["what_this_closes"] == closes,
            computed["status"],
        ),
        check(
            "four switch cases present",
            sorted(table) == ["none", "pic0_only", "source_and_pic0", "source_only"],
            sorted(table),
        ),
        check(
            "pic0 only still needs source",
            table["pic0_only"]["validator_exit_code"] == 2
            and "source.selected_by_mtt is not true" in table["pic0_only"]["open_items"],
            table["pic0_only"],
        ),
        check(
            "source only still needs Pic0",
            table["source_only"]["validator_exit_code"] == 2
            and "Pic0 resolution rule missing" in table["source_only"]["open_items"],
            table["source_only"],
        ),
        check(
            "both switches pass validator",
            table["source_and_pic0"]["validator_exit_code"] == 0
            and table["source_and_pic0"]["validator_status"] == "PASS"
            and table["source_and_pic0"]["open_items"] == [],
            table["source_and_pic0"],
        ),
        check(
            "closures are switch-table closures only",
            closes["pic0_is_independent_required_switch"] is True
            and closes["source_selection_is_independent_required_switch"] is True
            and closes["both_switches_suffice_for_ordered_source_validator"] is True,
            closes,
        ),
        check(
            "hard gates remain open",
            not_closed["actual_source_switch_from_MTT"] is True
            and not_closed["actual_pic0_rule_from_MTT_or_physical_quotient"] is True
            and not_closed["same_source_D_E_dotD_Riesz_Green"] is True,
            not_closed,
        ),
        check(
            "guardrails prevent overclaim",
            guardrails["claims_pic0_rule_proved"] is False
            and guardrails["claims_source_selection_proved"] is False
            and guardrails["claims_ordered_source_closed_unconditionally"] is False
            and guardrails["claims_Ext_packet_selected"] is False,
            guardrails,
        ),
        check(
            "note records next artifact",
            "source and Pic0   -> PASS" in note
            and "Selected_Monad_Difference_L2_Source_and_Pic0_Quotient_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected Qa/SU3 m=1 Pic0/source switch table audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
