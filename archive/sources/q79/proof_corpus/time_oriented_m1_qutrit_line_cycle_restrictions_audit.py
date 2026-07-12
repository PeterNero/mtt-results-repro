"""Audit the selected qutrit line-cycle restriction packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "construct_time_oriented_m1_qutrit_line_cycle_restrictions.py"
VALIDATOR = REPO / "scripts" / "validate_time_oriented_m1_selected_cycle_restrictions.py"
PACKET = REPO / "certificates" / "time_oriented_m1_qutrit_line_cycle_restrictions.selected.json"
CANDIDATE = REPO / "candidate_data" / "time_oriented_m1_qutrit_line_cycle_restrictions.candidate.json"
CERT = REPO / "certificates" / "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json"
PAPER = REPO / "proof_corpus" / "Time_Oriented_m1_Qutrit_Line_Cycle_Restrictions_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: str) -> tuple[str, bool, str]:
    return name, condition, detail


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def run_validator(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def main() -> int:
    proc = run_script()
    checks: list[tuple[str, bool, str]] = [
        check("constructor exits 0", proc.returncode == 0, proc.stdout[:1000]),
        check("packet exists", PACKET.exists(), str(PACKET)),
        check("candidate exists", CANDIDATE.exists(), str(CANDIDATE)),
        check("certificate exists", CERT.exists(), str(CERT)),
        check("paper exists", PAPER.exists(), str(PAPER)),
    ]

    if PACKET.exists() and CANDIDATE.exists() and CERT.exists() and PAPER.exists():
        packet = load_json(PACKET)
        candidate = load_json(CANDIDATE)
        cert = load_json(CERT)
        validator_proc = run_validator(PACKET)
        calc = cert.get("calculation_results", {})
        closes = cert.get("what_this_closes", {})
        still_open = cert.get("still_open", {})
        guardrails = cert.get("guardrails", {})
        spin = cert.get("spinC_W3_argument", {})
        cycles = packet.get("cycles", [])
        paper = PAPER.read_text(encoding="utf-8")

        checks.extend(
            [
                check(
                    "status line-cycle closed visible list open",
                    cert.get("status")
                    == "TIME_ORIENTED_M1_QUTRIT_LINE_CYCLE_RESTRICTIONS_CLOSED_VISIBLE_CYCLE_LIST_OPEN"
                    and candidate.get("status") == cert.get("status"),
                    str(cert.get("status")),
                ),
                check(
                    "selected packet validates",
                    validator_proc.returncode == 0
                    and "selected-cycle restriction PASS" in validator_proc.stdout,
                    validator_proc.stdout.strip(),
                ),
                check(
                    "clock and shift cycles present",
                    len(cycles) == 2
                    and cycles[0].get("id") == "qutrit_clock_line"
                    and cycles[0].get("pi1_image_generators_F3_2") == [[1, 0]]
                    and cycles[1].get("id") == "qutrit_shift_line"
                    and cycles[1].get("pi1_image_generators_F3_2") == [[0, 1]],
                    str(cycles),
                ),
                check(
                    "qutrit line restrictions closed but not complete FW",
                    calc.get("qutrit_line_cycle_restrictions_closed") is True
                    and calc.get("complete_visible_cycle_or_brane_list_supplied") is False
                    and calc.get("full_Freed_Witten_for_visible_sector_verified") is False,
                    str(calc),
                ),
                check(
                    "spinC/W3 scope guarded",
                    spin.get("scope") == "clock/shift line representatives only"
                    and spin.get("does_not_determine_W3_for_arbitrary_visible_cycles") is True,
                    str(spin),
                ),
                check(
                    "what closes and remains",
                    closes.get("selected_qutrit_clock_line_DD_restriction") is True
                    and closes.get("selected_qutrit_shift_line_DD_restriction") is True
                    and still_open.get("complete_selected_visible_cycle_or_brane_list") is True
                    and still_open.get("selected_visible_SM_operator_source") is True,
                    str({"closes": closes, "still_open": still_open}),
                ),
                check(
                    "guardrails prevent overclaim",
                    guardrails.get("claims_complete_visible_cycle_list") is False
                    and guardrails.get("claims_full_Freed_Witten_verification") is False
                    and guardrails.get("claims_selected_visible_operator_source") is False
                    and guardrails.get("claims_full_SM_closure") is False,
                    str(guardrails),
                ),
                check(
                    "paper records split frontier",
                    "qutrit polarization lines: closed" in paper
                    and "complete visible worldvolume packet: open" in paper
                    and "complete visible cycle or brane list" in paper,
                    "paper split present",
                ),
            ]
        )

    print("Time-oriented m=1 qutrit line-cycle restrictions audit")
    print("======================================================")
    failures = 0
    for name, ok, detail in checks:
        print(f"{name:55} {'PASS' if ok else 'FAIL'}  {detail}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
