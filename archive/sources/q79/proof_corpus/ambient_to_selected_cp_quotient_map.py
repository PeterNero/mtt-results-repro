"""Check the quotient map from ambient Z_1344 to selected CP Z_448.

The ambient carrier is interpreted as

    Z_64 x Z_7 x Z_3 ~= Z_1344.

The family factor is the kernel of the quotient map

    pi: Z_1344 -> Z_448,   pi(x) = x mod 448.

Family-trivial ambient characters are precisely labels k divisible by 3.
Such a label k=3r is the pullback of the Z_448 character labelled r.
"""

from __future__ import annotations

from math import gcd


def order_mod(n: int, k: int) -> int:
    return n // gcd(n, k % n)


def character_value_num(n: int, k: int, x: int) -> int:
    """Return the numerator of k*x/n modulo 1, represented modulo n."""
    return (k * x) % n


def main() -> None:
    ambient_n = 1344
    cp_n = 448
    kernel = [0, 448, 896]
    labels = {
        "CKM CP": 237,
        "PMNS quarter-turn": 1008,
        "phase-sum partner": 99,
    }

    print("Ambient-to-selected quotient")
    print("============================")
    print(f"ambient: Z_{ambient_n}")
    print(f"selected CP quotient: Z_{cp_n}")
    print("pi(x) = x mod 448")
    print(f"kernel(pi) = {kernel}")
    print()

    print("Pullback labels")
    print("===============")
    for name, k in labels.items():
        r = k // 3
        pullback_ok = k % 3 == 0
        same_order = order_mod(ambient_n, k) == order_mod(cp_n, r)
        kernel_trivial = all(character_value_num(ambient_n, k, x) == 0 for x in kernel)
        print(
            f"{name:18s} ambient k={k:4d} -> CP r={r:3d} "
            f"order={order_mod(ambient_n, k):3d} "
            f"pullback={pullback_ok} same_order={same_order} "
            f"kernel_trivial={kernel_trivial}"
        )
    print()

    cp_sum = sum(k // 3 for k in labels.values()) % cp_n
    ambient_sum = sum(labels.values()) % ambient_n
    print("Closure")
    print("=======")
    print(f"ambient label sum mod {ambient_n}: {ambient_sum}")
    print(f"selected CP label sum mod {cp_n}: {cp_sum}")
    print()

    print("Criterion")
    print("=========")
    print("ambient character k descends to Z_448 iff k = 0 mod 3")


if __name__ == "__main__":
    main()
