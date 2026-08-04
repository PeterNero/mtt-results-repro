"""Audit QCD threshold residual rows and profile-fill guardrails."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESIDUALS = PACKET_DIR / "qcd_threshold_residual_rows.packet.json"
REPAIR = PACKET_DIR / "qcd_threshold_repair_obligations.packet.json"
PROFILE = PACKET_DIR / "correlated_profile_fill_status_after_qcd_thresholds.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDThresholdRows_or_CorrelatedProfileFill_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDTHRESHOLDROWS_OR_CORRELATEDPROFILEFILL_BUILT_RESIDUALS_REPAIR_OPEN"
NEXT = "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    residuals = load(RESIDUALS)
    repair = load(REPAIR)
    profile = load(PROFILE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(residuals["summary"]["row_count"] == 2, "QCD residual row count mismatch")
    require(set(residuals["summary"]["channels"]) == {"H_to_ss", "H_to_gg"}, "QCD channels mismatch")
    require(residuals["summary"]["all_forbidden_fit_factors_blocked"] is True, "fit factor guard failed")
    require(residuals["summary"]["threshold_corrected_values_filled"] is False, "threshold value overfilled")
    for row in residuals["rows"]:
        require(row["forbidden_fit_factor_may_be_applied"] is False, f"fit factor applied: {row['channel']}")
        require(row["accepted_as_threshold_corrected_value"] is False, f"threshold overclaim: {row['channel']}")
        require(row["benchmark_over_proxy_ratio"] > 0.0, f"bad ratio: {row['channel']}")
    require(repair["status"] == "QCD_THRESHOLD_REPAIR_OBLIGATIONS_ENUMERATED", "repair status mismatch")
    require(len(repair["rows"]) == 2, "repair rows missing")
    require("diagnostics only" in repair["global_guardrail"], "repair guardrail missing")
    require(profile["full_matrix"]["dimension"] == 10, "profile dimension mismatch")
    require(profile["qcd_block_status"]["covariance_entries_filled"] == 0, "covariance overfilled")
    require(profile["qcd_block_status"]["accepted_as_correlated_profile"] is False, "profile overclaimed")
    require(data["closure_decision"]["residual_rows_closed"] is True, "residual rows not closed")
    require(data["closure_decision"]["threshold_repair_values_filled"] is False, "repair values overfilled")
    require(data["closure_decision"]["precision_rows_promoted"] == 0, "precision overpromoted")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("forbidden fit factors" in note, "note missing fit guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
