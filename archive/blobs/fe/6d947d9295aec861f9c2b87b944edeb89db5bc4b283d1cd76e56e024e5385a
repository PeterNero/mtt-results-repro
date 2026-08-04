"""Audit the SU(5) qutrit polarization-selection gate."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "su5_qutrit_polarization_selection_gate_certificate.json"
TEMPLATE = REPO / "certificates" / "selected_su5_qutrit_polarization_data.template.json"
PAPER = ROOT / "SU5_Qutrit_Polarization_Selection_Gate_v1.md"
SCRIPT = REPO / "scripts" / "analyze_su5_qutrit_polarization_selection_gate.py"


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
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    analysis = run_analysis()

    source = analysis.get("source_status", {})
    shortcut = analysis.get("finite_exterior_square_shortcut_test", {})
    closed = analysis.get("closed_now", {})
    remaining = analysis.get("remaining_finite_packet", {})
    verdict = analysis.get("verdict", {})
    guardrails = analysis.get("guardrails", {})
    calc = cert.get("calculation_results", {})
    cert_closed = cert.get("what_this_closes", {})
    cert_open = cert.get("still_open", {})
    cert_remaining = cert.get("remaining_finite_packet", {})
    cert_guardrails = cert.get("guardrails", {})
    cert_verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "SU5_QUTRIT_POLARIZATION_SELECTION_GATE_CLOSED_SELECTED_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["def wedge2", "hodge_transport_wedge2_to_dual"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "template open",
            "PASS"
            if template.get("status") == "OPEN"
            and template.get("sector_basis_data", {}).get("10_M", {}).get("basis_matrix_U10")
            is None
            and template.get("sector_basis_data", {}).get("bar5_M", {}).get(
                "basis_matrix_Ubar5"
            )
            is None
            else "FAIL",
            str(TEMPLATE),
        ),
        Gate(
            "source status",
            "PASS"
            if source.get("finite_transport_lemma_proved") is True
            and source.get("existing_direct_selector_found") is False
            and source.get("typed_monad_cech_can_close_now") is False
            and source.get("monad_can_compute_H1_now") is False
            and source.get("selected_projective_twist_source_found") is False
            and source.get("selected_zero_mode_sector_values_supplied") is False
            and source.get("selected_basis_template", {}).get(
                "selected_sector_basis_matrices_supplied"
            )
            is False
            else "FAIL",
            str(source),
        ),
        Gate(
            "exterior-square shortcut",
            "PASS"
            if shortcut.get("Z_cubed_identity") is True
            and shortcut.get("X_cubed_identity") is True
            and shortcut.get("wedge2_Z_is_monomial") is True
            and shortcut.get("wedge2_X_is_monomial") is True
            and shortcut.get("hodge_transport_is_monomial") is True
            and shortcut.get("hodge_support_count") == 3
            and shortcut.get("fourier_support_count") == 9
            and shortcut.get("hodge_can_equal_F_mod_rephase_permutation") is False
            and shortcut.get("exterior_square_shortcut_rejected") is True
            else "FAIL",
            str(shortcut),
        ),
        Gate(
            "closed-now fields",
            "PASS" if all(value is True for value in closed.values()) else "FAIL",
            str(closed),
        ),
        Gate(
            "remaining packet",
            "PASS"
            if remaining.get("target_template")
            == "certificates/selected_su5_qutrit_polarization_data.template.json"
            and remaining.get("required_matrices") == ["U_10", "U_bar5"]
            and any(
                "U_10^dagger U_bar5 equals F" in item
                for item in remaining.get("finite_acceptance_tests", [])
            )
            else "FAIL",
            str(remaining),
        ),
        Gate(
            "analysis verdict",
            "PASS"
            if verdict.get("sector_polarization_selection_proved_from_current_data") is False
            and verdict.get("can_promote_su5_qutrit_heavy_link_candidate_to_selected_input")
            is False
            and verdict.get("current_best_status")
            == "gate closed; selected sector-basis data still open"
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "analysis guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("finite_transport_lemma_proved") is True
            and calc.get("existing_direct_selector_found") is False
            and calc.get("typed_monad_cech_can_close_now") is False
            and calc.get("monad_can_compute_H1_now") is False
            and calc.get("selected_projective_twist_source_found") is False
            and calc.get("selected_zero_mode_sector_values_supplied") is False
            and calc.get("selected_sector_basis_matrices_supplied") is False
            and calc.get("exterior_square_shortcut_rejected") is True
            and calc.get("hodge_support_count") == 3
            and calc.get("fourier_support_count") == 9
            else "FAIL",
            str(calc),
        ),
        Gate(
            "certificate closed fields",
            "PASS" if all(value is True for value in cert_closed.values()) else "FAIL",
            str(cert_closed),
        ),
        Gate(
            "certificate still open",
            "PASS" if all(value is True for value in cert_open.values()) else "FAIL",
            str(cert_open),
        ),
        Gate(
            "certificate remaining packet",
            "PASS"
            if cert_remaining.get("target_template")
            == "certificates/selected_su5_qutrit_polarization_data.template.json"
            and cert_remaining.get("required_matrices") == ["U_10", "U_bar5"]
            else "FAIL",
            str(cert_remaining),
        ),
        Gate(
            "certificate guardrails",
            "PASS" if all(value is False for value in cert_guardrails.values()) else "FAIL",
            str(cert_guardrails),
        ),
        Gate(
            "certificate verdict",
            "PASS"
            if cert_verdict.get("sector_polarization_selection_proved_from_current_data")
            is False
            and cert_verdict.get(
                "can_promote_su5_qutrit_heavy_link_candidate_to_selected_input"
            )
            is False
            else "FAIL",
            str(cert_verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "10_M    uses the qutrit clock polarization",
                    "bar5_M  uses the qutrit shift polarization",
                    "wedge2(E) ~= E^*",
                    "monomial",
                    "cannot become `F`",
                    "selected_su5_qutrit_polarization_data.template.json",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) qutrit polarization-selection gate audit")
    print("==============================================")
    print()
    print(f"selected_now={verdict.get('sector_polarization_selection_proved_from_current_data')}")
    print(f"hodge_support={shortcut.get('hodge_support_count')}")
    print(f"fourier_support={shortcut.get('fourier_support_count')}")
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
