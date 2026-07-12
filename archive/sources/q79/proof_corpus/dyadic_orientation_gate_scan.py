"""Dyadic orientation gate scan for the CKM component.

The finite arithmetic has two adjacent primitive labels around the dyadic
quarter-turn l64=16:

    pre-quarter  q64=15
    post-quarter q64=17

This script combines each with the Mukai component q7=2 and checks the resulting
Z_448 labels and phase-sum partners.
"""

from __future__ import annotations

import math
from math import gcd


def crt_pair(a64: int, a7: int) -> int:
    for x in range(448):
        if x % 64 == a64 % 64 and x % 7 == a7 % 7:
            return x
    raise ValueError("no CRT solution")


def order_mod(label: int, modulus: int) -> int:
    return modulus // gcd(label % modulus, modulus)


def signed_phase(label: int, modulus: int = 448) -> float:
    angle = 2.0 * math.pi * label / modulus
    if angle > math.pi:
        angle -= 2.0 * math.pi
    return angle


def main() -> None:
    l64, l7 = 16, 0
    q7 = 2
    r7 = (-q7 - l7) % 7
    l = crt_pair(l64, l7)

    cases = [
        ("retarded/pre-quarter", 15),
        ("advanced/post-quarter", 17),
    ]

    print("Dyadic orientation gate scan")
    print("============================")
    print("quarter-turn dyadic label:", l64)
    print("Mukai q7 component:", q7)
    print("lepton full label:", l)
    print()

    for name, q64 in cases:
        r64 = (-(q64 + l64)) % 64
        q = crt_pair(q64, q7)
        r = crt_pair(r64, r7)
        print(name)
        print("-" * len(name))
        print(f"q64={q64}, q7={q7} -> q={q}")
        print(f"r64={r64}, r7={r7} -> r={r}")
        print("closure mod 448:", (q + l + r) % 448)
        print("order(q):", order_mod(q, 448))
        print("signed full phase:", f"{signed_phase(q):.12f}")
        print()

    print("Gate status")
    print("===========")
    gates = [
        ("pre-quarter orientation selects q=79", "PASS", "q64=15, q7=2"),
        ("post-quarter orientation selects q=401", "PASS", "q64=17, q7=2"),
        ("unoriented nearest-cell rule is ambiguous", "PASS", "{15,17}"),
        ("MTT derives retarded/pre-quarter sign", "OPEN", "needs overlap calculation"),
    ]
    width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{width}s}  {status:{status_width}s}  {note}")

    assert crt_pair(15, 2) == 79
    assert crt_pair(17, 2) == 401
    assert l == 336


if __name__ == "__main__":
    main()
