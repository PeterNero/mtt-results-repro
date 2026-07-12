"""Finalize the Qa/SU3 compact-Nil Hodge branch status.

At this point the compact-Nil scalar spectrum, Weitzenbock term, p=0 ghost
measure, and p!=0 BRST physical quotient have all been selected or computed.
The branch overshoots the exact weak-split requirement by a finite lowest-mode
excess.

This script records whether the current corpus supplies a selected
projector/Jacobian that removes that excess.  It intentionally does not create
one by target matching.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PNZ_CERT = ROOT / "certificates" / "selected_qa_su3_pnonzero_physical_quotient_determinant_certificate.json"
PATH_CERT = ROOT / "certificates" / "selected_qa_su3_projector_endomorphism_pathways_certificate.json"
WEITZ_CERT = ROOT / "certificates" / "selected_qa_su3_canonical_bundle_weitzenbock_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    pnz = load(PNZ_CERT)
    pathway = load(PATH_CERT)
    weitz = load(WEITZ_CERT)

    selected = pnz["numeric_effect"]
    selected_qa = float(selected["selected_unweighted_Qa"])
    required_qa = float(selected["required_unweighted_Qa"])
    excess = selected_qa - required_qa
    selected_lambda = selected["selected_lambda_12"]
    lambda_excess = float(selected_lambda["residual_lambda_12"])

    c_nil = float(weitz["selected_geometry"]["c_nil"])
    candidate_projector_factor = math.exp(-excess)
    candidate_projector_per_color = math.exp(-excess / 3.0)

    output = {
        "status": "QA_SU3_COMPACT_NIL_HODGE_BRANCH_OBSTRUCTED_PROJECTOR_RESOLUTION_OPEN",
        "computed_branch": {
            "scalar_spectrum_computed": True,
            "weitzenbock_E_identified_and_not_double_counted": True,
            "p0_ghost_measure_selected": True,
            "pnonzero_BRST_physical_quotient_selected": True,
            "selected_unweighted_Qa": selected_qa,
            "required_unweighted_Qa": required_qa,
            "excess_selected_minus_required": excess,
            "selected_lambda_12": float(selected_lambda["lambda_12_candidate"]),
            "target_lambda_12": float(selected_lambda["target_lambda_12"]),
            "lambda_12_excess": lambda_excess,
        },
        "projector_resolution_test": {
            "needed_log_projector_jacobian_to_close": -excess,
            "needed_multiplicative_projector_factor": candidate_projector_factor,
            "needed_factor_per_color_dimension_if_split_equally": candidate_projector_per_color,
            "current_corpus_selects_this_projector": False,
            "reason_not_selected": "The corpus supplies unit L2 harmonic/projector normalization and quotient-measure rules, but no selected finite coherent projector/Jacobian equal to the lowest-mode excess.",
            "earlier_projector_gate_status": pathway["status"],
        },
        "structural_diagnostics": {
            "c_nil": c_nil,
            "minus_log_c_nil": -math.log(c_nil),
            "minus_3_log_c_nil": -3.0 * math.log(c_nil),
            "lowest_mode_excess": excess,
            "excess_minus_minus_log_c_nil": excess - (-math.log(c_nil)),
            "interpretation": "The excess is near but not equal to simple selected Nil volume factors; near-numerology is not a selection theorem.",
        },
        "verdict": {
            "compact_nil_hodge_branch_fully_computed": True,
            "compact_nil_hodge_branch_closes_Qa_SU3": False,
            "selected_projector_jacobian_available": False,
            "target_fitting_used": False,
            "branch_status": "OBSTRUCTED_AS_FINAL_NO_KNOB_QA_SU3_CLOSURE",
            "allowed_next_paths": [
                "derive a source-selected finite coherent projector/Jacobian before comparing to the target",
                "replace the Qa/SU3 threshold operator with another corpus-selected operator and recompute",
                "treat the compact-Nil Hodge branch as a near-miss diagnostic, not the final proof source",
            ],
            "next_required_artifact": "Selected_Qa_SU3_Alternative_Operator_or_Projector_Source_Hunt_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
