"""Audit the selected matter-slot transversality source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
VALIDATOR = REPO / "scripts" / "validate_selected_matter_slot_transversality_source.py"
ATTEMPT_SCRIPT = REPO / "scripts" / "attempt_fill_selected_matter_slot_transversality_source.py"
TEMPLATE = REPO / "certificates" / "selected_matter_slot_transversality_source.template.json"
VALIDATOR_CERT = REPO / "certificates" / "selected_matter_slot_transversality_source_validator_certificate.json"
ATTEMPT_PACKET = REPO / "certificates" / "selected_matter_slot_transversality_source.attempt.json"
ATTEMPT_CANDIDATE = REPO / "candidate_data" / "selected_matter_slot_transversality_source_attempt.candidate.json"
ATTEMPT_CERT = REPO / "certificates" / "selected_matter_slot_transversality_source_attempt_certificate.json"
PAPER = ROOT / "Selected_Matter_Slot_Transversality_Source_Gate_v1.md"


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


def run_command(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def run_attempt() -> dict[str, Any]:
    code, output = run_command([sys.executable, str(ATTEMPT_SCRIPT)])
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def main() -> None:
    attempt = run_attempt()
    template_code, template_output = run_command([sys.executable, str(VALIDATOR), str(TEMPLATE)])
    attempt_packet_code, attempt_packet_output = run_command(
        [sys.executable, str(VALIDATOR), str(ATTEMPT_PACKET)]
    )
    validator_text = read(VALIDATOR)
    attempt_text = read(ATTEMPT_SCRIPT)
    paper = read(PAPER)
    validator_cert = load_json(VALIDATOR_CERT)
    attempt_candidate = load_json(ATTEMPT_CANDIDATE)
    attempt_cert = load_json(ATTEMPT_CERT)

    calc = attempt.get("calculation_results", {})
    closed = attempt.get("what_this_closes", {})
    open_items = attempt.get("still_open", {})
    guardrails = attempt.get("guardrails", {})
    verdict = attempt.get("verdict", {})
    validation_report = attempt.get("validator", {}).get("report", {})

    gates = [
        Gate(
            "validator present",
            "PASS"
            if VALIDATOR.exists()
            and contains_all(
                validator_text,
                [
                    "SelectedMatterSlotTransversalitySource.v1",
                    "source.selected_by_mtt must be true",
                    "selected_origin_verified",
                    "route_c_evidence.{key} must be true",
                    "relative U_10^dagger C Ubar5 must be F",
                ],
            )
            else "FAIL",
            str(VALIDATOR),
        ),
        Gate(
            "attempt script present",
            "PASS"
            if ATTEMPT_SCRIPT.exists()
            and contains_all(
                attempt_text,
                [
                    "ROUTE_C_SOURCE_ATTEMPT_BLOCKED_SELECTED_ORIGIN_MISSING",
                    "selected_origin_still_missing",
                    "basis_matrix_U10",
                    "basis_matrix_Ubar5",
                ],
            )
            else "FAIL",
            str(ATTEMPT_SCRIPT),
        ),
        Gate(
            "template refused",
            "PASS"
            if template_code == 2 and "OPEN" in template_output
            else "FAIL",
            template_output.strip(),
        ),
        Gate(
            "validator certificate",
            "PASS"
            if validator_cert.get("status")
            == "SELECTED_MATTER_SLOT_TRANSVERSALITY_SOURCE_VALIDATOR_FORMULATED_SOURCE_OPEN"
            and validator_cert.get("verdict", {}).get("validator_formulated") is True
            and validator_cert.get("verdict", {}).get("selected_source_verified") is False
            else "FAIL",
            str(validator_cert.get("status")),
        ),
        Gate(
            "attempt packet rejected",
            "PASS"
            if attempt_packet_code == 1
            and "source.selected_by_mtt must be true" in attempt_packet_output
            and "route_c_evidence.selected_origin_verified must be true" in attempt_packet_output
            else "FAIL",
            attempt_packet_output.strip(),
        ),
        Gate(
            "attempt certificate status",
            "PASS"
            if attempt_cert.get("status")
            == "SELECTED_MATTER_SLOT_TRANSVERSALITY_SOURCE_ATTEMPT_BLOCKED_ROUTE_C_SELECTED_ORIGIN_MISSING"
            and attempt_candidate.get("calculation") == "SelectedMatterSlotTransversalitySourceRouteCAttempt"
            else "FAIL",
            str((attempt_cert.get("status"), attempt_candidate.get("calculation"))),
        ),
        Gate(
            "route c status",
            "PASS"
            if calc.get("route_c_q79_branch_available") is True
            and calc.get("route_c_honest_rhoE_metric_sector_pass") is True
            and calc.get("route_c_honest_selected_origin_pass") is False
            and calc.get("route_c_selected_origin_still_missing") is True
            and calc.get("lifted_selected_flags_algebra_passes") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "finite matrices not blocker",
            "PASS"
            if calc.get("attempt_packet_relative_transport_is_F") is True
            and validation_report.get("matter_slot_source", {}).get("relative_transport_orientation")
            == "F"
            else "FAIL",
            str(validation_report),
        ),
        Gate(
            "source remains blocked",
            "PASS"
            if calc.get("selected_source_verified") is False
            and calc.get("promotes_su5_matter_slot_transversality") is False
            and open_items.get("route_c_selected_origin") is True
            and open_items.get("selected_D_E_dotD_same_branch") is True
            else "FAIL",
            str((calc, open_items)),
        ),
        Gate(
            "closed fields",
            "PASS"
            if closed.get("source_packet_interface_instantiated") is True
            and closed.get("route_c_first_fill_attempt_executed") is True
            and closed.get("finite_I_F_matrices_not_the_blocker") is True
            and closed.get("route_c_selected_origin_blocker_confirmed") is True
            else "FAIL",
            str(closed),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_selected_source_verified") is False
            and guardrails.get("claims_ordered_su5_packet_selected") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("uses_benchmark_flavor_entries") is False
            and guardrails.get("claims_full_SM_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("attempted_route_c_fill") is True
            and verdict.get("selected_source_verified") is False
            and verdict.get("current_status") == "BLOCKED_ROUTE_C_SELECTED_ORIGIN_MISSING"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "Validator Contract",
                    "Route C First Attempt",
                    "selected-origin D_E/Riesz/Green/dotD validators fail",
                    "finite object is not the blocker",
                    "selected Route C origin",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected matter-slot transversality source gate audit")
    print("=====================================================")
    print()
    print(f"template_exit={template_code}")
    print(f"attempt_exit={attempt_packet_code}")
    print(f"selected_source={calc.get('selected_source_verified')}")
    print(f"relative_transport={validation_report.get('matter_slot_source', {}).get('relative_transport_orientation')}")
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
