"""Audit the U1/Y Route-C dotD alpha1 transport derivative and driver gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json"
CONTRACT = REPO / "candidate_data" / "selected_u1y_routec_alpha1_source_strength_value_contract.open.json"
CERT = REPO / "certificates" / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_TRANSPORT_DERIVATIVE_CLOSED_DRIVER_VALUE_OPEN"
NEXT = "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"


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
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    formula = data["transport_derivative_payload"]
    boundary = data["validator_replay_boundary"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("formula closed", decision["transport_derivative_formula_closed"] is True and formula["dU_dalpha"].startswith("-(du/dalpha)"), formula),
        check("dotD source algebra", decision["selected_dotD_source_formula_closed"] is True and decision["selected_dotD_source_verified_by_transport_derivative"] is True, decision),
        check("prior replay imported", decision["projector_riesz_green_replay_closed"] is True and decision["validator_ready_rho_s_closed"] is True, decision),
        check("validator boundary exact", boundary["mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"] is True and boundary["source_only_fails_only_by_alpha1_driver"] is True, boundary),
        check("contract created", contract["status"] == "OPEN_SOURCE_STRENGTH_VALUE_REQUIRED" and contract["required_value"]["du_dalpha1_equals_h_ext"] is None, contract),
        check("driver still open", decision["normalization_value_emitted_now"] is False and decision["alpha1_driver_verified_now"] is False and decision["honest_dotD_validator_closed_now"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and guardrails["claims_lambda12"] is False and guardrails["claims_full_sm_closure"] is False, guardrails),
        check("no shortcut", guardrails["uses_full_flag_probe_as_proof"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents requirement", "du/dalpha1 = h_ext" in note and "without lifted flags" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C dotD alpha1 transport derivative and driver audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
