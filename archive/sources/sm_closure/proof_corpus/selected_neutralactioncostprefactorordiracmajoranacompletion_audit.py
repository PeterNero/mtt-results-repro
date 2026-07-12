from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralactioncostprefactorordiracmajoranacompletion"
STATUS = "MTT_SELECTED_NEUTRAL_RELATIVE_AMPLITUDE_ORBIT_CLOSED_ABSOLUTE_ACTION_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "neutral_second_order_relative_amplitude_orbit.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(packet["observed_data_used_as_selector"] is False and packet["target_fitting_used"] is False, "empirical selector used")
    require(packet["orbit_representative_count"] == 2, "orbit count changed")
    require(packet["relative_value_rows_closed"] == 18, "relative row count changed")
    require({row["lambda_static"] for row in packet["selected_relative_amplitude_orbit"]} == {"1+omega", "1+omega2"}, "lambda orbit changed")
    require(all(row["exact_matrix_match"] for row in packet["selected_relative_amplitude_orbit"]), "matrix mismatch")
    require({row["cyclic_shift_phase"] for row in packet["selected_relative_amplitude_orbit"]} == {"+pi/6", "-pi/6"}, "phase orbit changed")
    require(all(row["cyclic_shift_magnitude_exact"] == "sqrt(3)" for row in packet["selected_relative_amplitude_orbit"]), "magnitude changed")
    require(all(row["hermitian_spectrum"] == [1.0, 4.0, 7.0] for row in packet["selected_relative_amplitude_orbit"]), "spectrum changed")

    closes = packet["what_closes_here"]
    require(closes["selected_second_order_neutral_relative_amplitude_orbit"] is True, "relative orbit open")
    require(closes["relative_magnitude_and_phase_orbit"] is True, "relative values open")
    for key in ["individual_orbit_representative", "neutral_action_cost_rows_S_gamma", "absolute_prefactors_A_gamma", "unique_retarded_sign_row", "Dirac_only_action_completeness", "physical_Gamma_nu_amplitudes"]:
        require(closes[key] is False, f"overclosed: {key}")

    require(packet["neutral_overlap_OK_gates_closed"] == 6 and packet["neutral_overlap_OK_gates_total"] == 9, "OK count changed")
    require(packet["readiness_subfields_closed"] == 8 and packet["readiness_subfields_total"] == 13, "readiness changed")
    require(packet["new_absolute_value_fields_closed_here"] == 0, "absolute value overclosed")
    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    for field in ["dimensionful_M_D_3x3_closed", "dimensionful_M_L_3x3_closed", "dimensionful_M_R_3x3_closed", "absolute_normalization_and_scheme_closed", "selected_neutral_operator_accepted", "U5_closed"]:
        require(packet[field] is False and cert[field] is False, f"overclosed: {field}")
    for phrase in ["3/2 + i sqrt(3)/2", "magnitude `sqrt(3)`", "`+pi/6` or `-pi/6`", "not `OK6`", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"relative_rows": "18/18 over two representatives", "shift_magnitude": "sqrt(3)", "phase_orbit": ["+pi/6", "-pi/6"], "absolute_value_fields": 0, "neutral_OK_gates": "6/9", "next": NEXT}, indent=2))
    print("selected neutral relative amplitude orbit audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
