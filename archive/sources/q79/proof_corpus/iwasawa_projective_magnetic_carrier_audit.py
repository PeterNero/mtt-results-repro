"""Audit the projective magnetic-translation carrier prototype."""

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
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_projective_magnetic_carrier_certificate.json"
PROMOTION_CERT = CERT_DIR / "iwasawa_selected_source_promotion_gate_certificate.json"
SOLVABLE_CERT = CERT_DIR / "iwasawa_n1_solvable_carrier_obstruction_certificate.json"
PAPER = ROOT / "Iwasawa_Projective_Magnetic_Carrier_v1.md"
SCRIPT = REPO / "scripts" / "construct_iwasawa_projective_magnetic_carrier.py"
MESH_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_mesh.py"
METRIC_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_metric.py"
COBOUNDARY_DIAGNOSTIC = REPO / "scripts" / "detect_iwasawa_face_graph_coboundary.py"


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


def construct_summary(candidate_path: Path) -> dict[str, Any]:
    code, output = run_command(
        [sys.executable, str(SCRIPT), "--emit-candidate", str(candidate_path)]
    )
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def main() -> None:
    cert = load_json(CERT)
    promotion_cert = load_json(PROMOTION_CERT)
    solvable_cert = load_json(SOLVABLE_CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)

    with tempfile.TemporaryDirectory() as temp_dir:
        candidate_path = Path(temp_dir) / "projective_magnetic_carrier.json"
        summary = construct_summary(candidate_path)
        mesh_exit, mesh_output = run_command(
            [sys.executable, str(MESH_VALIDATOR), str(candidate_path)]
        )
        metric_exit, metric_output = run_command(
            [sys.executable, str(METRIC_VALIDATOR), str(candidate_path)]
        )
        coboundary_exit, coboundary_output = run_command(
            [sys.executable, str(COBOUNDARY_DIAGNOSTIC), str(candidate_path)]
        )
        if coboundary_exit != 0:
            raise RuntimeError(coboundary_output)
        coboundary = json.loads(coboundary_output)

    diagnostic = summary.get("diagnostic", {})
    expected = cert.get("mesh_N1_diagnostic", {})
    validator_behavior = cert.get("validator_behavior", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "IWASAWA_PROJECTIVE_MAGNETIC_CARRIER_PROTOTYPE_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if promotion_cert.get("verdict", {}).get("promotion_gate_ready") is True
            and solvable_cert.get("verdict", {}).get(
                "finite_solvable_carriers_blocked_at_N1_source_level"
            )
            is True
            else "FAIL",
            "promotion gate and solvable obstruction",
        ),
        Gate(
            "constructor script",
            "PASS"
            if contains_all(
                script_text,
                [
                    "clock_matrix",
                    "shift_matrix",
                    "projective_gerbe_gluing_passes",
                    "central_twist_is_nontrivial",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "projective diagnostic",
            "PASS"
            if diagnostic.get("strict_mismatch_count")
            == expected.get("strict_mismatch_count")
            and diagnostic.get("projective_mismatch_count")
            == expected.get("projective_mismatch_count")
            and diagnostic.get("nontrivial_central_twist_count")
            == expected.get("nontrivial_central_twist_count")
            and diagnostic.get("central_phase_histogram")
            == expected.get("central_phase_histogram")
            and diagnostic.get("projective_gerbe_gluing_passes") is True
            and diagnostic.get("strict_vector_bundle_gluing_passes") is False
            and diagnostic.get("max_centrality_error", 1.0)
            < expected.get("max_centrality_error_below", 0.0)
            and diagnostic.get("max_pairwise_commutator_abs", 0.0)
            > expected.get("max_pairwise_commutator_abs_above", 1e9)
            else "FAIL",
            str(diagnostic),
        ),
        Gate(
            "ordinary mesh rejected",
            "PASS"
            if mesh_exit == validator_behavior.get("ordinary_rhoE_mesh_validator_exit")
            and "corner product mismatch" in mesh_output
            else "FAIL",
            f"exit={mesh_exit}; output={mesh_output[:240]!r}",
        ),
        Gate(
            "metric validator passes",
            "PASS"
            if metric_exit == validator_behavior.get("rhoE_metric_validator_exit")
            and "rho_E metric validation PASS" in metric_output
            else "FAIL",
            f"exit={metric_exit}; output={metric_output.strip()}",
        ),
        Gate(
            "face coboundary false",
            "PASS"
            if coboundary.get("face_graph_coboundary")
            == validator_behavior.get("face_graph_coboundary")
            and coboundary.get("max_consistency_error", 0.0) > 1.0
            else "FAIL",
            str(coboundary),
        ),
        Gate(
            "what this closes",
            "PASS" if all(cert.get("what_this_closes", {}).values()) else "FAIL",
            str(cert.get("what_this_closes", {})),
        ),
        Gate(
            "still open",
            "OPEN" if all(cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open", {})),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("projective_route_is_live_but_requires_new_selected_twist_data")
            is True
            and verdict.get("ordinary_source_promotion_is_forbidden") is True
            and "gerbe" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records route",
            "PASS"
            if contains_all(
                paper,
                [
                    "projective representations",
                    "ordinary vector-bundle gluing fails",
                    "projective gerbe-style gluing holds",
                    "Freed-Witten",
                    "twisted rho_E promotion gate",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa projective magnetic carrier audit")
    print("=========================================")
    print()
    print(f"mesh_exit={mesh_exit}")
    print(f"metric_exit={metric_exit}")
    print(f"face_graph_coboundary={coboundary.get('face_graph_coboundary')}")
    print(f"strict_mismatch_count={diagnostic.get('strict_mismatch_count')}")
    print(f"nontrivial_central_twist_count={diagnostic.get('nontrivial_central_twist_count')}")
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
