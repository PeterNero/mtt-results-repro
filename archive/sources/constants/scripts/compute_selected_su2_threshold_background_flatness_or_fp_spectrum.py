"""Prove the selected SU2 threshold background flatness branch.

The previous ghost determinant gate reduced SU2 to one sharp alternative:

1. prove the selected SU2 threshold background is the trivial/constant
   massless mode, so the Faddeev-Popov operator is field-independent; or
2. supply a selected non-flat FP spectrum.

Theta II and III are strong enough for the first part at leading threshold
order: Theta II takes the massless gauge harmonic constant after gauge fixing,
and Theta III linearizes the SU2 twistor action about the trivial bundle with
a constant massless twistor harmonic.

This closes background flatness.  It intentionally does not silently discard
the resulting flat adjoint determinant; that last move is a quotient
normalization policy, not a spectral calculation.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXACT_CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
GHOST_CERT = ROOT / "certificates" / "selected_su2_nonabelian_ghost_quotient_determinant_certificate.json"


def run_json(script: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    exact = run_json(EXACT_CIRCLE_SPHERE)
    ghost = json.loads(GHOST_CERT.read_text(encoding="utf-8"))

    p_scalar = float(exact["finite_parts"]["SU2_effective_sphere"])
    casimir_weight = float(ghost["selected_inputs"]["C_A_SU2_candidate"])
    adjoint_dim = int(ghost["selected_inputs"]["adjoint_dimension_SU2"])
    p_su2_no_extra = casimir_weight * p_scalar
    flat_adjoint_fp = adjoint_dim * p_scalar

    p_y = float(ghost["selected_inputs"]["p_Y_candidate_from_current_table"])
    lambda_no_extra = p_y - p_su2_no_extra
    lambda_keep_subtracting_ghost = p_y - (p_su2_no_extra - flat_adjoint_fp)
    lambda_keep_adding_ghost = p_y - (p_su2_no_extra + flat_adjoint_fp)

    output = {
        "status": "SU2_THRESHOLD_BACKGROUND_FLATNESS_CLOSED_FP_POLICY_OPEN",
        "purpose": "Close the selected SU2 threshold background flatness gate and isolate the remaining quotient-normalization policy.",
        "source_theorem": {
            "theta_ii": {
                "selected_geometry": "effective constant-curvature S2 lens layer",
                "selected_massless_harmonic": "constant on Sigma_2 after gauge fixing",
                "role": "Route A supports constant selected SU2 gauge harmonic.",
            },
            "theta_iii": {
                "twistor_background": "linearization about the trivial rank-2 holomorphic bundle",
                "selected_massless_harmonic": "constant along the twistor fiber",
                "overlap_result": "I_2^(0)=4*pi*(f2*R_lens)^2",
                "role": "Route B independently fixes the same leading SU2 zero-mode normalization.",
            },
        },
        "proved_flatness_statement": {
            "selected_threshold_background": "trivial-bundle constant massless SU2 zero mode",
            "connection_background": "A=0 at the selected leading threshold background",
            "fp_operator_reduction": "M_G[A]=partial^mu D_mu[A] -> -Delta_0 tensor ad(SU2)",
            "field_dependent_nonabelian_ghost_interactions_at_this_order": False,
            "closed": True,
        },
        "computed_flat_fp_data": {
            "p_scalar": p_scalar,
            "C_A_SU2": casimir_weight,
            "dim_ad_SU2": adjoint_dim,
            "p_SU2_no_extra_ghost_term": p_su2_no_extra,
            "flat_adjoint_fp_logdet": flat_adjoint_fp,
        },
        "remaining_policy_options": {
            "discard_or_absorb_flat_fp": {
                "status": "PREFERRED_BY_QUOTIENT_DISCIPLINE_BUT_NOT_YET_SOURCE_CERTIFIED_AS_THRESHOLD_POLICY",
                "rule": "field-independent FP quotient Jacobian is pure representative-measure normalization or already absorbed into C_A(SU2)",
                "p_SU2": p_su2_no_extra,
                "lambda_12": lambda_no_extra,
            },
            "keep_explicit_grassmann_subtraction": {
                "status": "DIAGNOSTIC_NOT_SELECTED",
                "rule": "retain -dim(ad SU2)*p_scalar as an additional finite threshold term",
                "p_SU2": p_su2_no_extra - flat_adjoint_fp,
                "lambda_12": lambda_keep_subtracting_ghost,
            },
            "keep_explicit_opposite_sign": {
                "status": "DIAGNOSTIC_NOT_SELECTED",
                "rule": "retain +dim(ad SU2)*p_scalar as an additional finite threshold term",
                "p_SU2": p_su2_no_extra + flat_adjoint_fp,
                "lambda_12": lambda_keep_adding_ghost,
            },
        },
        "verdict": {
            "selected_su2_threshold_background_flat": True,
            "selected_nonflat_fp_spectrum_required": False,
            "fp_operator_spectrum_reduced_to_scalar_sphere_times_adjoint": True,
            "quotient_normalization_policy_closed": False,
            "su2_selected_for_lambda_12_accounting": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Selected_Flat_FP_Quotient_Normalization_Policy_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
