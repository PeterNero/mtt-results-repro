from __future__ import annotations

from dataclasses import dataclass
from math import exp, gcd


Matrix = list[list[int]]


@dataclass(frozen=True)
class Gate:
    name: str
    status: str
    detail: str


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def identity(n: int) -> Matrix:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matpow(a: Matrix, power: int) -> Matrix:
    out = identity(len(a))
    for _ in range(power):
        out = matmul(out, a)
    return out


def is_zero(a: Matrix) -> bool:
    return all(x == 0 for row in a for x in row)


def primitive_labels(modulus: int) -> list[int]:
    return [k for k in range(modulus) if gcd(k, modulus) == 1]


def retarded_predecessors(quarter: int, modulus: int) -> list[int]:
    return [k for k in primitive_labels(modulus) if k < quarter]


def selected_survivor(quarter: int, candidates: list[int]) -> int:
    return min(candidates, key=lambda k: (k - quarter) ** 2)


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    for x in range(m * n):
        if x % m == a % m and x % n == b % n:
            return x
    raise AssertionError("CRT solution not found")


def sharp_filter_weights(quarter: int, candidates: list[int], epsilon: float) -> dict[int, float]:
    raw = {k: exp(-((k - quarter) ** 2) / (epsilon * epsilon)) for k in candidates}
    total = sum(raw.values())
    return {k: v / total for k, v in raw.items()}


def main() -> None:
    # A depth-three nilpotent shift, modeling finite nil termination.
    n_shift: Matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]
    n2 = matpow(n_shift, 2)
    n3 = matpow(n_shift, 3)

    quarter = 16
    modulus = 64
    candidates = retarded_predecessors(quarter, modulus)
    q64 = selected_survivor(quarter, candidates)
    q448 = crt_pair(q64, 64, 2, 7)
    weights_1 = sharp_filter_weights(quarter, candidates, epsilon=1.0)
    weights_025 = sharp_filter_weights(quarter, candidates, epsilon=0.25)

    gates = [
        Gate("nilpotent depth-three model", "PASS" if not is_zero(n2) and is_zero(n3) else "FAIL", "N^2 nonzero and N^3=0"),
        Gate("finite retarded primitive survivor set", "PASS" if candidates else "FAIL", str(candidates)),
        Gate("sharp filter concentrates on q64=15", "PASS" if q64 == 15 else "FAIL", f"q64={q64}"),
        Gate("epsilon=1 filter already dominated by q64=15", "PASS" if max(weights_1, key=weights_1.get) == 15 else "FAIL", f"w15={weights_1[15]:.12f}"),
        Gate("epsilon=0.25 filter sharply dominated by q64=15", "PASS" if weights_025[15] > 0.999999 else "FAIL", f"w15={weights_025[15]:.12f}"),
        Gate("CRT with q7=2 gives q=79", "PASS" if q448 == 79 else "FAIL", f"q={q448}"),
        Gate("actual MTT nil operator supplied", "OPEN", "requires N_MTT and closure-strain Hessian"),
        Gate("Z64 carry rows derived", "OPEN", "requires recursive shared-circle relation matrix"),
    ]

    print("Nil-survivor execution audit")
    print("============================")
    print(f"N^2 zero: {is_zero(n2)}")
    print(f"N^3 zero: {is_zero(n3)}")
    print(f"retarded primitive candidates: {candidates}")
    print(f"selected q64: {q64}")
    print(f"q448 from (q64,q7)=({q64},2): {q448}")
    print(f"filter weight at q64=15, epsilon=1.0: {weights_1[15]:.12f}")
    print(f"filter weight at q64=15, epsilon=0.25: {weights_025[15]:.12f}")
    print()
    print("Gate status")
    print("===========")
    for gate in gates:
        print(f"{gate.name:<55} {gate.status:<5} {gate.detail}")


if __name__ == "__main__":
    main()
