from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_hybrid_matter_slot_galerkin_import_certificate.json"
OUT_CERT = ROOT / "certificates" / "routec_source_overlap_packet_chain_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_source_overlap_packet_chain_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Source_Overlap_Packet_Chain_Import_v1.md"

STATUS = "ROUTEC_SOURCE_OVERLAP_PACKET_CHAIN_IMPORTED_CURRENT_SCAFFOLD_NOGO"

ARTIFACTS = [
    {
        "name": "selected operator-source/overlap packet",
        "data": "candidate_data/selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json",
        "cert": "certificates/selected_routec_selected_operator_source_and_overlap_tensor_packet_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1.md",
        "status": "MTT_SELECTED_ROUTEC_OPERATOR_SOURCE_OVERLAP_PACKET_AUDITED_SOURCE_LEVEL_CARRIER_CLOSED_SELECTED_C1_ROUTING_OPEN",
        "next": "MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1",
    },
    {
        "name": "selected C1 routing/normalization/overlap source packet",
        "data": "candidate_data/selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json",
        "cert": "certificates/selected_routec_selected_c1_routing_normalization_and_overlap_source_packet_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Selected_C1_Routing_Normalization_and_Overlap_Source_Packet_v1.md",
        "status": "MTT_SELECTED_ROUTEC_C1_ROUTING_NORMALIZATION_OVERLAP_SOURCE_ATTEMPT_BUILT_SELECTION_STILL_OPEN",
        "next": "MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1",
    },
    {
        "name": "selected matter-slot charge/overlap-normalization theorem",
        "data": "candidate_data/selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json",
        "cert": "certificates/selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md",
        "status": "MTT_SELECTED_ROUTEC_MATTERSLOT_CHARGE_OVERLAP_NORMALIZATION_THEOREM_ATTEMPT_REDUCED_TO_SAME_SOURCE_OPERATOR_PACKET",
        "next": "MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1",
    },
    {
        "name": "same-source matter-slot/overlap operator packet contract",
        "data": "candidate_data/selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json",
        "cert": "certificates/selected_routec_samesource_matter_slot_overlap_operator_packet_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_SameSource_MatterSlot_Overlap_Operator_Packet_v1.md",
        "status": "MTT_SELECTED_ROUTEC_SAMESOURCE_MATTERSLOT_OVERLAP_OPERATOR_PACKET_CONTRACT_BUILT_VALUES_OPEN",
        "next": "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1",
    },
    {
        "name": "same-source operator-packet fill/no-go",
        "data": "candidate_data/selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json",
        "cert": "certificates/selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json",
        "note": "proof_corpus/MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md",
        "status": "MTT_SELECTED_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY",
        "next": "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1",
    },
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    input_checks = {
        "previous_import_proved": prev["theorem"]["proved"] is True,
        "previous_next_matches_first_artifact": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_Selected_OperatorSource_and_OverlapTensor_Packet_v1",
    }

    imported = []
    for artifact in ARTIFACTS:
        data_path = SM / artifact["data"]
        cert_path = SM / artifact["cert"]
        note_path = SM / artifact["note"]
        data = load(data_path)
        cert = load(cert_path)
        note = note_path.read_text(encoding="utf-8")

        checks = {
            "data_status_matches": data["status"] == artifact["status"],
            "cert_status_matches": cert["status"] == artifact["status"],
            "next_matches": data["next_required_artifact"] == artifact["next"],
            "closure_not_claimed": data.get("closure_claimed") is False,
            "target_fitting_not_used": data.get("target_fitting_used") is False,
            "note_mentions_next": artifact["next"] in note,
        }
        imported.append(
            {
                "name": artifact["name"],
                "source_data": str(data_path),
                "source_certificate": str(cert_path),
                "source_note": str(note_path),
                "status": data["status"],
                "next_required_artifact": data["next_required_artifact"],
                "checks": checks,
                "what_closes_now": data.get("what_closes_now") or cert.get("what_closes"),
                "what_remains_open": data.get("what_remains_open") or cert.get("what_remains_open"),
            }
        )

    final_data = load(SM / ARTIFACTS[-1]["data"])
    validator = final_data["validator_report"]
    fill = final_data["fill_summary"]
    final_checks = {
        "validator_rejects_current_packet": validator["ok"] is False and validator["exit_code"] == 1,
        "seven_fields_required": fill["required_fields"] == 7,
        "no_selected_fields_emitted": fill["selected_emitted"] == 0,
        "support_shapes_present": fill["support_present"] >= 6,
        "conditional_A_not_promoted": final_data["fill_summary"]["can_promote_A_selected"] is False,
        "conditional_b_not_promoted": final_data["fill_summary"]["can_promote_b_selected"] is False,
    }

    theorem = {
        "name": "RouteCSourceOverlapPacketChainImportTheorem",
        "proved": all(input_checks.values())
        and all(all(item["checks"].values()) for item in imported)
        and all(final_checks.values()),
        "statement": (
            "The selected operator-source/overlap chain is imported through the "
            "same-source fill/no-go packet. Source-level Weyl carrier and "
            "conditional C1 routing/normalization are exact, finite SU(5) "
            "transversality supplies conditional support, and a seven-field "
            "same-source promotion validator is defined. The current scaffolds "
            "fail that validator: no required field is emitted as a selected "
            "theorem-derived same-source value, so A_selected and b_selected "
            "are not promoted."
        ),
    }

    verdict = {
        "source_level_weyl_carrier_closed": True,
        "conditional_c1_routing_exact": True,
        "conditional_normalization_exact": True,
        "finite_su5_transversality_imported": True,
        "same_source_promotion_contract_built": True,
        "current_same_source_fill_validates": False,
        "selected_A_selected_emitted": False,
        "selected_b_selected_emitted": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": final_data["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "imported_artifacts": imported,
        "final_checks": final_checks,
        "final_validator_errors": validator["errors"],
        "final_why_fill_fails": final_data["why_fill_fails"],
        "verdict": verdict,
    }

    note = """# Route-C Source/Overlap Packet Chain Import v1

## Result

The selected operator-source and overlap chain is now imported through the
current same-source fill/no-go packet.

What is closed or sharply localized:

```text
source-level qutrit Weyl carrier
conditional Z -> u/e and X -> d/nuD C1 route
conditional deltaTheta = (1,1) normalization
finite SU(5) transversality support: U_10 = I_3, U_bar5 = F
seven-field same-source promotion validator
```

What the validator proves about current scaffolds:

```text
required fields = 7
support fields present >= 6
selected theorem-derived same-source fields = 0
current packet rejected
A_selected not promoted
b_selected not promoted
```

The packet is therefore not blocked by finite algebra anymore. It is blocked by
source emission: the same selected branch must emit operator-source identity,
matter-slot charge including the `1_M` neutrino rule, selected D_E/dotD/Riesz
and Green values, selected overlap transfer, selected trace/Hessian
normalization, and selected primitive contractions.

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_SOURCE_OVERLAP_PACKET_CHAIN_IMPORTED_CURRENT_SCAFFOLD_NOGO
```

The next required artifact is:

```text
MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_source_overlap_packet_chain_import",
                "status": STATUS,
                "input_certificate": str(PREV_IMPORT),
                "theorem": theorem,
                "input_checks": input_checks,
                "imported_artifacts": imported,
                "final_checks": final_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
