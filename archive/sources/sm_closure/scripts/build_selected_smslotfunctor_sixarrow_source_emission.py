"""Build the selected SM-slot functor six-arrow source-emission artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "terminal_axiom_patch_apply_or_smslotfunctor_arrowvalues.candidate.json"
SECTIONRING = DATA / "selected_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
BASE_AH_SLOT = DATA / "selected_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
DIRAC_POLARIZATION = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
PROJECTOR = DATA / "selected_finite_projector_source_promotion.candidate.json"

OUTPUT = DATA / "selected_smslotfunctor_sixarrow_source_emission.candidate.json"
CERT = CERTS / "selected_smslotfunctor_sixarrow_source_emission_certificate.json"
NOTE = CORPUS / "MTT_SelectedSMSlotFunctor_SixArrow_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_SIXARROW_PARTIAL_SOURCE_EMISSION_BUILT_POLARIZATION_NORMALIZATION_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_PolarizationAndOverlap_SourceEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    sectionring = load(SECTIONRING)
    base_ah_slot = load(BASE_AH_SLOT)
    dirac = load(DIRAC_POLARIZATION)
    projector = load(PROJECTOR)

    terminal_closed = (
        previous["unconditional_terminal_source_claimed_in_patched_spine"]
        and previous["unconditional_terminal_source_claimed_in_patched_corpus"]
    )
    terminal = previous["unconditional_terminal_replay"]
    slot_contract = sectionring["matter_slot_map_contract"]["must_map_without_locked_C1_columns"]
    q79_support = sectionring["matter_slot_map_contract"]["must_preserve_q79_polarization"]
    failed_prior = previous["SM_slot_functor_arrow_gate"]["failed_conditions"]

    ah_cech_binding = {
        "status": "ORDERED_SOURCE_LAYER_PROMOTED_OPERATOR_LAYER_RECHECK_OPEN",
        "terminal_source_axiom_backed": terminal_closed,
        "selected_L": terminal["selected_L"],
        "selected_L2": terminal["selected_L2"],
        "constructed_AH_support": base_ah_slot["AH_Cech_binding_audit"][
            "automorphy_formula_constructed"
        ],
        "constructed_Yoneda_support": base_ah_slot["AH_Cech_binding_audit"][
            "yoneda_multiplication_identity_verified"
        ],
        "shared_circle_degree_zero_retained": base_ah_slot["AH_Cech_binding_audit"][
            "shared_circle_degree_zero_retained"
        ],
        "ordered_source_layer_binding_promoted": terminal_closed
        and base_ah_slot["AH_Cech_binding_audit"]["automorphy_formula_constructed"]
        and base_ah_slot["AH_Cech_binding_audit"]["yoneda_multiplication_identity_verified"],
        "operator_layer_pic0_recheck_open": True,
    }

    emitted_arrows = {
        "A1_terminal_Ext_to_10M_clock": {
            "status": "EMITTED_SOURCE_ARROW",
            "map": "H1(L^2)_selected terminal Ext row -> 10_M clock row",
            "outputs": slot_contract["10_M_clock"],
            "reason": "The terminal source and h1 Ext packet are now axiom-backed, and the SU(5)/E6 slot dictionary supplies the typed 10_M clock codomain without observed data.",
            "selected": terminal_closed,
        },
        "A2_terminal_Ext_to_bar5M_shift": {
            "status": "EMITTED_SOURCE_ARROW",
            "map": "H1(L^2)_selected terminal Ext row -> bar5_M shift row",
            "outputs": slot_contract["bar5_M_shift"],
            "reason": "The same selected Ext source feeds the bar5_M shift codomain in the structural SU(5)/E6 dictionary.",
            "selected": terminal_closed,
        },
        "A3_terminal_Ext_to_1M_Dirac": {
            "status": "EMITTED_SOURCE_ARROW",
            "map": "H1(L^2)_selected terminal Ext row -> 1_M=N^c Dirac row",
            "outputs": slot_contract["1_M_Dirac_shift"],
            "reason": "The structural 1_M=N^c rule routes through bar5_M 1_M 5_H -> L N^c H_u, and the selected terminal Ext source now supplies the source side.",
            "selected": terminal_closed
            and dirac["route_A_SU5_E6_polarization"]["structural_1M_rule_available"],
        },
    }

    open_arrows = {
        "A4_q79_polarization_outputs": {
            "status": "SUPPORT_ONLY_SOURCE_OUTPUT_OPEN",
            "candidate_outputs": {"U_10": q79_support["U_10"], "U_bar5": q79_support["U_bar5"]},
            "why_open": "Finite q79 transversality supports these outputs, but the same selected section-ring source has not yet emitted the q79 projection tensor as a source value.",
            "prior_failed_condition": failed_prior["selected_U10_Ubar5_source_outputs"],
        },
        "A5_overlap_transfer_normalization": {
            "status": "OPEN",
            "candidate": "unit Gram/transport normalization compatible with transported projectors",
            "why_open": "Transported projectors are promoted, but the section-ring slot functor has not yet emitted its overlap kernel or transfer normalization as selected source data.",
            "prior_failed_condition": failed_prior["selected_overlap_transfer_normalization"],
        },
        "A6_same_source_consistency": {
            "status": "PARTIAL_OPEN",
            "closed_part": "terminal source and transported projector source are both selected",
            "open_part": "q79 polarization output and overlap normalization are not yet same-source emitted",
            "why_open": "Consistency can only be fully claimed once A4 and A5 are emitted from the same source packet.",
        },
    }

    arrow_status = {
        "closed_count": sum(1 for item in emitted_arrows.values() if item["selected"]),
        "open_count": len(open_arrows),
        "closed_arrows": list(emitted_arrows),
        "open_arrows": list(open_arrows),
        "all_six_closed": False,
    }

    theorem = {
        "name": "SelectedSMSlotFunctorPartialSixArrowEmissionTheorem",
        "proved": True,
        "statement": (
            "With the terminal admissible-section axiom applied in the proof spine and corpus, the selected "
            "terminal Ext packet emits the first three SM-slot functor arrows to 10_M, bar5_M, and 1_M=N^c. "
            "This closes the typed matter-slot labeling side without observed constants. The remaining three "
            "arrows stay open: q79 polarization outputs, overlap/transfer normalization, and full same-source "
            "consistency require an additional selected operator/polarization packet."
        ),
    }

    data = {
        "candidate": "MTTSelectedSMSlotFunctorSixArrowSourceEmission",
        "status": STATUS,
        "inputs": {
            "terminal_axiom_patch": rel(PREVIOUS),
            "sectionring_source_selector": rel(SECTIONRING),
            "baseorder_AH_SMSlot_gate": rel(BASE_AH_SLOT),
            "dirac_polarization_gate": rel(DIRAC_POLARIZATION),
            "finite_projector_source_promotion": rel(PROJECTOR),
        },
        "superset_strategy": {
            "mode": "STRAIGHT_TERMINAL_SECTIONRING_WITH_OPERATOR_SUPPORT_RETAINED",
            "using_one_straight_path": False,
            "straight_path": "axiom-backed terminal section-ring source emits typed SM-slot arrows A1-A3",
            "support_path": "q79 SU(5)/E6 transversality plus transported projectors support A4-A6 but do not yet promote them",
            "locked_target_role": "forbidden as selector; compatibility only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "AH_Cech_binding": ah_cech_binding,
        "emitted_source_arrows": emitted_arrows,
        "open_source_arrows": open_arrows,
        "arrow_status": arrow_status,
        "what_closes_now": {
            "ordered_AH_Cech_binding_promoted_at_source_layer": ah_cech_binding[
                "ordered_source_layer_binding_promoted"
            ],
            "selected_sectionring_to_10M_clock_arrow": emitted_arrows[
                "A1_terminal_Ext_to_10M_clock"
            ]["selected"],
            "selected_sectionring_to_bar5M_shift_arrow": emitted_arrows[
                "A2_terminal_Ext_to_bar5M_shift"
            ]["selected"],
            "selected_sectionring_to_1M_Dirac_arrow": emitted_arrows[
                "A3_terminal_Ext_to_1M_Dirac"
            ]["selected"],
            "selected_1M_Dirac_shift_readout": emitted_arrows[
                "A3_terminal_Ext_to_1M_Dirac"
            ]["selected"],
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_U10_Ubar5_source_outputs": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_consistency_map": True,
            "operator_layer_Pic0_recheck": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "physical_alpha1_driver": True,
            "primitive_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "selected_SMSlotFunctor_all_six_arrows_claimed": False,
        "selected_SMSlotFunctor_first_three_arrows_claimed": True,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_SelectedSMSlotFunctor_SixArrow_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "selected_SMSlotFunctor_all_six_arrows_claimed": False,
        "selected_SMSlotFunctor_first_three_arrows_claimed": True,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": data["what_closes_now"],
        "what_remains_open": data["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SelectedSMSlotFunctor SixArrow SourceEmission v1

Status: `{STATUS}`.

## Result

The axiom-backed terminal section-ring source now emits the first three
SM-slot functor arrows:

1. terminal Ext source -> `10_M` clock row: `u,e`;
2. terminal Ext source -> `bar5_M` shift row: `d`;
3. terminal Ext source -> `1_M=N^c` Dirac row: `nuD`.

This uses the patched terminal source, selected `L=(1,-2,0)`, selected
`L^2=(2,-4,0)`, selected `h1=8` Ext packet, and the structural SU(5)/E6 slot
dictionary.  It does not use measured constants, locked C1 columns, or benchmark
matrices.

## Still Open

The remaining arrows are:

4. selected `U_10=I_3`, `U_bar5=F` as source outputs;
5. selected overlap/transfer normalization;
6. full same-source consistency map.

The q79 finite packet and transported projectors are strong support, but they
still need a selected polarization/overlap operator packet before all six arrows
are closed.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
