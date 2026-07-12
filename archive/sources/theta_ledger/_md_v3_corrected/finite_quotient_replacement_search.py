"""Search finite cyclic quotients that can replace the Z_448 CP benchmark.

This script is diagnostic.  It does not derive a quotient from MTT; it tells us
how good a derived cyclic quotient Z_N would be if MTT selected it.
"""

from __future__ import annotations

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


def phase_error(delta: float) -> float:
    # Compare modulo the sine ambiguity only near the target branch used here.
    return abs(delta - DELTA_TARGET)


def best_ckm_j_only_for_n(n: int) -> tuple[int, float, float, float]:
    best = None
    for k in range(n):
        delta = 2 * pi * k / n
        err = abs(j_ckm(delta) - J_TARGET)
        candidate = (err, k, delta, j_ckm(delta))
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    err, k, delta, j = best
    return k, delta, j, err


def best_ckm_phase_branch_for_n(n: int) -> tuple[int, float, float, float, float]:
    best = None
    for k in range(n):
        delta = 2 * pi * k / n
        perr = phase_error(delta)
        jerr = abs(j_ckm(delta) - J_TARGET)
        candidate = (perr, jerr, k, delta, j_ckm(delta))
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    perr, jerr, k, delta, j = best
    return k, delta, j, jerr, perr


def best_lepton_pi_over_2_for_n(n: int) -> tuple[int, float, float]:
    target = -pi / 2
    best = None
    for k in range(n):
        # choose representative in [-pi, pi)
        delta = ((2 * pi * k / n + pi) % (2 * pi)) - pi
        err = abs(delta - target)
        candidate = (err, k, delta)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    err, k, delta = best
    return k, delta, err


def main() -> None:
    print(f"CKM target delta from J={J_TARGET:.3e}: {DELTA_TARGET:.12f} rad")
    print()

    rows = []
    for n in range(4, 1025):
        kq, dq, jq, jerr, perr = best_ckm_phase_branch_for_n(n)
        kl, dl, lerr = best_lepton_pi_over_2_for_n(n)
        score = perr + lerr
        rows.append((score, n, kq, dq, jq, jerr, perr, kl, dl, lerr, n % 4 == 0))

    print("Best cyclic replacement quotients up to N=1024, target phase branch:")
    print("score     N    kq   delta_q       phase_err    J_CKM          J_err       kl   delta_l       l_err     pi/2 exact")
    for score, n, kq, dq, jq, jerr, perr, kl, dl, lerr, exact in sorted(rows)[:25]:
        print(
            f"{score:8.3e} {n:4d} {kq:5d} {dq:12.9f} "
            f"{perr:10.3e} {jq:12.8e} {jerr:10.3e} {kl:5d} {dl:12.9f} "
            f"{lerr:9.2e} {str(exact):>10}"
        )

    print()
    print("Best quotients with exact -pi/2 lepton phase, i.e. N divisible by 4:")
    exact_rows = [row for row in rows if row[-1]]
    for score, n, kq, dq, jq, jerr, perr, kl, dl, lerr, exact in sorted(exact_rows)[:20]:
        print(
            f"N={n:4d}, kq={kq:4d}, delta_q={dq:.9f}, "
            f"phase_err={perr:.3e}, J={jq:.8e}, J_err={jerr:.3e}, kl={kl}"
        )

    print()
    for n in [68, 112, 224, 336, 448, 672, 896]:
        kq, dq, jq, jerr, perr = best_ckm_phase_branch_for_n(n)
        kl, dl, lerr = best_lepton_pi_over_2_for_n(n)
        kj, dj, jj, jjerr = best_ckm_j_only_for_n(n)
        print(
            f"Selected N={n:4d}: kq={kq:4d}, delta_q={dq:.9f}, "
            f"phase_err={perr:.3e}, J={jq:.8e}, J_err={jerr:.3e}, "
            f"kl={kl:4d}, delta_l={dl:.9f}, l_err={lerr:.3e}; "
            f"J-only k={kj}, delta={dj:.9f}, J_err={jjerr:.3e}"
        )


if __name__ == "__main__":
    main()
