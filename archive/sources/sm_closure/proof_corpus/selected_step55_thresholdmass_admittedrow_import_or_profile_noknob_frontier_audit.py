"""Audit Step55 threshold/mass admitted-row import / profile no-knob frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROW_IMPORT = PACKET_DIR / "step55_threshold_mass_admitted_row_import.packet.json"
ATOMIC_RECHECK = PACKET_DIR / "step55_atomic_route_recheck_after_threshold_mass.packet.json"
VALUE_RECHECK = PACKET_DIR / "step55_value_readiness_recheck_after_threshold_mass.packet.json"
CUTSET = PACKET_DIR / "step55_next_profile_noknob_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step55_ThresholdMassAdmittedRowImport_or_ProfileNoKnobFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP55_THRESHOLD_MASS_ADMITTED_ROWS_IMPORTED_PROFILE_NOKNOB_OPEN"
NEXT = "MTT_Selected_FullProfileOrDiagonalTheoremPostPi_or_NoKnobValueDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    row_import = load(ROW_IMPORT)
    atomic = load(ATOMIC_RECHECK)
    values = load(VALUE_RECHECK)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step55 theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for packet in [data, row_import, atomic, values, cutset, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(
        row_import["threshold_matching_source_rows_closed_at_admitted_external_tier"] is True,
        "threshold rows not imported",
    )
    require(
        row_import["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"] is True,
        "mass rows not imported",
    )
    require(row_import["admitted_threshold_row_count"] == 7, "threshold row count mismatch")
    require(row_import["admitted_mass_scheme_row_count"] == 3, "mass row count mismatch")
    require(row_import["accepted_internal_selected_Rtheta_row_count"] == 0, "internal rows overaccepted")
    require(row_import["closed_as_no_knob_Rtheta_derivation"] is False, "no-knob derivation overclosed")

    require(atomic["previous_closed_atomic_count"] == 2, "previous atomic count mismatch")
    require(atomic["closed_atomic_count"] == 4, "closed atomic count mismatch")
    require(atomic["required_atomic_count"] == 6, "required atomic count mismatch")
    for key in [
        "no_observed_selector_proof",
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows_admitted_external",
        "mass_scheme_conversion_source_rows_admitted_external",
    ]:
        require(key in atomic["closed_atomic_lemmas"], f"closed atomic lemma missing: {key}")
    require(atomic["remaining_atomic_failures"] == [
        "selected_response_functional_map",
        "profile_response_or_diagonal_limitation",
        "no_knob_value_derivation",
    ], "remaining atomic failures mismatch")
    require(atomic["external_likelihood_route_has_admitted_rows"] is True, "external row route not closed")
    require(atomic["external_likelihood_route_is_full_profile"] is False, "profile route overclosed")
    require(atomic["minimal_parameter_route_still_open"] is True, "minimal route overclosed")

    require(values["previous_present_count"] == 5, "previous readiness mismatch")
    require(values["present_count"] == 7, "present readiness mismatch")
    require(values["requirement_count"] == 9, "readiness requirement mismatch")
    require(values["retired_blocking_failures"] == [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
    ], "retired failures mismatch")
    require(values["blocking_failures"] == [
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ], "remaining value blockers mismatch")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
        "closure_claimed",
    ]:
        require(values[key] is False, f"value recheck overclosed: {key}")
    require(values["accepted_coefficient_value_count"] == 0, "coefficient values overaccepted")
    require(values["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")

    require(cutset["status"] == "NEXT_FRONTIER_PROFILE_OR_NOKNOB_VALUE_DERIVATION", "cutset status mismatch")
    for key in [
        "same_branch_scale_scheme_loop_convention",
        "threshold_matching_source_rows_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_at_admitted_external_tier",
        "Rtheta_readiness_present_count_advanced_to_7_of_9",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closure missing: {key}")
    for key in [
        "selected_internal_Rtheta_threshold_mass_derivation",
        "selected_threshold_response_functional_instantiated",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
        "numeric_Rtheta_coefficient_values",
        "lambda_H_value_execution",
        "Yukawa_mass_mixing_value_closure",
        "true_SM_equivalence",
    ]:
        require(cutset["still_open"][key] is True, f"cutset overclosed: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    decision = data["closure_decision"]
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "threshold_matching_source_rows_closed",
        "threshold_matching_source_rows_closed_at_admitted_external_tier",
        "mass_scheme_conversion_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    for key in [
        "selected_internal_Rtheta_threshold_mass_derivation_closed",
        "selected_threshold_response_functional_instantiated",
        "selected_value_evaluator_closed",
        "accepted_lambda_H_value",
        "no_knob_value_derivation_closed",
        "full_profile_likelihood_or_accepted_diagonal_theorem_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["Rtheta_readiness_present_count"] == 7, "candidate readiness mismatch")
    require(decision["Rtheta_readiness_requirement_count"] == 9, "candidate requirement mismatch")
    require(decision["accepted_external_threshold_row_count"] == 7, "candidate threshold count mismatch")
    require(decision["accepted_external_mass_scheme_row_count"] == 3, "candidate mass count mismatch")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "candidate internal rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(cert["closed_at_admitted_external_tier_only"] is True, "tier guard missing")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "threshold matching rows closed      : true",
        "mass-scheme conversion rows closed  : true",
        "closed tier                          : admitted external replay",
        "selected internal Rtheta rows        : 0",
        "Rtheta readiness                     : 7/9",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
