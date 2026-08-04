"""Audit threshold/pole-running map scaffold and covariance-profile gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_thresholdpolerunningmaps_or_covarianceprofile"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
GAUGE = PACKET_DIR / "one_loop_gauge_mz_to_mt_transport.packet.json"
RESIDUALS = PACKET_DIR / "pole_threshold_residual_map_requirements.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_threshold_map_scaffold.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ThresholdPoleRunningMaps_or_CovarianceProfile_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_THRESHOLDPOLERUNNINGMAPS_OR_COVARIANCEPROFILE_BUILT_GAUGE_BRIDGE_THRESHOLDS_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    gauge = load(GAUGE)
    residuals = load(RESIDUALS)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    transport = gauge["transport"]
    require(transport["scheme"] == "MSbar, GUT-normalized U(1)", "scheme mismatch")
    require(transport["mu0_GeV"] == 91.1876, "MZ mismatch")
    require(transport["mu1_GeV"] > transport["mu0_GeV"], "Mt must exceed MZ")
    require(transport["beta_coefficients"]["g_1_GUT"] == 41.0 / 10.0, "g1 beta mismatch")
    require(transport["beta_coefficients"]["g_2"] == -19.0 / 6.0, "g2 beta mismatch")
    require(transport["beta_coefficients"]["g_3"] == -7.0, "g3 beta mismatch")
    require(abs(transport["transported_values"]["g_Y_Mt_one_loop"] - transport["transported_values"]["g_1_GUT_Mt_one_loop"] / math.sqrt(5.0 / 3.0)) < 1e-15, "hypercharge normalization mismatch")
    require(len(gauge["comparison_rows"]) == 3, "gauge comparison row count mismatch")
    require(gauge["passes_coarse_gauge_bridge"] is True, "coarse gauge bridge should pass")
    require(gauge["accepted_as_precision_threshold_match"] is False, "precision match overclaimed")
    require(gauge["max_absolute_delta_to_literature"] < 0.01, "gauge bridge too far from literature")

    slots = residuals["residual_slots"]
    for key in [
        "top_tree_to_MSbar_Mt",
        "top_firstpass_MZ_to_MSbar_Mt",
        "lambda_tree_to_MSbar_Mt",
        "lambda_firstpass_MZ_to_MSbar_Mt",
    ]:
        require(key in slots, f"missing residual slot: {key}")
        require(slots[key]["promotable_now"] is False, f"residual slot overpromoted: {key}")
        require(math.isfinite(slots[key]["required_additive_delta"]), f"nonfinite residual delta: {key}")
    require("required_multiplicative_map" in slots["top_tree_to_MSbar_Mt"], "top multiplicative map missing")
    require(residuals["target_fitting_used"] is False, "residuals use target fitting")

    require("one-loop gauge M_Z-to-M_t transport scaffold" in updated["closed_now"], "gauge scaffold not closed")
    require("pole/threshold residual slots identified" in updated["closed_now"], "residual slots not closed")
    require("precision pole/running threshold residual maps" in updated["remaining_true_equivalence_blockers"], "residual blocker missing")
    require(updated["guardrails"]["residuals_are_requirements_not_fitted_corrections"] is True, "residual guard missing")
    require(updated["guardrails"]["gauge_bridge_is_precision_match"] is False, "precision guard missing")

    for key in [
        "one_loop_gauge_MZ_to_Mt_transport_scaffold",
        "external_literature_gauge_bridge_compared",
        "pole_threshold_residual_slots_identified",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["precision_threshold_maps_closed"] is False, "precision closure overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_PoleThresholdResidualValues_or_CovarianceProfile_v1", "next artifact mismatch")

    for packet in [gauge, residuals, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("one-loop MSbar gauge transport" in note, "note missing gauge transport")
    require("requirements, not fitted" in note, "note missing residual guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
