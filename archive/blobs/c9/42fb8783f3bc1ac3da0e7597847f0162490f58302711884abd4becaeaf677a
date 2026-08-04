"""Audit the U1/Y Route-C symbolic transport projector replay gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json"
REPLAY = REPO / "candidate_data" / "selected_u1y_routec_symbolic_transport_projector_replay.values.json"
CERT = REPO / "certificates" / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1.md"

STATUS = "U1Y_ROUTEC_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1"


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
    replay = json.loads(REPLAY.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    result = replay["validator_result"]
    acceptance = replay["symbolic_acceptance"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("theorem proved", data["theorem"]["proved"] is True and "dotD_alpha1" in data["theorem"]["statement"], data["theorem"]),
        check("symbolic replay accepted", decision["symbolic_transport_projector_replay_accepted"] is True and acceptance["validator_extension"] == "exact_symbolic_transport_conjugation", acceptance),
        check("raw aliasing bypassed", acceptance["raw_direct_truncated_relative_residual"] > 0.01 and decision["raw_finite_aliasing_rejected_as_failure"] is True, acceptance),
        check("gauge frame residual", acceptance["gauge_frame_replay_passes"] is True and decision["gauge_frame_residual_l2"] < acceptance["gauge_frame_residual_tolerance"], acceptance),
        check("all sector replay", len(replay["sector_replay_slots"]) == 7 and all(slot["selected_green_operator_valid"] for slot in replay["sector_replay_slots"].values()), replay["sector_replay_slots"]),
        check("stationary replay closes", result["selected_source_verified"] is True and result["selected_rho_s_validator_ready"] is True and cert["projector_riesz_green_replay_closed"] is True, result),
        check("dotD remains open", decision["selected_dotD_source_verified"] is False and decision["alpha1_driver_verified"] is False and decision["dotD_alpha1_closed_by_this_artifact"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and guardrails["claims_lambda12"] is False and guardrails["claims_full_sm_closure"] is False, guardrails),
        check("guardrails", guardrails["claims_raw_fourier_aliasing_zero"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents boundary", "does not close `dotD_alpha1`" in note and "dU/dalpha" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C symbolic transport projector replay audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
