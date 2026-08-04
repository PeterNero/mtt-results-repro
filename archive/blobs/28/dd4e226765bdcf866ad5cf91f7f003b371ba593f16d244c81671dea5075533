"""Build current execution artifact for precision profile values or Qa/SU3 payload."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionprofileloopvalues_or_actualqasu3operatorpayload_currentexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "route_a_precision_profile_loop_execution.packet.json"
ROUTE_B = PACKET_DIR / "route_b_qasu3_hym_operator_execution.packet.json"
DECISION = PACKET_DIR / "current_execution_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionProfileLoopValues_or_ActualQaSU3OperatorPayload_CurrentExecution_v1.md"

STATUS = "MTT_SELECTED_PRECISIONPROFILELOOPVALUES_OR_ACTUALQASU3OPERATORPAYLOAD_CURRENTEXECUTION_BUILT_BOTH_ROUTES_OPEN"
NEXT = "MTT_Selected_LocalQFTPrecisionObservableTable_or_QaSU3HYMOperatorPacket_ValueAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    frontier = load(DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json")
    correlated = load(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json")
    precision_qft = load(DATA / "selected_precisionqftobservablerows_or_actualqasu3packet.candidate.json")
    external_rg = load(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json")
    qasu3_partial = load(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json")
    qasu3_crossrepo = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")
    hym_first = load(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json")
    stationary = load(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json")

    route_a = {
        "schema": "MTTPrecisionProfileLoopValuesCurrentExecution.RouteA.v1",
        "route": "precision_profile_loop_values",
        "inputs": {
            "frontier": rel(DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"),
            "correlated_profile_values": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
            "precision_qft_rows": rel(DATA / "selected_precisionqftobservablerows_or_actualqasu3packet.candidate.json"),
            "external_literature_rg": rel(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"),
        },
        "available_now": {
            "external_literature_RG_values": external_rg["what_closes_now"][
                "external_literature_rg_benchmark_values_filled"
            ],
            "hypercharge_basis_reduction": correlated["what_closes_now"]["hypercharge_basis_reduction"],
            "correlation_robust_profile_envelope": correlated["what_closes_now"][
                "correlation_robust_profile_envelope"
            ],
            "representative_tree_level_decay_rows": precision_qft["what_closes_now"][
                "representative_tree_level_decay_rows"
            ],
            "finite_nonnegative_decay_widths": precision_qft["what_closes_now"][
                "finite_nonnegative_decay_widths"
            ],
        },
        "missing_for_true_equivalence": {
            "published_or_reconstructed_correlated_profile_values": correlated["what_remains_open"][
                "published_or_reconstructed_correlated_profile_values"
            ],
            "local_QFT_observable_value_rows": correlated["what_remains_open"][
                "local_QFT_observable_value_rows"
            ],
            "loop_corrected_local_QFT_correlator_smatrix_decay_rows": precision_qft["what_remains_open"][
                "loop_corrected_local_QFT_correlator_smatrix_decay_rows"
            ],
            "multi_loop_threshold_convention_values": precision_qft["what_remains_open"][
                "multi_loop_threshold_convention_values"
            ],
        },
        "execution_result": {
            "route_attempted": True,
            "precision_value_table_emitted_now": False,
            "full_profile_likelihood_emitted_now": False,
            "accepted_for_true_SM_equivalence": False,
            "reason": (
                "Current Route A reaches external RG rows, basis reduction, correlation envelope, "
                "and representative tree QFT rows, but it still lacks full loop/profile observable values."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTActualQaSU3HYMOperatorPayloadCurrentExecution.RouteB.v1",
        "route": "actual_qasu3_hym_operator_payload",
        "inputs": {
            "frontier": rel(DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"),
            "partial_qasu3_payload": rel(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"),
            "crossrepo_qasu3_status": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
            "hym_first_solve": rel(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"),
            "stationary_dotd_frontier": rel(DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"),
        },
        "available_now": {
            "partial_same_source_payload_emitted": qasu3_partial["what_closes_now"][
                "partial_same_source_payload_emitted"
            ],
            "best_qasu3_payload_lane_selected": qasu3_partial["what_closes_now"][
                "best_qasu3_payload_lane_selected"
            ],
            "selected_diagonal_HYM_first_solve": hym_first["what_closes_now"][
                "selected_diagonal_HYM_first_solve"
            ],
            "diagonal_End0_DE_formula": hym_first["what_closes_now"]["diagonal_End0_DE_formula"],
            "stationary_projector_rho_s_reconciled": stationary["what_closes_now"][
                "stationary_projector_rho_s_reconciled"
            ],
            "crossrepo_promotable_qasu3_packet_found": qasu3_crossrepo[
                "any_promotable_qasu3_packet_found"
            ],
        },
        "missing_for_true_equivalence": {
            "actual_QaSU3_operator_payload": qasu3_partial["what_remains_open"][
                "actual_QaSU3_operator_payload"
            ],
            "Pic0_selection_or_quotient": qasu3_partial["what_remains_open"][
                "Pic0_selection_or_quotient"
            ],
            "selected_HYM_Riesz_Green_dotD": qasu3_partial["what_remains_open"][
                "selected_HYM_Riesz_Green_dotD"
            ],
            "dynamic_sector_ready_operator_payload": frontier["what_remains_open"][
                "dynamic_sector_ready_operator_payload"
            ],
            "selected_dynamic_PhiFin_C1_payload": stationary["what_remains_open"][
                "selected_dynamic_PhiFin_C1_payload"
            ],
        },
        "execution_result": {
            "route_attempted": True,
            "actual_operator_payload_emitted_now": False,
            "promotable_crossrepo_packet_found": False,
            "accepted_for_true_SM_equivalence": False,
            "reason": (
                "Current Route B has a partial same-source payload and diagonal HYM support, "
                "but no scanned repo or local artifact emits the selected dynamic Qa/SU3 operator packet."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPrecisionProfileOrQaSU3CurrentExecutionDecision.v1",
        "status": "BOTH_ROUTES_EXECUTED_SUPPORT_ONLY_TRUE_EQUIVALENCE_OPEN",
        "SM_parity_closed": frontier["closure_decision"]["SM_parity_closed"],
        "route_A": {
            "support_strength": "strong_for_benchmark_and_proxy_values",
            "closed_now": False,
            "next_fill": [
                "full precision observable value table",
                "published/reconstructed profile likelihood",
                "loop/scheme/threshold/covariance convention packet",
            ],
        },
        "route_B": {
            "support_strength": "strong_for_source_scaffold_and_partial_payload",
            "closed_now": False,
            "next_fill": [
                "actual selected Qa/SU3 operator packet",
                "Pic0/quotient selection",
                "sector-ready HYM/Riesz/Green/dotD/C1 payload",
            ],
        },
        "preferred_next": (
            "Execute a narrow value-attempt artifact that fills either Route A's precision observable table "
            "or Route B's selected Qa/SU3-HYM operator packet."
        ),
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionProfileLoopValuesOrActualQaSU3OperatorPayloadCurrentExecution",
        "status": STATUS,
        "inputs": {
            "current_frontier": rel(DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"),
            "correlated_profile_values": rel(DATA / "selected_correlatedprofilevalues_or_localqftobservablevalues.candidate.json"),
            "precision_qft_rows": rel(DATA / "selected_precisionqftobservablerows_or_actualqasu3packet.candidate.json"),
            "partial_qasu3_payload": rel(DATA / "selected_qasu3candidatepayloadfill_or_profilesourceacquisition.candidate.json"),
            "crossrepo_qasu3_status": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
        },
        "output_packets": {
            "route_a_precision_profile_loop_execution": rel(ROUTE_A),
            "route_b_qasu3_hym_operator_execution": rel(ROUTE_B),
            "current_execution_decision": rel(DECISION),
        },
        "theorem": {
            "name": "PrecisionProfileOrQaSU3CurrentExecutionTheorem",
            "proved": True,
            "statement": (
                "At the current true-equivalence frontier, both legal superset routes can be executed "
                "honestly using existing artifacts. Route A imports external RG, correlation-envelope, "
                "and tree/local-QFT support but lacks precision loop/profile values. Route B imports "
                "partial Qa/SU3 source payload and diagonal HYM support but lacks the actual selected "
                "dynamic operator packet. Therefore this artifact advances the execution state but does "
                "not close true SM equivalence."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "route_A_precision_profile_loop_values_closed": False,
            "route_B_actual_QaSU3_operator_payload_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "route_A_current_execution_audited": True,
            "route_B_current_execution_audited": True,
            "both_routes_kept_as_superset_paths": True,
            "next_value_attempt_target_selected": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "full_precision_observable_value_table": True,
            "published_or_reconstructed_profile_likelihood": True,
            "actual_QaSU3_operator_packet": True,
            "sector_ready_HYM_Riesz_Green_dotD_C1_payload": True,
            "QM_GR_measurement_response_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionProfileLoopValues_or_ActualQaSU3OperatorPayload_CurrentExecution_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "route_A_precision_profile_loop_values_closed": False,
        "route_B_actual_QaSU3_operator_payload_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected PrecisionProfileLoopValues or ActualQaSU3OperatorPayload CurrentExecution v1

This artifact executes both true-equivalence routes from the locked frontier.

Route A has external RG, profile-envelope, and tree/local-QFT support, but does
not yet emit the full precision observable table or accepted profile likelihood.

Route B has partial same-source Qa/SU3 payload and diagonal HYM support, but
does not yet emit the actual selected dynamic Qa/SU3 operator packet.

This is a superset execution checkpoint, not a closure claim and not a target
fit.  Observed constants remain downstream replay data only.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
