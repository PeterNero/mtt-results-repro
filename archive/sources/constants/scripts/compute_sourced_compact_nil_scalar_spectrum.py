"""Import the compact Heisenberg nilmanifold scalar spectrum.

This closes one narrow data gap for the Qa/Nil route: the scalar compact
nilmanifold multiplicities.  It does not close the selected Qa gauge determinant,
because the gauge operator, BRST quotient, and analytic zeta finite part are
separate inputs.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
R1_CERT = ROOT / "certificates" / "selected_central_circle_damping_identification_lemma_certificate.json"
QA_REDUCTION_CERT = ROOT / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def selected_r1_for_n(cert: dict[str, Any], n_value: int) -> float:
    for row in cert["tested_cases"]:
        if int(row["N"]) == n_value:
            return float(row["R1_z64_normalized"])
    raise KeyError(f"N={n_value} not found")


def scalar_eigenvalue_p0(m: int, n: int, r1: float, r2: float) -> float:
    return (2.0 * math.pi * m / r1) ** 2 + (2.0 * math.pi * n / r2) ** 2


def scalar_eigenvalue_p_nonzero(k: int, oscillator_n: int, r3: float, f_struct: float) -> float:
    return (2.0 * math.pi * k / r3) ** 2 + (2 * oscillator_n + 1) * abs(k) * 2.0 * math.pi * abs(f_struct) / r3


def main() -> int:
    r1_cert = load(R1_CERT)
    qa_reduction = load(QA_REDUCTION_CERT)

    n_selected = 79
    r1_selected = selected_r1_for_n(r1_cert, n_selected)
    c_nil = 1.439 * r1_selected

    # Match the MTT convention used by Theta II: a=b=1 and central length c_nil.
    # For the external compact spectrum notation, this is r^1=r^2=1, r^3=c_nil,
    # N=(r1*r2/r3)*f.  The standard selected lattice takes N=1, hence f=c_nil.
    r_base_1 = 1.0
    r_base_2 = 1.0
    r_central = c_nil
    lattice_n = 1
    f_struct = lattice_n * r_central / (r_base_1 * r_base_2)

    sample_modes = {
        "p0_first_modes": [
            {
                "m": 1,
                "n": 0,
                "multiplicity_from_signs": 4,
                "eigenvalue": scalar_eigenvalue_p0(1, 0, r_base_1, r_base_2),
            },
            {
                "m": 1,
                "n": 1,
                "multiplicity_from_signs": 4,
                "eigenvalue": scalar_eigenvalue_p0(1, 1, r_base_1, r_base_2),
            },
        ],
        "p_nonzero_first_modes": [
            {
                "k_abs": k_abs,
                "oscillator_n": oscillator_n,
                "sign_pair_l_multiplicity": 2 * k_abs,
                "eigenvalue": scalar_eigenvalue_p_nonzero(k_abs, oscillator_n, r_central, f_struct),
            }
            for k_abs, oscillator_n in [(1, 0), (1, 1), (2, 0), (3, 0)]
        ],
    }

    exact_first = sample_modes["p_nonzero_first_modes"][0]["eigenvalue"]
    prior_schema_first = (
        2.0 * math.pi * 1 * (2.0 * 0 + 1.0)
        + (2.0 * math.pi * 1) ** 2 / (c_nil * c_nil)
    )

    exact_scalar_branch = next(
        item
        for item in qa_reduction["diagnostic_branch_summaries"]
        if item["name"] == "sign_pair_abs_p_multiplicity"
    )
    old_proxy_branch = next(
        item
        for item in qa_reduction["diagnostic_branch_summaries"]
        if item["name"] == "sign_pair_unit_multiplicity"
    )

    output = {
        "status": "COMPACT_NIL_SCALAR_SPECTRUM_SOURCE_IMPORTED_DETERMINANT_OPEN",
        "external_source": {
            "title": "Laplacian spectrum on a nilmanifold, truncations and effective theories",
            "arxiv": "1806.05156",
            "url": "https://arxiv.org/abs/1806.05156",
            "used_data": [
                "scalar p0 torus eigenvalues",
                "scalar p!=0 oscillator eigenvalues",
                "integer ranges k in Z*, oscillator n in N, l=0,...,|k|-1",
            ],
        },
        "selected_geometry_map": {
            "N": n_selected,
            "R1_z64_normalized": r1_selected,
            "r_base_1": r_base_1,
            "r_base_2": r_base_2,
            "r_central": r_central,
            "lattice_integer_N": lattice_n,
            "f_struct": f_struct,
            "relation": "lattice_integer_N=(r_base_1*r_base_2/r_central)*f_struct",
        },
        "spectrum_formula": {
            "p0_sector": "mu_{m,n}^2=(2*pi*m/r1)^2+(2*pi*n/r2)^2, (m,n) in Z^2",
            "p_nonzero_sector": "M_{k,l,n}^2=k^2*(2*pi/r3)^2+(2n+1)*|k|*2*pi*|f|/r3",
            "integer_ranges": "k in Z*, n in N, l=0,...,|k|-1",
            "selected_mtt_form": "M_{k,n}^2=(2*pi*k/c_nil)^2+(2n+1)*|k|*2*pi for N=1",
            "p_nonzero_multiplicity_after_signs_and_l": "2*|k|",
        },
        "sample_modes": sample_modes,
        "consistency_checks": {
            "first_p_nonzero_eigenvalue_matches_prior_schema": abs(exact_first - prior_schema_first),
            "prior_sign_pair_unit_multiplicity_was_not_compact_scalar_spectrum": True,
            "compact_scalar_multiplicity_branch_name": "sign_pair_abs_p_multiplicity",
            "compact_scalar_branch_residual_lambda_12_if_naively_fitted": exact_scalar_branch[
                "residual_lambda_12"
            ],
            "old_proxy_branch_residual_lambda_12": old_proxy_branch["residual_lambda_12"],
        },
        "verdict": {
            "compact_scalar_eigenvalue_formula_imported": True,
            "compact_scalar_p_nonzero_multiplicity_imported": True,
            "old_unit_multiplicity_proxy_retired_for_compact_scalar_claims": True,
            "selected_Qa_gauge_operator_closed": False,
            "BRST_ghost_quotient_closed": False,
            "analytic_zeta_determinant_closed": False,
            "numeric_electroweak_closure_certified": False,
            "next_required_artifact": "Exact_Selected_Nil_Gauge_Threshold_Zeta_Determinant_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
