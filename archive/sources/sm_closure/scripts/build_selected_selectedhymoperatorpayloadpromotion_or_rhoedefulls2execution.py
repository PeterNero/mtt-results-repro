"""Build selected HYM operator payload promotion / rhoE-D_E full-S2 execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_selectedhymoperatorpayloadpromotion_or_rhoedefulls2execution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PAYLOAD = PACKET_DIR / "selected_hym_operator_payload_promotion_gate.packet.json"
FULLS2 = PACKET_DIR / "rhoede_full_s2_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hym_operator_payload_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SelectedHYMOperatorPayloadPromotion_or_RhoEDEFullS2Execution_v1.md"

STATUS = (
    "MTT_SELECTED_SELECTEDHYMOPERATORPAYLOADPROMOTION_OR_RHOEDEFULLS2EXECUTION_"
    "BUILT_DIAGONAL_END0_CLOSED_PHIFIN_TRACE_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json")
    full_exps = load(DATA / "selected_full_exps_hym_newton_replay.candidate.json")
    hym_payload = load(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")
    end0_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")
    riesz = load(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json")
    t1t2 = load(DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json")
    firstsolve = load(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json")
    offdiag = load(DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json")
    physical = load(DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json")
    alpha1_tangent = load(DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json")
    alpha1_fill = load(DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json")
    sector_after = load(DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json")

    diagonal_end0_closed = (
        full_exps["coefficient_packet"]["diagonal_expS_solution_closed"]
        and hym_payload["operator_payload_boundary"]["diagonal_rank2_metric_connection_payload_extracted"]
        and end0_de["what_closes_now"]["directionwise_D_E_connection_matrices"]
        and riesz["operator_payload_boundary"]["protected_T3_Riesz_projector_extracted"]
        and riesz["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"]
        and t1t2["what_closes_now"]["T1_T2_covariant_Green"]
        and t1t2["what_closes_now"]["full_diagonal_End0_Riesz_Green"]
        and offdiag["what_closes_now"]["offdiagonal_Ext_source_has_zero_T1_T2_projection_in_selected_row_model"]
    )

    payload_gate = {
        "schema": "MTTSelectedHYMOperatorPayloadPromotionGate.v1",
        "status": "DIAGONAL_END0_OPERATOR_PAYLOAD_CLOSED_SECTOR_PROMOTION_OPEN",
        "closed_diagonal_payload": {
            "full_expS_diagonal_replay": full_exps["coefficient_packet"]["diagonal_expS_solution_closed"],
            "rank2_metric_connection_payload": hym_payload["operator_payload_boundary"][
                "diagonal_rank2_metric_connection_payload_extracted"
            ],
            "End0_D_E_connection_matrices": end0_de["what_closes_now"]["directionwise_D_E_connection_matrices"],
            "protected_T3_Riesz_Green": riesz["operator_payload_boundary"]["protected_T3_Riesz_projector_extracted"]
            and riesz["operator_payload_boundary"]["protected_T3_reduced_Green_extracted"],
            "T1_T2_covariant_Green": t1t2["what_closes_now"]["T1_T2_covariant_Green"],
            "row_model_offdiagonal_Ext_control": offdiag["what_closes_now"][
                "offdiagonal_Ext_source_has_zero_T1_T2_projection_in_selected_row_model"
            ],
        },
        "promotion_boundary": {
            "rank2_End0_payload_closed": firstsolve["closure_decision"]["rank2_End0_payload_closed"],
            "selected_diagonal_HYM_first_solve_closed": firstsolve["closure_decision"][
                "selected_diagonal_HYM_first_solve_closed"
            ],
            "rank2_to_sector_transfer_closed": firstsolve["closure_decision"]["rank2_to_sector_transfer_closed"],
            "physical_dotD_alpha1_closed": firstsolve["closure_decision"]["physical_dotD_alpha1_closed"],
            "selected_End0_to_sector_routing_values_extracted": sector_after["closure_decision"][
                "selected_End0_to_sector_routing_values_extracted"
            ],
            "finite_projector_values_promoted_to_selected": sector_after["closure_decision"][
                "finite_projector_values_promoted_to_selected"
            ],
            "PhiFin_selected_trace_emitted": sector_after["closure_decision"]["PhiFin_selected_trace_emitted"],
        },
        "rejected_shortcuts": {
            "continuous_Ext_scale_as_physical_alpha1": physical["what_closes_now"][
                "physical_alpha1_not_confused_with_continuous_knob"
            ],
            "alpha1_tangent_without_source_or_routing_lemma": alpha1_tangent["what_closes_now"][
                "no_promotion_without_source_or_routing_lemma_recorded"
            ],
            "q79_constants_support_as_sector_routing_values": alpha1_fill["what_closes_now"][
                "q79_constants_support_not_promoted"
            ],
            "model_active_projectors_as_selected_Ps_Ks": not sector_after["closure_decision"][
                "finite_projector_values_promoted_to_selected"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    fulls2 = {
        "schema": "MTTRhoEDEFullS2ExecutionGateFromHYMOperatorPayload.v1",
        "status": "FULL_S2_EXECUTION_BLOCKED_BY_PHIFIN_MINIMIZER_TRACE_AND_SECTOR_ROUTING",
        "ready": {
            "diagonal_End0_payload_ready": diagonal_end0_closed,
            "row_model_offdiagonal_control_ready": True,
            "PhiFin_selected_minimizer_trace_ready": sector_after["closure_decision"]["PhiFin_selected_trace_emitted"],
            "selected_projector_promotion_ready": sector_after["closure_decision"][
                "finite_projector_values_promoted_to_selected"
            ],
            "physical_dotD_alpha1_ready": sector_after["closure_decision"]["physical_dotD_alpha1_closed"],
            "End0_to_sector_routing_ready": sector_after["closure_decision"][
                "selected_End0_to_sector_routing_values_extracted"
            ],
            "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1": False,
            "full_S2_scalar_execution_ready": False,
        },
        "blocked_by": [
            "Phi_fin selected minimizer trace or equivalent full selected HYM/Strominger operator values",
            "promotion of finite projector values to selected P_s and ordered K_s",
            "selected rho_s matrix values and End0-to-sector routing values",
            "physical dotD_alpha1 same-branch driver",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterSelectedHYMOperatorPayloadGate.v1",
        "status": "NEXT_ATTACK_PHIFIN_MINIMIZER_TRACE_OR_FULL_SELECTED_STROMINGER_OPERATOR_VALUES",
        "closed_now": [
            "full diagonal End0 HYM payload",
            "T1/T2 covariant Green by pure-gauge equivalence",
            "selected row-model offdiagonal Ext control",
            "naive alpha1 scale route rejected",
        ],
        "recommended_next": {
            "artifact": NEXT_ARTIFACT,
            "reason": (
                "The remaining bridge is not another diagonal HYM solve. It is the source theorem that "
                "promotes model-active finite projector/rho_s data to selected Phi_fin/minimizer-trace "
                "sector payload, or an equivalent full selected HYM/Strominger operator value theorem."
            ),
        },
        "minimal_remaining_rows": [
            "Phi_fin_selected_minimizer_trace",
            "selected_P_s_K_s_projector_promotion",
            "selected_rho_s_matrix_values",
            "selected_End0_to_sector_routing_values",
            "physical_dotD_alpha1_same_branch_driver",
            "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    for path, packet in [(PAYLOAD, payload_gate), (FULLS2, fulls2), (CUTSET, cutset)]:
        write_json(path, packet)

    candidate = {
        "candidate": "MTTSelectedSelectedHYMOperatorPayloadPromotionOrRhoEDEFullS2Execution",
        "status": STATUS,
        "inputs": {
            "higher_response_payload_attempt": rel(
                DATA / "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution.candidate.json"
            ),
            "full_expS_hym_newton_replay": rel(DATA / "selected_full_exps_hym_newton_replay.candidate.json"),
            "hym_operator_payload": rel(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"),
            "end0_de_payload": rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"),
            "riesz_green_dotd": rel(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"),
            "t1t2_covariant_green": rel(DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"),
            "hym_firstsolve_sector_boundary": rel(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"),
            "physical_dotd_sector_routing_after_hym": rel(DATA / "selected_physicaldotd_sectorrouting_after_hymfirstsolve.candidate.json"),
        },
        "output_packets": {
            "selected_hym_operator_payload_promotion_gate": rel(PAYLOAD),
            "rhoede_full_s2_execution_gate": rel(FULLS2),
            "next_cutset_after_hym_operator_payload_gate": rel(CUTSET),
        },
        "what_closes_now": {
            "full_diagonal_End0_HYM_payload_closed": diagonal_end0_closed,
            "T1_T2_covariant_Green_closed": t1t2["what_closes_now"]["T1_T2_covariant_Green"],
            "row_model_offdiagonal_Ext_control_closed": offdiag["what_closes_now"][
                "offdiagonal_Ext_source_has_zero_T1_T2_projection_in_selected_row_model"
            ],
            "naive_alpha1_scale_route_retired": sector_after["what_closes_now"]["naive_alpha1_scale_route_retired"],
            "next_phifin_trace_cutset_selected": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "Phi_fin_selected_minimizer_trace": True,
            "selected_P_s_K_s_projector_promotion": True,
            "selected_rho_s_matrix_values": True,
            "selected_End0_to_sector_routing_values": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "validator_ready_sector_rhoE_DE_Riesz_Green_dotD_C1": True,
            "full_S2_value_execution": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "closure_decision": {
            "diagonal_End0_operator_payload_closed": diagonal_end0_closed,
            "selected_HYM_sector_payload_closed": False,
            "rank2_to_sector_transfer_closed": False,
            "physical_dotD_alpha1_closed": False,
            "rhoE_DE_fullS2_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "SelectedHYMPayloadPromotionReductionTheorem",
            "proved": diagonal_end0_closed
            and not sector_after["closure_decision"]["PhiFin_selected_trace_emitted"]
            and not sector_after["closure_decision"]["selected_End0_to_sector_routing_values_extracted"],
            "statement": (
                "The selected diagonal End0 HYM operator payload, T1/T2 covariant Green, and row-model "
                "offdiagonal Ext control are closed. Full-S2/rhoE-D_E execution still cannot proceed because "
                "the finite projector/rho_s/sector-routing data are model-active rather than promoted by a "
                "Phi_fin selected minimizer trace or equivalent full selected HYM/Strominger operator theorem."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    cert = {
        "certificate": "MTT_Selected_SelectedHYMOperatorPayloadPromotion_or_RhoEDEFullS2Execution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "diagonal_End0_operator_payload_closed": diagonal_end0_closed,
        "selected_HYM_sector_payload_closed": False,
        "rhoE_DE_fullS2_execution_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected SelectedHYMOperatorPayloadPromotion or RhoEDEFullS2Execution v1

Status: `{STATUS}`.

Closed now:

- full diagonal End0 HYM payload.
- `T1/T2` covariant Green by pure-gauge equivalence.
- selected row-model offdiagonal Ext control.
- rejection of the naive continuous Ext-scale alpha1 route.

Still open:

- `Phi_fin` selected minimizer trace.
- selected `P_s`, `K_s`, and `rho_s` promotion.
- selected End0-to-sector routing values.
- physical `dotD_alpha1` same-branch driver.
- validator-ready sector `rhoE/D_E/Riesz/Green/dotD/C1` packet.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
