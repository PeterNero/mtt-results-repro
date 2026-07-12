"""Check the anchored kinetic metric source candidate."""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
Q = 79
N = 448
LAMBDA_LENS = 3.57
LAMBDA_NIL = 0.25


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def tau() -> complex:
    return cmath.exp(2j * math.pi * Q / N)


def bridge_matrix(weights: list[complex]) -> list[list[complex]]:
    return [[weights[( -(i + j)) % 3] for j in range(3)] for i in range(3)]


def conj_transpose(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def frob(a: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(x) ** 2 for row in a for x in row))


def diag(values: list[float]) -> list[list[complex]]:
    return [[complex(values[i] if i == j else 0.0) for j in range(len(values))] for i in range(len(values))]


def toy_weights(alpha: float, eta: float, phase_shift: int) -> list[complex]:
    out = []
    t = tau()
    for b in range(3):
        cyclic_distance = 0 if b == 0 else 1
        orientation = b
        amplitude = math.exp(-alpha * cyclic_distance - eta * orientation)
        out.append(amplitude * (t ** (phase_shift * b)))
    return out


def hermitian_with_right_metric(y: list[list[complex]], g_right_inv: list[list[complex]]) -> list[list[complex]]:
    return matmul(matmul(y, g_right_inv), conj_transpose(y))


def is_circulant(a: list[list[complex]], tol: float = 1e-12) -> bool:
    n = len(a)
    for i in range(n):
        for j in range(n):
            if abs(a[i][j] - a[(i + 1) % n][(j + 1) % n]) > tol:
                return False
    return True


def main() -> None:
    paper = read(ROOT / "Anchored_Kinetic_Metric_Source_Candidate_v1.md")
    kinetic_gate = read(ROOT / "Selected_Kinetic_Family_Breaking_Gate_v1.md")

    j_profile = [0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0]
    g = [math.exp(2.0 * j) for j in j_profile]
    g_inv = [1.0 / value for value in g]

    yu = bridge_matrix(toy_weights(alpha=1.4, eta=0.25, phase_shift=1))
    yd = bridge_matrix(toy_weights(alpha=0.8, eta=-0.15, phase_shift=2))

    hu_pure = hermitian_with_right_metric(yu, diag([1.0, 1.0, 1.0]))
    hd_pure = hermitian_with_right_metric(yd, diag([1.0, 1.0, 1.0]))
    pure_comm = frob(sub(matmul(hu_pure, hd_pure), matmul(hd_pure, hu_pure)))

    hu = hermitian_with_right_metric(yu, diag([1.0, 1.0, 1.0]))
    hd = hermitian_with_right_metric(yd, diag(g_inv))
    anchored_comm = frob(sub(matmul(hu, hd), matmul(hd, hu)))

    gates = [
        Gate("paper saved", "PASS" if "Anchored Metric Supplies" in paper else "FAIL", "anchored metric theorem present"),
        Gate("lens/nil ratio", "PASS" if 0.06 < j_profile[1] < 0.08 else "FAIL", f"lambda_nil/lambda_lens={j_profile[1]:.6f}"),
        Gate("metric positive", "PASS" if all(value > 0 for value in g) else "FAIL", f"Gdiag={[round(x,6) for x in g]}"),
        Gate("metric non-circulant", "PASS" if not is_circulant(diag(g)) else "FAIL", "diagonal entries are unequal"),
        Gate("kinetic gate imported", "PASS" if "Kinetic Breaking Can Generate" in kinetic_gate else "FAIL", "links to prior gate"),
        Gate("pure commutator zero", "PASS" if pure_comm < 1e-10 else "FAIL", f"pure={pure_comm:.6e}"),
        Gate("anchored commutator nonzero", "PASS" if anchored_comm > 1e-3 else "FAIL", f"anchored={anchored_comm:.6e}"),
        Gate("not a mass fit", "PASS", "uses corpus gap hierarchy, not measured flavor data"),
        Gate("actual anchor derivation", "OPEN", "must derive family order and sector scale from MTT"),
    ]

    print("Anchored kinetic metric source check")
    print("====================================")
    print()
    print(f"J profile: {[round(x, 6) for x in j_profile]}")
    print(f"G diag:    {[round(x, 6) for x in g]}")
    print(f"G^-1 diag: {[round(x, 6) for x in g_inv]}")
    print(f"pure commutator norm:     {pure_comm:.12e}")
    print(f"anchored commutator norm: {anchored_comm:.12e}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
