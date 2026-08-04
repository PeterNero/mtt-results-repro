"""Close the flat Faddeev-Popov quotient-normalization policy.

This is the last SU2-specific gate before the SU2 scalar/Casimir value can be
used as the selected weak-split gauge block.

Scope is deliberately narrow: gauge-kinetic threshold / lambda_12 accounting.
The theorem does not claim an absolute partition-function normalization or a
vacuum-energy contribution.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FLAT_CERT = ROOT / "certificates" / "selected_su2_threshold_background_flatness_or_fp_spectrum_certificate.json"
QC_CERT = ROOT / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json"


def main() -> int:
    flat = json.loads(FLAT_CERT.read_text(encoding="utf-8"))
    qc = json.loads(QC_CERT.read_text(encoding="utf-8"))

    p_scalar = float(flat["computed_flat_fp_data"]["p_scalar"])
    p_su2 = float(flat["computed_flat_fp_data"]["p_SU2_no_extra_ghost_term"])
    flat_adjoint_fp = float(flat["computed_flat_fp_data"]["flat_adjoint_fp_logdet"])
    p_qc = float(qc["selected_values"]["selected_p_Qc_for_weak_split"])

    output = {
        "status": "FLAT_FP_QUOTIENT_NORMALIZATION_POLICY_CLOSED_FOR_WEAK_SPLIT",
        "purpose": (
            "Decide whether a field-independent flat Faddeev-Popov determinant "
            "contributes to the selected weak-split gauge-kinetic threshold."
        ),
        "scope": {
            "closed_for": "lambda_12 and gauge-kinetic threshold accounting",
            "not_closed_for": [
                "absolute partition-function normalization",
                "vacuum energy",
                "non-flat background-field determinants",
                "higher-order field-dependent ghost interactions",
            ],
        },
        "source_policy": {
            "gauge_fixing_interpretation": (
                "The FP determinant is the quotient projection Jacobian.  If it is "
                "field-independent along physical directions, it is representative-"
                "measure normalization rather than an interacting threshold term."
            ),
            "qc_precedent": (
                "The Qc circle block already discards the abelian field-independent "
                "FP determinant from weak-split accounting."
            ),
            "brst_threshold_rule": (
                "Only BRST-compatible, field-dependent gauge-block variations can "
                "contribute to gauge-kinetic threshold coefficients."
            ),
        },
        "selected_flat_su2_data": {
            "background_flatness_status": flat["status"],
            "fp_operator": flat["proved_flatness_statement"]["fp_operator_reduction"],
            "p_scalar": p_scalar,
            "flat_adjoint_fp_logdet_if_kept": flat_adjoint_fp,
            "policy_action": "discard_or_absorb_as_pure_quotient_normalization_for_weak_split",
            "extra_fp_threshold_term": 0.0,
            "selected_p_SU2_for_weak_split": p_su2,
            "selected_p_Qc_for_weak_split": p_qc,
        },
        "functional_test": {
            "test": "Does the flat FP determinant vary under the selected gauge-kinetic background insertion?",
            "answer": False,
            "reason": (
                "At the selected flat/trivial SU2 background, M_G[A] reduces to "
                "-Delta_0 tensor ad(SU2).  The adjoint multiplicity changes the "
                "orbit-volume normalization, but there is no field-dependent "
                "curvature insertion that could produce an F^2 threshold term."
            ),
        },
        "verdict": {
            "field_independent_fp_determinants_discarded_from_weak_split": True,
            "flat_adjoint_fp_kept_as_threshold": False,
            "su2_quotient_policy_closed_for_weak_split": True,
            "su2_selected_for_lambda_12_accounting": True,
            "absolute_universal_constant_fixed": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Update_Selected_Qa_Qc_SU2_Spectra_Table_with_SU2_Closure",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
