"""Audit lambda-orbit second-order matrix packet or Rtheta scalar execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX_PACKET = PACKET_DIR / "lambda_orbit_second_order_matrix_packet.packet.json"
QUALITATIVE = PACKET_DIR / "second_order_orbit_qualitative_sm_tests.packet.json"
SCALAR_GATE = PACKET_DIR / "rtheta_scalar_execution_gate_after_second_order_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_order_orbit_matrix_packet.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LambdaOrbitSecondOrderMatrixPacket_or_RThetaScalarExecution_v1.md"

STATUS = (
    "MTT_SELECTED_LAMBDAORBITSECONDORDERMATRIXPACKET_OR_RTHETASCALAREXECUTION_"
    "BUILT_SECOND_ORDER_ORBIT_MATRIX_PACKET_SCALARS_OPEN"
)
NEXT = "MTT_Selected_SecondOrderOrbitQualitativeSMClosure_or_RThetaScalarValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    matrix = load(MATRIX_PACKET)
    qualitative = load(QUALITATIVE)
    scalar = load(SCALAR_GATE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(matrix, errors, "matrix_packet", closure=True)
    guard(qualitative, errors, "qualitative", closure=True)
    guard(scalar, errors, "scalar_gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    expect(matrix.get("orbit_matrix_packet_selected") is True, "matrix packet not selected", errors)
    expect(matrix.get("individual_lambda_selected") is False, "individual lambda overselected", errors)
    expect(matrix.get("selected_branch_ids") == [
        "phase_lambda_1+omega__shift_lambda_1+omega",
        "phase_lambda_1+omega2__shift_lambda_1+omega2",
    ], "branch ids mismatch", errors)
    expect(len(matrix.get("matrix_branches", [])) == 2, "matrix branch count mismatch", errors)
    for branch in matrix.get("matrix_branches", []):
        expect(branch.get("hermitian_spectrum_each_sector") == [1.0, 4.0, 7.0], f"spectrum mismatch {branch.get('branch_id')}", errors)
        expect(branch.get("commutator_norm_sq") == 324.0, f"commutator mismatch {branch.get('branch_id')}", errors)
        expect(branch.get("cp_odd_exact_magnitude") == "972*sqrt(3)", f"CP magnitude mismatch {branch.get('branch_id')}", errors)
        expect(branch.get("cp_odd_orientation") == "positive", f"CP orientation mismatch {branch.get('branch_id')}", errors)

    expect(qualitative.get("all_orbit_representatives_split_three_families") is True, "splitting not closed", errors)
    expect(qualitative.get("all_orbit_representatives_emit_nonzero_CP_odd_invariant") is True, "CP not closed", errors)
    expect(qualitative.get("all_selected_orbit_representatives_positive_orientation") is True, "orientation not positive", errors)
    expect(qualitative.get("twofold_first_response_degeneracy_removed") is True, "twofold degeneracy not removed", errors)
    for key in [
        "measured_Yukawa_magnitudes",
        "CKM_PMNS_measured_angles",
        "lambda_H_value",
        "threshold_mass_scheme_values",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(qualitative.get("what_this_does_not_close", {}).get(key) is True, f"qualitative guard missing: {key}", errors)

    expect(scalar.get("second_order_orbit_matrix_packet_closed") is True, "scalar gate did not import matrix packet", errors)
    expect(scalar.get("codomain_scalar_row_count") == 10, "scalar row count mismatch", errors)
    expect(scalar.get("execution_inputs_available_now") is False, "execution inputs overclaimed", errors)
    expect(scalar.get("selected_functional_executed") is False, "functional overexecuted", errors)
    expect(scalar.get("accepted_scalar_row_count_now") == 0, "scalar rows overaccepted", errors)
    expect(scalar.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "selected_second_order_orbit_matrix_packet",
        "three_family_splitting_at_orbit_layer",
        "nonzero_CP_at_orbit_layer",
        "first_response_twofold_degeneracy_removed",
        "individual_lambda_selection_not_forced",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "higher_response_Rtheta_scalar_rows",
        "accepted_Yukawa_magnitudes",
        "CKM_PMNS_measured_values",
        "lambda_H_value_execution",
        "threshold_mass_scheme_values",
        "individual_lambda_representative_after_scalar_execution",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"remaining blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    for key in [
        "selected_second_order_orbit_matrix_packet_closed",
        "qualitative_three_family_splitting_closed",
        "qualitative_CP_nonzero_closed",
    ]:
        expect(decision.get(key) is True, f"decision close missing: {key}", errors)
        expect(cert.get(key) is True, f"certificate close missing: {key}", errors)
    for key in [
        "individual_lambda_representative_selected",
        "higher_response_Rtheta_scalar_rows_executed",
        "accepted_value_layer_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("three-family splitting           : true" in note, "note missing splitting", errors)
    expect("accepted scalar value layer" not in note, "note overclaims scalar layer", errors)

    if errors:
        print("Lambda orbit second-order matrix audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Lambda orbit second-order matrix audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
