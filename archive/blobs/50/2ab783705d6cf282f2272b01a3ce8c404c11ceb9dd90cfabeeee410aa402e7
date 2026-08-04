"""Audit the Higgs decay residual and precision-promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsdecayresidualaudit_or_precisionpromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RESIDUALS = PACKET_DIR / "higgs_decay_proxy_residual_audit.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_acceptance_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_higgs_decay_residual_audit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsDecayResidualAudit_or_PrecisionPromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSDECAYRESIDUALAUDIT_OR_PRECISIONPROMOTION_BUILT_NONFIT_AUDIT_PRECISION_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    residuals = load(RESIDUALS)
    promotion = load(PROMOTION)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["closure_decision"]["residual_audit_closed"] is True, "residual audit not closed")
    require(data["closure_decision"]["precision_promotion_accepted"] is False, "precision promotion overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")

    rows = residuals["residual_rows"]
    require(len(rows) == 6, "expected three stages for two channels")
    require(residuals["accepted_as_nonfit_residual_audit"] is True, "audit not accepted")
    require(residuals["accepted_as_precision_promotion"] is False, "residual audit overpromoted")
    require(residuals["audit_result"]["reference_mass_tree_and_qcd_proxy_are_not_precision_plausible_for_bb"] is True, "bb bad proxy not detected")
    require(residuals["audit_result"]["running_mass_proxy_is_best_available_stage_for_b"] is True, "b best stage mismatch")
    require(residuals["audit_result"]["running_mass_proxy_is_best_available_stage_for_c"] is True, "c best stage mismatch")
    require(residuals["audit_result"]["running_mass_proxy_within_factor_two_for_all_audited_channels"] is True, "factor-two plausibility failed")
    require(residuals["audit_result"]["running_mass_proxy_within_twenty_percent_for_all_audited_channels"] is False, "20 percent gate should remain open")

    require(promotion["precision_promotion_accepted"] is False, "promotion gate overclaimed")
    require(promotion["best_current_stage"] == "one_loop_running_mass_qcd_proxy", "best stage mismatch")
    require("versioned multiloop alpha_s and mass-running/matching equations" in promotion["minimum_next_rows_for_promotion"], "multiloop requirement missing")
    require("versioned multiloop Higgs partial-width formula set" in updated["remaining_true_equivalence_blockers"], "formula-set blocker missing")
    require(updated["guardrails"]["residual_benchmark_not_used_for_fit"] is True, "benchmark fit guard missing")

    for packet in [residuals, promotion, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("not used to tune" in note, "note missing no-fit guard")
    require("precision promotion must still be" in note, "note missing promotion rejection")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
