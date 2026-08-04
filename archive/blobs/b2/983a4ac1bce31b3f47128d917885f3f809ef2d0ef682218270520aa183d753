"""Audit the U1/Y Route-C dotD/alpha1/C1 response emission gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_dotd_alpha1_c1_response_emission.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_dotd_alpha1_c1_response_emission.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_dotd_alpha1_c1_response_emission_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_dotD_Alpha1_C1_Response_Emission_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_C1_RESPONSE_REDUCED_TANGENT_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_Tangent_or_RetardedOverlap_Kernel_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = data["derivative_payload_checks"]
    remains = data["what_remains_open"]
    lane = data["lane_classification"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("closed prefix carried", decision["D_E_gap_Riesz_Green_layer_closed"] is True and decision["same_basis_dotD_alpha1_values_available"] is True, decision),
        check("nonzero dotD is not source proof", decision["dotD_alpha1_has_nonzero_entries"] is True and decision["selected_dotD_source_theorem_proved"] is False, decision),
        check("derivative obstruction exact", checks["D4_operator_level_selected_projector_retention_for_dotD"] is False and checks["D5_selected_alpha1_tangent_parameter"] is False and checks["D6_retarded_overlap_derivative_formula"] is False, checks),
        check("C1 not emitted", decision["C1_response_operator_emitted"] is False and lane["c1_response_lane"]["status"] == "OPEN_C1_RESPONSE_EMISSION_REQUIRES_SELECTED_OPERATOR_BLOCKS", lane["c1_response_lane"]["status"]),
        check("selected blocks absent", decision["A_selected_emitted"] is False and decision["b_selected_emitted"] is False and remains["selected_Hess_Xi_finite_blocks"] is True, remains),
        check("no closure overreach", data["closure_claimed"] is False and decision["lambda_12_computable"] is False and decision["Yukawa_or_full_SM_closure"] is False, decision),
        check("guardrails", guardrails["claims_selected_dotD_source"] is False and guardrails["promotes_diagnostic_lift_as_proof"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note records missing tangent", "selected first-variation theorem" in note and "Do not infer selected `dotD`" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C dotD/alpha1/C1 response emission audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
