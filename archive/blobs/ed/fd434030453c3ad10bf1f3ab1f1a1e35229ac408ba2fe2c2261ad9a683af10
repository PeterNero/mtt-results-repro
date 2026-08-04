"""Build profile row replacement payload or Qa/SU3 slot source theorem attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = PACKET_DIR / "external_higgs_br_width_row_payload_candidate.packet.json"
QASU3 = PACKET_DIR / "qasu3_slot_source_theorem_attempt.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_profile_payload_or_slot_theorem.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ProfileRowReplacementPayload_or_QaSU3SlotSourceTheorem_v1.md"

STATUS = "MTT_SELECTED_PROFILEROWREPLACEMENTPAYLOAD_OR_QASU3SLOTSOURCETHEOREM_BUILT_EXTERNAL_ROWS_AND_SLOT_THEOREM_OPEN"
NEXT = "MTT_Selected_CovarianceProfilePayload_or_QaSU3SelectedSlotValues_v1"

CERN_BR_URL = "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAtMH12509_2014"
YR4_URL = "https://arxiv.org/abs/1610.07922"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues.candidate.json")
    edge_b = load(
        DATA
        / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues"
        / "edge_b_selected_qasu3_operator_slot_source_values_attempt.packet.json"
    )
    same_source = load(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json")

    total_width_mev = 4.08
    br_rows = [
        ("H_to_bb", "H->bb", 0.575, 2.8, 2.8),
        ("H_to_tautau", "H->tautau", 6.30e-2, 6.1, 6.0),
        ("H_to_mumu", "H->mumu", 2.19e-4, 6.4, 6.3),
        ("H_to_cc", "H->cc", 2.90e-2, 12.2, 12.2),
        ("H_to_gg", "H->gg", 8.56e-2, 10.6, 10.3),
        ("H_to_gammagamma", "H->gammagamma", 2.28e-3, 5.4, 5.3),
        ("H_to_Zgamma", "H->Zgamma", 1.55e-3, 9.4, 9.3),
        ("H_to_WW", "H->WW", 0.216, 4.8, 4.7),
        ("H_to_ZZ", "H->ZZ", 2.66e-2, 4.8, 4.7),
    ]
    replacement_payload_rows = []
    for row_id, channel, br, total_up, total_down in br_rows:
        partial_width_mev = br * total_width_mev
        replacement_payload_rows.append(
            {
                "id": row_id,
                "channel": channel,
                "branching_ratio": br,
                "total_width_MeV": total_width_mev,
                "partial_width_MeV": partial_width_mev,
                "total_uncertainty_plus_percent": total_up,
                "total_uncertainty_minus_percent": total_down,
                "source": CERN_BR_URL,
                "accepted_as_route_A_replacement_now": False,
                "why_not_accepted": (
                    "External BR and Gamma_H row payload is present, but the full correlated profile/"
                    "covariance semantics required by the repo acceptance controller are not present."
                ),
            }
        )

    profile_payload = {
        "schema": "MTTExternalHiggsBRWidthRowPayloadCandidate.v1",
        "external_sources": {
            "cern_12509_twiki": {
                "url": CERN_BR_URL,
                "role": "machine-encoded downstream BR and Gamma_H row payload candidate",
                "declared_scope": "M_H=125.09 GeV, Report-3-interpolated BR table with uncertainties and Gamma_H=4.08 MeV",
                "accepted_as_full_profile": False,
            },
            "yellow_report_4": {
                "url": YR4_URL,
                "role": "modern precision reference target for eventual accepted profile import",
                "declared_scope": "cross sections, branching ratios, PDFs, off-shell Higgs production/interference",
                "accepted_as_machine_row_payload_now": False,
            },
        },
        "row_payloads": replacement_payload_rows,
        "summary": {
            "row_payload_count": len(replacement_payload_rows),
            "rows_with_central_BR_and_partial_width": len(replacement_payload_rows),
            "accepted_route_A_replacement_rows_now": 0,
            "total_width_MeV": total_width_mev,
            "has_row_uncertainty_percent": True,
            "has_full_correlated_covariance_profile": False,
            "accepted_precision_profile_import_closed": False,
            "accepted_row_replacements_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    slot_attempt = edge_b["slot_source_value_attempt"]
    theorem_checks = {}
    for slot, slot_data in slot_attempt.items():
        theorem_checks[slot] = {
            "support_present": slot_data["support_present"],
            "selected_source_value_emitted_before": slot_data["selected_source_value_emitted"],
            "selected_source_value_emitted_now": False,
            "theorem_status": "SUPPORT_ONLY_SOURCE_VALUE_OPEN",
            "minimal_next_proof": slot_data["blocking_condition"],
        }

    qasu3_packet = {
        "schema": "MTTQaSU3SlotSourceTheoremAttempt.v1",
        "input_same_source_packet": rel(DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"),
        "input_edge_b": rel(
            DATA
            / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues"
            / "edge_b_selected_qasu3_operator_slot_source_values_attempt.packet.json"
        ),
        "same_source_support": {
            "topological_L3_minus_K2_candidate_imported": same_source["gate_results"][
                "topological_L3_minus_K2_candidate_imported"
            ],
            "s3_gs_support_imported_closed": same_source["gate_results"][
                "s3_gs_support_imported_closed"
            ],
            "monad_c2_mismatch_rejected": same_source["gate_results"]["monad_c2_mismatch_rejected"],
            "operator_source_promoted": same_source["gate_results"]["operator_source_promoted"],
        },
        "slot_theorem_attempts": theorem_checks,
        "summary": {
            "required_slot_count": len(theorem_checks),
            "support_slots_present_count": edge_b["slot_summary"]["support_slots_present_count"],
            "selected_source_values_emitted_now": 0,
            "actual_QaSU3_operator_packet_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTProfilePayloadOrQaSU3SlotTheoremDecision.v1",
        "status": "EXTERNAL_ROW_PAYLOAD_BUILT_SLOT_THEOREMS_SUPPORT_ONLY",
        "edge_A": {
            "external_higgs_BR_width_payload_built": True,
            "accepted_route_A_replacement_rows_now": 0,
            "accepted_precision_profile_import_closed": False,
            "remaining_blocker": "full correlated covariance/profile payload or accepted replacement-row provenance",
        },
        "edge_B": {
            "qasu3_slot_source_theorem_attempted": True,
            "selected_source_values_emitted_now": 0,
            "actual_QaSU3_operator_packet_closed": False,
            "remaining_blocker": "selected source theorem/value emission for at least one operator slot",
        },
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedProfileRowReplacementPayloadOrQaSU3SlotSourceTheorem",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(
                DATA / "selected_acceptedprecisionprofileimport_or_selectedqasu3operatorslotsourcevalues.candidate.json"
            ),
            "same_source_qasu3_packet": rel(
                DATA / "selected_qa_su3_same_source_visible_color_operator_packet.candidate.json"
            ),
            "external_cern_BR_source": CERN_BR_URL,
            "external_yellow_report_4_reference": YR4_URL,
        },
        "output_packets": {
            "external_higgs_br_width_row_payload_candidate": rel(PROFILE),
            "qasu3_slot_source_theorem_attempt": rel(QASU3),
            "promotion_decision_after_profile_payload_or_slot_theorem": rel(DECISION),
        },
        "theorem": {
            "name": "ProfileRowReplacementPayloadOrQaSU3SlotSourceTheoremAttempt",
            "proved": True,
            "statement": (
                "External CERN/LHCHXSWG data can be encoded as BR and Gamma_H row payload candidates, "
                "yielding partial-width candidates for nine Higgs channels. This improves Route A but "
                "does not satisfy the accepted precision-profile rule because full correlated covariance/"
                "profile semantics are absent. Route B attempts all eight Qa/SU3 slot source theorems and "
                "keeps every slot support-only until selected source values are emitted."
            ),
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "external_profile_row_payload_built": True,
            "accepted_route_A_row_value_replacements_closed": False,
            "accepted_precision_profile_import_closed": False,
            "selected_operator_slot_source_values_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "external_BR_GammaH_row_payload_candidate_built": True,
            "nine_partial_width_candidates_emitted": True,
            "qasu3_eight_slot_source_theorem_attempted": True,
            "profile_covariance_blocker_sharpened": True,
            "slot_value_emission_blocker_sharpened": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "accepted_external_precision_profile_packet": True,
            "full_correlated_covariance_profile": True,
            "accepted_route_A_row_value_replacements": True,
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
        "certificate": "MTT_Selected_ProfileRowReplacementPayload_or_QaSU3SlotSourceTheorem_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": True,
        "external_profile_row_payload_built": True,
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

    note = f"""# MTT Selected ProfileRowReplacementPayload or QaSU3SlotSourceTheorem v1

This artifact tries both next edges using corpus, repo state, and external data.

Route A encodes an external CERN/LHCHXSWG M_H=125.09 GeV BR and Gamma_H row
payload candidate.  It emits nine partial-width candidates, but does not accept
them as precision replacements because the full correlated covariance/profile
payload is still absent.

Route B attempts all eight Qa/SU3 slot source theorems.  Every slot remains
support-only; zero selected source values are emitted.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (PROFILE, profile_payload),
        (QASU3, qasu3_packet),
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
