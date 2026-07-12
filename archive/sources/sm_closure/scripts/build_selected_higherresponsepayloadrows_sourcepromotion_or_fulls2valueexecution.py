"""Build higher-response payload row source-promotion / full-S2 execution attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higherresponsepayloadrows_sourcepromotion_or_fulls2valueexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROMOTION = PACKET_DIR / "higher_response_payload_source_promotion_attempt.packet.json"
FULLS2 = PACKET_DIR / "full_s2_value_execution_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higher_response_payload_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HigherResponsePayloadRows_SourcePromotion_or_FullS2ValueExecution_v1.md"

STATUS = (
    "MTT_SELECTED_HIGHERRESPONSEPAYLOADROWS_SOURCEPROMOTION_OR_FULLS2VALUEEXECUTION_"
    "BUILT_DOTD_RETIRED_OPERATOR_PAYLOAD_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_SelectedHYMOperatorPayloadPromotion_or_RhoEDEFullS2Execution_v1"


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

    frontier = load(DATA / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger.candidate.json")
    ledger = load(
        DATA
        / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger"
        / "higher_response_payload_ledger_update.packet.json"
    )
    hym_projector = load(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json")
    hym_operator = load(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")
    end0_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")
    routec_de = load(DATA / "selected_routec_de_action_on_smooth_bn.candidate.json")
    routec_dotd = load(DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json")
    routec_rhoe = load(DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json")
    ext_hodge = load(DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json")
    end0_functor = load(DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json")
    alpha1 = load(DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json")
    higher = load(DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json")
    internal = load(DATA / "selected_internalrthetavaluederivation_or_minimaluniversalparameterselection.candidate.json")

    alpha1_dotd_closed = (
        alpha1["closure_decision"]["same_branch_alpha1_derivative_closed"]
        and alpha1["closure_decision"]["honest_dotd_validator_replay_closed"]
        and alpha1["closure_decision"]["visible_routec_operator_source_closed"]
    )

    promotion_rows = [
        {
            "row_id": "HYM_projector_zero_mode_basis_values",
            "support_present": hym_projector["what_closes_now"]["finite_model_active_projector_values_emitted"],
            "selected_now": False,
            "blocking_reason": "Projector values are model-active; selected HYM/Strominger source promotion remains open.",
            "source": rel(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"),
        },
        {
            "row_id": "Hermitian_metric_and_HYM_connection",
            "support_present": hym_operator["what_closes_now"]["diagonal_metric_bounds"]
            and hym_operator["what_closes_now"]["diagonal_connection_gradient_summaries"],
            "selected_now": False,
            "blocking_reason": "Diagonal replay exists, but full sector payload/offdiagonal control and rhoE/D_E transition payload remain open.",
            "source": rel(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"),
        },
        {
            "row_id": "D_E_action",
            "support_present": routec_de["what_closes_now"]["D_E_matrix_on_27_mode_BN_emitted"],
            "selected_now": False,
            "blocking_reason": "Honest D_E packet has selected_source_verified=false; source-lift diagnostic is not a selected source.",
            "source": rel(DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"),
        },
        {
            "row_id": "sector_projectors_dotD_alpha1",
            "support_present": routec_dotd["what_closes_now"]["sector_projectors_on_27_mode_BN_emitted"]
            and routec_dotd["what_closes_now"]["dotD_alpha1_matrix_in_same_basis_emitted"],
            "selected_now": alpha1_dotd_closed,
            "blocking_reason": (
                "dotD/alpha1 is retired by the same-branch alpha1 payload, but full sector projector payload still "
                "depends on selected HYM/operator source promotion."
            ),
            "source": rel(DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"),
        },
        {
            "row_id": "rho_E_transition_data",
            "support_present": routec_rhoe["what_closes_now"]["nonidentity_projective_rhoE_candidate_built"],
            "selected_now": False,
            "blocking_reason": "Nonidentity projective rhoE candidate exists, but BN/source-promotion and full transition payload remain open.",
            "source": rel(DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"),
        },
        {
            "row_id": "Ext_HYM_Hodge_projector_table",
            "support_present": ext_hodge["what_closes_now"]["Hodge_Lambda_row_table"],
            "selected_now": False,
            "blocking_reason": "Ext/Hodge projector table is support; nonlinear HYM correction coefficients remain open.",
            "source": rel(DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"),
        },
        {
            "row_id": "End0_to_sector_functor",
            "support_present": end0_functor["what_closes_now"]["minimal_functor_contract_emitted"],
            "selected_now": False,
            "blocking_reason": "The existing values were rejected as selected End0-sector functor values.",
            "source": rel(DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"),
        },
    ]

    selected_now = [row["row_id"] for row in promotion_rows if row["selected_now"]]
    support_only = [row["row_id"] for row in promotion_rows if row["support_present"] and not row["selected_now"]]

    promotion = {
        "schema": "MTTHigherResponsePayloadSourcePromotionAttempt.v1",
        "status": "DOTD_ALPHA1_RETIRED_REMAINING_OPERATOR_PAYLOAD_SUPPORT_ONLY",
        "frontier_source": rel(DATA / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger.candidate.json"),
        "ledger_source": rel(
            DATA
            / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger"
            / "higher_response_payload_ledger_update.packet.json"
        ),
        "promotion_rows": promotion_rows,
        "selected_now": selected_now,
        "support_only_rows": support_only,
        "closed_now": {
            "same_branch_alpha1_derivative": alpha1["closure_decision"]["same_branch_alpha1_derivative_closed"],
            "honest_dotd_validator_replay": alpha1["closure_decision"]["honest_dotd_validator_replay_closed"],
            "visible_routec_operator_source": alpha1["closure_decision"]["visible_routec_operator_source_closed"],
        },
        "not_promoted_now": {
            "selected_HYM_projector_zero_mode_basis_values": True,
            "full_sector_HYM_metric_connection_payload": True,
            "selected_D_E_source_promotion": True,
            "selected_rho_E_transition_payload": True,
            "selected_End0_to_sector_functor_values": True,
            "nonlinear_HYM_correction_coefficients": True,
        },
        "guardrail": {
            "diagnostic_source_lift_not_counted_as_selected": True,
            "model_active_values_not_counted_as_selected": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    fulls2_ready = {
        "higher_response_Rtheta_contract_closed": higher["closure_decision"]["higher_response_Rtheta_functional_contract_closed"],
        "first_response_no_go_preserved": internal["closure_decision"]["first_response_only_route_rejected_for_scalar_no_knob_values"],
        "alpha1_dotd_retired": alpha1_dotd_closed,
        "selected_HYM_operator_payload_ready": False,
        "selected_rhoE_DE_operator_payload_ready": False,
        "selected_End0_sector_functor_ready": False,
        "scalar_Rtheta_rows_executable_now": False,
    }
    fulls2 = {
        "schema": "MTTFullS2ValueExecutionGateAfterPayloadPromotionAttempt.v1",
        "status": "FULL_S2_VALUE_EXECUTION_BLOCKED_BY_SELECTED_OPERATOR_PAYLOAD",
        "ready_fields": fulls2_ready,
        "execution_attempted": True,
        "execution_allowed_now": False,
        "accepted_scalar_row_count_now": 0,
        "codomain_scalar_row_count": higher["closure_decision"]["codomain_scalar_row_count"],
        "why_blocked": [
            "selected HYM/projector zero-mode values are still model-active, not selected",
            "honest D_E/rhoE operator payload is support-only or diagnostic-lifted",
            "End0-to-sector functor values are rejected as selected values",
            "nonlinear HYM correction/offdiagonal control remains open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHigherResponsePayloadAttempt.v1",
        "status": "NEXT_ATTACK_SELECTED_HYM_OPERATOR_PAYLOAD_OR_RHOE_DE_FULLS2_EXECUTION",
        "closed_now": [
            "same-branch alpha1 derivative and honest dotD replay retired",
            "visible Route-C operator source support retained",
            "higher-response execution blocked for a precise selected-operator-payload reason",
        ],
        "recommended_next": {
            "artifact": NEXT_ARTIFACT,
            "reason": (
                "The only payload row promoted in this attack is dotD/alpha1. The remaining full-S2 value "
                "execution wall is selected HYM/Strominger operator payload: zero-mode projectors, full "
                "metric/connection, rhoE/D_E/Riesz/Green, and End0-to-sector functor values."
            ),
        },
        "minimal_remaining_rows": [
            "selected_HYM_projector_zero_mode_basis_values",
            "full_sector_HYM_metric_connection_payload",
            "selected_rho_E_D_E_Riesz_Green_payload",
            "selected_End0_to_sector_functor_values",
            "scalar_Rtheta_value_rows_after_operator_payload",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    for path, packet in [(PROMOTION, promotion), (FULLS2, fulls2), (CUTSET, cutset)]:
        write_json(path, packet)

    candidate = {
        "candidate": "MTTSelectedHigherResponsePayloadRowsSourcePromotionOrFullS2ValueExecution",
        "status": STATUS,
        "inputs": {
            "current_frontier_reconciliation": rel(DATA / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger.candidate.json"),
            "higher_response_payload_ledger": rel(
                DATA
                / "selected_currentfrontierreconciliation_or_higherresponsepayloadledger"
                / "higher_response_payload_ledger_update.packet.json"
            ),
            "hym_projector_values": rel(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"),
            "hym_operator_payload": rel(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"),
            "end0_de_payload": rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"),
            "routec_de": rel(DATA / "selected_routec_de_action_on_smooth_bn.candidate.json"),
            "routec_dotd": rel(DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"),
            "routec_rhoe": rel(DATA / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"),
            "alpha1_payload": rel(DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"),
        },
        "output_packets": {
            "higher_response_payload_source_promotion_attempt": rel(PROMOTION),
            "full_s2_value_execution_gate": rel(FULLS2),
            "next_cutset_after_higher_response_payload_attempt": rel(CUTSET),
        },
        "what_closes_now": {
            "same_branch_alpha1_derivative_closed": alpha1["closure_decision"]["same_branch_alpha1_derivative_closed"],
            "honest_dotd_validator_replay_closed": alpha1["closure_decision"]["honest_dotd_validator_replay_closed"],
            "visible_routec_operator_source_closed": alpha1["closure_decision"]["visible_routec_operator_source_closed"],
            "higher_response_payload_support_audited": True,
            "full_S2_blocker_reduced_to_selected_operator_payload": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_HYM_projector_zero_mode_basis_values": True,
            "full_sector_HYM_metric_connection_payload": True,
            "selected_rho_E_D_E_Riesz_Green_payload": True,
            "selected_End0_to_sector_functor_values": True,
            "scalar_Rtheta_value_rows_after_operator_payload": True,
            "Yukawa_mass_mixing_value_closure": True,
            "lambda_H_value_execution": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "closure_decision": {
            "dotD_alpha1_payload_closed": alpha1_dotd_closed,
            "selected_operator_payload_closed": False,
            "full_S2_value_execution_closed": False,
            "higher_response_Rtheta_executed": False,
            "Yukawa_mass_mixing_value_closure": False,
            "lambda_H_value_execution": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "theorem": {
            "name": "HigherResponsePayloadAttemptReductionTheorem",
            "proved": alpha1_dotd_closed
            and fulls2_ready["higher_response_Rtheta_contract_closed"]
            and fulls2_ready["first_response_no_go_preserved"]
            and not fulls2["execution_allowed_now"],
            "statement": (
                "The same-branch alpha1/dotD part of the higher-response payload is retired, but all "
                "available HYM/projector/rhoE/D_E/End0 values are either model-active, diagnostic-lifted, "
                "or support-only. Therefore full-S2 scalar value execution is blocked exactly by selected "
                "operator payload promotion, not by first-response C1 source rows."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    cert = {
        "certificate": "MTT_Selected_HigherResponsePayloadRows_SourcePromotion_or_FullS2ValueExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": candidate["theorem"]["proved"],
        "dotD_alpha1_payload_closed": alpha1_dotd_closed,
        "selected_operator_payload_closed": False,
        "full_S2_value_execution_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected HigherResponsePayloadRows SourcePromotion or FullS2ValueExecution v1

Status: `{STATUS}`.

This artifact attacks the current higher-response payload rows.

Closed now:

- same-branch alpha1 derivative.
- honest dotD validator replay.
- visible Route-C operator-source support.

Still open:

- selected HYM/Strominger zero-mode projector values.
- full sector HYM metric/connection payload.
- selected rhoE/D_E/Riesz/Green operator payload.
- selected End0-to-sector functor values.
- full-S2 scalar `R_theta` value execution.

The diagnostic source-lift and model-active HYM/Route-C packets are useful
support, but they are not counted as selected full-S2 operator data.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
