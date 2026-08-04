"""Audit the matrix-level Jarlskog closure criterion."""

from __future__ import annotations

import cmath
import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "jarlskog_closure_criterion_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "z64_exact_branch_certificate.json"
NONCOMM_CERT = ROOT.parent / "certificates" / "ckm_leading_noncommutation_criterion_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


Matrix = list[list[complex]]


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def eye() -> Matrix:
    return [[1 + 0j if i == j else 0j for j in range(3)] for i in range(3)]


def diag(entries: list[float]) -> Matrix:
    return [[complex(entries[i]) if i == j else 0j for j in range(3)] for i in range(3)]


def mul(left: Matrix, right: Matrix) -> Matrix:
    return [[sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] - right[i][j] for j in range(3)] for i in range(3)]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(3)] for i in range(3)]


def comm(left: Matrix, right: Matrix) -> Matrix:
    return sub(mul(left, right), mul(right, left))


def det3(matrix: Matrix) -> complex:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def trace(matrix: Matrix) -> complex:
    return sum(matrix[i][i] for i in range(3))


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def ckm_like(s12: float, s23: float, s13: float, delta: float) -> Matrix:
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    phase = cmath.exp(1j * delta)
    phase_conj = phase.conjugate()
    return [
        [c12 * c13, s12 * c13, s13 * phase_conj],
        [
            -s12 * c23 - c12 * s23 * s13 * phase,
            c12 * c23 - s12 * s23 * s13 * phase,
            s23 * c13,
        ],
        [
            s12 * s23 - c12 * c23 * s13 * phase,
            -c12 * s23 - s12 * c23 * s13 * phase,
            c23 * c13,
        ],
    ]


def main() -> None:
    cert = load_json(CERT)
    q79_cert = load_json(Q79_CERT)
    noncomm_cert = load_json(NONCOMM_CERT)
    weight_protocol_cert = load_json(WEIGHT_PROTOCOL_CERT)
    paper = read(ROOT / "Jarlskog_Closure_Criterion_for_No_Proxy_Flavor_v1.md")

    closed = cert.get("closed", {})
    open_fields = cert.get("open", {})
    criterion = cert.get("criterion", {})

    q = q79_cert.get("conclusion", {}).get("q_mod_448")
    delta = 2.0 * math.pi * q / 448.0

    h_u = diag([1.0, 4.0, 11.0])
    v = ckm_like(0.23, 0.17, 0.11, delta)
    h_d = mul(mul(v, diag([2.0, 5.0, 13.0])), adjoint(v))
    c = comm(h_u, h_d)
    det_c = det3(c)
    trace_cube = trace(mul(mul(c, c), c))

    v_real = ckm_like(0.23, 0.17, 0.11, 0.0)
    h_d_real = mul(mul(v_real, diag([2.0, 5.0, 13.0])), adjoint(v_real))
    det_real = det3(comm(h_u, h_d_real))

    degenerate_hu = diag([1.0, 1.0, 11.0])
    det_degenerate = det3(comm(degenerate_hu, h_d))

    gates = [
        Gate(
            "certificate status",
            "CRITERION-CLOSED"
            if cert.get("status") == "JARLSKOG_CLOSURE_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "q79 CP input",
            "CLOSED" if q == 79 else "FAIL",
            "q=79 read from exact branch certificate",
        ),
        Gate(
            "noncommutation input",
            "CRITERION-CLOSED"
            if noncomm_cert.get("status") == "CKM_LEADING_NONCOMMUTATION_CRITERION_CLOSED_VALUES_OPEN"
            else "FAIL",
            str(noncomm_cert.get("status")),
        ),
        Gate(
            "no-proxy protocol input",
            "FORMULATED"
            if weight_protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(weight_protocol_cert.get("status")),
        ),
        Gate(
            "anti-Hermitian commutator",
            "PASS" if max_abs(sub(adjoint(c), [[-entry for entry in row] for row in c])) < 1e-10 else "FAIL",
            "C^dagger=-C",
        ),
        Gate(
            "determinant trace identity",
            "PASS" if abs(det_c - trace_cube / 3.0) < 1e-10 else "FAIL",
            f"det={det_c:.6g}, TrC3/3={trace_cube/3.0:.6g}",
        ),
        Gate(
            "q79 sample CP scalar",
            "PASS" if abs(det_c.imag) > 1e-8 and abs(det_c.real) < 1e-8 else "FAIL",
            f"Im det(C)={det_c.imag:.6g}",
        ),
        Gate(
            "zero phase sanity check",
            "PASS" if abs(det_real.imag) < 1e-10 else "FAIL",
            f"Im det(delta=0)={det_real.imag:.6g}",
        ),
        Gate(
            "degeneracy guard",
            "PASS"
            if abs(det_degenerate.imag) < abs(det_c.imag)
            and closed.get("nondegenerate_spectrum_requirement_identified") is True
            else "FAIL",
            "nondegenerate spectra are required before reading J_CKM",
        ),
        Gate(
            "values remain open",
            "OPEN"
            if open_fields.get("selected_Y_u") is True
            and open_fields.get("selected_Y_d") is True
            and open_fields.get("Delta_CP_value") is True
            else "FAIL",
            "criterion only; selected matrices are not computed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "No-Proxy Jarlskog Closure Criterion" in paper else "FAIL",
            "Jarlskog criterion theorem is written",
        ),
    ]

    print("Jarlskog closure criterion audit")
    print("================================")
    print()
    print(f"q={q}")
    print(f"sample_delta={delta:.15f}")
    print(f"sample_Im_det_commutator={det_c.imag:.15e}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
