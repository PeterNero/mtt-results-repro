"""Audit q79/rank source formula for the integer sector correction."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourceintegersectoramplitudetheorem_or_q79rankrhoformula"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_FORMULA = PACKET_DIR / "q79_rank_source_formula.packet.json"
EXECUTION = PACKET_DIR / "integer_sector_amplitude_execution.packet.json"
DECISION = PACKET_DIR / "source_integer_sector_amplitude_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_Q79RankRhoFormula_v1.md"

STATUS = "MTT_SELECTED_SOURCEINTEGERSECTORAMPLITUDETHEOREM_BUILT_Q79_RANK_RHO_FORMULA_PPM_EXACTNESS_OPEN"
NEXT = "MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    formula = load(SOURCE_FORMULA)
    execution = load(EXECUTION)
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

    inputs = formula["selected_inputs"]
    q64 = inputs["q64"]
    q7 = inputs["q7"]
    q_mod = inputs["q_mod"]
    carrier_rank = inputs["carrier_rank"]
    projector_rank = inputs["projector_rank"]
    epsilon_theta = inputs["epsilon_theta"]
    s_beta = inputs["selected_s_beta"]
    require((q64, q7, q_mod) == (15, 2, 448), "q79 integers")
    require(inputs["q_residue_mod_448"] == 79, "q79 residue")
    require(inputs["q_mod_source"] == "finite quotient order named by q_mod_448 in the q79 bridge packet", "q modulus source")
    require((carrier_rank, projector_rank) == (3, 2), "qutrit ranks")
    require(inputs["phase_side"] == ["u", "e"], "phase side")
    require(inputs["shift_side"] == ["d", "nuD"], "shift side")
    require(formula["status"] == "Q79_RANK_SOURCE_FORMULA_CONSTRUCTED_FROM_SELECTED_INPUTS", "formula status")
    require(formula["observed_data_used_as_selector"] is False, "formula observed guard")
    require(formula["target_fitting_used"] is False, "formula fitting guard")

    rows = formula["derived_rows"]
    require(rows["integer_sector_shape"] == [17.0, 15.0, -21.0], "integer sector shape")
    require(rows["integer_shape_matches_prior_fitted_clue"] is True, "integer prior match")
    require(rows["curvature_ratio_formula"] == "carrier_rank/(q64-projector_rank*q7)", "ratio formula")
    require(abs(rows["curvature_ratio_value"] - (3.0 / 11.0)) < 1.0e-15, "ratio value")
    expected_rho = epsilon_theta * s_beta * carrier_rank * projector_rank * q64 * q64 / q_mod
    require(abs(rows["rho_value"] - expected_rho) < 1.0e-18, "rho formula")
    require(formula["law_status"]["closed_selected_inputs"] is True, "closed selected inputs")
    require(formula["law_status"]["finite_projected_curvature_amplitude_law_constructed_here"] is True, "law not constructed")
    require(formula["law_status"]["independent_variational_or_hym_source_law_already_in_prior_packets"] is False, "law overaccepted")

    lift = formula["sector_lift_rule"]
    require(lift["ell_s"] == {"u": 1, "d": 0, "e": 3}, "lift ell")
    require(lift["sigma_s"] == {"u": 1, "d": 1, "e": -1}, "lift sigma")
    require("charged_lepton_transpose" in lift["slot_evidence"]["e_gen3"]["scalar_coupling_slot"], "e transpose evidence")
    require("down_type" in lift["slot_evidence"]["d_gen3"]["scalar_coupling_slot"], "d down evidence")
    require("self_ladder" in lift["slot_evidence"]["u_gen3"]["scalar_coupling_slot"], "u self evidence")

    require(execution["status"] == "Q79_RANK_RHO_EXECUTED_PPM_RESIDUAL_REMAINS", "execution status")
    require(execution["sector_shape"] == [17.0, 15.0, -21.0], "execution sector shape")
    require(abs(execution["rho_source"] - expected_rho) < 1.0e-18, "execution rho")
    require(abs(execution["rho_relative_to_fitted_prior_minus_one"]) < 1.0e-6, "rho ppm fit")
    require(execution["remaining_max_abs_log_residual"] < 4.0e-6, "ppm residual")
    require(execution["remaining_max_abs_log_residual"] > 1.0e-12, "exactness should remain open")
    require(execution["remaining_worst_multiplicative_yukawa_error"] < 1.000004, "multiplicative residual")

    require(decision["status"] == "SOURCE_FORMULA_CONSTRUCTED_PPM_RESIDUAL_EXACTNESS_OPEN", "decision status")
    require(len(decision["closed_now"]) == 3, "closed-now count")
    require(len(decision["not_closed"]) == 3, "not-closed count")
    counts = decision["source_row_counts"]
    require(counts["constructed_integer_sector_shape_rows"] == 1, "integer constructed count")
    require(counts["constructed_curvature_ratio_rows"] == 1, "ratio constructed count")
    require(counts["constructed_rho_formula_rows"] == 1, "rho constructed count")
    require(counts["accepted_strict_exact_yukawa_value_rows"] == 0, "exact rows overaccepted")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "Yukawa rows overaccepted")
    acceptance = decision["acceptance"]
    require(acceptance["integer_sector_shape_source_constructed"] is True, "integer not constructed")
    require(acceptance["curvature_ratio_source_constructed"] is True, "ratio not constructed")
    require(acceptance["rho_formula_uses_only_selected_inputs"] is True, "rho selected inputs")
    require(acceptance["rho_formula_ppm_success"] is True, "rho ppm success")
    require(acceptance["residual_exactness_closed"] is False, "exactness overclosed")
    require(acceptance["strict_no_knob_yukawa_closure"] is False, "strict closure overclaimed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclaimed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    theorem = data["theorem"]
    require(theorem["name"] == "Q79RankIntegerSectorAmplitudeSourceFormulaTheorem", "theorem name")
    require(theorem["proved"] is False, "theorem overproved")
    require(theorem["open_sublemma"] == "finite projected curvature-amplitude law from the same selected HYM/retarded-overlap source", "open sublemma")
    closure = data["closure_decision"]
    require(closure["residual_exactness_closed"] is False, "candidate exactness overclosed")
    require(closure["strict_no_knob_yukawa_closure"] is False, "candidate no-knob overclosed")

    require(cert["integer_sector_shape_source_constructed"] is True, "cert integer")
    require(cert["curvature_ratio_source_constructed"] is True, "cert ratio")
    require(cert["rho_formula_uses_only_selected_inputs"] is True, "cert rho")
    require(cert["rho_formula_ppm_success"] is True, "cert ppm")
    require(cert["residual_exactness_closed"] is False, "cert exactness")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert closure")
    require(cert["accepted_full_no_knob_yukawa_rows"] == 0, "cert row count")

    for phrase in [
        "`[17,15,-21] = [q64+q7, q64, -(q64+carrier_rank*q7)]`",
        "`3/11 = carrier_rank/(q64-projector_rank*q7)`",
        "`rho = epsilon_theta * s_beta * carrier_rank * projector_rank * q64^2 / q`",
        "not yet full strict Yukawa closure",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    # Keep a concrete numeric sanity check so future refactors cannot preserve
    # only the text while changing the source arithmetic.
    require(math.isclose(execution["rho_source"], 2.6454590873348714e-05, rel_tol=0.0, abs_tol=1.0e-18), "rho numeric")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
