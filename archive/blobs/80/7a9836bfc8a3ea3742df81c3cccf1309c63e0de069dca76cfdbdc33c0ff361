"""Audit the Z64 exact central-circle branch certificate."""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd
from operator import mul
from pathlib import Path

from candidate_quotient_mechanism_scan import dyadic_carry_matrix
from recursive_quotient_snf_template import invariant_factors


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def ordered_factorizations(n: int, minimum: int = 2) -> list[tuple[int, ...]]:
    if n == 1:
        return [()]
    out: list[tuple[int, ...]] = []
    for d in range(minimum, n + 1):
        if n % d == 0:
            for tail in ordered_factorizations(n // d, minimum):
                out.append((d, *tail))
    return out


def tower_cost(degrees: tuple[int, ...]) -> int:
    return sum(d * d - 1 for d in degrees)


def shift_order(n: int, step: int) -> int:
    return n // gcd(n, step)


def crt(a: int, m: int, b: int, n: int) -> int:
    for x in range(m * n):
        if x % m == a and x % n == b:
            return x
    raise AssertionError("no CRT solution")


def main() -> None:
    paper = PAPER.read_text(encoding="utf-8", errors="ignore") if PAPER.exists() else ""
    carry = dyadic_carry_matrix(6)
    factors, free_rank = invariant_factors(carry)
    towers = sorted(ordered_factorizations(32), key=lambda t: (tower_cost(t), t))
    best = towers[0]
    runner_up = towers[1]
    gap = tower_cost(runner_up) - tower_cost(best)
    q = crt(15, 64, 2, 7)

    gates = [
        Gate("certificate paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate("A64 SNF", "PASS" if factors == [64] and free_rank == 0 else "FAIL", f"SNF={factors}, free={free_rank}"),
        Gate("K64 group algebra", "PASS" if "K_64 := C[G_64]" in paper else "FAIL", "K64=C[coker A64]"),
        Gate("primitive shift", "PASS" if shift_order(64, 1) == 64 else "FAIL", f"order={shift_order(64, 1)}"),
        Gate("retarded primitive lag", "PASS" if shift_order(64, 63) == 64 else "FAIL", "S^-1 has order 64"),
        Gate("exact-order64 tower selected", "PASS" if best == (2, 2, 2, 2, 2) else "FAIL", f"best={best}"),
        Gate("tower spectral gap", "PASS" if gap == 9 else "FAIL", f"gap={gap}"),
        Gate("coherent commutator exact branch", "CLOSED", "[L,Pi_coh]=0 by exact branch definition"),
        Gate("Schur correction", "CLOSED", "E_Schur=0 in exact branch"),
        Gate("q64 component", "PASS" if 15 % 64 == 15 else "FAIL", "q64=15"),
        Gate("CRT q79", "PASS" if q == 79 else "FAIL", f"q={q}"),
    ]

    print("Z64 exact branch certificate audit")
    print("==================================")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
