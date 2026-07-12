"""Build the terminal admissible-section axiom insertion and SM-slot functor package."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "terminaladmissible_principle_promotion_or_smslotfunctor.candidate.json"
TERMINAL_CONDITIONAL = DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"
DIRAC_GATE = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
PROJECTOR_PROMOTION = DATA / "selected_finite_projector_source_promotion.candidate.json"

OUTPUT = DATA / "terminaladmissible_axiominsertion_and_smslotfunctor.candidate.json"
CERT = CERTS / "terminaladmissible_axiominsertion_and_smslotfunctor_certificate.json"
NOTE = CORPUS / "MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1.md"

STATUS = "MTT_TERMINALADMISSIBLE_AXIOM_INSERTION_PACKAGE_BUILT_SMSLOTFUNCTOR_SIGNATURE_OPEN"
NEXT = "MTT_SelectedSMSlotFunctor_ValueEmission_or_AxiomPaperPatch_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    terminal = load(TERMINAL_CONDITIONAL)
    dirac = load(DIRAC_GATE)
    projector = load(PROJECTOR_PROMOTION)

    axiom = previous["proposed_axiom"]
    terminal_closure = terminal["conditional_terminal_source_closure"]
    slot_status = terminal["SM_slot_functor_status"]

    insertion_package = {
        "status": "INSERTION_READY_NOT_APPLIED_TO_CORPUS",
        "axiom_name": axiom["name"],
        "axiom_text": axiom["statement"],
        "guardrail_text": axiom["guardrail_clause"],
        "target_papers": [
            {
                "paper": previous["inputs"]["corpus_sources"]["B0_local_admissible_sections"],
                "placement": "after the local admissible section discussion",
                "purpose": "state terminal uniqueness as the finite case where admissible sections become canonical",
            },
            {
                "paper": previous["inputs"]["corpus_sources"]["B2_gauge_fixing_as_section_selection"],
                "placement": "after non-canonicity of gauge fixing",
                "purpose": "explain that ordinary gauge fixing is non-canonical, but finite terminal uniqueness is a special selected-source criterion",
            },
            {
                "paper": previous["inputs"]["corpus_sources"]["B5_minimal_extension"],
                "placement": "after minimal extension/saturation criterion",
                "purpose": "bind minimal added obstruction responsibility to terminal representative selection",
            },
            {
                "paper": previous["inputs"]["corpus_sources"]["C_refinement_stable_operators"],
                "placement": "after refinement-stable discrete descriptions/operators",
                "purpose": "record refinement stability as a required selector predicate",
            },
        ],
        "paper_ready_insert": (
            "Terminal admissible-section selection axiom. For a finite terminal representative class "
            "produced inside an MTT selected sector, if exactly one representative is refinement-stable "
            "under admissible cover/encoding refinement, preserves the shared circle constraint, realizes "
            "the active obstruction or Chern/Bianchi row, and adds no extra obstruction-resolution "
            "responsibility, then that representative is the selected source section. If more than one "
            "representative satisfies these conditions, no selection is made without additional same-source "
            "operator data. This rule is evaluated before observed masses, mixings, benchmark matrices, "
            "locked C1 columns, or diagnostic lifted selected flags are admitted."
        ),
    }

    after_insertion_replay = {
        "can_rerun_terminal_source_as_unconditional_after_insertion": True,
        "promoted_items_after_insertion": {
            "selected_source_label": terminal_closure["selected_source_label"],
            "selected_L": terminal_closure["selected_L"],
            "selected_L2": terminal_closure["selected_L2"],
            "selected_c2": terminal_closure["selected_c2"],
            "base_order": terminal_closure["base_order"],
            "ordered_source_validator_passes": terminal_closure["ordered_source_validator_passes"],
            "cohomology_validator_passes": terminal_closure["cohomology_validator_passes"],
            "h1_Ext_promotes_rank_two_route": terminal_closure["promotes_rank_two_route"],
        },
        "current_repo_status": "ready_for_unconditional_replay_after_paper_or_axiom-packet insertion",
        "why_not_replayed_now_as_unconditional": "The axiom package is drafted but has not yet been inserted into the target corpus papers or proved from projection-admissibility inside this repo.",
    }

    sm_slot_functor_signature = {
        "status": "SIGNATURE_BUILT_VALUES_OPEN",
        "domain": {
            "selected_terminal_source": "g3 / L3-K2",
            "L": terminal_closure["selected_L"],
            "L2": terminal_closure["selected_L2"],
            "h1_Ext_packet": "selected h1=8 nonzero Ext packet under terminal principle",
            "stationary_projector_source": {
                "selected_projector_source_verified": projector["promotion_decision"][
                    "selected_projector_source_verified"
                ],
                "validator_ready_stationary_rho_s": projector["promotion_decision"][
                    "validator_ready_stationary_rho_s"
                ],
                "transported_packet_promoted": projector["promotion_decision"][
                    "transported_packet_promoted"
                ],
            },
        },
        "codomain": {
            "matter_slots": slot_status["slot_contract"],
            "q79_polarization_support": dirac["route_A_SU5_E6_polarization"]["finite_packet"],
            "operator_channels": dirac["same_branch_promotion_contract"]["must_emit"][
                "selected_ordered_matter_slot_packet"
            ],
        },
        "required_arrows": [
            "section-ring/cohomology generator map: terminal Ext source -> 10_M clock row",
            "section-ring/cohomology generator map: terminal Ext source -> bar5_M shift row",
            "section-ring/cohomology generator map: terminal Ext source -> 1_M=N^c Dirac row",
            "selected q79 polarization map emitting U_10=I_3 and U_bar5=F as source outputs",
            "overlap/transfer normalization functor compatible with transported projector bases",
            "same-source consistency map tying the terminal source, projectors, and matter-slot labels",
        ],
        "support_already_closed": {
            "finite_q79_polarization_support": slot_status["support_from_dirac_gate"][
                "finite_q79_polarization_support"
            ],
            "structural_1M_rule_available": slot_status["support_from_dirac_gate"][
                "structural_1M_rule_available"
            ],
            "stationary_projector_source_promoted": projector["promotion_decision"][
                "finite_projector_source_promotion_proved"
            ],
        },
        "values_not_yet_emitted": {
            "selected_U10_Ubar5_source_outputs": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "selected_functor_arrows": True,
        },
    }

    theorem = {
        "name": "TerminalAxiomInsertionAndSMSlotFunctorSignatureTheorem",
        "proved": True,
        "statement": (
            "The terminal admissible-section axiom is now insertion-ready with target paper placements and "
            "guardrails. After insertion or an internal projection-admissibility proof, the terminal source "
            "and h1=8 Ext replay can be rerun as unconditional. Independently, the selected SM-slot functor "
            "has a precise domain, codomain, and arrow list, but its values remain open: U_10/U_bar5, the "
            "1_M Dirac row, overlap normalization, and same-source functor arrows are not emitted yet."
        ),
    }

    data = {
        "candidate": "MTTTerminalAdmissibleAxiomInsertionAndSMSlotFunctor",
        "status": STATUS,
        "inputs": {
            "previous_axiom_promotion_audit": rel(PREVIOUS),
            "terminal_conditional_source": rel(TERMINAL_CONDITIONAL),
            "dirac_polarization_gate": rel(DIRAC_GATE),
            "finite_projector_promotion": rel(PROJECTOR_PROMOTION),
        },
        "superset_strategy": {
            "mode": "AXIOM_INSERTION_PACKAGE_PLUS_FUNCTOR_SIGNATURE",
            "using_one_straight_path": False,
            "primary_path": "insert/prove terminal admissible-section axiom, then rerun terminal source unconditionally",
            "parallel_path": "emit selected SM-slot functor values from the same source",
            "locked_target_role": "forbidden as selector; downstream compatibility only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "insertion_package": insertion_package,
        "after_insertion_replay": after_insertion_replay,
        "SM_slot_functor_signature": sm_slot_functor_signature,
        "what_closes_now": {
            "axiom_insertion_package_ready": True,
            "target_paper_placements_identified": True,
            "unconditional_terminal_replay_conditions_identified": True,
            "SM_slot_functor_signature_built": True,
            "selected_projector_source_imported_as_functor_domain_support": True,
        },
        "what_remains_open": {
            "actually_insert_or_prove_terminal_axiom": True,
            "rerun_terminal_source_as_unconditional_after_axiom": True,
            "selected_SM_slot_functor_values": True,
            "selected_U10_Ubar5_source_outputs": True,
            "selected_1M_Dirac_shift_readout": True,
            "selected_overlap_transfer_normalization": True,
            "operator_layer_Pic0_recheck": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "unconditional_MTT_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "unconditional_MTT_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": data["what_closes_now"],
        "what_remains_open": data["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT TerminalAdmissibleSection AxiomInsertion and SelectedSMSlotFunctor v1

Status: `{STATUS}`.

## Result

The terminal admissible-section axiom is now insertion-ready.  The package names
the target papers, placement points, guardrail language, and the exact theorem
text needed to make the q79 terminal-source result unconditional.

After that insertion, the already-verified replay promotes:

- `g3 / L3-K2`;
- `L=(1,-2,0)`;
- `L^2=(2,-4,0)`;
- base order `E1/g1g2` positive and `E2/g3g4` negative;
- ordered-source validator pass;
- selected `h1=8` nonzero Ext packet.

## SM-Slot Functor

The selected SM-slot functor is now specified as a real typed object.  Its
domain is the selected terminal `L3-K2`/Ext packet plus the transported finite
projector source.  Its codomain is:

```text
10_M -> u,e
bar5_M -> d
1_M=N^c -> nuD
```

with q79 support `U_10=I_3`, `U_bar5=F`.

The values are still open.  We need the selected functor arrows, selected
`U_10/U_bar5` source outputs, selected `1_M` Dirac shift, and overlap/transfer
normalization.

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
