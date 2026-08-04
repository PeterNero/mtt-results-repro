"""Audit q79 global destabilizer/AH/monad source chain import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_global_destabilizer_ah_monad_source_chain.py"
PACKET = DATA / "q79_global_destabilizer_ah_monad_source_chain_import.candidate.json"
CERT = CERTS / "q79_global_destabilizer_ah_monad_source_chain_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Global_Destabilizer_AH_Monad_Source_Chain_Import_v1.md"


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

    expected = "Q79_GLOBAL_DESTABILIZER_AH_MONAD_SOURCE_CHAIN_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported", cert["theorem"]["proved"] is True, cert["theorem"])

    checks = packet["import_checks"]
    check("all import checks pass", all(checks.values()), checks)

    chain = packet["chain"]
    check(
        "reduced AH stability only",
        chain["global_destabilizer_enumeration"]["reduced_AH_model_stability_proved"]
        and chain["global_destabilizer_enumeration"]["claims_full_stability"] is False
        and chain["global_destabilizer_enumeration"]["selected_AH_or_goodcover_open"],
        chain["global_destabilizer_enumeration"],
    )
    check(
        "conditional HYM bridge only",
        chain["ah_goodcover_promotion_hym_bridge"]["reflexive_hull_reduction_proved"]
        and chain["ah_goodcover_promotion_hym_bridge"]["conditional_HYM_bridge_ready"]
        and chain["ah_goodcover_promotion_hym_bridge"][
            "claims_hym_unconditionally"
        ]
        is False
        and chain["ah_goodcover_promotion_hym_bridge"][
            "selected_Gauduchon_chamber_open"
        ],
        chain["ah_goodcover_promotion_hym_bridge"],
    )
    check(
        "AH reduced to terminal lane and Pic0",
        chain["ah_source_or_routec_residual_reduction"][
            "ah_goodcover_equivalence_closed"
        ]
        and chain["ah_source_or_routec_residual_reduction"][
            "selected_AH_reduced_to_terminal_lane"
        ]
        and chain["ah_source_or_routec_residual_reduction"]["operator_pic0_open"],
        chain["ah_source_or_routec_residual_reduction"],
    )
    check(
        "monad L2 source closed only conditionally",
        chain["selected_monad_l2_source_operatorpic0_or_routec_residual"][
            "selected_monad_L2_source_closed_under_explicit_principle"
        ]
        and chain["selected_monad_l2_source_operatorpic0_or_routec_residual"][
            "claims_unconditional_terminal_section_principle"
        ]
        is False
        and chain["selected_monad_l2_source_operatorpic0_or_routec_residual"][
            "operator_layer_pic0_open"
        ],
        chain["selected_monad_l2_source_operatorpic0_or_routec_residual"],
    )
    check(
        "next gate exact",
        cert["verdict"]["next_required_artifact"]
        == "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1"
        and packet["decision"]["operator_layer_pic0_or_routec_residual_open"],
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_claim_full_stability_or_HYM"]
        and cert["guardrails"]["does_not_claim_selected_RouteC_residual"]
        and cert["guardrails"]["does_not_claim_operator_layer_Pic0_closed"]
        and cert["guardrails"]["does_not_claim_A_selected_or_b_selected"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records operator provenance blocker", "operator provenance" in note, NOTE)

    print("\nQ79 global destabilizer AH monad source chain import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
