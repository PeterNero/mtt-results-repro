"""Audit the SU(5) qutrit transport-selector source hunt."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "su5_qutrit_transport_selector_hunt_certificate.json"
PAPER = ROOT / "SU5_Qutrit_Transport_Selector_Hunt_v1.md"
SCRIPT = REPO / "scripts" / "hunt_su5_qutrit_transport_selector.py"


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


def run_hunt() -> dict[str, Any]:
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
    script_text = read(SCRIPT)
    hunt = run_hunt()

    ingredients = hunt.get("supporting_ingredients", {})
    verdict = hunt.get("verdict", {})
    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    cert_verdict = cert.get("verdict", {})
    expected_exclusions = {
        "su5_qutrit_basis_transport",
        "su5_qutrit_transport_selector",
        "qutrit_polarization_transport_lemma",
        "prove_qutrit_polarization_transport",
        "su5_qutrit_polarization_selection",
        "selected_su5_qutrit_polarization",
        "su5_projection_tensor_derivation",
        "selected_su5_source_proof_attempt",
        "attempt_selected_su5_source_proof",
        "selected_fourier_transport_proof_attempt",
        "attempt_selected_fourier_transport_proof",
        "selected_gerbe_fourier_type",
        "prove_selected_gerbe_fourier_type",
        "time_oriented_conjugate_branch_selection",
        "prove_time_oriented_conjugate_branch_selection",
        "su5_matter_slot_transversality",
        "prove_su5_matter_slot_transversality",
        "selected_matter_slot_transversality_source",
        "validate_selected_matter_slot_transversality_source",
        "attempt_fill_selected_matter_slot_transversality_source",
        "selected_matter_source_two_path_exploration",
        "explore_selected_matter_source_two_paths",
        "selected_hym_operator_source",
        "validate_selected_hym_operator_source",
        "attempt_selected_hym_operator_source",
        "visible_operator_source_blocker_resolution",
        "resolve_visible_operator_source_blocker",
        "q79_theorem_change_list_for_paper_updates",
    }

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status") == "SU5_QUTRIT_TRANSPORT_SELECTOR_NOT_FOUND_CANDIDATE_CONDITIONAL"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["direct_selector_predicate", "EXCLUDE_SUBSTRINGS"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "support ingredients present",
            "PASS"
            if all(len(ingredients.get(key, [])) > 0 for key in ingredients)
            and verdict.get("ingredients_present_separately") is True
            else "FAIL",
            str(ingredients),
        ),
        Gate(
            "direct selector absent",
            "PASS"
            if hunt.get("selector_found") is False
            and hunt.get("direct_selector_hits") == []
            and verdict.get("selected_B10_Bbar5_transport_found") is False
            else "FAIL",
            str(hunt.get("direct_selector_hits")),
        ),
        Gate(
            "generated files excluded from hunt",
            "PASS"
            if expected_exclusions.issubset(set(hunt.get("exclusions", [])))
            and calc.get("candidate_files_excluded_from_source_hunt") is True
            and calc.get("finite_transport_lemma_files_excluded_from_source_hunt") is True
            and calc.get("polarization_selection_gate_files_excluded_from_source_hunt") is True
            and calc.get("downstream_source_proof_attempt_files_excluded_from_source_hunt") is True
            and calc.get("selected_fourier_proof_attempt_files_excluded_from_source_hunt") is True
            and calc.get("selected_gerbe_fourier_type_files_excluded_from_source_hunt") is True
            and calc.get("time_oriented_branch_selection_files_excluded_from_source_hunt") is True
            and calc.get("su5_matter_slot_transversality_files_excluded_from_source_hunt") is True
            and calc.get("selected_matter_slot_source_files_excluded_from_source_hunt") is True
            and calc.get("selected_matter_source_two_path_files_excluded_from_source_hunt") is True
            and calc.get("selected_hym_operator_source_files_excluded_from_source_hunt") is True
            and calc.get("visible_operator_source_resolution_files_excluded_from_source_hunt") is True
            else "FAIL",
            str(hunt.get("exclusions")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("su5_yukawa_split_present") is True
            and calc.get("qutrit_clock_shift_present") is True
            and calc.get("fourier_common_gauge_guardrail_present") is True
            and calc.get("zero_mode_or_monad_route_present") is True
            and calc.get("direct_selector_found") is False
            and calc.get("finite_transport_lemma_files_excluded_from_source_hunt") is True
            and calc.get("downstream_source_proof_attempt_files_excluded_from_source_hunt") is True
            and calc.get("selected_fourier_proof_attempt_files_excluded_from_source_hunt") is True
            and calc.get("selected_gerbe_fourier_type_files_excluded_from_source_hunt") is True
            and calc.get("time_oriented_branch_selection_files_excluded_from_source_hunt") is True
            and calc.get("su5_matter_slot_transversality_files_excluded_from_source_hunt") is True
            and calc.get("selected_matter_slot_source_files_excluded_from_source_hunt") is True
            and calc.get("selected_matter_source_two_path_files_excluded_from_source_hunt") is True
            and calc.get("selected_hym_operator_source_files_excluded_from_source_hunt") is True
            and calc.get("visible_operator_source_resolution_files_excluded_from_source_hunt") is True
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
            if cert_verdict.get("ingredients_present_separately") is True
            and cert_verdict.get("selected_B10_Bbar5_transport_found") is False
            and cert_verdict.get("candidate_status") == "conditional"
            else "FAIL",
            str(cert_verdict),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "selected B_10/B_bar5 transport theorem = absent",
                    "candidate remains legitimate but conditional",
                    "typed monad/Cech cohomology",
                    "non-invariant spectral Galerkin zero modes",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) qutrit transport selector hunt audit")
    print("==========================================")
    print()
    print(f"selector_found={hunt.get('selector_found')}")
    print(f"direct_selector_hits={hunt.get('direct_selector_hits')}")
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
