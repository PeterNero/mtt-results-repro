"""Audit the U1/Y Route-C zero-mode basis from HYM projector source theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem.candidate.json"
CONTRACT = REPO / "candidate_data" / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_payload.open.json"
CERT = REPO / "certificates" / "selected_u1y_routec_zeromodebasis_from_hym_projector_source_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_ZEROMODEBASIS_FROM_HYM_PROJECTOR_SOURCE_THEOREM_PROVED_PAYLOAD_OPEN"
NEXT = "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1"


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
    required = contract["required_payload"]
    sector_payload = required["sector_projectors"]
    basis_payload = required["ordered_zero_mode_bases_K_s"]
    action_payload = required["End0_action_on_zero_modes"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("theorem proved", data["theorem"]["proved"] is True and cert["theorem_proved"] is True, data["theorem"]),
        check("payload contract", decision["payload_contract_created"] is True and contract["status"] == "OPEN_VALUES_REQUIRED", contract["status"]),
        check("source families", decision["accepted_source_families_count"] == 3 and len(contract["accepted_source_families"]) == 3, contract["accepted_source_families"]),
        check("sector payload dimensions", sector_payload["Q"]["rank_required"] == 3 and sector_payload["H"]["rank_required"] == 1, sector_payload),
        check("basis payload dimensions", basis_payload["N"]["dimension_required"] == 3 and basis_payload["H"]["dimension_required"] == 1, basis_payload),
        check("action target models", action_payload["Q"]["target_model"] == "adjoint_triplet" and action_payload["H"]["target_model"] == "trivial_singlet", action_payload),
        check("promotion rule", data["promotion_rule"]["rho_s_definition"].startswith("rho_s(T_i)=P_s"), data["promotion_rule"]),
        check("selected values still open", decision["selected_projector_payload_filled"] is False and decision["selected_zero_mode_bases_emitted"] is False and decision["selected_source_map_rho_s_emitted"] is False, decision),
        check("downstream still open", decision["physical_dotD_alpha1_payload_extracted"] is False and guardrails["claims_full_sm_closure"] is False and data["closure_claimed"] is False, guardrails),
        check("no overpromotion", guardrails["promotes_model_carrier_without_source_payload"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents conditionality", "does not fill" in note and "conditional until the selected projector payload is filled" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C zero-mode basis source theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
