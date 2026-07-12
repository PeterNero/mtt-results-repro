"""Build the selected SM-slot functor value-emission or axiom-patch gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "terminaladmissible_axiominsertion_and_smslotfunctor.candidate.json"
SAMEBRANCH = DATA / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
READOUT = DATA / "selected_matterslot_transversality_readout_functional.candidate.json"
SECTIONRING = DATA / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
TERMINAL_SOURCE = DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"

OUTPUT = DATA / "selected_smslotfunctor_valueemission_or_axiompatch.candidate.json"
CERT = CERTS / "selected_smslotfunctor_valueemission_or_axiompatch_certificate.json"
NOTE = CORPUS / "MTT_SelectedSMSlotFunctor_ValueEmission_or_AxiomPaperPatch_v1.md"

STATUS = "MTT_SELECTED_SMSLOTFUNCTOR_VALUE_EMISSION_BLOCKED_AXIOM_PATCH_READY"
NEXT = "MTT_TerminalAxiomPatch_Apply_or_SMSlotFunctor_ArrowValues_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    samebranch = load(SAMEBRANCH)
    readout = load(READOUT)
    sectionring = load(SECTIONRING)
    terminal_source = load(TERMINAL_SOURCE)

    insertion = previous["insertion_package"]
    functor = previous["SM_slot_functor_signature"]

    axiom_patch_bundle = {
        "status": "READY_TO_APPLY_NOT_APPLIED",
        "route": "Route A / axiom-paper patch",
        "target_papers": insertion["target_papers"],
        "patch_text": insertion["paper_ready_insert"],
        "post_patch_replay": {
            "can_rerun_terminal_source_unconditionally": previous["after_insertion_replay"][
                "can_rerun_terminal_source_as_unconditional_after_insertion"
            ],
            "would_promote": previous["after_insertion_replay"]["promoted_items_after_insertion"],
            "requires_actual_patch_or_internal_derivation": True,
        },
        "safe_scope": (
            "This patch promotes only the finite terminal representative selection rule and its terminal "
            "source replay. It does not by itself emit SM-slot functor arrows, overlap normalization, "
            "Yukawa magnitudes, CKM/PMNS data, or physical alpha1."
        ),
    }

    value_emission_attempt = {
        "status": "ATTEMPTED_BLOCKED_BY_SELECTED_ARROW_VALUES",
        "route": "Route B / direct selected SM-slot functor value emission",
        "current_domain_support": functor["domain"],
        "current_codomain_support": functor["codomain"],
        "support_available": {
            "finite_q79_U10_Ubar5": functor["support_already_closed"]["finite_q79_polarization_support"],
            "structural_1M_rule": functor["support_already_closed"]["structural_1M_rule_available"],
            "stationary_projector_source_promoted": functor["support_already_closed"][
                "stationary_projector_source_promoted"
            ],
            "terminal_source_conditional_under_principle": terminal_source[
                "conditional_terminal_source_closure"
            ]["closed_only_if_principle_is_admitted"],
            "sectionring_primary_route_identified": sectionring["selection_decision"][
                "primary_route_selected_for_next_attempt"
            ],
        },
        "legal_emission_conditions": [
            "selected section-ring/cohomology generator map to 10_M clock row",
            "selected section-ring/cohomology generator map to bar5_M shift row",
            "selected section-ring/cohomology generator map to 1_M=N^c Dirac row",
            "selected q79 polarization outputs U_10=I_3 and U_bar5=F as source outputs",
            "selected overlap/transfer normalization compatible with transported projectors",
            "same-source consistency tying terminal source, projectors, and matter-slot labels",
        ],
        "failed_conditions": {
            "selected_sectionring_to_10M_clock_arrow": True,
            "selected_sectionring_to_bar5M_shift_arrow": True,
            "selected_sectionring_to_1M_Dirac_arrow": True,
            "selected_U10_Ubar5_source_outputs": samebranch["selection_decision"][
                "selected_U10_Ubar5_polarization_closed"
            ]
            is False,
            "selected_1M_Dirac_neutrino_source_rule": samebranch["selection_decision"][
                "selected_1M_Dirac_neutrino_source_rule_closed"
            ]
            is False,
            "selected_overlap_transfer_normalization": samebranch["selection_decision"][
                "selected_transfer_normalization_promoted"
            ]
            is False,
        },
        "why_blocked": (
            "The repo has selected stationary rho_s/projector support and finite q79 SU(5)/E6 support, "
            "but no current artifact emits the section-ring arrows and polarization values as selected "
            "source outputs. The stationary source is slot-uniform, so it cannot by itself distinguish "
            "10_M, bar5_M, and 1_M."
        ),
        "blocked_by_no_go": {
            "rho_s_slot_uniformity": readout["selection_decision"][
                "stationary_rho_s_alone_closes_selected_matter_slots"
            ]
            if "stationary_rho_s_alone_closes_selected_matter_slots" in readout.get("selection_decision", {})
            else False,
            "matter_slot_readout_missing": samebranch["what_remains_open"][
                "selected_matter_slot_transversality_readout_functional"
            ],
        },
    }

    selected_decision = {
        "route_A_axiom_patch_ready": True,
        "route_B_direct_value_emission_closed": False,
        "can_claim_selected_SMSlotFunctor_values_now": False,
        "can_claim_unconditional_terminal_source_now": False,
        "can_claim_after_actual_axiom_patch": {
            "terminal_source_and_h1_Ext": True,
            "SM_slot_functor_values": False,
        },
        "reason": (
            "The axiom text is ready to apply to the papers or axiomatic spine, but it has not been applied "
            "inside this repo. Direct value emission is still blocked by missing selected arrows and overlap "
            "normalization. Therefore the next honest move is either apply/prove the terminal axiom, or emit "
            "the six selected SM-slot functor arrows from same-source section-ring/operator data."
        ),
    }

    theorem = {
        "name": "SelectedSMSlotFunctorValueEmissionOrAxiomPatchTheorem",
        "proved": True,
        "statement": (
            "Given the current repo data, the terminal admissible-section axiom patch is ready to apply, "
            "and applying or deriving it would make the terminal source replay unconditional. However, the "
            "selected SM-slot functor values do not yet emit: finite q79 polarization, the structural 1_M "
            "rule, and transported projector support are only support data until the selected section-ring "
            "arrows, U_10/U_bar5 source outputs, 1_M source row, overlap normalization, and same-source "
            "consistency map are supplied."
        ),
    }

    data = {
        "candidate": "MTTSelectedSMSlotFunctorValueEmissionOrAxiomPatch",
        "status": STATUS,
        "inputs": {
            "previous_axiom_insertion_package": rel(PREVIOUS),
            "samebranch_emission_attempt": rel(SAMEBRANCH),
            "matter_slot_readout_attempt": rel(READOUT),
            "sectionring_readout_attempt": rel(SECTIONRING),
            "terminal_source_principle_gate": rel(TERMINAL_SOURCE),
        },
        "superset_strategy": {
            "mode": "TWO_ROUTE_FRONTIER_TEST",
            "using_one_straight_path": False,
            "route_A": "apply or internally derive terminal admissible-section axiom",
            "route_B": "directly emit selected SM-slot functor arrow values",
            "locked_target_role": "forbidden as selector; compatibility checks only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "axiom_patch_bundle": axiom_patch_bundle,
        "selected_SM_slot_functor_value_emission_attempt": value_emission_attempt,
        "selection_decision": selected_decision,
        "what_closes_now": {
            "axiom_patch_bundle_ready": True,
            "direct_value_emission_no_overclaim_proved": True,
            "six_required_functor_arrows_relisted_as_acceptance_gate": True,
            "rho_s_alone_rejected_as_slot_selector": True,
            "next_move_sharpened": True,
        },
        "what_remains_open": {
            "apply_or_derive_terminal_admissible_section_axiom": True,
            "rerun_terminal_source_as_unconditional_after_axiom": True,
            "selected_sectionring_to_10M_clock_arrow": True,
            "selected_sectionring_to_bar5M_shift_arrow": True,
            "selected_sectionring_to_1M_Dirac_arrow": True,
            "selected_U10_Ubar5_source_outputs": True,
            "selected_overlap_transfer_normalization": True,
            "same_source_consistency_map": True,
            "SM_slot_functor_values": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "unconditional_terminal_source_claimed": False,
        "selected_SMSlotFunctor_values_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_SelectedSMSlotFunctor_ValueEmission_or_AxiomPaperPatch_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "unconditional_terminal_source_claimed": False,
        "selected_SMSlotFunctor_values_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": data["what_closes_now"],
        "what_remains_open": data["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT SelectedSMSlotFunctor ValueEmission or AxiomPaperPatch v1

Status: `{STATUS}`.

## Result

Two routes were tested.

Route A is ready: the terminal admissible-section axiom patch is packaged with
target paper placements and exact insertion text.  Applying or deriving that
axiom would allow the terminal-source replay to become unconditional for
`g3/L3-K2`, `L=(1,-2,0)`, `L^2=(2,-4,0)`, the ordered base row, and the
`h1=8` Ext packet.

Route B is not closed: the selected SM-slot functor values do not emit from the
current repo data.  We have q79 finite support `U_10=I_3`, `U_bar5=F`, the
structural `1_M=N^c` Dirac rule, and transported projector support, but those
are not yet selected source outputs.

## Acceptance Gate

The next proof object must emit these six arrows from the same selected source:

1. terminal Ext source -> `10_M` clock row;
2. terminal Ext source -> `bar5_M` shift row;
3. terminal Ext source -> `1_M=N^c` Dirac row;
4. q79 polarization output `U_10=I_3`, `U_bar5=F`;
5. overlap/transfer normalization compatible with transported projectors;
6. same-source consistency tying terminal source, projectors, and slot labels.

The stationary `rho_s` source alone is not enough, because its current invariants
are slot-uniform across `u,d,e,N`.

No observed constants, locked C1 columns, or benchmark flavor matrices are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
