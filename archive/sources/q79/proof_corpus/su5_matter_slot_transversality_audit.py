"""Audit the SU(5) matter-slot transversality theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "prove_su5_matter_slot_transversality.py"
CANDIDATE = REPO / "candidate_data" / "su5_matter_slot_transversality.candidate.json"
CERT = REPO / "certificates" / "su5_matter_slot_transversality_certificate.json"
PAPER = ROOT / "SU5_Matter_Slot_Transversality_Theorem_v1.md"


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


def case_by_name(report: dict[str, Any], name: str) -> dict[str, Any]:
    for case in report.get("finite_case_scan", []):
        if case.get("name") == name:
            return case
    return {}


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    calc = report.get("calculation_results", {})
    closed = report.get("what_this_closes", {})
    open_items = report.get("still_open", {})
    guardrails = report.get("guardrails", {})
    verdict = report.get("verdict", {})
    q79_case = case_by_name(report, "transverse_q79_U10_I_Ubar5_F")
    q369_case = case_by_name(report, "transverse_conjugate_U10_I_Ubar5_Fstar")
    common_i = case_by_name(report, "common_identity_U10_I_Ubar5_I")
    common_f = case_by_name(report, "common_fourier_U10_F_Ubar5_F")

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "common_slot_transport_is_gauge",
                    "transverse_slot_transport_nonzero",
                    "retarded_q79_orientation_closed",
                    "selected_mtt_source_present",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status")
            == "FINITE_SU5_MATTER_SLOT_TRANSVERSALITY_CLOSED_SOURCE_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "common gauge cases vanish",
            "PASS"
            if common_i.get("Delta_t_nonzero") is False
            and common_f.get("Delta_t_nonzero") is False
            and calc.get("common_slot_transport_is_gauge") is True
            else "FAIL",
            str((common_i.get("Delta_t"), common_f.get("Delta_t"))),
        ),
        Gate(
            "transverse cases nonzero",
            "PASS"
            if q79_case.get("Delta_t_nonzero") is True
            and q369_case.get("Delta_t_nonzero") is True
            and calc.get("transverse_slot_transport_nonzero") is True
            else "FAIL",
            str((q79_case.get("Delta_t"), q369_case.get("Delta_t"))),
        ),
        Gate(
            "retarded q79 packet",
            "PASS"
            if calc.get("retarded_q79_orientation_closed") is True
            and calc.get("selected_packet", {}).get("U_10") == "I_3"
            and calc.get("selected_packet", {}).get("U_bar5") == "F"
            and calc.get("selected_packet", {}).get("q") == 79
            else "FAIL",
            str(calc.get("selected_packet")),
        ),
        Gate(
            "finite theorem closed",
            "PASS"
            if calc.get("finite_qutrit_transport_proved") is True
            and calc.get("basis_candidate_matches_B10_I_Bbar5_F") is True
            and calc.get("finite_transversality_theorem_closed") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "source guard preserved",
            "PASS"
            if calc.get("selected_mtt_source_present") is False
            and calc.get("selected_ordered_su5_packet_closed") is False
            and open_items.get("selected_matter_slot_transversality_source") is True
            else "FAIL",
            str((calc, open_items)),
        ),
        Gate(
            "closed fields",
            "PASS"
            if closed.get("common_fourier_gauge_eliminated") is True
            and closed.get("retarded_q79_selects_F_over_Fstar") is True
            and closed.get("finite_uniqueness_of_ordered_packet_under_transversality")
            is True
            and closed.get("exact_remaining_source_is_not_finite_algebra") is True
            else "FAIL",
            str(closed),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_selected_source_present") is False
            and guardrails.get("claims_ordered_su5_packet_selected_without_source") is False
            and guardrails.get("uses_observed_flavor_data") is False
            and guardrails.get("uses_benchmark_flavor_entries") is False
            and guardrails.get("claims_full_SM_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("finite_transversality_theorem_closed") is True
            and verdict.get("selected_ordered_su5_packet_closed") is False
            and "selected MTT source" in verdict.get("honest_answer", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "Finite theorem",
                    "Source theorem",
                    "retarded q79 branch forces",
                    "U_10=I_3, U_bar5=F",
                    "This theorem does not claim that MTT has supplied the transversality source",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) matter-slot transversality audit")
    print("======================================")
    print()
    print(f"finite_closed={calc.get('finite_transversality_theorem_closed')}")
    print(f"source_present={calc.get('selected_mtt_source_present')}")
    print(f"selected_packet_closed={calc.get('selected_ordered_su5_packet_closed')}")
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
