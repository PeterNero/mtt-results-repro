"""Audit Step54 same-branch convention import / threshold-mass rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step54_samebranch_convention_import_or_thresholdmassrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CONVENTION_IMPORT = PACKET_DIR / "step54_samebranch_convention_import.packet.json"
ATOMIC_RECHECK = PACKET_DIR / "step54_atomic_route_recheck_after_convention.packet.json"
VALUE_RECHECK = PACKET_DIR / "step54_value_execution_recheck_after_convention.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step54_SameBranchConventionImport_or_ThresholdMassRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP54_SAMEBRANCH_CONVENTION_IMPORTED_THRESHOLD_MASS_ROWS_OPEN"
NEXT = "MTT_Selected_ThresholdMatchingRowsPostPi_or_MassSchemeSourceRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    convention = load(CONVENTION_IMPORT)
    atomic = load(ATOMIC_RECHECK)
    values = load(VALUE_RECHECK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "Step54 theorem not proved")

    for packet in [data, convention, atomic, values, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require(convention["step53_atomic_routes_locked"] is True, "Step53 routes not imported")
    require(convention["same_branch_scale_scheme_loop_convention_closed"] is True, "convention not closed")
    require(convention["post_pi_formal_convention_source_contract_closed"] is True, "contract not closed")
    require(convention["target_scale"] == "M_Z", "target scale mismatch")
    require(convention["target_scheme"] == "MSbar", "target scheme mismatch")

    require(atomic["closed_atomic_lemmas"] == [
        "no_observed_selector_proof",
        "same_branch_scale_scheme_loop_convention",
    ], "closed atomic lemma list mismatch")
    require(atomic["previous_closed_atomic_count"] == 1, "previous atomic count mismatch")
    require(atomic["closed_atomic_count"] == 2, "closed atomic count mismatch")
    require(atomic["required_atomic_count"] == 6, "required atomic count mismatch")
    for key in [
        "selected_response_functional_map",
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "profile_response_or_diagonal_limitation",
    ]:
        require(key in atomic["remaining_atomic_failures"], f"remaining atomic failure missing: {key}")
    require(atomic["recommended_next"] == NEXT, "atomic next mismatch")
    require(atomic["external_likelihood_route_still_open"] is True, "external route overclosed")
    require(atomic["minimal_parameter_route_still_open"] is True, "parameter route overclosed")

    require(values["previous_present_count"] == 4, "previous readiness mismatch")
    require(values["present_count"] == 5, "present readiness mismatch")
    require(values["requirement_count"] == 9, "requirement count mismatch")
    require(values["retired_blocking_failure"] == "same_branch_scale_scheme_loop_convention", "wrong retired blocker")
    require(values["blocking_failures"] == [
        "threshold_matching_source_rows",
        "mass_scheme_conversion_source_rows",
        "no_knob_value_derivation",
        "full_profile_likelihood_or_accepted_diagonal_theorem",
    ], "blocking failures mismatch")
    for key in [
        "selected_threshold_response_functional_instantiated",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(values[key] is False, f"value recheck overclosed: {key}")
    require(values["accepted_internal_Rtheta_coefficient_row_count"] == 0, "Rtheta rows overaccepted")
    require(values["accepted_internal_scalar_row_count"] == 0, "scalar rows overaccepted")

    decision = data["closure_decision"]
    for key in [
        "same_branch_scale_scheme_loop_convention_closed",
        "post_pi_formal_convention_source_contract_closed",
    ]:
        require(decision[key] is True, f"candidate closure missing: {key}")
        require(cert[key] is True, f"certificate closure missing: {key}")
    require(decision["closed_atomic_count"] == 2, "candidate atomic count mismatch")
    require(decision["Rtheta_readiness_present_count"] == 5, "candidate readiness mismatch")
    require(decision["Rtheta_readiness_requirement_count"] == 9, "candidate requirement mismatch")
    for key in [
        "threshold_matching_source_rows_closed",
        "mass_scheme_conversion_source_rows_closed",
        "selected_threshold_response_functional_instantiated",
        "selected_lambda_H_row_closed",
        "minimal_parameter_closure_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "candidate Rtheta rows overaccepted")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(data["minimal_parameter_closure_claimed"] is False, "minimal closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    for phrase in [
        "same-branch convention closed          : true",
        "closed atomic lemmas                   : 2/6",
        "Rtheta readiness                       : 5/9",
        "accepted internal Rtheta rows          : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
