"""Audit the U1/Y Route-C U10/Ubar5/1M same-branch source-promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_u10ubar5_1m_sourcepromotion_samebranch_emission_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1.md"

STATUS = "U1Y_ROUTEC_U10UBAR5_1M_SOURCEPROMOTION_PACKET_BUILT_SELECTOR_OPEN"
NEXT = "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1"


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
    packet = data["source_promotion_packet"]
    decision = data["decision"]
    selector = data["branch_coherence_selector"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("support complete", cert["support_present"] == cert["required_fields"] == 8 and decision["support_complete"] is True, cert),
        check("finite packet retained", packet["U_10_clock"]["value"] == "I_3" and packet["U_bar5_shift"]["value"] == "F", packet),
        check("1M route retained", packet["one_M_Dirac_shift"]["value"]["1_M"] == "N^c" and packet["one_M_Dirac_shift"]["value"]["route"] == ["d", "nuD"], packet["one_M_Dirac_shift"]),
        check("functional layer present", cert["functional_selected"] > 0 and packet["rho_s_and_zero_mode_bases"]["functional_selected"] is True, cert),
        check("physical and same branch remain open", cert["physical_selected"] == 0 and cert["same_branch"] == 0 and decision["same_branch_complete"] is False, cert),
        check("selector obligations named", selector["needed"] is True and len(selector["must_prove"]) == 6 and len(selector["acceptable_payloads"]) == 3, selector),
        check("alpha1 not promoted", decision["N_alpha1_h_ext_promoted_to_du_dalpha1"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("guardrails hold", guardrails["claims_selected_U10_Ubar5"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records no overpromotion", "support_present = 8 / 8" in note and "physical_selected = 0 / 8" in note and "Do not promote compatible support pieces" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C U10/Ubar5/1M same-branch source-promotion audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
