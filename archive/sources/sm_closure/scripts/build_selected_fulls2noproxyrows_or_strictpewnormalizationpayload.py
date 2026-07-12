"""Build the full-S2/no-proxy ledger update after finite-replay Yukawa closure."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_fulls2noproxyrows_or_strictpewnormalizationpayload"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
FULLS2_UPDATE = PACKET_DIR / "fulls2_obligation_update_after_yukawa_finite_replay.packet.json"
PEW_STATUS = PACKET_DIR / "strict_pew_normalization_payload_status.packet.json"
DECISION = PACKET_DIR / "post_yukawa_fulls2_blocker_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FullS2NoProxyRows_or_StrictPEWNormalizationPayload_v1.md"

STRICT_FORK = DATA / "selected_strictpewdirectk_or_qasu3step10valueexecution.candidate.json"
STRICT_DECISION = (
    DATA
    / "selected_strictpewdirectk_or_qasu3step10valueexecution"
    / "post_step10_blocker_decision.packet.json"
)
FULLS2 = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
FULLS2_GAP = (
    DATA
    / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
    / "fulls2_no_proxy_remaining_gap.packet.json"
)
YUKAWA_FINITE = DATA / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure.candidate.json"
YUKAWA_DECISION = (
    DATA
    / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure"
    / "strict_sm_noknob_closure_decision.packet.json"
)
YUKAWA_DYNAMIC_GAP = (
    DATA / "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap.candidate.json"
)
PEW_PAYLOAD = DATA / "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload.candidate.json"

STATUS = (
    "MTT_SELECTED_FULLS2NOPROXYROWS_OR_STRICTPEWNORMALIZATIONPAYLOAD_"
    "BUILT_YUKAWA_SUPERSEDED_CKMPMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_CKMPMNSRows_or_HiggsThresholdStrictPEWExit_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    strict_fork = load(STRICT_FORK)
    strict_decision = load(STRICT_DECISION)
    fulls2 = load(FULLS2)
    fulls2_gap = load(FULLS2_GAP)
    yukawa_finite = load(YUKAWA_FINITE)
    yukawa_decision = load(YUKAWA_DECISION)
    yukawa_dynamic_gap = load(YUKAWA_DYNAMIC_GAP)
    pew_payload = load(PEW_PAYLOAD)

    first_dynamic_rows = strict_fork["key_numbers"]["accepted_first_dynamic_value_rows"]
    finite_yukawa_rows = yukawa_decision["source_row_counts"][
        "accepted_finite_replay_yukawa_magnitude_rows"
    ]
    finite_tail_rows = yukawa_decision["source_row_counts"]["accepted_finite_tail_source_rows"]
    strict_phase_rows = yukawa_decision["source_row_counts"][
        "accepted_strict_phase_antisymmetry_scalar_source_rows"
    ]
    finite_replay_yukawa_closed = yukawa_decision["acceptance"][
        "finite_replay_yukawa_exactness_closed"
    ]
    dynamic_yukawa_functional_closed = yukawa_dynamic_gap["closure_decision"][
        "Yukawa_magnitude_value_functional_closed"
    ]
    previous_closed = fulls2_gap["closed_value_source_obligation_rows_after"]
    previous_required = fulls2_gap["required_obligation_rows"]
    updated_closed = previous_closed + (1 if finite_replay_yukawa_closed else 0)
    updated_open = previous_required - updated_closed

    fulls2_update = {
        "schema": "MTTFullS2ObligationUpdateAfterFiniteReplayYukawa.v1",
        "status": "YUKAWA_MAGNITUDE_OBLIGATION_CLOSED_BY_FINITE_REPLAY_FULLS2_STILL_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_gap_packet": rel(FULLS2_GAP),
        "finite_replay_yukawa_decision": rel(YUKAWA_DECISION),
        "dynamic_yukawa_gap_candidate": rel(YUKAWA_DYNAMIC_GAP),
        "required_fullS2_obligation_rows": previous_required,
        "closed_value_source_obligation_rows_before": previous_closed,
        "closed_value_source_obligation_rows_after": updated_closed,
        "open_value_source_obligation_rows_after": updated_open,
        "closed_obligations": [
            {
                "id": "VSD-01.first_response_subrow",
                "source": rel(STRICT_FORK),
                "accepted_row_count": first_dynamic_rows,
                "closed": first_dynamic_rows == 2,
            },
            {
                "id": "charged_yukawa_magnitude_finite_replay_rows",
                "source": rel(YUKAWA_DECISION),
                "accepted_row_count": finite_yukawa_rows,
                "strict_phase_source_rows": strict_phase_rows,
                "finite_tail_source_rows": finite_tail_rows,
                "closed": finite_replay_yukawa_closed,
            },
        ],
        "supersession": {
            "stale_blocker": "derive magnitude/value functional from selected dynamic responses",
            "superseded_for_global_fullS2_ledger": finite_replay_yukawa_closed,
            "dynamic_first_response_value_functional_itself_closed": dynamic_yukawa_functional_closed,
            "reason": (
                "The dynamic-only theorem remains correct for the first-response route, but the "
                "global full-S2 charged-Yukawa magnitude obligation is now discharged by the "
                "selected finite projected replay source rows."
            ),
        },
        "still_required_payloads": [
            "derive running mass ratios and CKM/PMNS angles/phases without measured targets as selectors",
            "integrate selected Higgs/lambda_H and threshold/mass-scheme rows",
            "close strict P_EW/direct K_threshold.Omega_H.lambda as the parallel precision exit",
        ],
        "closed_flags_after_update": {
            "VSD_01_first_response_subrow_closed": first_dynamic_rows == 2,
            "charged_yukawa_magnitude_rows_closed_by_finite_replay": finite_replay_yukawa_closed,
            "dynamic_first_response_yukawa_functional_closed": dynamic_yukawa_functional_closed,
            "full_S2_no_proxy_rows_closed": False,
            "true_SM_equivalence_closed": False,
        },
    }

    pew_status = {
        "schema": "MTTStrictPEWNormalizationPayloadStatusAfterYukawaReplay.v1",
        "status": "STRICT_PEW_PAYLOAD_CONTRACT_LOCKED_VALUES_OPEN",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "payload_candidate": rel(PEW_PAYLOAD),
        "payload_contract_locked": pew_payload["closure_decision"]["payload_contract_locked"],
        "source_required_field_count": pew_payload["closure_decision"]["source_required_field_count"],
        "source_filled_field_count": pew_payload["closure_decision"]["source_filled_field_count"],
        "accepted_strict_P_EW_source_rows": pew_payload["closure_decision"][
            "accepted_strict_P_EW_source_rows"
        ],
        "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_payload["closure_decision"][
            "accepted_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "best_A_EW_expression_formula": pew_payload["closure_decision"]["best_A_EW_expression_formula"],
        "best_A_EW_expression_relative_residual": pew_payload["closure_decision"][
            "best_A_EW_expression_relative_residual"
        ],
        "strict_PEW_normalization_values_closed": False,
        "direct_K_certificate_values_closed": False,
    }

    decision = {
        "schema": "MTTPostYukawaFullS2BlockerDecision.v1",
        "status": "YUKAWA_MAGNITUDES_SUPERSEDED_FULLS2_REDUCED_TO_THREE_OPEN_CLASSES",
        "closed_now": [
            "The full-S2 charged-Yukawa magnitude obligation is closed by the finite projected replay source route.",
            "The older dynamic-only Yukawa magnitude functional gap is retained as a route-specific no-go, not as the active global blocker.",
            "Full-S2 obligation accounting moves from 1/5 to 2/5 closed.",
            "The strict PEW/direct-K payload contract is locked and remains a value-emission target, not an undefined task.",
        ],
        "not_closed": [
            "CKM/PMNS orientation and running mass-ratio value rows remain open.",
            "Higgs/lambda_H plus threshold and mass-scheme value rows remain open.",
            "Strict P_EW/direct K_threshold.Omega_H.lambda normalization values remain open.",
        ],
        "source_row_counts": {
            "accepted_first_dynamic_value_rows": first_dynamic_rows,
            "accepted_finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "accepted_strict_phase_antisymmetry_scalar_source_rows": strict_phase_rows,
            "accepted_finite_tail_source_rows": finite_tail_rows,
            "accepted_strict_P_EW_source_rows": pew_status["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": pew_status[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
        },
        "acceptance": {
            "charged_yukawa_magnitude_requirement_closed_by_finite_replay": finite_replay_yukawa_closed,
            "dynamic_first_response_yukawa_functional_closed": dynamic_yukawa_functional_closed,
            "fullS2_obligation_rows_required": previous_required,
            "fullS2_obligation_rows_closed_before": previous_closed,
            "fullS2_obligation_rows_closed_after_yukawa_update": updated_closed,
            "fullS2_obligation_rows_still_open_after_yukawa_update": updated_open,
            "fullS2_no_proxy_rows_closed": False,
            "strict_PEW_normalization_payload_values_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedFullS2NoProxyRowsOrStrictPEWNormalizationPayload",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "strict_pew_or_qasu3_step10_candidate": rel(STRICT_FORK),
            "strict_pew_or_qasu3_step10_decision": rel(STRICT_DECISION),
            "fulls2_candidate": rel(FULLS2),
            "fulls2_gap": rel(FULLS2_GAP),
            "finite_replay_yukawa_candidate": rel(YUKAWA_FINITE),
            "finite_replay_yukawa_decision": rel(YUKAWA_DECISION),
            "dynamic_yukawa_gap_candidate": rel(YUKAWA_DYNAMIC_GAP),
            "strict_pew_payload_candidate": rel(PEW_PAYLOAD),
        },
        "output_packets": {
            "fulls2_obligation_update_after_yukawa_finite_replay": rel(FULLS2_UPDATE),
            "strict_pew_normalization_payload_status": rel(PEW_STATUS),
            "post_yukawa_fulls2_blocker_decision": rel(DECISION),
        },
        "theorem": {
            "name": "FullS2NoProxyLedgerUpdateAfterFiniteReplayYukawaTheorem",
            "proved": True,
            "statement": (
                "Once finite-replay Yukawa magnitude exactness is accepted at the selected finite "
                "projected source standard, the global full-S2 charged-Yukawa magnitude obligation "
                "is discharged even though the dynamic first-response route-specific magnitude "
                "functional remains open. The active full-S2 ledger therefore moves from 1/5 to "
                "2/5 obligations closed and reduces to CKM/PMNS/running ratios, Higgs/threshold "
                "rows, and strict PEW/direct-K normalization values."
            ),
        },
        "key_numbers": {
            "accepted_first_dynamic_value_rows": first_dynamic_rows,
            "accepted_finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
            "accepted_strict_phase_antisymmetry_scalar_source_rows": strict_phase_rows,
            "accepted_finite_tail_source_rows": finite_tail_rows,
            "fullS2_obligation_rows_required": previous_required,
            "fullS2_obligation_rows_closed_before": previous_closed,
            "fullS2_obligation_rows_closed_after_yukawa_update": updated_closed,
            "fullS2_obligation_rows_still_open_after_yukawa_update": updated_open,
            "strict_PEW_source_required_field_count": pew_status["source_required_field_count"],
            "strict_PEW_source_filled_field_count": pew_status["source_filled_field_count"],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_FullS2NoProxyRows_or_StrictPEWNormalizationPayload_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "charged_yukawa_magnitude_requirement_closed_by_finite_replay": finite_replay_yukawa_closed,
        "dynamic_first_response_yukawa_functional_closed": dynamic_yukawa_functional_closed,
        "accepted_finite_replay_yukawa_magnitude_rows": finite_yukawa_rows,
        "fullS2_obligation_rows_required": previous_required,
        "fullS2_obligation_rows_closed_after_yukawa_update": updated_closed,
        "fullS2_no_proxy_rows_closed": False,
        "strict_PEW_normalization_payload_values_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FullS2NoProxyRows or StrictPEWNormalizationPayload v1

Status: `{STATUS}`

## Closed Now

The charged-Yukawa magnitude obligation in the full-S2/no-proxy ledger is now
closed by the finite projected replay source route:

- accepted finite-replay Yukawa magnitude rows: `{finite_yukawa_rows}`
- strict phase-antisymmetry scalar source rows: `{strict_phase_rows}`
- finite tail source rows: `{finite_tail_rows}`
- full-S2 obligation count: `{previous_closed}/5 -> {updated_closed}/5`

This supersedes the older dynamic-only Yukawa magnitude blocker for the global
ledger.  It does not falsify that theorem: the dynamic first-response route
still does not emit the full nine charged magnitudes by itself.

## Still Open

The remaining active value-row classes are:

- CKM/PMNS orientation and running mass-ratio rows
- Higgs/`lambda_H` plus threshold and mass-scheme rows
- strict `P_EW` / direct `K_threshold.Omega_H.lambda` normalization rows

Strict PEW/direct-K remains at:

- strict `P_EW` rows: `{pew_status["accepted_strict_P_EW_source_rows"]}`
- direct-K rows: `{pew_status["accepted_direct_K_threshold_Omega_H_lambda_rows"]}`
- payload fields filled: `{pew_status["source_filled_field_count"]}/{pew_status["source_required_field_count"]}`

## Next Target

Next required artifact: `{NEXT}`.
"""

    write_json(FULLS2_UPDATE, fulls2_update)
    write_json(PEW_STATUS, pew_status)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
