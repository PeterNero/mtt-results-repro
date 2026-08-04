"""Build source-rule derivation attempt or axiom-promotion package."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DERIVATION = PACKET_DIR / "unpatched_source_rule_derivation_attempt.packet.json"
AXIOM_PROMOTION = PACKET_DIR / "explicit_axiom_promotion_package.packet.json"
PAPER_INSERTION = PACKET_DIR / "paper_insertion_workorder.packet.json"
DECISION = PACKET_DIR / "derivation_or_axiom_promotion_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_or_AxiomPromotion_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_SOURCERULE_DERIVATION_OPEN_AXIOMPROMOTION_READY"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_Attack_or_PaperAxiomInsertion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    final_decision = load(DATA / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision.candidate.json")
    route_template = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "route_a_physical_source_theorem_template.packet.json"
    )
    promotion_attempt = load(
        DATA
        / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
        / "physical_c1_variation_source_promotion_attempt.packet.json"
    )
    current = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "current_physical_boundary_firstvariation_attempt.packet.json"
    )
    conditional = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "conditional_physical_source_emission_witness.packet.json"
    )

    missing = promotion_attempt["missing_for_unpatched_promotion"]
    derivation = {
        "schema": "MTTDifferentiatedPhiFinC1SourceRuleDerivationAttempt.v1",
        "status": "UNPATCHED_DERIVATION_ATTEMPT_SUPPORT_COMPLETE_REQUIRED_CLAUSES_OPEN",
        "theorem_target": route_template["theorem_name"],
        "minimal_statement_to_prove": route_template["minimal_statement_to_prove"],
        "closed_support": promotion_attempt["support_closed"],
        "required_clauses": {
            "physical_C1_variation_principle": {
                "closed_now": not missing["derive_or_insert_physical_C1_variation_principle"],
                "current_packet_value": current["physical_first_variation_identity"],
                "conditional_witness_value": conditional["physical_first_variation_identity"],
            },
            "selected_PhiFinC1_applies_Q_residual": {
                "closed_now": not missing["prove_selected_PhiFinC1_applies_Q_residual"],
                "current_packet_value": False,
                "conditional_witness_value": True,
            },
            "selected_dynamic_trace_boundary_cancellation": {
                "closed_now": not missing["prove_boundary_cancellation_for_selected_dynamic_trace"],
                "current_packet_value": current["no_extra_physical_boundary_or_source_term"],
                "conditional_witness_value": conditional["no_extra_physical_boundary_or_source_term"],
            },
            "same_source_b_selected_physical_emission": {
                "closed_now": not missing["emit_b_selected_as_physical_source_not_patch_replay"],
                "current_packet_value": current["same_source_b_selected_emission"],
                "conditional_witness_value": conditional["same_source_b_selected_emission"],
            },
        },
        "current_route_A_emissions": current["current_route_A_emissions"],
        "conditional_witness_validates_if_theorem_supplied": conditional["theorem_derived"] is True,
        "unpatched_source_rule_proved_now": False,
        "why_not_proved": route_template["why_not_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    axiom_promotion = {
        "schema": "MTTDifferentiatedPhiFinC1SourceAxiomPromotionPackage.v1",
        "status": "EXPLICIT_AXIOM_PROMOTION_PACKAGE_READY_NOT_INSERTED",
        "axiom_name": "DifferentiatedPhiFinC1ResidualProjectorAxiom",
        "axiom_text": (
            "On the selected q79/F,m=1 terminal/Theta/Strominger branch, admissible differentiated "
            "Phi_fin^C1 trace variations are governed by the unique C1DefectLeakageFunctional. "
            "Equivalently, the physical C1 action first variation applies the canonical trace/Frobenius "
            "residual projector Q_residual to the selected enriched Weyl-pair legs, emits R_Z and R_X, "
            "has vanishing selected dynamic-trace boundary term, and emits the same-source Hessian vector b_selected."
        ),
        "if_inserted_then": {
            "patched_spine_dynamic_C1_closed": True,
            "A_selected_promoted": True,
            "b_selected_promoted": True,
            "deltaTheta_C1_promoted": True,
            "sector_response_matrices_promoted": True,
        },
        "does_not_by_itself_close": {
            "unpatched_derivation": True,
            "true_SM_equivalence": True,
            "no_knob_flavor_constants": True,
        },
        "acceptance_guardrail": (
            "This is a declared source axiom unless independently derived from unpatched MTT. "
            "It must be labeled as an axiom/premise in papers, not as a theorem proved by prior packets."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    paper_insertion = {
        "schema": "MTTDifferentiatedPhiFinC1SourceAxiomPaperInsertionWorkorder.v1",
        "status": "PAPER_INSERTION_WORKORDER_READY_AWAITING_APPROVAL_OR_DERIVATION",
        "targets": route_template["paper_insertion_targets"],
        "sections_to_add": [
            "Statement of DifferentiatedPhiFinC1ResidualProjectorAxiom",
            "Conditional patched Dynamic C1 closure theorem",
            "Guardrail: unpatched/no-knob derivation remains open",
            "Machine-checkable exact value replay appendix",
        ],
        "theorem_text": (
            "Assuming the DifferentiatedPhiFinC1ResidualProjectorAxiom, the selected dynamic C1 packet "
            "has A^T A=12 I_2, A^T b=(12,12), deltaTheta_C1=(1,1), and promotes A_selected, "
            "b_selected, and sector response matrices in the patched proof spine."
        ),
        "external_papers_modified_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTDifferentiatedPhiFinC1DerivationOrAxiomPromotionDecision.v1",
        "status": "DERIVATION_NOT_CLOSED_AXIOM_PROMOTION_READY",
        "decision": {
            "unpatched_derivation_closes_now": False,
            "axiom_promotion_package_ready": True,
            "honest_galerkin_replacement_still_available": True,
            "recommended_scientific_claim": "axiom-conditional SM-parity dynamic C1 closure",
        },
        "why_this_advances": (
            "The previous final gate named the source rule. This artifact tests that rule against current "
            "Route A evidence, emits the exact four-clause failure matrix, and prepares a paper-safe axiom "
            "promotion package if the project chooses the axiom route."
        ),
        "superset_strategy": {
            "paths": [
                "unpatched physical variation/source derivation",
                "explicit source axiom promotion",
                "honest selected Galerkin replacement",
            ],
            "locked_target": "same dynamic C1 packet with R_Z/R_X/b_selected/deltaTheta",
            "paths_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (DERIVATION, derivation),
        (AXIOM_PROMOTION, axiom_promotion),
        (PAPER_INSERTION, paper_insertion),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1SourceRuleDerivationOrAxiomPromotion",
        "status": STATUS,
        "inputs": {
            "perfected_final_gate": rel(DATA / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision.candidate.json"),
            "route_A_template": rel(
                DATA
                / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                / "route_a_physical_source_theorem_template.packet.json"
            ),
            "promotion_attempt": rel(
                DATA
                / "selected_physicalc1variation_sourcepromotion_or_independentquadratureexecution"
                / "physical_c1_variation_source_promotion_attempt.packet.json"
            ),
        },
        "output_packets": {
            "unpatched_source_rule_derivation_attempt": rel(DERIVATION),
            "explicit_axiom_promotion_package": rel(AXIOM_PROMOTION),
            "paper_insertion_workorder": rel(PAPER_INSERTION),
            "derivation_or_axiom_promotion_decision": rel(DECISION),
        },
        "theorem": {
            "name": "DifferentiatedPhiFinC1SourceRuleDerivationOrAxiomPromotionDecisionTheorem",
            "proved": True,
            "statement": (
                "Current support does not derive the DifferentiatedPhiFinC1ResidualProjectorAxiom "
                "unpatched. It does, however, provide a complete conditional witness and a paper-safe "
                "axiom promotion package. If accepted as an explicit axiom, the patched dynamic C1 packet "
                "closes; otherwise the remaining routes are deriving the axiom or exporting honest selected "
                "Galerkin C1 values."
            ),
        },
        "closure_decision": {
            "unpatched_source_rule_proved": False,
            "axiom_promotion_ready": True,
            "patched_spine_dynamic_C1_closed_if_axiom_inserted": True,
            "external_papers_modified": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "four_clause_derivation_failure_matrix_built": True,
            "explicit_axiom_promotion_package_ready": True,
            "paper_insertion_workorder_ready": True,
            "conditional_witness_retained": True,
        },
        "what_remains_open": {
            "derive_axiom_unpatched": True,
            "or_insert_axiom_into_target_papers": True,
            "or_export_honest_selected_galerkin_tables": True,
            "true_SM_equivalence_without_axiom": True,
            "no_knob_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_or_AxiomPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "unpatched_source_rule_proved": False,
        "axiom_promotion_ready": True,
        "external_papers_modified": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1 SourceRule Derivation or AxiomPromotion v1

Status: `{STATUS}`.

This artifact attacks the final source rule directly.

Result:

- unpatched derivation is still open;
- the four missing clauses are explicit and machine-checkable;
- an explicit source-axiom promotion package is ready;
- a paper insertion workorder is ready but not applied.

If the axiom is accepted, the patched proof spine closes the dynamic C1 packet.
If the axiom is not accepted, the remaining routes are deriving it from
unpatched MTT/Theta/Strominger action data or exporting honest selected
Galerkin C1 tables.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
