"""Audit phase-antisymmetry scalar source candidate and error certificate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCALAR = PACKET_DIR / "phase_antisymmetry_scalar_source_candidate.packet.json"
ERROR_CERT = PACKET_DIR / "final_yukawa_residual_error_certificate.packet.json"
DECISION = PACKET_DIR / "final_yukawa_magnitude_closure_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhaseAntisymmetryCurvatureScalarSource_or_FinalYukawaMagnitudeClosure_v1.md"

STATUS = "MTT_SELECTED_PHASEANTISYMMETRYCURVATURESCALARSOURCE_BUILT_Q64_SBETA_ERROR_CERT_STRICT_EXACTNESS_OPEN"
NEXT = "MTT_Selected_StrictPhaseAntisymmetryScalarDerivation_or_NoKnobYukawaExactness_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    scalar = load(SCALAR)
    error_cert = load(ERROR_CERT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(
        scalar["status"] == "Q64_SBETA_PHASE_ANTISYMMETRY_SCALAR_CANDIDATE_CONSTRUCTED",
        "scalar status",
    )
    require(scalar["observed_data_used_as_selector"] is False, "scalar observed selector")
    require(scalar["target_fitting_used"] is False, "scalar target fitting")
    require(scalar["selected_inputs"]["q64"] == 15, "q64")
    require(abs(scalar["selected_inputs"]["selected_s_beta"] - 0.004701083905943647) < 1.0e-18, "s_beta")
    source = scalar["source_candidate"]
    require(source["delta_c2_formula"] == "-((q64+1)/q64) * s_beta", "delta formula")
    require(abs(source["delta_c2_value"] - (-0.005014489499673223)) < 1.0e-18, "delta value")
    require(
        source["residual_operator_coefficient_formula"]
        == "epsilon_theta * s_beta * delta_c2_source",
        "coefficient formula",
    )
    require(abs(source["residual_operator_coefficient"] - (-4.402222824618228e-08)) < 1.0e-20, "coefficient")
    compare = scalar["comparison_to_prior_fitted_phase_split"]
    require(abs(compare["source_coefficient_minus_best_fit"] - (-5.934214541811071e-12)) < 1.0e-22, "best delta")
    status = scalar["source_status"]
    require(status["scalar_candidate_uses_only_selected_inputs"] is True, "selected inputs")
    require(status["strict_derivation_from_variational_HYM_kernel_proved"] is False, "derivation overproved")
    require(status["accepted_as_strict_source_theorem"] is False, "strict source overaccepted")

    require(
        error_cert["status"] == "ULTRATIGHT_ERROR_CERTIFICATE_ACCEPTED_FOR_Q64_SBETA_SCALAR_CANDIDATE",
        "error cert status",
    )
    require(error_cert["observed_data_used_as_selector"] is False, "error observed selector")
    require(error_cert["target_fitting_used"] is False, "error target fitting")
    require(error_cert["operator"]["family_shape_Q"] == [-2.0, 3.0, -1.0], "family Q")
    require(error_cert["operator"]["sector_operator_vector"] == [27.0, 6.0, 26.0], "operator vector")
    bound = error_cert["error_bound"]
    require(bound["declared_max_log_residual_bound"] == 8.0e-9, "declared bound")
    require(bound["actual_max_log_residual"] < 8.0e-9, "actual bound")
    require(abs(bound["actual_max_log_residual"] - 7.959463247076954e-09) < 1.0e-20, "actual max")
    require(bound["actual_worst_multiplicative_yukawa_error"] < 1.000000008, "worst factor")
    require(bound["bound_passes"] is True, "bound pass")
    accepted = error_cert["accepted_as"]
    require(accepted["bounded_error_certificate_for_q64_sbeta_scalar_candidate"] is True, "bounded not accepted")
    require(accepted["strict_exactness_certificate"] is False, "strict exactness overaccepted")
    require(accepted["strict_no_knob_yukawa_closure"] is False, "no-knob overaccepted")
    require(accepted["true_SM_equivalence_closure"] is False, "true SM overaccepted")

    require(
        decision["status"]
        == "Q64_SBETA_SCALAR_CANDIDATE_EXECUTED_ULTRATIGHT_ERROR_CERT_STRICT_SOURCE_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["constructed_phase_antisymmetry_scalar_candidates"] == 1, "candidate count")
    require(counts["accepted_bounded_error_certificates_for_candidate"] == 1, "error count")
    require(counts["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 0, "strict source rows")
    require(counts["accepted_exact_yukawa_magnitude_rows"] == 0, "exact rows")
    require(counts["accepted_full_no_knob_yukawa_rows"] == 0, "no-knob rows")
    acceptance = decision["acceptance"]
    require(acceptance["q64_sbeta_scalar_candidate_constructed"] is True, "accept candidate")
    require(acceptance["q64_sbeta_scalar_uses_only_selected_inputs"] is True, "accept selected inputs")
    require(acceptance["ultratight_error_certificate_accepted"] is True, "accept error")
    require(acceptance["strict_phase_scalar_source_theorem_proved"] is False, "strict theorem overproved")
    require(acceptance["strict_exactness_closed"] is False, "strict exactness overclosed")
    require(acceptance["strict_no_knob_yukawa_closure"] is False, "no-knob overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(data["theorem"]["name"] == "PhaseAntisymmetryQ64SBetaScalarCandidateTheorem", "theorem name")
    require(data["theorem"]["proved"] is False, "theorem overproved")
    require(len(data["theorem"]["proved_components"]) == 3, "component count")
    require(data["closure_decision"] == acceptance, "closure decision copy")

    require(cert["q64_sbeta_scalar_candidate_constructed"] is True, "cert candidate")
    require(cert["q64_sbeta_scalar_uses_only_selected_inputs"] is True, "cert selected")
    require(cert["ultratight_error_certificate_accepted"] is True, "cert error")
    require(cert["strict_phase_scalar_source_theorem_proved"] is False, "cert theorem")
    require(cert["strict_exactness_closed"] is False, "cert exactness")
    require(cert["strict_no_knob_yukawa_closure"] is False, "cert no-knob")
    require(cert["accepted_exact_yukawa_magnitude_rows"] == 0, "cert exact rows")

    for phrase in [
        "`delta_c2 = -((q64+1)/q64) * s_beta`",
        "`epsilon_theta * s_beta * delta_c2",
        "accepted ultra-tight bounded-error certificate below `8e-9`",
        "strict derivation of this scalar",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
