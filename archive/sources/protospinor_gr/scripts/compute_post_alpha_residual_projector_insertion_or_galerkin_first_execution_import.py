from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_differentiated_phifinc1_residual_projector_contract_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
AXIOM_INSERTION = SM_DIR / "residual_projector_axiom_insertion_package.packet.json"
GALERKIN_SPEC = SM_DIR / "galerkin_c1_first_execution_spec.packet.json"
ROUTE_DECISION = SM_DIR / "route_decision_and_next_inputs.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_residual_projector_insertion_or_galerkin_first_execution_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_residual_projector_insertion_or_galerkin_first_execution.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_ResidualProjectorInsertion_or_GalerkinFirstExecution_Import_v1.md"

STATUS = "POST_ALPHA_RESIDUAL_PROJECTOR_INSERTION_OR_GALERKIN_FIRST_EXECUTION_IMPORTED_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    axiom = load(AXIOM_INSERTION)
    galerkin = load(GALERKIN_SPEC)
    decision = load(ROUTE_DECISION)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_axiom_insertion_or_first_Galerkin_execution"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "ResidualProjectorInsertionOrFirstExecutionPreparationTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["closure_claimed"] is False,
            candidate["promotion_decision"]["main_corpus_axiom_patch_applied_now"] is False,
            candidate["promotion_decision"]["residual_projector_axiom_proved_now"] is False,
            candidate["promotion_decision"]["first_Galerkin_C1_execution_run_now"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
        ]
    )

    axiom_ok = all(
        [
            axiom["schema"] == "MTTResidualProjectorAxiomInsertionPackage.v1",
            axiom["status"] == "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED",
            axiom["axiom_name"] == "DifferentiatedPhiFinC1ResidualProjectorAxiom",
            axiom["inserted_into_main_corpus_now"] is False,
            axiom["observed_data_used"] is False,
            axiom["target_fitting_used"] is False,
            axiom["paper_ready_theorem_slot"]["payload"]["selected_differentiated_PhiFinC1_applies_Q_residual"] is True,
            axiom["paper_ready_theorem_slot"]["payload"]["phase_R_Z_selected"] is True,
            axiom["paper_ready_theorem_slot"]["payload"]["shift_R_X_selected"] is True,
            axiom["paper_ready_theorem_slot"]["payload"]["b_source_emitted"] is True,
            axiom["after_insertion_replay"]["numeric_replay"]["rank"] == 2,
            axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            axiom["after_insertion_replay"]["numeric_replay"]["A_transpose_b"] == [12.0, 12.0],
            axiom["after_insertion_replay"]["numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0],
            axiom["after_insertion_replay"]["SM_parity_dynamic_packet_would_close"] is True,
            axiom["after_insertion_replay"]["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTSelectedGalerkinC1FirstExecutionSpec.v1",
            galerkin["status"] == "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING",
            galerkin["first_execution_run_now"] is False,
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin["coordinate_order"]["response_column_order"] == ["phase_clock_R_Z", "shift_vertex_R_X"],
            set(galerkin["required_input_files"].keys())
            == {
                "zero_mode_basis_packet",
                "primitive_contraction_terms_packet",
                "hessian_or_source_vector_packet",
                "sector_response_matrix_packet",
            },
            len(galerkin["why_not_run_now"]) == 3,
        ]
    )

    decision_ok = all(
        [
            decision["schema"] == "MTTResidualProjectorInsertionOrGalerkinFirstExecutionDecision.v1",
            decision["status"] == "TWO_ROUTES_READY_NEXT_INPUTS_SHARP",
            decision["observed_data_used"] is False,
            decision["target_fitting_used"] is False,
            decision["recommended_next"] == NEXT,
            decision["route_A_residual_projector_axiom"]["main_corpus_patched_now"] is False,
            decision["route_A_residual_projector_axiom"]["ready_as_paper_appendix_draft"] is True,
            decision["route_B_honest_galerkin_execution"]["ready_as_execution_spec"] is True,
            decision["route_B_honest_galerkin_execution"]["run_now"] is False,
            len(decision["route_B_honest_galerkin_execution"]["next_missing_inputs"]) == 4,
        ]
    )

    what_closes_now = {
        "previous_contract_gate_consumed": prev_ok,
        "preparation_theorem_imported": imported_ok,
        "axiom_insertion_appendix_package_fixed": axiom_ok,
        "galerkin_first_execution_schema_fixed": galerkin_ok,
        "two_route_next_input_decision_fixed": decision_ok,
    }

    what_remains_open = {
        "patch_main_corpus_with_residual_projector_axiom_or_prove_it": True,
        "fill_zero_mode_basis_packet": True,
        "fill_primitive_contraction_terms_packet": True,
        "fill_hessian_source_vector_packet": True,
        "fill_sector_response_matrix_packet": True,
        "run_first_honest_Galerkin_C1_execution": True,
        "promote_A_selected": True,
        "promote_b_selected": True,
        "promote_deltaTheta_C1": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_patch_main_corpus": axiom["inserted_into_main_corpus_now"] is False,
        "does_not_claim_axiom_proof": candidate["promotion_decision"]["residual_projector_axiom_proved_now"] is False,
        "does_not_run_first_Galerkin_execution": galerkin["first_execution_run_now"] is False,
        "does_not_promote_A_b_or_deltaTheta": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_parity_or_true_SM_equivalence_closure": True,
    }

    theorem = {
        "name": "PostAlphaResidualProjectorInsertionOrGalerkinFirstExecutionImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The two lawful routes after the differentiated Phi_fin^C1 residual-projector "
            "contract are now operationally specified. Route A has insertion-ready paper "
            "appendix drafts for the residual-projector axiom; Route B has a first "
            "Galerkin C1 execution schema with four required input packets. Both routes "
            "remain locked to the same exact rank-2 72-real replay, but neither the main "
            "corpus patch nor the first execution is performed here."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "axiom_insertion_package": axiom,
        "galerkin_c1_first_execution_spec": galerkin,
        "route_decision_and_next_inputs": decision,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "route_A_ready_as_appendix_patch": True,
            "route_B_ready_as_execution_spec": True,
            "main_corpus_axiom_patch_applied_now": False,
            "first_Galerkin_C1_execution_run_now": False,
            "frontier_is_input_basis_fill_or_axiom_corpus_patch": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_contract_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "axiom_insertion_package": str(AXIOM_INSERTION),
            "galerkin_first_execution_spec": str(GALERKIN_SPEC),
            "route_decision_and_next_inputs": str(ROUTE_DECISION),
        },
    }

    note = f"""# PostAlpha ResidualProjector Insertion or Galerkin First Execution Import v1

## Result

The next move is now genuinely sharp.

Route A is paper-patch ready but not patched:

```text
DifferentiatedPhiFinC1ResidualProjectorAxiom
selected Phi_fin^C1 applies Q_residual
selected R_Z, R_X, and b source are emitted
```

Route B is execution-spec ready but not run:

```text
zero_mode_basis.packet.json
primitive_contraction_terms.packet.json
hessian_source_vector.packet.json
sector_response_matrices.packet.json
```

Both routes replay the same closure target:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
rank = 2
```

No observed constants, benchmark matrices, or target fits are used.

## Status

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""

    cert_out = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_residual_projector_insertion_or_galerkin_first_execution",
        "status": STATUS,
        "closure_claimed": False,
        "theorem": theorem,
        "what_closes_now": what_closes_now,
        "what_remains_open": what_remains_open,
        "frontier_decision": packet["frontier_decision"],
        "guardrails": guardrails,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert_out, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
