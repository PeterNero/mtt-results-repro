"""Audit literature pole/threshold residual formula replay and covariance scaffold."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_polethresholdresidualvalues_or_covarianceprofile"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FORMULAS = PACKET_DIR / "buttazzo_boundary_formula_replay.packet.json"
COVARIANCE = PACKET_DIR / "diagonal_sensitivity_covariance_scaffold.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_formula_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PoleThresholdResidualValues_or_CovarianceProfile_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_POLETHRESHOLDRESIDUALVALUES_OR_COVARIANCEPROFILE_BUILT_FORMULA_REPLAY_COVARIANCE_OPEN"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    formulas = load(FORMULAS)
    covariance = load(COVARIANCE)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    replay = formulas["buttazzo_central_input_replay"]
    require(replay["replays_encoded_literature_values"] is True, "literature formula replay failed")
    require(replay["max_absolute_delta_to_encoded_literature"] < 1e-14, "formula replay residual too large")
    require(formulas["formula_reference"]["g_Y_Mt"].startswith("0.35830"), "gY formula missing")
    require("- 0.00020" in formulas["formula_reference"]["g_Y_Mt"], "gY MW sign mismatch")
    require(abs(replay["values"]["g_1_GUT_Mt"] - math.sqrt(5.0 / 3.0) * replay["values"]["g_Y_Mt"]) < 1e-15, "GUT normalization mismatch")
    require(formulas["current_repo_input_variant"]["accepted_as_selected_MTT_prediction"] is False, "current variant overpromoted")
    require(formulas["residuals_promoted_to_literature_formula_requirements"] is True, "residuals not promoted to formula requirements")
    require(formulas["precision_equivalence_closed"] is False, "precision equivalence overclaimed")

    jac = covariance["jacobian"]
    require(jac["lambda_Mt"]["M_h_GeV"] == 0.00206, "lambda Higgs sensitivity mismatch")
    require(jac["lambda_Mt"]["M_t_GeV"] == -0.00004, "lambda top sensitivity mismatch")
    require(jac["y_t_Mt"]["alpha3_MZ"] == -0.00042 / 0.0007, "yt alpha3 sensitivity mismatch")
    require(jac["g_3_Mt"]["alpha3_MZ"] == 0.00314 / 0.0007, "g3 alpha3 sensitivity mismatch")
    require(covariance["correlations_included"] is False, "correlations overclaimed")
    require(covariance["full_profile_likelihood_closed"] is False, "profile likelihood overclaimed")
    for key, row in covariance["propagated_diagonal_uncertainties"].items():
        require(row["diagonal_sigma"] >= 0.0, f"negative sigma: {key}")
        require(math.isfinite(row["diagonal_sigma"]), f"nonfinite sigma: {key}")

    require("Buttazzo boundary formula replay" in updated["closed_now"], "formula replay not closed")
    require("diagonal sensitivity covariance scaffold" in updated["closed_now"], "covariance scaffold not closed")
    require("full covariance/profile likelihood values" in updated["remaining_true_equivalence_blockers"], "covariance blocker missing")
    require(updated["guardrails"]["formula_values_are_literature_replay_not_MTT_source"] is True, "formula guard missing")
    require(updated["guardrails"]["current_input_variant_is_not_selected_prediction"] is True, "variant guard missing")

    for key in [
        "buttazzo_boundary_formula_replay",
        "pole_threshold_residual_formula_requirements_filled",
        "diagonal_sensitivity_covariance_scaffold",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["literature_formula_replay_closed"] is True, "formula closure flag missing")
    require(data["closure_decision"]["precision_profile_likelihood_closed"] is False, "profile closure overclaimed")
    require(cert["next_required_artifact"] == "MTT_Selected_FullCovarianceProfile_or_MultiLoopConventionAudit_v1", "next artifact mismatch")

    for packet in [formulas, covariance, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("downstream" in note, "note missing downstream guard")
    require("Full covariance/profile" in note, "note missing covariance gap")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
