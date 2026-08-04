"""Reduce the selected SU2 nonabelian ghost quotient determinant gate.

The previous SU2 gate showed that the effective sphere scalar zeta piece is
exact, but cannot be promoted to the selected gauge block until the
nonabelian Faddeev-Popov quotient determinant is accounted for.

This computation keeps the no-knob discipline: it does not fit the observed
weak angle or import a preferred sign by target proximity.  It enumerates the
source-supported algebraic branches and records the exact missing source
statement needed to close SU2.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXACT_CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
SPECTRA_CERT = ROOT / "certificates" / "selected_qaqcsu2_operator_spectra_or_heat_coefficients_certificate.json"
SU2_REDUCTION_CERT = ROOT / "certificates" / "selected_su2_sphere_gauge_block_equivalence_certificate.json"


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


def branch(
    name: str,
    status: str,
    description: str,
    p_y: float,
    p_scalar: float,
    casimir_weight: float,
    ghost_multiplier: float | None,
    selectable_now: bool,
    reason: str,
) -> dict[str, Any]:
    ghost_contribution = None if ghost_multiplier is None else ghost_multiplier * p_scalar
    p_su2 = None if ghost_contribution is None else casimir_weight * p_scalar + ghost_contribution
    lambda_12 = None if p_su2 is None else p_y - p_su2
    return {
        "name": name,
        "status": status,
        "description": description,
        "formula": {
            "p_SU2_selected": None if ghost_multiplier is None else "C_A(SU2)*p_scalar + ghost_multiplier*p_scalar",
            "ghost_multiplier": ghost_multiplier,
            "C_A_SU2": casimir_weight,
        },
        "values": {
            "ghost_finite_part": ghost_contribution,
            "p_SU2_selected": p_su2,
            "lambda_12_candidate": lambda_12,
        },
        "selection": {
            "selectable_now": selectable_now,
            "reason": reason,
        },
    }


def main() -> int:
    exact = run_json(EXACT_CIRCLE_SPHERE)
    spectra = json.loads(SPECTRA_CERT.read_text(encoding="utf-8"))
    su2_reduction = json.loads(SU2_REDUCTION_CERT.read_text(encoding="utf-8"))

    p_scalar = float(exact["finite_parts"]["SU2_effective_sphere"])
    casimir_weight = float(
        su2_reduction["available_exact_data"]["casimir_heat_weight_candidate"]
    )
    accounting = spectra["candidate_hypercharge_accounting"]
    p_y = float(accounting["p_Y_candidate"])
    prior_p_su2 = float(accounting["p_SU2_candidate"])
    prior_lambda_12 = float(accounting["lambda_12_candidate"])

    adjoint_dim = 3.0
    flat_fp_logdet = adjoint_dim * p_scalar

    branches = [
        branch(
            name="flat_background_universal_or_absorbed_ghost",
            status="CONDITIONAL_CLOSURE_BRANCH",
            description=(
                "If the selected SU2 representative is the constant massless harmonic/flat "
                "background and the FP determinant is field-independent after projection, "
                "then the quotient determinant is universal or already absorbed into the "
                "Casimir heat coefficient.  The extra weak-split finite term is zero."
            ),
            p_y=p_y,
            p_scalar=p_scalar,
            casimir_weight=casimir_weight,
            ghost_multiplier=0.0,
            selectable_now=False,
            reason=(
                "Theta II supports the constant massless harmonic after gauge fixing, "
                "but the corpus does not yet prove that the selected threshold FP "
                "operator is flat/universal in the physical quotient."
            ),
        ),
        branch(
            name="explicit_flat_adjoint_ghost_subtraction",
            status="DIAGNOSTIC_SIGN_BRANCH_NOT_SELECTED",
            description=(
                "Treat the flat ghost determinant as an explicit complex Grassmann "
                "adjoint subtraction relative to the gauge-block finite part."
            ),
            p_y=p_y,
            p_scalar=p_scalar,
            casimir_weight=casimir_weight,
            ghost_multiplier=-adjoint_dim,
            selectable_now=False,
            reason=(
                "The sign and normalization of this finite internal threshold are not "
                "selected by the current MTT quotient convention; using it would be a "
                "model choice rather than a theorem."
            ),
        ),
        branch(
            name="explicit_flat_adjoint_ghost_addition",
            status="DIAGNOSTIC_SIGN_BRANCH_NOT_SELECTED",
            description=(
                "Treat the flat ghost determinant as an explicit adjoint contribution "
                "with the opposite finite-threshold sign."
            ),
            p_y=p_y,
            p_scalar=p_scalar,
            casimir_weight=casimir_weight,
            ghost_multiplier=adjoint_dim,
            selectable_now=False,
            reason=(
                "Included only as a sign-convention stress test.  The current corpus "
                "does not select this sign or promote it to a physical quotient rule."
            ),
        ),
        branch(
            name="curved_nonabelian_fp_operator",
            status="OPEN_SELECTED_SPECTRUM_REQUIRED",
            description=(
                "Use the genuine nonabelian operator M_G[A]=partial^mu D_mu[A] for a "
                "selected non-flat SU2 connection and compute its zeta determinant."
            ),
            p_y=p_y,
            p_scalar=p_scalar,
            casimir_weight=casimir_weight,
            ghost_multiplier=None,
            selectable_now=False,
            reason=(
                "Requires selected connection A, curvature endomorphism, domain, "
                "zero-mode removal, and determinant sign rule."
            ),
        ),
    ]

    output = {
        "status": "SU2_NONABELIAN_GHOST_QUOTIENT_REDUCED_NOT_CLOSED",
        "purpose": "Determine whether the SU2 nonabelian FP ghost quotient contributes an additional finite weak-split term.",
        "selected_inputs": {
            "p_SU2_scalar_exact": p_scalar,
            "C_A_SU2_candidate": casimir_weight,
            "adjoint_dimension_SU2": adjoint_dim,
            "flat_adjoint_fp_logdet_candidate": flat_fp_logdet,
            "p_Y_candidate_from_current_table": p_y,
            "prior_p_SU2_candidate": prior_p_su2,
            "prior_lambda_12_candidate": prior_lambda_12,
        },
        "source_constraints": {
            "gauge_fixing": {
                "abelian_fp_decouples": True,
                "nonabelian_fp_operator": "M_G[A] = partial^mu D_mu[A]",
                "nonabelian_fp_field_dependent_for_general_A": True,
            },
            "theta_ii_lens_layer": {
                "effective_geometry": "constant-curvature S2 with radius_squared=(f2*R_lens)^2",
                "massless_gauge_harmonic": "constant on Sigma_2 after gauge fixing",
                "supports_flat_background_candidate": True,
                "proves_full_fp_quotient_policy": False,
            },
            "brst_discipline": {
                "ghosts_are_quotient_measure_bookkeeping": True,
                "physical_states_are_bst_cohomology": True,
                "finite_threshold_sign_must_be_selected_not_fitted": True,
            },
        },
        "computed_branches": branches,
        "conditional_theorem": {
            "statement": (
                "If the selected SU2 threshold background is the constant flat "
                "representative and the physical quotient discards or absorbs the "
                "field-independent adjoint FP determinant, then the SU2 block stays "
                "p_SU2=C_A(SU2)*p_scalar and no extra ghost finite term enters lambda_12."
            ),
            "would_close_SU2_block": True,
            "resulting_p_SU2": prior_p_su2,
            "resulting_lambda_12": prior_lambda_12,
            "missing_single_source_statement": (
                "Selected_SU2_Threshold_Background_is_Flat_and_FP_Determinant_is_Universal_or_Casimir_Absorbed"
            ),
        },
        "verdict": {
            "flat_zero_extra_branch_identified": True,
            "curved_branch_requires_new_spectrum": True,
            "su2_ghost_quotient_closed": False,
            "su2_selected_for_lambda_12_accounting": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Selected_SU2_Threshold_Background_Flatness_or_FP_Spectrum_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
