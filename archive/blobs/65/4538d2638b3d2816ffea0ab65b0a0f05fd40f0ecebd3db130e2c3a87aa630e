from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_weylpair_sector_charge_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_weylpair_matter_slot_blocksector_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_weylpair_matter_slot_blocksector_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_MatterSlot_BlockSector_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_MATTERSLOT_BLOCKSECTOR_IMPORTED_HYBRID_PACKET_NEXT"
SOURCE_STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    theorem_attempt = src["theorem_attempt"]
    routes = src["routes"]
    clue = src["new_clue_from_qutrit_embedding"]
    hybrid = src["hybrid_closing_packet"]

    input_checks = {
        "previous_sector_charge_imported": prev["theorem"]["proved"] is True,
        "previous_next_matches": prev["verdict"]["next_required_artifact"]
        == "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1",
        "source_status_matches": src["status"] == SOURCE_STATUS,
        "certificate_status_matches": src_cert["status"] == SOURCE_STATUS,
        "next_artifact_matches": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    theorem_checks = {
        "not_closed_now": theorem_attempt["closed_now"] is False,
        "locked_target_not_promoted": theorem_attempt["previous_locked_target_not_promoted"] is True,
        "goal_mentions_routing": "Z -> u,e" in theorem_attempt["goal"]
        and "X -> d,nuD" in theorem_attempt["goal"],
    }

    route_checks = {
        "high_scale_route_conditional": routes["high_scale_SU5_E6"]["closes_now"] is False,
        "finite_transport_not_blocker": routes["high_scale_SU5_E6"]["evidence"][
            "finite_I_F_transport_not_blocker"
        ]
        is True,
        "selected_source_not_verified": routes["high_scale_SU5_E6"]["evidence"][
            "selected_source_verified"
        ]
        is False,
        "block_route_insufficient": routes["block_factorized_sector_resolved"]["closes_now"]
        is False,
        "left_right_coherent": routes["block_factorized_sector_resolved"]["evidence"][
            "left_right_sector_split_coherent"
        ]
        is True,
        "sector_resolved_required": routes["block_factorized_sector_resolved"]["evidence"][
            "sector_resolved_C1_or_high_scale_source_required"
        ]
        is True,
        "monolithic_su5_shortcut_rejected": routes["block_factorized_sector_resolved"]["evidence"][
            "monolithic_su5_tensor_inherits_from_block_route"
        ]
        is False,
    }

    clue_checks = {
        "d7_equivariant_selector_present": clue["d7_equivariant_selector_present"] is True,
        "d7_qutrit_symmetry_selector_present": clue["d7_qutrit_symmetry_selector_present"] is True,
        "clock_shift_symmetry_preserved": clue["clock_shift_symmetry_preserved_until_source_breaks"]
        is True,
        "minimal_s3_stack": clue["minimal_equivariant_stack_s3"] is True,
        "clue_does_not_assign_slots": "does not by itself assign"
        in clue["implication_for_matter_routing"],
    }

    hybrid_checks = {
        "recommended_hybrid_strategy": hybrid["recommended_strategy"]
        == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES",
        "minimal_packet_six_items": len(hybrid["minimal_closing_packet"]) == 6,
        "path_A_supplies_source_origin": "selected operator/source origin" in hybrid["path_A_supplies"],
        "path_B_supplies_zero_modes": "family zero-mode basis" in hybrid["path_B_supplies"],
    }

    guardrail_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "target_fitting_excluded": src["what_closes_now"]["target_fitting_excluded"] is True,
    }

    theorem = {
        "name": "RouteCWeylPairMatterSlotBlockSectorImportTheorem",
        "proved": all(input_checks.values())
        and all(theorem_checks.values())
        and all(route_checks.values())
        and all(clue_checks.values())
        and all(hybrid_checks.values())
        and all(guardrail_checks.values()),
        "statement": (
            "The Weyl-pair matter-slot/block-sector source theorem attempt is "
            "imported as a reduction to the hybrid Galerkin packet. The SU(5)/E6 "
            "matter-slot route supplies structural charge-sector guidance but "
            "lacks selected source validation; the selected block route supplies "
            "honest coherence but lacks sector-resolved C1 routing. The next "
            "minimal object is a selected HYM/Strominger origin followed by "
            "Galerkin zero modes, L2 metrics, dotD/C1 responses, singlet-neutrino "
            "routing, and Weyl-pair normalization."
        ),
    }

    verdict = {
        "matter_slot_and_block_routes_compared": True,
        "monolithic_su5_shortcut_rejected": True,
        "clock_shift_symmetry_clue_imported": True,
        "hybrid_packet_identified": True,
        "selected_matter_slot_source_closed": False,
        "selected_blocksector_source_closed": False,
        "conditional_A_promoted_to_A_selected": False,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "input_checks": input_checks,
        "theorem_checks": theorem_checks,
        "route_checks": route_checks,
        "clue_checks": clue_checks,
        "hybrid_checks": hybrid_checks,
        "guardrail_checks": guardrail_checks,
        "routes": routes,
        "new_clue_from_qutrit_embedding": clue,
        "hybrid_closing_packet": hybrid,
        "what_closes_now": src["what_closes_now"],
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Weyl-Pair MatterSlot BlockSector Import v1

## Result

The Weyl-pair matter-slot/block-sector theorem attempt is now imported.

Route A, high-scale SU(5)/E6 matter slots:

```text
right structural dictionary
finite I_3/F transport is not the blocker
selected source validation remains open
```

Route B, selected block-sector data:

```text
left/right coherence is honest
u/e versus d/nuD sector-resolved C1 routing is not emitted
monolithic SU(5) inheritance from the block route is rejected
```

The q79 D7 equivariant clue helps select the active S3 stack, but it does not
assign matter slots by itself. The next object is therefore the hybrid packet:

```text
selected HYM/Strominger source
selected D_E, Riesz/Green, dotD
selected Galerkin zero modes and L2 metrics
selected 10_M/bar5_M/1_M or u,d,e,N sector routing
Weyl-pair A_selected normalization
```

No observed masses, mixings, CP phase, thresholds, benchmark values, or lifted
selected flags are used as selectors.

## Status

```text
ROUTEC_WEYLPAIR_MATTERSLOT_BLOCKSECTOR_IMPORTED_HYBRID_PACKET_NEXT
```

The next required artifact is:

```text
MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_weylpair_matter_slot_blocksector_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_weylpair_sector_charge_import": str(PREV_IMPORT),
                    "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem": str(SRC_CERT),
                },
                "theorem": theorem,
                "input_checks": input_checks,
                "theorem_checks": theorem_checks,
                "route_checks": route_checks,
                "clue_checks": clue_checks,
                "hybrid_checks": hybrid_checks,
                "guardrail_checks": guardrail_checks,
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
