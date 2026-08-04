"""Try to promote the Weyl-pair matter-slot/block-sector routing source."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"
Q79_DATA = Q79 / "candidate_data"
Q79_CORPUS = Q79 / "proof_corpus"

PREVIOUS = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
MATTER_TWO_PATH = Q79_DATA / "selected_matter_source_two_path_exploration.candidate.json"
MATTER_ATTEMPT = Q79_DATA / "selected_matter_slot_transversality_source_attempt.candidate.json"
BLOCK_SPLIT = Q79_DATA / "su5_block_orientation_route_split.candidate.json"
D7_SYMM = Q79_CORPUS / "Visible_Twisted_D7_Qutrit_Symmetry_Selector_v1.md"
D7_EQUIV = Q79_CORPUS / "Visible_Twisted_D7_Equivariant_Embedding_Selector_v1.md"

OUTPUT = DATA / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem.candidate.json"
CERT = CERTS / "selected_routec_weylpair_matter_slot_or_blocksector_source_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_WeylPair_MatterSlot_or_BlockSector_Source_Theorem_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET"
NEXT = "MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text_has(path: Path, needle: str) -> bool:
    return needle in path.read_text(encoding="utf-8")


def main() -> None:
    previous = load(PREVIOUS)
    two_path = load(MATTER_TWO_PATH)
    matter_attempt = load(MATTER_ATTEMPT)
    block_split = load(BLOCK_SPLIT)

    symmetry_clue = {
        "d7_qutrit_symmetry_selector_present": D7_SYMM.exists(),
        "d7_equivariant_selector_present": D7_EQUIV.exists(),
        "clock_shift_symmetry_preserved_until_source_breaks": text_has(D7_EQUIV, "Without an extra selected source that breaks the qutrit"),
        "minimal_equivariant_stack_s3": text_has(D7_EQUIV, "minimal equivariant twisted D7 stack = S3"),
        "implication_for_matter_routing": (
            "Clock/shift exchange symmetry can pick the active S3 stack, but it does not by itself assign "
            "10_M, bar5_M, and 1_M matter slots.  A further selected source or Galerkin zero-mode packet "
            "must break or represent the matter-slot split."
        ),
    }

    high_scale_route = {
        "name": "high_scale_SU5_E6_matter_slot_route",
        "status": "CONDITIONAL_NOT_SELECTED",
        "closes_now": False,
        "evidence": {
            "finite_I_F_transport_not_blocker": two_path["calculation_results"]["finite_I_F_transport_not_the_blocker"],
            "selected_matter_source_validator_ready": two_path["calculation_results"]["selected_matter_source_validator_ready"],
            "selected_transversality_attempt_promotes": matter_attempt["calculation_results"]["promotes_su5_matter_slot_transversality"],
            "selected_source_verified": matter_attempt["calculation_results"]["selected_source_verified"],
        },
        "blocker": "Needs selected zero-mode basis, selected L2 metrics, projector retention, and same-branch D_E/dotD source.",
    }

    block_sector_route = {
        "name": "block_factorized_sector_resolved_route",
        "status": "HONEST_SELECTED_BLOCK_DATA_INSUFFICIENT",
        "closes_now": False,
        "evidence": {
            "left_right_sector_split_coherent": block_split["calculation_results"]["left_right_sector_split_coherent_under_current_branch_packets"],
            "su5_multiplets_uniform": block_split["calculation_results"]["su5_multiplets_uniform_under_current_branch_packets"],
            "sector_resolved_C1_or_high_scale_source_required": block_split["calculation_results"]["sector_resolved_C1_or_high_scale_source_required"],
            "monolithic_su5_tensor_inherits_from_block_route": block_split["calculation_results"]["monolithic_su5_tensor_inherits_from_block_route"],
        },
        "blocker": "Current block data gives left/right coherence, not u/e versus d/nuD sector-resolved C1 routing.",
    }

    hybrid = {
        "recommended_strategy": two_path["verdict"]["best_next_path"],
        "why_hybrid": two_path["coupling_between_paths"]["why_not_either_alone"],
        "path_A_supplies": two_path["coupling_between_paths"]["path_A_supplies"],
        "path_B_supplies": two_path["coupling_between_paths"]["path_B_supplies"],
        "minimal_closing_packet": [
            "selected HYM/Strominger or equivalent selected operator/source packet for D_E",
            "Riesz projectors, complement gap, reduced Green operator, and truncation certificate",
            "selected zero-mode bases and L2 metrics for 10_M, bar5_M, and 1_M or sector-resolved u,d,e,N",
            "selected dotD_alpha1 and primitive C1 responses in the same branch",
            "proof that the 1_M Dirac-neutrino leg routes with the shift/non-10 side",
            "normalization compatibility with the Weyl-pair A_selected basis",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedRouteCWeylPairMatterSlotOrBlockSectorSourceTheorem",
        "status": STATUS,
        "inputs": {
            "previous_sector_charge_certificate": rel(PREVIOUS),
            "q79_selected_matter_two_path": rel(MATTER_TWO_PATH),
            "q79_selected_matter_slot_attempt": rel(MATTER_ATTEMPT),
            "q79_su5_block_split": rel(BLOCK_SPLIT),
            "q79_d7_qutrit_symmetry_selector": rel(D7_SYMM),
            "q79_d7_equivariant_selector": rel(D7_EQUIV),
        },
        "theorem_attempt": {
            "goal": "Prove selected source routing for Z -> u,e and X -> d,nuD.",
            "closed_now": False,
            "reason_not_closed": "Both legal source routes remain blocked before the hybrid selected Galerkin/operator packet is supplied.",
            "previous_locked_target_not_promoted": previous["superset_paths"]["combined_locked_target_use"]["source_data_independently_selects_route"] is False,
        },
        "routes": {
            "high_scale_SU5_E6": high_scale_route,
            "block_factorized_sector_resolved": block_sector_route,
        },
        "new_clue_from_qutrit_embedding": symmetry_clue,
        "hybrid_closing_packet": hybrid,
        "what_closes_now": {
            "matter_slot_and_block_routes_compared": True,
            "clock_shift_symmetry_clue_imported": True,
            "monolithic_su5_shortcut_rejected_for_current_block_source": True,
            "hybrid_hym_then_galerkin_packet_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_hym_or_strominger_operator_source": True,
            "selected_galerkin_zero_mode_bases": True,
            "selected_L2_metrics_and_projector_retention": True,
            "selected_dotD_and_C1_responses": True,
            "selected_1M_singlet_neutrino_shift_rule": True,
            "promote_conditional_weylpair_A_to_A_selected": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C WeylPair MatterSlot or BlockSector Source Theorem

Status: `MTT_SELECTED_ROUTEC_WEYLPAIR_MATTERSLOT_OR_BLOCKSECTOR_SOURCE_THEOREM_REDUCED_TO_HYBRID_GALERKIN_PACKET`

Goal:

```text
Z -> u,e
X -> d,nuD
```

This theorem is not closed yet.  It is reduced to one hybrid packet.

## Route A: High-Scale Matter Slots

The SU(5)/E6 route gives the right structural dictionary:

```text
u,e   -> 10_M clock/phase side
d     -> bar5_M shift side
nuD   -> 1_M singlet, needing a Dirac-neutrino shift rule
```

But q79's selected matter-slot transversality attempt still fails selected
source validation.  The finite `I_3/F` algebra is not the blocker; the selected
zero-mode basis, L2 metrics, projector retention, and same-branch `D_E/dotD`
source are.

## Route B: Block-Sector Route

The honest selected block data gives left/right coherence.  It does not source
the monolithic SU(5) tensor, and it does not split the right-family sectors into
`u,e` versus `d,nuD`.  Therefore Route B needs sector-resolved C1/dotD response
data, not just the current Phi_fin orientation table.

## New Clue

The q79 D7 equivariant selector says clock/shift exchange symmetry is preserved
unless a selected source breaks it.  This helps select the active S3 stack, but
it does not assign matter slots by itself.  For matter routing, the symmetry
must be represented by selected zero modes or broken by a selected operator
source.

## Correct Next Object

Build the hybrid packet:

```text
selected HYM/Strominger source
  -> selected D_E, Riesz/Green, dotD
  -> selected Galerkin zero modes and L2 metrics
  -> selected 10_M/bar5_M/1_M or u,d,e,N sector routing
  -> Weyl-pair A_selected normalization
```

Next artifact: `MTT_Selected_RouteC_Hybrid_MatterSlot_Galerkin_Source_Packet_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
