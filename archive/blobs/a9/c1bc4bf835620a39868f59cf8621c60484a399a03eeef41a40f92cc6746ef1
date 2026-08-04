"""Build the terminal admissible-section principle promotion audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_terminalmap_sourceprinciple_or_smslotfunctor.candidate.json"

OUTPUT = DATA / "terminaladmissible_principle_promotion_or_smslotfunctor.candidate.json"
CERT = CERTS / "terminaladmissible_principle_promotion_or_smslotfunctor_certificate.json"
NOTE = CORPUS / "MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1.md"

STATUS = "MTT_TERMINALADMISSIBLE_PRINCIPLE_PROMOTION_AUDITED_AXIOM_INSERTION_OR_SMSLOTFUNCTOR_OPEN"
NEXT = "MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1"

CORE = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\1 Core & Encodings")
DELTA = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\5 Dirac Delta")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    previous = load(PREVIOUS)

    corpus_sources = {
        "B0_local_admissible_sections": str(
            CORE / "The_Modal_Triplet_Theory_Program_B0__Why_Description_Forces_Circle__Lens__and_Nil.md"
        ),
        "B2_gauge_fixing_as_section_selection": str(
            CORE / "The_Modal_Triplet_Theory_Program_B2__Gauge_Structure_as_Redundancy_Encoding.md"
        ),
        "B3_nil_survivors": str(
            CORE / "The_Modal_Triplet_Theory_Program_B3__Quantization_as_Discrete_Constraint_Encoding.md"
        ),
        "B5_minimal_extension": str(
            CORE / "The_Modal_Triplet_Theory_Program_B5__Saturated_and_Unified_Encodings.md"
        ),
        "C_refinement_stable_operators": str(
            CORE / "The_Modal_Triplet_Theory_Program_C__Realizing_the_Modal_Triplet_Core.md"
        ),
        "delta_gauge_fixing": str(
            DELTA / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
        ),
        "delta_projection": str(
            DELTA / "Dirac_Delta_Functions_as_Singular_Shadows_of_Admissible_Projection.md"
        ),
        "finite_projection": str(DELTA / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"),
    }

    promotion_audit = {
        "corpus_supports": {
            "local_admissible_sections_exist": True,
            "representatives_are_not_fundamental_objects": True,
            "gauge_fixing_is_admissible_section_selection": True,
            "delta_kernels_can_idealize_representative_selection": True,
            "nil_boundaries_select_discrete_survivors": True,
            "refinement_stable_descriptions_are_privileged": True,
            "minimal_extension_required_by_saturation": True,
        },
        "not_yet_in_corpus_as_general_axiom": {
            "terminal_unique_refinement_stable_survivor_selects_source": True,
            "minimal_added_obstruction_responsibility_total_order": True,
            "visible_Chern_Bianchi_compatibility_as_terminal_selector": True,
        },
        "why_not_enough_for_unconditional_proof": (
            "Existing corpus proves the language and admissibility of representative selection, "
            "but also warns that gauge fixing is generally non-canonical. The terminal theorem "
            "needs an extra finite-terminal uniqueness clause: once a quotient class has been "
            "reduced to finitely many terminal representatives, the unique representative that "
            "is refinement-stable, central-neutral, minimal, and compatible with the active "
            "Chern/Bianchi obstruction is the selected source."
        ),
    }

    proposed_axiom = {
        "name": "TerminalAdmissibleSectionSelectionAxiom",
        "statement": (
            "For a finite terminal representative class produced inside an MTT selected sector, "
            "if exactly one representative is refinement-stable under admissible cover/encoding "
            "refinement, preserves the shared circle constraint, realizes the active obstruction "
            "or Chern/Bianchi row, and adds no extra obstruction-resolution responsibility, then "
            "that representative is the selected source section. If more than one representative "
            "satisfies these conditions, no selection is made without additional same-source "
            "operator data."
        ),
        "guardrail_clause": (
            "The axiom is evaluated before observed masses, mixings, benchmark matrices, locked "
            "C1 columns, or diagnostic lifted selected flags are admitted."
        ),
        "why_it_matches_terminal_q79_case": {
            "finite_terminal_class": "L_i-K2 terminal monad differences",
            "unique_refinement_stable_candidate_under_filters": "g3 / L3-K2",
            "shared_circle_constraint": "central degree zero",
            "active_obstruction_row": "c2(V_alpha)=4 alpha_1 with c1(V_alpha)=0",
            "base_order": "E1/g1g2 positive and E2/g3g4 negative",
        },
    }

    sm_slot_functor_parallel = {
        "still_needed": previous["SM_slot_functor_status"]["needed_functor"],
        "can_bypass_axiom_promotion_for_slot_readout": True,
        "must_emit": [
            "selected U_10=I_3 and U_bar5=F as outputs, not fixtures",
            "selected 1_M=N^c Dirac-neutrino slot rule",
            "selected overlap/transfer normalization",
            "same-source consistency with the terminal L3-K2/H1/Ext packet",
        ],
    }

    theorem = {
        "name": "TerminalAdmissibleSectionPrinciplePromotionAuditTheorem",
        "proved": True,
        "statement": (
            "The existing MTT corpus supports admissible representative selection, nil survivor "
            "selection, refinement stability, and minimal saturation, but it does not yet contain "
            "the exact terminal uniqueness axiom needed to make q79's TerminalAdmissibleSection "
            "principle unconditional. Therefore the rigorous next step is either to insert/prove "
            "the proposed terminal admissible-section axiom or to bypass it by emitting the selected "
            "SM-slot functor from the same source."
        ),
    }

    candidate = {
        "candidate": "MTTTerminalAdmissiblePrinciplePromotionOrSMSlotFunctor",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "corpus_sources": corpus_sources,
        },
        "superset_strategy": {
            "mode": "AXIOM_PROMOTION_AUDIT_WITH_PARALLEL_SMSLOT_ROUTE",
            "using_one_straight_path": False,
            "primary_path": "promote or derive terminal admissible-section selection axiom",
            "parallel_path": "emit selected SM-slot functor directly",
            "locked_target_role": "forbidden as selector; only downstream compatibility after selected source",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "promotion_audit": promotion_audit,
        "proposed_axiom": proposed_axiom,
        "SM_slot_functor_parallel": sm_slot_functor_parallel,
        "what_closes_now": {
            "principle_promotion_gap_identified": True,
            "corpus_support_for_axiom_scaffold_collected": True,
            "exact_axiom_text_drafted": True,
            "noncanonical_gauge_fixing_guardrail_retained": True,
            "SM_slot_functor_parallel_route_retained": True,
        },
        "what_remains_open": {
            "insert_axiom_into_target_papers_or_prove_from_projection_admissibility": True,
            "rerun_terminal_source_as_unconditional_after_axiom": True,
            "selected_SM_slot_functor": True,
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

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "certificate": "MTT_TerminalAdmissibleSection_PrinciplePromotion_or_SelectedSMSlotFunctor_v1",
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
        """# MTT TerminalAdmissibleSection PrinciplePromotion or SelectedSMSlotFunctor v1

Status: `MTT_TERMINALADMISSIBLE_PRINCIPLE_PROMOTION_AUDITED_AXIOM_INSERTION_OR_SMSLOTFUNCTOR_OPEN`

The corpus supports the ingredients of q79's
`TerminalAdmissibleSectionSourcePrinciple`: admissible section selection,
representative selection, nil survivor selection, refinement-stable operators,
and minimal saturation.

But the corpus also warns that representative choice is generally
non-canonical.  So the unconditional theorem needs one explicit terminal
uniqueness clause.

## Proposed Axiom

For a finite terminal representative class produced inside an MTT selected
sector, if exactly one representative is refinement-stable under admissible
cover/encoding refinement, preserves the shared circle constraint, realizes the
active obstruction or Chern/Bianchi row, and adds no extra
obstruction-resolution responsibility, then that representative is the selected
source section.

If more than one representative satisfies these conditions, no selection is
made without additional same-source operator data.

This is evaluated before observed masses, mixings, benchmark matrices, locked
`C1` columns, or diagnostic lifted selected flags are admitted.

## Current Meaning

This does not yet claim unconditional MTT closure. It gives the exact insertion
needed to make the q79 terminal-source result unconditional, or else the
parallel selected SM-slot functor can bypass the axiom-promotion step for the
matter-slot readout.

Next artifact:
`MTT_TerminalAdmissibleSection_AxiomInsertion_and_SelectedSMSlotFunctor_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
