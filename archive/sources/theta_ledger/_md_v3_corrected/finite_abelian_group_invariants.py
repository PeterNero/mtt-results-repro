"""Finite abelian group helpers for MTT quotient diagnostics."""

from __future__ import annotations

from math import gcd


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def exponent(factors: tuple[int, ...]) -> int:
    out = 1
    for d in factors:
        out = lcm(out, d)
    return out


def two_torsion_generators(factors: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Return nonzero elementary generators of G[2] for product Z_d."""
    gens = []
    for i, d in enumerate(factors):
        if d % 2 == 0:
            g = [0] * len(factors)
            g[i] = d // 2
            gens.append(tuple(g))
    return gens


def main() -> None:
    candidates = [
        (448,),
        (64, 7),
        (2, 2, 2, 2, 2, 2),
        (3, 2, 2, 2, 2, 2, 2),
        (3, 64),
        (4, 112),
        (2, 224),
        (68,),
        (3,),
    ]
    for factors in candidates:
        print(f"G={factors}")
        print(f"  exponent: {exponent(factors)}")
        print(f"  two-torsion generators: {two_torsion_generators(factors)}")
        print()


if __name__ == "__main__":
    main()
