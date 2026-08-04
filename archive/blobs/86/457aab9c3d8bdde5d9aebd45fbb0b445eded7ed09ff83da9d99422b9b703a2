"""Build the matter-slot grading / section-ring readout attempt.

The previous artifact proved that selected rho_s invariants are too symmetric
to read out the SU(5)/E6 matter-slot split.  This artifact tests the four legal
replacement routes and ranks the terminal monad / section-ring lane as the
minimal next contract, while keeping it open because the selector is not yet
proved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_matterslot_transversality_readout_functional.candidate.json"
TERMINAL_LOCAL = DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"
CENTRAL_FILTER = Q79 / "certificates" / "central_circle_neutral_terminal_lane_filter_certificate.json"
MONAD_SUFF = Q79 / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json"
AH_REDUCTION = Q79 / "candidate_data" / "q79_ah_source_selection_or_routec_residual_reduction.candidate.json"
E6_DICT = Q79 / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
SU5_SOURCE = Q79 / "certificates" / "selected_su5_source_proof_attempt_certificate.json"
SU5_TRANS = Q79 / "certificates" / "su5_matter_slot_transversality_certificate.json"
ROUTEC_HYBRID = DATA / "selected_routec_hybrid_matter_slot_galerkin_source_packet.candidate.json"

OUTPUT = DATA / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
CERT = CERTS / "selected_matterslot_grading_or_sectionring_readout_certificate.json"
NOTE = CORPUS / "MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1.md"

STATUS = "MTT_SELECTED_MATTERSLOT_GRADING_SECTIONRING_READOUT_ATTEMPT_REDUCED_TO_TERMINAL_MONAD_SELECTOR"
NEXT = "MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    terminal = load(TERMINAL_LOCAL)
    central = load(CENTRAL_FILTER)
    monad = load(MONAD_SUFF)
    ah = load(AH_REDUCTION)
    e6 = load(E6_DICT)
    su5_source = load(SU5_SOURCE)
    su5_trans = load(SU5_TRANS)
    hybrid = load(ROUTEC_HYBRID)

    selected_l3 = central["terminal_lane_filter"]["selected_by_filter"]
    terminal_gate = terminal["gate_results"]
    monad_open = monad["what_this_does_not_close"]
    ah_open = ah["what_remains_open"]

    route_candidates = [
        {
            "id": "typed_monad_cech_sectionring",
            "rank": 1,
            "support_closed": (
                central["conditional_theorem"]["proved"] is True
                and monad["relative_theorem"]["proved"] is True
                and ah["AH_goodcover_representative_equivalence_theorem"]["proved"] is True
            ),
            "selected_closed": False,
            "why_primary": (
                "It is the only current route that can add actual source labels/degrees rather than another "
                "sector-invariant rho_s readout.  It already has conditional uniqueness and validator sufficiency."
            ),
            "open_items": [
                "terminal monad lane source selector",
                "standard/equivalent lattice and base factor order",
                "Pic0 selection or operator-layer quotient",
                "binding L3-K2 to AH/Cech transition data",
                "promotion from visible line-source label to SM matter-slot grading",
            ],
        },
        {
            "id": "selected_su5_e6_source_identity",
            "rank": 2,
            "support_closed": su5_trans["calculation_results"]["finite_transversality_theorem_closed"],
            "selected_closed": su5_source["guardrails"]["claims_selected_U10_Ubar5"],
            "why_primary": "Excellent structural target, but current q79 certificate says selected U10/Ubar5 source is still absent.",
            "open_items": su5_source["minimal_closing_packet"]["must_include"],
        },
        {
            "id": "samebranch_operator_channel_grading",
            "rank": 3,
            "support_closed": hybrid["current_support"]["model_zero_cluster_available"]
            if "current_support" in hybrid and "model_zero_cluster_available" in hybrid["current_support"]
            else True,
            "selected_closed": False,
            "why_primary": "Would be the most direct physical route, but current Galerkin/matter-slot packet still gives identity transport and no 1_M rule.",
            "open_items": [
                "selected zero-mode operator channel labels",
                "non-uniform family/slot transport from same selected source",
                "selected 1_M Dirac-neutrino channel",
            ],
        },
        {
            "id": "locked_c1_inverse_readout",
            "rank": 99,
            "support_closed": True,
            "selected_closed": False,
            "why_primary": "Rejected: it distinguishes the target partition but would use the locked splitter columns as a source selector.",
            "open_items": ["forbidden as proof source"],
        },
    ]

    terminal_monad_contract = {
        "name": "SelectedTerminalMonadMatterSlotSectionRingSourceSelector",
        "source_selector_to_prove": {
            "terminal_lane": "L_i-K2",
            "central_circle_filter": "z=0",
            "forced_label_inside_lane": selected_l3["label"],
            "forced_value": selected_l3["value"],
            "forced_double": selected_l3["double_value"],
            "ordered_pair": selected_l3["ordered_pair"],
        },
        "must_bind_to_matter_slot_grading": {
            "10_M_clock": ["u", "e"],
            "bar5_M_shift": ["d"],
            "1_M_Dirac_shift": ["nuD"],
            "operator_channels": e6["representation_dictionary"]["operator_channels"],
            "polarization_output": su5_trans["calculation_results"]["selected_packet"],
        },
        "source_requirements": [
            "MTT selects terminal monad lane L_i-K2, not a post-hoc line choice",
            "central circle neutrality selects L3-K2 within that lane",
            "standard/equivalent lattice and base order are selected",
            "AH/Cech transition representative is bound to the same selected source class",
            "Pic0 is selected, quotient-invariant at operator layer, or replaced by same-source gerbe/twisted D_E",
            "section-ring/cohomology labels map to SU(5)/E6 matter slots without locked C1 target columns",
        ],
    }

    selection_decision = {
        "selected_matter_slot_grading_readout_closed": False,
        "primary_route_selected_for_next_attempt": "typed_monad_cech_sectionring",
        "terminal_monad_selector_closed": terminal_gate["selected_terminal_lane_pic0_source_proved"],
        "central_circle_filter_closed": central["what_this_closes"]["central_circle_neutrality_filter_inside_terminal_lane"],
        "monad_sufficiency_closed_conditionally": monad["what_this_closes"][
            "sufficiency_of_selected_monad_difference_for_ordered_source_gate"
        ],
        "ah_goodcover_equivalence_closed": ah["what_closes_now"][
            "AH_or_goodcover_selection_reduced_to_single_source_class_selection"
        ],
        "reason": (
            "The terminal monad/section-ring route is sufficient and uniquely filtered inside its lane, "
            "but actual lane selection, base-order selection, Pic0/operator-layer discipline, and the map "
            "from visible line-source labels to SM matter-slot grading are still open."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedMatterSlotGradingOrSectionRingReadout",
        "status": STATUS,
        "inputs": {
            "previous_readout_attempt": rel(PREVIOUS),
            "local_terminal_monad_pic0_gate": rel(TERMINAL_LOCAL),
            "q79_central_circle_filter": rel(CENTRAL_FILTER),
            "q79_monad_sufficiency": rel(MONAD_SUFF),
            "q79_ah_source_reduction": rel(AH_REDUCTION),
            "q79_e6_dictionary": rel(E6_DICT),
            "q79_su5_source_attempt": rel(SU5_SOURCE),
            "q79_su5_transversality": rel(SU5_TRANS),
            "routec_hybrid_matter_slot_packet": rel(ROUTEC_HYBRID),
        },
        "superset_strategy": {
            "mode": "RANKED_MULTI_ROUTE_READOUT_SEARCH",
            "using_one_straight_path": False,
            "primary_route": "typed monad/Cech/section-ring source selector",
            "support_routes": [
                "selected SU(5)/E6 structural dictionary",
                "q79 finite transversality",
                "same-branch stationary rho_s no-go",
                "Route-C/Galerkin operator-channel support",
            ],
            "locked_target_role": "forbidden as a selector; only checks downstream compatibility",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "route_candidates": route_candidates,
        "terminal_monad_sectionring_contract": terminal_monad_contract,
        "selection_decision": selection_decision,
        "what_closes_now": {
            "primary_route_ranked": True,
            "central_circle_filter_imported": True,
            "terminal_lane_conditional_uniqueness_imported": terminal_gate["terminal_lane_conditional_uniqueness_imported"],
            "monad_validator_sufficiency_imported": True,
            "AH_Cech_representative_equivalence_imported": True,
            "selected_grading_still_open": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_terminal_monad_lane_source_selector": monad_open["actual_MTT_selection_of_L3_minus_K2"],
            "selected_lattice_and_base_factor_order": ah_open["selected_lattice_and_base_factor_order"],
            "operator_layer_Pic0_selection_or_quotient": ah_open["operator_layer_Pic0_selection_or_quotient"],
            "binding_L3_minus_K2_to_AH_or_Cech_transitions": ah_open["binding_L3_minus_K2_to_AH_or_Cech_transitions"],
            "section_ring_to_SU5_E6_matter_slot_map": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
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
                "closure_claimed": False,
                "target_fitting_used": False,
                "primary_route": "typed_monad_cech_sectionring",
                "selected_grading_readout_closed": False,
                "next_required_artifact": NEXT,
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected MatterSlot Grading or SectionRing Readout

Status: `MTT_SELECTED_MATTERSLOT_GRADING_SECTIONRING_READOUT_ATTEMPT_REDUCED_TO_TERMINAL_MONAD_SELECTOR`

This artifact tests the possible selected readouts that could break the
`u,d,e,N` symmetry left by the universal adjoint `rho_s`.

## Result

The primary route is now the typed monad/Cech/section-ring lane.

Why:

- the central-circle filter proves that, inside the terminal monad lane, the
  unique central-neutral difference is `L3-K2=(1,-2,0)`;
- the monad-difference sufficiency certificate proves that if the source
  selector and Pic0 fields are supplied, the ordered-source validator passes;
- the AH/good-cover theorem removes literal cover choice as an independent
  physical selector;
- unlike `rho_s` invariants, monad/section data can carry actual labels and
  degrees.

## What Remains Open

This does not yet close the matter-slot grading.  The next theorem must prove:

- MTT selects the terminal monad lane `L_i-K2`;
- the central-circle filter selects `L3-K2`;
- the standard/equivalent lattice and base order are selected;
- Pic0 is selected, quotient-invariant at operator layer, or replaced by a
  same-source gerbe/twisted `D_E`;
- the selected section/cohomology labels map to `10_M`, `bar5_M`, and `1_M`
  matter slots.

Only after that can the source emit:

- `10_M -> u,e`,
- `bar5_M -> d`,
- `1_M=N^c -> nuD`,
- `U_10=I_3`, `U_bar5=F`,
- and the same-branch normalization link.

Next artifact: `MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
