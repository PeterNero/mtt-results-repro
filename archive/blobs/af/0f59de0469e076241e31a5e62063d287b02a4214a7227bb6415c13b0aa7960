"""Audit finite-projected curvature-amplitude lockdown."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LAW = PACKET_DIR / "finite_projected_curvature_amplitude_law_lock.packet.json"
RESIDUAL = PACKET_DIR / "remaining_yukawa_residual_lockdown.packet.json"
DECISION = PACKET_DIR / "yukawa_exactness_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteProjectedCurvatureAmplitudeLaw_or_YukawaExactnessClosure_v1.md"

STATUS = "MTT_SELECTED_FINITEPROJECTEDCURVATUREAMPLITUDELAW_LOCKED_SOURCE_FORMULA_EXACTNESS_OPEN"
NEXT = "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    law = load(LAW)
    residual = load(RESIDUAL)
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

    require(law["status"] == "SOURCE_FORMULA_LOCKED_FINITE_EXACTNESS_AVAILABLE_BUT_NOT_YUKAWA_EXACTNESS", "law status")
    selected = law["selected_source_formula"]
    require(selected["sector_shape"] == [17.0, 15.0, -21.0], "sector shape")
    require(abs(selected["curvature_ratio"] - (3.0 / 11.0)) < 1.0e-15, "curvature ratio")
    require(abs(selected["rho"] - 2.6454590873348714e-05) < 1.0e-18, "rho")
    support = law["finite_projected_source_support"]
    require(support["A_N_exactness_closed"] is True, "A_N exactness")
    require(support["finite_projected_HYM_source_principle_closed"] is True, "finite HYM source")
    require(support["H_scalar_functional_on_A_N_closed"] is True, "H scalar")
    require(support["strict_tau_H_promoted"] is True, "tau_H")
    require(support["strict_r_H_promoted"] is True, "r_H")
    require(law["lockdown_theorem"]["proved"] is True, "lockdown theorem")

    require(residual["status"] == "PPM_RESIDUAL_LOCALIZED_NO_ACCEPTED_SOURCE_CORRECTION", "residual status")
    require(residual["family_shape_Q_retained"] == [-2.0, 3.0, -1.0], "family Q")
    require(residual["remaining_max_abs_log_residual"] > 3.5e-6, "residual lower")
    require(residual["remaining_max_abs_log_residual"] < 3.6e-6, "residual upper")
    require(residual["remaining_worst_multiplicative_yukawa_error"] < 1.000004, "multiplicative upper")
    require(residual["too_large_for_existing_finite_replay_floor"] is True, "floor guard")
    require(residual["residual_floor_ratio"] > 1.0e6, "floor ratio")
    trials = residual["diagnostic_correction_trials"]
    require(trials["carrier_boundary_27_6_26"]["vector"] == [27.0, 6.0, 26.0], "27/6/26 vector")
    require(trials["carrier_boundary_27_6_26"]["accepted_as_source_correction"] is False, "27/6/26 overaccepted")
    require(trials["carrier_boundary_27_6_26"]["max_abs_remaining_sector_amplitude"] < 3.0e-9, "27/6/26 diagnostic changed")
    for trial in trials.values():
        require(trial["accepted_as_source_correction"] is False, "diagnostic overaccepted")

    require(decision["status"] == "SOURCE_LAW_LOCKED_EXACT_YUKAWA_MAGNITUDE_CLOSURE_OPEN", "decision status")
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["locked_q79_rank_amplitude_laws"] == 1, "locked law count")
    require(counts["accepted_residual_correction_rows"] == 0, "residual rows overaccepted")
    require(counts["accepted_exact_yukawa_magnitude_rows"] == 0, "exact rows overaccepted")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "no-knob rows overaccepted")
    acceptance = decision["acceptance"]
    require(acceptance["finite_projected_curvature_amplitude_law_locked"] is True, "law locked")
    require(acceptance["finite_cutoff_exactness_blocker_retired_for_A_N"] is True, "finite cutoff")
    require(acceptance["yukawa_specific_exactness_closed"] is False, "Yukawa exactness overclosed")
    require(acceptance["ppm_residual_promoted_by_error_certificate"] is False, "error cert overclosed")
    require(acceptance["strict_no_knob_yukawa_closure"] is False, "strict closure overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "FiniteProjectedCurvatureAmplitudeLawLockdownTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "theorem proved")
    closure = data["closure_decision"]
    require(closure["finite_projected_curvature_amplitude_law_locked"] is True, "candidate law locked")
    require(closure["yukawa_specific_exactness_closed"] is False, "candidate exactness overclosed")
    require(closure["strict_no_knob_yukawa_closure"] is False, "candidate no-knob overclosed")

    require(cert["finite_projected_curvature_amplitude_law_locked"] is True, "cert law")
    require(cert["finite_cutoff_exactness_blocker_retired_for_A_N"] is True, "cert finite")
    require(cert["yukawa_specific_exactness_closed"] is False, "cert exactness")
    require(cert["accepted_residual_correction_rows"] == 0, "cert residual rows")
    require(cert["accepted_exact_yukawa_magnitude_rows"] == 0, "cert exact rows")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert no-knob")

    for phrase in [
        "`rho = 2.6454590873348714e-05`",
        "finite cutoff approximation",
        "`[27,6,26]`",
        "not emitted by a selected Yukawa/HYM operator",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
