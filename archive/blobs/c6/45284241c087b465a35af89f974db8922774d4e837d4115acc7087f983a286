"""Independently audit the exact partial q79 u2 CRT gluing theorem."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULUS = 101
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_u1_002_partial_CRT_gluing.py"
RENDERER = ROOT / "scripts" / "render_q79_Ronly_u1_002_partial_CRT_gluing_theorem.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_Partial_CRT_Gluing_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_Partial_CRT_Gluing_v1.md")
PREFIX_AUDIT = Path(__file__).with_name("q79_Ronly_u1_002_contiguous_prefix_audit.py")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, check=False,
    )


def evaluate(poly: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % MODULUS
    return result


def source_matches(entry: dict[str, object]) -> bool:
    path = ROOT / str(entry["path"])
    return bool(
        path.is_file()
        and path.stat().st_size == entry["bytes"]
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    )


def main() -> None:
    required = [CERTIFIER, RENDERER, CERTIFICATE, THEOREM, PREFIX_AUDIT]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)
    prefix_run = run([sys.executable, str(PREFIX_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-u1-002-crt-") as directory:
        temporary = Path(directory)
        regenerated_certificate = temporary / "certificate.json"
        regenerated_theorem = temporary / "theorem.md"
        certifier_run = run([sys.executable, str(CERTIFIER), "--output", str(regenerated_certificate)])
        renderer_run = run([
            sys.executable, str(RENDERER),
            "--certificate", str(regenerated_certificate),
            "--output", str(regenerated_theorem),
        ])
        certificate_equal = (
            regenerated_certificate.is_file()
            and regenerated_certificate.read_bytes() == CERTIFICATE.read_bytes()
        )
        theorem_equal = (
            regenerated_theorem.is_file()
            and regenerated_theorem.read_bytes() == THEOREM.read_bytes()
        )
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    spaces = certificate.get("spaces", [])
    algebra_checks = []
    details = []
    for entry in spaces:
        roots = entry["closed_u2_values"]
        polynomial = entry["projector_polynomial"]["coefficients_ascending_mod_101"]
        field_roots = [value for value in range(MODULUS) if evaluate(polynomial, value) == 0]
        projectors = entry["CRT_idempotents"]
        matrix = [
            [evaluate(row["idempotent_coefficients_ascending"], value) for value in roots]
            for row in projectors
        ]
        identity = [
            [int(i == j) for j in range(len(roots))]
            for i in range(len(roots))
        ]
        summed = [0] * len(roots)
        for row in projectors:
            coefficients = row["idempotent_coefficients_ascending"]
            for index, coefficient in enumerate(coefficients):
                summed[index] = (summed[index] + coefficient) % MODULUS
        algebra_checks.append(
            roots == list(range(1, len(roots) + 1))
            and field_roots == roots
            and matrix == identity
            and summed == [1] + [0] * (len(roots) - 1)
            and all(row["derivative_denominator"] * row["derivative_denominator_inverse"] % MODULUS == 1 for row in projectors)
        )
        details.append(f"space{entry['space_index']}={len(roots)}")
    checks = certificate.get("checks", {})
    total = sum(len(entry["closed_u2_values"]) for entry in spaces)
    theorem = THEOREM.read_text(encoding="utf-8")
    full_torus_polynomial = [100, *([0] * 99), 1]
    full_torus = (
        certificate.get("status") == "EXACT_FULL_NONZERO_U2_CRT_GLUE_CERTIFIED"
        and certificate.get("coverage_status")
        == "COMPLETE_F101_NONZERO_U2_TORUS_IN_BOTH_SPACES"
        and total == 200
        and all(
            len(entry["closed_u2_values"]) == 100
            and entry["projector_polynomial"]["coefficients_ascending_mod_101"]
            == full_torus_polynomial
            for entry in spaces
        )
    )
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("contiguous-prefix source audit", "PASS" if prefix_run.returncode == 0 else "FAIL", prefix_run.stdout[-120:].strip()),
        Gate("source certificate hash", "PASS" if source_matches(certificate["source_artifact"]) else "FAIL", certificate["source_artifact"]["path"]),
        Gate("certifier reruns", "PASS" if certifier_run.returncode == 0 else "FAIL", certifier_run.stdout[-150:].strip()),
        Gate("certificate reproduces", "PASS" if certificate_equal else "FAIL", "byte-for-byte"),
        Gate("renderer reruns", "PASS" if renderer_run.returncode == 0 else "FAIL", renderer_run.stdout[-150:].strip()),
        Gate("theorem reproduces", "PASS" if theorem_equal else "FAIL", "byte-for-byte"),
        Gate("independent CRT arithmetic", "PASS" if len(spaces) == 2 and all(algebra_checks) else "FAIL", "; ".join(details)),
        Gate(
            "complete nonzero-u2 finite tori",
            "PASS" if full_torus else "FAIL",
            "P5=P6=u2^100-1; components=200",
        ),
        Gate("accounting", "PASS" if certificate["accounting"] == {"cross_space_components_glued": total, "canonical_fixed_F101_fibers_represented": 100 * total, "new_symbolic_lines_classified": 0} else "FAIL", f"components={total}"),
        Gate("all declared checks", "PASS" if checks and all(checks.values()) else "FAIL", f"{sum(bool(v) for v in checks.values())}/{len(checks)}"),
        Gate(
            "strict claim boundary",
            "PASS"
            if "No new line is classified" in theorem
            and "closes each entire selected nonzero finite `u2` torus" in theorem
            and "characteristic zero" in theorem
            and "`138/140`" in theorem
            else "FAIL",
            str(THEOREM),
        ),
        Gate("zero fit parameters", "PASS" if certificate.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]
    print("q79 u1=2 partial CRT gluing audit")
    print("====================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
