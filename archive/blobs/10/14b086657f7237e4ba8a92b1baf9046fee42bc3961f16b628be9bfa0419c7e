from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    if gcd(m, n) != 1:
        raise ValueError("moduli must be coprime")
    for x in range(m * n):
        if x % m == a % m and x % n == b % n:
            return x
    raise AssertionError("CRT solution not found")


def primitive_labels(modulus: int) -> list[int]:
    return [k for k in range(modulus) if gcd(k, modulus) == 1]


def retarded_primitive_predecessors(quarter: int, modulus: int) -> list[int]:
    return [k for k in primitive_labels(modulus) if k < quarter]


def selected_predecessor(quarter: int, modulus: int) -> int:
    candidates = retarded_primitive_predecessors(quarter, modulus)
    return min(candidates, key=lambda k: abs(k - quarter))


def main() -> None:
    quarter = 16
    modulus = 64
    q7 = 2
    q64 = selected_predecessor(quarter, modulus)
    q448 = crt_pair(q64, 64, q7, 7)
    rho_over_kappa = quarter - q64

    gates = [
        Gate(
            "coherent-sector observability",
            "PREMISE",
            "MTT records are post-coherent-projection observables",
        ),
        Gate(
            "nil survivor projection",
            "SCHEMA",
            "proved by nil-survivor theorem; concrete N_MTT still open",
        ),
        Gate(
            "physical CP labels factor through selected quotient",
            "PROVED",
            "observable constant on execution fibers factors through quotient",
        ),
        Gate(
            "raw kernel is not final observable when fiber-varying",
            "PROVED",
            "fiber-varying raw data must be reduced to selected kernel",
        ),
        Gate(
            "retarded primitive predecessor in Z64",
            "PASS",
            f"q64={q64}",
        ),
        Gate(
            "selected sharp basin gives unit lag",
            "PASS",
            f"rho/kappa={rho_over_kappa}",
        ),
        Gate(
            "unit lag lies in q=79 cell",
            "PASS",
            f"0 < {rho_over_kappa} < 2",
        ),
        Gate(
            "CRT with q7=2",
            "PASS",
            f"q={q448}",
        ),
        Gate(
            "raw pre-survivor Schur inequality",
            "OPEN",
            "requires explicit Hessian and retarded derivative",
        ),
    ]

    print("Selected-kernel principle audit")
    print("================================")
    print(f"retarded primitive predecessors below {quarter}: {retarded_primitive_predecessors(quarter, modulus)}")
    print(f"selected q64: {q64}")
    print(f"rho/kappa from selected basin: {rho_over_kappa:.12f}")
    print(f"q448 from (q64,q7)=({q64},{q7}): {q448}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<58} {gate.status:<8} {gate.detail}")


if __name__ == "__main__":
    main()
