"""Audit the N=1 phase coboundary obstruction for Route C."""

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
CERT = CERT_DIR / "iwasawa_n1_phase_coboundary_obstruction_certificate.json"
PROMOTION_CERT = CERT_DIR / "iwasawa_selected_source_promotion_gate_certificate.json"
PHASE_CERT = CERT_DIR / "iwasawa_rotated_phase_mesh_rhoE_sector_prototype_certificate.json"
PAPER = ROOT / "Iwasawa_N1_Phase_Coboundary_Obstruction_v1.md"
SCRIPT = REPO / "scripts" / "analyze_iwasawa_n1_phase_coboundary_obstruction.py"
ROTATED_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_rotated_phase_mesh.py"
PROMOTION_VALIDATOR = REPO / "scripts" / "validate_iwasawa_selected_source_promotion.py"


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


def run_analysis() -> dict[str, Any]:
    code, output = run_command([sys.executable, str(SCRIPT)])
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def run_rotated_source_promotion(temp: Path) -> tuple[int, str]:
    candidate_path = temp / "rotated_phase.json"
    packet_path = temp / "rotated_phase_source_promotion.json"
    code, output = run_command(
        [
            sys.executable,
            str(ROTATED_CONSTRUCTOR),
            "--mesh-N",
            "1",
            "--modulus",
            "3",
            "--basis-indices",
            "0,1,2",
            "--emit-candidate",
            str(candidate_path),
        ]
    )
    if code != 0:
        raise RuntimeError(output)
    write_json(
        packet_path,
        {
            "schema": "IwasawaSelectedSourcePromotionPacket.v1",
            "status": "CANDIDATE",
            "target_level": "rhoE_source",
            "source_kind": "finite_HYM_Strominger_solve",
            "selected_source_verified": True,
            "no_observed_flavor_inputs": True,
            "uses_execution_ii_benchmarks": False,
            "uses_observed_masses_or_mixings": False,
            "uses_diagnostic_h1_three_as_selected": False,
            "uses_pure_gauge_prototype_as_selected": False,
            "paths": {
                "rhoE_mesh": str(candidate_path),
                "rhoE_metric": str(candidate_path),
                "sector_maps": str(candidate_path),
            },
        },
    )
    return run_command([sys.executable, str(PROMOTION_VALIDATOR), str(packet_path)])


def main() -> None:
    cert = load_json(CERT)
    promotion_cert = load_json(PROMOTION_CERT)
    phase_cert = load_json(PHASE_CERT)
    paper = read(PAPER)
    script_text = read(SCRIPT)
    analysis = run_analysis()

    with tempfile.TemporaryDirectory() as temp_dir:
        promotion_code, promotion_output = run_rotated_source_promotion(Path(temp_dir))

    certified_moduli = cert.get("certified_scope", {}).get("prime_fields", [])
    common_counts = cert.get("common_counts", {})
    field_results = cert.get("field_results", {})
    analyses = analysis.get("analyses", [])
    common_counts_match = all(
        entry.get("closed_nodes") == common_counts.get("closed_nodes")
        and entry.get("unknown_face_values") == common_counts.get("unknown_face_values")
        and entry.get("corner_equations") == common_counts.get("corner_equations")
        and entry.get("corner_equation_rank") == common_counts.get("corner_equation_rank")
        and entry.get("flat_solution_dimension") == common_counts.get("flat_solution_dimension")
        and entry.get("source_key_gauge_components") == common_counts.get("source_key_gauge_components")
        and entry.get("source_key_coboundary_rank") == common_counts.get("source_key_coboundary_rank")
        and entry.get("gauge_kernel_dimension") == common_counts.get("gauge_kernel_dimension")
        for entry in analyses
    )
    field_results_match = all(
        field_results.get(entry.get("field"), {}).get(
            "flat_solution_space_equals_source_key_coboundaries"
        )
        is True
        and entry.get("flat_solution_space_equals_source_key_coboundaries") is True
        and entry.get("coboundary_image_equation_residual_count") == 0
        for entry in analyses
    )

    gates = [
        Gate(
            "certificate status",
            "PROVED"
            if cert.get("status") == "IWASAWA_N1_PHASE_COBOUNDARY_OBSTRUCTION_PROVED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if promotion_cert.get("verdict", {}).get("promotion_gate_ready") is True
            and phase_cert.get("verdict", {}).get("finite_validator_stack_exercised_through_sector_maps") is True
            else "FAIL",
            "promotion gate and rotated phase prototype",
        ),
        Gate(
            "analysis script",
            "PASS"
            if contains_all(
                script_text,
                [
                    "flat_solution_space_equals_source_key_coboundaries",
                    "source_key_coboundary_rank",
                    "gauge_kernel_dimension",
                    "rhoE_source_promotion_possible_in_scalar_phase_ansatz",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "certified moduli",
            "PASS" if analysis.get("moduli") == certified_moduli else "FAIL",
            str(analysis.get("moduli")),
        ),
        Gate(
            "common counts",
            "PASS" if common_counts_match else "FAIL",
            str(analyses),
        ),
        Gate(
            "field results",
            "PASS" if field_results_match else "FAIL",
            str(field_results),
        ),
        Gate(
            "global verdict",
            "PASS"
            if analysis.get("global_verdict", {}).get("scalar_phase_ansatz_source_promotion_blocked")
            is True
            and analysis.get("global_verdict", {}).get("diagonal_rank_three_phase_ansatz_blocked_componentwise")
            is True
            and analysis.get("global_verdict", {}).get("constant_unitary_conjugates_blocked")
            is True
            else "FAIL",
            str(analysis.get("global_verdict", {})),
        ),
        Gate(
            "rotated source promotion rejected",
            "PASS"
            if promotion_code == 1
            and "rhoE_face_graph_coboundary=True" in promotion_output
            and "pure-gauge finite tables cannot be promoted" in promotion_output
            else "FAIL",
            f"exit={promotion_code}; output={promotion_output.strip()}",
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
            "PASS" if all(value is False for value in cert.get("guardrails", {}).values()) else "FAIL",
            str(cert.get("guardrails", {})),
        ),
        Gate(
            "paper records obstruction",
            "PASS"
            if contains_all(
                paper,
                [
                    "flat scalar phase solutions = source-key-compatible coboundaries",
                    "The scalar phase branch cannot pass source-level promotion",
                    "This is not a no-go theorem for MTT",
                    "search genuinely matrix-valued non-coboundary finite transition data",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa N=1 phase coboundary obstruction audit")
    print("==============================================")
    print()
    print(f"moduli={analysis.get('moduli')}")
    print(f"status={analysis.get('status')}")
    print(f"rotated_source_promotion_exit={promotion_code}")
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
