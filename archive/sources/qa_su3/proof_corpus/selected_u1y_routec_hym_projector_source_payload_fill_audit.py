"""Audit the U1/Y Route-C HYM projector source payload fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_hym_projector_source_payload_fill.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json"
PAYLOAD = REPO / "candidate_data" / "selected_u1y_routec_hym_projector_source_payload.functional.json"
CERT = REPO / "certificates" / "selected_u1y_routec_hym_projector_source_payload_fill_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1.md"

STATUS = "U1Y_ROUTEC_HYM_PROJECTOR_PAYLOAD_FILLED_FUNCTIONAL_TRACE_FINITE_REPLAY_OPEN"
NEXT = "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1"


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
    payload = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("functional payload filled", decision["functional_projector_payload_filled"] is True and payload["status"].endswith("FINITE_VALIDATOR_REPLAY_OPEN"), payload["status"]),
        check("sector dimensions", payload["sector_projectors"]["Q"]["rank_required"] == 3 and payload["sector_projectors"]["H"]["rank_required"] == 1, payload["sector_projectors"]),
        check("basis dimensions", payload["ordered_zero_mode_bases_K_s"]["u"]["dimension_emitted"] == 3 and payload["ordered_zero_mode_bases_K_s"]["H"]["dimension_emitted"] == 1, payload["ordered_zero_mode_bases_K_s"]),
        check("rho matrices filled", payload["End0_action_on_zero_modes"]["Q"]["rho_s_T3"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]] and payload["End0_action_on_zero_modes"]["H"]["rho_s_T3"] == [[0]], payload["End0_action_on_zero_modes"]),
        check("source theorem promotes functional rho", decision["source_theorem_can_promote_functional_rho_s"] is True and decision["functional_source_map_rho_s_emitted"] is True, decision),
        check("finite replay still open", decision["finite_27mode_validator_replay_closed"] is False and decision["validator_ready_sector_packet_emitted"] is False, decision),
        check("dotD still open", decision["selected_dotD_source_verified"] is False and decision["alpha1_driver_verified"] is False and decision["physical_dotD_alpha1_payload_extracted"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and guardrails["claims_lambda12"] is False and guardrails["claims_full_sm_closure"] is False, guardrails),
        check("no target fitting", data["target_fitting_used"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents boundary", "functional transport-trace level" in note and "does not yet close finite" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C HYM projector payload fill audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
