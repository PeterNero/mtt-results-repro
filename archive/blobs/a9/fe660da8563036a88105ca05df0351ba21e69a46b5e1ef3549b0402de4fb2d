"""Audit the q79 space-6 u1=2,u2=14 finite-Groebner D closure."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "scripts" / "verify_q79_Ronly_symbolic_finite_groebner_exception_D_unit.py"
RENDERER = ROOT / "scripts" / "render_q79_Ronly_u1_002_space6_u2_014_finite_groebner_D_theorem.py"
DIRECTORY = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
CERTIFICATE = DIRECTORY / "space6_class1_u1_002_a_041_symbolic_t_finite_groebner.D_unit.certificate.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_Space6_U2_014_Finite_Groebner_D_Closure_v1.md")
PARENT = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines" / "space_6_h0_g0_class1_inverse_root.msolve.in"
FAMILY = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix" / "family.packet.json"
INPUT = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix" / "inputs" / "space6_u1_002_u2_014.msolve.in"
BASIS = INPUT.with_suffix(".out")
LOG = INPUT.with_suffix(".log")
PARENT5 = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines" / "space_5_h0_g0_class1_inverse_root.msolve.in"
FAMILY5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix" / "family.packet.json"
INPUT5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix" / "inputs" / "space5_u1_002_u2_004.msolve.in"
BASIS5 = INPUT5.with_suffix(".out")
LOG5 = INPUT5.with_suffix(".log")
OLD_AFFINE_CERTIFICATE = DIRECTORY / "space5_class1_u1_002_a_050_symbolic_v.D_unit.certificate.json"


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


def artifact_matches(entry: dict[str, object]) -> bool:
    path = Path(str(entry["path"]))
    if not path.is_absolute():
        path = ROOT / path
    return bool(
        path.is_file()
        and path.stat().st_size == entry["bytes"]
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    )


def main() -> None:
    required = [
        VERIFIER, RENDERER, CERTIFICATE, THEOREM, PARENT, FAMILY, INPUT, BASIS, LOG,
        PARENT5, FAMILY5, INPUT5, BASIS5, LOG5, OLD_AFFINE_CERTIFICATE,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)
    with tempfile.TemporaryDirectory(prefix="q79-space6-u2-014-D-") as directory:
        temporary = Path(directory)
        regenerated_certificate = temporary / "certificate.json"
        regenerated_theorem = temporary / "theorem.md"
        verifier_run = run([
            sys.executable, str(VERIFIER),
            "--parent", str(PARENT),
            "--family-packet", str(FAMILY),
            "--source-input", str(INPUT),
            "--basis-output", str(BASIS),
            "--basis-log", str(LOG),
            "--space", "6", "--u1", "2", "--u2", "14",
            "--scalar-class", "1", "--a", "41",
            "--output", str(regenerated_certificate),
        ])
        renderer_run = run([
            sys.executable, str(RENDERER),
            "--certificate", str(regenerated_certificate),
            "--output", str(regenerated_theorem),
        ])
        regression_certificate = temporary / "space5_u2_004_general.json"
        regression_run = run([
            sys.executable, str(VERIFIER),
            "--parent", str(PARENT5),
            "--family-packet", str(FAMILY5),
            "--source-input", str(INPUT5),
            "--basis-output", str(BASIS5),
            "--basis-log", str(LOG5),
            "--space", "5", "--u1", "2", "--u2", "4",
            "--scalar-class", "1", "--a", "50",
            "--output", str(regression_certificate),
        ])
        regression = (
            json.loads(regression_certificate.read_text(encoding="utf-8"))
            if regression_certificate.is_file()
            else {}
        )
        certificate_equal = (
            regenerated_certificate.is_file()
            and regenerated_certificate.read_bytes() == CERTIFICATE.read_bytes()
        )
        theorem_equal = (
            regenerated_theorem.is_file()
            and regenerated_theorem.read_bytes() == THEOREM.read_bytes()
        )
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    old_affine = json.loads(OLD_AFFINE_CERTIFICATE.read_text(encoding="utf-8"))
    quotient = certificate.get("quotient_algebra", {})
    witness = certificate.get("unit_witness", {})
    checks = certificate.get("checks", {})
    artifacts = certificate.get("artifacts", {})
    D_data = certificate.get("D_terminal_data", {})
    dimension = quotient.get("dimension")
    expected_basis = [
        "1", "t", "u7", "u6", "u5", "u4", "u3", "h6", "h5", "h4",
        "h3", "h2", "h1", "t^2", "u7*t", "u6*t", "u5*t", "u4*t",
        "h6*t", "h5*t",
    ]
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("verifier reruns", "PASS" if verifier_run.returncode == 0 else "FAIL", verifier_run.stdout[-180:].strip()),
        Gate("certificate reproduces", "PASS" if certificate_equal else "FAIL", "byte-for-byte"),
        Gate("renderer reruns", "PASS" if renderer_run.returncode == 0 else "FAIL", renderer_run.stdout[-160:].strip()),
        Gate("theorem reproduces", "PASS" if theorem_equal else "FAIL", "byte-for-byte"),
        Gate(
            "general-engine affine regression",
            "PASS"
            if regression_run.returncode == 0
            and regression.get("quotient_algebra", {}).get("dimension")
            == old_affine.get("quotient_algebra", {}).get("dimension") == 10
            and regression.get("unit_witness", {}).get("parent_row")
            == old_affine.get("unit_witness", {}).get("parent_row") == 18
            and regression.get("unit_witness", {}).get("D_multiplication_determinant")
            == old_affine.get("unit_witness", {}).get("D_multiplication_determinant") == 95
            and regression.get("unit_witness", {}).get("product_coefficients")
            == [1] + [0] * 9
            else "FAIL",
            "space5 u2=4: dimension=10, D18 det=95",
        ),
        Gate("all source artifacts hash-bind", "PASS" if artifacts and all(artifact_matches(entry) for entry in artifacts.values()) else "FAIL", f"artifacts={len(artifacts)}"),
        Gate("selected coordinates", "PASS" if certificate.get("space_index") == 6 and certificate.get("fixed_coordinates") == {"u1": 2, "a_equals_v_times_u3": 41, "selected_u0": 76, "selected_u2": 14} else "FAIL", str(certificate.get("fixed_coordinates"))),
        Gate("finite standard basis", "PASS" if dimension == 20 and quotient.get("standard_basis") == expected_basis else "FAIL", f"dimension={dimension}"),
        Gate("Buchberger criterion", "PASS" if quotient.get("Buchberger_pair_certificate") == {"total_pairs": 3003, "product_criterion_pairs": 2211, "explicit_zero_reductions": 792} else "FAIL", str(quotient.get("Buchberger_pair_certificate"))),
        Gate("complete multiplication table", "PASS" if quotient.get("basis_product_rows") == 210 and len(quotient.get("basis_product_table_sha256", "")) == 64 else "FAIL", str(quotient.get("basis_product_table_sha256"))),
        Gate("associativity", "PASS" if quotient.get("associativity_basis_triple_checks") == 20 ** 3 else "FAIL", str(quotient.get("associativity_basis_triple_checks"))),
        Gate("four unit y pivots", "PASS" if [row["pivot_multiplication_determinant"] for row in quotient.get("reconstructed_y_rows", {}).values()] == [95, 95, 95, 95] else "FAIL", "det=95 each"),
        Gate("all four D terminals are units", "PASS" if [D_data[str(index)]["multiplication_determinant"] for index in range(18, 22)] == [1, 1, 1, 87] else "FAIL", str({key: row.get("multiplication_determinant") for key, row in D_data.items()})),
        Gate("explicit D18 inverse", "PASS" if witness.get("parent_row") == 18 and witness.get("D_multiplication_determinant") == 1 and witness.get("product_coefficients") == [1] + [0] * 19 else "FAIL", "D18 * inverse = 1"),
        Gate("all declared checks", "PASS" if checks and all(checks.values()) else "FAIL", f"{sum(bool(value) for value in checks.values())}/{len(checks)}"),
        Gate("zero fit parameters", "PASS" if certificate.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]
    print("q79 space-6 u1=2,u2=14 finite-Groebner D audit")
    print("====================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
