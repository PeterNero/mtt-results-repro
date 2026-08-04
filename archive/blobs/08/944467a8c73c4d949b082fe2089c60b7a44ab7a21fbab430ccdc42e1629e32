"""Evaluate the Qa/SU3 BRST determinant after identifying Weitzenbock E.

The key point is that the sourced co-closed one-form spectrum is a Hodge
one-form spectrum, so its eigenvalues already include the Ricci/Weitzenbock
endomorphism.  Therefore the computed E term is not an additional tunable shift.

This script builds the currently justified determinant bookkeeping table:

* scalar external-component proxy,
* sourced p != 0 co-closed Hodge one-form determinant,
* p=0 transverse two-torus quotient diagnostics,
* ghost/scalar quotient candidates.

It records the strongest selected conclusion: E has been included, but the full
BRST physical determinant still requires a source-selected p=0/zero-mode
measure and ghost normalization rule.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCALAR_CERT = ROOT / "certificates" / "compact_nil_scalar_hurwitz_zeta_candidate_certificate.json"
QUOTIENT_CERT = (
    ROOT / "certificates" / "selected_qa_su3_gauge_block_quotient_operator_certificate.json"
)
GAP_CERT = ROOT / "certificates" / "selected_qa_su3_gauge_quotient_gap_certificate.json"
WEITZ_CERT = ROOT / "certificates" / "selected_qa_su3_canonical_bundle_weitzenbock_certificate.json"
QA_REDUCTION_CERT = ROOT / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def compare(value: float, target: float) -> dict[str, float]:
    return {
        "value": value,
        "difference_from_required": value - target,
        "absolute_difference_from_required": abs(value - target),
    }


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
    scalar = load(SCALAR_CERT)
    quotient = load(QUOTIENT_CERT)
    gap = load(GAP_CERT)
    weitz = load(WEITZ_CERT)
    qa_reduction = load(QA_REDUCTION_CERT)

    central = scalar["central_window_result"]
    p0_scalar = float(central["p0_finite_logdet_part"])
    pnz_scalar = float(central["p_nonzero_finite_logdet_part"])
    scalar_total = float(central["total_scalar_finite_logdet_candidate"])

    finite = quotient["finite_parts"]
    pnz_coclosed_oneform = float(finite["p_nonzero_co_closed_oneform_logdet"])
    lowest_scalar_mode = float(finite["lowest_scalar_mode_logdet"])
    best_natural_gap = float(quotient["best_natural_candidate"]["value"])

    required_total = float(
        qa_reduction["exact_required_Qa_after_Qc_SU2_closure"][
            "unweighted_p_a_required_if_CA_SU3_is_3"
        ]
    )
    required_gap = float(gap["computed_gap"]["unweighted_Qa_gap"])

    # p=0 diagnostics.  For central momentum zero, the horizontal co-closed
    # quotient on the two-torus has one transverse representative per nonzero
    # scalar mode, so its determinant finite part equals the scalar p0 finite
    # part.  The BRST ghost subtraction can cancel this sector, preserve it, or
    # leave a half-density depending on the selected measure.  The corpus does
    # not yet select among those options.
    p0_diagnostics = {
        "p0_transverse_equals_scalar": p0_scalar,
        "p0_transverse_minus_ghost_scalar": 0.0,
        "p0_half_density_transverse": 0.5 * p0_scalar,
        "p0_remove_harmonic_only": p0_scalar,
    }

    pnz_diagnostics = {
        "p_nonzero_coclosed_oneform": pnz_coclosed_oneform,
        "p_nonzero_coclosed_minus_scalar": pnz_coclosed_oneform - pnz_scalar,
        "p_nonzero_scalar_minus_half_coclosed": pnz_scalar - 0.5 * pnz_coclosed_oneform,
        "best_previous_natural_gap_candidate": best_natural_gap,
    }

    # Combine the selected scalar external block with p!=0 quotient diagnostics
    # and possible p=0 treatments.  These are bookkeeping candidates only.
    candidate_totals: dict[str, float] = {
        "scalar_proxy_only": scalar_total,
        "scalar_plus_best_previous_natural_gap": scalar_total + best_natural_gap,
        "scalar_plus_required_gap_for_reference_forbidden": scalar_total + required_gap,
    }
    for p0_name, p0_value in p0_diagnostics.items():
        for pnz_name, pnz_value in pnz_diagnostics.items():
            candidate_totals[f"{p0_name}__{pnz_name}"] = p0_value + pnz_value

    compared_totals = {
        name: {
            **compare(value, required_total),
            **lambda_from_unweighted_p(value, qa_reduction),
        }
        for name, value in candidate_totals.items()
    }
    closest_name = min(
        (
            name
            for name in compared_totals
            if name != "scalar_plus_required_gap_for_reference_forbidden"
        ),
        key=lambda name: compared_totals[name]["absolute_difference_from_required"],
    )

    output = {
        "status": "QA_SU3_BRST_DETERMINANT_WITH_WEITZENBOCK_E_EVALUATED_CLOSURE_OPEN",
        "input_statuses": {
            "scalar_status": scalar["status"],
            "quotient_status": quotient["status"],
            "weitzenbock_status": weitz["status"],
        },
        "selected_weitzenbock_inclusion": {
            "E_term_identified": True,
            "E_is_already_in_sourced_hodge_oneform_spectrum": True,
            "do_not_add_E_again_as_shift": True,
            "ricci_oneform_eigenvalues": weitz["canonical_weitzenbock_path"][
                "ricci_oneform_eigenvalues"
            ],
            "hodge_zero_mode_cancellation": weitz["canonical_weitzenbock_path"][
                "bochner_identity_check_zero_mode"
            ],
        },
        "finite_parts_used": {
            "p0_scalar": p0_scalar,
            "p_nonzero_scalar": pnz_scalar,
            "scalar_total": scalar_total,
            "p_nonzero_coclosed_hodge_oneform": pnz_coclosed_oneform,
            "lowest_scalar_mode": lowest_scalar_mode,
            "required_unweighted_Qa": required_total,
            "required_gap_over_scalar": required_gap,
        },
        "p0_sector_diagnostics": p0_diagnostics,
        "p_nonzero_sector_diagnostics": pnz_diagnostics,
        "candidate_total_comparison": compared_totals,
        "closest_unforbidden_candidate": {
            "name": closest_name,
            **compared_totals[closest_name],
        },
        "forbidden_reference": {
            "name": "scalar_plus_required_gap_for_reference_forbidden",
            **compared_totals["scalar_plus_required_gap_for_reference_forbidden"],
            "reason_forbidden": "This inserts the target residual rather than selecting a BRST quotient.",
        },
        "verdict": {
            "computed_E_included_without_double_counting": True,
            "full_BRST_candidate_table_built": True,
            "any_unforbidden_candidate_closes_required_Qa": compared_totals[closest_name][
                "absolute_difference_from_required"
            ]
            < 1e-3,
            "selected_p0_measure_rule_available": False,
            "selected_ghost_normalization_available": False,
            "numeric_electroweak_closure_certified": False,
            "selected_Qa_SU3_operator_closed": False,
            "next_required_artifact": "Selected_Qa_SU3_P0_Ghost_Measure_Normalization_Theorem_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
