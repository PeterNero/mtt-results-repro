"""Audit residual Weyl-polynomial source theorem attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"
WEYL_PACKET = (
    ROOT
    / "candidate_data"
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "residual_weyl_polynomial_decomposition.packet.json"
)
SELECTION_GATE = (
    ROOT
    / "candidate_data"
    / "selected_residual_weylpolynomial_source_theorem_attempt"
    / "canonical_residual_projector_selection_gate.packet.json"
)
CERT = ROOT / "certificates" / "selected_residual_weylpolynomial_source_theorem_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Residual_WeylPolynomial_Source_Theorem_Attempt_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_residual_weylpolynomial_source_theorem_attempt.py"

STATUS = "MTT_SELECTED_RESIDUAL_WEYLPOLYNOMIAL_SOURCE_THEOREM_ATTEMPT_BUILT_PROJECTOR_SELECTION_OPEN"
NEXT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"
TOL = 1e-9


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    weyl = load(WEYL_PACKET)
    gate = load(SELECTION_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(weyl["status"] == "EXACT_LOW_DEGREE_WEYL_POLYNOMIAL_DECOMPOSITION_COMPUTED", "Weyl packet status mismatch")
    require(weyl["source_level_weyl_carrier_selected"] is True, "Weyl carrier not attached")
    require(weyl["active_shift_selected"] is True, "active shift not attached")
    require(weyl["static_source_selector_selected"] is True, "source selector not attached")
    require(weyl["observed_data_used"] is False, "observed data used")
    require(weyl["target_fitting_used"] is False, "target fitting used")

    rz = weyl["decompositions"]["R_Z"]
    rx = weyl["decompositions"]["R_X"]
    require(rz["coefficient_count"] == 6, "R_Z coefficient count mismatch")
    require(rx["coefficient_count"] == 3, "R_X coefficient count mismatch")
    require(abs(rz["reconstruction_error_norm_sq"]) <= TOL, "R_Z reconstruction error")
    require(abs(rx["reconstruction_error_norm_sq"]) <= TOL, "R_X reconstruction error")
    require(abs(rz["norm_sq"] - 4.0) <= TOL, "R_Z norm mismatch")
    require(abs(rx["norm_sq"] - 2.0) <= TOL, "R_X norm mismatch")
    require("R_X" in weyl["exact_polynomial_form"], "R_X exact form missing")
    require("R_Z" in weyl["exact_polynomial_form"], "R_Z exact form missing")

    require(gate["status"] == "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN", "selection gate status mismatch")
    require(gate["current_decision"] == "SOURCE_CARRIER_AND_CANONICAL_POLYNOMIAL_CLOSED_PROJECTOR_SELECTION_OPEN", "selection decision mismatch")
    require(gate["if_projector_selection_theorem_is_supplied"]["SM_parity_dynamic_packet_closes"] is True, "SM parity implication missing")
    require(gate["if_projector_selection_theorem_is_supplied"]["no_knob_flavor_constants_derived"] is False, "no-knob overclaim")

    closes = data["what_closes_now"]
    for key in [
        "residuals_compressed_to_low_degree_weyl_polynomials",
        "source_level_weyl_carrier_attached",
        "canonical_trace_projector_target_identified",
        "Lane_A_reduced_to_projector_selection_theorem",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "canonical_residual_projector_selection_theorem",
        "selected_PhiFinC1_transfer_functor_on_residual_polynomial",
        "honest_selected_Galerkin_C1_value_run",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1",
        "SM_parity_dynamic_packet_closure",
        "full_no_knob_flavor_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    decision = data["promotion_decision"]
    for key in [
        "Lane_A_promoted",
        "canonical_residual_projector_promoted",
        "residual_weyl_polynomial_selected_as_dynamic_response",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["SM_parity_dynamic_packet_closure_claimed"] is False, "SM parity overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("Weyl polynomials" in note, "note missing Weyl polynomial result")
    require("projector" in note, "note missing projector gate")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
