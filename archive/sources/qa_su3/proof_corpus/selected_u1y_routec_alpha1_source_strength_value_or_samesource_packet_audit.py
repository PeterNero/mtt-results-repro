"""Audit the U1/Y Route-C alpha1 source-strength value theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1.md"

STATUS = "U1Y_ROUTEC_ALPHA1_SOURCE_STRENGTH_VALUE_THEOREM_DERIVED_CURRENT_SOURCE_VALUE_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_ChernWeil_Operator_Functional_Value_v1"


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
    evidence = data["current_value_evidence"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("equivalence theorem", data["theorem"]["proved"] is True and decision["necessary_and_sufficient_for_dotD_closure"] is True, data["theorem"]),
        check("local dotD ready", evidence["transport_derivative_formula_closed"] is True and evidence["dotD_matrices_pass_if_driver_theorem_supplied"] is True, evidence),
        check("value still absent", decision["normalization_value_emitted_now"] is False and decision["du_dalpha1_equals_h_ext_emitted"] is False, decision),
        check("current no-go", data["current_source_no_go"]["proved"] is True and decision["current_source_value_no_go_proved"] is True, data["current_source_no_go"]),
        check("driver not flipped", decision["alpha1_driver_verified_now"] is False and decision["honest_dotD_validator_closed_now"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and guardrails["claims_lambda12"] is False and guardrails["claims_full_sm_closure"] is False, guardrails),
        check("guardrails", guardrails["uses_diagnostic_lift_as_proof"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents nonclosure", "current corpus does not emit that value" in note and "cannot honestly be flipped" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C alpha1 source-strength value theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
