"""Finite admissibility filter check for the CKM label q=79.

This script turns the remaining CKM numerator problem into a reproducible
finite selection calculation.  It does not claim to derive the continuous CKM
phase from MTT geometry.  Instead it proves the exact gate:

    if the selected MTT overlap kernel produces an oriented CKM phase inside
    the computed stability interval, the sharp finite admissibility filter on
    the selected Z_448 character uniquely selects q=79.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from math import gcd


N = 448
LEPTON = 336


@dataclass(frozen=True)
class Candidate:
    q: int
    r: int
    delta: float
    phase_error: float
    j_error: float


def order_mod(label: int, modulus: int) -> int:
    return modulus // gcd(label % modulus, modulus)


def phase(label: int, modulus: int = N) -> float:
    return 2.0 * math.pi * label / modulus


def ckm_target() -> tuple[float, float, float]:
    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    target_delta = math.asin(target_j / prefactor)
    return target_delta, target_j, prefactor


def admissible_candidates(target_delta: float, target_j: float, prefactor: float) -> list[Candidate]:
    rows: list[Candidate] = []
    for q in range(N):
        if order_mod(q, N) != N:
            continue
        r = (-(q + LEPTON)) % N
        if order_mod(r, N) != N:
            continue
        delta = phase(q)
        j = prefactor * math.sin(delta)
        rows.append(
            Candidate(
                q=q,
                r=r,
                delta=delta,
                phase_error=abs(delta - target_delta),
                j_error=abs(j - target_j),
            )
        )
    return rows


def midpoint(a: float, b: float) -> float:
    return 0.5 * (a + b)


def main() -> None:
    target_delta, target_j, prefactor = ckm_target()
    candidates = admissible_candidates(target_delta, target_j, prefactor)
    by_phase = sorted(candidates, key=lambda row: row.phase_error)

    selected = by_phase[0]
    lower_competitors = [row for row in candidates if row.delta < selected.delta]
    upper_competitors = [row for row in candidates if row.delta > selected.delta]
    lower = max(lower_competitors, key=lambda row: row.delta)
    upper = min(upper_competitors, key=lambda row: row.delta)

    lower_boundary = midpoint(lower.delta, selected.delta)
    upper_boundary = midpoint(selected.delta, upper.delta)
    stability_radius = min(target_delta - lower_boundary, upper_boundary - target_delta)

    print("Overlap admissibility filter for q=79")
    print("=====================================")
    print("modulus:", N)
    print("lepton label:", LEPTON)
    print("order(lepton):", order_mod(LEPTON, N))
    print("target_delta:", f"{target_delta:.12f}")
    print("target_J:", f"{target_j:.12e}")
    print("prefactor:", f"{prefactor:.12e}")
    print("admissible primitive labels:", len(candidates))
    print()

    print("Best labels by oriented phase distance")
    print("======================================")
    for row in by_phase[:10]:
        print(
            f"q={row.q:3d} l={LEPTON:3d} r={row.r:3d} "
            f"delta={row.delta:.12f} "
            f"phase_error={row.phase_error:.3e} "
            f"J_error={row.j_error:.3e}"
        )
    print()

    print("Voronoi stability cell for selected label")
    print("=========================================")
    print(f"selected q: {selected.q}")
    print(f"selected r: {selected.r}")
    print(f"lower nearest admissible q: {lower.q}")
    print(f"upper nearest admissible q: {upper.q}")
    print(f"lower boundary: {lower_boundary:.12f}")
    print(f"upper boundary: {upper_boundary:.12f}")
    print(f"target distance to nearest boundary: {stability_radius:.12f}")
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("finite order-448 CP character", "PASS", "used as selected quotient"),
        ("primitive q and primitive phase partner", "PASS", "defines admissible set"),
        ("sharp admissibility filter selects q=79", "PASS", "unique phase minimizer"),
        ("phase-sum closure fixes r=33", "PASS", "79+336+33=448"),
        ("MTT derives target delta", "OPEN", "requires overlap-kernel computation"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")

    assert selected.q == 79
    assert selected.r == 33
    assert order_mod(selected.q, N) == N
    assert order_mod(selected.r, N) == N
    assert (selected.q + LEPTON + selected.r) % N == 0
    assert lower_boundary < target_delta < upper_boundary
    assert stability_radius > 0.014


if __name__ == "__main__":
    main()
