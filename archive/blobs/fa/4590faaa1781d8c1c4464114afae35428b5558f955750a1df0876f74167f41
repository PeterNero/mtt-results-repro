"""Build CONST-HIGGS-01 H7B1S Huv bridge functor or nonlinear HYM row execution."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1s_huv_bridge_functor_or_nonlinear_hym_row_execution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SECTION_C1_BRIDGE = BASE / "sectionring_and_c1_bridge_attempt.packet.json"
HYM_ROW_ATTEMPT = BASE / "direct_nonlinear_hym_row_execution_attempt.packet.json"
MINIMAL_THEOREM = BASE / "minimal_uv_higgs_plane_binding_theorem.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1S_HuvBridgeFunctorOrNonlinearHYMRowExecution_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1S_NEARHITS_TESTED_UV_HIGGS_PLANE_BINDING_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1r_path = DATA / "const_higgs_01_h7b1r_huv_source_operator_or_primitive_c1_lambda_bridge.candidate.json"
    h7b1r_contract_path = DATA / "const_higgs_01_h7b1r_huv_source_operator_or_primitive_c1_lambda_bridge" / "huv_bridge_acceptance_contract.packet.json"
    h7b1a_contract_path = DATA / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source" / "selected_splitting_or_projector_source_contract.packet.json"
    h7b1a_under_path = DATA / "const_higgs_01_h7b1a_selected_two_higgs_metric_or_light_projector_source" / "quotient_to_projector_underdetermination_proof.packet.json"

    sectionring_path = SM_PARITY / "candidate_data" / "selected_matterslot_grading_or_sectionring_readout.candidate.json"
    first_row_path = SM_PARITY / "candidate_data" / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource" / "first_row_exact_weyl_execution.packet.json"
    flavor_split_path = SM_PARITY / "candidate_data" / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
    hym_payload_path = SM_PARITY / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
    hym_newton_path = SM_PARITY / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"
    raw_nmtt_path = NONSM / "candidate_data" / "raw_nmtt_terminal_source_operator.candidate.json"

    h7b1r = load(h7b1r_path)
    h7b1r_contract = load(h7b1r_contract_path)
    h7b1a_contract = load(h7b1a_contract_path)
    h7b1a_under = load(h7b1a_under_path)
    sectionring = load(sectionring_path)
    first_row = load(first_row_path)
    flavor_split = load(flavor_split_path)
    hym_payload = load(hym_payload_path)
    hym_newton = load(hym_newton_path)
    raw_nmtt = load(raw_nmtt_path)

    operator_channels = sectionring["terminal_monad_sectionring_contract"]["must_bind_to_matter_slot_grading"]["operator_channels"]
    has_Hu_Hd_channel_labels = all(
        [
            "H_u" in operator_channels["up"],
            "H_d" in operator_channels["down"],
            "H_d" in operator_channels["charged_lepton"],
            "H_u" in operator_channels["dirac_neutrino"],
        ]
    )
    first_row_formula = first_row["selected_primitive_kernel_formula"]
    first_row_mentions_Hu = "H_u" in first_row_formula
    first_row_exact = first_row["computed_complex_entry_value"]["exact"] == "4/3"

    flavor_HuHd_is_not_Higgs_plane = all(
        [
            "Y_s(eps)" in flavor_split["path_A_higher_order_criterion"]["setup"],
            "H_s(eps)=Y_s(eps)Y_s(eps)^*" in flavor_split["path_A_higher_order_criterion"]["setup"],
            flavor_split["path_A_higher_order_criterion"]["current_values_available"] is False,
        ]
    )

    diagonal_metric = hym_payload["diagonal_metric_payload"]
    diagonal_hym_support_closed = all(
        [
            hym_payload["diagonal_metric_payload"]["closed"] is True,
            hym_payload["diagonal_connection_payload"]["closed"] is True,
            hym_payload["curvature_residual_payload"]["closed"] is True,
            hym_newton["closure_decision"]["selected_diagonal_HYM_first_solve_closed"] is True,
            hym_newton["closure_decision"]["rank2_End0_payload_closed"] is True,
        ]
    )

    terminal_source_support_closed = all(
        [
            raw_nmtt["verdict"]["finite_terminal_raw_operator_closed"] is True,
            raw_nmtt["verdict"]["q79_terminal_source_selected_by_operator_kernel"] is True,
            raw_nmtt["operator_checks"]["N7_positive_gap"] is True,
            raw_nmtt["what_closes_now"]["unique_zero_mode_selects_L3_K2"] is True,
        ]
    )

    uv_higgs_plane_binding_closed = False
    bridge_functor_emitted = False
    direct_nonlinear_hym_rows_emitted = False

    section_c1_bridge = {
        "schema": "MTTConstHiggs01H7B1SSectionRingAndC1BridgeAttempt.v1",
        "status": "SECTIONRING_AND_C1_NEARHITS_TESTED_NO_HUV_BRIDGE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-A-SECTIONRING-C1-BRIDGE",
        "input_sources": {
            "H7B1R": rel(h7b1r_path),
            "H7B1R_Huv_bridge_contract": rel(h7b1r_contract_path),
            "sectionring_readout": rel(sectionring_path),
            "first_row_exact_weyl_execution": rel(first_row_path),
            "higher_order_flavor_splitting": rel(flavor_split_path),
        },
        "nearhit_support": {
            "operator_channels_label_Hu_Hd": has_Hu_Hd_channel_labels,
            "sectionring_primary_route_ranked": sectionring["selection_decision"]["primary_route_selected_for_next_attempt"] == "typed_monad_cech_sectionring",
            "first_C1_row_exact_value_computed": first_row_exact,
            "first_C1_row_formula_mentions_Hu": first_row_mentions_Hu,
            "flavor_Hu_Hd_criterion_built": flavor_split["path_A_higher_order_criterion"]["proved"],
            "flavor_current_layer_no_go_proved": flavor_split["current_layer_no_go"]["proved"],
        },
        "why_not_Huv_bridge": {
            "sectionring_readout_closed": sectionring["selection_decision"]["selected_matter_slot_grading_readout_closed"],
            "terminal_monad_selector_closed_in_sectionring_packet": sectionring["selection_decision"]["terminal_monad_selector_closed"],
            "first_row_independent_and_provenance_clean": first_row["first_row_independently_executed_now"],
            "first_row_provenance_independent": first_row["provenance_independent_of_residual_projector_replay"],
            "first_row_codomain": first_row["row_id"],
            "flavor_HuHd_notation_is_Yukawa_Hermitian_not_Higgs_plane": flavor_HuHd_is_not_Higgs_plane,
            "Herm2_Huv_codomain_emitted": False,
            "T_Huv_emitted": False,
        },
        "decision": {
            "sectionring_C1_bridge_closes_Huv": False,
            "operator_channel_labels_can_replace_UV_Higgs_metric": False,
            "first_C1_row_can_replace_Huv_row": False,
            "reason": "The section-ring and first-row packets mention H_u/H_d in Yukawa operator channels, but they do not emit the UV Higgs-plane metric, light line, or Herm(2) mass-strain codomain required by H7B1R.",
        },
        **clean_flags(),
    }

    hym_row_attempt = {
        "schema": "MTTConstHiggs01H7B1SDirectNonlinearHYMRowExecutionAttempt.v1",
        "status": "DIAGONAL_HYM_AND_TERMINAL_SOURCE_SUPPORT_CLOSED_HUV_BINDING_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-B-NONLINEAR-HYM-ROW-ATTEMPT",
        "input_sources": {
            "H7B1A_selected_splitting_contract": rel(h7b1a_contract_path),
            "H7B1A_underdetermination_proof": rel(h7b1a_under_path),
            "diagonal_HYM_operator_payload": rel(hym_payload_path),
            "HYM_Newton_Galerkin_first_solve": rel(hym_newton_path),
            "raw_NMTT_terminal_source_operator": rel(raw_nmtt_path),
        },
        "closed_support": {
            "terminal_source_operator_kernel_selects_L3_K2": raw_nmtt["verdict"]["q79_terminal_source_selected_by_operator_kernel"],
            "terminal_positive_gap": raw_nmtt["operator_checks"]["N7_positive_gap"],
            "diagonal_HYM_metric_payload_closed": diagonal_metric["closed"],
            "diagonal_HYM_connection_payload_closed": hym_payload["diagonal_connection_payload"]["closed"],
            "diagonal_HYM_curvature_residual_closed": hym_payload["curvature_residual_payload"]["closed"],
            "selected_diagonal_HYM_first_solve_closed": hym_newton["closure_decision"]["selected_diagonal_HYM_first_solve_closed"],
            "rank2_End0_payload_closed": hym_newton["closure_decision"]["rank2_End0_payload_closed"],
        },
        "diagonal_HYM_payload": {
            "H_diagonal": diagonal_metric["H_diagonal"],
            "determinant": diagonal_metric["determinant"],
            "mesh": diagonal_metric["mesh"],
            "residual_l2": hym_payload["curvature_residual_payload"]["residual_l2"],
            "gradient_l2": hym_payload["diagonal_connection_payload"]["gradient_l2"],
        },
        "blocked_binding": {
            "diagonal_metric_bound_to_E_H_UV": False,
            "ordered_basis_Hu_Hddagger_emitted_by_this_route": False,
            "selected_horizontal_lift_emitted": h7b1a_contract["accepted_equivalent_payloads"]["selected_horizontal_lift"]["filled"],
            "selected_rank_one_projector_emitted": h7b1a_contract["accepted_equivalent_payloads"]["selected_rank_one_projector"]["filled"],
            "selected_Hermitian_metric_plus_minimal_lift_rule_emitted": h7b1a_contract["accepted_equivalent_payloads"]["selected_Hermitian_metric_plus_minimal_lift_rule"]["filled"],
            "selected_two_Higgs_mass_or_strain_matrix_emitted": h7b1a_contract["accepted_equivalent_payloads"]["selected_two_Higgs_mass_or_strain_matrix"]["filled"],
            "direct_selected_s_beta_emitted": h7b1a_contract["accepted_equivalent_payloads"]["direct_selected_s_beta"]["filled"],
            "single_Higgs_quotient_determines_s_beta": h7b1a_under["proof_result"]["single_Higgs_projection_determines_s_beta"],
        },
        "strict_outputs": {
            "B_Huv": None,
            "M_source": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "decision": {
            "direct_nonlinear_HYM_row_execution_closes_Huv": direct_nonlinear_hym_rows_emitted,
            "diagonal_HYM_metric_promoted_to_UV_Higgs_plane_metric": False,
            "raw_terminal_source_operator_promoted_to_Huv_rows": False,
            "reason": "The selected diagonal HYM and finite terminal source operator are strong same-branch support, but current packets do not bind that rank-2 End0 lane to E_H^UV or emit the selected light-line/Herm(2) payload.",
        },
        **clean_flags(),
    }

    minimal_theorem = {
        "schema": "MTTConstHiggs01H7B1SMinimalUVHiggsPlaneBindingTheorem.v1",
        "status": "MINIMAL_THEOREM_REDUCED_TO_UV_HIGGS_PLANE_BINDING_AND_LIGHTLINE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-C-MINIMAL-THEOREM",
        "theorem_to_prove_next": {
            "name": "SelectedUVHiggsPlaneBindingAndLightLineSourceTheorem",
            "statement": "The selected q79/F,m=1 terminal source and diagonal HYM rank-2 End0 lane act on the UV Higgs exact sequence 0 -> Ker(q)=span(H_u-H_d^dagger) -> E_H^UV -> span(H) -> 0, and emit either a selected light-line/projector P_L or a Hermitian Huv mass-strain matrix.",
            "clauses": [
                "section-ring/terminal source emits the ordered UV Higgs basis (H_u,H_d^dagger)",
                "selected diagonal HYM rank-2 metric/connection is proven to be the metric/operator on E_H^UV, not only an End0 support lane",
                "same-source rule emits a horizontal/minimal lift, rank-one projector, direct s_beta, B_Huv+M_source, or direct Huu,Hud,Hdd",
                "finite residual/truncation/source exactness certificate is attached",
                "no measured Higgs mass, beta, lambda, or threshold residual is used as selector",
            ],
        },
        "why_this_is_now_minimal": {
            "alpha_overlap_blocker_retired": h7b1r["same_source_functional_exit_closed"],
            "lambda12_shortcut_retired": h7b1r["lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda"],
            "single_Higgs_quotient_underdetermination_proved": h7b1a_under["proof_result"]["single_Higgs_projection_determines_s_beta"] is False,
            "diagonal_HYM_support_available": diagonal_hym_support_closed,
            "terminal_source_support_available": terminal_source_support_closed,
        },
        "would_close_if_proved": {
            "UV_Higgs_plane_binding_closed": True,
            "selected_s_beta_computable": True,
            "Huv_entries_computable": True,
            "lambda_H_after_EW_boundary_RG_policy": True,
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1SNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1S",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "H7B1R_lambda12_as_lambdaH_shortcut": h7b1r["lambda12_reclassified_as_gauge_threshold_not_Higgs_lambda"],
            "first_C1_row_as_Huv_row": first_row_exact,
            "flavor_HuHd_notation_as_UV_Higgs_plane": flavor_HuHd_is_not_Higgs_plane,
            "single_Higgs_quotient_as_light_projector": h7b1a_under["proof_result"]["single_Higgs_projection_determines_light_line_projector"] is False,
            "diagonal_HYM_metric_without_UV_binding_as_Huv_value": True,
        },
        "active_not_retired": {
            "UV_Higgs_plane_binding_theorem": True,
            "selected_light_line_or_projector": True,
            "direct_Herm2_Huv_rows": True,
            "nonlinear_HYM_correction_coefficients_with_residual_certificate": True,
        },
        "circulation_test": {
            "is_reopening_H7B1R": False,
            "is_reopening_quotient_underdetermination": False,
            "is_promoting_nearhit_notation_as_Huv": False,
            "new_information_added": [
                "section-ring H_u/H_d channel labels tested but not promoted",
                "exact first C1 row 4/3 imported and rejected as Huv row",
                "finite raw N_MTT terminal operator and diagonal HYM first solve combined as support",
                "minimal remaining theorem reduced to UV Higgs plane binding plus light-line/Herm2 emission",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1SNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1T_UV_HIGGS_PLANE_BINDING_OR_MINIMAL_LIFT_THEOREM",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM",
            "task": "Prove that the selected terminal source/diagonal HYM rank-2 lane binds to the UV Higgs exact sequence and emits a selected light-line/projector or direct Herm(2) Huv payload.",
        },
        "legal_exits": [
            {
                "id": "H7B1T-A",
                "label": "UV plane binding plus minimal lift",
                "must_emit": "E_H^UV basis, selected metric/connection binding, and horizontal/minimal lift or rank-one P_L",
            },
            {
                "id": "H7B1T-B",
                "label": "direct Herm2 payload",
                "must_emit": "B_Huv and M_source or direct Huu,Hud,Hdd with residual/exactness certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected diagonal HYM/End0 nonlinear row lane",
            "support_path": "terminal monad/section-ring labels plus exact C1 row support, used only after UV Higgs-plane binding",
            "locked_target": "selected UV Higgs light line or Herm(2) Huv payload, not observed lambda_H",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1SHuvBridgeFunctorOrNonlinearHYMRowExecutionTheorem",
        "proved": True,
        "statement": (
            "H7B1S tests the strongest near-hits after H7B1R. Section-ring/Yukawa H_u/H_d labels, the exact first C1 row value 4/3, flavor Hermitian H_u/H_d criteria, the finite raw terminal source operator, and the selected diagonal HYM first solve are all real support. None currently emits the UV Higgs-plane binding, selected light-line/projector, or Herm(2) Huv payload. Therefore the remaining theorem is minimal: prove that the selected terminal source and diagonal HYM rank-2 lane bind to E_H^UV=span(H_u,H_d^dagger) and emit either a light-line/minimal lift or direct Huv rows."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1SHuvBridgeFunctorOrNonlinearHYMRowExecution",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION",
        "output_packets": {
            "sectionring_and_c1_bridge_attempt": rel(SECTION_C1_BRIDGE),
            "direct_nonlinear_hym_row_execution_attempt": rel(HYM_ROW_ATTEMPT),
            "minimal_uv_higgs_plane_binding_theorem": rel(MINIMAL_THEOREM),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1R_imported": h7b1r["status"] == "MTT_CONST_HIGGS_01_H7B1R_BOTH_EXITS_TESTED_HUV_SOURCE_PAYLOAD_OPEN",
        "terminal_source_operator_kernel_selects_L3_K2": terminal_source_support_closed,
        "diagonal_HYM_first_solve_support_closed": diagonal_hym_support_closed,
        "first_C1_row_exact_value_computed": first_row_exact,
        "sectionring_Hu_Hd_channel_labels_present": has_Hu_Hd_channel_labels,
        "UV_Higgs_plane_binding_closed": uv_higgs_plane_binding_closed,
        "bridge_functor_emitted": bridge_functor_emitted,
        "direct_nonlinear_HYM_rows_emitted": direct_nonlinear_hym_rows_emitted,
        "minimal_missing_theorem_built": True,
        "UV_twoHiggs_basis_emitted": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1T_UVHiggsPlaneBindingOrMinimalLiftTheorem_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1S_HuvBridgeFunctorOrNonlinearHYMRowExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "terminal_source_operator_kernel_selects_L3_K2": terminal_source_support_closed,
        "diagonal_HYM_first_solve_support_closed": diagonal_hym_support_closed,
        "first_C1_row_exact_value_computed": first_row_exact,
        "sectionring_Hu_Hd_channel_labels_present": has_Hu_Hd_channel_labels,
        "UV_Higgs_plane_binding_closed": uv_higgs_plane_binding_closed,
        "bridge_functor_emitted": bridge_functor_emitted,
        "direct_nonlinear_HYM_rows_emitted": direct_nonlinear_hym_rows_emitted,
        "minimal_missing_theorem_built": True,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1S Huv Bridge Functor Or Nonlinear HYM Row Execution v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1S-HUV-BRIDGE-FUNCTOR-OR-NONLINEAR-HYM-ROW-EXECUTION`

## Result

```text
terminal source operator selects L3-K2            {terminal_source_support_closed}
diagonal HYM first solve support closed           {diagonal_hym_support_closed}
section-ring H_u/H_d channel labels present       {has_Hu_Hd_channel_labels}
first C1 row exact value computed                 {first_row_exact}
UV Higgs plane binding closed                     {uv_higgs_plane_binding_closed}
bridge functor emitted                            {bridge_functor_emitted}
direct nonlinear HYM/Huv rows emitted             {direct_nonlinear_hym_rows_emitted}
B_Huv / M_source / direct Huv emitted             False
s_beta / lambda_H promoted                        False
```

## What Moved Forward

H7B1S imports the strongest near-hits and sorts them without overclaiming:
section-ring `H_u/H_d` channel labels, exact first C1 row `4/3`, the finite raw
terminal `N_MTT` source operator, and the selected diagonal HYM first solve are
all real support.  None yet emits the UV Higgs-plane binding or a Hermitian
`Huv` row.

## Remaining Boundary

The remaining theorem is now sharply minimal:

`SelectedUVHiggsPlaneBindingAndLightLineSourceTheorem`

It must bind the selected terminal source and diagonal HYM rank-2 lane to
`E_H^UV=span(H_u,H_d^dagger)` and emit either a selected light-line/projector or
direct `Huu,Hud,Hdd` rows.

Next label:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1T-UV-HIGGS-PLANE-BINDING-OR-MINIMAL-LIFT-THEOREM`
"""

    for path, payload in [
        (SECTION_C1_BRIDGE, section_c1_bridge),
        (HYM_ROW_ATTEMPT, hym_row_attempt),
        (MINIMAL_THEOREM, minimal_theorem),
        (NO_CYCLE, no_cycle),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
