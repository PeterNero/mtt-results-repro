"""Verify the SM-parity closure reproduction capsule."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
REPORT = ROOT / "reports" / "verification_report.txt"
BUILDER = ROOT / "scripts" / "build.py"


def load(name: str) -> dict:
    return json.loads((OUTPUTS / name).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    replacement = load("qasu3_parity_interface_replacement.packet.json")
    final_packet = load("final_sm_packet_certificate_parity_closure.packet.json")
    decision = load("sm_parity_closure_decision.packet.json")
    candidate = load("selected_qasu3sourcepacket_or_finalsmparityclosure.candidate.json")

    checks: list[str] = []

    def check(condition: bool, label: str) -> None:
        require(condition, label)
        checks.append(f"PASS: {label}")

    check(replacement["accepted_for_SM_parity_interface"] is True, "Qa/SU3 replacement accepted for SM-parity")
    check(replacement["accepted_as_actual_selected_no_knob_packet"] is False, "Qa/SU3 no-knob packet not claimed")
    check(replacement["accepted_for_true_precision_equivalence"] is False, "true precision equivalence not claimed")
    for key, value in replacement["guardrails"].items():
        check(value is False, f"guardrail false: {key}")

    check(final_packet["all_source_rows_closed_for_sm_parity_interface"] is True, "all source rows parity-closed")
    check(final_packet["any_source_row_closed_as_actual_no_knob_packet"] is False, "no source row no-knob-closed")
    check(final_packet["can_close_SM_parity_interface_now"] is True, "final packet closes SM-parity")
    check(final_packet["can_close_true_SM_equivalence_now"] is False, "final packet does not close true equivalence")
    check(final_packet["can_close_no_knob_SM_derivation_now"] is False, "final packet does not close no-knob derivation")
    check(final_packet["qasu3_row"]["closed_for_sm_parity_interface"] is True, "Qa/SU3 row parity-closed")
    check(final_packet["qasu3_row"]["closed_as_actual_selected_no_knob_packet"] is False, "Qa/SU3 row no-knob open")

    check(decision["SM_parity_closed"] is True, "SM-parity closure true")
    check(decision["true_SM_equivalence_closed"] is False, "true SM equivalence false")
    check(decision["no_knob_closed"] is False, "no-knob closure false")
    check(decision["current_SM_parity_blockers"] == [], "no remaining SM-parity blockers")
    check(decision["observed_data_used_as_selector"] is False, "observed data not selector")
    check(decision["target_fitting_used"] is False, "target fitting not used")

    check(candidate["theorem"]["proved"] is True, "theorem proved flag true")
    check(candidate["source_boundary_preserved"] is True, "source boundary preserved")
    check(candidate["actual_selected_operator_packet_claimed"] is False, "actual selected operator packet not claimed")
    check(len(candidate["input_hashes"]) == 5, "five frozen input hashes recorded")

    lines = [
        "MTT SM-parity closure reproduction report",
        "=========================================",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        *checks,
        "",
        "Verification result: PASS",
        "SM-parity closure: TRUE",
        "true SM equivalence: FALSE",
        "no-knob closure: FALSE",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
