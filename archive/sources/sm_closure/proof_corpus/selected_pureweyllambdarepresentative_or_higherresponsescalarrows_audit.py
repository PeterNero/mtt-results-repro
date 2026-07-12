"""Audit pure-Weyl lambda representative or higher-response scalar rows gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ORBIT_PACKET = PACKET_DIR / "selected_lambda_orbit_scaled_pure_weyl_rows.packet.json"
COEXISTENCE = PACKET_DIR / "lambda_orbit_coexistence_theorem.packet.json"
SCALAR_GATE = PACKET_DIR / "higher_response_scalar_rows_after_lambda_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_lambda_orbit_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1.md"

STATUS = (
    "MTT_SELECTED_PUREWEYLLAMBDAREPRESENTATIVE_OR_HIGHERRESPONSESCALARROWS_"
    "BUILT_LAMBDA_ORBIT_ROWS_CLOSED_SCALARS_OPEN"
)
NEXT = "MTT_Selected_LambdaOrbitSecondOrderMatrixPacket_or_RThetaScalarExecution_v1"


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
    orbit = load(ORBIT_PACKET)
    coexistence = load(COEXISTENCE)
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
    guard(orbit, errors, "orbit_packet", closure=True)
    guard(coexistence, errors, "coexistence", closure=True)
    guard(scalar, errors, "scalar_gate", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    expect(orbit.get("status") == "LAMBDA_ORBIT_SCALED_PURE_WEYL_ROWS_CLOSED", "orbit status mismatch", errors)
    expect(orbit.get("lambda_orbit") == ["1+omega", "1+omega2"], "lambda orbit mismatch", errors)
    expect(orbit.get("representative_count") == 2, "representative count mismatch", errors)
    expect(orbit.get("individual_lambda_selected") is False, "individual lambda overselected", errors)
    expect(orbit.get("orbit_selected") is True, "orbit not selected", errors)
    family = orbit.get("scaled_row_family", {})
    expect(family.get("unscaled_R_Z_row_count") == 18, "R_Z count mismatch", errors)
    expect(family.get("unscaled_R_X_row_count") == 18, "R_X count mismatch", errors)
    expect(family.get("scaled_rows_per_representative") == 36, "scaled rows per representative mismatch", errors)
    expect(family.get("orbit_scaled_row_count") == 72, "orbit scaled row count mismatch", errors)

    expect(coexistence.get("conjugate_pair") is True, "conjugate pair missing", errors)
    comparison = coexistence.get("physical_signature_comparison", {})
    expect(comparison.get("same_hermitian_spectrum_each_sector") is True, "spectrum mismatch", errors)
    expect(comparison.get("hermitian_spectrum_each_sector") == [1.0, 4.0, 7.0], "spectrum value mismatch", errors)
    expect(comparison.get("same_cp_odd_exact_magnitude") is True, "CP magnitude mismatch", errors)
    expect(comparison.get("cp_odd_exact_magnitude") == "972*sqrt(3)", "CP magnitude value mismatch", errors)
    expect(comparison.get("same_cp_odd_orientation") is True, "CP orientation mismatch", errors)
    expect(comparison.get("cp_odd_orientation") == "positive", "CP orientation value mismatch", errors)
    for phrase in [
        "an individual representative is selected",
        "Yukawa magnitudes or CKM/PMNS measured values are derived",
        "lambda_H or threshold values are emitted",
    ]:
        expect(phrase in coexistence.get("what_this_does_not_prove", []), f"coexistence guard missing: {phrase}", errors)

    expect(scalar.get("lambda_orbit_scaled_pure_rows_available") is True, "lambda orbit not imported to scalar gate", errors)
    expect(scalar.get("codomain_scalar_row_count") == 10, "scalar row count mismatch", errors)
    expect(scalar.get("execution_inputs_available_now") is False, "execution inputs overclaimed", errors)
    expect(scalar.get("selected_functional_executed") is False, "functional overexecuted", errors)
    expect(scalar.get("accepted_scalar_row_count_now") == 0, "scalar rows overaccepted", errors)
    expect(scalar.get("lambda_H_row_emitted") is False, "lambda_H overemitted", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "lambda_static_orbit_selected",
        "lambda_orbit_scaled_pure_R_Z_rows",
        "lambda_orbit_scaled_pure_R_X_rows",
        "coexistence_theorem_current_invariant_layer",
        "individual_lambda_selection_not_forced",
    ]:
        expect(closed.get(key) is True, f"cutset close flag missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "individual_lambda_representative_selection",
        "selected_second_order_matrix_packet_from_orbit_rows",
        "higher_response_Rtheta_scalar_rows",
        "lambda_H_value_execution",
        "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"remaining blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    for key in [
        "lambda_static_orbit_selected",
        "lambda_orbit_scaled_pure_Weyl_rows_closed",
        "coexistence_theorem_current_invariant_layer_closed",
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

    expect("individual lambda selected        : false" in note, "note missing individual guard", errors)
    expect("orbit-scaled pure rows closed     : true" in note, "note missing orbit row closure", errors)
    expect("full no-knob" not in note or "full no-knob closure" not in note, "note wording too broad", errors)

    if errors:
        print("Pure-Weyl lambda representative audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Pure-Weyl lambda representative audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
