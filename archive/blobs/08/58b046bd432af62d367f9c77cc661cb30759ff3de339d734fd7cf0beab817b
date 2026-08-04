"""Audit the Iwasawa C6 support/noncommutation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_c6_support_noncommutation_gate_certificate.json"
PAPER = ROOT / "Iwasawa_C6_Support_Noncommutation_Gate_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_c6_support_noncommutation_gate.py"


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


def run_analysis() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)
    analysis = run_analysis()

    calc = cert.get("calculation_results", {})
    scan = analysis.get("selected_support_data_scan", {})
    phase = analysis.get("selected_c6_phase_block", {})
    symbolic = analysis.get("symbolic_decomposition", {})
    finite_gate = analysis.get("finite_gate", {})
    case_table = analysis.get("case_table", [])
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    input_statuses = analysis.get("input_statuses", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_C6_SUPPORT_NONCOMMUTATION_GATE_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if input_statuses.get("certificates/iwasawa_c6_global_phase_block_certificate.json")
            == "IWASAWA_C6_GLOBAL_PHASE_BLOCK_CLOSED_AMPLITUDES_OPEN"
            and input_statuses.get("certificates/ckm_leading_noncommutation_criterion_certificate.json")
            == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            and input_statuses.get("certificates/jarlskog_closure_criterion_certificate.json")
            == "JARLSKOG_CLOSURE_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(input_statuses),
        ),
        Gate(
            "phase block inherited",
            "PASS"
            if phase.get("selected_label") == 79
            and phase.get("conjugate_label") == 369
            and phase.get("all_c6_channels_share_one_phase_per_branch") is True
            and phase.get("pure_flat_action_S") == 0
            and phase.get("exp_minus_S") == 1
            else "FAIL",
            str(phase),
        ),
        Gate(
            "support absence scan",
            "PASS"
            if scan.get("selected_c6_support_data_found") is False
            and scan.get("selected_c6_support_values_computed") is False
            and scan.get("present_selected_c6_support_files") == []
            else "FAIL",
            str(scan),
        ),
        Gate(
            "symbolic decomposition",
            "PASS"
            if symbolic.get("c6_decomposition") == "M_s = T_s + chi_q C_s"
            and symbolic.get("delta_v") == "Delta_v = Delta_t + chi_q Delta_c"
            and symbolic.get("heavy_link_vector") == "v_s = (M_s13, M_s23) = t_s + chi_q c_s"
            else "FAIL",
            str(symbolic),
        ),
        Gate(
            "finite gate",
            "PASS"
            if finite_gate.get("leading_noncommutation_condition") == "Delta_v != (0,0)"
            and finite_gate.get("expanded_condition") == "Delta_t + chi_q Delta_c != (0,0)"
            and finite_gate.get("c6_affects_leading_heavy_link_if") == "Delta_c != (0,0)"
            and finite_gate.get("c6_alone_cannot_close_full_cp") is True
            else "FAIL",
            str(finite_gate),
        ),
        Gate(
            "case table",
            "PASS"
            if len(case_table) == 4
            and case_table[0].get("q79_drives_leading_gate") is False
            and case_table[1].get("q79_drives_leading_gate") is False
            and case_table[2].get("q79_drives_leading_gate") is True
            else "FAIL",
            str(case_table),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("selected_label") == 79
            and calc.get("conjugate_label") == 369
            and calc.get("selected_c6_support_data_found") is False
            and calc.get("selected_c6_support_values_computed") is False
            and calc.get("heavy_link_decomposition") == "Delta_v = Delta_t + chi_q Delta_c"
            and calc.get("expanded_condition") == "Delta_t + chi_q Delta_c != (0,0)"
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
            "verdict",
            "PASS"
            if verdict.get("criterion_closed") is True
            and verdict.get("selected_c6_support_values_open") is True
            and verdict.get("numeric_ckm_noncommutation_open") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "Delta_v = Delta_t + chi_q Delta_c",
                    "Delta_t + chi_q Delta_c != (0,0)",
                    "None are present in the current package.",
                    "C6 support entry target",
                    "Im det([Y_uY_u^dagger,Y_dY_d^dagger])",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa C6 support/noncommutation gate audit")
    print("============================================")
    print()
    print(f"selected_label={phase.get('selected_label')}")
    print(f"present_support_files={scan.get('present_selected_c6_support_files')}")
    print(f"expanded_condition={finite_gate.get('expanded_condition')}")
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
