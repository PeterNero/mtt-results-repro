"""Evaluate finite abelian quotient character spectra for MTT flavor CP.

Given invariant factors from a Smith normal form, this script searches
characters of G = Z_d1 x ... x Z_dr for phases close to the CKM branch target
and the illustrative leptonic -pi/2 benchmark.

The phase assigned to a tuple k is the diagonal character phase
  2*pi * sum_i k_i / d_i   mod 2*pi.

This is the natural first diagnostic for product quotients.  A more detailed
MTT model may restrict which diagonal characters are physically selected.
"""

from __future__ import annotations

from itertools import product
from math import asin, cos, pi, sin, sqrt


S12 = 0.2250
S23 = 0.0411
S13 = 0.0036
J_TARGET = 2.9e-5


def c(s: float) -> float:
    return sqrt(1.0 - s * s)


J_PREF = c(S12) * c(S23) * c(S13) ** 2 * S12 * S23 * S13
DELTA_TARGET = asin(J_TARGET / J_PREF)


def j_ckm(delta: float) -> float:
    return J_PREF * sin(delta)


def canonical_phase(x: float) -> float:
    return x % (2 * pi)


def signed_phase(x: float) -> float:
    return ((x + pi) % (2 * pi)) - pi


def tuple_phase(factors: tuple[int, ...], weights: tuple[int, ...]) -> float:
    return canonical_phase(2 * pi * sum(k / d for k, d in zip(weights, factors)))


def search_ckm(factors: tuple[int, ...]) -> tuple[tuple[int, ...], float, float, float]:
    best = None
    for weights in product(*(range(d) for d in factors)):
        delta = tuple_phase(factors, weights)
        phase_err = abs(delta - DELTA_TARGET)
        jerr = abs(j_ckm(delta) - J_TARGET)
        candidate = (phase_err, jerr, weights, delta)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    phase_err, jerr, weights, delta = best
    return weights, delta, phase_err, jerr


def search_lepton(factors: tuple[int, ...]) -> tuple[tuple[int, ...], float, float]:
    target = -pi / 2
    best = None
    for weights in product(*(range(d) for d in factors)):
        delta = signed_phase(tuple_phase(factors, weights))
        err = abs(delta - target)
        candidate = (err, weights, delta)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    err, weights, delta = best
    return weights, delta, err


def report(factors: tuple[int, ...]) -> None:
    wq, dq, perr, jerr = search_ckm(factors)
    wl, dl, lerr = search_lepton(factors)
    print(
        f"G={factors}: CKM weights={wq}, delta={dq:.12f}, "
        f"phase_err={perr:.3e}, J_err={jerr:.3e}; "
        f"lepton weights={wl}, delta_l={dl:.12f}, l_err={lerr:.3e}"
    )


def main() -> None:
    print(f"Target CKM branch delta = {DELTA_TARGET:.12f} rad")
    print()
    candidates = [
        (3,),
        (68,),
        (64, 7),
        (7, 64),
        (4, 112),
        (8, 56),
        (16, 28),
        (32, 14),
        (448,),
        (2, 224),
        (4, 4, 28),
        (8, 8, 7),
        (64,),
        (7,),
        (112,),
        (224,),
    ]
    for factors in candidates:
        # Keep brute force bounded.
        size = 1
        for d in factors:
            size *= d
        if size > 5000:
            print(f"G={factors}: skipped, size={size}")
            continue
        report(factors)


if __name__ == "__main__":
    main()

