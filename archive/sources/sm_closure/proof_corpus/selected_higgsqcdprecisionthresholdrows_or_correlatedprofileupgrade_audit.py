"""Audit Higgs QCD precision-threshold gate and correlation stress profile."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
THRESHOLD_GATE = PACKET_DIR / "higgs_qcd_precision_threshold_row_gate.packet.json"
STRESS = PACKET_DIR / "higgs_qcd_correlation_stress_profile.packet.json"
DECISION = PACKET_DIR / "higgs_qcd_precision_promotion_decision_after_stress.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDPrecisionThresholdRows_or_CorrelatedProfileUpgrade_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDPRECISIONTHRESHOLDROWS_OR_CORRELATEDPROFILEUPGRADE_BUILT_STRESS_PROFILE_PRECISION_OPEN"
NEXT = "MTT_Selected_HiggsQCDPrecisionFormulaValues_or_EmpiricalFullProfile_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    threshold = load(THRESHOLD_GATE)
    stress = load(STRESS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting guard missing")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(threshold["firstpass_nonfit_formula_values_available"] is True, "first-pass formulas missing")
    require(threshold["precision_threshold_values_filled"] is False, "threshold precision overfilled")
    require(threshold["precision_threshold_values_promotable"] is False, "threshold precision overpromoted")
    require([row["channel"] for row in threshold["rows"]] == ["H_to_ss", "H_to_gg"], "threshold channels mismatch")
    require(stress["channels"] == ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"], "stress channels mismatch")
    require(stress["summary"]["stress_models_checked"] == 4, "stress grid size mismatch")
    require(stress["summary"]["all_models_psd_by_equicorrelation_bound"] is True, "PSD stress check failed")
    require(stress["summary"]["accepted_as_correlation_stress_profile"] is True, "stress profile not accepted")
    require(stress["summary"]["accepted_as_full_correlated_profile"] is False, "full profile overclaimed")
    require(stress["summary"]["min_chi_square"] <= stress["summary"]["diagonal_chi_square"], "chi-square min invalid")
    require(stress["summary"]["max_chi_square"] >= stress["summary"]["diagonal_chi_square"], "chi-square max invalid")
    require(decision["correlation_stress_profile_built"] is True, "decision missing stress closure")
    require(decision["full_correlated_profile_filled"] is False, "decision full profile overclaimed")
    require(decision["precision_threshold_values_filled"] is False, "decision precision overfilled")
    require(decision["values_promotable_to_precision_now"] is False, "decision overpromoted")
    require(data["closure_decision"]["correlation_stress_profile_built"] is True, "candidate stress closure missing")
    require(data["closure_decision"]["full_correlated_profile_filled"] is False, "candidate full profile overclaimed")
    require(data["closure_decision"]["precision_threshold_values_filled"] is False, "candidate precision overfilled")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not a full empirical covariance/profile likelihood" in note, "note missing profile guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
