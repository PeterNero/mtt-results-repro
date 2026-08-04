"""Build precision value emission attempt or Qa/SU3 source payload fill."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_precisionvalueemissionattempt_or_qasu3sourcepayloadfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRECISION_VALUES = PACKET_DIR / "partial_precision_value_emission.packet.json"
QASU3_ATTEMPT = PACKET_DIR / "qasu3_source_payload_fill_attempt.packet.json"
PROMOTION = PACKET_DIR / "true_equivalence_promotion_decision_after_value_attempt.packet.json"
CUTSET = PACKET_DIR / "next_value_completion_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrecisionValueEmissionAttempt_or_QaSU3SourcePayloadFill_v1.md"

STATUS = "MTT_SELECTED_PRECISIONVALUEEMISSIONATTEMPT_OR_QASU3SOURCEPAYLOADFILL_BUILT_PARTIAL_VALUES_QASU3_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json")
    diagonal = load(
        DATA
        / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
        / "diagonal_profile_likelihood_execution.packet.json"
    )
    envelope = load(
        DATA
        / "selected_correlatedprofilevalues_or_localqftobservablevalues"
        / "correlation_robust_profile_envelope.packet.json"
    )
    qasu3_contract = load(
        DATA
        / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade"
        / "actual_qasu3_operator_upgrade_contract.packet.json"
    )
    qasu3_crossrepo = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")

    value_rows = []
    for row in diagonal["profile_rows"]:
        value_rows.append(
            {
                "id": row["id"],
                "value": row["current_input_formula_value"],
                "benchmark": row["buttazzo_central_value"],
                "delta": row["delta"],
                "total_diagonal_sigma": row["total_diagonal_sigma"],
                "pull": row["pull"],
                "chi2_contribution": row["chi2_contribution"],
                "accepted_as_partial_precision_value": True,
                "accepted_as_full_correlated_profile_value": False,
            }
        )

    precision_values = {
        "schema": "MTTPartialPrecisionValueEmission.v1",
        "status": "PARTIAL_DIAGONAL_PRECISION_VALUES_EMITTED_FULL_PROFILE_OPEN",
        "source_profile": rel(
            DATA
            / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
            / "diagonal_profile_likelihood_execution.packet.json"
        ),
        "value_rows": value_rows,
        "row_count": len(value_rows),
        "diagonal_chi2": diagonal["chi2_diagonal"],
        "diagonal_reduced_chi2": diagonal["reduced_chi2_diagonal"],
        "max_abs_pull": diagonal["max_abs_pull"],
        "passes_coarse_diagonal_profile": diagonal["passes_coarse_diagonal_profile"],
        "correlation_envelope_source": rel(
            DATA
            / "selected_correlatedprofilevalues_or_localqftobservablevalues"
            / "correlation_robust_profile_envelope.packet.json"
        ),
        "passes_core_correlation_envelope": envelope["chi2_envelope"]["passes_core_correlation_envelope"],
        "passes_extreme_correlation_stress_envelope": envelope["chi2_envelope"]["passes_extreme_correlation_stress_envelope"],
        "accepted_as_value_emission_attempt": True,
        "accepted_as_full_true_equivalence_profile": False,
        "why_not_full_true_equivalence": [
            "full published or reconstructed covariance/profile matrix is absent",
            "extreme equicorrelation stress envelope does not pass",
            "precision local-QFT loop rows are not filled",
            "actual selected Qa/SU3 operator packet is not filled",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    qasu3_attempt = {
        "schema": "MTTQaSU3SourcePayloadFillAttempt.v1",
        "status": "QASU3_SOURCE_PAYLOAD_NOT_FILLED_CONTRACT_RETAINED",
        "contract_source": rel(
            DATA
            / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade"
            / "actual_qasu3_operator_upgrade_contract.packet.json"
        ),
        "crossrepo_status_source": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
        "crossrepo_status": qasu3_crossrepo["status"],
        "required_source_payload": qasu3_contract["required_source_payload"],
        "source_payload_fields": {
            "selected_color_operator_packet": None,
            "selected_representation_anomaly_certificate": None,
            "selected_D_E_or_rho_E_operator_data": None,
            "typed_monad_Cech_section_ring_operator_maps": None,
            "precision_observable_attachment_to_actual_packet": None,
        },
        "source_payload_filled": False,
        "accepted_as_actual_QaSU3_operator_upgrade": False,
        "accepted_for_true_SM_equivalence": False,
        "accepted_for_no_knob": False,
        "why_not_filled": [
            "cross-repo scan still reports no final actual packet",
            "current repo only has parity-interface replacement for SM-parity",
            "tree/precision replay values cannot select or define source-side operator data",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTTrueEquivalencePromotionDecisionAfterValueAttempt.v1",
        "status": "PARTIAL_VALUE_EMISSION_ACCEPTED_TRUE_EQUIVALENCE_STILL_OPEN",
        "route_A_precision_values": {
            "partial_values_emitted": True,
            "full_profile_values_filled": False,
            "can_close_true_SM_equivalence_now": False,
        },
        "route_B_qasu3_payload": {
            "source_payload_filled": False,
            "can_close_true_SM_equivalence_now": False,
            "can_close_no_knob_now": False,
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextValueCompletionCutset.v1",
        "status": "FULL_PROFILE_OR_ACTUAL_QASU3_VALUES_REQUIRED",
        "closed_now": [
            "partial diagonal precision value table emitted",
            "core correlation-envelope status attached",
            "Qa/SU3 source payload fill attempted and rejected as unfilled",
            "true-equivalence promotion decision recorded",
        ],
        "remaining_minimal_payloads": [
            "full non-Higgs covariance/profile matrix or likelihood workspace",
            "precision local-QFT loop/threshold observable values",
            "actual selected Qa/SU3 source/operator packet",
            "Higgs final-three route-A kernels or stronger likelihood replacement",
        ],
        "recommended_next_artifact": "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPrecisionValueEmissionAttemptOrQaSU3SourcePayloadFill",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade.candidate.json"),
            "diagonal_profile": rel(
                DATA
                / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
                / "diagonal_profile_likelihood_execution.packet.json"
            ),
            "correlation_envelope": rel(
                DATA
                / "selected_correlatedprofilevalues_or_localqftobservablevalues"
                / "correlation_robust_profile_envelope.packet.json"
            ),
            "qasu3_contract": rel(
                DATA
                / "selected_trueequivalenceprecisionvaluetable_or_actualqasu3operatorupgrade"
                / "actual_qasu3_operator_upgrade_contract.packet.json"
            ),
        },
        "output_packets": {
            "partial_precision_value_emission": rel(PRECISION_VALUES),
            "qasu3_source_payload_fill_attempt": rel(QASU3_ATTEMPT),
            "true_equivalence_promotion_decision": rel(PROMOTION),
            "next_value_completion_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "PartialPrecisionValueEmissionAndQaSU3FillAttemptTheorem",
            "proved": True,
            "statement": (
                "The repo can now emit a partial diagonal precision value table from the locked Mt-scale "
                "profile replay and correlation envelope, but this does not close true SM equivalence. "
                "The parallel Qa/SU3 source-payload fill remains unfilled because no actual selected "
                "operator packet is present. Therefore the next gate is full profile reconstruction or "
                "actual Qa/SU3 packet search."
            ),
        },
        "what_closes_now": {
            "partial_diagonal_precision_value_table": True,
            "qasu3_source_payload_fill_attempted": True,
            "promotion_decision_after_value_attempt": True,
            "next_value_completion_cutset": True,
        },
        "what_remains_open": {
            "true_SM_equivalence": True,
            "no_knob_closure": True,
            "full_nonHiggs_covariance_profile": True,
            "precision_local_QFT_loop_values": True,
            "actual_QaSU3_operator_packet": True,
        },
        "closure_decision": {
            "SM_parity_closed": previous["closure_decision"]["SM_parity_closed"],
            "partial_precision_values_emitted": True,
            "qasu3_source_payload_filled": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": cutset["recommended_next_artifact"],
    }

    cert = {
        "certificate": "MTT_Selected_PrecisionValueEmissionAttempt_or_QaSU3SourcePayloadFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "partial_precision_values_emitted": True,
        "qasu3_source_payload_filled": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": candidate["next_required_artifact"],
    }

    note = f"""# MTT Selected PrecisionValueEmissionAttempt or QaSU3SourcePayloadFill v1

Status: `{STATUS}`.

This artifact emits the first partial true-equivalence value table: the Mt-scale
diagonal profile rows with pulls, chi-square contributions, and correlation
envelope status.

The result is useful but not final:

- partial diagonal precision values are emitted;
- full covariance/profile likelihood is still absent;
- Qa/SU3 source-payload fill is attempted but remains unfilled;
- true SM equivalence and no-knob closure remain open.
"""

    for path, payload in [
        (PRECISION_VALUES, precision_values),
        (QASU3_ATTEMPT, qasu3_attempt),
        (PROMOTION, promotion),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
