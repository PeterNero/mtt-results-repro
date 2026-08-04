"""Audit first non-looping value-layer row emission / threshold import execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_valuelayerfirstnonloopingrowemission_or_thresholdimportexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INTERNAL_ATTEMPT = PACKET_DIR / "internal_selected_value_row_attempt.packet.json"
EXTERNAL_ATTEMPT = PACKET_DIR / "external_threshold_import_execution.packet.json"
DECISION = PACKET_DIR / "first_nonlooping_value_row_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ValueLayerFirstNonLoopingRowEmission_or_ThresholdImportExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VALUELAYERFIRSTNONLOOPINGROWEMISSION_OR_THRESHOLDIMPORTEXECUTION_"
    "BUILT_SOURCE_LAYER_ROW_AVAILABLE_VALUE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseFunctionalRowEmission_or_ExternalSourceRowImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    internal = load(INTERNAL_ATTEMPT)
    external = load(EXTERNAL_ATTEMPT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(internal["status"] == "SOURCE_LAYER_ROW_AVAILABLE_VALUE_FUNCTIONAL_NOT_EMITTED", "internal status mismatch")
    require(internal["source_layer_closed"] is True, "source layer not closed")
    require(internal["primitive_exactness_backimported"] is True, "primitive exactness missing")
    require(internal["candidate_row_payload_available"] is True, "candidate row payload missing")
    require(internal["candidate_row_was_previously_rejected_as_selected_source"] is True, "prior rejection not preserved")
    require(internal["accepted_as_true_value_source_row"] is False, "true value row overaccepted")
    require(internal["accepted_as_SM_parity_downstream_support"] is True, "downstream support not accepted")
    require(internal["observed_data_used_as_selector"] is False, "internal observed selector used")
    require(internal["target_fitting_used"] is False, "internal target fitting used")

    require(external["status"] == "NO_ACCEPTED_EXTERNAL_THRESHOLD_SOURCE_ROW_AVAILABLE", "external status mismatch")
    require(external["accepted_external_rows_present"] is False, "external rows overpresent")
    require(external["local_common_scale_packet_available"] is True, "common-scale packet missing")
    require(external["local_threshold_residuals_all_finite"] is True, "threshold residuals not finite")
    require(external["accepted_external_threshold_row_imported"] is False, "external row overimported")

    require(decision["status"] == "FIRST_NONLOOPING_ATTEMPT_EXECUTED_VALUE_FUNCTIONAL_OR_EXTERNAL_IMPORT_OPEN", "decision status mismatch")
    require(decision["internal_lane"]["source_layer_row_available"] is True, "internal lane missing row")
    require(decision["internal_lane"]["accepted_as_true_value_source_row"] is False, "internal lane overclosed")
    require(decision["external_lane"]["accepted_external_threshold_row_imported"] is False, "external lane overclosed")
    for key in [
        "first_nonlooping_internal_attempt_executed",
        "closed_VSD_source_layer_used_as_input_not_reproved",
        "external_import_lane_executed_against_manifest",
        "value_functional_gap_identified",
        "observed_constants_excluded_as_selectors",
    ]:
        require(decision["what_closes_now"][key] is True, f"decision close flag missing: {key}")
    for key in [
        "selected_threshold_response_functional",
        "selected_Yukawa_Higgs_value_functional",
        "accepted_external_threshold_source_row",
        "accepted_threshold_mass_scheme_source_rows",
        "full_correlated_likelihood_source",
        "true_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(decision["what_remains_open"][key] is True, f"decision open flag missing: {key}")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    closes = data["what_closes_now"]
    require(closes == decision["what_closes_now"], "candidate close flags diverge")
    remains = data["what_remains_open"]
    require(remains == decision["what_remains_open"], "candidate remaining flags diverge")
    final = data["closure_decision"]
    require(final["source_layer_row_available"] is True, "final source row missing")
    require(final["accepted_true_value_source_row_emitted"] is False, "final value row overemitted")
    require(final["accepted_external_threshold_row_imported"] is False, "final external row overimported")
    require(final["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(final["full_no_knob_closed"] is False, "no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector used")
    require(data["target_fitting_used"] is False, "candidate target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("selected value functional" in note, "note missing value functional gap")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
