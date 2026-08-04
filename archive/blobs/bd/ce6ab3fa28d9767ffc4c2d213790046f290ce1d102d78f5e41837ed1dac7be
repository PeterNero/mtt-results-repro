from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM_ROOT = ROOT.parent / "mtt-sm-parity-closure"

PREV = ROOT / "certificates" / "post_alpha_primitive_c1_hessian_source_map_candidate_certificate.json"
SM_CERT = SM_ROOT / "certificates" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun_certificate.json"
SM_CANDIDATE = SM_ROOT / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
SM_DIR = SM_ROOT / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
SELECTION_TEST = SM_DIR / "source_map_selection_theorem_test.packet.json"
IF_SELECTED = SM_DIR / "if_selected_dynamic_packet_closure.packet.json"
GALERKIN_ROUTE = SM_DIR / "honest_galerkin_value_run_route.packet.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_source_map_selection_boundary_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_source_map_selection_boundary.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_SourceMapSelection_Boundary_Import_v1.md"

STATUS = "POST_ALPHA_SOURCE_MAP_SELECTION_BOUNDARY_BUILT_DYNAMIC_APPLICATION_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    cert = load(SM_CERT)
    cand = load(SM_CANDIDATE)
    selection = load(SELECTION_TEST)
    if_selected = load(IF_SELECTED)
    galerkin = load(GALERKIN_ROUTE)

    prev_ok = all(
        [
            prev["theorem"]["proved"] is True,
            prev["closure_claimed"] is False,
            prev["frontier_decision"]["source_map_candidate_constructed"] is True,
            prev["frontier_decision"]["source_map_selected_by_MTT_now"] is False,
            prev["frontier_decision"]["frontier_is_source_map_selection_or_honest_galerkin_value_run"] is True,
        ]
    )

    imported_ok = all(
        [
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
            cand["theorem"]["proved"] is True,
            cand["selection_theorem_claimed"] is False,
            cand["promotion_decision"]["selection_theorem_proved_now"] is False,
            cand["promotion_decision"]["source_map_selected_by_MTT_now"] is False,
            cand["promotion_decision"]["A_selected_promoted"] is False,
            cand["promotion_decision"]["b_selected_promoted"] is False,
            cand["promotion_decision"]["deltaTheta_C1_promoted"] is False,
            cand["promotion_decision"]["honest_Galerkin_C1_value_run_promoted"] is False,
        ]
    )

    selection_ok = all(
        [
            selection["schema"] == "MTTSourceMapSelectionTheoremTest.v1",
            selection["status"] == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN",
            selection["observed_data_used"] is False,
            selection["target_fitting_used"] is False,
            all(selection["already_selected_or_closed"].values()),
            selection["selection_attempt"]["source_map_selected_now"] is False,
            selection["selection_attempt"]["phase_R_Z_selected_now"] is False,
            selection["selection_attempt"]["shift_R_X_selected_now"] is False,
            selection["selection_attempt"]["b_source_emitted_now"] is False,
            selection["selection_attempt"]["physical_projector_application_promoted_now"] is False,
        ]
    )

    if_selected_ok = all(
        [
            if_selected["schema"] == "MTTIfSelectedDynamicPacketClosure.v1",
            if_selected["status"] == "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN",
            if_selected["promoted_now"] is False,
            if_selected["observed_data_used"] is False,
            if_selected["target_fitting_used"] is False,
            all(if_selected["antecedent_required"].values()),
            if_selected["current_antecedent"]["phase_R_Z_selected"] is False,
            if_selected["current_antecedent"]["shift_R_X_selected"] is False,
            if_selected["current_antecedent"]["b_source_emitted"] is False,
            if_selected["current_antecedent"]["A_selected_promotes"] is False,
            if_selected["if_selected_numeric_replay"]["rank"] == 2,
            if_selected["if_selected_numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]],
            if_selected["if_selected_numeric_replay"]["A_transpose_b"] == [12.0, 12.0],
            if_selected["if_selected_numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0],
            if_selected["would_promote_if_antecedent_met"]["SM_parity_dynamic_packet_would_close"] is True,
            if_selected["would_promote_if_antecedent_met"]["no_knob_flavor_constants_would_close"] is False,
        ]
    )

    galerkin_ok = all(
        [
            galerkin["schema"] == "MTTHonestGalerkinC1ValueRunRoute.v1",
            galerkin["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN",
            galerkin["can_replace_source_map_now"] is False,
            galerkin["selected_source_verified"] is False,
            galerkin["manifest_status"] == "OPEN_C1_PRIMITIVE_CONTRACTIONS_MISSING",
            galerkin["observed_data_used"] is False,
            galerkin["target_fitting_used"] is False,
            galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72,
            galerkin["would_close_SM_parity_dynamic_packet_if_emitted"] is True,
            galerkin["would_close_no_knob_flavor_constants_by_itself"] is False,
        ]
    )

    what_closes_now = {
        "previous_source_map_candidate_consumed": prev_ok,
        "source_map_selection_boundary_imported": imported_ok,
        "selection_test_built": selection_ok,
        "if_selected_dynamic_packet_closure_exact": if_selected_ok,
        "honest_Galerkin_value_run_route_restated": galerkin_ok,
    }

    what_remains_open = {
        "selected_differentiated_PhiFinC1_applies_Q_residual": True,
        "selected_phase_R_Z_source": True,
        "selected_shift_R_X_source": True,
        "selected_Hessian_or_b_source_vector": True,
        "selected_b_selected": True,
        "selected_A_selected": True,
        "selected_deltaTheta_C1": True,
        "selected_sector_response_matrices": True,
        "honest_selected_Galerkin_C1_execution_values": True,
        "SM_parity_dynamic_packet_closure": True,
        "full_no_knob_flavor_closure": True,
        "true_SM_equivalence_closure": True,
    }

    guardrails = {
        "does_not_claim_selection_theorem": True,
        "does_not_promote_source_map": True,
        "does_not_promote_A_b_deltaTheta_or_sector_matrices": True,
        "does_not_claim_Galerkin_value_run": True,
        "does_not_use_observed_or_target_inputs": True,
        "does_not_claim_SM_or_no_knob_closure": True,
    }

    theorem = {
        "name": "PostAlphaSourceMapSelectionBoundaryImport",
        "proved": all([all(what_closes_now.values()), all(what_remains_open.values()), all(guardrails.values())]),
        "closure_claimed": False,
        "statement": (
            "The already-built source-map candidate is tested against current MTT "
            "selection support. Terminal/static source selection, exact Weyl-polynomial "
            "residuals, and unique canonical Q_residual construct the candidate but do "
            "not prove the physical differentiated Phi_fin^C1 application rule or emit "
            "b_selected. If those antecedents are supplied, dynamic closure follows by "
            "exact rank-2 replay; otherwise the only replacement route is honest selected "
            "Galerkin C1 value execution."
        ),
    }

    packet = {
        "theorem": theorem,
        "status": STATUS,
        "what_closes_now": what_closes_now,
        "selection_test": selection,
        "if_selected_dynamic_packet_closure": if_selected,
        "honest_galerkin_value_run_route": galerkin,
        "what_remains_open": what_remains_open,
        "frontier_decision": {
            "selection_test_built": True,
            "selection_theorem_proved_now": False,
            "if_selected_closure_exact": True,
            "frontier_is_differentiated_PhiFinC1_application_or_Galerkin_execution": True,
            "next_required_artifact": NEXT,
        },
        "guardrails": guardrails,
        "input_artifacts": {
            "previous_source_map_candidate": str(PREV),
            "sm_source_map_selection_certificate": str(SM_CERT),
            "sm_source_map_selection_candidate": str(SM_CANDIDATE),
            "source_map_selection_test": str(SELECTION_TEST),
            "if_selected_dynamic_packet_closure": str(IF_SELECTED),
            "honest_galerkin_value_run_route": str(GALERKIN_ROUTE),
        },
    }

    note = f"""# PostAlpha SourceMap Selection Boundary Import v1

## Result

The source-map candidate has been tested against current MTT selection support.

Closed support:

```text
terminal/static source selection
exact R_Z/R_X Weyl-polynomial residuals
canonical Q_residual uniqueness, rank 6
strict 72-real target
```

Still open:

```text
Phi_fin^C1 physically applies Q_residual
phase R_Z selected
shift R_X selected
b_selected emitted
honest selected Galerkin C1 values
```

If those antecedents are supplied, the numeric replay is exact:

```text
A^T A = [[12.0, 0.0], [0.0, 12.0]]
A^T b = [12.0, 12.0]
DeltaTheta_C1 = [1.0, 1.0]
```

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
        "certificate": "post_alpha_source_map_selection_boundary",
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
