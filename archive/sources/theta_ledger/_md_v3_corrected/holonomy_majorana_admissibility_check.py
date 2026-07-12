"""Finite-character checks for the holonomy/Majorana admissibility note."""

from math import gcd


def order_mod(n: int, k: int) -> int:
    """Order of k in Z_n as an additive character weight."""
    return n // gcd(n, k % n)


def majorana_allowed(n: int, k: int) -> bool:
    """A flat line character is self-conjugate iff 2k = 0 mod n."""
    return (2 * k) % n == 0


def main() -> None:
    n = 448
    weights = [79, -112, 33]

    print(f"N = {n}")
    print(f"phase-sum mod N = {sum(weights) % n}")
    print()

    for k in weights:
        kk = k % n
        print(
            f"k = {k:>4} (mod {n}: {kk:>3}), "
            f"order = {order_mod(n, k):>3}, "
            f"Majorana self-character = {majorana_allowed(n, k)}"
        )

    allowed = [k for k in range(n) if majorana_allowed(n, k)]
    print()
    print(f"Majorana-admissible weights in Z_{n}: {allowed}")
    print()
    print("Bare Lens L(3,1) torsion character group: Z_3")
    print("Therefore Z_448 is not selected by the bare lens torsion alone.")


if __name__ == "__main__":
    main()

