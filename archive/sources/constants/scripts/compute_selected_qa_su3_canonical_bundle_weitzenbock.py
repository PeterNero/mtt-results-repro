"""Compute the canonical Nil color-bundle and Weitzenbock data for Qa/SU3.

This script turns the previous projector-or-endomorphism gate into concrete
geometry.  The selected SU3 color fiber is the compact Heisenberg nilmanifold
with isotropic horizontal metric

    g = sigma_1^2 + sigma_2^2 + c_nil^2 sigma_3^2.

For the orthonormal coframe e1=sigma1, e2=sigma2, e3=c_nil*sigma3, the only
structure coefficient is |[E1,E2]| = c_nil.  The standard 3D Heisenberg Ricci
endomorphism on one-forms is diag(-f^2/2, -f^2/2, +f^2/2).  That is the
canonical Weitzenbock curvature term for the Hodge one-form block.

The output is intentionally conservative: it computes selected geometric data
and compares it with the remaining Qa/SU3 determinant gap, but it does not
promote a near miss into closure.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SPECTRUM_CERT = ROOT / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json"
GAP_CERT = ROOT / "certificates" / "selected_qa_su3_gauge_quotient_gap_certificate.json"
PATH_CERT = ROOT / "certificates" / "selected_qa_su3_projector_endomorphism_pathways_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def compare(value: float, target: float) -> dict[str, float]:
    return {
        "value": value,
        "difference_from_required_gap": value - target,
        "absolute_difference_from_required_gap": abs(value - target),
    }


def main() -> int:
    spectrum = load(SPECTRUM_CERT)
    gap = load(GAP_CERT)
    pathway = load(PATH_CERT)

    c_nil = float(spectrum["selected_geometry_map"]["r_central"])
    f = float(spectrum["selected_geometry_map"]["f_struct"])
    required_gap = float(gap["computed_gap"]["unweighted_Qa_gap"])

    # Selected Nil color fiber with a=b=1 has volume c and canonical overlap c
    # for a left-invariant horizontal harmonic one-form.
    nil_volume = c_nil
    leading_su3_overlap = c_nil
    unit_normalized_horizontal_harmonic_density = 1.0 / c_nil

    f2 = f * f
    ricci_oneform_eigenvalues = {
        "horizontal_e1": -0.5 * f2,
        "horizontal_e2": -0.5 * f2,
        "central_e3": 0.5 * f2,
    }
    rough_laplacian_on_harmonic_horizontal = 0.5 * f2
    hodge_laplacian_on_harmonic_horizontal = (
        rough_laplacian_on_harmonic_horizontal + ricci_oneform_eigenvalues["horizontal_e1"]
    )
    curvature_loss_bound = 0.5 * f2

    # These are geometry-derived diagnostics, not determinant values.  A real
    # determinant response still requires the selected spectral action of E_Qa
    # on the physical quotient.
    geometric_response_diagnostics = {
        "ricci_loss_one_horizontal": curvature_loss_bound,
        "two_horizontal_ricci_losses": 2.0 * curvature_loss_bound,
        "central_positive_ricci": ricci_oneform_eigenvalues["central_e3"],
        "full_structure_square": f2,
        "minus_log_selected_nil_overlap": -math.log(leading_su3_overlap),
        "minus_3_log_selected_nil_overlap": -3.0 * math.log(leading_su3_overlap),
    }
    compared = {
        name: compare(value, required_gap)
        for name, value in geometric_response_diagnostics.items()
    }
    closest_name = min(
        compared,
        key=lambda name: compared[name]["absolute_difference_from_required_gap"],
    )

    output = {
        "status": "QA_SU3_CANONICAL_BUNDLE_WEITZENBOCK_DATA_COMPUTED_CLOSURE_OPEN",
        "selected_geometry": {
            "fiber": "Gamma\\Nil_3 compact Heisenberg color fiber",
            "metric": "sigma_1^2 + sigma_2^2 + c_nil^2 sigma_3^2",
            "a_horizontal": 1.0,
            "b_horizontal": 1.0,
            "c_nil": c_nil,
            "structure_constant_f": f,
            "nil_volume": nil_volume,
            "leading_su3_overlap_I3_0": leading_su3_overlap,
            "unit_normalized_horizontal_harmonic_density": unit_normalized_horizontal_harmonic_density,
        },
        "canonical_projector_path": {
            "source_selected_color_norm": "I3^(0)=c_nil for canonical left-invariant horizontal harmonic one-form",
            "unit_L2_normalization_density": unit_normalized_horizontal_harmonic_density,
            "log_overlap": math.log(leading_su3_overlap),
            "negative_log_overlap": -math.log(leading_su3_overlap),
            "required_projector_log_jacobian_if_alone": pathway["projector_path"][
                "required_projector_log_jacobian_if_alone"
            ],
            "projector_closes_gap_from_selected_overlap": False,
            "reason_not_closed": "The selected leading overlap supplies c_nil, not the required determinant Jacobian exp(gap). A determinant Jacobian over additional quotient directions would require a separate selection theorem.",
        },
        "canonical_weitzenbock_path": {
            "orthonormal_structure_equation": "de^3 = -c_nil e^1 wedge e^2",
            "ricci_oneform_eigenvalues": ricci_oneform_eigenvalues,
            "rough_laplacian_on_harmonic_horizontal": rough_laplacian_on_harmonic_horizontal,
            "hodge_laplacian_on_harmonic_horizontal": hodge_laplacian_on_harmonic_horizontal,
            "curvature_loss_bound_Delta_curv": curvature_loss_bound,
            "bochner_identity_check_zero_mode": abs(hodge_laplacian_on_harmonic_horizontal) < 1e-12,
            "required_logdet_response_if_alone": required_gap,
            "selected_E_term_computed": True,
            "determinant_response_computed": False,
            "reason_not_closed": "The selected Ricci/Weitzenbock endomorphism is now identified, but its finite determinant response on the full BRST physical quotient is not obtained by equating it with f^2 or a Ricci bound.",
        },
        "diagnostic_comparison_to_gap": {
            "required_unweighted_Qa_gap": required_gap,
            "candidates": compared,
            "closest_geometry_diagnostic": {
                "name": closest_name,
                **compared[closest_name],
            },
        },
        "verdict": {
            "canonical_color_bundle_selected": True,
            "canonical_projector_overlap_computed": True,
            "canonical_weitzenbock_E_identified": True,
            "projector_path_closed": False,
            "endomorphism_path_closed": False,
            "numeric_electroweak_closure_certified": False,
            "selected_Qa_SU3_operator_closed": False,
            "next_required_artifact": "Selected_Qa_SU3_BRST_Physical_Determinant_With_Computed_Weitzenbock_E_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
