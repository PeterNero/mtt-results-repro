"""Evaluate the two remaining Qa/SU3 closure pathways.

This is a gate computation, not a proof of closure.  It compares the exact
residual determinant gap with:

1. a physical coherent-sector projector/Jacobian route, and
2. a curvature/Weitzenbock endomorphism route.

The script deliberately rejects target-selected corrections.  A candidate only
closes the branch if it is already selected by the MTT operator data.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GAP_CERT = ROOT / "certificates" / "selected_qa_su3_gauge_quotient_gap_certificate.json"
QUOTIENT_CERT = (
    ROOT / "certificates" / "selected_qa_su3_gauge_block_quotient_operator_certificate.json"
)
SPECTRUM_CERT = ROOT / "certificates" / "sourced_compact_nil_scalar_spectrum_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def compare(value: float, target: float) -> dict[str, float]:
    return {
        "value": value,
        "difference_from_required_gap": value - target,
        "absolute_difference_from_required_gap": abs(value - target),
    }


def main() -> int:
    gap = load(GAP_CERT)
    quotient = load(QUOTIENT_CERT)
    spectrum = load(SPECTRUM_CERT)

    required_gap = float(gap["computed_gap"]["unweighted_Qa_gap"])
    lambda_gap = float(gap["computed_gap"]["lambda_12_gap"])
    c_nil = float(spectrum["selected_geometry_map"]["r_central"])
    f_struct = float(spectrum["selected_geometry_map"]["f_struct"])
    best_quotient = float(quotient["best_natural_candidate"]["value"])
    quotient_excess = best_quotient - required_gap

    required_projector_factor = math.exp(required_gap)
    required_projector_factor_per_color = math.exp(required_gap / 3.0)
    required_endomorphism_log_response = required_gap

    nil_factor_candidates = {
        "unit_L2_projector_no_extra_jacobian": 0.0,
        "minus_log_c_nil": -math.log(c_nil),
        "minus_2_log_c_nil": -2.0 * math.log(c_nil),
        "minus_3_log_c_nil": -3.0 * math.log(c_nil),
        "log_1_plus_f_squared": math.log(1.0 + f_struct * f_struct),
        "half_f_squared": 0.5 * f_struct * f_struct,
        "f_squared": f_struct * f_struct,
        "best_coclosed_quotient_candidate": best_quotient,
    }
    compared_nil_factors = {
        name: compare(value, required_gap) for name, value in nil_factor_candidates.items()
    }
    closest_nil_factor_name = min(
        compared_nil_factors,
        key=lambda name: compared_nil_factors[name]["absolute_difference_from_required_gap"],
    )

    output = {
        "status": "QA_SU3_PROJECTOR_ENDOMORPHISM_PATHS_EVALUATED_CLOSURE_OPEN",
        "inputs": {
            "required_unweighted_Qa_gap": required_gap,
            "lambda_12_gap": lambda_gap,
            "c_nil": c_nil,
            "f_struct": f_struct,
            "best_coclosed_quotient_candidate": best_quotient,
            "best_coclosed_quotient_excess": quotient_excess,
        },
        "projector_path": {
            "corpus_rule": "filter after quotienting, or filter covariantly before quotienting; preserve physical/BRST gauge content",
            "unit_L2_harmonic_projector_logdet_gap": 0.0,
            "reason_unit_L2_alone_is_insufficient": "A normalized idempotent projector selects the physical subspace but supplies no determinant finite part unless a nontrivial selected projector Jacobian or fiber norm is computed.",
            "required_projector_log_jacobian_if_alone": required_gap,
            "required_projector_multiplicative_factor_if_alone": required_projector_factor,
            "required_factor_per_color_dimension_if_split_equally": required_projector_factor_per_color,
            "route_b_completion_condition": "specify the canonical twistor/color bundle and compute the L2 harmonic norm directly on that bundle",
            "selected_by_current_corpus": False,
        },
        "endomorphism_path": {
            "operator_form": "D_Qa = -(connection Laplacian on physical SU3 gauge content) + E_Qa",
            "required_logdet_response_if_alone": required_endomorphism_log_response,
            "required_heat_weighted_response_if_alone": gap["computed_gap"]["heat_weighted_Qa_gap"],
            "reason_not_closed": "The corpus requires the bundle representation, connection, ghost/subtraction rule, and Weitzenbock/curvature endomorphism before E_Qa can be evaluated.",
            "selected_constant_shift_available": False,
            "forbidden_move": "choosing E_Qa or a scalar curvature coefficient only to reproduce the residual gap",
        },
        "structural_factor_scan": {
            "purpose": "diagnostic only; these values are not closure unless independently selected by the operator construction",
            "candidates": compared_nil_factors,
            "closest_candidate": {
                "name": closest_nil_factor_name,
                **compared_nil_factors[closest_nil_factor_name],
            },
        },
        "verdict": {
            "both_paths_evaluated": True,
            "unit_L2_projector_alone_closes_gap": False,
            "projector_path_requires_new_selected_norm_or_jacobian": True,
            "endomorphism_path_requires_selected_weitzenbock_term": True,
            "tempting_nil_volume_factor_is_not_selected": True,
            "numeric_electroweak_closure_certified": False,
            "selected_Qa_SU3_operator_closed": False,
            "next_required_artifact": "Selected_Qa_SU3_Canonical_Twistor_Bundle_Projector_or_Weitzenbock_E_Term_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
