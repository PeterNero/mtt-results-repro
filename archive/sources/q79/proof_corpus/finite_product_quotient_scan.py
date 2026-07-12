"""Scan small two-factor finite abelian quotients for CP phase quality."""

from __future__ import annotations

from math import gcd

from finite_abelian_quotient_character_search import search_ckm, search_lepton


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def main() -> None:
    rows = []
    for d1 in range(2, 129):
        for d2 in range(2, 129):
            size = d1 * d2
            if size > 5000:
                continue
            wq, dq, perr, jerr = search_ckm((d1, d2))
            wl, dl, lerr = search_lepton((d1, d2))
            exp = lcm(d1, d2)
            # exact or very near lepton benchmark, and good CKM branch
            if lerr < 1e-12 and perr < 1e-4:
                rows.append((perr, jerr, exp, d1, d2, wq, wl))

    print("Two-factor product quotients with exact -pi/2 and CKM phase error < 1e-4:")
    print("phase_err    J_err       exp    d1   d2   CKM weights   lepton weights")
    for perr, jerr, exp, d1, d2, wq, wl in sorted(rows)[:50]:
        print(
            f"{perr:10.3e} {jerr:10.3e} {exp:6d} {d1:5d} {d2:5d} "
            f"{str(wq):>13} {str(wl):>15}"
        )


if __name__ == "__main__":
    main()

