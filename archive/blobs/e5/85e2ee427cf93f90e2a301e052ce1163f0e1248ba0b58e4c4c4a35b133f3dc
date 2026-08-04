"""Audit the q79 space-5 u1=2,u2=23 finite-Groebner D closure."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = (
    ROOT / "scripts" / "verify_q79_Ronly_symbolic_finite_groebner_exception_D_unit.py"
)
RENDERER = (
    ROOT
    / "scripts"
    / "render_q79_Ronly_u1_002_space5_u2_023_finite_groebner_D_theorem.py"
)
DIRECTORY = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
CERTIFICATE = (
    DIRECTORY
    / "space5_class1_u1_002_a_027_symbolic_t_finite_groebner.D_unit.certificate.json"
)
THEOREM = Path(__file__).with_name(
    "Q79_Ronly_U1_002_Space5_U2_023_Finite_Groebner_D_Closure_v1.md"
)
EXECUTION_AUDIT = Path(__file__).with_name(
    "q79_Ronly_u1_002_u2_023_execution_audit.py"
)
PARENT = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_classfree_representative_lines"
    / "space_5_h0_g0_class1_inverse_root.msolve.in"
)
FAMILY = (
    ROOT
    / "candidate_data"
    / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
    / "family.packet.json"
)
INPUT = FAMILY.parent / "inputs" / "space5_u1_002_u2_023.msolve.in"
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
        VERIFIER,
        RENDERER,
        CERTIFICATE,
        THEOREM,
        EXECUTION_AUDIT,
        PARENT,
        FAMILY,
        INPUT,
        BASIS,
        LOG,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    execution = run([sys.executable, str(EXECUTION_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-space5-u2-023-D-") as directory:
        temporary = Path(directory)
        regenerated_certificate = temporary / "certificate.json"
        regenerated_theorem = temporary / "theorem.md"
        certificate_run = run(
            [
                sys.executable,
                str(VERIFIER),
                "--parent",
                str(PARENT),
                "--family-packet",
                str(FAMILY),
                "--source-input",
                str(INPUT),
                "--basis-output",
                str(BASIS),
                "--basis-log",
                str(LOG),
                "--space",
                "5",
                "--u1",
                "2",
                "--u2",
                "23",
                "--scalar-class",
                "1",
                "--a",
                "27",
                "--output",
                str(regenerated_certificate),
            ]
        )
        renderer_run = run(
            [
                sys.executable,
                str(RENDERER),
                "--certificate",
                str(regenerated_certificate),
                "--output",
                str(regenerated_theorem),
            ]
        )
        certificate_equal = (
            regenerated_certificate.is_file()
            and json.loads(regenerated_certificate.read_text(encoding="utf-8"))
            == json.loads(CERTIFICATE.read_text(encoding="utf-8"))
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
    dimension = int(quotient.get("dimension", 0))
    basis_rows = int(quotient.get("reduced_basis_rows", 0))
    buchberger = quotient.get("Buchberger_pair_certificate", {})
    y_rows = quotient.get("reconstructed_y_rows", {})
    D_determinants = [
        int(D_data.get(str(index), {}).get("multiplication_determinant", 0)) % 101
        for index in range(18, 22)
    ]
    parent_row = int(witness.get("parent_row", 0))
    product = witness.get("product_coefficients", [])
    expected_standard_basis = [
        "1",
        "t",
        "u7",
        "u6",
        "u5",
        "u4",
        "u3",
        "h6",
        "h5",
        "h4",
        "h3",
        "h2",
        "h1",
        "t^2",
        "u7*t",
        "u6*t",
        "u5*t",
        "u4*t",
        "h6*t",
        "h5*t",
    ]
    gates = [
        Gate(
            "durable execution audit",
            execution.returncode == 0,
            execution.stdout[-140:].strip(),
        ),
        Gate(
            "finite-algebra certifier reruns",
            certificate_run.returncode == 0,
            certificate_run.stdout[-180:].strip(),
        ),
        Gate("certificate reproduces", certificate_equal, "JSON-semantic equality"),
        Gate(
            "theorem renderer reruns",
            renderer_run.returncode == 0,
            renderer_run.stdout[-160:].strip(),
        ),
        Gate("theorem reproduces", theorem_equal, "byte-for-byte"),
        Gate(
            "all source artifacts hash-bind",
            bool(artifacts)
            and all(artifact_matches(entry) for entry in artifacts.values()),
            f"artifacts={len(artifacts)}",
        ),
        Gate(
            "selected coordinates",
            certificate.get("space_index") == 5
            and certificate.get("scalar_square_class_representative") == 1
            and coordinates
            == {
                "u1": 2,
                "a_equals_v_times_u3": 27,
                "selected_u0": 76,
                "selected_u2": 23,
            },
            str(coordinates),
        ),
        Gate(
            "finite standard basis",
            dimension == 20
            and basis_rows == 78
            and quotient.get("standard_basis") == expected_standard_basis,
            f"rows={basis_rows}; dimension={dimension}",
        ),
        Gate(
            "Buchberger criterion",
            buchberger
            == {
                "total_pairs": 3003,
                "product_criterion_pairs": 2211,
                "explicit_zero_reductions": 792,
            },
            str(buchberger),
        ),
        Gate(
            "complete multiplication table",
            quotient.get("basis_product_rows") == 210
            and quotient.get("basis_product_table_sha256")
            == "91f39c75931ac62f856618e06e1b21b4f85912f6971b8ee81b2b52068178da5e",
            str(quotient.get("basis_product_table_sha256")),
        ),
        Gate(
            "associativity",
            quotient.get("associativity_basis_triple_checks") == 8000,
            str(quotient.get("associativity_basis_triple_checks")),
        ),
        Gate(
            "four unit y pivots",
            set(y_rows) == {"y1", "y2", "y3", "y4"}
            and [
                y_rows[name].get("pivot_multiplication_determinant")
                for name in ("y1", "y2", "y3", "y4")
            ]
            == [95, 95, 95, 95],
            str(
                {
                    key: value.get("pivot_multiplication_determinant")
                    for key, value in y_rows.items()
                }
            ),
        ),
        Gate(
            "selected D unit exists",
            set(D_data) == {"18", "19", "20", "21"}
            and D_determinants == [1, 95, 87, 95],
            str(D_determinants),
        ),
        Gate(
            "explicit D inverse",
            parent_row == 18
            and witness.get("D_multiplication_determinant") == 1
            and D_data.get("18", {}).get("multiplication_determinant") == 1
            and len(witness.get("D_inverse_coefficients", [])) == dimension
            and product == [1] + [0] * (dimension - 1),
            f"D{parent_row}; det={witness.get('D_multiplication_determinant')}",
        ),
        Gate(
            "all certificate checks",
            bool(checks) and all(checks.values()),
            f"{sum(bool(value) for value in checks.values())}/{len(checks)}",
        ),
        Gate(
            "zero fit parameters",
            certificate.get("new_continuous_fit_parameters") == 0,
            "zero",
        ),
        Gate(
            "claim boundary retained",
            "(class,a)=(1,27)" in THEOREM.read_text(encoding="utf-8")
            and "does not classify another line" in THEOREM.read_text(encoding="utf-8"),
            str(THEOREM),
        ),
    ]
    print("q79 space-5 u1=2,u2=23 finite-Groebner D audit")
    print("====================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {'PASS' if gate.passed else 'FAIL':4s}  {gate.detail}")
    if not all(gate.passed for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
