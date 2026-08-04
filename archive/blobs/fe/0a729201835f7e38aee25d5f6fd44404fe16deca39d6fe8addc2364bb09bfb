"""Audit the time-oriented conjugate branch-selection theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_time_oriented_conjugate_branch_selection.py"
CANDIDATE = REPO / "candidate_data" / "time_oriented_conjugate_branch_selection.candidate.json"
CERT = REPO / "certificates" / "time_oriented_conjugate_branch_selection_certificate.json"
PAPER = ROOT / "Time_Oriented_Conjugate_Branch_Selection_v1.md"


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


def run_script() -> dict[str, Any]:
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
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    calc = report.get("calculation_results", {})
    residues = report.get("residue_calculation", {})
    selected = residues.get("selected_residues", {})
    conjugate = residues.get("conjugate_residues", {})
    gates_data = report.get("source_gates", {})
    proved = report.get("what_this_proves", {})
    open_items = report.get("still_open", {})
    guardrails = report.get("guardrails", {})
    verdict = report.get("verdict", {})

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "crt_mod_448",
                    "time_oriented_retarded_branch_selects_q79",
                    "q369_retained_as_global_antiunitary_conjugate",
                    "ordered SU(5) matter-slot packet",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "TIME_ORIENTED_Q79_F_BRANCH_SELECTED_ORDERED_SU5_PACKET_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "retarded CRT",
            "PASS"
            if selected.get("q_64") == 15
            and selected.get("q_7") == 2
            and selected.get("crt_q") == 79
            and conjugate.get("q") == 369
            and conjugate.get("q_64") == 49
            and conjugate.get("q_7") == 5
            and residues.get("q79_plus_q369_mod_448") == 0
            else "FAIL",
            str(residues),
        ),
        Gate(
            "source gates",
            "PASS"
            if gates_data.get("z64_retarded_kernel", {}).get("closed") is True
            and gates_data.get("z7_charge_sector", {}).get("closed") is True
            and gates_data.get("orientation_bridge", {}).get("closed") is True
            and gates_data.get("global_conjugate_pair", {}).get("closed") is True
            and gates_data.get("selected_gerbe_fourier_type", {}).get("closed") is True
            else "FAIL",
            str(gates_data),
        ),
        Gate(
            "branch theorem closed",
            "PASS"
            if calc.get("z64_retarded_kernel_selected") is True
            and calc.get("z7_charge_sector_selected") is True
            and calc.get("crt_selects_q79") is True
            and calc.get("conjugate_label_is_q369") is True
            and calc.get("branch_packet_map_q79_F_q369_Fstar") is True
            and calc.get("unoriented_conjugate_pair_retained") is True
            and calc.get("time_oriented_retarded_branch_selects_q79") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "conjugate interpretation",
            "PASS"
            if calc.get("q369_retained_as_global_antiunitary_conjugate") is True
            and calc.get("two_unrelated_universe_interpretation_rejected") is True
            and calc.get("unique_without_retarded_boundary_or_operator_source") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "proved fields",
            "PASS"
            if proved.get("without_time_orientation_MTT_selects_pair_not_single_representative")
            is True
            and proved.get("with_closed_retarded_kernel_MTT_selects_q79_representative")
            is True
            and proved.get("q369_Fstar_remains_conjugate_partner") is True
            and proved.get("retarded_initial_or_boundary_condition_can_function_as_branch_selector")
            is True
            else "FAIL",
            str(proved),
        ),
        Gate(
            "open items preserved",
            "PASS"
            if calc.get("ordered_su5_packet_selected") is False
            and calc.get("full_sm_closure") is False
            and open_items.get("ordered_SU5_slot_assignment_10M_clock_bar5M_shift") is True
            and open_items.get("selected_D_E_dotD_or_monad_source_for_matter_slots") is True
            and open_items.get("full_SM_closure") is True
            else "FAIL",
            str((calc, open_items)),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_q369_wrong_or_nonexistent") is False
            and guardrails.get("claims_two_independent_physical_universes") is False
            and guardrails.get("claims_both_branches_simultaneously_observed") is False
            and guardrails.get("claims_exact_SU5_packet_selected") is False
            and guardrails.get("uses_observed_CP_sign_to_select_branch") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("claims_full_SM_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if "q79/F" in verdict.get("time_oriented_status", "")
            and verdict.get("ordered_su5_packet_status") == "OPEN"
            and "conjugate partner" in verdict.get("honest_answer", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "Without time orientation",
                    "selected retarded kernel",
                    "therefore q = 79 mod 448",
                    "q=369",
                    "Exact ordered SU(5) matter-slot selection",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Time-oriented conjugate branch-selection audit")
    print("==============================================")
    print()
    print(f"time_oriented_q79={calc.get('time_oriented_retarded_branch_selects_q79')}")
    print(f"q369_retained={calc.get('q369_retained_as_global_antiunitary_conjugate')}")
    print(f"ordered_su5_packet={calc.get('ordered_su5_packet_selected')}")
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
