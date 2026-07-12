"""Build PSM-C1-02 Route-A RA-1 or Route-B RB-1 input-basis fill gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_routea_clause1_or_routeb_inputbasisfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_ra1_physical_c1_variation_principle_attempt.packet.json"
ROUTE_B = PACKET_DIR / "route_b_rb1_zero_mode_basis_input_fill.packet.json"
RB1_INPUT = DATA / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "inputs" / "zero_mode_basis.packet.json"
DECISION = PACKET_DIR / "psm_c1_02_ra1_rb1_decision.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_RouteAClause1_PhysicalC1Variation_or_RouteBInputBasisFill_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_ROUTEA_RA1_OR_ROUTEB_RB1_BUILT_RB1_INPUT_FILLED_SELECTION_OPEN"
PREVIOUS_SLUG = "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_RouteA_RA1_DerivationAttack_or_RouteB_RB2_PrimitiveTermsFill_v1"

POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / f"{PREVIOUS_SLUG}.candidate.json")
    previous_route_a = load(DATA / PREVIOUS_SLUG / "route_a_four_clause_ladder.packet.json")
    previous_route_b = load(DATA / PREVIOUS_SLUG / "route_b_honest_galerkin_export_manifest.packet.json")
    source_rule_attempt = load(DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion" / "unpatched_source_rule_derivation_attempt.packet.json")
    support_basis = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "zero_mode_basis.packet.json")
    hym_basis_theorem = load(DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json")

    ra1_clause = source_rule_attempt["required_clauses"]["physical_C1_variation_principle"]
    route_a = {
        "schema": "MTTPSMC102RouteARA1PhysicalC1VariationPrincipleAttempt.v1",
        "status": "ROUTE_A_RA1_SUPPORT_IDENTIFIED_UNPATCHED_DERIVATION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "clause_id": "RA-1",
        "clause_name": "physical_C1_variation_principle",
        "current_clause": ra1_clause,
        "closed_now": ra1_clause["closed_now"],
        "conditional_witness_value": ra1_clause["conditional_witness_value"],
        "minimal_statement": "The physical C1 action first variation equals the C1DefectLeakageFunctional normal equation on the selected q79/F,m=1 terminal/Theta/Strominger branch.",
        "support_available": {
            "finite_variational_euler_projection": source_rule_attempt["closed_support"]["finite_variational_euler_projection"],
            "canonical_Q_residual_available": source_rule_attempt["closed_support"]["canonical_Q_residual_available"],
            "least_norm_completion_selects_Q_residual": source_rule_attempt["closed_support"]["least_norm_completion_selects_Q_residual"],
            "alpha1_dotD_driver_verified": source_rule_attempt["closed_support"]["alpha1_dotD_driver_verified"],
        },
        "why_not_proved": [
            "The corpus still identifies a candidate leakage functional, not an unpatched physical action equality.",
            "The accepted local axiom would close this, but accepting it here would use a patch.",
            "RA-1 must be derived from unpatched MTT/Theta/Strominger action text or replaced by ROUTE-B selected execution.",
        ],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rb1_input_packet = {
        "schema": "MTTPSMC102RouteBRB1ZeroModeBasisInputPacket.v1",
        "status": "ROUTE_B_RB1_ZERO_MODE_BASIS_INPUT_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-1",
        "input_name": "selected zero-mode basis input packet for honest Galerkin execution",
        "source_support": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs" / "zero_mode_basis.packet.json"),
        "hym_projector_theorem": rel(DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"),
        "basis_dimension": support_basis["basis_dimension"],
        "basis": support_basis["basis"],
        "support_basis_status": support_basis["status"],
        "support_selected_source_verified": support_basis["selected_source_verified"],
        "hym_selected_values_emitted": hym_basis_theorem["theorem"]["selected_values_emitted"],
        "hym_projector_values_open": hym_basis_theorem["finite_acceptance_validator"]["passes_now"] is False,
        "selected_emitted": False,
        "theorem_derived": False,
        "source_owner_verified": False,
        "same_branch": True,
        "why_selection_open": [
            support_basis["why_not_honest_selected_yet"],
            "The HYM projector basis theorem is a bridge theorem; selected projector/basis values remain open.",
            "This file fills the execution input slot for RB-1 but does not promote the basis as an honest selected Galerkin source.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(RB1_INPUT, rb1_input_packet)

    route_b = {
        "schema": "MTTPSMC102RouteBRB1InputBasisFill.v1",
        "status": "ROUTE_B_RB1_INPUT_PATH_FILLED_SUPPORT_LEVEL_SELECTION_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "input_id": "RB-1",
        "filled_input_path": rel(RB1_INPUT),
        "input_file_exists_now": RB1_INPUT.exists(),
        "basis_dimension": rb1_input_packet["basis_dimension"],
        "selected_emitted": rb1_input_packet["selected_emitted"],
        "theorem_derived": rb1_input_packet["theorem_derived"],
        "source_owner_verified": rb1_input_packet["source_owner_verified"],
        "remaining_route_b_inputs": [
            item
            for item in previous_route_b["missing_selected_inputs"]
            if not item["path"].endswith("zero_mode_basis.packet.json")
        ],
        "remaining_route_b_input_count_after_rb1": previous_route_b["missing_input_count"] - 1,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPSMC102RA1RB1Decision.v1",
        "status": "RA1_OPEN_RB1_INPUT_FILLED_SELECTION_OPEN_NEXT_RA1_ATTACK_OR_RB2_FILL",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_A": {
            "route_label": "ROUTE-A",
            "clause_id": "RA-1",
            "closed_now": route_a["closed_now"],
            "free_axiom_patch_used": route_a["free_axiom_patch_used"],
        },
        "route_B": {
            "route_label": "ROUTE-B",
            "input_id": "RB-1",
            "input_filled_now": True,
            "selected_source_promoted_now": False,
            "remaining_input_count": route_b["remaining_route_b_input_count_after_rb1"],
        },
        "superset_strategy": {
            "using_one_straight_path": False,
            "combined_paths": ["ROUTE-A RA-1 unpatched derivation", "ROUTE-B RB-1 support-level input fill"],
            "locked_target": "same PSM-C1-02 source-promotion packet and 72-real Galerkin execution target",
            "paths_used_as_knobs": False,
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PSMC102RouteAClause1OrRouteBInputBasisFillTheorem",
        "proved": True,
        "statement": (
            "For PSM-C1-02, ROUTE-A/RA-1 remains open because current support does not derive the physical C1 variation "
            "principle from unpatched MTT/Theta/Strominger action. In parallel, ROUTE-B/RB-1 can now be filled as a support-level "
            "zero-mode basis input for honest Galerkin execution by importing the canonical qutrit matrix-unit basis and HYM "
            "projector bridge, but this does not promote selected zero-mode values because the HYM projector value-emission gate "
            "remains open."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102RouteAClause1PhysicalC1VariationOrRouteBInputBasisFill",
        "status": STATUS,
        "previous_artifact": rel(DATA / f"{PREVIOUS_SLUG}.candidate.json"),
        "previous_status": previous["status"],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A/RA-1", "ROUTE-B/RB-1"],
        "theorem": theorem,
        "what_closes_now": {
            "ROUTE_A_RA1_support_matrix_recorded": True,
            "ROUTE_B_RB1_zero_mode_basis_input_file_filled": True,
            "RB1_selected_source_promotion_guarded_open": True,
            "superset_strategy_locked_to_same_target": True,
        },
        "what_remains_open": {
            "ROUTE_A_RA1_unpatched_physical_C1_variation_derivation": True,
            "ROUTE_B_RB1_selected_HYM_projector_basis_value_emission": True,
            "ROUTE_B_RB2_primitive_contraction_terms": True,
            "ROUTE_B_RB3_hessian_source_vector": True,
            "ROUTE_B_RB4_sector_response_matrices": True,
        },
        "output_packets": {
            "route_a_ra1_attempt": rel(ROUTE_A),
            "route_b_rb1_fill": rel(ROUTE_B),
            "route_b_rb1_input_file": rel(RB1_INPUT),
            "decision": rel(DECISION),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102RA1RB1.v1",
        "status": "NEXT_WORKORDER_RA1_DERIVATION_ATTACK_OR_RB2_PRIMITIVE_TERMS_FILL",
        "active_label": "PSM-C1-02",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route_label": "ROUTE-A",
            "clause_id": "RA-1",
            "task": "Attack the unpatched derivation of the physical C1 variation principle.",
        },
        "secondary": {
            "route_label": "ROUTE-B",
            "input_id": "RB-2",
            "task": "Fill primitive contraction terms input packet for honest Galerkin execution.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "MTT_Selected_PSM_C1_02_RouteAClause1_PhysicalC1Variation_or_RouteBInputBasisFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "active_label": "PSM-C1-02",
        "route_A_clause": "RA-1",
        "route_A_RA1_closed": route_a["closed_now"],
        "route_B_input": "RB-1",
        "route_B_RB1_input_filled": True,
        "route_B_RB1_selected_promoted": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM C1 02 RouteAClause1 PhysicalC1Variation or RouteBInputBasisFill v1

Status label: `PSM-C1-02 / ROUTE-A / RA-1` and `PSM-C1-02 / ROUTE-B / RB-1`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Route Status

- `PSM-C1-02 / ROUTE-A / RA-1`: open; no unpatched physical C1 action equality has been derived.
- `PSM-C1-02 / ROUTE-B / RB-1`: input file filled at support level; selected HYM/zero-mode value promotion remains open.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    write_json(ROUTE_A, route_a)
    write_json(ROUTE_B, route_b)
    write_json(DECISION, decision)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
