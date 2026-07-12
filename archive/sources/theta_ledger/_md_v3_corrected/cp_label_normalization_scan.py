"""CP label normalization scan for the selected Z448 character.

Once theta_CP has order 448, the finite topology fixes the denominator but not
automatically the CKM numerator 79.  A cyclic group has automorphisms, and many
primitive labels have order 448.

This script separates:

1. exact finite/topological constraints:
   - q has order 448;
   - lepton label l=336 gives -pi/2;
   - q+l+r=0;
   - r also has order 448;
2. numerical/overlap selection:
   - q=79 is the best label for the CKM/Jarlskog benchmark on the chosen branch.
"""

from __future__ import annotations

import math
from math import gcd


def order_mod(label: int, modulus: int) -> int:
    return modulus // gcd(label % modulus, modulus)


def phase(label: int, modulus: int) -> float:
    return 2.0 * math.pi * label / modulus


def main() -> None:
    n = 448
    lepton = 336

    s12_q, s23_q, s13_q = 0.2250, 0.0411, 0.0036
    c12_q = math.sqrt(1.0 - s12_q * s12_q)
    c23_q = math.sqrt(1.0 - s23_q * s23_q)
    c13_q = math.sqrt(1.0 - s13_q * s13_q)
    target_j = 2.9e-5
    prefactor = c12_q * c23_q * c13_q**2 * s12_q * s23_q * s13_q
    target_delta = math.asin(target_j / prefactor)

    candidates = []
    for q in range(n):
        if order_mod(q, n) != n:
            continue
        r = (-(q + lepton)) % n
        if order_mod(r, n) != n:
            continue
        delta = phase(q, n)
        j = prefactor * math.sin(delta)
        candidates.append(
            {
                "q": q,
                "l": lepton,
                "r": r,
                "delta": delta,
                "phase_error": abs(delta - target_delta),
                "j_error": abs(j - target_j),
            }
        )

    best_by_phase = sorted(candidates, key=lambda row: row["phase_error"])
    best_by_j = sorted(candidates, key=lambda row: row["j_error"])

    print("CP label normalization scan")
    print("===========================")
    print("modulus:", n)
    print("lepton quarter-turn label:", lepton)
    print("order(lepton):", order_mod(lepton, n))
    print("target_delta:", f"{target_delta:.12f}")
    print("number of primitive q with primitive phase-sum partner:", len(candidates))
    print()

    print("Best labels by phase error")
    print("==========================")
    for row in best_by_phase[:12]:
        print(
            f"q={row['q']:3d} l={row['l']:3d} r={row['r']:3d} "
            f"delta={row['delta']:.12f} "
            f"phase_error={row['phase_error']:.3e} "
            f"J_error={row['j_error']:.3e}"
        )
    print()

    print("Best labels by Jarlskog error")
    print("=============================")
    for row in best_by_j[:12]:
        print(
            f"q={row['q']:3d} l={row['l']:3d} r={row['r']:3d} "
            f"delta={row['delta']:.12f} "
            f"phase_error={row['phase_error']:.3e} "
            f"J_error={row['j_error']:.3e}"
        )
    print()

    selected = best_by_phase[0]
    assert selected["q"] == 79
    assert selected["r"] == 33
    assert selected["l"] == 336
    assert (selected["q"] + selected["l"] + selected["r"]) % n == 0
    assert order_mod(selected["q"], n) == 448
    assert order_mod(selected["r"], n) == 448
    assert order_mod(selected["l"], n) == 4

    print("Gate status")
    print("===========")
    gates = [
        (
            "finite group supplies denominator 448",
            "PASS",
            "theta_CP has order 448",
        ),
        (
            "lepton quarter-turn fixes label 336 in chosen orientation",
            "PASS",
            "order 4 and -pi/2",
        ),
        (
            "phase-sum partner is determined once q is chosen",
            "PASS",
            "r=-(q+336)",
        ),
        (
            "finite topology uniquely fixes q=79",
            "FAIL",
            "many primitive q remain",
        ),
        (
            "CKM/Jarlskog benchmark selects q=79",
            "NUMERICAL PASS",
            "best phase branch",
        ),
        (
            "MTT derives q=79 from overlap/selection dynamics",
            "OPEN",
            "next proof gate",
        ),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")


if __name__ == "__main__":
    main()
