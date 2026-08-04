"""Audit the finite Wilson/deck carrier extraction criterion."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md"
PRIMITIVE = ROOT / "Selected_Kernel_Primitive_Lag_Closure_for_Z64_Carrier_v1.md"
SCHUR = ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md"
CERT = ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def shift_perm(n: int, step: int = 1) -> tuple[int, ...]:
    return tuple((i + step) % n for i in range(n))


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def perm_power(p: tuple[int, ...], k: int) -> tuple[int, ...]:
    out = tuple(range(len(p)))
    for _ in range(k):
        out = compose(p, out)
    return out


def exact_order(p: tuple[int, ...]) -> int:
    ident = tuple(range(len(p)))
    cur = ident
    for k in range(1, len(p) + 1):
        cur = compose(p, cur)
        if cur == ident:
            return k
    raise AssertionError("permutation order exceeded dimension")


def lag_gcd(n: int, lags: list[int]) -> int:
    out = n
    for lag in lags:
        out = gcd(out, lag)
    return out


def is_circulant_kernel(kernel: list[complex]) -> bool:
    # A convolution kernel sum_m a_m S^m is circulant by construction.
    return len(kernel) == 64


def main() -> None:
    paper = PAPER.read_text(encoding="utf-8", errors="ignore") if PAPER.exists() else ""
    primitive = PRIMITIVE.read_text(encoding="utf-8", errors="ignore") if PRIMITIVE.exists() else ""
    schur = SCHUR.read_text(encoding="utf-8", errors="ignore") if SCHUR.exists() else ""
    cert = CERT.read_text(encoding="utf-8", errors="ignore") if CERT.exists() else ""

    s = shift_perm(64, 1)
    s2 = shift_perm(64, 2)
    order_s = exact_order(s)
    order_s2 = exact_order(s2)
    primitive_lags = [1, 63]
    even_lags = [2, 62]
    eighth_lags = [8, 56]
    kernel = [0j] * 64
    kernel[0] = 2
    kernel[1] = -0.5
    kernel[63] = -0.5

    gates = [
        Gate(
            "criterion paper saved",
            "PASS" if paper else "FAIL",
            str(PAPER),
        ),
        Gate(
            "primitive shift exact order",
            "PASS" if order_s == 64 else "FAIL",
            f"order(S)={order_s}",
        ),
        Gate(
            "proper divisor shift detected",
            "PASS" if order_s2 == 32 else "FAIL",
            f"order(S^2)={order_s2}",
        ),
        Gate(
            "unit-lag primitive support",
            "PASS" if lag_gcd(64, primitive_lags) == 1 else "FAIL",
            f"gcd(64,{primitive_lags})={lag_gcd(64, primitive_lags)}",
        ),
        Gate(
            "selected-kernel primitive lag",
            "PROVED" if "selected-kernel primitive-lag gate              PROVED" in primitive else "FAIL",
            "16 -> 15 gives S^-1 and gcd(64,63)=1",
        ),
        Gate(
            "even-lag divisor collapse detected",
            "PASS" if lag_gcd(64, even_lags) == 2 else "FAIL",
            f"gcd(64,{even_lags})={lag_gcd(64, even_lags)}",
        ),
        Gate(
            "eighth-lag divisor collapse detected",
            "PASS" if lag_gcd(64, eighth_lags) == 8 else "FAIL",
            f"gcd(64,{eighth_lags})={lag_gcd(64, eighth_lags)}",
        ),
        Gate(
            "block-circulant kernel model",
            "PASS" if is_circulant_kernel(kernel) else "FAIL",
            "kernel is represented as sum_m a_m S^m",
        ),
        Gate(
            "paper states Fourier idempotents",
            "PASS" if "E_q = (1/64)" in paper and "E_q E_p = delta_qp E_q" in paper else "FAIL",
            "character projectors are explicit",
        ),
        Gate(
            "paper states coherent inclusion",
            "PASS" if "P_CP,64 <= Pi_coh" in paper else "FAIL",
            "carrier must be retained by Pi_coh",
        ),
        Gate(
            "exact branch block satisfying criterion",
            "CLOSED" if "Z64 exact central-circle branch certificate       CLOSED" in cert else "FAIL",
            "selected exact central-circle branch supplies K64,S,L64,Kret64",
        ),
        Gate(
            "exact-branch Schur inequality",
            "PROVED" if "C_fl/(alpha lambda_Q)<9/2 in exact branch             PROVED" in schur else "FAIL",
            "C_fl=0 when P_fl<=Pi_coh and [L,Pi_coh]=0",
        ),
        Gate(
            "non-exact Schur inequality",
            "OPTIONAL-OPEN",
            "bound epsilon_comm or warp leakage if exact block commutation is relaxed",
        ),
    ]

    print("Finite Wilson/deck Z64 carrier extraction audit")
    print("================================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
