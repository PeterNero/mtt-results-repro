"""Audit the U1/Y Route-C TraceEquals27Mode/FullHYMReplay gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_TraceEquals27Mode_or_FullHYMReplay_v1.md"

STATUS = "U1Y_ROUTEC_TRACE_EQUALS_27MODE_DE_GAP_LAYER_CLOSED_DOTD_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_Alpha1_C1_Response_Emission_v1"


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
    proof_steps = data["finite_trace_route"]["proof_steps"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("trace equality closed", decision["selected_trace_equality_for_27mode_DE"] is True and cert["selected_trace_equality_for_27mode_DE"] is True, decision),
        check("gap layer closed", decision["DE_gap_Riesz_Green_layer_closed"] is True and cert["DE_gap_Riesz_Green_layer_closed"] is True, cert),
        check("gap numbers", cert["basis_dimension"] == 27 and cert["selected_eta_N"] < cert["eta_threshold"] and cert["selected_gap_lower_bound"] > 0, cert),
        check("proof steps all proved", all(step["proved"] is True for step in proof_steps.values()), proof_steps),
        check("dotD/C1 remain open", decision["dotD_alpha1_C1_closed"] is False and data["what_remains_open"]["dotD_alpha1_source"] is True and data["what_remains_open"]["primitive_C1_response"] is True, data["what_remains_open"]),
        check("not full closure", decision["full_Phi_fin_closed"] is False and cert["full_Phi_fin_closed"] is False and data["closure_claimed"] is False, decision),
        check("guardrails exclude overreach", guardrails["promotes_diagnostic_dotD_flags"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records boundary", "Do not infer `dotD` source" in note and "selected Green norm bound" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C trace-equals-27mode/full-HYM replay audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
