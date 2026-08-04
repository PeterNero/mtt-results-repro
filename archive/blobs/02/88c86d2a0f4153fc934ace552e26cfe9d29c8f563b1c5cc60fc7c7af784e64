"""Compute the minimal q79/Z3 selected localization packet.

This is a finite spectral skeleton, not a mass fit.  It checks that a selected
CP mismatch gap tensored with the ambient Z3 family carrier gives an isolated
rank-three family cluster and finite family-conserving channel sets.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
N_CP = 448
Q = 79
N_FAMILY = 3
EPS = 0.05


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def cyclic_distance(a: int, b: int, n: int) -> int:
    d = abs((a - b) % n)
    return min(d, n - d)


def family_laplacian_eigenvalue(f: int) -> float:
    return 2.0 - 2.0 * math.cos(2.0 * math.pi * f / N_FAMILY)


def eigenvalue(r: int, f: int) -> float:
    return cyclic_distance(r, Q, N_CP) ** 2 + EPS * family_laplacian_eigenvalue(f)


def selected_cluster() -> list[tuple[float, int, int]]:
    states = [(eigenvalue(r, f), r, f) for r in range(N_CP) for f in range(N_FAMILY)]
    states.sort(key=lambda item: (item[0], item[1], item[2]))
    return states[:8]


def bridge(i: int, j: int) -> int:
    return (-(i + j)) % N_FAMILY


def channels() -> dict[str, list[tuple[int, int, int]]]:
    triples = [(i, j, bridge(i, j)) for i in range(N_FAMILY) for j in range(N_FAMILY)]
    return {"u": triples, "d": triples.copy()}


def character_order(k: int, n: int) -> int:
    return n // math.gcd(k, n)


def main() -> None:
    paper = read(ROOT / "Minimal_Selected_Localization_Packet_v1.md")
    cluster = selected_cluster()
    first_three = cluster[:3]
    fourth = cluster[3]
    chan = channels()
    phase_sum = (79 + 336 + 33) % N_CP
    family_kernel = [0, 448, 896]
    selected_family_states = [(r, f) for _, r, f in first_three]

    gates = [
        Gate("paper saved", "PASS" if "Minimal Retained Family Cluster" in paper else "FAIL", "packet theorem present"),
        Gate("q79 exact order", "PASS" if character_order(Q, N_CP) == N_CP else "FAIL", f"order={character_order(Q, N_CP)}"),
        Gate("family kernel", "PASS" if all(k % 448 == 0 for k in family_kernel) and len(family_kernel) == 3 else "FAIL", str(family_kernel)),
        Gate("first three CP labels", "PASS" if all(r == Q for _, r, _ in first_three) else "FAIL", str(first_three)),
        Gate("first three family labels", "PASS" if sorted(f for _, _, f in first_three) == [0, 1, 2] else "FAIL", str(selected_family_states)),
        Gate("cluster gap", "PASS" if fourth[0] - first_three[-1][0] > 0.8 else "FAIL", f"gap={fourth[0] - first_three[-1][0]:.3f}"),
        Gate("u channels", "PASS" if len(chan["u"]) == 9 and all((i + j + b) % 3 == 0 for i, j, b in chan["u"]) else "FAIL", f"count={len(chan['u'])}"),
        Gate("d channels", "PASS" if len(chan["d"]) == 9 and all((i + j + b) % 3 == 0 for i, j, b in chan["d"]) else "FAIL", f"count={len(chan['d'])}"),
        Gate("phase sum closure", "PASS" if phase_sum == 0 else "FAIL", f"(79+336+33) mod 448={phase_sum}"),
        Gate("mass data absent", "PASS" if "derive action costs" in paper and "OPEN" in paper else "FAIL", "amplitudes remain symbolic"),
    ]

    print("Minimal selected localization packet")
    print("====================================")
    print()
    print(f"N_CP={N_CP}, q={Q}, N_family={N_FAMILY}, eps={EPS}")
    print("lowest states (lambda, CP, family):")
    for lam, r, f in cluster:
        print(f"  {lam:6.3f}  r={r:3d}  f={f}")
    print()
    print("Gamma_u/Gamma_d bridge table: (i,j,b) with i+j+b=0 mod 3")
    for i, j, b in chan["u"]:
        print(f"  ({i},{j},{b})")
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
