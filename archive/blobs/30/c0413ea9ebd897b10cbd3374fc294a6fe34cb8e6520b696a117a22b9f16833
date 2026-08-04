"""Check the selected kinetic family-breaking gate.

The metrics below are fixed toy positive metrics.  They are not fitted to CKM
data.  They only demonstrate the theorem-schema point: once the bridge packet
is canonically normalized by non-circulant selected metrics, the common
family-Fourier left basis can be broken.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
Q = 79
N = 448


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


def main() -> None:
    paper = read(ROOT / "Selected_Kinetic_Family_Breaking_Gate_v1.md")
    bridge_paper = read(ROOT / "Bridge_Reduced_Yukawa_Packet_v1.md")

    yu = bridge_matrix(toy_weights(alpha=1.4, eta=0.25, phase_shift=1))
    yd = bridge_matrix(toy_weights(alpha=0.8, eta=-0.15, phase_shift=2))

    identity = diag([1.0, 1.0, 1.0])
    g_u_inv = identity
    # A fixed positive, non-circulant toy right-sector metric inverse.
    g_d_inv = diag([1.0, 1.0 / 1.1, 1.0 / 1.3])

    hu_pure = hermitian_with_right_metric(yu, identity)
    hd_pure = hermitian_with_right_metric(yd, identity)
    pure_comm = frob(sub(matmul(hu_pure, hd_pure), matmul(hd_pure, hu_pure)))

    hu = hermitian_with_right_metric(yu, g_u_inv)
    hd = hermitian_with_right_metric(yd, g_d_inv)
    broken_comm = frob(sub(matmul(hu, hd), matmul(hd, hu)))

    gates = [
        Gate("paper saved", "PASS" if "Kinetic Breaking Can Generate" in paper else "FAIL", "kinetic gate theorem present"),
        Gate("bridge no-go imported", "PASS" if "pure bridge Hermitian forms commute" in bridge_paper else "FAIL", "pure bridge limitation imported"),
        Gate("pure commutator zero", "PASS" if pure_comm < 1e-10 else "FAIL", f"pure ||[Hu,Hd]||_F={pure_comm:.6e}"),
        Gate("positive metric", "PASS" if all(x > 0 for x in [1.0, 1.1, 1.3]) else "FAIL", "toy G_d diagonal entries positive"),
        Gate("broken commutator nonzero", "PASS" if broken_comm > 1e-4 else "FAIL", f"broken ||[Hu,Hd]||_F={broken_comm:.6e}"),
        Gate("not a CKM fit", "PASS", "metrics are structural toy values only"),
        Gate("actual metric source", "OPEN", "must derive non-circulant metrics from Sigma_MTT"),
    ]

    print("Selected kinetic family-breaking check")
    print("======================================")
    print()
    print(f"pure commutator norm:   {pure_comm:.12e}")
    print(f"broken commutator norm: {broken_comm:.12e}")
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
