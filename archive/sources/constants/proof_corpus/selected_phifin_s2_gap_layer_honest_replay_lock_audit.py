"""Audit the selected Phi_fin S2 D_E gap-layer replay lock."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "lock_selected_phifin_s2_gap_layer_honest_replay.py"
PACKET = DATA / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"
CERT = CERTS / "selected_phifin_s2_gap_layer_honest_replay_lock_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_PhiFin_S2_Gap_Layer_Honest_Replay_Lock_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_cert = json.loads(proc.stdout)

    expected = "SELECTED_PHIFIN_S2_D_E_GAP_LAYER_LOCKED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])

    contract = packet["locked_contract"]
    check(
        "D_E replay locked",
        contract["scope"] == "D_E gap/Riesz/Green layer only"
        and contract["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3"
        and contract["basis_dimension"] == 27
        and contract["D_E_honest_replay_passes_after_theorem_derived_source_flags"]
        and contract["D_E_source_flags_are_theorem_derived"],
        contract,
    )
    check(
        "selected gap positive",
        contract["selected_eta_N"] == 1.0
        and contract["eta_threshold"] > contract["selected_eta_N"]
        and contract["selected_gap_lower_bound"] > 0.0
        and contract["selected_green_norm_bound"] > 0.0
        and contract["Riesz_Green_layer_closes"],
        contract,
    )
    check(
        "formula locked",
        packet["formula_lock"]["all_sector_formulas_match"]
        and packet["formula_lock"]["H_shift_indices"] == [13, 14]
        and "rank-two projector" in packet["formula_lock"]["H_sector"],
        packet["formula_lock"],
    )
    check(
        "replay delta is narrow",
        packet["replay_delta"]["previous_D_E_replay_failed_only_by_source_flags"]
        and packet["replay_delta"]["new_source_flags_theorem_derived_for_D_E"]
        and packet["replay_delta"]["previous_dotD_replay_failed_by_source_driver_flags"]
        and packet["replay_delta"]["full_s2_honest_replay_without_lifted_flags"] is False,
        packet["replay_delta"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_promote_dotD_flags"]
        and cert["guardrails"]["does_not_claim_full_S2_honest_replay"]
        and cert["guardrails"]["does_not_claim_A_selected_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"]
        and cert["guardrails"]["does_not_use_observed_or_benchmark_inputs"]
        and cert["guardrails"]["locks_only_theorem_derived_D_E_flags"],
        cert["guardrails"],
    )
    check(
        "next artifact named",
        cert["verdict"]["next_required_artifact"]
        == "Selected_PhiFin_dotD_alpha1_C1_Response_Emission_v1",
        cert["verdict"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records boundary", "does not promote `dotD_alpha1`" in note, NOTE)

    print("\nSelected PhiFin S2 gap-layer honest replay lock audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
