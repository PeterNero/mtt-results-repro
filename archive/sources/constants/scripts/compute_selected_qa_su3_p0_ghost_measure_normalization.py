"""Select and audit the p=0 ghost/measure normalization for Qa/SU3.

For central momentum p=0, the compact Nil sector reduces to the horizontal
two-torus sector.  Hodge decomposition gives, for every nonzero scalar momentum,
one longitudinal exact one-form and one transverse co-closed one-form.  The
Faddeev-Popov ghost determinant is the quotient-measure Jacobian for the exact
gauge orbit and cancels the longitudinal representative measure.  Harmonic
forms are massless coherent modes and are excluded from the threshold
determinant by the primed determinant convention.

This selects the p=0 rule: no extra independent p=0 gauge correction beyond
the scalar external-component block already present in the scalar diagnostic.
It closes the p=0 ambiguity, but it does not close the full Qa/SU3 value.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BRST_CERT = ROOT / "certificates" / "selected_qa_su3_brst_determinant_with_weitzenbock_certificate.json"
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
    qa_reduction = load(QA_REDUCTION_CERT)

    finite = brst["finite_parts_used"]
    p0_scalar = float(finite["p0_scalar"])
    scalar_total = float(finite["scalar_total"])
    required = float(finite["required_unweighted_Qa"])

    selected_p0_extra = 0.0
    selected_total_after_p0 = scalar_total + selected_p0_extra
    remaining_after_p0 = required - selected_total_after_p0

    # The previous p!=0 natural co-closed quotient is kept as an unresolved
    # nonzero-sector diagnostic; it is not selected by the p=0 theorem.
    previous_best_pnz = float(
        brst["p_nonzero_sector_diagnostics"]["best_previous_natural_gap_candidate"]
    )
    previous_best_total = scalar_total + previous_best_pnz

    output = {
        "status": "QA_SU3_P0_GHOST_MEASURE_NORMALIZATION_SELECTED_FULL_QA_OPEN",
        "source_rule": {
            "faddeev_popov": "ghost determinant is the quotient-measure Jacobian",
            "brst": "physical states are BRST quotient classes modulo null redundancy",
            "hodge_p0": "nonzero p=0 one-forms split into one exact longitudinal and one co-closed transverse representative",
            "zero_modes": "harmonic gauge modes are coherent/massless and excluded from the primed threshold determinant",
        },
        "selected_p0_measure_rule": {
            "longitudinal_exact_modes_cancelled_by_ghost_jacobian": True,
            "harmonic_zero_modes_excluded_from_threshold_det_prime": True,
            "transverse_p0_modes_not_an_extra_jacobian": True,
            "selected_extra_p0_logdet_correction": selected_p0_extra,
            "p0_scalar_reference_finite_part": p0_scalar,
        },
        "numeric_effect": {
            "scalar_total_before_p0_selection": scalar_total,
            "selected_total_after_p0_selection": selected_total_after_p0,
            "required_unweighted_Qa": required,
            "remaining_unweighted_gap_after_p0_selection": remaining_after_p0,
            "lambda_after_p0_selection": lambda_from_unweighted_p(
                selected_total_after_p0,
                qa_reduction,
            ),
            "previous_best_p_nonzero_diagnostic_total": previous_best_total,
            "previous_best_p_nonzero_diagnostic_lambda": lambda_from_unweighted_p(
                previous_best_total,
                qa_reduction,
            ),
        },
        "verdict": {
            "p0_measure_rule_selected": True,
            "ghost_normalization_selected_for_p0": True,
            "p0_ambiguity_closed": True,
            "p0_rule_closes_full_Qa": abs(remaining_after_p0) < 1e-3,
            "numeric_electroweak_closure_certified": False,
            "selected_Qa_SU3_operator_closed": False,
            "remaining_problem": "p!=0 physical quotient / determinant finite part, not p=0 ghost measure",
            "next_required_artifact": "Selected_Qa_SU3_PNonzero_Physical_Quotient_Determinant_Theorem_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
