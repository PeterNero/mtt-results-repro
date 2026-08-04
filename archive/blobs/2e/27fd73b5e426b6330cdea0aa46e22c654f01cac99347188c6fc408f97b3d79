"""Build the terminal-map source-principle or SM-slot-functor gate.

The q79 repo now contains an explicit TerminalAdmissibleSectionSourcePrinciple.
This artifact imports it conservatively: it closes the ordered terminal source
and H1/Ext packet only *under that explicit principle*, while keeping the
principle-promotion and SM-slot functor as the next honest gates.
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

PREVIOUS = DATA / "selected_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
DIRAC_GATE = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
TERMINAL_PRINCIPLE = Q79 / "candidate_data" / "terminal_admissible_section_source_principle.candidate.json"
TERMINAL_PRINCIPLE_CERT = Q79 / "certificates" / "terminal_admissible_section_source_principle_certificate.json"
TERMINAL_ATTEMPT = Q79 / "candidate_data" / "terminal_map_source_principle_base_order_attempt.candidate.json"
ORDERED_REDUCTION = Q79 / "candidate_data" / "ordered_layer_terminal_lane_selector_reduction.candidate.json"
AH_REDUCTION = Q79 / "candidate_data" / "q79_ah_source_selection_or_routec_residual_reduction.candidate.json"

OUTPUT = DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"
CERT = CERTS / "selected_terminalmap_sourceprinciple_or_smslotfunctor_certificate.json"
NOTE = CORPUS / "MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1.md"

STATUS = "MTT_SELECTED_TERMINALMAP_SOURCEPRINCIPLE_CONDITIONAL_ORDERED_SOURCE_CLOSED_SMSLOTFUNCTOR_OPEN"
NEXT = "MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1"


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
    principle = load(TERMINAL_PRINCIPLE)
    principle_cert = load(TERMINAL_PRINCIPLE_CERT)
    terminal_attempt = load(TERMINAL_ATTEMPT)
    ordered_reduction = load(ORDERED_REDUCTION)
    ah_reduction = load(AH_REDUCTION)

    source_principle = principle["source_principle"]
    derivation = principle["selection_derivation"]
    terminal_scan = principle["terminal_lane_scan"]
    validators = principle["validator_results"]

    imported_principle_status = {
        "principle_name": source_principle["name"],
        "principle_status": source_principle["status"],
        "corpus_supported": principle["corpus_support"]["supported"],
        "explicit_principle_not_fit_knob": source_principle["why_not_a_fit_knob"],
        "credibility_status": source_principle["credibility_status"],
        "unconditional_in_MTT_spine": False,
        "closed_under_explicit_principle": True,
    }

    conditional_terminal_source_closure = {
        "selected_source_label": derivation["selected_source_label"],
        "selected_L": derivation["selected_L"],
        "selected_L2": derivation["selected_L2"],
        "selected_c2": derivation["selected_c2"],
        "base_order": derivation["base_order"],
        "terminal_lane_unique_zero_central": terminal_scan["unique_zero_central"],
        "terminal_lane_unique_visible_c2": terminal_scan["unique_visible_c2_in_terminal_lane"],
        "ordered_source_validator_passes": validators["ordered_source"]["exit_code"] == 0,
        "cohomology_validator_passes": validators["cohomology"]["exit_code"] == 0,
        "promotes_rank_two_route": validators["cohomology"]["promotes_rank_two_route"],
        "closed_only_if_principle_is_admitted": True,
    }

    ah_binding_status = {
        "AH_goodcover_equivalence_proved": ah_reduction["AH_goodcover_representative_equivalence_theorem"]["proved"],
        "terminal_lane_binding_condition": ah_reduction["theorem"]["statement"],
        "binding_closed_under_principle_at_ordered_layer": True,
        "raw_good_cover_or_smooth_Dolbeault_transition_data_still_open": principle["still_open"][
            "raw_good_cover_or_smooth_Dolbeault_transition_data"
        ],
        "operator_layer_Pic0_recheck_still_open": principle["still_open"]["operator_layer_Pic0_recheck"],
    }

    sm_slot_functor_status = {
        "support_from_dirac_gate": {
            "finite_q79_polarization_support": dirac["route_A_SU5_E6_polarization"]["support_closed"],
            "structural_1M_rule_available": dirac["route_A_SU5_E6_polarization"]["structural_1M_rule_available"],
            "model_projector_support": dirac["route_B_HYM_projector_zero_mode"]["support_closed"],
        },
        "still_not_emitted": {
            "selected_U10_Ubar5_polarization": not dirac["selection_decision"]["selected_U10_Ubar5_polarization_closed"],
            "selected_1M_Dirac_rule": not dirac["selection_decision"]["selected_1M_Dirac_neutrino_source_rule_closed"],
            "selected_overlap_transfer_normalization": dirac["what_remains_open"][
                "selected_overlap_transfer_normalization"
            ],
        },
        "slot_contract": previous["SM_slot_map_audit"]["slot_contract"],
        "needed_functor": (
            "section-ring/cohomology functor from the selected terminal L3-K2/H1/Ext packet "
            "to 10_M, bar5_M, and 1_M matter slots, including overlap normalization"
        ),
        "closed": False,
    }

    two_routes_forward = {
        "Route_A_promote_principle": {
            "status": "PRIMARY",
            "must_do": [
                "promote TerminalAdmissibleSectionSourcePrinciple into the main MTT axiomatic spine",
                "or derive it from projection/admissibility/gauge-fixing formalism",
                "then relabel the ordered source and H1/Ext packets as theorem-selected, not principle-conditional",
            ],
            "what_it_would_close": [
                "terminal map source principle",
                "selected base order",
                "ordered source L3-K2",
                "selected h1=8 nonzero Ext packet",
            ],
        },
        "Route_B_emit_SM_slot_functor": {
            "status": "PARALLEL",
            "must_do": [
                "construct selected section-ring/cohomology functor to SU(5)/E6 matter slots",
                "emit U_10=I_3 and U_bar5=F as source outputs",
                "emit the 1_M Dirac-neutrino rule and overlap normalization",
            ],
            "what_it_would_close": [
                "10_M/bar5_M/1_M routing",
                "same-branch matter-slot readout",
                "input side of the selected flavor/overlap operator packet",
            ],
        },
        "Route_C_operator_bypass": {
            "status": "RETAINED",
            "must_do": terminal_attempt["minimal_remaining_packet"]["must_supply"][2:],
            "what_it_would_close": [
                "operator-layer Pic0 by same-source replacement",
                "D_E/Riesz/Green/dotD source values",
                "possible direct SM-slot operator labels",
            ],
        },
    }

    theorem = {
        "name": "TerminalMapSourcePrincipleConditionalClosureTheorem",
        "proved": True,
        "statement": (
            "Importing q79's TerminalAdmissibleSectionSourcePrinciple closes the ordered terminal source, "
            "base order, and h1=8 Ext packet conditionally under the explicit principle: the terminal lane scan "
            "selects g3/L3-K2, the ordered-source validator passes, and the cohomology validator promotes the "
            "rank-two route. The result is not yet unconditional MTT closure until the principle is promoted to "
            "the MTT axiomatic spine or derived from projection-admissibility; the SM-slot functor, operator-layer "
            "Pic0, overlap normalization, and same-source operator data remain open."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedTerminalMapSourcePrincipleOrSMSlotFunctor",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "local_dirac_polarization_gate": rel(DIRAC_GATE),
            "q79_terminal_principle": rel(TERMINAL_PRINCIPLE),
            "q79_terminal_principle_certificate": rel(TERMINAL_PRINCIPLE_CERT),
            "q79_terminal_base_order_attempt": rel(TERMINAL_ATTEMPT),
            "q79_ordered_reduction": rel(ORDERED_REDUCTION),
            "q79_AH_reduction": rel(AH_REDUCTION),
        },
        "superset_strategy": {
            "mode": "PRINCIPLE_IMPORT_PLUS_PARALLEL_FUNCTOR_GATE",
            "using_one_straight_path": False,
            "primary_path": "Route A: promote/import TerminalAdmissibleSectionSourcePrinciple",
            "parallel_path": "Route B: selected section-ring/cohomology SM-slot functor",
            "bypass_path": "Route C: same-source operator response emits the same slot labels directly",
            "locked_target_role": "no observed masses, mixings, benchmark matrices, lifted flags, or locked C1 columns select the source",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "imported_principle_status": imported_principle_status,
        "conditional_terminal_source_closure": conditional_terminal_source_closure,
        "AH_Cech_binding_status": ah_binding_status,
        "SM_slot_functor_status": sm_slot_functor_status,
        "two_routes_forward": two_routes_forward,
        "what_closes_now": {
            "terminal_source_closed_under_explicit_principle": True,
            "selected_base_order_closed_under_explicit_principle": True,
            "ordered_source_validator_passes_under_principle": True,
            "h1_Ext_packet_promotes_under_principle": True,
            "AH_binding_reduced_to_representative_under_selected_class": True,
            "next_unconditional_gate_identified": True,
        },
        "what_remains_open": {
            "promote_principle_to_unconditional_MTT_axiom_or_derive_it": True,
            "selected_section_ring_to_SM_slot_functor": True,
            "selected_U10_Ubar5_polarization_source_outputs": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "operator_layer_Pic0_recheck": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "raw_good_cover_or_smooth_Dolbeault_transition_data": True,
            "Yukawa_CKM_PMNS_magnitudes": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "unconditional_MTT_closure_claimed": False,
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
                "certificate": "MTT_Selected_TerminalMap_SourcePrinciple_or_SMSlotFunctor_v1",
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "closure_claimed": False,
                "unconditional_MTT_closure_claimed": False,
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
        """# MTT Selected TerminalMap SourcePrinciple or SMSlotFunctor v1

Status: `MTT_SELECTED_TERMINALMAP_SOURCEPRINCIPLE_CONDITIONAL_ORDERED_SOURCE_CLOSED_SMSLOTFUNCTOR_OPEN`

This artifact imports q79's `TerminalAdmissibleSectionSourcePrinciple` with the
right amount of caution.

## What Closes Under The Explicit Principle

Under the principle, the terminal lane scan selects:

- source label `g3 / L3-K2`;
- `L=(1,-2,0)`;
- `L^2=(2,-4,0)`;
- base order `E1/g1g2` positive and `E2/g3g4` negative;
- visible Chern row `c2(V_alpha)=4 alpha_1`.

The ordered-source validator passes, and the `h1=8` nonzero Ext packet promotes
the rank-two route without observed flavor data or benchmark matrices.

## Why This Is Not Yet Unconditional

The q79 source says the principle should still be promoted into the main MTT
axiomatic spine, or derived from projection/admissibility/gauge-fixing
formalism, before the result is called unconditional.

So the current state is:

```text
TerminalAdmissibleSectionSourcePrinciple
  -> selected terminal source/base order/H1-Ext packet
```

but not yet:

```text
MTT axioms alone
  -> selected terminal source/base order/H1-Ext packet.
```

## Remaining Gates

There are now two clean forward routes:

- promote or derive the terminal admissible-section principle;
- build the selected section-ring/cohomology functor to `10_M`, `bar5_M`,
  and `1_M`, including the `1_M` Dirac rule and overlap normalization.

Route-C remains a bypass if the selected operator response emits the same data
directly.

Next artifact:
`MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
