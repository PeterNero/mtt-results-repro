"""Majorana/two-torsion check for the ambient Z_1344 flavor carrier."""

from __future__ import annotations

from math import gcd


def order_mod(n: int, k: int) -> int:
    return n // gcd(n, k % n)


def majorana_allowed(n: int, k: int) -> bool:
    return (2 * k) % n == 0


def main() -> None:
    n = 1344
    labels = {
        "CKM CP k_q": 237,
        "PMNS quarter-turn k_l": 1008,
        "phase-sum partner k_31": 99,
        "trivial neutral": 0,
        "ambient two-torsion": n // 2,
    }

    print(f"Ambient carrier N = {n}")
    print(f"family factor condition: k = 0 mod 3")
    print()
    for name, k in labels.items():
        print(
            f"{name:26s} k={k:4d} "
            f"order={order_mod(n, k):4d} "
            f"family_trivial={k % 3 == 0!s:5s} "
            f"Majorana_allowed={majorana_allowed(n, k)}"
        )

    cp = [labels["CKM CP k_q"], labels["PMNS quarter-turn k_l"], labels["phase-sum partner k_31"]]
    print()
    print(f"phase-sum closure: {sum(cp) % n}")
    print(f"all CP labels family-trivial: {all(k % 3 == 0 for k in cp)}")
    print(f"CP labels Majorana-allowed: {[majorana_allowed(n, k) for k in cp]}")
    print()
    print("Majorana-admissible flat line weights in Z_1344:")
    print([k for k in range(n) if majorana_allowed(n, k)])


if __name__ == "__main__":
    main()
