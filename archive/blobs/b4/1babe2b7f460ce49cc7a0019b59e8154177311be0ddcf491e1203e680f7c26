"""Compute the exact U1 circle and SU2 sphere zeta determinant pieces.

This closes the analytic zeta determinant for the gauge-factor pieces whose
selected scalar proxy spectra are exact in the current scaffold:

U1:
    lambda_n = n^2/R1^2, multiplicity 2.

SU2:
    lambda_l = l(l+1)/A, multiplicity 2l+1, A=(f2 R_lens)^2.

The SU3 Nil determinant is intentionally not filled here.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CENTRAL_CERT = ROOT / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"

# Glaisher-Kinkelin constant.  zeta_R'(-1)=1/12-log(A_G).
GLAISHER_KINKELIN = 1.2824271291006226368753425688697917277676889273250


def selected_r1(n: int = 79) -> float:
    data = json.loads(CENTRAL_CERT.read_text(encoding="utf-8"))
    for row in data["tested_cases"]:
        if row["N"] == n:
            return float(row["R1_z64_normalized"])
    raise ValueError(f"N={n} is not present in {CENTRAL_CERT}")


def zeta_prime_minus_one() -> float:
    return (1.0 / 12.0) - math.log(GLAISHER_KINKELIN)


def circle_finite_part(r1: float) -> float:
    # -d/ds [2 R1^(2s) zeta_R(2s)] at s=0.
    return 2.0 * math.log(2.0 * math.pi * r1)


def sphere_finite_part(radius_squared: float) -> float:
    # For the unit sphere:
    #   S(s)=sum_{l>=1}(2l+1)(l(l+1))^-s
    #   S(0)=-2/3
    #   -S'(0)=-4 zeta_R'(-1)
    # Scaling by radius_squared=A gives -d/ds[A^s S(s)]_0.
    unit = -4.0 * zeta_prime_minus_one()
    return unit + (2.0 / 3.0) * math.log(radius_squared)


def main() -> int:
    r1 = selected_r1(79)
    lens_radius_squared = 0.280 * r1
    u1 = circle_finite_part(r1)
    su2 = sphere_finite_part(lens_radius_squared)
    output = {
        "status": "EXACT_U1_SU2_ZETA_PIECES_CLOSED_SU3_NIL_OPEN",
        "selected_scaffold": {
            "N": 79,
            "R1_z64_normalized": r1,
            "lens_radius_squared": lens_radius_squared,
            "nil_c": 1.439 * r1,
        },
        "constants": {
            "glaisher_kinkelin": GLAISHER_KINKELIN,
            "zeta_R_prime_minus_one": zeta_prime_minus_one(),
        },
        "finite_parts": {
            "U1_circle": u1,
            "SU2_effective_sphere": su2,
            "U1_minus_SU2": u1 - su2,
            "SU3_nil": None,
        },
        "closed_formulas": {
            "U1_circle": "2*log(2*pi*R1)",
            "SU2_effective_sphere": "-4*zeta_R'(-1)+(2/3)*log((f2*R_lens)^2)",
        },
        "verdict": {
            "u1_circle_zeta_closed": True,
            "su2_effective_sphere_zeta_closed": True,
            "su3_nil_zeta_closed": False,
            "numeric_electroweak_closure": False,
            "next_required_computation": "Exact compact Nil/gauge-threshold zeta determinant and topology-certified weights.",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
