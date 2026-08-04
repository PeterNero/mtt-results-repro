"""Audit Phi_fin/B_N model-active equivalence attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_phifin_bn_modelactive_equivalence_or_minimizer_trace.py"
CANDIDATE = ROOT / "candidate_data" / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
CERT = ROOT / "certificates" / "phifin_bn_modelactive_equivalence_or_minimizer_trace_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1.md"

STATUS = "MTT_PHIFIN_BN_MODEL_ACTIVE_EQUIVALENCE_REJECTED_GAUGE_TRANSPORT_TRACE_REQUIRED"
NEXT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    tests = data["exact_equivalence_tests"]
    theorem = data["no_go_theorem"]
    repair = data["gauge_transport_repair"]
    decision = data["promotion_decision"]

    audit = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate path", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "finite side clean but exact equivalence rejected",
            tests["finite_BN_value_side_clean"] is True
            and tests["exact_untransported_model_active_equivalence_possible"] is False
            and cert["untransported_model_active_equivalence_rejected"] is True,
            tests,
        ),
        check(
            "selected connection nonzero",
            tests["selected_diagonal_End0_connection_closed"] is True
            and tests["selected_connection_has_nonzero_du"] is True
            and len(data["nonzero_gradient_dirs"]) >= 1,
            data["nonzero_gradient_dirs"],
        ),
        check(
            "adT3 acts on T1T2",
            tests["ad_T3_nonzero_on_T1_T2"] is True
            and data["ad_T3_matrix"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            data["ad_T3_matrix"],
        ),
        check(
            "no-go theorem proved",
            theorem["proved"] is True
            and any("untransported constant T1/T2 section is not D-flat" in step for step in theorem["proof_steps"]),
            theorem,
        ),
        check(
            "gauge transport repair identified",
            repair["can_promote_after_repair"] is True
            and repair["why_legal"] is True
            and "U=exp(-u ad(T3))" in repair["required_transport"],
            repair,
        ),
        check(
            "source flags not promoted",
            decision["selected_source_flags_may_be_flipped_now"] is False
            and decision["exact_model_active_equivalence_rejected"] is True
            and data["what_remains_open"]["gauge_transported_BN_trace"] is True,
            decision,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            cert,
        ),
        check(
            "note records correction",
            "The exact untransported equivalence is rejected." in note
            and "This does not kill Route A.  It corrects it." in note
            and "K_s^selected = exp(-u ad(T3)) K_s^model" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT Phi_fin B_N model-active equivalence audit")
    return 0 if all(audit) else 1


if __name__ == "__main__":
    sys.exit(main())
