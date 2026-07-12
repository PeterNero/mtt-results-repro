"""Audit the selected gerbe-Fourier type theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_selected_gerbe_fourier_type.py"
CANDIDATE = REPO / "candidate_data" / "selected_gerbe_fourier_type_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_gerbe_fourier_type_theorem_certificate.json"
PAPER = ROOT / "Selected_Gerbe_Fourier_Type_Theorem_v1.md"


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
    torsion = report.get("finite_torsion_calculation", {})
    evidence = report.get("corpus_evidence", {})
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
                    "Layer 1 closes",
                    "Layer 2 remains open",
                    "torsion_label_report",
                    "selected_gerbe_fourier_type_closed",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "SELECTED_GERBE_FOURIER_TYPE_PROVED_SU5_PACKET_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "corpus evidence",
            "PASS"
            if evidence
            and all(item.get("present") is True for item in evidence.values())
            and calc.get("selected_structural_sources_present") is True
            else "FAIL",
            str(evidence),
        ),
        Gate(
            "finite torsion",
            "PASS"
            if torsion.get("nontrivial_bianchi_closed_labels") == [1, 2]
            and torsion.get("trivial_label_rank") == 0
            and torsion.get("nontrivial_labels_have_rank_two") is True
            else "FAIL",
            str(torsion),
        ),
        Gate(
            "type proof closed",
            "PASS"
            if calc.get("gerbe_cocycle_closed") is True
            and calc.get("four_route_selects_nontrivial_conjugate_pair") is True
            and calc.get("finite_fourier_transport_closed") is True
            and calc.get("global_conjugate_pair_closed") is True
            and calc.get("selected_gerbe_fourier_type_closed") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "exact packet not overclaimed",
            "PASS"
            if calc.get("exact_su5_packet_selected") is False
            and calc.get("unique_orientation_selected") is False
            and calc.get("exact_q79_packet_U10_I_Ubar5_F_selected") is False
            and open_items.get("exact_packet_U10_I_Ubar5_F_as_selected_data") is True
            else "FAIL",
            str((calc, open_items)),
        ),
        Gate(
            "proved fields",
            "PASS"
            if proved.get("nontrivial_Z3_flat_gerbe_type_selected_as_MTT_family_phase_space")
            is True
            and proved.get("Fourier_transport_F_or_F_conjugate_selected_up_to_global_orientation")
            is True
            and proved.get("trivial_m0_torsion_rejected_for_family_Fourier_type") is True
            else "FAIL",
            str(proved),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_exact_SU5_packet_selected") is False
            and guardrails.get("claims_unique_orientation_without_source") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("uses_benchmark_flavor_entries") is False
            and guardrails.get("claims_full_SM_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("selected_fourier_type_proved") is True
            and verdict.get("already_computed_packet_fully_selected") is False
            and "ordered SU(5) packet" in verdict.get("honest_answer", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "Layer 1",
                    "Layer 2",
                    "MTT selects the nontrivial gerbe-Fourier qutrit type up to conjugation",
                    "Still open",
                    "U_10=I_3, U_bar5=F",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Selected gerbe-Fourier type theorem audit")
    print("==========================================")
    print()
    print(f"selected_type={calc.get('selected_gerbe_fourier_type_closed')}")
    print(f"exact_packet={calc.get('exact_q79_packet_U10_I_Ubar5_F_selected')}")
    print(f"nontrivial_labels={torsion.get('nontrivial_bianchi_closed_labels')}")
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
