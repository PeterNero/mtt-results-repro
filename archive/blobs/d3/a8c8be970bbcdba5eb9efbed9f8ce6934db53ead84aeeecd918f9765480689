"""Audit the SU(5) qutrit polarization packet fill attempt."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json"
PACKET = REPO / "certificates" / "selected_su5_qutrit_polarization_data.attempt.json"
PAPER = ROOT / "Selected_SU5_Qutrit_Polarization_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_selected_su5_qutrit_polarization_packet.py"
VALIDATOR = REPO / "scripts" / "validate_selected_su5_qutrit_polarization.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_attempt() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--output", str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def run_validator() -> tuple[int, str, dict[str, Any]]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    match = re.search(r"polarization_validation_report=(\{.*\})", proc.stdout)
    report = json.loads(match.group(1)) if match else {}
    return proc.returncode, proc.stdout, report


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    attempt = run_attempt()
    packet = load_json(PACKET)
    validator_code, validator_output, validator_report = run_validator()

    upstream = attempt.get("upstream_status", {})
    verdict = attempt.get("verdict", {})
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    cert_verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "SELECTED_SU5_QUTRIT_POLARIZATION_PACKET_ATTEMPT_FINITE_PASS_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["build_attempt_packet", "run_validator"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "attempt packet written",
            "PASS"
            if PACKET.exists()
            and packet.get("schema") == "SelectedSU5QutritPolarizationData.v1"
            and packet.get("candidate_role") == "UNSELECTED_FIXTURE"
            else "FAIL",
            str(PACKET),
        ),
        Gate(
            "upstream status",
            "PASS"
            if upstream.get("block_factorized_candidate_valid") is True
            and upstream.get("gerbe_candidate_map_closed") is True
            and upstream.get("selected_source_available") is False
            else "FAIL",
            str(upstream),
        ),
        Gate(
            "validator run",
            "PASS"
            if validator_code == 0
            and validator_report.get("orientation_mod_rephase_permutation") == "F"
            and validator_report.get("relative_transport_matches_qutrit_fourier") is True
            and validator_report.get("promotes_to_selected_heavy_link_input") is False
            else "FAIL",
            validator_output.strip(),
        ),
        Gate(
            "attempt verdict",
            "PASS"
            if verdict.get("finite_packet_constructed") is True
            and verdict.get("validator_passes_finite_algebra") is True
            and verdict.get("orientation") == "F"
            and verdict.get("promotes_to_selected_heavy_link_input") is False
            and verdict.get("selected_source_available") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("attempt_packet_written") is True
            and calc.get("block_factorized_candidate_valid") is True
            and calc.get("gerbe_candidate_map_closed") is True
            and calc.get("selected_source_available") is False
            and calc.get("candidate_role") == "UNSELECTED_FIXTURE"
            and calc.get("validator_exit_code") == 0
            and calc.get("validator_passes_finite_algebra") is True
            and calc.get("validator_orientation") == "F"
            and calc.get("promotes_to_selected_heavy_link_input") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closed fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in still_open.values()) else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "certificate verdict",
            "PASS"
            if cert_verdict.get("finite_packet_constructed_and_validated") is True
            and cert_verdict.get("selected_packet_constructed") is False
            and cert_verdict.get("can_promote_su5_qutrit_heavy_link_candidate_now") is False
            else "FAIL",
            str(cert_verdict),
        ),
        Gate(
            "paper records attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "U_10 = I_3",
                    "U_bar5 = F",
                    "validator exit code = 0",
                    "promotes_to_selected_heavy_link_input = false",
                    "selected gerbe source and sector maps not filled",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected SU(5) qutrit polarization packet fill attempt audit")
    print("============================================================")
    print()
    print(f"packet={PACKET}")
    print(f"validator_report={validator_report}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
