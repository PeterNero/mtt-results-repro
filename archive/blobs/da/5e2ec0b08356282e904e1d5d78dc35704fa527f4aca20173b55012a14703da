"""Build PSM-C1-02 unpatched source-rule proof or honest Galerkin export gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_unpatched_source_rule_proof_attempt.packet.json"
ROUTE_A_LADDER = PACKET_DIR / "route_a_four_clause_ladder.packet.json"
ROUTE_B = PACKET_DIR / "route_b_honest_galerkin_export_manifest.packet.json"
IMPLICATION = PACKET_DIR / "psm_c1_02_unpatched_closure_implication.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedSourceRuleProof_or_HonestGalerkinExport_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_UNPATCHEDSOURCERULEPROOF_OR_HONESTGALERKINEXPORT_BUILT_INPUTS_SHARP"
PREVIOUS_SLUG = "selected_psm_c1_02_selectedsourcepromotionpacket"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_RouteAClause1_PhysicalC1Variation_or_RouteBInputBasisFill_v1"

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
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def path_status(path_text: str) -> dict[str, Any]:
    path = ROOT / path_text
    return {
        "path": path_text,
        "exists_now": path.exists(),
        "selected_emitted": False,
        "theorem_derived": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / f"{PREVIOUS_SLUG}.candidate.json")
    source_matrix = load(DATA / PREVIOUS_SLUG / "psm_c1_02_source_promotion_matrix.packet.json")
    source_rule_attempt = load(DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion" / "unpatched_source_rule_derivation_attempt.packet.json")
    route_decision = load(DATA / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution" / "route_decision_and_next_inputs.packet.json")
    final_gate = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues" / "final_dynamic_value_gate.packet.json")
    ready_values = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues" / "ready_to_promote_dynamic_value_table.packet.json")
    conditional_source_packet = load(DATA / PREVIOUS_SLUG / "conditional_unpatched_selected_source_promotion_packet.packet.json")
    conditional_source_result = load(DATA / PREVIOUS_SLUG / "conditional_unpatched_source_promotion_validator_result.packet.json")

    required_clauses = source_rule_attempt["required_clauses"]
    route_a = {
        "schema": "MTTPSMC102RouteAUnpatchedSourceRuleProofAttempt.v1",
        "status": "ROUTE_A_UNPATCHED_SOURCE_RULE_SUPPORT_COMPLETE_REQUIRED_CLAUSES_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "theorem_target": source_rule_attempt["theorem_target"],
        "minimal_statement_to_prove": source_rule_attempt["minimal_statement_to_prove"],
        "closed_support": source_rule_attempt["closed_support"],
        "required_clauses": required_clauses,
        "all_required_clauses_closed_now": all(item["closed_now"] for item in required_clauses.values()),
        "unpatched_source_rule_proved_now": source_rule_attempt["unpatched_source_rule_proved_now"],
        "why_not_proved": source_rule_attempt["why_not_proved"],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    route_a_ladder = {
        "schema": "MTTPSMC102RouteAFourClauseLadder.v1",
        "status": "ROUTE_A_FOUR_CLAUSES_ORDERED_FOR_NEXT_ATTACK",
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-A",
        "ordered_clauses": [
            {
                "clause_id": "RA-1",
                "name": "physical_C1_variation_principle",
                "task": "Identify the physical C1 action first variation with the C1 defect leakage normal equation.",
                "closed_now": required_clauses["physical_C1_variation_principle"]["closed_now"],
            },
            {
                "clause_id": "RA-2",
                "name": "selected_dynamic_trace_boundary_cancellation",
                "task": "Prove selected admissible differentiated variations have no extra physical boundary/source term.",
                "closed_now": required_clauses["selected_dynamic_trace_boundary_cancellation"]["closed_now"],
            },
            {
                "clause_id": "RA-3",
                "name": "selected_PhiFinC1_applies_Q_residual",
                "task": "Show differentiated Phi_fin^C1 applies the canonical residual projector and emits R_Z/R_X before replay.",
                "closed_now": required_clauses["selected_PhiFinC1_applies_Q_residual"]["closed_now"],
            },
            {
                "clause_id": "RA-4",
                "name": "same_source_b_selected_physical_emission",
                "task": "Emit b_selected from the same physical source, not from A^T b replay.",
                "closed_now": required_clauses["same_source_b_selected_physical_emission"]["closed_now"],
            },
        ],
        "first_open_clause": "RA-1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    missing_inputs = route_decision["route_B_honest_galerkin_execution"]["next_missing_inputs"]
    route_b = {
        "schema": "MTTPSMC102RouteBHonestGalerkinExportManifest.v1",
        "status": "ROUTE_B_HONEST_GALERKIN_EXPORT_SPEC_READY_INPUTS_OPEN",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "route_label": "ROUTE-B",
        "ready_as_execution_spec": route_decision["route_B_honest_galerkin_execution"]["ready_as_execution_spec"],
        "run_now": route_decision["route_B_honest_galerkin_execution"]["run_now"],
        "would_close_dynamic_packet_if_values_pass": route_decision["route_B_honest_galerkin_execution"]["would_close_dynamic_packet_if_values_pass"],
        "missing_selected_inputs": [path_status(path) for path in missing_inputs],
        "missing_input_count": len(missing_inputs),
        "all_missing_inputs_exist_now": all((ROOT / path).exists() for path in missing_inputs),
        "honest_galerkin_table_exported": final_gate["closure_decision"]["honest_galerkin_table_exported"],
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    implication = {
        "schema": "MTTPSMC102UnpatchedClosureImplication.v1",
        "status": "UNPATCHED_CLOSURE_REDUCED_TO_ROUTE_A_CLAUSES_OR_ROUTE_B_INPUT_EXPORT",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "source_promotion_conditional_packet_passes": conditional_source_result["passes"],
        "conditional_source_packet": conditional_source_packet["status"],
        "current_source_promotion_packet_passes": source_matrix["current_packet_passes"],
        "patched_packet_rejected_for_unpatched_proof": not source_matrix["patched_packet_passes_unpatched_validator"],
        "exact_dynamic_values_ready": final_gate["closure_decision"]["dynamic_values_ready"],
        "ready_values_status": ready_values["status"],
        "route_A_would_close_if_all_four_clauses": True,
        "route_B_would_close_if_four_inputs_exported_and_strict_validator_passes": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    theorem = {
        "name": "PSMC102UnpatchedSourceRuleOrHonestGalerkinExportReductionTheorem",
        "proved": True,
        "statement": (
            "For label PSM-C1-02, unpatched source promotion is reduced to two labelled exits. ROUTE-A must prove four "
            "physical source-rule clauses: physical C1 variation principle, selected dynamic boundary cancellation, "
            "Phi_fin^C1 application of Q_residual producing R_Z/R_X, and same-source b_selected emission. ROUTE-B must "
            "export four selected Galerkin execution inputs: zero-mode basis, primitive contraction terms, Hessian source "
            "vector, and sector response matrices. Exact dynamic values and the conditional source-promotion packet are "
            "ready, but neither route is currently filled."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102UnpatchedSourceRuleProofOrHonestGalerkinExport",
        "status": STATUS,
        "previous_artifact": rel(DATA / f"{PREVIOUS_SLUG}.candidate.json"),
        "previous_status": previous["status"],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_routes": ["ROUTE-A", "ROUTE-B"],
        "theorem": theorem,
        "what_closes_now": {
            "ROUTE_A_four_clause_ladder_created": True,
            "ROUTE_B_four_input_manifest_created": True,
            "conditional_source_promotion_implication_preserved": True,
            "patched_axiom_excluded_from_unpatched_route": True,
            "labels_preserved_for_next_work": True,
        },
        "what_remains_open": {
            "ROUTE_A_RA_1_physical_C1_variation_principle": True,
            "ROUTE_A_RA_2_boundary_cancellation": True,
            "ROUTE_A_RA_3_Q_residual_application": True,
            "ROUTE_A_RA_4_b_selected_emission": True,
            "ROUTE_B_selected_zero_mode_basis": True,
            "ROUTE_B_primitive_contraction_terms": True,
            "ROUTE_B_hessian_source_vector": True,
            "ROUTE_B_sector_response_matrices": True,
        },
        "output_packets": {
            "route_a_unpatched_source_rule_proof_attempt": rel(ROUTE_A),
            "route_a_four_clause_ladder": rel(ROUTE_A_LADDER),
            "route_b_honest_galerkin_export_manifest": rel(ROUTE_B),
            "unpatched_closure_implication": rel(IMPLICATION),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102UnpatchedSourceRuleOrGalerkinExport.v1",
        "status": "NEXT_WORKORDER_ROUTE_A_RA1_OR_ROUTE_B_INPUT_BASIS_FILL",
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route_label": "ROUTE-A",
            "clause_id": "RA-1",
            "task": "Prove physical C1 variation principle from unpatched MTT/Theta/Strominger action.",
        },
        "secondary": {
            "route_label": "ROUTE-B",
            "input_id": "RB-1",
            "task": "Emit selected zero-mode basis input packet for honest Galerkin execution.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "MTT_Selected_PSM_C1_02_UnpatchedSourceRuleProof_or_HonestGalerkinExport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "active_label": "PSM-C1-02",
        "routes": ["ROUTE-A", "ROUTE-B"],
        "route_A_all_clauses_closed": route_a["all_required_clauses_closed_now"],
        "route_B_run_now": route_b["run_now"],
        "conditional_source_promotion_packet_passes": conditional_source_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PSM C1 02 UnpatchedSourceRuleProof or HonestGalerkinExport v1

Status label: `PSM-C1-02 / ROUTE-A / ROUTE-B`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Route Status

- `PSM-C1-02 / ROUTE-A`: four unpatched source-rule clauses are ordered as `RA-1` through `RA-4`; all remain open.
- `PSM-C1-02 / ROUTE-B`: honest Galerkin execution is a ready spec, but the four selected input packets remain unexported.
- `PSM-C1-02 / CONDITIONAL`: the conditional source-promotion packet still validates.

## Next Artifact

`{NEXT_ARTIFACT}`
"""

    write_json(ROUTE_A, route_a)
    write_json(ROUTE_A_LADDER, route_a_ladder)
    write_json(ROUTE_B, route_b)
    write_json(IMPLICATION, implication)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
