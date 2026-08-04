"""Audit phase-lane curvature residual exactness/source-correction rows."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phaselanecurvatureresidualexactness_or_sourcecorrectionrows"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FACTORIZATION = PACKET_DIR / "rank1_residual_family_shape_factorization.packet.json"
CORRECTIONS = PACKET_DIR / "source_correction_shape_trials.packet.json"
DECISION = PACKET_DIR / "residual_exactness_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhaseLaneCurvatureResidualExactness_or_SourceCorrectionRows_v1.md"

STATUS = "MTT_SELECTED_PHASELANECURVATURERESIDUALEXACTNESS_OR_SOURCECORRECTIONROWS_BUILT_RANK1_SHAPE_INTEGER_CLUE_SOURCE_OPEN"
NEXT = "MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_GammaCorrectionRows_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    factorization = load(FACTORIZATION)
    corrections = load(CORRECTIONS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is True, "candidate observed selector")
    require(data["target_fitting_used"] is True, "candidate target fitting")

    require(data["theorem"]["name"] == "PhaseLaneCurvatureResidualFamilyShapeTheorem", "theorem name")
    require(data["theorem"]["proved"] is True, "shape theorem not proved")

    require(factorization["status"] == "RANK1_FAMILY_SHAPE_FACTORIZATION_EXACT", "factorization status")
    require(factorization["family_shape_Q"] == [-2.0, 3.0, -1.0], "family shape")
    checks = factorization["family_shape_checks"]
    require(abs(checks["sum_Q"]) < 1.0e-12, "Q sum")
    require(abs(checks["dot_Q_family_eigenvalues"]) < 1.0e-12, "Q dot F")
    require(checks["orthogonal_to_affine_family_basis"] is True, "Q affine complement")
    require(factorization["residual_rank"] == 1, "rank")
    require(factorization["max_abs_factorization_error"] < 1.0e-12, "factorization error")
    require(factorization["accepted_as_exact_shape_theorem"] is True, "shape not accepted")
    require(factorization["accepted_as_numeric_source_rows"] is False, "numeric rows overaccepted")

    require(corrections["status"] == "SOURCE_CORRECTION_SHAPE_TRIALS_EXECUTED_SOURCE_OPEN", "corrections status")
    require(corrections["best_compressive_clue"] == "one_amplitude_integer_17_15_minus21", "best clue")
    exact = corrections["trials"]["exact_three_eta"]
    require(exact["parameter_count"] == 3, "exact eta count")
    require(exact["remaining_max_abs_log_residual"] < 1.0e-12, "exact eta should close arithmetic")
    require(exact["accepted_as_source_row"] is False, "exact eta overaccepted")

    quark = corrections["trials"]["one_amplitude_quark_lepton_sign"]
    require(quark["sector_shape"] == [1.0, 1.0, -1.0], "quark/lepton sector shape")
    require(quark["remaining_worst_multiplicative_yukawa_error"] < 1.0003, "quark/lepton clue too weak")
    require(quark["accepted_as_source_row"] is False, "quark/lepton overaccepted")

    integer = corrections["trials"]["one_amplitude_integer_17_15_minus21"]
    require(integer["sector_shape"] == [17.0, 15.0, -21.0], "integer sector shape")
    require(integer["remaining_worst_multiplicative_yukawa_error"] < 1.000004, "integer clue too weak")
    require(integer["remaining_max_abs_log_residual"] < 4.0e-6, "integer residual too large")
    require(integer["accepted_as_source_row"] is False, "integer overaccepted")
    require(integer["observed_data_used_as_selector"] is True, "integer observed guard")
    require(integer["target_fitting_used"] is True, "integer target guard")

    two = corrections["trials"]["two_amplitude_quark_common_lepton"]
    require(two["parameter_count"] == 2, "two-param count")
    require(two["remaining_worst_multiplicative_yukawa_error"] < 1.00008, "two-param clue too weak")
    require(two["accepted_as_source_row"] is False, "two-param overaccepted")

    require(decision["status"] == "RANK1_SHAPE_CLOSED_INTEGER_SECTOR_AMPLITUDE_CLUE_SOURCE_OPEN", "decision status")
    require(len(decision["closed_now"]) == 3, "closed-now count")
    require(len(decision["not_closed"]) == 3, "not-closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_gamma_rows"] == 0, "gamma rows overaccepted")
    require(counts["accepted_three_over_eleven_ratio_rows"] == 0, "ratio rows overaccepted")
    require(counts["accepted_residual_correction_rows"] == 0, "correction rows overaccepted")
    require(counts["accepted_no_knob_yukawa_rows"] == 0, "Yukawa rows overaccepted")
    require(decision["next_exact_target"] == NEXT, "decision next")
    require(len(decision["legal_next_routes"]) == 3, "legal routes")
    require(len(decision["forbidden_routes"]) == 3, "forbidden routes")

    closure = data["closure_decision"]
    require(closure["residual_family_shape_closed"] is True, "closure shape")
    require(closure["source_correction_rows_closed"] is False, "closure source overclosed")
    require(closure["strict_no_knob_flavor_closure"] is False, "closure flavor overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "closure true SM overclosed")
    require(closure["full_no_knob_closed"] is False, "closure no-knob overclosed")

    require(cert["residual_family_shape_theorem_proved"] is True, "cert shape")
    require(cert["source_correction_rows_closed"] is False, "cert rows overclosed")
    require(cert["integer_sector_amplitude_source_proved"] is False, "cert integer overproved")
    require(cert["accepted_no_knob_yukawa_rows"] == 0, "cert Yukawa rows")

    for phrase in [
        "`Q = [-2, 3, -1]`",
        "`rho [17,15,-21] outer Q`",
        "not a source theorem",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
