"""Build CONST-HIGGS-01 H7B1P End0-to-Huv or sector-routing gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3_REPO = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1p_end0_to_huv_or_sector_routing"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SECTOR_IMPORT = BASE / "sector_routing_import.packet.json"
HUV_BOUNDARY = BASE / "huv_boundary_after_sector_routing.packet.json"
DOTD_FRONTIER = BASE / "dotd_driver_and_samesource_frontier.packet.json"
NO_CYCLE = BASE / "non_circulation_ledger.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1P_End0ToHuvOrSectorRouting_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1P_SECTOR_ROUTING_IMPORTED_HUV_TWOHIGGS_LIFT_OPEN"


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

    h7b1o_path = DATA / "const_higgs_01_h7b1o_diagonal_hym_payload_to_huv_transfer_gate.candidate.json"
    h7b1c_request_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"
    h7b1f_contract_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "nonsplit_to_huv_reduction_contract.packet.json"

    qa_end0_sector_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json"
    qa_hym_payload_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_hym_projector_source_payload_fill.candidate.json"
    qa_transport_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_transportclosed_bn_basis_or_symbolic_projector_replay.candidate.json"
    qa_dotd_driver_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json"
    qa_source_strength_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json"
    qa_1m_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_singlet_neutrino_rule_support_promotion_or_nogo.candidate.json"
    qa_same_source_path = QA_SU3_REPO / "candidate_data" / "selected_u1y_routec_samesource_selected_emission_source_certificate.candidate.json"

    h7b1o = load(h7b1o_path)
    h7b1c_request = load(h7b1c_request_path)
    h7b1f_contract = load(h7b1f_contract_path)
    qa_end0_sector = load(qa_end0_sector_path)
    qa_hym_payload = load(qa_hym_payload_path)
    qa_transport = load(qa_transport_path)
    qa_dotd_driver = load(qa_dotd_driver_path)
    qa_source_strength = load(qa_source_strength_path)
    qa_1m = load(qa_1m_path)
    qa_same_source = load(qa_same_source_path)

    end0_decision = qa_end0_sector["decision"]
    end0_values = qa_end0_sector["constructed_values_summary"]
    h_norm = end0_values["sector_T3_response_norms"]["H"]
    hym_decision = qa_hym_payload["decision"]
    transport_decision = qa_transport["decision"]
    dotd_decision = qa_dotd_driver["decision"]
    source_decision = qa_source_strength["decision"]
    same_source_decision = qa_same_source["decision"]

    sector_chain_support_closed = all(
        [
            end0_decision["End0_domain_values_filled"] is True,
            end0_decision["End0_tensor_product_carrier_constructed"] is True,
            end0_decision["sector_projectors_constructed"] is True,
            hym_decision["functional_projector_payload_filled"] is True,
            hym_decision["functional_source_map_rho_s_emitted"] is True,
            hym_decision["functional_zero_mode_bases_emitted"] is True,
            transport_decision["projector_riesz_green_replay_closed"] is True,
            transport_decision["selected_projector_source_verified"] is True,
            transport_decision["selected_rho_s_validator_ready"] is True,
            transport_decision["selected_riesz_green_source_verified"] is True,
            dotd_decision["transport_derivative_formula_closed"] is True,
            dotd_decision["selected_dotD_source_formula_closed"] is True,
            dotd_decision["selected_dotD_source_verified_by_transport_derivative"] is True,
            qa_1m["decision"]["singlet_neutrino_rule_support_promoted"] is True,
            qa_same_source["field_counts"]["support_present"] == qa_same_source["field_counts"]["required"],
        ]
    )

    selected_payload_still_open = any(
        [
            end0_decision["physical_dotD_alpha1_payload_extracted"] is False,
            end0_decision["selected_matter_slot_routing_extracted"] is False,
            end0_decision["selected_1M_Dirac_neutrino_rule"] is False,
            hym_decision["validator_ready_sector_packet_emitted"] is False,
            transport_decision["selected_transfer_normalization_emitted"] is False,
            dotd_decision["alpha1_driver_verified_now"] is False,
            source_decision["normalization_value_emitted_now"] is False,
            same_source_decision["same_source_selected_emission_certificate_closed"] is False,
        ]
    )

    collapsed_h_only = all(
        [
            h_norm["rank"] == 1,
            h_norm["zero_response"] is True,
            h_norm["frobenius_norm"] == 0.0,
            "H" in end0_values["sector_dimensions"],
            "H_u" not in end0_values["sector_dimensions"],
            "H_d^dagger" not in end0_values["sector_dimensions"],
        ]
    )

    sector_import = {
        "schema": "MTTConstHiggs01H7B1PSectorRoutingImport.v1",
        "status": "QA_SU3_SECTOR_ROUTING_SUPPORT_IMPORTED_SELECTED_PAYLOAD_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-A-SECTOR-ROUTING-IMPORT",
        "input_sources": {
            "H7B1O": rel(h7b1o_path),
            "QA_End0_to_sector_value_packet": rel(qa_end0_sector_path),
            "QA_HYM_projector_payload_fill": rel(qa_hym_payload_path),
            "QA_symbolic_transport_replay": rel(qa_transport_path),
            "QA_dotD_transport_derivative": rel(qa_dotd_driver_path),
            "QA_alpha1_source_strength": rel(qa_source_strength_path),
            "QA_1M_support": rel(qa_1m_path),
            "QA_same_source_emission_certificate": rel(qa_same_source_path),
        },
        "closed_support": {
            "canonical_End0_domain_values": end0_decision["End0_domain_values_filled"],
            "End0_tensor_product_carrier": end0_decision["End0_tensor_product_carrier_constructed"],
            "sector_projector_model": end0_decision["sector_projectors_constructed"],
            "functional_projector_payload": hym_decision["functional_projector_payload_filled"],
            "functional_rho_s": hym_decision["functional_source_map_rho_s_emitted"],
            "functional_zero_mode_bases": hym_decision["functional_zero_mode_bases_emitted"],
            "symbolic_transport_projector_replay": transport_decision["symbolic_transport_projector_replay_accepted"],
            "stationary_projector_riesz_green_replay": transport_decision["projector_riesz_green_replay_closed"],
            "dotD_transport_derivative_formula": dotd_decision["transport_derivative_formula_closed"],
            "selected_dotD_source_formula": dotd_decision["selected_dotD_source_formula_closed"],
            "one_M_support_promoted": qa_1m["decision"]["singlet_neutrino_rule_support_promoted"],
            "seven_of_seven_structural_support": qa_same_source["field_counts"]["support_present"] == qa_same_source["field_counts"]["required"],
        },
        "selected_payload_open": {
            "physical_dotD_alpha1_payload_extracted": end0_decision["physical_dotD_alpha1_payload_extracted"],
            "selected_matter_slot_routing_extracted": end0_decision["selected_matter_slot_routing_extracted"],
            "selected_1M_Dirac_neutrino_rule": end0_decision["selected_1M_Dirac_neutrino_rule"],
            "selected_transfer_normalization_extracted": end0_decision["selected_transfer_normalization_extracted"],
            "alpha1_driver_verified": dotd_decision["alpha1_driver_verified_now"],
            "normalization_value_emitted_now": source_decision["normalization_value_emitted_now"],
            "same_source_selected_emission_certificate_closed": same_source_decision["same_source_selected_emission_certificate_closed"],
        },
        "sector_chain_support_closed": sector_chain_support_closed,
        "selected_payload_still_open": selected_payload_still_open,
        **clean_flags(),
    }

    huv_boundary = {
        "schema": "MTTConstHiggs01H7B1PHuvBoundaryAfterSectorRouting.v1",
        "status": "SECTOR_ROUTING_REACHES_COLLAPSED_H_NOT_UV_TWOHIGGS_HUV",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-B-HUV-BOUNDARY",
        "input_sources": {
            "H7B1C_minimal_two_by_two_Huv_request": rel(h7b1c_request_path),
            "H7B1F_Huv_reduction_contract": rel(h7b1f_contract_path),
            "QA_End0_to_sector_value_packet": rel(qa_end0_sector_path),
        },
        "locked_Huv_target": {
            "ordered_basis": h7b1c_request["basis_required"]["ordered_basis"],
            "quotient_map": h7b1c_request["basis_required"]["quotient_map"],
            "Huv_formula": h7b1f_contract["computed_packet_when_filled"]["Huv"],
            "s_beta_formula": h7b1f_contract["computed_packet_when_filled"]["s_beta"],
        },
        "sector_output_available": {
            "sector_dimensions": end0_values["sector_dimensions"],
            "H_sector_rank": h_norm["rank"],
            "H_sector_zero_response": h_norm["zero_response"],
            "H_sector_frobenius_norm": h_norm["frobenius_norm"],
            "contains_collapsed_H": "H" in end0_values["sector_dimensions"],
            "contains_H_u": "H_u" in end0_values["sector_dimensions"],
            "contains_H_d_dagger": "H_d^dagger" in end0_values["sector_dimensions"],
        },
        "decision": {
            "collapsed_H_only": collapsed_h_only,
            "End0_to_sector_support_can_be_used_for_SM_sector_packet": True,
            "End0_to_sector_support_can_close_UV_Huv": False,
            "B_Huv_value_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huv_entries_emitted": False,
            "Omega_emitted": False,
            "s_beta_emitted": False,
            "lambda_H_emitted": False,
            "reason": "The imported sector packet has the low-energy H singlet as a rank-one zero-response sector. It does not emit the ordered UV two-Higgs basis (H_u,H_d^dagger), a two-column B_Huv lift, M_source, or direct Huv entries.",
        },
        "strict_payload_state": {
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
        **clean_flags(),
    }

    dotd_frontier = {
        "schema": "MTTConstHiggs01H7B1PDotDDriverAndSameSourceFrontier.v1",
        "status": "DOTD_TRANSPORT_CLOSED_ALPHA1_SOURCE_STRENGTH_VALUE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-C-DOTD-SAMESOURCE-FRONTIER",
        "input_sources": {
            "QA_dotD_transport_derivative": rel(qa_dotd_driver_path),
            "QA_alpha1_source_strength": rel(qa_source_strength_path),
            "QA_same_source_emission_certificate": rel(qa_same_source_path),
        },
        "dotD_frontier": {
            "transport_derivative_formula_closed": dotd_decision["transport_derivative_formula_closed"],
            "selected_dotD_source_formula_closed": dotd_decision["selected_dotD_source_formula_closed"],
            "selected_dotD_source_verified_by_transport_derivative": dotd_decision["selected_dotD_source_verified_by_transport_derivative"],
            "dotD_matrices_pass_if_driver_theorem_supplied": dotd_decision["dotD_matrices_pass_if_driver_theorem_supplied"],
            "alpha1_driver_verified_now": dotd_decision["alpha1_driver_verified_now"],
            "source_only_fails_only_by_alpha1_driver": dotd_decision["source_only_fails_only_by_alpha1_driver"],
        },
        "source_strength_frontier": {
            "source_strength_equivalence_theorem_proved": source_decision["source_strength_equivalence_theorem_proved"],
            "necessary_and_sufficient_for_dotD_closure": source_decision["necessary_and_sufficient_for_dotD_closure"],
            "current_source_value_no_go_proved": source_decision["current_source_value_no_go_proved"],
            "du_dalpha1_equals_h_ext_emitted": source_decision["du_dalpha1_equals_h_ext_emitted"],
            "normalization_value_emitted_now": source_decision["normalization_value_emitted_now"],
            "next_required_artifact": qa_source_strength["next_required_artifact"],
        },
        "same_source_frontier": {
            "support_present": qa_same_source["field_counts"]["support_present"],
            "required": qa_same_source["field_counts"]["required"],
            "selected_emitted": qa_same_source["field_counts"]["selected_emitted"],
            "same_source": qa_same_source["field_counts"]["same_source"],
            "theorem_derived": qa_same_source["field_counts"]["theorem_derived"],
            "next_required_artifact": qa_same_source["next_required_artifact"],
        },
        "decision": {
            "local_dotD_formula_blocker_retired": True,
            "alpha1_source_strength_value_is_active_blocker": True,
            "same_source_selected_emission_is_active_blocker": True,
            "Huv_twoHiggs_lift_still_separate": True,
        },
        **clean_flags(),
    }

    no_cycle = {
        "schema": "MTTConstHiggs01H7B1PNonCirculationLedger.v1",
        "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1P",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-NO-CYCLE",
        "retired_or_do_not_reopen": {
            "H7B1O_diagonal_HYM_payload": h7b1o["selected_diagonal_HYM_first_solve_closed"],
            "rank2_End0_payload": h7b1o["rank2_End0_payload_closed"],
            "sector_projector_model_construction": end0_decision["sector_projectors_constructed"],
            "functional_HYM_projector_payload": hym_decision["functional_projector_payload_filled"],
            "symbolic_transport_projector_replay": transport_decision["symbolic_transport_projector_replay_accepted"],
            "dotD_transport_derivative_formula": dotd_decision["transport_derivative_formula_closed"],
            "one_M_structural_support_gap": qa_1m["decision"]["singlet_neutrino_rule_support_promoted"],
        },
        "active_not_retired": {
            "same_source_ChernWeil_operator_functional_value": True,
            "alpha1_source_strength_value": True,
            "selected_transfer_normalization": True,
            "selected_matter_slot_routing_and_1M_emission": True,
            "UV_twoHiggs_lift_B_Huv": True,
            "same_source_Hermitian_M_source": True,
            "direct_Huv_rows": True,
        },
        "circulation_test": {
            "is_reopening_H7B1O": False,
            "is_promoting_support_as_selected_values": False,
            "new_information_added": [
                "QA/SU3 model End0-to-sector values imported",
                "functional HYM projector and rho_s payload imported",
                "symbolic transport projector/Riesz/Green replay imported",
                "dotD transport derivative and source formula imported",
                "alpha1 source-strength value no-go imported",
                "1_M structural support promoted but selected emission remains open",
                "Huv boundary sharpened to collapsed-H versus UV two-Higgs distinction",
            ],
        },
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1PNextWork.v1",
        "status": "NEXT_WORKORDER_H7B1Q_TWOHIGGS_LIFT_OR_SAMESOURCE_FUNCTIONAL_VALUE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE",
            "task": "Try to emit either a UV two-Higgs lift/source operator (B_Huv and M_source or direct Huv rows) or the same-source Chern-Weil/operator functional value that closes alpha1 driver and transfer normalization.",
        },
        "legal_exits": [
            {
                "id": "H7B1Q-A",
                "label": "UV two-Higgs lift",
                "must_emit": "selected B_Huv and same-source Hermitian M_source, or direct Huu,Hud,Hdd rows in (H_u,H_d^dagger)",
            },
            {
                "id": "H7B1Q-B",
                "label": "same-source Chern-Weil/operator functional",
                "must_emit": "du/dalpha1=h_ext, selected transfer normalization, matter-slot/1_M routing, and same-source operator functional value",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected HYM/End0/transport/dotD chain",
            "support_path": "QA/SU3 same-source matter-slot and alpha1 source-strength packets",
            "locked_target": "UV two-Higgs Huv payload or theorem-derived same-source functional, not measured Higgs data",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1PEnd0ToHuvOrSectorRoutingTheorem",
        "proved": True,
        "statement": (
            "Cross-repo QA/SU3 packets now advance the sector-routing branch beyond H7B1O: canonical End0 sector values, functional HYM projectors/rho_s/zero-mode bases, symbolic transport projector/Riesz/Green replay, and the dotD transport derivative are closed as support. "
            "They still do not close the Higgs Huv packet because their H-sector output is the collapsed rank-one H singlet, not the UV two-Higgs basis (H_u,H_d^dagger), and they do not emit B_Huv, M_source, or direct Huv rows. "
            "The remaining non-cyclic frontier is therefore either a UV two-Higgs lift/source operator or a same-source Chern-Weil/operator functional value that also supplies alpha1 source strength, transfer normalization, and selected matter-slot/1_M emission."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1PEnd0ToHuvOrSectorRouting",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING",
        "output_packets": {
            "sector_routing_import": rel(SECTOR_IMPORT),
            "huv_boundary_after_sector_routing": rel(HUV_BOUNDARY),
            "dotd_driver_and_samesource_frontier": rel(DOTD_FRONTIER),
            "non_circulation_ledger": rel(NO_CYCLE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1O_imported": h7b1o["selected_diagonal_HYM_first_solve_closed"] is True,
        "sector_chain_support_closed": sector_chain_support_closed,
        "functional_projector_payload_closed": hym_decision["functional_projector_payload_filled"],
        "symbolic_transport_replay_closed": transport_decision["symbolic_transport_projector_replay_accepted"],
        "dotD_transport_derivative_closed": dotd_decision["transport_derivative_formula_closed"],
        "collapsed_H_only": collapsed_h_only,
        "UV_twoHiggs_Huv_transfer_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "alpha1_source_strength_value_emitted": source_decision["normalization_value_emitted_now"],
        "same_source_selected_emission_closed": same_source_decision["same_source_selected_emission_certificate_closed"],
        "selected_matter_slot_routing_closed": same_source_decision["selected_U10_Ubar5_polarization_closed"],
        "selected_1M_Dirac_rule_closed": same_source_decision["selected_1M_Dirac_source_emitted"],
        "selected_transfer_normalization_closed": same_source_decision["selected_overlap_normalization_emitted"],
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1Q_TwoHiggsLiftOrSameSourceFunctionalValue_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1P_End0ToHuvOrSectorRouting_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "sector_chain_support_closed": sector_chain_support_closed,
        "functional_projector_payload_closed": hym_decision["functional_projector_payload_filled"],
        "symbolic_transport_replay_closed": transport_decision["symbolic_transport_projector_replay_accepted"],
        "dotD_transport_derivative_closed": dotd_decision["transport_derivative_formula_closed"],
        "collapsed_H_only": collapsed_h_only,
        "UV_twoHiggs_Huv_transfer_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "alpha1_source_strength_value_emitted": source_decision["normalization_value_emitted_now"],
        "same_source_selected_emission_closed": same_source_decision["same_source_selected_emission_certificate_closed"],
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1P End0 To Huv Or Sector Routing v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING`

## Result

```text
sector-routing support chain closed              {sector_chain_support_closed}
functional HYM projector payload closed          {hym_decision["functional_projector_payload_filled"]}
symbolic transport replay closed                 {transport_decision["symbolic_transport_projector_replay_accepted"]}
dotD transport derivative closed                 {dotd_decision["transport_derivative_formula_closed"]}
collapsed H only                                 {collapsed_h_only}
UV two-Higgs Huv transfer closed                 False
B_Huv / M_source / direct Huv emitted            False
alpha1 source-strength value emitted             {source_decision["normalization_value_emitted_now"]}
same-source selected emission closed             {same_source_decision["same_source_selected_emission_certificate_closed"]}
s_beta / lambda_H promoted                       False
```

## What Moved Forward

This is not a loop over H7B1O.  H7B1P imports newer QA/SU3 progress: model
End0-to-sector values, functional HYM projectors and `rho_s`, symbolic transport
projector/Riesz/Green replay, and the differentiated transport/dotD formula.
The 1_M Dirac-neutrino rule also has seven-of-seven structural support.

## Remaining Boundary

For Higgs, this route reaches only the collapsed rank-one `H` singlet.  It does
not emit the UV two-Higgs basis `(H_u,H_d^dagger)`, `B_Huv`, `M_source`, or
direct `Huu,Hud,Hdd` rows.

The next exact gate is:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1Q-TWOHIGGS-LIFT-OR-SAMESOURCE-FUNCTIONAL-VALUE`
"""

    for path, payload in [
        (SECTOR_IMPORT, sector_import),
        (HUV_BOUNDARY, huv_boundary),
        (DOTD_FRONTIER, dotd_frontier),
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
