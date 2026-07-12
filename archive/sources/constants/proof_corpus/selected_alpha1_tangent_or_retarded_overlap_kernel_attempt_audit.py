"""Audit Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_Attempt_v1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "attempt_selected_alpha1_tangent_or_retarded_overlap_kernel.py"
PACKET = DATA / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
CERT = CERTS / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_Attempt_v1.md"


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

    expected = "SELECTED_ALPHA1_TANGENT_OR_RETARDED_OVERLAP_KERNEL_ATTEMPT_BUILT_SECTOR_CHARGE_OPEN"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem not overclaimed", cert["theorem"]["proved"] is False, cert["theorem"])

    checks = packet["transfer_checks"]
    check(
        "pattern and support available",
        checks["K0_derivative_payload_gate_is_current_next"]
        and checks["K1_ckm_retarded_kernel_pattern_available"]
        and checks["K2_q79_phi_fin_alpha1_support_available"]
        and checks["K3_source_level_weyl_carrier_available"],
        checks,
    )
    check(
        "typed selected transfer remains open",
        checks["K4_selected_sector_charge_or_chirality"] is False
        and checks["K5_selected_transfer_normalization"] is False
        and checks["K6_selected_BN_tangent_or_retarded_kernel"] is False
        and checks["K7_honest_dotD_replay_from_kernel"] is False,
        checks,
    )
    retarded = packet["retarded_kernel_transfer"]
    check(
        "CKM retarded kernel not imported as SM dotD",
        retarded["ckm_nil_survivor_kernel_available"]
        and retarded["ckm_unit_lag_ratio_closed"]
        and retarded["schur_formula_available"]
        and retarded["typed_sm_dotD_kernel_emitted"] is False,
        retarded,
    )
    ladder = packet["q79_source_ladder"]
    check(
        "q79 PhiFin gate stays open",
        ladder["phifin_alpha1_payload_gate"]["finite_codomain_confirmed"]
        and ladder["phifin_alpha1_payload_gate"]["alpha1_support_confirmed"]
        and ladder["phifin_alpha1_payload_gate"][
            "selected_dotD_alpha1_derivative_open"
        ]
        and ladder["phifin_alpha1_payload_gate"][
            "selected_payload_values_claimed"
        ]
        is False,
        ladder["phifin_alpha1_payload_gate"],
    )
    check(
        "weyl carrier source-level only",
        ladder["weylpair_source_provenance"]["source_level_carrier_closed"]
        and ladder["weylpair_source_provenance"]["selected_sector_charge_open"]
        and ladder["weylpair_source_provenance"][
            "selected_transfer_normalization_open"
        ],
        ladder["weylpair_source_provenance"],
    )
    check(
        "conditional A not promoted",
        ladder["weylpair_conditional_assembly"][
            "claims_conditional_A_is_A_selected"
        ]
        is False
        and ladder["weylpair_conditional_assembly"][
            "claims_selected_source_provenance_proved"
        ]
        is False,
        ladder["weylpair_conditional_assembly"],
    )
    check(
        "decision selects sector-charge gate",
        packet["decision"]["retarded_ckm_kernel_is_not_enough"]
        and packet["decision"]["basis_transport_weylpair_lane_is_primary"]
        and cert["next_required_artifact"]["name"]
        == "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_import_ckm_retarded_kernel_as_sm_dotd_proof"]
        and cert["guardrails"]["does_not_promote_conditional_A_to_A_selected"]
        and cert["guardrails"]["does_not_claim_selected_sector_routing"]
        and cert["guardrails"]["does_not_claim_alpha1_driver"]
        and cert["guardrails"]["does_not_claim_C1_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records source-charge next step", "sector-charge/chirality" in note, NOTE)

    print("\nSelected alpha1 tangent or retarded-overlap kernel attempt audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
