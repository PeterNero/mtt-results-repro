"""Audit Step52 VSD02 strict value-source frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step52_vsd02_strict_value_source_frontier_or_likelihoodworkspace"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "step52_vsd02_strict_frontier.packet.json"
ROW_RECHECK = PACKET_DIR / "step52_accepted_source_row_recheck.packet.json"
LIKELIHOOD = PACKET_DIR / "step52_external_likelihood_workspace_gate.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step52_next_threshold_functional_or_likelihood_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step52_VSD02StrictValueSourceFrontier_or_LikelihoodWorkspace_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP52_VSD02_STRICT_FRONTIER_LOCKED_ACCEPTED_ROWS_OPEN"
NEXT = "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    frontier = load(FRONTIER)
    rows = load(ROW_RECHECK)
    likelihood = load(LIKELIHOOD)
    next_frontier = load(NEXT_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step52 theorem not proved")

    for packet in [data, frontier, rows, likelihood, next_frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(frontier["step51_operator_domain_closed"] is True, "Step51 closure not imported")
    require(frontier["VSD01_legacy_dynamic_absence_blocker_retired"] is True, "VSD01 blocker not retired")
    require(frontier["VSD01_full_obligation_closed"] is False, "VSD01 overclosed")
    require(frontier["VSD02_route_classification_closed"] is True, "VSD02 classification missing")
    require(frontier["strict_accepted_source_row_schema_closed"] is True, "strict schema missing")
    require("VSD01 dynamic absence blocker" in frontier["superseded_blockers"], "VSD01 not superseded")

    require(rows["candidate_source_row_count"] == 6, "candidate row count mismatch")
    require(rows["accepted_row_count"] == 0, "source rows overaccepted")
    require(rows["accepted_threshold_matching_rows"] == [], "threshold rows overaccepted")
    require(rows["accepted_mass_scheme_conversion_rows"] == [], "mass rows overaccepted")
    require(rows["accepted_profile_likelihood_rows"] == [], "profile rows overaccepted")
    require(rows["accepted_no_knob_value_derivation_rows"] == [], "no-knob rows overaccepted")
    require(len(rows["candidate_results"]) == 6, "candidate result count mismatch")
    for result in rows["candidate_results"]:
        require(result["accepted_as_vsd02_source_row"] is False, f"candidate overaccepted: {result['candidate_id']}")
        require(result["support_present"] is True, f"support not recorded: {result['candidate_id']}")

    require(likelihood["manifest_closed"] is True, "external manifest not imported")
    require(likelihood["accepted_external_likelihood_import_closed"] is False, "external likelihood overclosed")
    require(likelihood["selected_threshold_response_functional_closed"] is False, "threshold functional overclosed")
    require(
        likelihood["no_knob_derivation_reduced_to_selected_response_functional"] is True,
        "no-knob reduction not imported",
    )

    require(next_frontier["next_required_artifact"] == NEXT, "next frontier mismatch")
    for key in [
        "Step51_operator_domain_backimport",
        "VSD01_v2_handoff_imported",
        "VSD02_route_classification_imported",
        "strict_source_row_schema_imported",
        "all_current_candidate_rows_rejected_without_overclaim",
    ]:
        require(next_frontier["closed_now"][key] is True, f"frontier close missing: {key}")
    for key in [
        "selected_threshold_response_functional_missing",
        "accepted_threshold_matching_source_rows_missing",
        "accepted_mass_scheme_conversion_source_rows_missing",
        "full_profile_likelihood_workspace_missing",
        "no_knob_Yukawa_Higgs_value_derivation_missing",
    ]:
        require(key in next_frontier["still_open"], f"still-open missing: {key}")

    decision = data["closure_decision"]
    require(decision["VSD02_strict_frontier_locked"] is True, "decision frontier not locked")
    require(decision["strict_accepted_source_row_schema_closed"] is True, "decision schema not closed")
    require(decision["candidate_source_rows_tested"] == 6, "decision candidate count mismatch")
    require(decision["accepted_vsd02_source_row_count"] == 0, "decision source rows overaccepted")
    for key in [
        "selected_threshold_response_functional_closed",
        "external_likelihood_workspace_closed",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "VSD02 strict frontier locked           : true",
        "candidate source rows tested           : 6",
        "accepted VSD02 source rows             : 0",
        "accepted internal Rtheta rows          : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
