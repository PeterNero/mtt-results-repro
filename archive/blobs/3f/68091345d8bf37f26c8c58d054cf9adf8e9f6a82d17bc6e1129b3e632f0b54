"""Compute the selected p!=0 BRST physical quotient determinant for Qa/SU3.

For nonzero central momentum the Nil Hodge complex has no harmonic zero modes:
the scalar ghost/exact sector is acyclic.  The selected BRST rule is therefore:

* exact longitudinal one-form modes are quotient representatives,
* scalar ghosts encode the Faddeev-Popov quotient Jacobian,
* the physical bosonic sector is the co-closed one-form block,
* Gaussian bosonic determinants enter with half-density weight.

Relative to the scalar external-component diagnostic already used in the Qa
reduction, this gives the finite p!=0 quotient response

    p_selected = p_scalar - 1/2 p_coclosed_oneform.

The sourced co-closed spectrum implies this equals the finite part of the
lowest scalar oscillator mode.  This script computes the selected value and
checks whether it closes the exact Qa/SU3 requirement.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BRST_CERT = ROOT / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json"
P0_CERT = ROOT / "certificates" / "selected_qa_su3_p0_ghost_measure_normalization_certificate.json"
QUOTIENT_CERT = (
    ROOT / "certificates" / "selected_qa_su3_gauge_block_quotient_operator_certificate.json"
)
QA_REDUCTION_CERT = ROOT / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def lambda_from_unweighted_p(p_unweighted: float, qa_reduction: dict[str, Any]) -> dict[str, float]:
    selected = qa_reduction["selected_inputs"]
    p_c = float(selected["p_Qc_selected"])
    p_su2 = float(selected["p_SU2_selected"])
    target = float(selected["target_lambda_12_diagnostic"])
    heat_weighted = 3.0 * p_unweighted
    lambda_12 = heat_weighted / 36.0 + p_c / 4.0 - p_su2
    return {
        "unweighted_p_a": p_unweighted,
        "heat_weighted_p_a": heat_weighted,
        "lambda_12_candidate": lambda_12,
        "target_lambda_12": target,
        "residual_lambda_12": lambda_12 - target,
        "absolute_residual_lambda_12": abs(lambda_12 - target),
    }


def main() -> int:
    brst = load(BRST_CERT)
    p0 = load(P0_CERT)
    quotient = load(QUOTIENT_CERT)
    qa_reduction = load(QA_REDUCTION_CERT)

    finite = brst["finite_parts_used"]
    scalar_total = float(finite["scalar_total"])
    p_nonzero_scalar = float(finite["p_nonzero_scalar"])
    p_nonzero_coclosed = float(finite["p_nonzero_coclosed_hodge_oneform"])
    required = float(finite["required_unweighted_Qa"])
    required_gap = float(finite["required_gap_over_scalar"])
    p0_extra = float(
        p0["selected_p0_measure_rule"]["selected_extra_p0_logdet_correction"]
    )

    selected_pnonzero_response = p_nonzero_scalar - 0.5 * p_nonzero_coclosed
    identity_lowest_mode = float(quotient["finite_parts"]["lowest_scalar_mode_logdet"])
    selected_total = scalar_total + p0_extra + selected_pnonzero_response
    remaining = required - selected_total

    output = {
        "status": "QA_SU3_PNONZERO_PHYSICAL_QUOTIENT_DETERMINANT_SELECTED_NOT_FULL_CLOSURE",
        "selected_rule": {
            "nonzero_central_hodge_complex_acyclic": True,
            "longitudinal_exact_modes_cancelled_by_scalar_ghosts": True,
            "co_closed_oneform_block_is_physical_bosonic_block": True,
            "bosonic_half_density_weight": 0.5,
            "relative_response_formula": "p_nonzero_scalar - 1/2 p_nonzero_coclosed_oneform",
        },
        "finite_parts": {
            "scalar_total_before_p0_and_pnonzero_response": scalar_total,
            "selected_p0_extra": p0_extra,
            "p_nonzero_scalar": p_nonzero_scalar,
            "p_nonzero_coclosed_hodge_oneform": p_nonzero_coclosed,
            "selected_pnonzero_physical_quotient_response": selected_pnonzero_response,
            "identity_lowest_scalar_mode_logdet": identity_lowest_mode,
            "identity_difference": selected_pnonzero_response - identity_lowest_mode,
            "required_gap_over_scalar": required_gap,
        },
        "numeric_effect": {
            "selected_unweighted_Qa": selected_total,
            "required_unweighted_Qa": required,
            "remaining_unweighted_difference_required_minus_selected": remaining,
            "selected_lambda_12": lambda_from_unweighted_p(selected_total, qa_reduction),
        },
        "comparison": {
            "selected_response_minus_required_gap": selected_pnonzero_response
            - required_gap,
            "absolute_response_gap_miss": abs(selected_pnonzero_response - required_gap),
            "interpretation": "The selected acyclic p!=0 BRST quotient overshoots the exact required gap; therefore the current compact-Nil Hodge quotient does not by itself close Qa/SU3.",
        },
        "verdict": {
            "pnonzero_physical_quotient_rule_selected": True,
            "pnonzero_determinant_response_computed": True,
            "p0_and_pnonzero_quotients_both_selected": True,
            "selected_Qa_SU3_operator_closed": abs(remaining) < 1e-3,
            "numeric_electroweak_closure_certified": False,
            "remaining_problem": "The selected compact-Nil Hodge/BRST quotient overshoots by the lowest-mode excess; closure requires either a source-selected additional finite coherent projector/Jacobian or a different selected Qa/SU3 operator, not a p0 or Weitzenbock adjustment.",
            "next_required_artifact": "Selected_Qa_SU3_Final_Obstruction_or_Projector_Jacobian_Resolution_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
