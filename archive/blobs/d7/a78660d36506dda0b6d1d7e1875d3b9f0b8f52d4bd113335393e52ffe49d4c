"""Audit the q79 space-6 u1=2,u2=21 finite-Groebner D closure."""

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
RENDERER = ROOT / "scripts" / "render_q79_Ronly_u1_002_space6_u2_021_finite_groebner_D_theorem.py"
DIRECTORY = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
CERTIFICATE = DIRECTORY / "space6_class1_u1_002_a_028_symbolic_t_finite_groebner.D_unit.certificate.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_Space6_U2_021_Finite_Groebner_D_Closure_v1.md")
EXECUTION_AUDIT = Path(__file__).with_name("q79_Ronly_u1_002_u2_021_execution_audit.py")
PARENT = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines" / "space_6_h0_g0_class1_inverse_root.msolve.in"
FAMILY = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix" / "family.packet.json"
INPUT = FAMILY.parent / "inputs" / "space6_u1_002_u2_021.msolve.in"
BASIS = INPUT.with_suffix(".out")
LOG = INPUT.with_suffix(".log")


@dataclass(frozen=True)
class Gate:
    label: str
    passed: bool
    detail: str


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def artifact_matches(entry: dict[str, object]) -> bool:
    path = Path(str(entry["path"]).replace("/", "\\"))
    path = path if path.is_absolute() else ROOT / path
    return bool(
        path.is_file()
        and path.stat().st_size == entry["bytes"]
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    )


def main() -> None:
    required = [
        VERIFIER, RENDERER, CERTIFICATE, THEOREM, EXECUTION_AUDIT,
        PARENT, FAMILY, INPUT, BASIS, LOG,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    execution = run([sys.executable, str(EXECUTION_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-space6-u2-021-D-") as directory:
        temporary = Path(directory)
        regenerated_certificate = temporary / "certificate.json"
        regenerated_theorem = temporary / "theorem.md"
        certificate_run = run([
            sys.executable, str(VERIFIER),
            "--parent", str(PARENT),
            "--family-packet", str(FAMILY),
            "--source-input", str(INPUT),
            "--basis-output", str(BASIS),
            "--basis-log", str(LOG),
            "--space", "6", "--u1", "2", "--u2", "21",
            "--scalar-class", "1", "--a", "28",
            "--output", str(regenerated_certificate),
        ])
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
    quotient = certificate.get("quotient_algebra", {})
    witness = certificate.get("unit_witness", {})
    checks = certificate.get("checks", {})
    artifacts = certificate.get("artifacts", {})
    D_data = certificate.get("D_terminal_data", {})
    coordinates = certificate.get("fixed_coordinates", {})
    gates = [
        Gate("durable execution audit", execution.returncode == 0, execution.stdout[-140:].strip()),
        Gate("finite-algebra certifier reruns", certificate_run.returncode == 0, certificate_run.stdout[-180:].strip()),
        Gate("certificate reproduces", certificate_equal, "byte-for-byte"),
        Gate("theorem renderer reruns", renderer_run.returncode == 0, renderer_run.stdout[-160:].strip()),
        Gate("theorem reproduces", theorem_equal, "byte-for-byte"),
        Gate("all source artifacts hash-bind", bool(artifacts) and all(artifact_matches(entry) for entry in artifacts.values()), f"artifacts={len(artifacts)}"),
        Gate("selected coordinates", certificate.get("space_index") == 6 and certificate.get("scalar_square_class_representative") == 1 and coordinates == {"u1": 2, "a_equals_v_times_u3": 28, "selected_u0": 76, "selected_u2": 21}, str(coordinates)),
        Gate("finite standard basis", quotient.get("dimension") == 10 and quotient.get("reduced_basis_rows") == 48 and quotient.get("standard_basis") == ["1", "t", "u7", "u6", "u5", "u4", "u3", "h6", "h5", "h4"], f"dimension={quotient.get('dimension')}"),
        Gate("Buchberger criterion", quotient.get("Buchberger_pair_certificate") == {"total_pairs": 1128, "product_criterion_pairs": 804, "explicit_zero_reductions": 324}, str(quotient.get("Buchberger_pair_certificate"))),
        Gate("complete multiplication table", quotient.get("basis_product_rows") == 55 and len(quotient.get("basis_product_table_sha256", "")) == 64, str(quotient.get("basis_product_table_sha256"))),
        Gate("associativity", quotient.get("associativity_basis_triple_checks") == 1000, str(quotient.get("associativity_basis_triple_checks"))),
        Gate("four unit y pivots", [row["pivot_multiplication_determinant"] for row in quotient.get("reconstructed_y_rows", {}).values()] == [14, 14, 14, 14], "det=14 each"),
        Gate("all selected D rows are units", [D_data[str(index)]["multiplication_determinant"] for index in range(18, 22)] == [84, 14, 6, 17], str({key: value.get("multiplication_determinant") for key, value in D_data.items()})),
        Gate("explicit D18 inverse", witness.get("parent_row") == 18 and witness.get("D_multiplication_determinant") == 84 and witness.get("product_coefficients") == [1] + [0] * 9, "D18 * inverse = 1"),
        Gate("all certificate checks", bool(checks) and all(checks.values()), f"{sum(bool(value) for value in checks.values())}/{len(checks)}"),
        Gate("zero fit parameters", certificate.get("new_continuous_fit_parameters") == 0, "zero"),
        Gate("claim boundary retained", "`138/140`" in THEOREM.read_text(encoding="utf-8"), str(THEOREM)),
    ]
    print("q79 space-6 u1=2,u2=21 finite-Groebner D audit")
    print("====================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {'PASS' if gate.passed else 'FAIL':4s}  {gate.detail}")
    if not all(gate.passed for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
