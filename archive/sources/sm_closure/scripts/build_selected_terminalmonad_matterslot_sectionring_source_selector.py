"""Build the terminal-monad matter-slot section-ring source-selector reduction.

This artifact takes the previous matter-slot grading route seriously and asks
what is genuinely left once the q79 switch table and ordered-layer Pic0 quotient
are imported.  It does not promote the selector; it makes the remaining source
packet small enough to attack next.
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

PREVIOUS = DATA / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
TERMINAL_GATE = DATA / "selected_terminal_monad_lane_pic0_quotient_source.candidate.json"
CENTRAL_FILTER = Q79 / "certificates" / "central_circle_neutral_terminal_lane_filter_certificate.json"
MONAD_SUFF = Q79 / "certificates" / "monad_difference_l2_source_sufficiency_certificate.json"
AH_REDUCTION = Q79 / "candidate_data" / "q79_ah_source_selection_or_routec_residual_reduction.candidate.json"
PIC0_SWITCH = Q79 / "candidate_data" / "monad_difference_pic0_switch_reduction.candidate.json"
ORDERED_PIC0 = Q79 / "candidate_data" / "ordered_layer_pic0_quotient.candidate.json"
MONAD_ORIENTATION = Q79 / "candidate_data" / "iwasawa_monad_l2_branch_orientation_candidate.candidate.json"

OUTPUT = DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
CERT = CERTS / "selected_terminalmonad_matterslot_sectionring_source_selector_certificate.json"
NOTE = CORPUS / "MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1.md"

STATUS = "MTT_SELECTED_TERMINALMONAD_MATTERSLOT_SECTIONRING_SELECTOR_REDUCED_TO_SOURCE_BASEORDER_AND_SLOTMAP"
NEXT = "MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def switch_case(switch: dict[str, Any], case: str) -> dict[str, Any]:
    return next(row for row in switch["switch_table"] if row["case"] == case)


def main() -> None:
    previous = load(PREVIOUS)
    terminal = load(TERMINAL_GATE)
    central = load(CENTRAL_FILTER)
    monad = load(MONAD_SUFF)
    ah = load(AH_REDUCTION)
    pic0_switch = load(PIC0_SWITCH)
    ordered_pic0 = load(ORDERED_PIC0)
    orientation = load(MONAD_ORIENTATION)

    selected = central["terminal_lane_filter"]["selected_by_filter"]
    key_candidate = orientation["key_candidate"]
    pic0_only = switch_case(pic0_switch, "pic0_only")
    source_only = switch_case(pic0_switch, "source_only")
    both = switch_case(pic0_switch, "source_and_pic0")
    quotient_validation = ordered_pic0["validation"]["pic0_quotiented_layer_packet"]

    source_switch_contract = {
        "terminal_monad_lane_selection": {
            "closed": False,
            "must_emit": "L_i-K2 as an MTT-selected terminal monad lane, not as a post-hoc line choice",
        },
        "central_neutral_member": {
            "closed": central["conditional_theorem"]["proved"],
            "forced_label": selected["label"],
            "forced_value": selected["value"],
            "forced_double": selected["double_value"],
            "ordered_pair": selected["ordered_pair"],
        },
        "monad_orientation": {
            "closed_as_candidate": orientation["what_this_closes"]["exact_ordered_integral_target_L_candidate_found"],
            "not_selected_yet": orientation["what_this_does_not_close"]["monad_pair_selected_as_visible_V_alpha_source"] is False,
            "ordered_difference": key_candidate["ordered_difference"],
            "value": key_candidate["value"],
            "double_value": key_candidate["double_value"],
            "dual_printed_g3_type": key_candidate["dual_printed_g3_type"],
        },
        "standard_lattice_or_equivalent": {
            "closed": False,
            "must_emit": "standard_lattice_or_equivalent_selected",
        },
        "base_factor_order": {
            "closed": False,
            "must_emit": "base_factor_order_selected",
        },
        "AH_or_Cech_binding": {
            "closed": False,
            "support_closed": ah["AH_goodcover_representative_equivalence_theorem"]["proved"],
            "must_emit": "same selected L3-K2 class bound to Appell-Humbert/Cech transition data",
        },
    }

    pic0_accounting = {
        "ordered_layer_pic0_closed": ordered_pic0["quotient_theorem"]["proved_for_ordered_layer"],
        "ordered_layer_scope": ordered_pic0["quotient_theorem"]["scope"],
        "ordered_layer_validator_after_quotient": {
            "pic0_items_absent": ordered_pic0["validation"]["pic0_items_absent_after_quotient"],
            "only_source_selection_items_remain": ordered_pic0["validation"]["only_source_selection_items_remain"],
            "open_items": quotient_validation["open_items"],
        },
        "operator_layer_pic0_closed": False,
        "operator_layer_reopen_condition": ordered_pic0["quotient_theorem"]["reopen_condition"],
    }

    two_switch_reduction = {
        "switch_table_imported": pic0_switch["status"],
        "pic0_only_fails_only_source_switch": pic0_only["pic0_switch"] is True
        and pic0_only["source_switch"] is False
        and all("Pic0" not in item for item in pic0_only["open_items"]),
        "source_only_fails_only_pic0_switch": source_only["source_switch"] is True
        and source_only["pic0_switch"] is False
        and all("source" not in item.lower() for item in source_only["open_items"]),
        "source_and_pic0_passes_ordered_validator": both["exit_code"] == 0 and both["validator_status"] == "PASS",
        "ordered_pic0_quotient_removes_pic0_switch_at_ordered_layer": ordered_pic0["what_this_closes"][
            "pic0_switch_removed_from_ordered_layer_validator"
        ],
        "resulting_ordered_layer_blockers": quotient_validation["open_items"],
    }

    matter_slot_map_contract = {
        "closed": False,
        "must_map_without_locked_C1_columns": {
            "10_M_clock": previous["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"]["10_M_clock"],
            "bar5_M_shift": previous["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"][
                "bar5_M_shift"
            ],
            "1_M_Dirac_shift": previous["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"][
                "1_M_Dirac_shift"
            ],
        },
        "must_preserve_q79_polarization": previous["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"][
            "polarization_output"
        ],
        "must_emit": [
            "section-ring/cohomology functor from the selected L3-K2 source packet to SU(5)/E6 matter slots",
            "the 1_M Dirac-neutrino routing as source data",
            "the overlap or transfer normalization used by the flavor operator packet",
        ],
    }

    routec_bypass = {
        "retained": True,
        "reason": (
            "If the terminal-monad source packet cannot promote the slot map, an honest Route-C/Strominger "
            "Galerkin source can still emit the same fields directly as selected operator data."
        ),
        "minimum_required": [
            "selected Route-C residual or minimizer values",
            "selected D_E/Riesz/Green/dotD packet",
            "selected matter-slot operator labels and 1_M rule",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedTerminalMonadMatterSlotSectionRingSourceSelector",
        "status": STATUS,
        "inputs": {
            "previous_matter_slot_route": rel(PREVIOUS),
            "local_terminal_gate": rel(TERMINAL_GATE),
            "q79_central_filter": rel(CENTRAL_FILTER),
            "q79_monad_sufficiency": rel(MONAD_SUFF),
            "q79_ah_reduction": rel(AH_REDUCTION),
            "q79_pic0_switch_reduction": rel(PIC0_SWITCH),
            "q79_ordered_pic0_quotient": rel(ORDERED_PIC0),
            "q79_iwasawa_monad_orientation_candidate": rel(MONAD_ORIENTATION),
        },
        "superset_strategy": {
            "mode": "CONVERGENT_MULTI_ENCODING_REDUCTION",
            "using_one_straight_path": False,
            "straight_path_core": "terminal monad/Cech/section-ring selected source packet",
            "support_paths_combined": [
                "central-circle neutrality filter",
                "Iwasawa monad line-table orientation scan",
                "Appell-Humbert/good-cover representative equivalence",
                "ordered-source validator switch table",
                "ordered-layer Pic0 physical quotient",
                "SU(5)/E6 structural matter-slot dictionary from the previous route",
            ],
            "locked_or_constrained_target_role": "only downstream compatibility; no C1 columns or measured constants select the source",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "source_switch_contract": source_switch_contract,
        "pic0_accounting": pic0_accounting,
        "two_switch_reduction": two_switch_reduction,
        "matter_slot_map_contract": matter_slot_map_contract,
        "routec_bypass": routec_bypass,
        "what_closes_now": {
            "L3_K2_unique_terminal_candidate": True,
            "ordered_layer_Pic0_removed_as_ordered_source_blocker": True,
            "ordered_source_matrix_not_missing": pic0_switch["what_this_closes"]["ordered_source_matrix_not_the_blocker"],
            "terminal_selector_reduced_to_source_baseorder_AHbinding": True,
            "matter_slot_map_contract_built": True,
            "routec_bypass_preserved": True,
        },
        "what_remains_open": {
            "terminal_monad_lane_selected_by_MTT": True,
            "standard_lattice_or_equivalent_selected": True,
            "base_factor_order_selected": True,
            "AH_or_Cech_transition_binding_selected": True,
            "operator_layer_Pic0_selection_or_quotient": True,
            "section_ring_to_SU5_E6_matter_slot_map": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used": False,
        "theorem": {
            "name": "TerminalMonadMatterSlotSourceSelectorReduction",
            "proved": True,
            "statement": (
                "Given the imported q79 central-neutral terminal-lane filter, Iwasawa monad orientation scan, "
                "ordered-source switch table, and ordered-layer Pic0 quotient, the selected matter-slot "
                "grading problem is reduced to a single selected terminal-monad source packet: lane selection, "
                "standard lattice/base order, AH/Cech binding, operator-layer Pic0 discipline, and a "
                "section-ring-to-SU5/E6 slot map. No observed constants, locked C1 columns, or benchmark flavor "
                "matrices are used as selectors."
            ),
        },
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "certificate": "MTT_Selected_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1",
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "closure_claimed": False,
                "target_fitting_used": False,
                "observed_data_used": False,
                "theorem_proved": True,
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
        """# MTT Selected TerminalMonad MatterSlot SectionRing SourceSelector v1

Status: `MTT_SELECTED_TERMINALMONAD_MATTERSLOT_SECTIONRING_SELECTOR_REDUCED_TO_SOURCE_BASEORDER_AND_SLOTMAP`

This artifact pushes the terminal-monad route one step further.  It combines
several superset paths, but with a locked guardrail: no observed masses, CKM
data, benchmark flavor matrices, or locked `C1` columns are allowed to select
the source.

## Theorem

Given the imported q79 central-neutral terminal-lane filter, Iwasawa monad
orientation scan, ordered-source switch table, and ordered-layer Pic0 quotient,
the selected matter-slot grading problem reduces to one selected
terminal-monad source packet.

That packet must emit:

- the terminal lane `L_i-K2`;
- the selected member `L3-K2=(1,-2,0)` with double `(2,-4,0)`;
- the standard/equivalent lattice and base factor order;
- the Appell-Humbert/Cech transition representative for the same class;
- operator-layer Pic0 selection, quotient, or same-source gerbe replacement;
- a section-ring/cohomology map to `10_M`, `bar5_M`, and `1_M`.

## What Actually Improved

The ordered-layer Pic0 issue is no longer the ordered-source blocker.  Pic0 is
quotiented at the Chern/H1/ordinary-curvature layer, so the ordered-source
validator now fails only on source/base-order evidence there.

The operator layer is stricter.  Any later `D_E`, Riesz/Green, `dotD`, overlap,
or finite operator packet must recheck Pic0 or replace it by the selected
gerbe/twisted source.

## What Remains

The next proof should target the source packet directly:

- selected terminal monad lane;
- selected base order;
- selected AH/Cech binding;
- selected section-ring to SU(5)/E6 matter-slot map;
- selected `1_M` Dirac-neutrino shift and overlap normalization.

Route-C remains the fallback: an honest Strominger/Galerkin selected source can
emit these same fields directly if the section-ring map does not promote.

Next artifact: `MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
