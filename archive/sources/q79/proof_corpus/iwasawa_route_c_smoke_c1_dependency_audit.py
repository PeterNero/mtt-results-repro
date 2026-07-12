"""Audit the Route C smoke-to-C1 dependency reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_iwasawa_route_c_smoke_c1_dependency.py"
CANDIDATE = REPO / "candidate_data" / "iwasawa_route_c_smoke_c1_dependency.candidate.json"
CERT = REPO / "certificates" / "iwasawa_route_c_smoke_c1_dependency_certificate.json"
PAPER = ROOT / "Iwasawa_Route_C_Smoke_C1_Dependency_v1.md"
BRANCHES = ("current_q79_orientation", "conjugate_q369_orientation")
SECTORS = ("u", "d", "e", "nuD")
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
    raise TypeError(f"cannot parse {value!r}")


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


def branch(report: dict[str, Any], name: str) -> dict[str, Any]:
    return report.get("branches", {}).get(name, {})


def family_identical(report: dict[str, Any], name: str) -> bool:
    coeffs = (
        branch(report, name)
        .get("response_coefficients", {})
        .get("family_complement_coefficients", {})
    )
    q = [to_complex(value) for value in coeffs.get("Q", [])]
    for slot in ("u", "d", "L", "e", "N"):
        values = [to_complex(value) for value in coeffs.get(slot, [])]
        if len(values) != len(q) or any(abs(a - b) > TOL for a, b in zip(q, values)):
            return False
    return True


def sector_counts_ok(report: dict[str, Any]) -> bool:
    for name in BRANCHES:
        sectors = branch(report, name).get("sectors", {})
        for sector in SECTORS:
            counts = sectors.get(sector, {}).get(
                "unknown_complex_overlap_slots_if_theta_vertex_basis_absent", {}
            )
            if counts.get("full_matrix") != 15:
                return False
            if counts.get("heavy_link_entries_13_23") != 5:
                return False
            links = sectors.get(sector, {}).get("heavy_link_dependency", [])
            if len(links) != 2:
                return False
    return True


def universal_zero(report: dict[str, Any]) -> bool:
    for name in BRANCHES:
        test = branch(report, name).get("universal_tensor_test", {})
        if test.get("leading_ckm_heavy_link_from_smoke_dotD_only") is not False:
            return False
        if test.get("Delta_t_ud_for_heavy_links") != [0.0, 0.0]:
            return False
    return True


def main() -> None:
    report = run_script()
    candidate = load_json(CANDIDATE)
    cert = load_json(CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    calc = report.get("calculation_results", {})
    cert_calc = cert.get("calculation_results", {})

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "IwasawaRouteCSmokeC1Dependency",
                    "universal_tensor_case_gives_Delta_t_zero",
                    "sector-resolved trilinear overlap tensors",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "candidate status",
            "PASS"
            if candidate.get("status") == "SYMBOLIC_DEPENDENCY_REDUCED_NUMERIC_VALUES_OPEN"
            and cert.get("status") == candidate.get("status")
            else "FAIL",
            str((candidate.get("status"), cert.get("status"))),
        ),
        Gate(
            "branch coefficients conjugate",
            "PASS"
            if calc.get("branch_pair_coefficients_are_conjugate") is True
            and cert_calc.get("branch_pair_coefficients_are_conjugate") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "family slots identical",
            "PASS" if all(family_identical(report, name) for name in BRANCHES) else "FAIL",
            str({name: family_identical(report, name) for name in BRANCHES}),
        ),
        Gate(
            "sector unknown counts",
            "PASS" if sector_counts_ok(report) else "FAIL",
            "15 full-matrix slots and 5 heavy-link slots per sector",
        ),
        Gate(
            "universal tensor no-go",
            "PASS"
            if universal_zero(report)
            and calc.get("universal_tensor_case_gives_Delta_t_zero") is True
            and calc.get("route_c_smoke_dotD_alone_closes_ckm_heavy_link") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "new required data",
            "PASS"
            if calc.get("new_required_selected_data")
            == [
                "sector-resolved trilinear overlap tensors T_s",
                "or selected SU(5) 10/bar5/H basis transport",
                "or selected theta/vertex/basis primitive terms",
            ]
            else "FAIL",
            str(calc.get("new_required_selected_data")),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "still open",
            "PASS" if all(value is True for value in cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "candidate file matches run",
            "PASS"
            if candidate.get("calculation_results") == report.get("calculation_results")
            and candidate.get("conjugate_branch_check") == report.get("conjugate_branch_check")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "paper records result",
            "PASS"
            if contains_all(
                paper,
                [
                    "15 complex overlap slots per sector",
                    "5 complex overlap slots per sector",
                    "M_u = M_d",
                    "Delta_t",
                    "not a selected C1 response computation",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa Route C smoke-to-C1 dependency audit")
    print("============================================")
    print()
    print(f"branch_pair_conjugate={calc.get('branch_pair_coefficients_are_conjugate')}")
    print(f"universal_tensor_delta_zero={calc.get('universal_tensor_case_gives_Delta_t_zero')}")
    print(f"heavy_link_unknowns_per_sector={calc.get('heavy_link_overlap_unknowns_per_sector')}")
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
