"""Audit profile row replacement payload or Qa/SU3 slot source theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_profilerowreplacementpayload_or_qasu3slotsourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROFILE = PACKET_DIR / "external_higgs_br_width_row_payload_candidate.packet.json"
QASU3 = PACKET_DIR / "qasu3_slot_source_theorem_attempt.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_profile_payload_or_slot_theorem.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProfileRowReplacementPayload_or_QaSU3SlotSourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PROFILEROWREPLACEMENTPAYLOAD_OR_QASU3SLOTSOURCETHEOREM_BUILT_EXTERNAL_ROWS_AND_SLOT_THEOREM_OPEN"
NEXT = "MTT_Selected_CovarianceProfilePayload_or_QaSU3SelectedSlotValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    profile = load(PROFILE)
    qasu3 = load(QASU3)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    summary = profile["summary"]
    require(summary["row_payload_count"] == 9, "external row count mismatch")
    require(summary["rows_with_central_BR_and_partial_width"] == 9, "partial-width candidate count mismatch")
    require(summary["accepted_route_A_replacement_rows_now"] == 0, "Route A rows overaccepted")
    require(summary["total_width_MeV"] == 4.08, "GammaH value mismatch")
    require(summary["has_row_uncertainty_percent"] is True, "row uncertainty missing")
    require(summary["has_full_correlated_covariance_profile"] is False, "covariance overclaimed")
    require(summary["accepted_precision_profile_import_closed"] is False, "profile import overclosed")
    require(summary["accepted_row_replacements_closed"] is False, "row replacements overclosed")
    for row in profile["row_payloads"]:
        require(row["branching_ratio"] > 0, f"nonpositive BR: {row['id']}")
        require(row["partial_width_MeV"] > 0, f"nonpositive partial width: {row['id']}")
        require(row["accepted_as_route_A_replacement_now"] is False, f"row overaccepted: {row['id']}")
        require(row["source"].startswith("https://twiki.cern.ch/"), f"row source not CERN TWiki: {row['id']}")
    require(profile["external_sources"]["cern_12509_twiki"]["accepted_as_full_profile"] is False, "CERN page overaccepted")
    require(
        profile["external_sources"]["yellow_report_4"]["accepted_as_machine_row_payload_now"] is False,
        "YR4 overaccepted as machine row payload",
    )

    support = qasu3["same_source_support"]
    require(support["topological_L3_minus_K2_candidate_imported"] is True, "L3-K2 support missing")
    require(support["s3_gs_support_imported_closed"] is True, "S3/GS support missing")
    require(support["monad_c2_mismatch_rejected"] is True, "monad mismatch guard missing")
    require(support["operator_source_promoted"] is False, "operator source overpromoted")
    require(qasu3["summary"]["required_slot_count"] == 8, "slot count mismatch")
    require(qasu3["summary"]["support_slots_present_count"] >= 7, "support slot count regressed")
    require(qasu3["summary"]["selected_source_values_emitted_now"] == 0, "selected slot values overemitted")
    require(qasu3["summary"]["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 overclosed")
    for slot, status in qasu3["slot_theorem_attempts"].items():
        require(status["selected_source_value_emitted_before"] is False, f"slot preselected unexpectedly: {slot}")
        require(status["selected_source_value_emitted_now"] is False, f"slot selected unexpectedly: {slot}")
        require(status["theorem_status"] == "SUPPORT_ONLY_SOURCE_VALUE_OPEN", f"slot theorem status mismatch: {slot}")
        require(status["minimal_next_proof"], f"slot minimal proof missing: {slot}")

    require(decision["status"] == "EXTERNAL_ROW_PAYLOAD_BUILT_SLOT_THEOREMS_SUPPORT_ONLY", "decision status mismatch")
    require(decision["edge_A"]["external_higgs_BR_width_payload_built"] is True, "edge A payload not built")
    require(decision["edge_A"]["accepted_route_A_replacement_rows_now"] == 0, "edge A overaccepted rows")
    require(decision["edge_A"]["accepted_precision_profile_import_closed"] is False, "edge A profile overclosed")
    require(decision["edge_B"]["qasu3_slot_source_theorem_attempted"] is True, "edge B theorem not attempted")
    require(decision["edge_B"]["selected_source_values_emitted_now"] == 0, "edge B overemitted selected values")
    require(decision["edge_B"]["actual_QaSU3_operator_packet_closed"] is False, "edge B overclosed Qa/SU3")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["external_profile_row_payload_built"] is True, "candidate row payload missing")
    require(data["closure_decision"]["accepted_route_A_row_value_replacements_closed"] is False, "candidate rows overclosed")
    require(data["closure_decision"]["selected_operator_slot_source_values_closed"] is False, "candidate slots overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require(data["what_closes_now"]["nine_partial_width_candidates_emitted"] is True, "partial width close flag missing")
    require(data["what_closes_now"]["qasu3_eight_slot_source_theorem_attempted"] is True, "slot theorem close flag missing")
    require(data["what_remains_open"]["full_correlated_covariance_profile"] is True, "covariance gate missing")
    require(data["what_remains_open"]["selected_operator_slot_source_values"] is True, "slot value gate missing")
    require("nine partial-width candidates" in note, "note missing row payload summary")
    require("zero selected source values" in note, "note missing zero selected source values guard")

    for packet in [data, profile, qasu3, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
