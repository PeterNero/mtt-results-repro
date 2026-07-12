"""Audit Step 42 executable value replay solution and no-knob boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step42_executable_value_replay_solution_or_noknobrowfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUE_SOLUTION = PACKET_DIR / "step42_executable_value_replay_solution.packet.json"
NOKNOB_FRONTIER = PACKET_DIR / "step42_noknob_internal_row_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step42_ExecutableValueReplaySolution_or_NoKnobRowFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP42_EXECUTABLE_VALUE_REPLAY_SOLUTION_ASSEMBLED_NOKNOB_ROWS_OPEN"
NEXT = "MTT_Selected_InternalRThetaCoefficientRows_or_UniversalAnchorTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    solution = load(VALUE_SOLUTION)
    frontier = load(NOKNOB_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(solution["status"] == "EXECUTABLE_ADMITTED_REPLAY_VALUE_SOLUTION_ASSEMBLED", "solution status mismatch")

    for packet in [data, solution, frontier, cert]:
        require(packet.get("target_fitting_used") is False, "target fitting violation")
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")

    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")

    branch = solution["selected_source_branch"]
    require(branch["q"] == 79, "wrong q branch")
    require(branch["orientation"] == "F", "wrong orientation")
    require(branch["torsion_m"] == 1, "wrong torsion")

    rows = solution["value_rows"]
    require(rows["reference_scale"] == "M_Z", "reference scale mismatch")
    require(len(rows["diag_abs_Y_u"]) == 3, "Y_u diagonal length mismatch")
    require(len(rows["diag_abs_Y_d"]) == 3, "Y_d diagonal length mismatch")
    require(len(rows["diag_abs_Y_e"]) == 3, "Y_e diagonal length mismatch")
    require(rows["lambda_H"] > 0, "lambda_H not positive")
    require(rows["Y_u_MZ_firstpass"][2][2][0] > 1.0, "top Yukawa row missing")

    for key, value in solution["replay_checks"].items():
        require(value is True, f"replay check failed: {key}")

    acceptance = solution["row_acceptance"]
    require(acceptance["accepted_for_SM_parity"] is True, "SM parity value row not accepted")
    require(acceptance["accepted_for_profile_execution_input"] is True, "profile input not accepted")
    require(acceptance["accepted_for_true_precision_equivalence"] is False, "true precision overaccepted")
    require(acceptance["accepted_as_no_knob_MTT_prediction"] is False, "no-knob row overaccepted")
    require(acceptance["accepted_internal_scalar_row_count"] == 0, "internal scalar rows overaccepted")

    support = solution["admitted_replay_support"]
    require(support["admitted_external_threshold_row_count"] == 7, "threshold row count mismatch")
    require(support["admitted_external_mass_scheme_row_count"] == 3, "mass row count mismatch")
    require(support["accepted_diagonal_profile_theorem_closed_at_replay_tier"] is True, "diagonal profile missing")
    require(support["Rtheta_readiness_8_of_9"] is True, "Rtheta readiness missing")

    decision = data["closure_decision"]
    for key in [
        "executable_admitted_replay_value_solution_closed",
        "Step41_source_branch_attached_to_value_rows",
        "versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted",
        "admitted_external_threshold_rows_closed",
        "admitted_external_mass_scheme_rows_closed",
        "diagonal_profile_replay_tier_closed",
        "Pi_Rtheta_closed",
        "Rtheta_readiness_8_of_9",
        "accepted_for_SM_parity",
        "accepted_for_profile_execution_input",
    ]:
        require(decision[key] is True, f"decision close missing: {key}")
        require(cert[key] is True, f"certificate close missing: {key}")

    require(decision["admitted_external_threshold_row_count"] == 7, "candidate threshold count mismatch")
    require(decision["admitted_external_mass_scheme_row_count"] == 3, "candidate mass count mismatch")
    for key in [
        "accepted_for_true_precision_equivalence",
        "accepted_as_no_knob_MTT_prediction",
        "selected_internal_Rtheta_coefficient_rows_closed",
        "selected_lambda_H_row_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_internal_scalar_row_count"] == 0, "candidate scalar rows overaccepted")
    require(decision["accepted_coefficient_value_count"] == 0, "candidate coefficients overaccepted")

    closed = frontier["closed_now"]
    for key in [
        "executable_admitted_replay_value_solution_closed",
        "Step41_source_branch_attached_to_value_rows",
        "versioned_common_scale_Yu_Yd_Ye_lambdaH_rows_emitted",
        "admitted_external_threshold_rows_closed",
        "admitted_external_mass_scheme_rows_closed",
        "diagonal_profile_replay_tier_closed",
        "Pi_Rtheta_closed",
        "Rtheta_readiness_8_of_9",
    ]:
        require(closed[key] is True, f"frontier close missing: {key}")

    open_rows = frontier["still_open_for_full_closure"]
    require(open_rows["selected_internal_Rtheta_coefficient_rows"] is True, "internal row frontier missing")
    require(open_rows["selected_threshold_response_functional_instantiated"] is True, "threshold frontier missing")
    require(open_rows["selected_value_evaluator_closed"] is True, "value evaluator frontier missing")
    require(open_rows["accepted_coefficient_value_count"] == 0, "frontier coefficient count mismatch")
    require(open_rows["accepted_internal_scalar_row_count"] == 0, "frontier scalar count mismatch")
    require(open_rows["accepted_lambda_H_value"] is False, "lambda_H overaccepted")
    require(open_rows["true_SM_equivalence_closed"] is False, "frontier true SM overclosed")
    require(open_rows["full_no_knob_closed"] is False, "frontier no-knob overclosed")
    require(frontier["next_required_payload"]["target"] == NEXT, "frontier next mismatch")

    for phrase in [
        "one executable value solution tier",
        "q=79",
        "Y_u(M_Z)",
        "accepted internal scalar rows: `0`",
        "true SM equivalence: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
