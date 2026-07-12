"""Reduce the SU2 sphere gauge-block equivalence gate.

Unlike Qc, SU2 is non-abelian.  The gauge-fixing corpus says the
Faddeev-Popov determinant is field-dependent for non-abelian Yang-Mills
operators, so the exact scalar sphere zeta determinant cannot by itself be
promoted to the selected gauge-threshold determinant.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXACT_CIRCLE_SPHERE = ROOT / "scripts" / "compute_exact_circle_sphere_zeta.py"
BLOCK_CERT = ROOT / "certificates" / "selected_qaqcsu2_gauge_threshold_operator_blocks_certificate.json"
U1_SU2_CERT = ROOT / "certificates" / "u1_su2_operator_weight_candidate_gate_certificate.json"


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


def main() -> int:
    exact = run_json(EXACT_CIRCLE_SPHERE)
    block = json.loads(BLOCK_CERT.read_text(encoding="utf-8"))
    u1_su2 = json.loads(U1_SU2_CERT.read_text(encoding="utf-8"))

    p_su2_scalar = float(exact["finite_parts"]["SU2_effective_sphere"])
    heat_weight = float(
        block["operator_blocks"]["D_SU2"]["trace_and_representation"]["heat_coefficient_candidate"]
    )
    weighted_candidate = p_su2_scalar * heat_weight
    de_rham = next(
        item
        for item in u1_su2["candidate_results"]
        if item["name"] == "formal_de_rham_vector_ghost"
    )

    output = {
        "status": "SU2_SPHERE_GAUGE_BLOCK_EQUIVALENCE_REDUCED_NOT_CLOSED",
        "selected_block": {
            "block_id": "D_SU2",
            "gauge_role": block["operator_blocks"]["D_SU2"]["gauge_role"],
            "candidate_equivalence": "D_SU2 would equal the effective sphere scalar zeta finite part times C_A(SU2)=2 if the non-abelian quotient determinant contributes no additional finite weak-split term.",
            "closure_status": "CONDITIONAL_ON_NONABELIAN_GHOST_QUOTIENT_DETERMINANT",
        },
        "available_exact_data": {
            "scalar_proxy_formula": exact["closed_formulas"]["SU2_effective_sphere"],
            "unweighted_scalar_proxy_finite_part": p_su2_scalar,
            "casimir_heat_weight_candidate": heat_weight,
            "heat_weighted_candidate": weighted_candidate,
        },
        "source_obstruction": {
            "nonabelian_fp_operator": "M_G[A] = partial^mu D_mu[A]",
            "field_dependence": True,
            "consequence": "The ghost/quotient determinant can carry a nontrivial finite threshold contribution and must be derived, not discarded.",
        },
        "negative_checks": {
            "naive_de_rham_vector_ghost_status": de_rham["status"],
            "naive_de_rham_vector_ghost_lambda_12": de_rham["lambda_12"],
            "meaning": "The previously tested naive de Rham vector/ghost determinant is explicitly not the selected SU2 closure.",
        },
        "missing_for_closure": [
            "selected SU2 connection and curvature endomorphism",
            "selected non-abelian Faddeev-Popov ghost operator in the physical quotient",
            "BRST-compatible determinant sign/subtraction rule for this internal block",
            "proof that the remaining finite quotient determinant is zero, universal, or exactly included in the C_A(SU2)=2 heat coefficient",
        ],
        "verdict": {
            "su2_scalar_sphere_zeta_exact": True,
            "casimir_weight_available": True,
            "nonabelian_ghosts_decouple": False,
            "su2_selected_for_lambda_12_accounting": False,
            "absolute_universal_constant_fixed": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Selected_SU2_Nonabelian_Ghost_Quotient_Determinant_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
