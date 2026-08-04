"""Audit the Iwasawa selected-source promotion gate."""

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
CERT = CERT_DIR / "iwasawa_selected_source_promotion_gate_certificate.json"
FACE_CERT = CERT_DIR / "iwasawa_face_graph_coboundary_diagnostic_certificate.json"
PAPER = ROOT / "Iwasawa_Selected_Source_Promotion_Gate_v1.md"
VALIDATOR = REPO / "scripts" / "validate_iwasawa_selected_source_promotion.py"
PUREGAUGE_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_puregauge_nonabelian_mesh.py"


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


def emit_puregauge(candidate_path: Path) -> None:
    code, output = run_command(
        [
            sys.executable,
            str(PUREGAUGE_CONSTRUCTOR),
            "--mesh-N",
            "1",
            "--emit-candidate",
            str(candidate_path),
        ]
    )
    if code != 0:
        raise RuntimeError(output)


def base_packet(candidate_path: Path, *, target_level: str) -> dict[str, Any]:
    return {
        "schema": "IwasawaSelectedSourcePromotionPacket.v1",
        "status": "CANDIDATE",
        "target_level": target_level,
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
    }


def validate_packet(packet_path: Path) -> tuple[int, str]:
    return run_command([sys.executable, str(VALIDATOR), str(packet_path)])


def main() -> None:
    cert = load_json(CERT)
    face_cert = load_json(FACE_CERT)
    paper = read(PAPER)
    validator_text = read(VALIDATOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        puregauge_path = temp / "puregauge_nonabelian.json"
        emit_puregauge(puregauge_path)

        open_packet_path = temp / "open_packet.json"
        write_json(
            open_packet_path,
            {
                "schema": "IwasawaSelectedSourcePromotionPacket.v1",
                "status": "OPEN",
                "target_level": "de_response",
            },
        )
        open_code, open_output = validate_packet(open_packet_path)

        pure_source_path = temp / "pure_source_packet.json"
        write_json(pure_source_path, base_packet(puregauge_path, target_level="rhoE_source"))
        pure_source_code, pure_source_output = validate_packet(pure_source_path)

        benchmark_path = temp / "benchmark_flag_packet.json"
        benchmark_packet = base_packet(puregauge_path, target_level="rhoE_source")
        benchmark_packet["uses_execution_ii_benchmarks"] = True
        write_json(benchmark_path, benchmark_packet)
        benchmark_code, benchmark_output = validate_packet(benchmark_path)

        de_missing_path = temp / "de_missing_packet.json"
        write_json(de_missing_path, base_packet(puregauge_path, target_level="de_response"))
        de_missing_code, de_missing_output = validate_packet(de_missing_path)

    implemented = cert.get("implemented_checks", {})
    audit_cases = cert.get("audit_cases", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_SELECTED_SOURCE_PROMOTION_GATE_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "face diagnostic dependency",
            "PASS"
            if face_cert.get("verdict", {}).get("diagnostic_ready") is True
            else "FAIL",
            str(FACE_CERT),
        ),
        Gate(
            "validator script",
            "PASS"
            if contains_all(
                validator_text,
                [
                    "IwasawaSelectedSourcePromotionPacket.v1",
                    "detect_iwasawa_face_graph_coboundary.py",
                    "validate_iwasawa_dotd_response.py",
                    "dotd_response_norms",
                    "rhoE_source promotion requires a non-coboundary finite face graph",
                ],
            )
            else "FAIL",
            str(VALIDATOR),
        ),
        Gate(
            "implemented checks",
            "PASS" if all(implemented.values()) else "FAIL",
            str(implemented),
        ),
        Gate(
            "open packet refused",
            "PASS"
            if open_code == 2 and "OPEN" in open_output
            else "FAIL",
            f"exit={open_code}; output={open_output.strip()}",
        ),
        Gate(
            "pure gauge source rejected",
            "PASS"
            if pure_source_code == 1
            and "rhoE_face_graph_coboundary=True" in pure_source_output
            and "pure-gauge finite tables cannot be promoted" in pure_source_output
            else "FAIL",
            f"exit={pure_source_code}; output={pure_source_output.strip()}",
        ),
        Gate(
            "benchmark packet rejected",
            "PASS"
            if benchmark_code == 1
            and "uses_execution_ii_benchmarks must be false" in benchmark_output
            else "FAIL",
            f"exit={benchmark_code}; output={benchmark_output.strip()}",
        ),
        Gate(
            "de response missing downstream",
            "PASS"
            if de_missing_code == 2 and "paths.route_c_residuals" in de_missing_output
            else "FAIL",
            f"exit={de_missing_code}; output={de_missing_output.strip()}",
        ),
        Gate(
            "audit cases",
            "PASS" if all(audit_cases.values()) else "FAIL",
            str(audit_cases),
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
            if verdict.get("promotion_gate_ready") is True
            and verdict.get("current_finite_noncommuting_prototypes_remain_unpromoted") is True
            and "dotD response" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "if face_graph_coboundary = true, rhoE_source promotion fails",
                    "noncommuting finite table values can still be pure gauge",
                    "max horizontal response norm",
                    "It is not a selected SM proof source",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa selected-source promotion gate audit")
    print("============================================")
    print()
    print(f"open_packet_exit={open_code}")
    print(f"pure_source_exit={pure_source_code}")
    print(f"benchmark_packet_exit={benchmark_code}")
    print(f"de_missing_exit={de_missing_code}")
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
