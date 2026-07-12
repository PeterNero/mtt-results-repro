"""Audit full-S2/no-proxy ledger update after finite-replay Yukawa closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fulls2noproxyrows_or_strictpewnormalizationpayload"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FULLS2_UPDATE = PACKET_DIR / "fulls2_obligation_update_after_yukawa_finite_replay.packet.json"
PEW_STATUS = PACKET_DIR / "strict_pew_normalization_payload_status.packet.json"
DECISION = PACKET_DIR / "post_yukawa_fulls2_blocker_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FullS2NoProxyRows_or_StrictPEWNormalizationPayload_v1.md"

STATUS = (
    "MTT_SELECTED_FULLS2NOPROXYROWS_OR_STRICTPEWNORMALIZATIONPAYLOAD_"
    "BUILT_YUKAWA_SUPERSEDED_CKMPMNS_HIGGS_PEW_OPEN"
)
NEXT = "MTT_Selected_CKMPMNSRows_or_HiggsThresholdStrictPEWExit_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    update = load(FULLS2_UPDATE)
    pew = load(PEW_STATUS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(
        update["status"] == "YUKAWA_MAGNITUDE_OBLIGATION_CLOSED_BY_FINITE_REPLAY_FULLS2_STILL_OPEN",
        "update status",
    )
    require(update["observed_data_used_as_selector"] is False, "update observed selector")
    require(update["target_fitting_used"] is False, "update target fitting")
    require(update["required_fullS2_obligation_rows"] == 5, "fullS2 required")
    require(update["closed_value_source_obligation_rows_before"] == 1, "closed before")
    require(update["closed_value_source_obligation_rows_after"] == 2, "closed after")
    require(update["open_value_source_obligation_rows_after"] == 3, "open after")
    require(len(update["closed_obligations"]) == 2, "closed obligations")
    require(update["closed_obligations"][0]["accepted_row_count"] == 2, "first dynamic row count")
    require(update["closed_obligations"][0]["closed"] is True, "first dynamic row closed")
    require(update["closed_obligations"][1]["accepted_row_count"] == 9, "finite replay row count")
    require(update["closed_obligations"][1]["strict_phase_source_rows"] == 1, "strict phase count")
    require(update["closed_obligations"][1]["finite_tail_source_rows"] == 2, "finite tail count")
    require(update["closed_obligations"][1]["closed"] is True, "finite replay closed")
    require(
        update["supersession"]["superseded_for_global_fullS2_ledger"] is True,
        "global supersession",
    )
    require(
        update["supersession"]["dynamic_first_response_value_functional_itself_closed"] is False,
        "dynamic route overclosed",
    )
    require(len(update["still_required_payloads"]) == 3, "remaining payload count")
    flags = update["closed_flags_after_update"]
    require(flags["VSD_01_first_response_subrow_closed"] is True, "VSD flag")
    require(flags["charged_yukawa_magnitude_rows_closed_by_finite_replay"] is True, "Yukawa flag")
    require(flags["dynamic_first_response_yukawa_functional_closed"] is False, "dynamic flag")
    require(flags["full_S2_no_proxy_rows_closed"] is False, "fullS2 flag")
    require(flags["true_SM_equivalence_closed"] is False, "true SM flag")

    require(pew["status"] == "STRICT_PEW_PAYLOAD_CONTRACT_LOCKED_VALUES_OPEN", "PEW status")
    require(pew["observed_data_used_as_selector"] is False, "PEW observed selector")
    require(pew["target_fitting_used"] is False, "PEW target fitting")
    require(pew["payload_contract_locked"] is True, "payload contract")
    require(pew["source_required_field_count"] == 8, "source required")
    require(pew["source_filled_field_count"] == 0, "source filled")
    require(pew["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(pew["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(pew["strict_PEW_normalization_values_closed"] is False, "PEW values overclosed")
    require(pew["direct_K_certificate_values_closed"] is False, "direct K values overclosed")

    require(
        decision["status"] == "YUKAWA_MAGNITUDES_SUPERSEDED_FULLS2_REDUCED_TO_THREE_OPEN_CLASSES",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_first_dynamic_value_rows"] == 2, "decision first rows")
    require(counts["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "decision Yukawa")
    require(counts["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "decision phase")
    require(counts["accepted_finite_tail_source_rows"] == 2, "decision tail")
    require(counts["accepted_strict_P_EW_source_rows"] == 0, "decision PEW")
    require(counts["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "decision direct K")
    acceptance = decision["acceptance"]
    require(
        acceptance["charged_yukawa_magnitude_requirement_closed_by_finite_replay"] is True,
        "accept Yukawa",
    )
    require(acceptance["dynamic_first_response_yukawa_functional_closed"] is False, "accept dynamic")
    require(acceptance["fullS2_obligation_rows_required"] == 5, "accept required")
    require(acceptance["fullS2_obligation_rows_closed_before"] == 1, "accept before")
    require(acceptance["fullS2_obligation_rows_closed_after_yukawa_update"] == 2, "accept after")
    require(acceptance["fullS2_obligation_rows_still_open_after_yukawa_update"] == 3, "accept open")
    require(acceptance["fullS2_no_proxy_rows_closed"] is False, "fullS2 overclosed")
    require(
        acceptance["strict_PEW_normalization_payload_values_closed"] is False,
        "PEW overclosed",
    )
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "FullS2NoProxyLedgerUpdateAfterFiniteReplayYukawaTheorem", "theorem")
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "key Yukawa")
    require(key["fullS2_obligation_rows_closed_after_yukawa_update"] == 2, "key closed")
    require(key["fullS2_obligation_rows_still_open_after_yukawa_update"] == 3, "key open")
    require(key["strict_PEW_source_required_field_count"] == 8, "key PEW required")
    require(key["strict_PEW_source_filled_field_count"] == 0, "key PEW filled")

    require(cert["charged_yukawa_magnitude_requirement_closed_by_finite_replay"] is True, "cert Yukawa")
    require(cert["dynamic_first_response_yukawa_functional_closed"] is False, "cert dynamic")
    require(cert["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "cert row count")
    require(cert["fullS2_obligation_rows_closed_after_yukawa_update"] == 2, "cert fullS2")
    require(cert["fullS2_no_proxy_rows_closed"] is False, "cert fullS2 overclosed")
    require(cert["strict_PEW_normalization_payload_values_closed"] is False, "cert PEW")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "full-S2 obligation count: `1/5 -> 2/5`",
        "dynamic first-response route",
        "CKM/PMNS orientation and running mass-ratio rows",
        "strict `P_EW` / direct `K_threshold.Omega_H.lambda` normalization rows",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
