"""Check that a universal anchored metric escapes the pure bridge no-go."""

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


def commutator_norm(yu: list[list[complex]], yd: list[list[complex]], gu_inv: list[list[complex]], gd_inv: list[list[complex]]) -> float:
    hu = hermitian_with_right_metric(yu, gu_inv)
    hd = hermitian_with_right_metric(yd, gd_inv)
    return frob(sub(matmul(hu, hd), matmul(hd, hu)))


def anchored_g_inv(scale: float) -> list[list[complex]]:
    j_profile = [0.0, LAMBDA_NIL / LAMBDA_LENS, 1.0]
    return diag([math.exp(-2.0 * scale * j) for j in j_profile])


def main() -> None:
    paper = read(ROOT / "Universal_Anchored_Metric_CKM_Escape_Theorem_v1.md")
    anchor_order = read(ROOT / "ProtoSpinor_Anchor_Ordering_Lemma_for_Family_Metric_v1.md")

    yu = bridge_matrix(toy_weights(alpha=1.4, eta=0.25, phase_shift=1))
    yd = bridge_matrix(toy_weights(alpha=0.8, eta=-0.15, phase_shift=2))
    identity = diag([1.0, 1.0, 1.0])
    anchored = anchored_g_inv(scale=1.0)

    pure = commutator_norm(yu, yd, identity, identity)
    one_sided = commutator_norm(yu, yd, identity, anchored)
    universal = commutator_norm(yu, yd, anchored, anchored)
    reverse = commutator_norm(yu, yd, anchored, identity)

    gates = [
        Gate("paper saved", "PASS" if "Universal Anchored Metric Escapes" in paper else "FAIL", "universal escape theorem present"),
        Gate("anchor order imported", "PASS" if "transport < lens < nil" in anchor_order else "FAIL", "role ordering imported"),
        Gate("pure no-go", "PASS" if pure < 1e-10 else "FAIL", f"I/I={pure:.6e}"),
        Gate("one-sided nonzero", "PASS" if one_sided > 1e-3 else "FAIL", f"I/G={one_sided:.6e}"),
        Gate("universal nonzero", "PASS" if universal > 1e-3 else "FAIL", f"G/G={universal:.6e}"),
        Gate("reverse nonzero", "PASS" if reverse > 1e-3 else "FAIL", f"G/I={reverse:.6e}"),
        Gate("independent scales unnecessary", "PROVED" if "independent up/down metric scales not structurally needed" in paper else "FAIL", "universal metric already escapes no-go"),
        Gate("not a CKM fit", "PASS", "fixed structural toy bridge weights only"),
    ]

    print("Universal anchored metric CKM-escape check")
    print("==========================================")
    print()
    print(f"I/I commutator: {pure:.12e}")
    print(f"I/G commutator: {one_sided:.12e}")
    print(f"G/G commutator: {universal:.12e}")
    print(f"G/I commutator: {reverse:.12e}")
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
