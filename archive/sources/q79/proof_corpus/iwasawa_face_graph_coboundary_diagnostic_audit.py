"""Audit the finite face-graph coboundary diagnostic for rho_E tables."""

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
CERT = CERT_DIR / "iwasawa_face_graph_coboundary_diagnostic_certificate.json"
PUREGAUGE_CERT = CERT_DIR / "iwasawa_puregauge_nonabelian_mesh_rhoE_prototype_certificate.json"
ROTATED_CERT = CERT_DIR / "iwasawa_rotated_phase_mesh_rhoE_sector_prototype_certificate.json"
MESH_VALIDATOR_CERT = CERT_DIR / "iwasawa_rhoE_mesh_validator_certificate.json"
PAPER = ROOT / "Iwasawa_Face_Graph_Coboundary_Diagnostic_v1.md"
DETECTOR = REPO / "scripts" / "detect_iwasawa_face_graph_coboundary.py"
PUREGAUGE_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_puregauge_nonabelian_mesh.py"
ROTATED_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_rotated_phase_mesh.py"
MESH_VALIDATOR = REPO / "scripts" / "validate_iwasawa_rhoE_mesh.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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


def emit_candidate(script: Path, candidate_path: Path, extra_args: list[str] | None = None) -> dict[str, Any]:
    args = [sys.executable, str(script), "--mesh-N", "1"]
    if extra_args:
        args.extend(extra_args)
    args.extend(["--emit-candidate", str(candidate_path)])
    code, output = run_command(args)
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def detect(candidate_path: Path) -> dict[str, Any]:
    code, output = run_command([sys.executable, str(DETECTOR), str(candidate_path)])
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def mesh_validate(candidate_path: Path) -> int:
    code, _ = run_command([sys.executable, str(MESH_VALIDATOR), str(candidate_path)])
    return code


def corrupt_first_g1(candidate_path: Path, out_path: Path) -> None:
    data = load_json(candidate_path)
    g1_values = data["generator_data"]["g1"]["values"]
    first_key = sorted(g1_values)[0]
    matrix = g1_values[first_key]["matrix"]
    g1_values[first_key]["matrix"] = [
        [
            -entry if isinstance(entry, (int, float)) else [-entry[0], -entry[1]]
            for entry in row
        ]
        for row in matrix
    ]
    write_json(out_path, data)


def main() -> None:
    cert = load_json(CERT)
    puregauge_cert = load_json(PUREGAUGE_CERT)
    rotated_cert = load_json(ROTATED_CERT)
    mesh_cert = load_json(MESH_VALIDATOR_CERT)
    paper = read(PAPER)
    detector_text = read(DETECTOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        puregauge_path = temp / "puregauge_nonabelian.json"
        rotated_path = temp / "rotated_phase.json"
        corrupted_path = temp / "corrupted_cycle.json"

        emit_candidate(PUREGAUGE_CONSTRUCTOR, puregauge_path)
        emit_candidate(
            ROTATED_CONSTRUCTOR,
            rotated_path,
            ["--modulus", "3", "--basis-indices", "0,1,2"],
        )
        corrupt_first_g1(puregauge_path, corrupted_path)

        puregauge = detect(puregauge_path)
        rotated = detect(rotated_path)
        corrupted = detect(corrupted_path)
        puregauge_mesh_exit = mesh_validate(puregauge_path)
        rotated_mesh_exit = mesh_validate(rotated_path)

    expected_counts = cert.get("expected_N1_graph_counts", {})
    actual_counts = {
        "closed_nodes": puregauge.get("closed_nodes"),
        "face_incidences": puregauge.get("face_incidences"),
        "unique_face_keys": puregauge.get("unique_face_keys"),
        "graph_connected_components": puregauge.get("graph_connected_components"),
    }
    proto = cert.get("prototype_diagnostics", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_FACE_GRAPH_COBOUNDARY_DIAGNOSTIC_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if puregauge_cert.get("verdict", {}).get("finite_validator_stack_handles_noncommuting_tables")
            is True
            and rotated_cert.get("verdict", {}).get("finite_validator_stack_exercised_through_sector_maps")
            is True
            and mesh_cert.get("verdict", {}).get("closes_finite_mesh_validator_for_rhoE_candidates")
            is True
            else "FAIL",
            "puregauge prototype, rotated prototype, mesh validator imported",
        ),
        Gate(
            "detector script",
            "PASS"
            if contains_all(
                detector_text,
                [
                    "matrix_inverse",
                    "build_edges",
                    "face_graph_coboundary",
                    "max_edge_reconstruction_error",
                ],
            )
            else "FAIL",
            str(DETECTOR),
        ),
        Gate(
            "N1 graph counts",
            "PASS" if actual_counts == expected_counts else "FAIL",
            str(actual_counts),
        ),
        Gate(
            "puregauge prototype detected",
            "PASS"
            if puregauge.get("face_graph_coboundary") is True
            and puregauge.get("max_consistency_error", 1.0)
            < proto.get("puregauge_nonabelian_prototype", {}).get("max_consistency_error_below", 0.0)
            and puregauge_mesh_exit == proto.get("puregauge_nonabelian_prototype", {}).get("mesh_validator_exit")
            else "FAIL",
            str(puregauge),
        ),
        Gate(
            "rotated prototype detected",
            "PASS"
            if rotated.get("face_graph_coboundary") is True
            and rotated.get("max_consistency_error", 1.0)
            < proto.get("rotated_phase_sector_prototype", {}).get("max_consistency_error_below", 0.0)
            and rotated_mesh_exit == proto.get("rotated_phase_sector_prototype", {}).get("mesh_validator_exit")
            else "FAIL",
            str(rotated),
        ),
        Gate(
            "corrupted candidate rejected",
            "PASS"
            if corrupted.get("face_graph_coboundary") is False
            and corrupted.get("max_consistency_error", 0.0)
            > proto.get("corrupted_cycle_candidate", {}).get("max_consistency_error_above", 1e9)
            else "FAIL",
            str(corrupted),
        ),
        Gate(
            "what this closes",
            "PASS"
            if all(cert.get("what_this_closes", {}).values())
            else "FAIL",
            str(cert.get("what_this_closes", {})),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(cert.get("still_open", {}).values())
            else "FAIL",
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
            if verdict.get("diagnostic_ready") is True
            and verdict.get("finite_noncommuting_prototype_is_pure_gauge") is True
            and "D_E response" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records diagnostic",
            "PASS"
            if contains_all(
                paper,
                [
                    "face_graph_coboundary = true",
                    "face_graph_coboundary = false",
                    "noncommuting finite table data are not sufficient",
                    "not merely pure gauge",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa face-graph coboundary diagnostic audit")
    print("==============================================")
    print()
    print(f"puregauge_coboundary={puregauge.get('face_graph_coboundary')}")
    print(f"rotated_coboundary={rotated.get('face_graph_coboundary')}")
    print(f"corrupted_coboundary={corrupted.get('face_graph_coboundary')}")
    print(f"corrupted_max_error={corrupted.get('max_consistency_error')}")
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
