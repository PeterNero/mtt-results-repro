"""Compute the remaining Qa/SU3 gauge-quotient gap after scalar Nil zeta."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCALAR_CERT = ROOT / "certificates" / "compact_nil_scalar_hurwitz_zeta_candidate_certificate.json"
QA_REDUCTION_CERT = ROOT / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    scalar = load(SCALAR_CERT)
    qa = load(QA_REDUCTION_CERT)

    required_unweighted = float(
        qa["exact_required_Qa_after_Qc_SU2_closure"]["unweighted_p_a_required_if_CA_SU3_is_3"]
    )
    scalar_unweighted = float(scalar["central_window_result"]["total_scalar_finite_logdet_candidate"])
    unweighted_gap = required_unweighted - scalar_unweighted
    heat_gap = 3.0 * unweighted_gap
    lambda_gap = heat_gap / 36.0

    output = {
        "status": "QA_SU3_GAUGE_QUOTIENT_GAP_COMPUTED_OPERATOR_OPEN",
        "inputs": {
            "required_unweighted_Qa": required_unweighted,
            "scalar_hurwitz_unweighted_Qa_candidate": scalar_unweighted,
            "scalar_candidate_lambda_12": scalar["central_window_result"]["hypercharge_if_used_for_Qa"][
                "lambda_12_candidate"
            ],
            "target_lambda_12": scalar["central_window_result"]["hypercharge_if_used_for_Qa"][
                "target_lambda_12"
            ],
        },
        "computed_gap": {
            "formula": "q_gap = p_a_required_unweighted - p_a_scalar_hurwitz",
            "unweighted_Qa_gap": unweighted_gap,
            "heat_weighted_Qa_gap": heat_gap,
            "lambda_12_gap": lambda_gap,
        },
        "candidate_sources_to_test": [
            "co-closed one-form gauge fluctuation determinant on compact Nil",
            "exact BRST ghost quotient relative to scalar external-component block",
            "physical coherent-sector projection onto the SU3 massless color harmonic",
            "bundle curvature or Weitzenbock endomorphism term for the selected gauge block",
        ],
        "forbidden_shortcuts": [
            "adding the gap as a counterterm",
            "choosing a multiplicity or subtraction constant to hit lambda_12",
            "using the observed weak mixing angle to select the quotient",
        ],
        "verdict": {
            "gap_computed": True,
            "gap_selected": False,
            "scalar_near_miss_confirmed": True,
            "selected_Qa_SU3_operator_closed": False,
            "numeric_electroweak_closure_certified": False,
            "next_required_artifact": "Selected_Qa_SU3_Gauge_Block_Quotient_Operator_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
