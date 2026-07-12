"""Import q79 Weyl-pair sector-charge and same-source no-go chain."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = DATA / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
Q79_SECTOR = Q79 / "certificates" / "q79_routec_weylpair_sector_charge_or_chirality_certificate.json"
Q79_MATTERSLOT = (
    Q79
    / "certificates"
    / "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
)
Q79_SAMESOURCE_NOGO = Q79 / "certificates" / "q79_samesource_operatorpacket_fill_or_nogo_certificate.json"
Q79_STABILITY = Q79 / "certificates" / "q79_stability_hym_or_routec_residual_source_certificate.json"
SM_SECTOR = (
    SM
    / "certificates"
    / "selected_routec_weylpair_sector_charge_or_chirality_certificate_certificate.json"
)
SM_SAMESOURCE_NOGO = (
    SM / "certificates" / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json"
)

OUTPUT_PACKET = DATA / "q79_weylpair_sector_charge_samesource_nogo_chain_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_weylpair_sector_charge_samesource_nogo_chain_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_WeylPair_SectorCharge_SameSource_NoGo_Chain_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    q79_sector = load_json(Q79_SECTOR)
    q79_matter = load_json(Q79_MATTERSLOT)
    q79_nogo = load_json(Q79_SAMESOURCE_NOGO)
    q79_stability = load_json(Q79_STABILITY)
    sm_sector = load_json(SM_SECTOR)
    sm_nogo = load_json(SM_SAMESOURCE_NOGO)

    chain = {
        "previous_kernel_transfer": {
            "status": previous["status"],
            "next_required_artifact": previous["verdict"]["next_required_artifact"],
        },
        "q79_sector_charge_or_chirality": {
            "status": q79_sector["status"],
            "closure_claimed": q79_sector["closure_claimed"],
            "structural_partition": "10_M={u,e}; non-10/singlet={d,nuD}",
            "selected_sector_charge_table_open": q79_sector["still_open"][
                "selected_sector_charge_or_chirality_table"
            ],
            "selected_1M_singlet_neutrino_shift_rule_open": q79_sector[
                "still_open"
            ]["selected_1M_singlet_neutrino_shift_rule"],
            "selected_transfer_normalization_open": q79_sector["still_open"][
                "selected_transfer_normalization"
            ],
            "next_required_artifact": q79_sector["next_required_artifact"],
        },
        "q79_matter_slot_charge_overlap": {
            "status": q79_matter["status"],
            "closure_claimed": q79_matter["closure_claimed"],
            "prove_selected_matter_slot_charge_open": q79_matter["still_open"][
                "prove_selected_matter_slot_charge"
            ],
            "prove_selected_1M_neutrino_rule_open": q79_matter["still_open"][
                "prove_selected_1M_neutrino_rule"
            ],
            "emit_selected_DE_dotD_Riesz_Green_open": q79_matter["still_open"][
                "emit_selected_DE_dotD_Riesz_Green"
            ],
            "emit_selected_overlap_transfer_functor_open": q79_matter[
                "still_open"
            ]["emit_selected_overlap_transfer_functor"],
            "next_required_artifact": q79_matter["next_required_artifact"],
        },
        "q79_same_source_operatorpacket_nogo": {
            "status": q79_nogo["status"],
            "closure_claimed": q79_nogo["closure_claimed"],
            "seven_field_validator_no_go_recorded": q79_nogo["what_closes_now"][
                "seven_field_validator_no_go_recorded"
            ],
            "same_source_D_E_rhoE_Riesz_Green_dotD_open": q79_nogo[
                "what_remains_open"
            ]["same_source_D_E_rhoE_Riesz_Green_dotD"],
            "selected_visible_operator_source_open": q79_nogo["what_remains_open"][
                "selected_visible_operator_source"
            ],
            "next_required_artifact": q79_nogo["next_required_artifact"],
        },
        "q79_stability_hym_routec_residual_frontier": {
            "status": q79_stability["status"],
            "closure_claimed": q79_stability["closure_claimed"],
            "central_neutral_destabilizers_obstructed": q79_stability[
                "what_closes_now"
            ]["central_neutral_base_pullback_destabilizers_obstructed"],
            "claims_full_stability": q79_stability["guardrails"][
                "claims_full_stability"
            ],
            "global_subsheaf_enumeration_open": q79_stability["what_remains_open"][
                "global_rank_one_torsion_free_subsheaf_enumeration"
            ],
            "selected_RouteC_residual_values_open": q79_stability[
                "what_remains_open"
            ]["selected_RouteC_residual_values"],
            "next_required_artifact": q79_stability["next_required_artifact"],
        },
        "sm_parity_alignment": {
            "sector_status": sm_sector["status"],
            "sector_next": sm_sector["next_required_artifact"],
            "same_source_nogo_status": sm_nogo["status"],
            "same_source_nogo_next": sm_nogo["next_required_artifact"],
            "same_source_nogo_current_scaffolds_support_only": sm_nogo[
                "what_closes"
            ]["current_scaffold_nogo_proved"],
        },
    }

    import_checks = {
        "C0_previous_next_matches_q79_sector_gate": chain["previous_kernel_transfer"][
            "next_required_artifact"
        ]
        == "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1",
        "C1_sector_gate_reduced_not_closed": q79_sector["closure_claimed"] is False
        and chain["q79_sector_charge_or_chirality"][
            "selected_sector_charge_table_open"
        ],
        "C2_matter_slot_reduced_not_closed": q79_matter["closure_claimed"] is False
        and chain["q79_matter_slot_charge_overlap"][
            "prove_selected_matter_slot_charge_open"
        ],
        "C3_same_source_packet_fill_nogo": q79_nogo["closure_claimed"] is False
        and chain["q79_same_source_operatorpacket_nogo"][
            "seven_field_validator_no_go_recorded"
        ],
        "C4_stability_frontier_advanced": q79_stability["closure_claimed"] is False
        and chain["q79_stability_hym_routec_residual_frontier"][
            "central_neutral_destabilizers_obstructed"
        ],
        "C5_no_A_or_b_or_SM_claim": all(
            [
                q79_sector["guardrails"]["claims_full_sm_closure"] is False,
                q79_matter["guardrails"]["claims_A_selected"] is False,
                q79_matter["guardrails"]["claims_b_selected"] is False,
                q79_nogo["guardrails"]["claims_A_selected"] is False,
                q79_nogo["guardrails"]["claims_b_selected"] is False,
                q79_stability["guardrails"]["claims_full_sm_closure"] is False,
            ]
        ),
    }

    proved = all(import_checks.values())
    return {
        "packet": "Q79_WeylPair_SectorCharge_SameSource_NoGo_Chain_Import_v1",
        "status": (
            "Q79_WEYLPAIR_SECTOR_CHARGE_SAMESOURCE_CHAIN_IMPORTED"
            if proved
            else "Q79_WEYLPAIR_SECTOR_CHARGE_SAMESOURCE_CHAIN_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "q79_sector_charge": str(Q79_SECTOR),
            "q79_matter_slot": str(Q79_MATTERSLOT),
            "q79_samesource_nogo": str(Q79_SAMESOURCE_NOGO),
            "q79_stability": str(Q79_STABILITY),
            "sm_sector_charge": str(SM_SECTOR),
            "sm_samesource_nogo": str(SM_SAMESOURCE_NOGO),
        },
        "theorem": {
            "name": "Q79WeylPairSectorChargeSameSourceNoGoChainImport",
            "proved": proved,
            "statement": (
                "The local alpha1 tangent frontier advances through the q79 "
                "sector-charge reduction, the selected matter-slot reduction, "
                "and the same-source operator-packet no-go.  The current next "
                "honest proof object is global stability/HYM or a selected "
                "Route-C residual source."
            ),
        },
        "import_checks": import_checks,
        "chain": chain,
        "decision": {
            "sector_partition_structurally_identified": True,
            "sector_partition_selected_by_source": False,
            "same_source_packet_fill_from_current_scaffolds_refuted": True,
            "central_neutral_stability_subtheorem_available": True,
            "full_stability_or_selected_routec_residual_open": True,
            "next_required_artifact": "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1",
        },
        "guardrails": {
            "does_not_claim_selected_sector_charge": True,
            "does_not_claim_selected_matter_slot_charge": True,
            "does_not_claim_selected_DE_dotD_Riesz_Green": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_full_stability_or_HYM": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The local frontier imports the q79 reduction chain: structural "
                "sector partition identified, same-source packet fill refuted "
                "from current scaffolds, and central-neutral destabilizers "
                "obstructed in the reduced stability lane."
            ),
            "what_remains": (
                "Prove global destabilizer enumeration or emit a selected "
                "Route-C residual source; then revisit the same-source operator "
                "packet and dotD/alpha1 replay."
            ),
            "next_required_artifact": "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79WeylPairSectorChargeSameSourceNoGoChainImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "decision": packet["decision"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 WeylPair SectorCharge SameSource NoGo Chain Import v1

## Result

Status: `{cert["status"]}`

The sector-charge path has advanced, but not closed.  The q79/SM data identify
the structural partition `10_M={{u,e}}` versus non-`10_M`/singlet `{{d,nuD}}`.
The selected same-source operator packet still cannot be filled from current
scaffolds, and the stability lane currently closes only the central-neutral
destabilizer subtheorem.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Chain

```json
{json.dumps(packet["chain"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
