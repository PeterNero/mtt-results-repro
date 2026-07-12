"""Generate a selected gauge-factor spectral table for determinant diagnostics.

This generator implements the first concrete spectral-table candidate from the
currently selected q79/Theta scaffold:

* U1  -> circle scalar Laplacian Fourier modes.
* SU2 -> effective round S2/lens scalar Laplacian modes.
* SU3 -> compact Nil scalar Laplacian diagnostic modes: exact p=0 torus
  sector plus a Landau-level lower-proxy for p != 0.

The output is suitable for compute_selected_local_determinant_response.py, but
it is not a final no-knob prediction because the Nil p != 0 sector, determinant
regularization, and representation/index weights are not yet fully certified.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CENTRAL_CERT = ROOT / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"


def selected_r1(n: int) -> float:
    data = json.loads(CENTRAL_CERT.read_text(encoding="utf-8"))
    for row in data["tested_cases"]:
        if row["N"] == n:
            return float(row["R1_z64_normalized"])
    raise ValueError(f"N={n} is not present in {CENTRAL_CERT}")


def circle_modes(r1: float, n_max: int) -> list[dict[str, float | str]]:
    modes = []
    for n in range(1, n_max + 1):
        modes.append(
            {
                "eigenvalue": (n * n) / (r1 * r1),
                "multiplicity": 2.0,
                "index_weight": 1.0,
                "label": f"circle_n={n}",
            }
        )
    return modes


def sphere_modes(radius_squared: float, ell_max: int) -> list[dict[str, float | str]]:
    modes = []
    for ell in range(1, ell_max + 1):
        modes.append(
            {
                "eigenvalue": ell * (ell + 1) / radius_squared,
                "multiplicity": float(2 * ell + 1),
                "index_weight": 1.0,
                "label": f"sphere_ell={ell}",
            }
        )
    return modes


def nil_modes(c_nil: float, m_max: int, p_max: int, k_max: int) -> list[dict[str, float | str]]:
    modes: list[dict[str, float | str]] = []
    seen: dict[float, float] = {}

    for m in range(-m_max, m_max + 1):
        for n in range(-m_max, m_max + 1):
            if m == 0 and n == 0:
                continue
            eigenvalue = 4.0 * math.pi * math.pi * (m * m + n * n)
            # Merge exactly equal integer shells in the p=0 torus sector.
            seen[eigenvalue] = seen.get(eigenvalue, 0.0) + 1.0

    for eigenvalue, multiplicity in sorted(seen.items()):
        modes.append(
            {
                "eigenvalue": eigenvalue,
                "multiplicity": multiplicity,
                "index_weight": 1.0,
                "label": "nil_p=0_torus_shell",
            }
        )

    for p in range(1, p_max + 1):
        for k in range(0, k_max + 1):
            eigenvalue = 2.0 * math.pi * p * (2 * k + 1) + (2.0 * math.pi * p) ** 2 / (c_nil * c_nil)
            modes.append(
                {
                    "eigenvalue": eigenvalue,
                    "multiplicity": 2.0,
                    "index_weight": 1.0,
                    "label": f"nil_landau_lower_proxy_p=±{p}_k={k}",
                }
            )

    return modes


def build_table(n: int, circle_n_max: int, sphere_ell_max: int, nil_m_max: int, nil_p_max: int, nil_k_max: int) -> dict:
    r1 = selected_r1(n)
    lens_radius_squared = 0.280 * r1
    c_nil = 1.439 * r1
    spectra = {
        "U1": circle_modes(r1, circle_n_max),
        "SU2": sphere_modes(lens_radius_squared, sphere_ell_max),
        "SU3": nil_modes(c_nil, nil_m_max, nil_p_max, nil_k_max),
    }
    return {
        "status": "DIAGNOSTIC_TRUNCATED_SPECTRAL_TABLE_NOT_FINAL_PREDICTION",
        "selected_local_determinant": {
            "reference_scale_squared": 1.0,
            "gauge_factor_spectra": spectra,
        },
        "selected_scaffold": {
            "N": n,
            "R1_z64_normalized": r1,
            "lens_radius_squared": lens_radius_squared,
            "nil_c": c_nil,
            "geometry_assignment": {
                "U1": "circle scalar Laplacian",
                "SU2": "effective round S2/lens scalar Laplacian",
                "SU3": "Nil scalar Laplacian diagnostic: exact p=0 torus sector plus p!=0 Landau lower-proxy",
            },
            "weight_profile": "unit diagnostic weights; representation/Dynkin weights still open",
        },
        "cutoffs": {
            "circle_n_max": circle_n_max,
            "sphere_ell_max": sphere_ell_max,
            "nil_m_max": nil_m_max,
            "nil_p_max": nil_p_max,
            "nil_k_max": nil_k_max,
        },
        "not_final_because": [
            "The Nil p!=0 compact spectrum is represented by a lower-proxy, not the exact selected spectrum.",
            "The determinant is a cutoff diagnostic, not zeta/heat-kernel finite part.",
            "Index weights are unit diagnostics rather than topology-certified gauge threshold weights.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=79)
    parser.add_argument("--circle-n-max", type=int, default=3)
    parser.add_argument("--sphere-ell-max", type=int, default=3)
    parser.add_argument("--nil-m-max", type=int, default=2)
    parser.add_argument("--nil-p-max", type=int, default=2)
    parser.add_argument("--nil-k-max", type=int, default=2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    table = build_table(
        args.N,
        args.circle_n_max,
        args.sphere_ell_max,
        args.nil_m_max,
        args.nil_p_max,
        args.nil_k_max,
    )
    text = json.dumps(table, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
