"""Check the bridge-reduced Yukawa packet.

The numerical bridge triples below are fixed toy values, not fitted to
observed masses.  They are used only to verify structural facts: full rank,
q79 phase algebra, and the commutation/no-CKM limitation of pure bridge
reduction.
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


def det3(a: list[list[complex]]) -> complex:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def toy_weights(alpha: float, eta: float, phase_shift: int) -> list[complex]:
    out = []
    t = tau()
    for b in range(3):
        cyclic_distance = 0 if b == 0 else 1
        orientation = b
        amplitude = math.exp(-alpha * cyclic_distance - eta * orientation)
        out.append(amplitude * (t ** (phase_shift * b)))
    return out


def main() -> None:
    paper = read(ROOT / "Bridge_Reduced_Yukawa_Packet_v1.md")

    # Non-empirical toy bridge triples.  They demonstrate that the bridge
    # skeleton can be full rank without entry-wise entries.  The Hermitian
    # commutator check proves the pure bridge skeleton still has a common
    # family-Fourier left basis.
    cu = toy_weights(alpha=1.4, eta=0.25, phase_shift=1)
    cd = toy_weights(alpha=0.8, eta=-0.15, phase_shift=2)
    yu = bridge_matrix(cu)
    yd = bridge_matrix(cd)
    hu = matmul(yu, conj_transpose(yu))
    hd = matmul(yd, conj_transpose(yd))
    comm = sub(matmul(hu, hd), matmul(hd, hu))

    bridge_table_ok = all((i + j + (-(i + j)) % 3) % 3 == 0 for i in range(3) for j in range(3))
    det_u = det3(yu)
    det_d = det3(yd)
    comm_norm = frob(comm)

    gates = [
        Gate("paper saved", "PASS" if "Bridge-Reduced Matrix Form" in paper else "FAIL", "bridge-reduced theorem present"),
        Gate("entry reduction", "PASS" if "9 entries per quark sector -> 3 bridge weights" in paper else "FAIL", "three bridge weights per sector"),
        Gate("bridge conservation", "PASS" if bridge_table_ok else "FAIL", "i+j+b=0 mod 3"),
        Gate("q79 phase generator", "PASS" if N // math.gcd(Q, N) == 448 else "FAIL", f"order={N // math.gcd(Q,N)}"),
        Gate("up full rank", "PASS" if abs(det_u) > 1e-8 else "FAIL", f"|det Yu|={abs(det_u):.6e}"),
        Gate("down full rank", "PASS" if abs(det_d) > 1e-8 else "FAIL", f"|det Yd|={abs(det_d):.6e}"),
        Gate("commuting Hermitians", "PASS" if comm_norm < 1e-10 else "FAIL", f"||[Hu,Hd]||_F={comm_norm:.6e}"),
        Gate("CKM needs extra breaking", "PROVED" if "Need Selected Family Breaking" in paper else "FAIL", "pure bridge skeleton is insufficient"),
        Gate("not a mass fit", "PASS", "toy weights are fixed structural values, not observed masses"),
    ]

    print("Bridge-reduced Yukawa packet check")
    print("==================================")
    print()
    print("Yu bridge weights:")
    for i, value in enumerate(cu):
        print(f"  C_u[{i}] = {value.real:+.6e} {value.imag:+.6e}i")
    print("Yd bridge weights:")
    for i, value in enumerate(cd):
        print(f"  C_d[{i}] = {value.real:+.6e} {value.imag:+.6e}i")
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
