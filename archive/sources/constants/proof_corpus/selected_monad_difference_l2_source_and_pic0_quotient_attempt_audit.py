"""Audit Selected_Monad_Difference_L2_Source_and_Pic0_Quotient attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_monad_difference_l2_source_and_pic0_quotient_attempt_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Monad_Difference_L2_Source_and_Pic0_Quotient_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_selected_monad_difference_l2_source_and_pic0_quotient.py"


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

    pic0 = cert["local_pic0_quotient_theorem"]
    validators = cert["validator_tests"]
    closed = cert["closed_now"]
    not_closed = cert["not_closed"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "PIC0_QUOTIENT_LOCAL_CW_H1_GATE_CLOSED_SOURCE_LANE_SELECTOR_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with certificate",
            computed["closed_now"] == closed
            and computed["not_closed"] == not_closed
            and computed["validator_tests"] == validators,
            computed["status"],
        ),
        check(
            "local Pic0 quotient scoped",
            pic0["proved_for_scope"] is True
            and pic0["scope"] == "ordered Chern-Weil/H1 source gate"
            and pic0["not_a_global_holonomy_claim"] is True,
            pic0,
        ),
        check(
            "pic0 alone still fails source selection",
            validators["pic0_quotient_only"]["exit_code"] == 2
            and "source.selected_by_mtt is not true"
            in validators["pic0_quotient_only"]["open_items"],
            validators["pic0_quotient_only"],
        ),
        check(
            "source and pic0 would pass",
            validators["source_and_pic0_quotient"]["exit_code"] == 0
            and validators["source_and_pic0_quotient"]["status"] == "PASS",
            validators["source_and_pic0_quotient"],
        ),
        check(
            "closed items are local only",
            closed["pic0_quotient_admissible_for_ordered_CW_H1_gate"] is True
            and closed["combined_source_and_pic0_packet_would_pass"] is True
            and closed["terminal_lane_conditional_uniqueness_closed"] is True,
            closed,
        ),
        check(
            "source lane remains open",
            not_closed["actual_MTT_source_lane_selector_for_L3_minus_K2"] is True
            and not_closed["promote_h1_packet_to_selected_data"] is True
            and not_closed["same_source_D_E_dotD_Riesz_Green"] is True,
            not_closed,
        ),
        check(
            "guardrails prevent overclaim",
            guardrails["claims_actual_source_lane_selector_proved"] is False
            and guardrails["claims_global_pic0_physics_quotiented"] is False
            and guardrails["claims_h1_packet_selected_now"] is False
            and guardrails["claims_full_SM_closure"] is False,
            guardrails,
        ),
        check(
            "note records boundary",
            "This is not a global holonomy theorem" in note
            and "Selected_Terminal_Monad_Lane_Source_Selector_v1" in note,
            NOTE,
        ),
    ]

    print("\nSelected monad-difference L2 source and Pic0 quotient attempt audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
