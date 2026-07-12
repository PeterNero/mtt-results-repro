"""Audit VSD-02 accepted source rows fill / no-knob threshold derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_SCHEMA = PACKET_DIR / "accepted_source_row_strict_schema.packet.json"
FILL_ATTEMPT = PACKET_DIR / "accepted_source_rows_fill_attempt.packet.json"
DERIVATION_REDUCTION = PACKET_DIR / "no_knob_threshold_derivation_reduction.packet.json"
DECISION = PACKET_DIR / "vsd02_accepted_rows_fill_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd02_fill_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VSD02AcceptedSourceRowsFill_or_NoKnobThresholdDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VSD02ACCEPTEDSOURCEROWSFILL_OR_NOKNOBTHRESHOLDERIVATION_"
    "BUILT_STRICT_FILL_ATTEMPT_ACCEPTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseFunctionalDerivation_or_ProfileLikelihoodAcquisition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    strict = load(STRICT_SCHEMA)
    fill = load(FILL_ATTEMPT)
    reduction = load(DERIVATION_REDUCTION)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(strict["status"] == "STRICT_ACCEPTED_SOURCE_ROW_SCHEMA_EMITTED", "strict schema status mismatch")
    require(len(strict["accepted_row_must_include"]) >= 9, "strict schema too small")
    require("finite residual comparison tables without source-owner theorem" in strict["forbidden_as_accepted_source_rows"], "residual-table guard missing")
    require("partial Higgs covariance without full likelihood/profile semantics" in strict["forbidden_as_accepted_source_rows"], "partial-covariance guard missing")
    require(strict["closure_claimed"] is True, "strict schema should close")

    require(fill["status"] == "STRICT_FILL_ATTEMPT_EXECUTED_NO_ACCEPTED_ROWS", "fill status mismatch")
    require(fill["row_route_count"] == 6, "wrong row route count")
    require(fill["candidate_source_row_count"] == 6, "wrong candidate count")
    require(fill["accepted_row_count"] == 0, "accepted rows overclaimed")
    for key in [
        "accepted_threshold_matching_rows",
        "accepted_mass_scheme_conversion_rows",
        "accepted_profile_likelihood_rows",
        "accepted_no_knob_value_derivation_rows",
    ]:
        require(fill[key] == [], f"{key} should be empty")
    for result in fill["candidate_results"]:
        require(result["accepted_as_vsd02_source_row"] is False, f"candidate overaccepted: {result['candidate_id']}")
        require(result["rejection_reasons"], f"candidate lacks rejection reasons: {result['candidate_id']}")
    require(fill["closure_claimed"] is False, "fill overclaimed")

    support = reduction["closed_support"]
    for key in [
        "versioned_firstpass_value_packet_present",
        "finite_residual_table_present",
        "accepted_source_row_schema_present",
        "VSD02_rows_classified",
    ]:
        require(support[key] is True, f"reduction support missing: {key}")
    theorem = reduction["minimal_new_theorem_required"]
    require(theorem["name"] == "SelectedThresholdResponseFunctional", "wrong minimal theorem")
    require(len(theorem["must_emit"]) >= 5, "minimal theorem output list too small")
    require(reduction["external_acquisition_alternative"]["full_likelihood_imported_now"] is False, "external likelihood overimported")
    require(reduction["closure_claimed"] is False, "reduction overclaimed")

    require(decision["strict_schema_emitted"] is True, "strict schema not emitted")
    require(decision["fill_attempt_executed"] is True, "fill attempt not executed")
    require(decision["accepted_row_count"] == 0, "decision overaccepted rows")
    for key in [
        "accepted_threshold_response_rule_closed",
        "accepted_external_likelihood_import_closed",
        "no_knob_threshold_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    for key in [
        "strict_accepted_source_row_schema",
        "all_current_candidates_tested_against_schema",
        "no_knob_derivation_reduced_to_selected_response_functional",
        "external_likelihood_acquisition_requirements_reaffirmed",
    ]:
        require(decision["what_closes_now"][key] is True, f"decision close flag missing: {key}")
    for key in [
        "selected_threshold_response_functional_missing",
        "accepted_threshold_matching_source_rows_missing",
        "accepted_mass_scheme_conversion_source_rows_missing",
        "full_profile_likelihood_workspace_missing",
        "no_knob_Yukawa_Higgs_value_derivation_missing",
    ]:
        require(key in decision["remaining_hard_failures"], f"hard failure missing: {key}")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    final = data["closure_decision"]
    require(final["strict_fill_attempt_closed"] is True, "strict fill attempt not closed")
    for key in [
        "accepted_vsd02_source_rows_closed",
        "selected_threshold_response_functional_closed",
        "external_likelihood_workspace_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("accepted VSD02 source rows      : 0" in note, "note missing zero-row guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
