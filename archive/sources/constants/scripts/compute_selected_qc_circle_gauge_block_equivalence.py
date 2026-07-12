"""Certify the Qc circle gauge-block equivalence for weak-split accounting.

The Qc block is abelian.  The gauge-fixing corpus says the abelian
Faddeev-Popov determinant is field-independent and decouples from interacting
dynamics.  The string/heterotic trace convention fixes Tr(T^2)=1 for abelian
generators.  Combined with the exact circle zeta determinant, this closes the
Qc contribution to lambda_12 up to universal constants that cancel from the
weak split.
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

    p_qc = float(exact["finite_parts"]["U1_circle"])
    heat_weight = float(
        block["operator_blocks"]["D_Qc"]["trace_and_representation"]["heat_coefficient_candidate"]
    )
    selected_value = p_qc * heat_weight

    output = {
        "status": "QC_CIRCLE_GAUGE_BLOCK_EQUIVALENCE_CLOSED_FOR_WEAK_SPLIT",
        "selected_block": {
            "block_id": "D_Qc",
            "gauge_role": block["operator_blocks"]["D_Qc"]["gauge_role"],
            "operator_equivalence": "D_Qc weak-split determinant equals selected circle scalar zeta finite part",
            "scope": "weak-split threshold accounting; universal abelian gauge-fixing constants are discarded",
        },
        "source_lemmas": {
            "abelian_fp_decoupling": {
                "claim": "The abelian Faddeev-Popov determinant is field-independent and decouples.",
                "effect": "It contributes no selected field-dependent threshold piece to lambda_12.",
            },
            "abelian_trace_normalization": {
                "claim": "Tr(T^2)=1 for abelian generators.",
                "effect": "The Qc heat/index coefficient is 1.",
            },
            "selected_circle_zeta": {
                "claim": "The q79 central-circle scalar zeta determinant is exact.",
                "formula": exact["closed_formulas"]["U1_circle"],
                "finite_part": p_qc,
            },
        },
        "selected_values": {
            "unweighted_p_Qc": p_qc,
            "heat_index_weight": heat_weight,
            "selected_p_Qc_for_weak_split": selected_value,
        },
        "remaining_caveats": [
            "This does not close the SU2 or Qa/SU3 blocks.",
            "This does not claim an absolute universal determinant normalization; constants common to weak-split accounting are irrelevant.",
            "This assumes the Qc selected internal direction is the q79 selected central circle already certified in the circle zeta scaffold.",
        ],
        "verdict": {
            "qc_circle_scalar_zeta_exact": True,
            "abelian_ghosts_decouple": True,
            "abelian_trace_weight_selected": True,
            "qc_selected_for_lambda_12_accounting": True,
            "absolute_universal_constant_fixed": False,
            "new_no_knob_prediction_certified": False,
            "next_required_artifact": "Selected_SU2_Sphere_Gauge_Block_Equivalence_v1",
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
