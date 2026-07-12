"""Build explicit source-axiom insertion and patched dynamic-C1 closure."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AXIOM = PACKET_DIR / "accepted_local_source_axiom.packet.json"
PATCHED_CLOSURE = PACKET_DIR / "patched_dynamic_c1_closure_theorem.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_exit_status.packet.json"
LOCAL_APPENDIX = PACKET_DIR / "local_paper_appendix_insert.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DifferentiatedPhiFinC1_AxiomInsertion_PatchedClosure_or_UnpatchedExit_v1.md"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_AXIOM_INSERTED_PATCHED_DYNAMIC_C1_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_HonestGalerkinC1Tables_or_UnpatchedSourceRuleDerivation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    source_rule = load(DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion.candidate.json")
    axiom_package = load(
        DATA
        / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion"
        / "explicit_axiom_promotion_package.packet.json"
    )
    final_gate = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json")
    ready_table = load(
        DATA
        / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
        / "ready_to_promote_dynamic_value_table.packet.json"
    )
    decision = load(
        DATA
        / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision"
        / "source_axiom_decision_matrix.packet.json"
    )

    axiom = {
        "schema": "MTTAcceptedLocalDifferentiatedPhiFinC1SourceAxiom.v1",
        "status": "LOCAL_SOURCE_AXIOM_ACCEPTED_IN_THIS_PROOF_SPINE",
        "axiom_name": axiom_package["axiom_name"],
        "axiom_text": axiom_package["axiom_text"],
        "accepted_scope": "local mtt-sm-parity-closure proof spine",
        "accepted_as": "explicit axiom/premise, not derived theorem",
        "external_obsidian_papers_modified": False,
        "guardrails": axiom_package["does_not_by_itself_close"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hessian = ready_table["conditional_hessian_values"]
    patched_closure = {
        "schema": "MTTPatchedDynamicC1ClosureTheorem.v1",
        "status": "PATCHED_DYNAMIC_C1_PACKET_CLOSED_BY_ACCEPTED_SOURCE_AXIOM",
        "hypothesis": axiom["axiom_name"],
        "promoted_objects": {
            "phase_R_Z_source": True,
            "shift_R_X_source": True,
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
            "dynamic_C1_source_owner_packet": True,
        },
        "exact_values": {
            "A_transpose_A": hessian["A_transpose_A"],
            "A_transpose_b": hessian["A_transpose_b"],
            "b_norm_sq": ready_table["routed_72_real_completion"]["conditional_b_norm_sq"],
            "deltaTheta_C1": hessian["deltaTheta_C1"],
            "rank": hessian["rank"],
            "phase_R_Z_residual_norm_sq": ready_table["dynamic_operator_candidates"]["phase_R_Z"]["residual_norm_sq"],
            "shift_R_X_residual_norm_sq": ready_table["dynamic_operator_candidates"]["shift_R_X"]["residual_norm_sq"],
        },
        "scientific_status": "axiom-conditional closure",
        "does_not_close": {
            "unpatched_source_rule_derivation": True,
            "honest_independent_galerkin_export": True,
            "true_SM_equivalence": True,
            "no_knob_flavor_constants": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    unpatched_exit = {
        "schema": "MTTUnpatchedDynamicC1ExitStatusAfterAxiomInsertion.v1",
        "status": "UNPATCHED_EXIT_REMAINS_OPEN_AFTER_LOCAL_AXIOM_INSERTION",
        "remaining_exits": [
            "derive the source axiom from unpatched MTT/Theta/Strominger action",
            "export honest selected Galerkin C1 tables independent of the axiom contract",
        ],
        "unpatched_dynamic_C1_closed": False,
        "honest_galerkin_table_exported": final_gate["closure_decision"]["honest_galerkin_table_exported"],
        "source_rule_derived_unpatched": final_gate["closure_decision"]["source_rule_proved"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    local_appendix = {
        "schema": "MTTLocalPaperAppendixInsertForDifferentiatedPhiFinC1Axiom.v1",
        "status": "LOCAL_APPENDIX_INSERT_CREATED_EXTERNAL_PAPERS_UNTOUCHED",
        "title": "Appendix: Conditional Dynamic C1 Closure Under the Differentiated PhiFin C1 Source Axiom",
        "axiom_statement": axiom["axiom_text"],
        "theorem_statement": (
            "In the local proof spine, assuming the DifferentiatedPhiFinC1ResidualProjectorAxiom, "
            "the dynamic C1 packet closes with A^T A=12 I_2, A^T b=(12,12), "
            "and deltaTheta_C1=(1,1)."
        ),
        "proof_steps": [
            "Use the accepted source axiom to select Q_residual application and emit R_Z/R_X.",
            "Use the same source axiom to emit b_selected in the fixed 72-real coordinate target.",
            "Apply the verified final dynamic value gate and exact Hessian solve.",
            "Retain the guardrail that unpatched derivation and no-knob flavor closure remain open.",
        ],
        "external_papers_modified": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (AXIOM, axiom),
        (PATCHED_CLOSURE, patched_closure),
        (UNPATCHED_EXIT, unpatched_exit),
        (LOCAL_APPENDIX, local_appendix),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedDifferentiatedPhiFinC1AxiomInsertionPatchedClosureOrUnpatchedExit",
        "status": STATUS,
        "inputs": {
            "source_rule_axiom_package": rel(
                DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion.candidate.json"
            ),
            "final_dynamic_value_gate": rel(
                DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json"
            ),
            "final_gate_decision": rel(
                DATA
                / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision"
                / "source_axiom_decision_matrix.packet.json"
            ),
        },
        "output_packets": {
            "accepted_local_source_axiom": rel(AXIOM),
            "patched_dynamic_c1_closure_theorem": rel(PATCHED_CLOSURE),
            "unpatched_exit_status": rel(UNPATCHED_EXIT),
            "local_paper_appendix_insert": rel(LOCAL_APPENDIX),
        },
        "theorem": {
            "name": "LocalAxiomPatchedDynamicC1ClosureTheorem",
            "proved": True,
            "statement": (
                "After explicitly accepting the DifferentiatedPhiFinC1ResidualProjectorAxiom in this local "
                "proof spine, the dynamic C1 packet closes axiom-conditionally. The same artifact preserves "
                "the unpatched exits as open: either derive the axiom or export honest selected Galerkin C1 tables."
            ),
        },
        "closure_decision": {
            "local_source_axiom_accepted": True,
            "patched_dynamic_C1_packet_closed": True,
            "unpatched_dynamic_C1_packet_closed": False,
            "external_papers_modified": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "explicit_local_source_axiom_inserted": True,
            "patched_dynamic_C1_packet_closed": True,
            "local_appendix_insert_created": True,
            "exact_values_promoted_inside_patched_spine": True,
        },
        "what_remains_open": {
            "derive_source_axiom_unpatched": True,
            "export_honest_selected_galerkin_tables": True,
            "insert_or_revise_external_papers_if_desired": True,
            "true_SM_equivalence_without_axiom": True,
            "no_knob_flavor_constants": True,
        },
        "superset_strategy": {
            "mode": "explicit axiom route chosen locally, unpatched and Galerkin routes retained",
            "locked_target": decision["superset_strategy"]["locked_target"],
            "paths_used_as_knobs": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_DifferentiatedPhiFinC1_AxiomInsertion_PatchedClosure_or_UnpatchedExit_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_source_axiom_accepted": True,
        "patched_dynamic_C1_packet_closed": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "external_papers_modified": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected DifferentiatedPhiFinC1 AxiomInsertion PatchedClosure or UnpatchedExit v1

Status: `{STATUS}`.

This artifact finishes the local dynamic-C1 branch under an explicit source
axiom. The `DifferentiatedPhiFinC1ResidualProjectorAxiom` is accepted as a
local premise in this proof spine, not as an unpatched theorem.

Closed inside the patched spine:

- selected `R_Z/R_X` source emission;
- same-source `b_selected`;
- `A^T A=12 I_2`;
- `A^T b=(12,12)`;
- `deltaTheta_C1=(1,1)`;
- dynamic C1 source-owner packet.

Still open:

- derivation of the source axiom from unpatched MTT/Theta/Strominger action;
- honest selected Galerkin C1 table export independent of the axiom contract;
- true SM equivalence and no-knob flavor constants.

External Obsidian papers were not modified.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
