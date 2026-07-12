"""Audit selected Weyl-pair matter-slot/block-sector theorem attempt."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET"
NEXT = "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    theorem = data["theorem_attempt"]
    routes = data["routes"]
    clue = data["new_clue_from_qutrit_embedding"]
    hybrid = data["hybrid_closing_packet"]

    checks = [
        check("status", data["status"] == STATUS, data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check(
            "theorem reduced not closed",
            theorem["closed_now"] is False and theorem["previous_locked_target_not_promoted"] is True,
            theorem,
        ),
        check(
            "high-scale route conditional",
            routes["high_scale_SU5_E6"]["closes_now"] is False
            and routes["high_scale_SU5_E6"]["evidence"]["finite_I_F_transport_not_blocker"] is True
            and routes["high_scale_SU5_E6"]["evidence"]["selected_source_verified"] is False,
            routes["high_scale_SU5_E6"],
        ),
        check(
            "block route insufficient",
            routes["block_factorized_sector_resolved"]["closes_now"] is False
            and routes["block_factorized_sector_resolved"]["evidence"]["left_right_sector_split_coherent"] is True
            and routes["block_factorized_sector_resolved"]["evidence"]["sector_resolved_C1_or_high_scale_source_required"] is True
            and routes["block_factorized_sector_resolved"]["evidence"]["monolithic_su5_tensor_inherits_from_block_route"] is False,
            routes["block_factorized_sector_resolved"],
        ),
        check(
            "clock shift clue imported",
            clue["clock_shift_symmetry_preserved_until_source_breaks"] is True
            and clue["minimal_equivariant_stack_s3"] is True
            and "does not by itself assign" in clue["implication_for_matter_routing"],
            clue,
        ),
        check(
            "hybrid packet specified",
            hybrid["recommended_strategy"] == "HYBRID_SELECTED_HYM_ORIGIN_THEN_GALERKIN_ZERO_MODES"
            and len(hybrid["minimal_closing_packet"]) == 6,
            hybrid,
        ),
        check(
            "no closure or fitting",
            data["closure_claimed"] is False and data["target_fitting_used"] is False,
            {"closure_claimed": data["closure_claimed"], "target_fitting_used": data["target_fitting_used"]},
        ),
        check("next artifact", data["next_required_artifact"] == NEXT, data["next_required_artifact"]),
        check(
            "note records hybrid reduction",
            "Route A" in note
            and "Route B" in note
            and "clock/shift exchange symmetry" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]
    print("\nMTT selected Route-C Weyl-pair matter-slot/block-sector theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
