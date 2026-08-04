"""Audit the Route B heavy-link overlap-difference calculator."""

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
SCRIPT = REPO / "scripts" / "compute_route_b_heavy_link_delta_t.py"
TEMPLATE = REPO / "certificates" / "route_b_heavy_link_overlap_differences.template.json"
CERT = REPO / "certificates" / "route_b_heavy_link_overlap_difference_calculator_certificate.json"
DEPENDENCY = REPO / "candidate_data" / "dual_route_closure_attempt.candidate.json"
PAPER = ROOT / "Route_B_Heavy_Link_Overlap_Difference_Calculator_v1.md"


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


def run_packet(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def parse_first_json(text: str) -> dict[str, Any]:
    start = text.find("{")
    if start < 0:
        raise ValueError(f"no JSON object in output: {text}")
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(text[start:])
    return obj


def close(a: float, b: float, tol: float = 1e-9) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    cert = load_json(CERT)
    dependency = load_json(DEPENDENCY)
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    open_proc = run_packet(TEMPLATE)

    witness_packet = {
        "schema": "RouteBHeavyLinkOverlapDifferencePacket.v1",
        "status": "UNSELECTED_ALGEBRAIC_WITNESS",
        "candidate_role": "UNSELECTED_FIXTURE",
        "branch": "current_q79_orientation",
        "source": {
            "source_kind": "algebraic_witness",
            "source_certificate": "dual_route_closure_attempt_certificate.json",
            "selected_by_mtt": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "overlap_differences": {
            "A_left_delta": 0,
            "B_right_row1_delta": [-1.1906045653108346, 2.3861206759449765],
            "B_right_row2_delta": 0,
            "C_higgs_row1_delta": 0,
            "C_higgs_row2_delta": 0,
        },
        "extra_delta_t_terms": {
            "theta_overlap_variation_delta": [0, 0],
            "explicit_vertex_delta": [0, 0],
            "basis_connection_delta": [0, 0],
        },
    }

    with tempfile.TemporaryDirectory() as tmp:
        witness_path = Path(tmp) / "route_b_unselected_witness.json"
        witness_path.write_text(json.dumps(witness_packet, indent=2), encoding="utf-8")
        witness_proc = run_packet(witness_path)

    witness_report = parse_first_json(witness_proc.stdout) if witness_proc.returncode == 0 else {}
    delta_t = witness_report.get("Delta_t", [])
    calc = cert.get("calculation_results", {})
    route_b = (
        dependency.get("routes", {})
        .get("B_block_factorized_sector_resolved_C1", {})
        .get("branches", {})
        .get("current_q79_orientation", {})
    )

    gates = [
        Gate(
            "script present",
            "PASS"
            if SCRIPT.exists()
            and contains_all(
                script_text,
                [
                    "RouteBHeavyLinkDeltaT",
                    "RouteBHeavyLinkOverlapDifferencePacket.v1",
                    "theta_overlap_variation_delta",
                    "promotes_to_selected_CKM_heavy_link_input",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "template refuses open data",
            "PASS"
            if open_proc.returncode == 2
            and "packet status is OPEN" in open_proc.stdout
            and template.get("status") == "OPEN"
            else "FAIL",
            open_proc.stdout.strip(),
        ),
        Gate(
            "unselected witness computes",
            "PASS" if witness_proc.returncode == 0 else "FAIL",
            witness_proc.stdout.strip(),
        ),
        Gate(
            "witness reaches Delta_t10",
            "PASS"
            if len(delta_t) == 2 and close(float(delta_t[0]), 1.0) and close(float(delta_t[1]), 0.0)
            else "FAIL",
            str(delta_t),
        ),
        Gate(
            "witness not promoted",
            "PASS"
            if witness_report.get("candidate_role") == "UNSELECTED_FIXTURE"
            and witness_report.get("source_selected_by_mtt") is False
            and witness_report.get("promotes_to_selected_CKM_heavy_link_input") is False
            else "FAIL",
            str(
                {
                    "role": witness_report.get("candidate_role"),
                    "source": witness_report.get("source_selected_by_mtt"),
                    "promoted": witness_report.get("promotes_to_selected_CKM_heavy_link_input"),
                }
            ),
        ),
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "ROUTE_B_HEAVY_LINK_OVERLAP_DIFFERENCE_CALCULATOR_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "certificate records five slots",
            "PASS"
            if calc.get("difference_variables")
            == [
                "A_left_delta",
                "B_right_row1_delta",
                "B_right_row2_delta",
                "C_higgs_row1_delta",
                "C_higgs_row2_delta",
            ]
            and calc.get("extra_terms_required_or_certified_zero")
            == [
                "theta_overlap_variation_delta",
                "explicit_vertex_delta",
                "basis_connection_delta",
            ]
            else "FAIL",
            str(calc),
        ),
        Gate(
            "dependency rank two",
            "PASS"
            if route_b.get("rank_over_complex") == 2
            and calc.get("route_b_linear_rank_from_prior_certificate") == 2
            else "FAIL",
            str(route_b),
        ),
        Gate(
            "guardrails remain false",
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails")),
        ),
        Gate(
            "open fields remain open",
            "PASS" if all(value is True for value in cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open")),
        ),
        Gate(
            "paper records contract",
            "PASS"
            if contains_all(
                paper,
                [
                    "five-slot calculator",
                    "template refusal",
                    "unselected witness non-promotion",
                    "Still open",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Route B heavy-link overlap-difference calculator audit")
    print("======================================================")
    print()
    print(f"template_returncode={open_proc.returncode}")
    print(f"witness_returncode={witness_proc.returncode}")
    print(f"witness_Delta_t={delta_t}")
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
