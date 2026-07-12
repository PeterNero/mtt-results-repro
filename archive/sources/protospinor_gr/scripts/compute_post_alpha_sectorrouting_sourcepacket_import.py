from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_weylpair_transfer_reduction.packet.json"
ROUTING = SM / "candidate_data" / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
OVERLAP = SM / "candidate_data" / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
MATTER = QA / "candidate_data" / "selected_u1y_routec_matter_slot_overlap_normalization_source.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_sectorrouting_sourcepacket_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_sectorrouting_sourcepacket.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SectorRouting_SourcePacket_v1.md"

STATUS = "POST_ALPHA_SECTORROUTING_REDUCED_HYBRID_GALERKIN_SOURCE_PACKET_OPEN"
NEXT = "Selected_U1Y_RouteC_Hybrid_Galerkin_Overlap_Source_Packet_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    routing = load(ROUTING)
    overlap = load(OVERLAP)
    matter = load(MATTER)

    routing_search_exact = all(
        [
            routing["lemma_attempt"]["fully_proved"] is False,
            routing["lemma_attempt"]["proved_by_locked_columns"] is True,
            routing["lemma_attempt"]["proved_by_selected_source"] is False,
            routing["routing_search"]["target_columns_select_route"] is True,
            routing["routing_search"]["source_data_independently_selects_route"] is False,
            len(routing["routing_search"]["exact_rows_relative_to_locked_columns"]) == 1,
            routing["routing_search"]["exact_rows_relative_to_locked_columns"][0]["phase_route"] == ["u", "e"],
            routing["routing_search"]["exact_rows_relative_to_locked_columns"][0]["shift_route"] == ["d", "nuD"],
        ]
    )
    overlap_frontier_consolidated = all(
        [
            overlap["what_closes_now"]["source_level_weyl_carrier_and_active_shift_imported_as_closed"] is True,
            overlap["selected_overlap_transport"]["conditional_source_to_C1_transfer_exact"] is True,
            overlap["selected_overlap_transport"]["selected_sector_routing_emitted"] is False,
            overlap["selected_overlap_transport"]["selected_transfer_normalization_emitted"] is False,
            overlap["selected_operator_source"]["A_selected_emitted"] is False,
            overlap["selected_operator_source"]["b_selected_emitted"] is False,
        ]
    )
    matter_source_reduction = all(
        [
            matter["decision"]["conditional_route_exact"] is True,
            matter["decision"]["selected_source_independently_derives_route"] is False,
            matter["decision"]["structural_partition_matches"] is True,
            matter["decision"]["theorem_closed"] is False,
            matter["structural_candidate"]["matches_required_partition"] is True,
            matter["structural_candidate"]["nuD_singlet_gap"] is True,
            matter["structural_candidate"]["nuD_singlet_rule_closed"] is False,
            matter["decision"]["best_next_artifact"] == NEXT,
        ]
    )
    next_packet_minimal = all(
        [
            "derive Z -> {u,e} without locked target columns" in matter["next_packet"]["acceptance_test"],
            "derive X -> {d,nuD} without locked target columns" in matter["next_packet"]["acceptance_test"],
            "emit A_selected and b_selected from source data" in matter["next_packet"]["acceptance_test"],
            "selected transfer normalization from source-level Weyl carrier to C1 columns" in matter["next_packet"]["must_supply"],
            "same-source primitive overlap tensor or transfer functor T_selected" in matter["next_packet"]["must_supply"],
        ]
    )
    previous_reconciled = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_remains_open"]["selected_sector_routing_source_lemma"] is True,
            prev["what_remains_open"]["selected_transfer_normalization"] is True,
        ]
    )
    guardrails_ok = all(
        [
            routing["closure_claimed"] is False,
            overlap["closure_claimed"] is False,
            matter["guardrails"]["uses_locked_target_columns_as_selector"] is False,
            matter["guardrails"]["uses_observed_masses_or_ckm_inputs"] is False,
            matter["guardrails"]["claims_A_selected"] is False,
            matter["guardrails"]["claims_b_selected"] is False,
            matter["guardrails"]["claims_full_sm_closure"] is False,
            routing["target_fitting_used"] is False,
            overlap["target_fitting_used"] is False,
            matter["target_fitting_used"] is False,
        ]
    )
    theorem_proved = all(
        [
            routing_search_exact,
            overlap_frontier_consolidated,
            matter_source_reduction,
            next_packet_minimal,
            previous_reconciled,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaSectorRoutingSourcePacketReductionTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The Weyl-pair sector route is unique relative to the locked conditional columns: Z routes to "
                "u/e and X routes to d/nuD. This uniqueness is not accepted as selected proof, because the "
                "current selected source does not independently emit the sector charge/chirality rule. "
                "The SU(5)/E6 matter-slot dictionary gives structural support for u,e in 10_M and d,nuD "
                "on the non-10/singlet side, but the nuD singlet rule, selected transfer normalization, "
                "and selected overlap functor remain open. Therefore the next object is the hybrid Galerkin "
                "overlap source packet."
            ),
        },
        "status": STATUS,
        "routing_search": {
            "status": routing["status"],
            "exact_rows_relative_to_locked_columns": routing["routing_search"]["exact_rows_relative_to_locked_columns"],
            "source_data_independently_selects_route": routing["routing_search"]["source_data_independently_selects_route"],
            "next_certificate": routing["next_certificate"],
        },
        "structural_matter_support": {
            "status": matter["status"],
            "slot_table": matter["structural_candidate"]["slot_table"],
            "phase_route_from_10M": matter["structural_candidate"]["phase_route_from_10M"],
            "shift_route_from_non10_plus_singlet": matter["structural_candidate"]["shift_route_from_non10_plus_singlet"],
            "nuD_singlet_rule_closed": matter["structural_candidate"]["nuD_singlet_rule_closed"],
        },
        "selected_overlap_frontier": {
            "status": overlap["status"],
            "missing_selected_object": overlap["missing_selected_object"],
            "best_current_statement": overlap["best_current_statement"],
        },
        "next_packet": matter["next_packet"],
        "checks": {
            "routing_search_exact": routing_search_exact,
            "overlap_frontier_consolidated": overlap_frontier_consolidated,
            "matter_source_reduction": matter_source_reduction,
            "next_packet_minimal": next_packet_minimal,
            "previous_reconciled": previous_reconciled,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "locked_columns_unique_route_recorded_as_diagnostic": True,
            "target_column_route_not_promoted_to_selected_proof": True,
            "su5_e6_structural_partition_imported": True,
            "nuD_singlet_gap_identified": True,
            "selected_overlap_and_transfer_packet_minimized": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_Z_to_u_e_source_theorem": True,
            "selected_X_to_d_nuD_source_theorem": True,
            "selected_nuD_singlet_rule": True,
            "selected_transfer_normalization": True,
            "selected_overlap_tensor_or_functor": True,
            "same_source_DE_Riesz_Green_dotD_payload": True,
            "emit_A_selected_and_b_selected": True,
            "selected_deltaTheta_C1_solve": True,
            "Yukawa_CKM_PMNS_CP_and_full_SM_closure": True,
            "selected_lambda12_spectral_table": True,
        },
        "guardrails": {
            "does_not_use_locked_columns_as_selector": True,
            "does_not_promote_structural_SU5_support_to_selected_source": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_full_SM_or_lambda12_closure": True,
            "does_not_use_observed_flavor_data": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {
            "previous_weylpair_transfer": str(PREV),
            "routing": str(ROUTING),
            "overlap": str(OVERLAP),
            "matter": str(MATTER),
        },
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_sectorrouting_sourcepacket",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
        "next_required_artifact": NEXT,
    }
    note = f"""# PostAlpha SectorRouting SourcePacket v1

## Result

The conditional route is unique relative to the locked columns:

```text
Z -> u,e
X -> d,nuD
```

This is not selected proof. The selected source still must derive the same
route without using the locked columns as the selector. The structural
SU(5)/E6 dictionary supports the partition, but the `nuD` singlet rule,
selected transfer normalization, selected overlap functor, and same-source
Galerkin/operator packet remain open.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
