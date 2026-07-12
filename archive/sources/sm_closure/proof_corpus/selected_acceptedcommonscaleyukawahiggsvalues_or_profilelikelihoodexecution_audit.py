"""Audit accepted common-scale Yukawa/Higgs values or profile-likelihood execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUES = PACKET_DIR / "versioned_common_scale_yukawa_higgs_values.packet.json"
PROFILE = PACKET_DIR / "profile_likelihood_execution_summary.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_value_profile_execution.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AcceptedCommonScaleYukawaHiggsValues_or_ProfileLikelihoodExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_ACCEPTEDCOMMONSCALEYUKAWAHIGGSVALUES_OR_PROFILELIKELIHOODEXECUTION_"
    "BUILT_VERSIONED_VALUES_AND_DIAGONAL_PROFILE_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    values = load(VALUES)
    profile = load(PROFILE)
    promotion = load(PROMOTION)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(values["accepted_as_versioned_common_scale_candidate_values"] is True, "versioned values missing")
    require(values["accepted_for_SM_parity"] is True, "SM-parity value acceptance missing")
    require(values["accepted_for_profile_execution_input"] is True, "profile input acceptance missing")
    require(values["accepted_for_true_precision_equivalence"] is False, "values overaccepted for true precision")
    require(values["accepted_as_no_knob_MTT_prediction"] is False, "values overaccepted as no-knob prediction")
    require(len(values["derived_magnitudes"]["diag_abs_Y_u"]) == 3, "Y_u magnitudes malformed")
    require(len(values["derived_magnitudes"]["diag_abs_Y_d"]) == 3, "Y_d magnitudes malformed")
    require(len(values["derived_magnitudes"]["diag_abs_Y_e"]) == 3, "Y_e magnitudes malformed")
    require(values["derived_magnitudes"]["lambda_H"] > 0, "lambda_H not positive")

    summary = profile["profile_summary"]
    require(summary["passes_coarse_diagonal_profile"] is True, "coarse diagonal profile should pass")
    require(summary["accepted_as_full_covariance_profile"] is False, "full profile overclaimed")
    require(profile["accepted_for_true_precision_equivalence"] is False, "profile overaccepted")
    require(profile["what_this_does_not_close"]["true_SM_equivalence"] is True, "true-equivalence guardrail missing")

    tests = promotion["promotion_tests"]
    require(tests["finite_firstpass_values_emitted"] is True, "finite values not emitted")
    require(tests["internal_RK_convergence_closed"] is True, "RK convergence missing")
    require(tests["coarse_diagonal_profile_passes"] is True, "coarse profile missing")
    for key in [
        "threshold_matching_values_emitted",
        "mass_scheme_conversion_values_emitted",
        "full_correlated_covariance_profile_emitted",
        "multi_loop_threshold_convention_values_emitted",
        "no_knob_MTT_source_derivation_of_values",
    ]:
        require(tests[key] is False, f"promotion test unexpectedly closed: {key}")
        require(key in promotion["hard_failures"], f"hard failure not recorded: {key}")

    decision = promotion["promotion_decision"]
    require(decision["accepted_as_versioned_common_scale_candidate_values"] is True, "candidate value acceptance missing")
    require(decision["accepted_for_SM_parity"] is True, "SM-parity promotion missing")
    require(decision["accepted_for_diagonal_profile_execution"] is True, "profile execution promotion missing")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overpromoted")
    require(decision["accepted_as_full_SM_no_knob_closure"] is False, "full no-knob overpromoted")
    require(promotion["closure_claimed"] is False, "promotion overclaimed closure")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed closure")
    require(data["closure_decision"]["value_profile_execution_layer_closed"] is True, "value/profile layer not closed")
    require(data["closure_decision"]["accepted_common_scale_values_for_true_precision"] is False, "true precision overclosed")
    require(data["closure_decision"]["full_profile_likelihood_closed"] is False, "full profile overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")
    require("does not promote first-pass values to true precision equivalence" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
