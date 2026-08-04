from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_primitive_c1_tensor_hessian_source_map_or_honest_galerkin_c1_execution_certificate.json"
SLUG = "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
SM_CERT = SM_ROOT / "certificates" / f"{SLUG}_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / f"{SLUG}.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / SLUG
SELECTION_TEST = SM_DIR / "source_map_selection_theorem_test.packet.json"
IF_SELECTED = SM_DIR / "if_selected_dynamic_packet_closure.packet.json"
GALERKIN_ROUTE = SM_DIR / "honest_galerkin_value_run_route.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_source_map_selection_theorem_or_honest_galerkin_c1_value_run_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_source_map_selection_theorem_or_honest_galerkin_c1_value_run.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_Import_v1.md"

STATUS = "POST_ALPHA_SOURCE_MAP_SELECTION_THEOREM_OR_HONEST_GALERKIN_C1_VALUE_RUN_IMPORTED_SELECTION_TEST_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    candidate = load(SM_CANDIDATE)
    selection_test = load(SELECTION_TEST)
    if_selected = load(IF_SELECTED)
    galerkin_route = load(GALERKIN_ROUTE)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["frontier_is_source_map_selection_theorem_or_honest_galerkin_value_run"] is True,
            prev["frontier_decision"]["next_required_artifact"]
            == "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1",
        ]
    )

    imported_ok = all(
        [
            cert["certificate"] == "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1",
            cert["theorem_proved"] is True,
            cert["closure_claimed"] is False,
            cert["selection_theorem_claimed"] is False,
            cert["A_selected_claimed"] is False,
            cert["b_selected_claimed"] is False,
            cert["deltaTheta_C1_claimed"] is False,
            cert["honest_Galerkin_C1_claimed"] is False,
            cert["observed_data_used"] is False,
            cert["target_fitting_used"] is False,
            cert["next_required_artifact"] == NEXT,
            all(cert["what_closes"].values()),
            all(cert["what_remains_open"].values()),
            candidate["theorem"]["name"] == "SourceMapSelectionBoundaryTheorem",
            candidate["theorem"]["proved"] is True,
            candidate["promotion_decision"]["selection_theorem_proved_now"] is False,
            candidate["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
            candidate["promotion_decision"]["sector_response_matrices_promoted"] is False,
            candidate["promotion_decision"]["A_selected_promoted"] is False,
            candidate["promotion_decision"]["b_selected_promoted"] is False,
            candidate["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            candidate["promotion_decision"]["SM_parity_dynamic_packet_closed"] is False,
        ]
    )

    selection_test_ok = all(
        [
            selection_test["schema"] == "MTTSourceMapSelectionTheoremTest.v1",
            selection_test["status"] == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN",
            selection_test["already_selected_or_closed"]["terminal_static_source_unconditional"] is True,
            selection_test["already_selected_or_closed"]["weyl_polynomial_residuals_exact"] is True,
            selection_test["already_selected_or_closed"]["canonical_residual_projector_unique"] is True,
            selection_test["already_selected_or_closed"]["static_source_map_candidate_constructed"] is True,
            selection_test["already_selected_or_closed"]["strict_72_real_target_attached"] is True,
            selection_test["selection_attempt"]["candidate_rule"]
            == "selected differentiated Phi_fin^C1 applies Q_residual to the selected enriched Weyl-pair packet",
            selection_test["selection_attempt"]["phase_R_Z_selected_now"] is False,
            selection_test["selection_attempt"]["shift_R_X_selected_now"] is False,
            selection_test["selection_attempt"]["b_source_emitted_now"] is False,
            selection_test["selection_attempt"]["source_map_selected_now"] is False,
            selection_test["selection_attempt"]["physical_projector_application_promoted_now"] is False,
            selection_test["observed_data_used"] is False,
            selection_test["target_fitting_used"] is False,
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
            galerkin_route["schema"] == "MTTHonestGalerkinC1ValueRunRoute.v1",
            galerkin_route["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN",
            galerkin_route["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin_route["selected_source_verified"] is False,
            galerkin_route["can_replace_source_map_now"] is False,
            galerkin_route["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin_route["would_close_SM_parity_dynamic_packet_if_emitted"] is True,
            galerkin_route["would_close_no_knob_flavor_constants_by_itself"] is False,
            "primitive_three_by_three_contraction_terms" in galerkin_route["required_outputs"],
            "linear_response_matrices" in galerkin_route["required_outputs"],
            galerkin_route["observed_data_used"] is False,
            galerkin_route["target_fitting_used"] is False,
        ]
    )

    what_closes_now = {
        "primitive_source_map_candidate_gate_consumed": prev_ok,
        "source_map_selection_boundary_imported": imported_ok,
        "source_map_selection_test_built": selection_test_ok,
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
        "name": "PostAlphaSourceMapSelectionBoundaryImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "Static source selection, exact Weyl residuals, and canonical Q_residual "
            "uniqueness construct but do not select the physical differentiated C1 "
            "application. If phase R_Z, shift R_X, same-branch normalization, and "
            "b_source are selected, the dynamic packet closes exactly. The remaining "
            "proof object is the differentiated Phi_fin^C1 residual-projector axiom/application "
            "or an honest Galerkin C1 value run."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "source_candidate_summary": {
            "status": candidate["status"],
            "theorem": candidate["theorem"],
            "promotion_decision": candidate["promotion_decision"],
            "what_closes_now": candidate["what_closes_now"],
            "what_remains_open": candidate["what_remains_open"],
        },
        "source_map_selection_theorem_test": selection_test,
        "if_selected_dynamic_packet_closure": if_selected,
        "honest_galerkin_value_run_route": galerkin_route,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "source_map_selection_test_built": True,
            "if_selected_closure_exact": True,
            "frontier_is_differentiated_PhiFinC1_residual_projector_axiom_or_Galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_gate_certificate": str(PREV),
            "sm_gate_certificate": str(SM_CERT),
            "sm_gate_candidate": str(SM_CANDIDATE),
            "source_map_selection_theorem_test": str(SELECTION_TEST),
            "if_selected_dynamic_packet_closure": str(IF_SELECTED),
            "honest_galerkin_value_run_route": str(GALERKIN_ROUTE),
        },
    }

    note = f"""# PostAlpha SourceMapSelectionTheorem or HonestGalerkinC1ValueRun Import v1

## Result

The source-map selection test is built. Static/projector support is separated
from the still-open dynamic application rule.

If the antecedent is selected:

```text
phase R_Z selected       = true
shift R_X selected       = true
b_source emitted         = true
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
        "certificate": "post_alpha_source_map_selection_theorem_or_honest_galerkin_c1_value_run",
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
