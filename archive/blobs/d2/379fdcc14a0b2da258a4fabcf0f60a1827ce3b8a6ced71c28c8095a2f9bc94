"""Audit the U1/Y Route-C branch-coherence selector or finite validator replay gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_branchcoherence_selector_or_finite_validator_replay_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1.md"

STATUS = "U1Y_ROUTEC_BRANCHCOHERENCE_GATE_PARTIAL_REPLAY_CLOSED_MATTERSLOT_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1"


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
    subgoals = data["subgoals"]
    decision = data["decision"]
    contract = data["orientation_selector_contract"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("one subgoal closed", cert["subgoals_closed"] == 1 and cert["required_subgoals"] == 6, cert),
        check("hym replay closed", subgoals["hym_finite_validator_replay"]["closed"] is True and decision["rho_s_validator_ready_promoted"] is True, subgoals["hym_finite_validator_replay"]),
        check("normalization conditional not physical", subgoals["sector_gram_normalization_ready"]["status"] == "CONDITIONAL_READY" and subgoals["sector_gram_normalization_ready"]["closed"] is False, subgoals["sector_gram_normalization_ready"]),
        check("q79 support remains support", subgoals["q79_finite_polarization_support"]["status"] == "SUPPORT_ONLY" and decision["q79_finite_polarization_selected"] is False, subgoals["q79_finite_polarization_support"]),
        check("orientation contract exact", contract["must_emit"]["phase_sectors"] == ["u", "e"] and contract["must_emit"]["shift_sectors"] == ["d", "nuD"] and contract["must_emit"]["finite_packet_match"]["U_bar5"] == "F", contract["must_emit"]),
        check("alpha1 not promoted", decision["N_alpha1_h_ext_promoted_to_du_dalpha1"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("guardrails hold", guardrails["claims_full_branch_coherence"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records boundary", "stationary HYM/projector replay side is now closed" in note and "Do not treat the closed HYM stationary replay" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C branch-coherence selector or finite validator replay audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
