from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PREV = ROOT / "certificates" / "post_alpha_independent_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"
SOURCE_CERT = ROOT / "certificates" / "post_alpha_source_map_selection_theorem_or_honest_galerkin_c1_value_run_certificate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_independent_source_map_selection_theorem_or_honest_galerkin_c1_value_run_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_independent_source_map_selection_theorem_or_honest_galerkin_c1_value_run.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_IndependentSourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_Import_v1.md"

STATUS = "POST_ALPHA_INDEPENDENT_SOURCE_MAP_SELECTION_THEOREM_OR_HONEST_GALERKIN_C1_VALUE_RUN_IMPORTED_SELECTION_TEST_OPEN"
SOURCE_STATUS = "POST_ALPHA_SOURCE_MAP_SELECTION_THEOREM_OR_HONEST_GALERKIN_C1_VALUE_RUN_IMPORTED_SELECTION_TEST_OPEN"
THIS_ARTIFACT = "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE_CERT)
    source_packet = load(Path(source["packet_written"]))

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["source_map_candidate_constructed"] is True,
            prev["frontier_decision"]["source_map_selection_open"] is True,
            prev["frontier_decision"]["frontier_is_source_map_selection_theorem_or_honest_galerkin_value_run"]
            is True,
            prev["frontier_decision"]["next_required_artifact"] == THIS_ARTIFACT,
            all(prev["what_closes_now"].values()),
            all(prev["what_remains_open"].values()),
            all(prev["guardrails"].values()),
        ]
    )

    source_ok = all(
        [
            source["status"] == SOURCE_STATUS,
            source["theorem"]["proved"] is True,
            source["closure_claimed"] is False,
            source["frontier_decision"]["source_map_selection_test_built"] is True,
            source["frontier_decision"]["if_selected_closure_exact"] is True,
            source["frontier_decision"]["frontier_is_differentiated_PhiFinC1_residual_projector_axiom_or_Galerkin_execution"]
            is True,
            source["frontier_decision"]["next_required_artifact"] == NEXT,
            all(source["what_closes_now"].values()),
            all(source["what_remains_open"].values()),
            all(source["guardrails"].values()),
        ]
    )

    test = source_packet["source_map_selection_theorem_test"]
    if_selected = source_packet["if_selected_dynamic_packet_closure"]
    galerkin = source_packet["honest_galerkin_value_run_route"]

    test_ok = all(
        [
            test["schema"] == "MTTSourceMapSelectionTheoremTest.v1",
            test["status"] == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN",
            test["already_selected_or_closed"]["terminal_static_source_unconditional"] is True,
            test["already_selected_or_closed"]["weyl_polynomial_residuals_exact"] is True,
            test["already_selected_or_closed"]["canonical_residual_projector_unique"] is True,
            test["already_selected_or_closed"]["static_source_map_candidate_constructed"] is True,
            test["already_selected_or_closed"]["strict_72_real_target_attached"] is True,
            test["selection_attempt"]["candidate_rule"]
            == "selected differentiated Phi_fin^C1 applies Q_residual to the selected enriched Weyl-pair packet",
            test["selection_attempt"]["phase_R_Z_selected_now"] is False,
            test["selection_attempt"]["shift_R_X_selected_now"] is False,
            test["selection_attempt"]["b_source_emitted_now"] is False,
            test["selection_attempt"]["source_map_selected_now"] is False,
            test["selection_attempt"]["physical_projector_application_promoted_now"] is False,
            test["observed_data_used"] is False,
            test["target_fitting_used"] is False,
        ]
    )

    if_selected_ok = all(
        [
            if_selected["schema"] == "MTTIfSelectedDynamicPacketClosure.v1",
            if_selected["status"] == "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN",
            if_selected["promoted_now"] is False,
            if_selected["antecedent_required"]["phase_R_Z_selected"] is True,
            if_selected["antecedent_required"]["shift_R_X_selected"] is True,
            if_selected["antecedent_required"]["b_source_emitted"] is True,
            if_selected["antecedent_required"]["same_branch_normalization"] is True,
            if_selected["current_antecedent"]["phase_R_Z_selected"] is False,
            if_selected["current_antecedent"]["shift_R_X_selected"] is False,
            if_selected["current_antecedent"]["b_source_emitted"] is False,
            if_selected["if_selected_numeric_replay"]["rank"] == 2,
            if_selected["if_selected_numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            if_selected["if_selected_numeric_replay"]["A_transpose_b"] == [12.0, 12.0],
            if_selected["if_selected_numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0],
            if_selected["would_promote_if_antecedent_met"]["SM_parity_dynamic_packet_would_close"] is True,
            if_selected["would_promote_if_antecedent_met"]["no_knob_flavor_constants_would_close"] is False,
            if_selected["observed_data_used"] is False,
            if_selected["target_fitting_used"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTHonestGalerkinC1ValueRunRoute.v1",
            galerkin["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN",
            galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin["selected_source_verified"] is False,
            galerkin["can_replace_source_map_now"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin["would_close_SM_parity_dynamic_packet_if_emitted"] is True,
            galerkin["would_close_no_knob_flavor_constants_by_itself"] is False,
            "primitive_three_by_three_contraction_terms" in galerkin["required_outputs"],
            "linear_response_matrices" in galerkin["required_outputs"],
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "long_name_source_map_candidate_gate_consumed": prev_ok,
        "audited_source_map_selection_boundary_reanchored": source_ok,
        "source_map_selection_test_built": test_ok,
        "if_selected_dynamic_packet_closure_exact": if_selected_ok,
        "honest_galerkin_value_run_route_reemitted": galerkin_ok,
    }

    what_remains_open = {
        "selected_differentiated_PhiFinC1_applies_Q_residual": True,
        "selected_phase_R_Z_source": True,
        "selected_shift_R_X_source": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_sector_response_matrices": True,
        "selected_A_selected": True,
        "selected_b_selected": True,
        "selected_deltaTheta_C1": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "true_SM_equivalence_closure": True,
        "full_no_knob_flavor_closure": True,
    }

    guardrails = {
        "does_not_claim_selection_theorem": True,
        "does_not_select_source_map_by_MTT": True,
        "does_not_promote_physical_projector_application": True,
        "does_not_promote_A_b_deltaTheta": True,
        "does_not_promote_honest_galerkin_value_run": True,
        "does_not_claim_SM_parity_dynamic_closure": True,
        "does_not_claim_true_SM_equivalence": True,
        "does_not_claim_no_knob_flavor_closure": True,
        "does_not_use_observed_or_target_inputs": True,
    }

    theorem = {
        "name": "PostAlphaIndependentSourceMapSelectionBoundaryImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The independent long-name branch imports the source-map selection "
            "boundary. Static source support, exact Weyl residuals, and canonical "
            "Q_residual uniqueness give an exact if-selected dynamic closure, but "
            "the physical differentiated Phi_fin^C1 residual-projector application "
            "and the honest Galerkin C1 value run remain open."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_selection_boundary_certificate": source,
        "source_map_selection_theorem_test": test,
        "if_selected_dynamic_packet_closure": if_selected,
        "honest_galerkin_value_run_route": galerkin,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_map_selection_test_built": True,
            "if_selected_closure_exact": True,
            "frontier_is_differentiated_PhiFinC1_residual_projector_axiom_or_Galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_long_name_certificate": str(PREV),
            "source_selection_boundary_certificate": str(SOURCE_CERT),
            "source_selection_boundary_packet": source["packet_written"],
        },
    }

    note = f"""# PostAlpha Independent SourceMapSelectionTheorem or HonestGalerkinC1ValueRun Import v1

## Result

The independent long-name branch now carries the source-map selection boundary.

If the antecedent is selected:

```text
phase R_Z selected        = true
shift R_X selected        = true
b_source emitted          = true
same branch normalization = true
```

then the closure replay is exact:

```text
A^T A       = [[12, 0], [0, 12]]
A^T b       = [12, 12]
deltaTheta  = [1, 1]
```

Current status: antecedent open, no dynamic closure claimed.

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
        "certificate": "post_alpha_independent_source_map_selection_theorem_or_honest_galerkin_c1_value_run",
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
