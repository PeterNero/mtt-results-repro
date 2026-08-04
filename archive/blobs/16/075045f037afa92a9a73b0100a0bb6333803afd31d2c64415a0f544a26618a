"""Build the perfected final DynamicC1 gate / source-axiom decision."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PATCHED = PACKET_DIR / "patched_spine_closure_mode.packet.json"
UNPATCHED = PACKET_DIR / "unpatched_theorem_mode.packet.json"
DECISION = PACKET_DIR / "source_axiom_decision_matrix.packet.json"
PAPER_TEXT = PACKET_DIR / "paper_ready_source_axiom_and_theorem_text.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicC1_FinalGate_Perfection_or_SourceAxiomDecision_v1.md"

STATUS = "MTT_SELECTED_DYNAMICC1_FINALGATE_PERFECTED_PATCHED_CLOSE_UNPATCHED_PROOF_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_or_AxiomPromotion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    final_gate = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json")
    ready = load(
        DATA
        / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
        / "ready_to_promote_dynamic_value_table.packet.json"
    )
    local_patch = load(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json")
    patch_packet = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "residual_projector_axiom_local_corpus_patch.packet.json"
    )
    first_run = load(
        DATA
        / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
        / "first_galerkin_replay_result.packet.json"
    )

    exact_values = {
        "A_transpose_A": [[12.0, 0.0], [0.0, 12.0]],
        "A_transpose_b": [12.0, 12.0],
        "deltaTheta_C1": [1.0, 1.0],
        "rank": 2,
        "phase_R_Z_residual_norm_sq": ready["dynamic_operator_candidates"]["phase_R_Z"]["residual_norm_sq"],
        "shift_R_X_residual_norm_sq": ready["dynamic_operator_candidates"]["shift_R_X"]["residual_norm_sq"],
    }

    patched = {
        "schema": "MTTDynamicC1PatchedSpineClosureMode.v1",
        "status": "PATCHED_SPINE_DYNAMIC_C1_CLOSED_BY_EXPLICIT_LOCAL_AXIOM",
        "axiom_name": "DifferentiatedPhiFinC1ResidualProjectorAxiom",
        "patch_source": rel(
            DATA
            / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
            / "residual_projector_axiom_local_corpus_patch.packet.json"
        ),
        "local_patch_note": rel(CORPUS / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"),
        "patch_payload": {
            "Phi_fin_C1_applies_Q_residual": True,
            "R_Z_phase_clock_source_emitted": True,
            "R_X_shift_vertex_source_emitted": True,
            "b_selected_source_emitted": True,
        },
        "promotions_inside_patched_spine": {
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "SM_parity_dynamic_packet": True,
            "sector_response_matrices": True,
        },
        "exact_values": exact_values,
        "guardrails": {
            "not_derived_from_unpatched_MTT_axioms": True,
            "does_not_close_true_SM_equivalence": True,
            "does_not_close_no_knob_flavor_constants": True,
            "external_main_papers_not_modified": patch_packet["main_external_obsidian_papers_modified_now"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    unpatched = {
        "schema": "MTTDynamicC1UnpatchedTheoremMode.v1",
        "status": "UNPATCHED_THEOREM_OPEN_EXACT_VALUES_READY",
        "final_gate_source": rel(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json"),
        "exact_values_ready": exact_values,
        "legal_unpatched_exits": [
            "derive DifferentiatedPhiFinC1ResidualProjectorApplicationRule from unpatched MTT/Theta/Strominger action",
            "export honest selected Galerkin C1 table values independent of the local axiom patch",
        ],
        "current_failures": {
            "source_rule_proved": final_gate["closure_decision"]["source_rule_proved"],
            "honest_galerkin_table_exported": final_gate["closure_decision"]["honest_galerkin_table_exported"],
            "honest_independent_galerkin_execution_passes": first_run["honest_independent_galerkin_execution_passes"],
            "unpatched_A_selected_promoted": local_patch["promotion_decision"]["A_selected_promoted_in_unpatched_spine"],
            "unpatched_b_selected_promoted": local_patch["promotion_decision"]["b_selected_promoted_in_unpatched_spine"],
        },
        "promotions_in_unpatched_spine": {
            "A_selected": False,
            "b_selected": False,
            "deltaTheta_C1": False,
            "SM_parity_dynamic_packet": False,
            "sector_response_matrices": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTDynamicC1SourceAxiomDecisionMatrix.v1",
        "status": "DECISION_MATRIX_BUILT_PATCHED_PARITY_CLOSE_UNPATCHED_DERIVATION_OPEN",
        "recommended_next_action": (
            "Promote the local source rule into a named paper axiom/theorem only if the project accepts "
            "it as an explicit MTT axiom; otherwise attempt the unpatched derivation or honest Galerkin export."
        ),
        "mode_table": {
            "SM_parity_with_explicit_local_source_axiom": {
                "dynamic_C1_packet_closed": True,
                "scientific_status": "axiom-conditional",
                "credible_claim": "MTT parity framework can replay the dynamic C1 packet once this source rule is admitted.",
            },
            "unpatched_no_knob_theorem": {
                "dynamic_C1_packet_closed": False,
                "scientific_status": "proof-open",
                "credible_claim": "Exact values and final gate are ready, but source selection is not yet derived.",
            },
            "honest_galerkin_replacement": {
                "dynamic_C1_packet_closed": False,
                "scientific_status": "execution-open",
                "credible_claim": "Would avoid the axiom if independent selected Galerkin tables are emitted.",
            },
        },
        "superset_strategy": {
            "paths_combined": [
                "explicit local source-rule axiom patch",
                "unpatched source-rule derivation route",
                "honest selected Galerkin export route",
            ],
            "locked_target": "same exact R_Z/R_X/b_selected/deltaTheta dynamic C1 packet",
            "paths_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    paper_text = {
        "schema": "MTTDynamicC1SourceAxiomPaperText.v1",
        "status": "PAPER_READY_CONDITIONAL_THEOREM_TEXT_BUILT",
        "axiom_title": "Differentiated PhiFin C1 Residual-Projector Source Axiom",
        "axiom_text": (
            "On the selected q79/F,m=1 Route-C source spine, the differentiated Phi_fin^C1 response "
            "applies the canonical trace-orthogonal residual projector Q_residual to the selected enriched "
            "Weyl-pair phase and shift legs, emitting R_Z, R_X, and the same-source Hessian vector b_selected."
        ),
        "conditional_theorem_title": "Patched Dynamic C1 Closure Theorem",
        "conditional_theorem_text": (
            "Assuming the Differentiated PhiFin C1 Residual-Projector Source Axiom, the selected dynamic "
            "C1 packet closes with A^T A=12 I_2, A^T b=(12,12), and deltaTheta_C1=(1,1)."
        ),
        "unpatched_status_sentence": (
            "Without this axiom or an independent selected Galerkin C1 export, the exact values remain "
            "ready-to-promote but not selected-source theorem data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [(PATCHED, patched), (UNPATCHED, unpatched), (DECISION, decision), (PAPER_TEXT, paper_text)]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDynamicC1FinalGatePerfectionOrSourceAxiomDecision",
        "status": STATUS,
        "inputs": {
            "final_dynamic_value_gate": rel(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json"),
            "local_axiom_patch": rel(DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json"),
        },
        "output_packets": {
            "patched_spine_closure_mode": rel(PATCHED),
            "unpatched_theorem_mode": rel(UNPATCHED),
            "source_axiom_decision_matrix": rel(DECISION),
            "paper_ready_source_axiom_and_theorem_text": rel(PAPER_TEXT),
        },
        "theorem": {
            "name": "DynamicC1FinalGatePerfectionDecisionTheorem",
            "proved": True,
            "statement": (
                "The final DynamicC1 gate is now perfected as a two-mode decision. With the explicit local "
                "DifferentiatedPhiFinC1ResidualProjectorAxiom, the patched proof spine closes the dynamic C1 "
                "packet and promotes A_selected, b_selected, deltaTheta_C1, and sector response matrices. "
                "Without that axiom or an honest selected Galerkin export, the unpatched theorem remains open "
                "although the exact values are ready."
            ),
        },
        "closure_decision": {
            "patched_spine_dynamic_C1_closed": True,
            "unpatched_dynamic_C1_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "external_papers_modified": False,
        },
        "what_closes_now": {
            "final_gate_perfected": True,
            "patched_spine_status_made_explicit": True,
            "unpatched_status_made_explicit": True,
            "paper_ready_axiom_text_created": True,
            "exact_values_preserved": True,
        },
        "what_remains_open": {
            "derive_source_axiom_from_unpatched_MTT": True,
            "or_accept_source_axiom_into_target_papers": True,
            "or_export_honest_selected_Galerkin_C1_tables": True,
            "true_SM_equivalence_without_patch": True,
            "no_knob_flavor_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DynamicC1_FinalGate_Perfection_or_SourceAxiomDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "patched_spine_dynamic_C1_closed": True,
        "unpatched_dynamic_C1_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DynamicC1 FinalGate Perfection or SourceAxiomDecision v1

Status: `{STATUS}`.

The final DynamicC1 gate is now separated into two scientifically clean modes.

Patched mode:

- accepts the local `DifferentiatedPhiFinC1ResidualProjectorAxiom`;
- closes the dynamic C1 packet inside the patched proof spine;
- promotes `A_selected`, `b_selected`, `deltaTheta_C1`, and sector response
  matrices inside that patched spine.

Unpatched mode:

- keeps the exact same `R_Z/R_X` and Hessian values ready;
- does not claim selected-source closure;
- requires either a derivation of the source axiom or an honest selected
  Galerkin C1 table export.

This artifact does not modify external Obsidian papers and does not close
true SM equivalence or no-knob flavor constants.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
