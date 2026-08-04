"""Audit same-branch convention or threshold-row emission frontier artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samebranchconvention_or_thresholdrowemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONVENTION_TARGET = PACKET_DIR / "true_precision_convention_target.packet.json"
SOURCE_GAP = PACKET_DIR / "same_branch_convention_source_gap.packet.json"
THRESHOLD_ORDER = PACKET_DIR / "threshold_row_emission_prerequisite_order.packet.json"
DECISION = PACKET_DIR / "same_branch_convention_or_threshold_row_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameBranchConvention_or_ThresholdRowEmission_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SAMEBRANCHCONVENTION_OR_THRESHOLDROWEMISSION_"
    "BUILT_CONVENTION_TARGET_IDENTIFIED_SOURCE_OPEN"
)
NEXT = "MTT_Selected_ConventionSourceTheorem_or_RGEngineThresholdPolicy_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    target = load(CONVENTION_TARGET)
    gap = load(SOURCE_GAP)
    order = load(THRESHOLD_ORDER)
    decision = load(DECISION)
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
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    require(
        target["status"] == "TRUE_PRECISION_CONVENTION_TARGET_IDENTIFIED_NOT_SELECTED_SOURCE",
        "target status mismatch",
    )
    require(target["target_scale"] == "M_Z", "target scale mismatch")
    require(target["target_scheme"] == "MSbar", "target scheme mismatch")
    require("gauge beta functions" in target["beta_functions_required"], "gauge beta missing")
    require("Higgs lambda beta function" in target["beta_functions_required"], "lambda beta missing")
    require(target["threshold_matching_required"]["top"], "top threshold missing")
    require(target["mass_scheme_conversion_required"]["direct_top_mass"] is True, "top mass scheme missing")
    require(target["target_identified"] is True, "target not identified")
    require(target["selected_same_branch_source_closed"] is False, "target overclosed source")
    require(target["closure_claimed"] is True, "target schema should close locally")

    require(
        gap["status"] == "SAME_BRANCH_TRUE_PRECISION_CONVENTION_SOURCE_OPEN",
        "gap status mismatch",
    )
    require(gap["firstpass_profile_layer_closed"] is True, "first-pass layer should be closed")
    require(gap["firstpass_accepted_for_profile_input"] is True, "first-pass profile input missing")
    require(gap["firstpass_accepted_for_true_precision"] is False, "first-pass precision overaccepted")
    require(gap["firstpass_is_not_true_precision"] is True, "first-pass rejection missing")
    require(gap["diagnostic_internal_rg_convergence_closed"] is True, "RG convergence missing")
    require(
        gap["diagnostic_engine_accepted_for_SM_parity_values"] is False,
        "diagnostic RG overaccepted",
    )
    require(
        gap["diagnostic_engine_not_accepted_as_true_precision_source"] is True,
        "diagnostic/source separation missing",
    )
    require(gap["common_scale_yukawa_higgs_values_emitted"] is False, "values overemitted")
    require(gap["accepted_threshold_mass_scheme_rows"] == 0, "accepted rows overclaimed")
    require(gap["finite_residual_table_present"] is True, "finite residual table missing")
    require(gap["finite_residual_table_is_not_source_rows"] is True, "residual source guard missing")
    require(
        gap["selected_same_branch_scale_scheme_loop_convention_closed"] is False,
        "same-branch convention overclosed",
    )
    require(gap["closure_claimed"] is False, "gap overclosed")

    require(
        order["status"] == "THRESHOLD_ROW_EMISSION_ORDERED_AFTER_CONVENTION_SOURCE",
        "order status mismatch",
    )
    require(order["can_emit_threshold_rows_now"] is False, "threshold rows overemitted")
    require(order["can_accept_external_rows_now"] is False, "external rows overaccepted")
    prereqs = order["ordered_prerequisites"]
    require(len(prereqs) == 5, "wrong prerequisite count")
    require(prereqs[0]["id"] == "selected_same_branch_convention_source", "convention source not first")
    require(prereqs[1]["id"] == "versioned_RG_engine_or_external_literature_benchmark", "RG benchmark not second")
    require(prereqs[2]["id"] == "threshold_matching_rows", "threshold rows not third")
    require(prereqs[3]["id"] == "mass_scheme_conversion_rows", "mass rows not fourth")
    require(prereqs[4]["id"] == "covariance_or_profile_response", "profile not fifth")
    for row in prereqs:
        require(row["closed"] is False, f"prerequisite overclosed: {row['id']}")
    require(order["closure_claimed"] is False, "order overclosed")

    require(decision["status"] == "CONVENTION_TARGET_CLOSED_SOURCE_AND_ROWS_OPEN", "decision status mismatch")
    require(decision["convention_target_identified"] is True, "decision target missing")
    for key in [
        "same_branch_true_precision_convention_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "external_likelihood_workspace_acquired",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(decision[key] is False, f"decision overclaimed: {key}")
    for key in [
        "true_precision_convention_target_schema",
        "firstpass_profile_convention_rejected_for_true_precision",
        "diagnostic_RG_convergence_separated_from_selected_convention_source",
        "threshold_row_prerequisite_order",
    ]:
        require(decision["what_closes_now"][key] is True, f"closed flag missing: {key}")
    for key in [
        "selected_same_branch_convention_source",
        "versioned_RG_engine_or_external_literature_benchmark",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "covariance_or_profile_response",
    ]:
        require(key in decision["remaining_hard_failures"], f"remaining failure missing: {key}")
    require(decision["next_required_artifact"] == NEXT, "decision next mismatch")

    closure = data["closure_decision"]
    require(closure["true_precision_convention_target_identified"] is True, "candidate target not closed")
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "profile_response_or_diagonal_limitation_closed",
        "external_likelihood_workspace_acquired",
        "selected_threshold_response_functional_instantiated",
        "accepted_vsd02_source_rows_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")
    require("target scale/scheme                         : M_Z / MSbar" in note, "note missing target")
    require("same-branch convention closed               : false" in note, "note missing open convention")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
