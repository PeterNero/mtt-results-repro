"""Audit the SU(5) qutrit basis-transport heavy-link candidate."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json"
CANDIDATE = REPO / "candidate_data" / "su5_qutrit_basis_transport_heavy_link.candidate.json"
PAPER = ROOT / "SU5_Qutrit_Basis_Transport_Heavy_Link_Candidate_v1.md"
SCRIPT = REPO / "scripts" / "analyze_su5_qutrit_basis_transport_heavy_links.py"
C1_CALCULATOR = REPO / "scripts" / "compute_c1_heavy_link_delta_t.py"
CKM_CALCULATOR = REPO / "scripts" / "compute_ckm_heavy_link_gate.py"
TOL = 1e-9


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


def to_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(value)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"cannot parse complex value {value!r}")


def approx_vector(values: list[Any], expected: list[complex]) -> bool:
    parsed = [to_complex(value) for value in values]
    return all(abs(value - target) < TOL for value, target in zip(parsed, expected))


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


def run_c1_fixture(packet: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "su5_transport_candidate_packet.json"
        path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(C1_CALCULATOR), str(path)],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def run_ckm_fixture(packet: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "su5_transport_candidate_ckm_packet.json"
        path.write_text(json.dumps(packet, indent=2), encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(CKM_CALCULATOR), str(path)],
            cwd=REPO,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout)
    return json.loads(proc.stdout)


def case_by_name(analysis: dict[str, Any], name: str) -> dict[str, Any]:
    for case in analysis.get("cases", []):
        if case.get("name") == name:
            return case
    return {}


def main() -> None:
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    analysis = run_analysis()
    best = analysis.get("best_candidate", {})
    fixture = run_c1_fixture(best.get("candidate_c1_heavy_link_primitives_packet", {}))
    ckm_fixture = run_ckm_fixture(best.get("candidate_ckm_heavy_link_packet", {}))

    expected = [
        1.0 / 3.0**0.5,
        complex(-1.0 / (2.0 * 3.0**0.5), -0.5),
    ]
    inverse_expected = [
        1.0 / 3.0**0.5,
        complex(-1.0 / (2.0 * 3.0**0.5), 0.5),
    ]
    aligned = case_by_name(analysis, "aligned_identity")
    common = case_by_name(analysis, "common_fourier_gauge")
    split = case_by_name(analysis, "su5_split_B10_identity_Bbar5_fourier")

    calc = cert.get("calculation_results", {})
    closed = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "SU5_QUTRIT_BASIS_TRANSPORT_HEAVY_LINK_CANDIDATE_VALIDATED_UNSELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "script exists",
            "PASS"
            if SCRIPT.exists()
            and contains_all(script_text, ["B_left^* I B_right", "10_M x bar5_M", "common unitary"])
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "unitary checks",
            "PASS" if all(analysis.get("unitarity_checks", {}).values()) else "FAIL",
            str(analysis.get("unitarity_checks")),
        ),
        Gate(
            "common transport cancels",
            "PASS"
            if analysis.get("gauge_cancellation", {}).get("aligned_identity_delta_zero") is True
            and analysis.get("gauge_cancellation", {}).get("common_fourier_delta_zero") is True
            and aligned.get("leading_heavy_link_gate_if_selected") is False
            and common.get("leading_heavy_link_gate_if_selected") is False
            else "FAIL",
            str(analysis.get("gauge_cancellation")),
        ),
        Gate(
            "SU5 split nonzero",
            "PASS"
            if split.get("leading_heavy_link_gate_if_selected") is True
            and approx_vector(split.get("Delta_t_candidate", []), expected)
            and approx_vector(best.get("Delta_t_candidate_numeric", []), expected)
            else "FAIL",
            str(best.get("Delta_t_candidate_numeric")),
        ),
        Gate(
            "inverse convention",
            "PASS"
            if approx_vector(
                analysis.get("inverse_candidate", {}).get("Delta_t_candidate_numeric", []),
                inverse_expected,
            )
            else "FAIL",
            str(analysis.get("inverse_candidate")),
        ),
        Gate(
            "C1 fixture computes",
            "PASS"
            if fixture.get("character_trivial_leading_noncommutation_pass") is True
            and approx_vector(fixture.get("Delta_t", []), expected)
            else "FAIL",
            json.dumps(fixture, sort_keys=True),
        ),
        Gate(
            "CKM gate fixture computes",
            "PASS"
            if ckm_fixture.get("gate", {}).get("leading_noncommutation_pass") is True
            and ckm_fixture.get("gate", {}).get("c6_affects_leading_gate") is False
            and approx_vector(ckm_fixture.get("derived", {}).get("Delta_c", []), [0j, 0j])
            and approx_vector(ckm_fixture.get("derived", {}).get("Delta_v", []), expected)
            else "FAIL",
            json.dumps(ckm_fixture, sort_keys=True),
        ),
        Gate(
            "candidate file guardrails",
            "PASS"
            if candidate.get("status") == "NONSELECTED_CANDIDATE"
            and candidate.get("best_candidate", {}).get("leading_heavy_link_gate_if_selected") is True
            and all(value is False for value in candidate.get("guardrails", {}).values())
            else "FAIL",
            str(candidate.get("guardrails")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("fourier_unitary_verified") is True
            and calc.get("aligned_identity_delta_zero") is True
            and calc.get("common_fourier_transport_delta_zero") is True
            and calc.get("su5_representation_split_nonzero") is True
            and calc.get("candidate_c1_fixture_passes_delta_t_calculator") is True
            and calc.get("candidate_ckm_fixture_passes_heavy_link_gate") is True
            and calc.get("candidate_ckm_fixture_uses_delta_c_zero") is True
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
            if verdict.get("representation_split_fourier_transport_is_a_viable_exact_candidate") is True
            and verdict.get("common_fourier_transport_is_not_viable_because_it_cancels") is True
            and verdict.get("candidate_promotes_missing_numbers_only_after_selection_theorem") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records candidate",
            "PASS"
            if contains_all(
                paper,
                [
                    "B_10=I_3",
                    "B_bar5=F",
                    "10_M x 10_M",
                    "10_M x bar5_M",
                    "common Fourier transport is only",
                    "Sector Transport Selection Lemma",
                    "This is not selected MTT data yet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("SU(5) qutrit basis transport heavy-link candidate audit")
    print("=======================================================")
    print()
    print(f"candidate_delta_t={best.get('Delta_t_candidate_numeric')}")
    print(f"fixture_delta_t={fixture.get('Delta_t')}")
    print(f"ckm_fixture_delta_v={ckm_fixture.get('derived', {}).get('Delta_v')}")
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
