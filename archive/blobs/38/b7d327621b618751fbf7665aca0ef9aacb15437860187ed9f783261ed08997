"""Audit the U1/Y Route-C same-source Chern-Weil functional value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_samesource_chernweil_operator_functional_value.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_samesource_chernweil_operator_functional_value_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SameSource_ChernWeil_Operator_Functional_Value_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_CHERNWEIL_FUNCTIONAL_VALUE_REDUCED_TO_MATTERSLOT_OVERLAP_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1"


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
    reductions = data["latest_reductions"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("support value", decision["support_candidate_value_N_alpha1_h_ext"] == 1.0 and cert["support_candidate_value_N_alpha1_h_ext"] == 1.0, decision),
        check("support residual", decision["support_candidate_residual_zero"] is True and cert["support_candidate_residual_zero"] is True, cert),
        check("theorem proved", data["theorem"]["proved"] is True and "N_alpha1(h_ext)=1" in data["theorem"]["statement"], data["theorem"]),
        check("latest q79 reductions imported", reductions["q79_basis_transport_theorem"]["weyl_pair_reconstructs_locked_splitter"] is True and reductions["q79_weylpair_sector_charge"]["su5_e6_partition_matches_required_route"] is True, reductions),
        check("selected promotion still open", decision["selected_value_emitted_now"] is False and decision["selected_transfer_normalization_closed"] is False, decision),
        check("driver still false", decision["alpha1_driver_verified_now"] is False and decision["honest_dotD_validator_closed_now"] is False, decision),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("guardrails", guardrails["claims_selected_value_emitted"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False and guardrails["uses_diagnostic_lift_as_proof"] is False, guardrails),
        check("note documents boundary", "support value is preserved but not used as proof" in note and "N_alpha1(h_ext)=1" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C same-source Chern-Weil functional value audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
