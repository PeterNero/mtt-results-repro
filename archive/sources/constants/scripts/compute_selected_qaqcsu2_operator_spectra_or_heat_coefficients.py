"""Assemble the current Qa/Qc/SU2 spectrum-or-heat-coefficient gate.

This gate carries forward the best available non-fitted data for each
gauge-threshold operator block:

* Qc: exact circle scalar-proxy zeta determinant.
* SU2: exact effective sphere zeta determinant, now selected for weak-split
  accounting after flat-background and flat-FP quotient-policy closure.
* Qa: diagnostic SU3/Nil finite-part proxy.

It then applies the conditional Casimir heat coefficients already audited.
The result is a concrete candidate table, not a selected electroweak theorem.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXACT_CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
STACK_TABLE = ROOT / "scripts" / "compute_stack_determinant_candidate_table.py"
BLOCK_CERT = ROOT / "certificates" / "selected_qaqcsu2_gauge_threshold_operator_blocks_certificate.json"
HEAT_CERT = ROOT / "certificates" / "selected_physical_quotient_heat_coefficients_certificate.json"
QC_CERT = ROOT / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json"
SU2_FP_POLICY_CERT = ROOT / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json"


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


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    exact = run_json(EXACT_CIRCLE_SPHERE)
    stack = run_json(STACK_TABLE)
    block_cert = load(BLOCK_CERT)
    heat_cert = load(HEAT_CERT)
    qc_cert = load(QC_CERT)
    su2_policy_cert = load(SU2_FP_POLICY_CERT)

    coeffs = {
        "D_Qa": float(
            block_cert["operator_blocks"]["D_Qa"]["trace_and_representation"]["heat_coefficient_candidate"]
        ),
        "D_Qc": float(
            block_cert["operator_blocks"]["D_Qc"]["trace_and_representation"]["heat_coefficient_candidate"]
        ),
        "D_SU2": float(
            block_cert["operator_blocks"]["D_SU2"]["trace_and_representation"]["heat_coefficient_candidate"]
        ),
    }
    unweighted = {
        "D_Qa": float(stack["candidate_table"]["Qa_SU3_stack"]["value"]),
        "D_Qc": float(exact["finite_parts"]["U1_circle"]),
        "D_SU2": float(exact["finite_parts"]["SU2_effective_sphere"]),
    }
    weighted = {name: unweighted[name] * coeffs[name] for name in unweighted}

    block_status = {
        "D_Qa": {
            "spectrum_or_heat_data_status": "DIAGNOSTIC_SU3_NIL_PROXY_NOT_SELECTED",
            "available_formula": "finite-part estimator from proxy SU3/Nil spectral-table cutoffs",
            "unweighted_finite_part": unweighted["D_Qa"],
            "heat_coefficient_candidate": coeffs["D_Qa"],
            "heat_weighted_finite_part_candidate": weighted["D_Qa"],
            "missing_for_selection": [
                "exact compact Nil p!=0 spectrum or heat coefficients",
                "selected gauge-threshold operator rather than scalar proxy",
                "topology-certified index weights",
                "analytic zeta/heat finite part instead of fitted cutoff constant",
            ],
        },
        "D_Qc": {
            "spectrum_or_heat_data_status": "SELECTED_QC_CIRCLE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT",
            "available_formula": exact["closed_formulas"]["U1_circle"],
            "unweighted_finite_part": float(qc_cert["selected_values"]["unweighted_p_Qc"]),
            "heat_coefficient_candidate": coeffs["D_Qc"],
            "heat_weighted_finite_part_candidate": float(qc_cert["selected_values"]["selected_p_Qc_for_weak_split"]),
            "missing_for_selection": [
                "absolute universal determinant normalization, irrelevant to lambda_12",
            ],
        },
        "D_SU2": {
            "spectrum_or_heat_data_status": "SELECTED_SU2_SPHERE_GAUGE_BLOCK_ZETA_CLOSED_FOR_WEAK_SPLIT",
            "available_formula": exact["closed_formulas"]["SU2_effective_sphere"],
            "unweighted_finite_part": su2_policy_cert["selected_flat_su2_data"]["p_scalar"],
            "heat_coefficient_candidate": coeffs["D_SU2"],
            "heat_weighted_finite_part_candidate": su2_policy_cert["selected_flat_su2_data"][
                "selected_p_SU2_for_weak_split"
            ],
            "missing_for_selection": [
                "absolute partition-function/vacuum normalization, irrelevant to lambda_12",
            ],
        },
    }

    p_su2_selected = float(su2_policy_cert["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"])
    p_y = weighted["D_Qa"] / 36.0 + weighted["D_Qc"] / 4.0
    lambda_12 = p_y - p_su2_selected
    target_lambda = float(heat_cert["diagnostic_comparison"]["target_lambda_12"])

    output = {
        "status": "QA_QC_SU2_SPECTRA_HEAT_CANDIDATE_TABLE_BUILT_SELECTION_OPEN",
        "block_status": block_status,
        "candidate_hypercharge_accounting": {
            "p_a_candidate": weighted["D_Qa"],
            "p_c_candidate": weighted["D_Qc"],
            "p_SU2_candidate": p_su2_selected,
            "p_Y_candidate": p_y,
            "lambda_12_candidate": lambda_12,
            "target_lambda_12_diagnostic_only": target_lambda,
            "residual_lambda_12_diagnostic_only": lambda_12 - target_lambda,
        },
        "selection_status_summary": {
            "D_Qa_exact_selected": False,
            "D_Qc_exact_scalar_proxy": True,
            "D_Qc_selected_gauge_block": True,
            "D_Qc_selected_scope": "weak-split accounting",
            "D_SU2_exact_scalar_proxy": True,
            "D_SU2_selected_gauge_block": True,
            "D_SU2_selected_scope": "weak-split accounting",
            "all_three_selected_for_physical_quotient": False,
        },
        "verdict": {
            "candidate_table_built": True,
            "exact_scalar_proxy_pieces_carried_forward": True,
            "qc_gauge_block_closed_for_weak_split": True,
            "su2_gauge_block_closed_for_weak_split": True,
            "su3_nil_selected_spectrum_closed": False,
            "selected_gauge_operator_spectra_closed": False,
            "finite_determinants_closed_in_selected_physical_quotient": False,
            "numeric_electroweak_closure": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Exact_Selected_Nil_or_Gauge_Threshold_Heat_Coefficients_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
