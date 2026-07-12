"""Audit the projective finite-mesh rho_E validator."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_projective_rhoE_mesh_validator_certificate.json"
PROJECTIVE_CERT = CERT_DIR / "iwasawa_projective_magnetic_carrier_certificate.json"
PUREGAUGE_CERT = CERT_DIR / "iwasawa_puregauge_nonabelian_mesh_rhoE_prototype_certificate.json"
PAPER = ROOT / "Iwasawa_Projective_RhoE_Mesh_Validator_v1.md"
VALIDATOR = REPO / "scripts" / "validate_iwasawa_projective_rhoE_mesh.py"
PROJECTIVE_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_projective_magnetic_carrier.py"
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


def emit_candidate(script: Path, out_path: Path) -> None:
    code, output = run_command(
        [sys.executable, str(script), "--mesh-N", "1", "--emit-candidate", str(out_path)]
    )
    if code != 0:
        raise RuntimeError(output)


def parse_report(output: str) -> dict[str, Any]:
    match = re.search(r"projective_report=(\{.*\})", output)
    if not match:
        raise RuntimeError(f"missing projective_report in output: {output}")
    return json.loads(match.group(1))


def corrupt_noncentral(candidate_path: Path, out_path: Path) -> None:
    data = load_json(candidate_path)
    data["generator_data"]["g3"] = {
        "matrix": [
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]
        ]
    }
    write_json(out_path, data)


def main() -> None:
    cert = load_json(CERT)
    projective_cert = load_json(PROJECTIVE_CERT)
    puregauge_cert = load_json(PUREGAUGE_CERT)
    paper = read(PAPER)
    validator_text = read(VALIDATOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        projective_path = temp / "projective.json"
        puregauge_path = temp / "puregauge.json"
        corrupted_path = temp / "noncentral_corrupted.json"

        emit_candidate(PROJECTIVE_CONSTRUCTOR, projective_path)
        emit_candidate(PUREGAUGE_CONSTRUCTOR, puregauge_path)
        corrupt_noncentral(projective_path, corrupted_path)

        projective_exit, projective_output = run_command(
            [sys.executable, str(VALIDATOR), str(projective_path)]
        )
        puregauge_exit, puregauge_output = run_command(
            [sys.executable, str(VALIDATOR), str(puregauge_path)]
        )
        corrupted_exit, corrupted_output = run_command(
            [sys.executable, str(VALIDATOR), str(corrupted_path)]
        )

    projective_report = parse_report(projective_output)
    puregauge_report = parse_report(puregauge_output)
    corrupted_report = parse_report(corrupted_output)
    audit_cases = cert.get("audit_cases", {})
    implemented = cert.get("implemented_checks", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_PROJECTIVE_RHOE_MESH_VALIDATOR_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies",
            "PASS"
            if projective_cert.get("verdict", {}).get(
                "projective_route_is_live_but_requires_new_selected_twist_data"
            )
            is True
            and puregauge_cert.get("verdict", {}).get(
                "finite_validator_stack_handles_noncommuting_tables"
            )
            is True
            else "FAIL",
            "projective carrier and puregauge carrier",
        ),
        Gate(
            "validator script",
            "PASS"
            if contains_all(
                validator_text,
                [
                    "product(path_2) product(path_1)^(-1) = lambda I",
                    "projective_gerbe_gluing_passes",
                    "central_twist_is_nontrivial",
                    "central_phase_histogram",
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
            "projective carrier passes",
            "PASS"
            if projective_exit == audit_cases.get("projective_magnetic_carrier", {}).get("validator_exit")
            and projective_report.get("strict_mismatch_count")
            == audit_cases.get("projective_magnetic_carrier", {}).get("strict_mismatch_count")
            and projective_report.get("projective_mismatch_count")
            == audit_cases.get("projective_magnetic_carrier", {}).get("projective_mismatch_count")
            and projective_report.get("nontrivial_central_twist_count")
            == audit_cases.get("projective_magnetic_carrier", {}).get("nontrivial_central_twist_count")
            and projective_report.get("central_twist_is_nontrivial") is True
            else "FAIL",
            str(projective_report),
        ),
        Gate(
            "strict carrier passes trivially",
            "PASS"
            if puregauge_exit == audit_cases.get("pure_gauge_nonabelian_carrier", {}).get("validator_exit")
            and puregauge_report.get("strict_mismatch_count") == 0
            and puregauge_report.get("nontrivial_central_twist_count") == 0
            and puregauge_report.get("central_twist_is_nontrivial") is False
            else "FAIL",
            str(puregauge_report),
        ),
        Gate(
            "noncentral corruption rejected",
            "PASS"
            if corrupted_exit == audit_cases.get("noncentral_corrupted_candidate", {}).get("validator_exit")
            and corrupted_report.get("projective_mismatch_count", 0)
            > audit_cases.get("noncentral_corrupted_candidate", {}).get(
                "projective_mismatch_count_above", 999
            )
            and "noncentral projective mismatch" in corrupted_output
            else "FAIL",
            f"exit={corrupted_exit}; report={corrupted_report}",
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
            if verdict.get("projective_validator_ready") is True
            and verdict.get("projective_magnetic_carrier_validated_as_twisted_not_ordinary")
            is True
            and "twisted-source promotion gate" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records validator",
            "PASS"
            if contains_all(
                paper,
                [
                    "product(path_2) product(path_1)^(-1) = lambda I",
                    "genuine projective/twisted data",
                    "invalid noncentral corner data",
                    "selected gerbe class",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa projective rho_E mesh validator audit")
    print("=============================================")
    print()
    print(f"projective_exit={projective_exit}")
    print(f"puregauge_exit={puregauge_exit}")
    print(f"corrupted_exit={corrupted_exit}")
    print(f"projective_report={projective_report}")
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
