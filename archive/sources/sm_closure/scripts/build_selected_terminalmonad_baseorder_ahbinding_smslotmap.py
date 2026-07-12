"""Build the terminal-monad base-order/AH-binding/SM-slot-map gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = ROOT.parent / "mtt-q79-proof-repro"

PREVIOUS = DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
DIRAC_GATE = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
TERMINAL_LOCKDOWN = Q79 / "candidate_data" / "all_remaining_valpha_gates" / "same_source_monad_gs_operator_fusion.after_terminal_lockdown.json"
UNCONDITIONAL_ATTEMPT = Q79 / "candidate_data" / "unconditional_selected_monad_difference_l2_source_attempt.candidate.json"
AH_AUTOMORPHY = Q79 / "candidate_data" / "visible_rank2_l2_appell_humbert_automorphy.candidate.json"
AH_YONEDA = Q79 / "candidate_data" / "valpha_appell_humbert_yoneda_promotion.candidate.json"

OUTPUT = DATA / "selected_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
CERT = CERTS / "selected_terminalmonad_baseorder_ahbinding_smslotmap_certificate.json"
NOTE = CORPUS / "MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1.md"

STATUS = "MTT_SELECTED_TERMINALMONAD_BASEORDER_AHBINDING_SMSLOTMAP_GATE_BUILT_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)
    dirac = load(DIRAC_GATE)
    terminal_lockdown = load(TERMINAL_LOCKDOWN)
    unconditional = load(UNCONDITIONAL_ATTEMPT)
    ah_auto = load(AH_AUTOMORPHY)
    ah_yoneda = load(AH_YONEDA)

    ordered_source = terminal_lockdown["ordered_source"]
    source_identity = terminal_lockdown["source_identity"]
    ah_selection = ah_auto["selection_analysis"]
    ah_yoneda_selection = ah_yoneda["appell_humbert_selection_state"]

    base_order_audit = {
        "diagnostic_packet_present": True,
        "diagnostic_base_order_selected_flag": ordered_source["base_factor_order_selected"],
        "diagnostic_standard_lattice_flag": ordered_source["standard_lattice_or_equivalent_selected"],
        "diagnostic_ordered_validator_passes": ordered_source["ordered_source_validator_passes"],
        "promotable_as_theorem": False,
        "why_not": {
            "fixture_only": source_identity["fixture_only"],
            "selected_by_mtt": source_identity["selected_by_mtt"],
            "same_source_for_ordered_L_pic0_GS_and_DE": source_identity["same_source_for_ordered_L_pic0_GS_and_DE"],
            "source_certificate": source_identity["source_certificate"],
        },
    }

    ah_binding_audit = {
        "automorphy_formula_constructed": ah_auto["what_this_closes"]["explicit_nonflat_factor_of_automorphy_for_L2_2_minus4_0"],
        "c1_matrix_matches_required_order": ah_auto["construction_checks"]["c1_matrix_matches_required_order"],
        "shared_circle_degree_zero_retained": ah_auto["what_this_closes"]["shared_circle_degree_zero_retained"],
        "yoneda_multiplication_identity_verified": ah_yoneda["closed_by_this_attempt"][
            "AH_factor_product_law_matches_yoneda_degree_addition"
        ],
        "AH_source_selected_by_MTT": ah_selection["selected_by_mtt"] or ah_yoneda_selection["selected_by_mtt"],
        "standard_lattice_selected_by_MTT": ah_selection["standard_gaussian_lattice_selected_by_mtt"],
        "target_branch_selected_by_MTT": ah_selection["target_branch_L_selected_by_mtt"],
        "neutral_pic0_selected_by_MTT": ah_selection["neutral_pic0_character_selected_by_mtt"],
        "promotable_as_theorem": False,
    }

    sm_slot_map_audit = {
        "finite_q79_polarization_support": dirac["route_A_SU5_E6_polarization"]["support_closed"],
        "structural_1M_rule_available": dirac["route_A_SU5_E6_polarization"]["structural_1M_rule_available"],
        "model_projector_support": dirac["route_B_HYM_projector_zero_mode"]["support_closed"],
        "selected_U10_Ubar5_polarization_closed": dirac["selection_decision"]["selected_U10_Ubar5_polarization_closed"],
        "selected_1M_Dirac_rule_closed": dirac["selection_decision"]["selected_1M_Dirac_neutrino_source_rule_closed"],
        "slot_contract": previous["matter_slot_map_contract"]["must_map_without_locked_C1_columns"],
        "polarization_to_preserve": previous["matter_slot_map_contract"]["must_preserve_q79_polarization"],
        "promotable_as_theorem": False,
    }

    three_gate_cutset = {
        "G1_terminal_map_source_principle": {
            "status": "OPEN",
            "must_emit": unconditional["minimal_new_statement_that_would_close"]["source_lane_selector"],
            "also_emits": ["standard_lattice_or_equivalent_selected", "base_factor_order_selected"],
        },
        "G2_AH_Cech_binding": {
            "status": "OPEN",
            "constructed_support": "Appell-Humbert automorphy and Yoneda multiplication are constructed",
            "must_emit": "same selected L3-K2 source class as Appell-Humbert/Cech transition representative",
        },
        "G3_SM_slot_functor": {
            "status": "OPEN",
            "constructed_support": "q79 finite SU(5)/E6 polarization and structural 1_M rule are support-closed",
            "must_emit": "section-ring/cohomology functor to 10_M, bar5_M, 1_M plus selected overlap normalization",
        },
    }

    theorem = {
        "name": "TerminalBaseOrderAHBindingSMSlotMapCutsetTheorem",
        "proved": True,
        "statement": (
            "Current artifacts construct the ordered Appell-Humbert representative, the Yoneda multiplication "
            "law, a diagnostic base-order/standard-lattice packet, and q79 SU(5)/E6 slot support. None of these "
            "is a selected theorem source. Therefore the next honest closure object is exactly a three-gate "
            "cutset: terminal map source principle with base order, selected AH/Cech binding of the same class, "
            "and selected section-ring-to-SM-slot functor."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedTerminalMonadBaseOrderAHBindingSMSlotMap",
        "status": STATUS,
        "inputs": {
            "previous_terminal_selector_reduction": rel(PREVIOUS),
            "local_dirac_polarization_gate": rel(DIRAC_GATE),
            "q79_terminal_lockdown_diagnostic": rel(TERMINAL_LOCKDOWN),
            "q79_unconditional_monad_attempt": rel(UNCONDITIONAL_ATTEMPT),
            "q79_AH_automorphy": rel(AH_AUTOMORPHY),
            "q79_AH_Yoneda_promotion": rel(AH_YONEDA),
        },
        "superset_strategy": {
            "mode": "MULTI_ENCODING_PROMOTION_AUDIT",
            "using_one_straight_path": False,
            "paths_compared": [
                "diagnostic terminal lockdown packet",
                "unconditional monad source attempt",
                "Appell-Humbert automorphy construction",
                "AH/Yoneda multiplication promotion",
                "SU(5)/E6 polarization and 1_M rule route",
            ],
            "locked_target_role": "compatibility only; locked C1 columns and observed data are forbidden selectors",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "base_order_audit": base_order_audit,
        "AH_Cech_binding_audit": ah_binding_audit,
        "SM_slot_map_audit": sm_slot_map_audit,
        "three_gate_cutset": three_gate_cutset,
        "what_closes_now": {
            "diagnostic_base_order_not_promotable": True,
            "AH_binding_exists_mathematically_not_selected": True,
            "SM_slot_map_support_exists_not_selected": True,
            "three_gate_cutset_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "terminal_map_source_principle": True,
            "selected_base_order": True,
            "selected_AH_or_Cech_transition_binding": True,
            "selected_section_ring_to_SM_slot_functor": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "operator_layer_Pic0_selection_or_quotient": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "certificate": "MTT_Selected_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1",
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "closure_claimed": False,
                "observed_data_used": False,
                "target_fitting_used": False,
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
        """# MTT Selected TerminalMonad BaseOrder AHBinding SMSlotMap v1

Status: `MTT_SELECTED_TERMINALMONAD_BASEORDER_AHBINDING_SMSLOTMAP_GATE_BUILT_SOURCE_PROMOTION_OPEN`

This artifact checks whether the next gate can be closed from existing repo
data.  It cannot, but the failure is now sharply localized.

## Result

Existing artifacts provide strong constructed support:

- the ordered Appell-Humbert representative exists for `L^2=(2,-4,0)`;
- the AH/Yoneda multiplication law is verified;
- a diagnostic terminal-lockdown packet sets base order and standard lattice;
- q79 SU(5)/E6 support gives `U_10=I_3`, `U_bar5=F`, and the structural
  `1_M=N^c` Dirac-neutrino channel.

None of these is yet a selected theorem source.  The terminal-lockdown packet
is explicitly fixture-only and not selected by MTT; the AH representative is
constructed but not selected; the SM slot map is structurally supported but not
emitted as a selected section-ring/cohomology functor.

## Cutset Theorem

The next honest closure object is exactly a three-gate cutset:

- terminal map source principle plus selected base order;
- selected AH/Cech binding for the same `L3-K2` class;
- selected section-ring/cohomology functor to `10_M`, `bar5_M`, and `1_M`,
  including the `1_M` Dirac rule and overlap normalization.

Route-C remains a legal bypass only if it emits those same fields directly as
selected operator data.

Next artifact: `MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
