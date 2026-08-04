"""Finite check for the dyadic pre-quarter selection rule.

If the lepton branch is the exact quarter-turn l64=16 in Z_64 and the CKM
dyadic component is the nearest primitive label strictly below it, then q64=15.
This script verifies the arithmetic and phase-sum partner.
"""

from __future__ import annotations

from math import gcd


N = 64
LEPTON = 16


def order_mod(label: int, modulus: int) -> int:
    return modulus // gcd(label % modulus, modulus)


def main() -> None:
    candidates = []
    for q in range(1, LEPTON):
        r = (-(q + LEPTON)) % N
        if order_mod(q, N) == N and order_mod(r, N) == N:
            candidates.append((q, r, LEPTON - q))

    selected_q, selected_r, distance_to_quarter = min(candidates, key=lambda row: row[2])

    print("Dyadic pre-quarter selection check")
    print("==================================")
    print("modulus:", N)
    print("lepton quarter-turn:", LEPTON)
    print("primitive pre-quarter candidates:", [q for q, _, _ in candidates])
    print("selected q64:", selected_q)
    print("selected r64:", selected_r)
    print("distance to quarter-turn:", distance_to_quarter)
    print("closure mod 64:", (selected_q + LEPTON + selected_r) % N)
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("lepton dyadic quarter-turn is 16", "PASS", "64/4"),
        ("nearest primitive pre-quarter label", "PASS", "q64=15"),
        ("phase-sum partner primitive", "PASS", "r64=33"),
        ("component closure", "PASS", "15+16+33=64"),
        ("MTT derives pre-quarter orientation", "OPEN", "physical proof needed"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")

    assert selected_q == 15
    assert selected_r == 33
    assert (selected_q + LEPTON + selected_r) % N == 0
    assert order_mod(selected_q, N) == N
    assert order_mod(selected_r, N) == N


if __name__ == "__main__":
    main()
