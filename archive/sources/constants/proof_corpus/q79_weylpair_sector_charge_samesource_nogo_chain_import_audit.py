"""Audit Q79 WeylPair SectorCharge SameSource NoGo Chain import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
SCRIPT = ROOT / "scripts" / "import_q79_weylpair_sector_charge_samesource_nogo_chain.py"
PACKET = DATA / "q79_weylpair_sector_charge_samesource_nogo_chain_import.candidate.json"
CERT = CERTS / "q79_weylpair_sector_charge_samesource_nogo_chain_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_WeylPair_SectorCharge_SameSource_NoGo_Chain_Import_v1.md"


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

    expected = "Q79_WEYLPAIR_SECTOR_CHARGE_SAMESOURCE_CHAIN_IMPORTED"
    check("certificate status", cert["status"] == expected, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem imported as reduction chain", cert["theorem"]["proved"] is True, cert["theorem"])

    checks = packet["import_checks"]
    check("all import checks pass", all(checks.values()), checks)

    chain = packet["chain"]
    check(
        "sector charge remains open",
        chain["q79_sector_charge_or_chirality"]["closure_claimed"] is False
        and chain["q79_sector_charge_or_chirality"][
            "selected_sector_charge_table_open"
        ]
        and chain["q79_sector_charge_or_chirality"][
            "selected_1M_singlet_neutrino_shift_rule_open"
        ],
        chain["q79_sector_charge_or_chirality"],
    )
    check(
        "matter slot remains open",
        chain["q79_matter_slot_charge_overlap"]["closure_claimed"] is False
        and chain["q79_matter_slot_charge_overlap"][
            "prove_selected_matter_slot_charge_open"
        ]
        and chain["q79_matter_slot_charge_overlap"][
            "emit_selected_DE_dotD_Riesz_Green_open"
        ],
        chain["q79_matter_slot_charge_overlap"],
    )
    check(
        "same-source fill no-go recorded",
        chain["q79_same_source_operatorpacket_nogo"]["closure_claimed"] is False
        and chain["q79_same_source_operatorpacket_nogo"][
            "seven_field_validator_no_go_recorded"
        ]
        and chain["q79_same_source_operatorpacket_nogo"][
            "same_source_D_E_rhoE_Riesz_Green_dotD_open"
        ],
        chain["q79_same_source_operatorpacket_nogo"],
    )
    check(
        "stability frontier partial only",
        chain["q79_stability_hym_routec_residual_frontier"][
            "central_neutral_destabilizers_obstructed"
        ]
        and chain["q79_stability_hym_routec_residual_frontier"][
            "claims_full_stability"
        ]
        is False
        and chain["q79_stability_hym_routec_residual_frontier"][
            "global_subsheaf_enumeration_open"
        ],
        chain["q79_stability_hym_routec_residual_frontier"],
    )
    check(
        "decision names true next gate",
        packet["decision"]["same_source_packet_fill_from_current_scaffolds_refuted"]
        and packet["decision"]["central_neutral_stability_subtheorem_available"]
        and packet["decision"]["full_stability_or_selected_routec_residual_open"]
        and cert["verdict"]["next_required_artifact"]
        == "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1",
        packet["decision"],
    )
    check(
        "guardrails retained",
        cert["guardrails"]["does_not_claim_selected_sector_charge"]
        and cert["guardrails"]["does_not_claim_selected_DE_dotD_Riesz_Green"]
        and cert["guardrails"]["does_not_claim_A_selected_or_b_selected"]
        and cert["guardrails"]["does_not_claim_full_stability_or_HYM"]
        and cert["guardrails"]["does_not_claim_Yukawa_or_SM_closure"],
        cert["guardrails"],
    )
    note = NOTE.read_text(encoding="utf-8")
    check("note records structural partition", "10_M={u,e}" in note, NOTE)

    print("\nQ79 WeylPair sector-charge same-source no-go chain import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
