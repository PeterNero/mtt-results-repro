"""Audit covariance/profile payload or Qa/SU3 selected slot values attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_covarianceprofilepayload_or_qasu3selectedslotvalues"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
COVARIANCE = PACKET_DIR / "higgs_external_row_covariance_surrogate_payload.packet.json"
QASU3 = PACKET_DIR / "qasu3_selected_slot_value_candidate_payload.packet.json"
DECISION = PACKET_DIR / "promotion_decision_after_covariance_or_slot_values.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CovarianceProfilePayload_or_QaSU3SelectedSlotValues_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_COVARIANCEPROFILEPAYLOAD_OR_QASU3SELECTEDSLOTVALUES_BUILT_SURROGATE_AND_CONDITIONAL_VALUES_OPEN"
NEXT = "MTT_Selected_ExternalProfileLikelihoodImport_or_QaSU3SlotSelectionProof_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    covariance = load(COVARIANCE)
    qasu3 = load(QASU3)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(covariance["profile_kind"] == "diagonal_uncertainty_surrogate_from_external_row_totals", "profile kind mismatch")
    require(covariance["row_count"] == 9, "covariance row count mismatch")
    require(covariance["summary"]["diagonal_covariance_rows"] == 9, "summary row count mismatch")
    require(covariance["summary"]["positive_variance_rows"] == 9, "variance rows not positive")
    for row in covariance["rows"]:
        require(row["central_partial_width_MeV"] > 0, f"nonpositive central value: {row['id']}")
        require(row["sigma_symmetric_MeV"] > 0, f"nonpositive sigma: {row['id']}")
        require(row["diagonal_variance_MeV2"] > 0, f"nonpositive variance: {row['id']}")
        require(row["accepted_as_full_profile_row_now"] is False, f"row overaccepted: {row['id']}")
    policy = covariance["covariance_policy"]
    require(policy["diagonal_covariance_built"] is True, "diagonal covariance not built")
    require(policy["offdiagonal_correlations_available"] is False, "offdiagonal correlations overclaimed")
    require(policy["profile_likelihood_available"] is False, "profile likelihood overclaimed")
    require(policy["accepted_as_full_correlated_profile"] is False, "full profile overaccepted")
    require(covariance["summary"]["accepted_precision_profile_import_closed"] is False, "precision profile overclosed")
    require(covariance["summary"]["accepted_route_A_row_replacements_closed"] is False, "row replacements overclosed")

    q_summary = qasu3["summary"]
    require(q_summary["required_slot_count"] == 8, "slot count mismatch")
    require(q_summary["conditional_value_candidates_emitted"] >= 7, "conditional slot values regressed")
    require(q_summary["selected_source_values_emitted"] == 0, "selected slot values overemitted")
    require(q_summary["actual_QaSU3_operator_packet_closed"] is False, "Qa/SU3 overclosed")
    for slot, value in qasu3["conditional_slot_values"].items():
        if value["support_present"]:
            require(value["conditional_value_candidate_emitted"] is True, f"support slot lacks conditional value: {slot}")
            require(value["candidate_value"] == "SUPPORTED", f"support token mismatch: {slot}")
        require(value["selected_source_value_emitted"] is False, f"slot overselected: {slot}")
        require(value["why_not_selected"], f"slot missing nonselection reason: {slot}")
    require("support token is not a selected slot value" in qasu3["promotion_rule"], "promotion rule missing guard")

    require(decision["status"] == "DIAGONAL_COVARIANCE_SURROGATE_AND_CONDITIONAL_SLOT_VALUES_BUILT", "decision mismatch")
    require(decision["route_A"]["diagonal_covariance_surrogate_built"] is True, "decision missing covariance")
    require(decision["route_A"]["accepted_full_profile_likelihood_imported"] is False, "decision overimported profile")
    require(decision["route_A"]["accepted_precision_profile_import_closed"] is False, "decision overclosed route A")
    require(decision["route_B"]["conditional_slot_value_candidates_built"] is True, "decision missing slot candidates")
    require(decision["route_B"]["selected_source_values_emitted"] == 0, "decision overemitted slot values")
    require(decision["route_B"]["actual_QaSU3_operator_packet_closed"] is False, "decision overclosed route B")
    require(decision["SM_parity_closed"] is True, "SM parity reopened")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["diagonal_covariance_surrogate_built"] is True, "candidate covariance missing")
    require(data["closure_decision"]["conditional_qasu3_slot_values_built"] is True, "candidate slot candidates missing")
    require(data["closure_decision"]["accepted_precision_profile_import_closed"] is False, "candidate profile overclosed")
    require(data["closure_decision"]["selected_operator_slot_source_values_closed"] is False, "candidate slot values overclosed")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_closed"] is False, "candidate Qa/SU3 overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require(data["what_closes_now"]["diagonal_covariance_surrogate_payload_built"] is True, "covariance close flag missing")
    require(data["what_closes_now"]["conditional_qasu3_slot_value_candidates_built"] is True, "slot close flag missing")
    require(data["what_remains_open"]["external_profile_likelihood_import"] is True, "profile likelihood gate missing")
    require(data["what_remains_open"]["selected_operator_slot_source_values"] is True, "selected slot value gate missing")
    require("not a full correlated profile likelihood" in note, "note missing profile guard")
    require("not selected source values" in note, "note missing slot guard")

    for packet in [data, covariance, qasu3, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
