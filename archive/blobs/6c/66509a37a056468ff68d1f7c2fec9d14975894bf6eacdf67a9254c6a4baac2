"""Audit correlated threshold/profile matrix or Yukawa/Higgs precision-promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BASIS = PACKET_DIR / "threshold_profile_basis_and_open_rows.packet.json"
MATRIX = PACKET_DIR / "correlated_threshold_profile_matrix.packet.json"
PROMOTION = PACKET_DIR / "yukawa_higgs_precision_promotion_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_correlated_threshold_profile_matrix.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_CORRELATEDTHRESHOLDPROFILEMATRIX_OR_YUKAWAHIGGSPRECISIONPROMOTION_"
    "BUILT_SURROGATE_MATRIX_PRECISION_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def symmetric(matrix: list[list[float]], tol: float = 1e-18) -> bool:
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if abs(value - matrix[j][i]) > tol:
                return False
    return True


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    basis = load(BASIS)
    matrix = load(MATRIX)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    outputs = basis["profile_output_basis"]
    require(len(outputs["independent_outputs"]) == 5, "independent profile basis malformed")
    require(outputs["redundant_outputs_removed"] == ["g_1_GUT_Mt"], "redundant hypercharge row not removed")
    for key in [
        "threshold_matching_values",
        "mass_scheme_conversion_values",
        "full_correlated_covariance_profile",
        "multi_loop_threshold_convention_values",
        "no_knob_MTT_source_derivation_of_values",
    ]:
        require(basis["open_precision_rows"][key] is True, f"basis overclosed {key}")

    require(matrix["accepted_as_surrogate_correlated_threshold_profile_matrix"] is True, "surrogate matrix not accepted")
    require(matrix["accepted_as_published_or_reconstructed_profile_likelihood"] is False, "full likelihood overaccepted")
    require(matrix["stress_envelope"]["all_matrices_positive_definite"] is True, "not all matrices positive definite")
    require(matrix["stress_envelope"]["coarse_core_profile_passes"] is True, "core profile should pass")
    require(len(matrix["delta_vector_order"]) == 5, "delta vector order malformed")
    for row in matrix["scan_rows"]:
        cov = row["covariance_matrix"]
        require(len(cov) == 5, "covariance matrix row count mismatch")
        require(all(len(cov_row) == 5 for cov_row in cov), "covariance matrix column count mismatch")
        require(symmetric(cov), "covariance matrix not symmetric")
        require(row["positive_definite"] is True, "declared matrix not positive definite")
        require(row["reduced_chi2"] >= 0.0, "negative reduced chi2")
    selected = matrix["selected_reference_matrix"]
    require(selected["rho_equicorrelation"] == 0.0, "reference matrix policy mismatch")
    require(selected["positive_definite"] is True, "reference matrix not positive definite")

    tests = promotion["promotion_tests"]
    require(tests["versioned_common_scale_value_packet_emitted"] is True, "value packet not emitted")
    require(tests["surrogate_correlated_threshold_profile_matrix_emitted"] is True, "surrogate matrix missing")
    require(tests["all_declared_surrogate_matrices_positive_definite"] is True, "PD validation missing")
    require(tests["coarse_core_profile_passes"] is True, "core profile test missing")
    for key in [
        "threshold_matching_values_emitted",
        "mass_scheme_conversion_values_emitted",
        "published_or_reconstructed_profile_likelihood_imported",
        "multi_loop_threshold_convention_values_emitted",
        "no_knob_MTT_source_derivation_of_values",
    ]:
        require(tests[key] is False, f"promotion overclosed {key}")
        require(key in promotion["remaining_hard_failures"], f"hard failure missing: {key}")

    decision = promotion["promotion_decision"]
    require(decision["accepted_as_surrogate_precision_scaffold"] is True, "surrogate scaffold not closed")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overpromoted")
    require(decision["accepted_as_full_SM_no_knob_closure"] is False, "no-knob overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(promotion["closure_claimed"] is False, "promotion overclaimed closure")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed closure")
    require(data["closure_decision"]["surrogate_precision_scaffold_closed"] is True, "scaffold not closed")
    require(data["closure_decision"]["accepted_for_true_precision_equivalence"] is False, "candidate true precision overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require("remaining wall is real source data" in note, "note missing source-data wall")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
