"""Audit Higgs route-A derivative engine execution or precision decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsrouteaderivativeengineexecution_or_precisiondecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LEPTONIC_ROWS = PACKET_DIR / "route_a_leptonic_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "leptonic_rows_imported_profile_comparison.packet.json"
EXECUTION_STATUS = PACKET_DIR / "route_a_derivative_engine_execution_status.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_route_a_leptonic_execution.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsRouteADerivativeEngineExecution_or_PrecisionDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSROUTEADERIVATIVEENGINEEXECUTION_OR_PRECISIONDECISION_BUILT_LEPTONIC_DERIVATIVES_QCD_EW_OPEN"
NEXT = "MTT_Selected_HiggsQCDRouteADerivativeRows_or_PrecisionDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    rows = load(LEPTONIC_ROWS)
    comparison = load(COMPARISON)
    status = load(EXECUTION_STATUS)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(rows["accepted_as_route_A_leptonic_derivative_block"] is True, "leptonic block not accepted")
    require(rows["accepted_as_full_Higgs_precision_block"] is False, "precision overaccepted")
    require(rows["rows_executed"] == 2, "wrong row count")
    require(rows["row_basis"] == ["H_to_tau_tau", "H_to_mu_mu"], "row basis mismatch")
    require(len(rows["leptonic_covariance_GeV2"]) == 2, "covariance row count mismatch")
    require(all(len(row) == 2 for row in rows["leptonic_covariance_GeV2"]), "covariance col count mismatch")
    require(rows["leptonic_covariance_GeV2"][0][1] == rows["leptonic_covariance_GeV2"][1][0], "covariance asymmetry")

    for channel in rows["row_basis"]:
        row = rows["rows"][channel]
        require(row["accepted_as_route_A_formula_derivative_row"] is True, f"{channel} not accepted")
        require(row["accepted_as_full_precision_row"] is False, f"{channel} precision overaccepted")
        require(row["central_width_GeV"] > 0, f"{channel} width missing")
        require(row["propagated_sigma_GeV"] > 0, f"{channel} sigma missing")
        require(row["relative_sigma"] > 0, f"{channel} relative sigma missing")
        require(row["analytic_derivatives"]["dGamma_dG_F"] > 0, f"{channel} dG_F sign")
        require(row["analytic_derivatives"]["dGamma_dM_H"] > 0, f"{channel} dM_H sign")
        require(row["analytic_derivatives"]["dGamma_dm_l"] > 0, f"{channel} dm_l sign")

    require(comparison["comparison_used_as_selector"] is False, "comparison used as selector")
    require(comparison["precision_promotion_from_comparison"] is False, "comparison promoted precision")
    require(comparison["max_abs_relative_delta_vs_imported"] > 0, "comparison delta missing")
    require(set(comparison["comparison_rows"]) == {"H_to_tau_tau", "H_to_mu_mu"}, "comparison row set mismatch")

    require(status["rows_required_total"] == 10, "total row count mismatch")
    require(status["rows_executed_now"] == ["H_to_tau_tau", "H_to_mu_mu"], "executed rows mismatch")
    require(len(status["rows_remaining"]) == 8, "remaining row count mismatch")
    require(status["precision_total_width_closed"] is False, "precision total overclosed")
    require(status["precision_branching_ratios_closed"] is False, "precision BR overclosed")

    require(updated["guardrails"]["route_A_leptonic_rows_executed"] is True, "updated leptonic flag missing")
    require(updated["guardrails"]["full_route_A_ten_row_engine_closed"] is False, "full route-A overclosed")
    require(updated["guardrails"]["comparison_used_as_selector"] is False, "updated selector violation")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["route_A_leptonic_derivative_block_closed"] is True, "candidate leptonic closure missing")
    require(data["closure_decision"]["full_route_A_ten_row_engine_closed"] is False, "candidate full route-A overclosed")
    require(cert["route_A_leptonic_derivative_block_closed"] is True, "certificate leptonic closure missing")
    require("leptonic derivative block only" in note, "note missing limited-closure guard")

    for packet in [rows, comparison, status, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
