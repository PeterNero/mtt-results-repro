"""Attempt the selected matter-slot transversality readout functional.

The previous artifact reduced the U10/Ubar5/1_M gate to a very specific object:
a same-branch readout functional that extracts the SU(5)/E6 matter-slot split
from the already selected stationary rho_s/projector/zero-mode source.

This builder tests the honest readouts currently available:

* End0/rho_s representation invariants,
* sector projector/rank/Gram/Casimir data,
* qutrit Weyl/source support,
* SU(5)/E6 structural support,
* locked C1 partition (as forbidden diagnostic target only).

It records the expected result: rho_s alone is too symmetric to distinguish
10_M clock from bar5_M/1_M shift.  The next missing object is a selected
matter-slot grading/section-label readout layered on the same source.
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

PREVIOUS = DATA / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
SOURCE_PAYLOAD = DATA / "selected_sector_zero_mode_source_payload_search_or_emission_attempt.candidate.json"
VALUE_FILL = DATA / "selected_sector_zero_mode_end0_action_matrix_or_matter_slot_routing_value_fill.candidate.json"
SECTOR_CERT = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
ONE_M = DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"
MATTER_THEOREM = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
WEYL_SOURCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
E6_DICT = Q79 / "certificates" / "e6_to_sm_yukawa_operator_dictionary_certificate.json"
SU5_TRANS = Q79 / "certificates" / "su5_matter_slot_transversality_certificate.json"

OUTPUT = DATA / "selected_matterslot_transversality_readout_functional.candidate.json"
CERT = CERTS / "selected_matterslot_transversality_readout_functional_certificate.json"
NOTE = CORPUS / "MTT_Selected_MatterSlot_Transversality_Readout_Functional_v1.md"

STATUS = "MTT_SELECTED_MATTERSLOT_TRANSVERSALITY_READOUT_FUNCTIONAL_ATTEMPT_RHOS_INVARIANT_NOGO_GRADING_OPEN"
NEXT = "MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1"

MATTER_SECTORS = ["u", "d", "e", "N"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_signature(rho: dict[str, list[list[float]]]) -> dict[str, Any]:
    return {
        "T1": rho["T1"],
        "T2": rho["T2"],
        "T3": rho["T3"],
    }


def main() -> None:
    previous = load(PREVIOUS)
    source_payload = load(SOURCE_PAYLOAD)
    value_fill = load(VALUE_FILL)
    sector_cert = load(SECTOR_CERT)
    one_m = load(ONE_M)
    matter = load(MATTER_THEOREM)
    weyl = load(WEYL_SOURCE)
    transfer = load(TRANSFER)
    e6 = load(E6_DICT)
    trans = load(SU5_TRANS)

    rho_candidate = source_payload["source_map_candidate"]["rho_candidate"]
    signatures = {sector: matrix_signature(rho_candidate[sector]["rho"]) for sector in MATTER_SECTORS}
    first_sig = signatures[MATTER_SECTORS[0]]
    all_matter_rho_identical = all(signatures[sector] == first_sig for sector in MATTER_SECTORS)

    gram = value_fill["conditional_gram_normalization_theorem"]
    value_gates = value_fill["selected_source_gates"]
    sector_uniform = sector_cert["current_mtt_data_tests"]["projector_dotd_uniformity"][
        "all_right_family_payloads_identical"
    ]

    candidate_readouts = [
        {
            "name": "rho_s_adjoint_invariant_readout",
            "allowed_as_selected_source": True,
            "available_now": previous["stationary_selected_source"]["selected_rho_s_validator_ready"],
            "distinguishes_required_partition": False,
            "reason": "All right-family matter sectors carry the same adjoint rho_s matrices and the same invariant Gram/Casimir data.",
        },
        {
            "name": "projector_rank_gap_gram_readout",
            "allowed_as_selected_source": True,
            "available_now": previous["stationary_selected_source"]["selected_projector_source_verified"],
            "distinguishes_required_partition": False,
            "reason": "Ranks, gaps, and invariant Gram normalization are common across matter sectors; H is distinguished only as singlet.",
        },
        {
            "name": "qutrit_weyl_source_carrier_readout",
            "allowed_as_selected_source": True,
            "available_now": weyl["source_level_weyl_carrier"]["proved"],
            "distinguishes_required_partition": False,
            "reason": "The source-level carrier gives Z/X and active shift provenance, but source-to-sector routing remains conditional.",
        },
        {
            "name": "su5_e6_structural_dictionary_readout",
            "allowed_as_selected_source": False,
            "available_now": True,
            "distinguishes_required_partition": True,
            "reason": "It gives the desired 10_M/bar5_M/1_M structure, but current selected source does not emit it.",
        },
        {
            "name": "locked_c1_partition_readout",
            "allowed_as_selected_source": False,
            "available_now": True,
            "distinguishes_required_partition": True,
            "reason": "The locked columns uniquely prefer u,e | d,nuD, but using them as source selectors is target-localized and forbidden.",
        },
    ]

    legal_readout_closes = any(
        row["allowed_as_selected_source"] and row["available_now"] and row["distinguishes_required_partition"]
        for row in candidate_readouts
    )

    selected_functional = {
        "domain_source_closed": previous["selection_decision"]["selected_stationary_source_available"],
        "rho_s_matter_invariants_identical": all_matter_rho_identical,
        "projector_dotd_payload_uniform": sector_uniform,
        "conditional_gram_theorem_proved": gram["proved"],
        "structural_e6_su5_partition_available": one_m["what_closes_now"]["structural_E6_dictionary_support"],
        "finite_su5_transversality_support": trans["calculation_results"]["finite_transversality_theorem_closed"],
        "selected_readout_functional_emitted": legal_readout_closes,
        "why": (
            "The selected stationary source supplies a valid universal matter adjoint carrier, but every legal "
            "readout currently available is invariant under permutation of u,d,e,N.  The readout that would "
            "select 10_M/bar5_M/1_M must add a selected matter-slot grading or section-label functional."
        ),
    }

    required_grading = {
        "name": "SelectedMatterSlotGradingOrSectionRingReadout",
        "must_emit": {
            "matter_slot_grading": {
                "10_M": ["u", "e"],
                "bar5_M": ["d"],
                "1_M_Dirac": ["nuD"],
            },
            "operator_channel_compatibility": {
                "up": "10_M 10_M 5_H",
                "down": "10_M bar5_M bar5_H",
                "charged_lepton": "10_M bar5_M bar5_H",
                "dirac_neutrino": "bar5_M 1_M 5_H",
            },
            "q79_polarization_output": {"U_10": "I_3", "U_bar5": "F"},
            "same_branch_normalization_link": "feeds sector Gram/transfer normalization and source-to-C1 transfer",
        },
        "allowed_source_types": [
            "typed monad/Cech cohomology label readout",
            "line-bundle section-ring degree readout",
            "selected SU(5)/E6 matter-slot source identity",
            "selected zero-mode operator channel grading from the same HYM/Strominger branch",
        ],
        "forbidden_promotions": [
            "observed masses or mixings",
            "benchmark flavor matrices",
            "locked C1 splitter columns",
            "conditional q79 SU(5) fixture treated as selected source",
            "universal rho_s adjoint symmetry broken by hand",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedMatterSlotTransversalityReadoutFunctional",
        "status": STATUS,
        "inputs": {
            "previous_samebranch_emission_attempt": rel(PREVIOUS),
            "sector_zero_mode_source_payload": rel(SOURCE_PAYLOAD),
            "sector_zero_mode_value_fill": rel(VALUE_FILL),
            "sector_charge_or_chirality_certificate": rel(SECTOR_CERT),
            "one_M_dirac_rule_attempt": rel(ONE_M),
            "matter_slot_charge_overlap_theorem": rel(MATTER_THEOREM),
            "weylpair_source_provenance": rel(WEYL_SOURCE),
            "weylpair_source_to_c1_transfer": rel(TRANSFER),
            "q79_e6_dictionary": rel(E6_DICT),
            "q79_su5_transversality": rel(SU5_TRANS),
        },
        "superset_strategy": {
            "mode": "READOUT_SEARCH_WITH_FORBIDDEN_TARGET_SELECTOR",
            "straight_path": "selected stationary rho_s/projector/zero-mode source invariants",
            "support_path": "SU(5)/E6 dictionary, q79 finite transversality, Weyl source carrier",
            "locked_target_role": "diagnostic only; cannot select the readout",
            "observed_data_used": False,
            "target_fitting_used": False,
            "diagnostic_lift_used_as_proof": False,
        },
        "rho_s_invariant_test": {
            "matter_sectors_checked": MATTER_SECTORS,
            "all_matter_rho_matrices_identical": all_matter_rho_identical,
            "all_matter_maps_use_same_adjoint_matrices": value_fill["direct_End0_action_value_fill"][
                "model_source_map_validation"
            ]["all_matter_maps_use_same_adjoint_matrices"],
            "conditional_gram_forces_common_I3": gram["proved"],
            "selected_matter_slot_routing_present": value_gates["selected_matter_slot_routing"],
            "selected_1M_Dirac_neutrino_rule_present": value_gates["selected_1M_Dirac_neutrino_rule"],
        },
        "candidate_readouts_tested": candidate_readouts,
        "selected_functional_decision": selected_functional,
        "required_next_readout": required_grading,
        "selection_decision": {
            "selected_matter_slot_transversality_readout_functional_closed": legal_readout_closes,
            "selected_U10_Ubar5_polarization_closed": False,
            "selected_1M_Dirac_neutrino_source_rule_closed": False,
            "selected_sector_charge_or_chirality_closed": False,
            "selected_transfer_normalization_promoted": False,
            "closure_claimed": False,
            "reason": selected_functional["why"],
        },
        "what_closes_now": {
            "rho_s_alone_readout_nogo": all_matter_rho_identical and sector_uniform,
            "legal_current_readouts_exhausted": True,
            "structural_su5_e6_support_retained": True,
            "locked_c1_target_rejected_as_source_selector": True,
            "next_object_sharpened_to_grading_or_section_ring_readout": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_matter_slot_grading_or_section_ring_readout": True,
            "selected_10M_clock_readout": True,
            "selected_bar5M_shift_readout": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_source_to_C1_transfer_promotion": True,
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
                "rho_s_alone_readout_nogo": candidate["what_closes_now"]["rho_s_alone_readout_nogo"],
                "selected_readout_functional_closed": legal_readout_closes,
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
        """# MTT Selected MatterSlot Transversality Readout Functional

Status: `MTT_SELECTED_MATTERSLOT_TRANSVERSALITY_READOUT_FUNCTIONAL_ATTEMPT_RHOS_INVARIANT_NOGO_GRADING_OPEN`

This artifact tries to build the selected readout that would turn the selected
stationary `rho_s` source into the SU(5)/E6 matter-slot split.

## Result

The selected stationary `rho_s` source is not enough by itself.

The honest `rho_s`/projector/Gram invariants are identical across the right
matter sectors `u,d,e,N`.  They distinguish the Higgs singlet from matter, but
they do not distinguish:

- `10_M` clock side,
- `bar5_M` shift side,
- `1_M=N^c` Dirac-neutrino shift side.

This is a useful no-go, not a failure of the program: it says the matter-slot
readout is an additional selected grading/label object, not a hidden consequence
of the universal adjoint action.

## What Still Works

The SU(5)/E6 dictionary and q79 finite transversality still give the intended
support:

- `10_M -> u,e`,
- `bar5_M -> d`,
- `1_M=N^c` through `bar5_M 1_M 5_H -> L N^c H_u`, giving `nuD`,
- `U_10=I_3`, `U_bar5=F` under the transversality/readout hypothesis.

But the locked C1 columns and conditional SU(5) fixture are not allowed to act
as selected source selectors.

## New Frontier

The next object is:

`SelectedMatterSlotGradingOrSectionRingReadout`.

It should come from one of:

- typed monad/Cech cohomology labels,
- line-bundle section-ring degree data,
- selected SU(5)/E6 matter-slot source identity,
- selected zero-mode operator-channel grading from the same HYM/Strominger branch.

Next artifact: `MTT_Selected_MatterSlot_Grading_or_SectionRing_Readout_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
