"""Audit the U1/Y Route-C matter-slot orientation selector from HYM replay gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_matterslot_orientationselector_from_hym_finitereplay_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_MatterSlot_OrientationSelector_from_HYM_FiniteReplay_v1.md"

STATUS = "U1Y_ROUTEC_MATTERSLOT_ORIENTATION_SELECTOR_HYM_REPLAY_NOGO_TERMINAL_GRADING_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


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
    tests = data["readout_tests"]
    nogo = data["hym_replay_orientation_no_go"]
    route = data["positive_route"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("hym no-go proved", nogo["stationary_hym_replay_cannot_select_orientation"] is True and decision["hym_replay_no_go_for_orientation_proved"] is True, nogo),
        check("hym readout no-go", tests["hym_rho_s_adjoint_readout"]["conclusion"] == "NO_GO_PERMUTATION_INVARIANT" and tests["hym_rho_s_adjoint_readout"]["allowed_as_selected_source"] is True, tests["hym_rho_s_adjoint_readout"]),
        check("support readouts not promotable", tests["qutrit_weyl_support_readout"]["distinguishes_required_partition"] is True and tests["qutrit_weyl_support_readout"]["allowed_as_selected_source"] is False, tests["qutrit_weyl_support_readout"]),
        check("locked target forbidden", tests["locked_c1_partition_readout"]["conclusion"] == "FORBIDDEN_TARGET_LOCALIZED_SELECTOR" and guardrails["uses_locked_c1_target_as_selector"] is False, tests["locked_c1_partition_readout"]),
        check("terminal route imported", route["primary_route"] == "terminal_monad_cech_sectionring" and route["selected_closed"] is False and route["source_selector_to_prove"]["forced_label_inside_lane"] == "L3-K2", route),
        check("orientation still open", decision["selected_matter_slot_orientation_emitted"] is False and decision["selected_U10_Ubar5_polarization_emitted"] is False, decision),
        check("alpha1 not promoted", decision["N_alpha1_h_ext_promoted_to_du_dalpha1"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("guardrails hold", guardrails["claims_alpha1_driver_verified"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records no-go and route", "permutation-invariant" in note and "terminal_monad_cech_sectionring" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C matter-slot orientation selector from HYM finite replay audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
