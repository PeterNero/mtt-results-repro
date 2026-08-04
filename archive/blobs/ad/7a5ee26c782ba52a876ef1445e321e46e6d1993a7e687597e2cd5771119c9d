"""Build covariance/profile payload or Qa/SU3 selected slot values attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
COVARIANCE = PACKET_DIR / "higgs_external_row_covariance_surrogate_payload.packet.json"
QASU3 = PACKET_DIR / "qasu3_selected_slot_value_candidate_payload.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_covariance_or_slot_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CovarianceProfilePayload_or_QaSU3SelectedSlotValues_v1.md"

STATUS = "MTT_SELECTED_COVARIANCEPROFILEPAYLOAD_OR_QASU3SELECTEDSLOTVALUES_BUILT_SURROGATE_AND_CONDITIONAL_VALUES_OPEN"
NEXT = "MTT_Selected_ExternalProfileLikelihoodImport_or_QaSU3SlotSelectionProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem.candidate.json")
    profile_rows = load(
        DATA
        / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
        / "external_higgs_br_width_row_payload_candidate.packet.json"
    )
    qasu3_attempt = load(
        DATA
        / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
        / "qasu3_slot_source_theorem_attempt.packet.json"
    )

    rows = profile_rows["row_payloads"]
    covariance_rows = []
    for row in rows:
        sigma_plus = row["partial_width_MeV"] * row["total_uncertainty_plus_percent"] / 100.0
        sigma_minus = row["partial_width_MeV"] * row["total_uncertainty_minus_percent"] / 100.0
        sigma_sym = 0.5 * (sigma_plus + sigma_minus)
        covariance_rows.append(
            {
                "id": row["id"],
                "channel": row["channel"],
                "central_partial_width_MeV": row["partial_width_MeV"],
                "sigma_plus_MeV": sigma_plus,
                "sigma_minus_MeV": sigma_minus,
                "sigma_symmetric_MeV": sigma_sym,
                "diagonal_variance_MeV2": sigma_sym * sigma_sym,
                "accepted_as_full_profile_row_now": False,
            }
        )

    covariance = {
        "schema": "MTTHiggsExternalRowCovarianceSurrogatePayload.v1",
        "input_row_payload": rel(
            DATA
            / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
            / "external_higgs_br_width_row_payload_candidate.packet.json"
        ),
        "profile_kind": "diagonal_uncertainty_surrogate_from_external_row_totals",
        "row_count": len(covariance_rows),
        "rows": covariance_rows,
        "covariance_policy": {
            "diagonal_covariance_built": True,
            "uses_symmetric_total_uncertainty_average": True,
            "offdiagonal_correlations_available": False,
            "profile_likelihood_available": False,
            "accepted_as_full_correlated_profile": False,
            "why_not_accepted": (
                "The payload has central values and diagonal uncertainties only. It lacks the external "
                "correlation matrix/profile likelihood semantics required for precision-profile acceptance."
            ),
        },
        "summary": {
            "diagonal_covariance_rows": len(covariance_rows),
            "positive_variance_rows": sum(row["diagonal_variance_MeV2"] > 0 for row in covariance_rows),
            "accepted_precision_profile_import_closed": False,
            "accepted_route_A_row_replacements_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_slot_values = {}
    for slot, slot_data in qasu3_attempt["slot_theorem_attempts"].items():
        support = bool(slot_data["support_present"])
        conditional_slot_values[slot] = {
            "support_present": support,
            "conditional_value_candidate_emitted": support,
            "selected_source_value_emitted": False,
            "candidate_kind": "support_token" if support else "missing_support",
            "candidate_value": "SUPPORTED" if support else None,
            "why_not_selected": slot_data["minimal_next_proof"],
        }

    qasu3 = {
        "schema": "MTTQaSU3SelectedSlotValueCandidatePayload.v1",
        "input_slot_theorem_attempt": rel(
            DATA
            / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
            / "qasu3_slot_source_theorem_attempt.packet.json"
        ),
        "conditional_slot_values": conditional_slot_values,
        "summary": {
            "required_slot_count": len(conditional_slot_values),
            "conditional_value_candidates_emitted": sum(
                1 for value in conditional_slot_values.values() if value["conditional_value_candidate_emitted"]
            ),
            "selected_source_values_emitted": 0,
            "actual_QaSU3_operator_packet_closed": False,
        },
        "promotion_rule": (
            "A support token is not a selected slot value. Promotion requires the slot's source theorem "
            "or same-branch operator value emission, not merely support_present=true."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTCovarianceProfileOrQaSU3SelectedSlotValuesDecision.v1",
        "status": "DIAGONAL_COVARIANCE_SURROGATE_AND_CONDITIONAL_SLOT_VALUES_BUILT",
        "route_A": {
            "diagonal_covariance_surrogate_built": True,
            "accepted_full_profile_likelihood_imported": False,
            "accepted_precision_profile_import_closed": False,
            "next_blocker": "external profile likelihood or correlated covariance matrix",
        },
        "route_B": {
            "conditional_slot_value_candidates_built": True,
            "selected_source_values_emitted": 0,
            "actual_QaSU3_operator_packet_closed": False,
            "next_blocker": "slot selection proof or same-branch operator value emission",
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedCovarianceProfilePayloadOrQaSU3SelectedSlotValues",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem.candidate.json"),
            "external_higgs_row_payload": rel(
                DATA
                / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
                / "external_higgs_br_width_row_payload_candidate.packet.json"
            ),
            "qasu3_slot_theorem_attempt": rel(
                DATA
                / "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
                / "qasu3_slot_source_theorem_attempt.packet.json"
            ),
        },
        "output_packets": {
            "higgs_external_row_covariance_surrogate_payload": rel(COVARIANCE),
            "qasu3_selected_slot_value_candidate_payload": rel(QASU3),
            "promotion_decision_after_covariance_or_slot_values": rel(DECISION),
        },
        "theorem": {
            "name": "CovarianceSurrogateOrConditionalSlotValueTheorem",
            "proved": True,
            "statement": (
                "The external Higgs row payload induces a diagonal covariance surrogate by converting "
                "published total uncertainty percentages into partial-width variances. The Qa/SU3 slot "
                "attempt induces conditional slot-value candidates for support-present slots. Neither "
                "object is accepted as final true-equivalence data: the covariance lacks offdiagonal/profile "
                "semantics and the conditional slot values lack selected source proofs."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "diagonal_covariance_surrogate_built": True,
            "conditional_qasu3_slot_values_built": True,
            "accepted_precision_profile_import_closed": False,
            "selected_operator_slot_source_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "diagonal_covariance_surrogate_payload_built": True,
            "positive_variance_profile_rows_built": True,
            "conditional_qasu3_slot_value_candidates_built": True,
            "profile_likelihood_blocker_sharpened": True,
            "slot_selection_proof_blocker_sharpened": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "external_profile_likelihood_import": True,
            "full_correlated_covariance_profile": True,
            "accepted_precision_profile_import": True,
            "selected_operator_slot_source_values": True,
            "actual_QaSU3_operator_packet": True,
            "sector_ready_HYM_Riesz_Green_dotD_C1_payload": True,
            "QM_GR_measurement_response_interfaces": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "previous_candidate_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_CovarianceProfilePayload_or_QaSU3SelectedSlotValues_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "diagonal_covariance_surrogate_built": True,
        "conditional_qasu3_slot_values_built": True,
        "accepted_precision_profile_import_closed": False,
        "selected_operator_slot_source_values_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected CovarianceProfilePayload or QaSU3SelectedSlotValues v1

This artifact advances both paths.

Route A builds a diagonal covariance surrogate from the external Higgs BR/GammaH
row payload by translating total uncertainty percentages into partial-width
variances.  It is not a full correlated profile likelihood.

Route B builds conditional slot-value candidates for support-present Qa/SU3
slots.  These are support tokens, not selected source values.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (COVARIANCE, covariance),
        (QASU3, qasu3),
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
