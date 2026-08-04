"""State-check the selected gauge-threshold heat-kernel theorem.

This is the operator-level gate after the conditional Casimir heat-coefficient
candidate.  It does not compute new electroweak data.  It checks whether the
available MTT/corpus ingredients are enough to promote the candidate weights
and finite stack determinants to a selected theorem.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HEAT_CERT = ROOT / "certificates" / "selected_physical_quotient_heat_coefficients_certificate.json"
LOCAL_DET_CERT = ROOT / "certificates" / "selected_local_determinant_computation_interface_certificate.json"
STACK_STATUS_CERT = ROOT / "certificates" / "selected_stack_determinant_source_status_certificate.json"
C1_CERT = ROOT / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    heat = load(HEAT_CERT)
    local_det = load(LOCAL_DET_CERT)
    stack_status = load(STACK_STATUS_CERT)
    c1 = load(C1_CERT)

    obligations = {
        "O1_selected_gauge_threshold_operator": {
            "required": "Gauge-factor-resolved Laplace-type threshold operators on Qa, Qc, and SU2 physical quotient sectors.",
            "current_status": "OPEN",
            "available_support": [
                "general MTT positive elliptic/Laplace-type smoothing operator",
                "selected local determinant computation interface",
            ],
            "missing": "actual selected gauge-fixed operator blocks, ghost treatment, bundle endomorphism terms, and domain/boundary conditions",
        },
        "O2_heat_trace_index_weights": {
            "required": "Derive Qa=3, Qc=1, SU2=2 or the corrected selected alternatives from the same operator.",
            "current_status": "CONDITIONAL_CANDIDATE",
            "available_support": heat["selected_physical_quotient_heat_coefficients"],
            "missing": "proof that the physical quotient trace reduces to these coefficients before electroweak comparison",
        },
        "O3_finite_stack_determinants": {
            "required": "Compute p_a, p_c, and p_SU2 as finite zeta/heat determinant parts in the selected threshold scheme.",
            "current_status": "OPEN",
            "available_support": {
                "determinant_interface_status": local_det["status"],
                "stack_source_status": stack_status["status"],
            },
            "missing": "selected full spectra or equivalent heat coefficients/finite parts for the three stacks",
        },
        "O4_retarded_kernel_c1_normalization": {
            "required": "Tie the determinant response to the selected C1 retarded-kernel derivative/normalization.",
            "current_status": "INTERFACE_BUILT_VALUES_OPEN",
            "available_support": {
                "c1_interface_status": c1["status"],
                "v1_tilde": c1["selected_values"]["v1_tilde"],
            },
            "missing": "selected derivative of the retarded overlap kernel acting on the gauge-threshold determinant source",
        },
    }

    theorem_closed = all(
        item["current_status"] == "CLOSED" for item in obligations.values()
    )

    output = {
        "status": "GAUGE_THRESHOLD_OPERATOR_HEAT_KERNEL_THEOREM_REDUCED_NOT_PROVED",
        "theorem_statement": (
            "If MTT supplies selected gauge-threshold Laplace-type operator "
            "blocks for Qa, Qc, and SU2, their physical quotient trace/index "
            "weights, their finite determinant parts, and the C1 retarded-kernel "
            "normalization from the same branch, then the electroweak "
            "hypercharge-normalized weak split is an executable no-knob theorem."
        ),
        "obligations": obligations,
        "current_numeric_candidate": {
            "heat_weighted_lambda_12": heat["hypercharge_accounting"]["lambda_12"],
            "heat_weighted_Delta_G_12": heat["hypercharge_accounting"]["Delta_G_12"],
            "residual_lambda_12": heat["diagnostic_comparison"]["residual_lambda_12"],
            "role": "conditional candidate only; not a selected prediction",
        },
        "verdict": {
            "operator_theorem_closed": theorem_closed,
            "general_heat_operator_language_available": True,
            "gauge_factor_resolved_operator_selected": False,
            "casimir_coefficients_derived_from_operator": False,
            "finite_stack_determinants_selected": False,
            "retarded_kernel_derivative_selected_for_threshold_source": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Selected_Qa_Qc_SU2_Gauge_Threshold_Operator_Blocks_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
