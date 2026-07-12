"""Audit strict phase-antisymmetry scalar derivation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DERIVATION = PACKET_DIR / "strict_phase_antisymmetry_scalar_derivation.packet.json"
REPLAY = PACKET_DIR / "strict_scalar_yukawa_replay.packet.json"
DECISION = PACKET_DIR / "noknob_yukawa_exactness_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPhaseAntisymmetryScalarDerivation_or_NoKnobYukawaExactness_v1.md"

STATUS = "MTT_SELECTED_STRICTPHASEANTISYMMETRYSCALARDERIVATION_BUILT_SCALAR_SOURCE_CLOSED_YUKAWA_EXACTNESS_OPEN"
NEXT = "MTT_Selected_FinalYukawaReplayResidualExactness_or_StrictSMNoKnobClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    derivation = load(DERIVATION)
    replay = load(REPLAY)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(derivation["status"] == "STRICT_Q64_SBETA_PHASE_ANTISYMMETRY_SCALAR_DERIVED", "derivation status")
    require(derivation["observed_data_used_as_selector"] is False, "derivation observed selector")
    require(derivation["target_fitting_used"] is False, "derivation target fitting")
    require(derivation["all_derivation_clauses_closed"] is True, "derivation clauses not closed")
    clauses = derivation["derivation_clauses"]
    for key in [
        "same_source_dynamic_overlap_packet",
        "charged_retarded_overlap_family",
        "charged_hym_overlap_rows",
        "phase_lane_u_e",
        "transpose_antisymmetry_sign",
        "retarded_q64_denominator",
        "one_circle_endpoint_unit",
        "hym_projection_angle",
    ]:
        require(clauses[key]["closed"] is True, f"clause not closed: {key}")
    require(clauses["phase_lane_u_e"]["phase_side"] == ["u", "e"], "phase side")
    require(clauses["transpose_antisymmetry_sign"]["sigma_e"] == -1, "transpose sign")
    require(clauses["retarded_q64_denominator"]["q64"] == 15, "q64")
    require(abs(clauses["hym_projection_angle"]["s_beta"] - 0.004701083905943647) < 1.0e-18, "s_beta")

    formula = derivation["derived_formula"]
    require(formula["central_circle_ratio"] == "(q64+1)/q64", "central ratio")
    require(formula["delta_c2_formula"] == "-((q64+1)/q64) * s_beta", "delta formula")
    require(abs(formula["delta_c2_value"] - (-0.005014489499673223)) < 1.0e-18, "delta value")
    require(abs(formula["residual_operator_coefficient"] - (-4.402222824618228e-08)) < 1.0e-20, "coefficient")
    matches = derivation["matches_previous_candidate"]
    require(abs(matches["delta_c2_difference"]) < 1.0e-24, "delta mismatch")
    require(abs(matches["coefficient_difference"]) < 1.0e-24, "coefficient mismatch")
    source_status = derivation["source_status"]
    require(source_status["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "source theorem")
    require(source_status["free_scalar_parameter_introduced"] is False, "free scalar introduced")
    require(source_status["observed_yukawa_values_used_to_select_scalar"] is False, "observed values used")

    require(replay["status"] == "STRICT_SCALAR_REPLAY_EXECUTED_NONZERO_RESIDUAL_REMAINS", "replay status")
    require(replay["observed_data_used_as_selector"] is False, "replay observed selector")
    require(replay["target_fitting_used"] is False, "replay target fitting")
    require(replay["operator"]["family_shape_Q"] == [-2.0, 3.0, -1.0], "replay Q")
    require(replay["operator"]["sector_operator_vector"] == [27.0, 6.0, 26.0], "replay vector")
    metrics = replay["replay_metrics"]
    require(metrics["remaining_max_abs_log_residual"] < 8.0e-9, "replay bound")
    require(abs(metrics["remaining_max_abs_log_residual"] - 7.959463247076742e-09) < 1.0e-20, "replay max")
    require(metrics["remaining_worst_multiplicative_yukawa_error"] < 1.000000008, "replay factor")
    require(replay["exact_zero_residual"] is False, "replay overclosed")

    require(
        decision["status"] == "STRICT_PHASE_SCALAR_SOURCE_CLOSED_FINAL_REPLAY_EXACTNESS_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "strict scalar count")
    require(counts["accepted_bounded_error_certificates_for_yukawa_replay"] == 1, "bounded count")
    require(counts["accepted_exact_yukawa_magnitude_rows"] == 0, "exact rows overaccepted")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "no-knob rows overaccepted")
    acceptance = decision["acceptance"]
    require(acceptance["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "accept theorem")
    require(acceptance["fitted_phase_split_retired_as_source_input"] is True, "fitted split not retired")
    require(acceptance["q64_sbeta_scalar_uses_only_selected_inputs"] is True, "selected input")
    require(acceptance["ultratight_error_certificate_accepted"] is True, "bounded cert")
    require(acceptance["strict_exactness_closed"] is False, "strict exactness overclosed")
    require(acceptance["strict_no_knob_yukawa_closure"] is False, "no-knob overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "StrictPhaseAntisymmetryQ64SBetaScalarSourceTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_decision"] == acceptance, "candidate closure copy")
    require(cert["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "cert theorem")
    require(cert["fitted_phase_split_retired_as_source_input"] is True, "cert retire")
    require(cert["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "cert scalar count")
    require(cert["accepted_exact_yukawa_magnitude_rows"] == 0, "cert exact rows")
    require(cert["strict_exactness_closed"] is False, "cert exactness")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert no-knob")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    for phrase in [
        "`delta_c2 = -((q64+1)/q64) * s_beta",
        "retired as a source input",
        "bounded-error certificate below `8e-9` remains accepted",
        "exact zero-residual Yukawa replay",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
