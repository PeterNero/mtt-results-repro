"""Audit Higgs QCD route-A derivative rows or precision decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdrouteaderivativerows_or_precisiondecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QCD_ROWS = PACKET_DIR / "route_a_qcd_fermionic_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "qcd_rows_imported_profile_comparison.packet.json"
PRECISION_DECISION = PACKET_DIR / "qcd_route_a_precision_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_route_a_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDRouteADerivativeRows_or_PrecisionDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSQCDROUTEADERIVATIVEROWS_OR_PRECISIONDECISION_BUILT_QCD_FERMIONIC_DERIVATIVES_LOOPS_EW_OPEN"
NEXT = "MTT_Selected_HiggsLoopOffshellRouteADerivativeRows_or_PrecisionDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    rows = load(QCD_ROWS)
    comparison = load(COMPARISON)
    decision = load(PRECISION_DECISION)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(rows["accepted_as_route_A_qcd_fermionic_derivative_block"] is True, "QCD block not accepted")
    require(rows["accepted_as_full_Higgs_precision_block"] is False, "QCD precision overaccepted")
    require(rows["rows_executed"] == 3, "wrong QCD row count")
    require(rows["row_basis"] == ["H_to_bb", "H_to_cc", "H_to_ss"], "QCD row basis mismatch")
    require(len(rows["qcd_fermionic_covariance_GeV2"]) == 3, "covariance row count mismatch")
    require(all(len(row) == 3 for row in rows["qcd_fermionic_covariance_GeV2"]), "covariance col count mismatch")

    for i in range(3):
        for j in range(3):
            require(
                abs(rows["qcd_fermionic_covariance_GeV2"][i][j] - rows["qcd_fermionic_covariance_GeV2"][j][i]) < 1e-30,
                "covariance asymmetry",
            )

    for channel in rows["row_basis"]:
        row = rows["rows"][channel]
        require(row["accepted_as_route_A_formula_derivative_row"] is True, f"{channel} not accepted")
        require(row["accepted_as_full_precision_row"] is False, f"{channel} precision overaccepted")
        require(row["central_width_GeV"] > 0, f"{channel} width missing")
        require(row["Gamma0_running_mass_GeV"] > 0, f"{channel} gamma0 missing")
        require(row["propagated_sigma_GeV"] > 0, f"{channel} sigma missing")
        require(row["relative_sigma"] > 0, f"{channel} relative sigma missing")
        require(row["analytic_derivatives"]["dGamma_dG_F"] > 0, f"{channel} dG_F sign")
        require(row["analytic_derivatives"]["dGamma_dM_H_fixed_running_mass"] > 0, f"{channel} dM_H sign")
        require(row["analytic_derivatives"]["dGamma_dm_q_running"] > 0, f"{channel} dm_q sign")
        require(row["analytic_derivatives"]["dGamma_dK_QCD"] > 0, f"{channel} dK sign")
        require("EFFECTIVE_K_SLOT" in row["alpha_s_derivative_status"], f"{channel} alpha_s guard missing")

    require(comparison["comparison_used_as_selector"] is False, "comparison used as selector")
    require(comparison["precision_promotion_from_comparison"] is False, "comparison promoted precision")
    require(comparison["max_abs_relative_delta_vs_imported"] > 0, "comparison delta missing")
    require(set(comparison["comparison_rows"]) == {"H_to_bb", "H_to_cc", "H_to_ss"}, "comparison row set mismatch")

    require(decision["route_A_rows_closed_total_including_leptonic"] == 5, "route-A total count mismatch")
    require(decision["precision_total_width_closed"] is False, "precision total overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "precision BR overclosed")
    require(len(decision["rows_remaining_for_route_A_ten_row_engine"]) == 5, "remaining route-A rows mismatch")
    require(any("alpha_s derivative" in reason for reason in decision["precision_rejection_reasons"]), "alpha_s rejection missing")

    require(updated["guardrails"]["route_A_qcd_fermionic_rows_executed"] is True, "updated QCD flag missing")
    require(updated["guardrails"]["full_route_A_ten_row_engine_closed"] is False, "full route-A overclosed")
    require(updated["guardrails"]["comparison_used_as_selector"] is False, "updated selector violation")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["route_A_qcd_fermionic_derivative_block_closed"] is True, "candidate QCD closure missing")
    require(data["closure_decision"]["route_A_rows_closed_total_including_leptonic"] == 5, "candidate closed row count mismatch")
    require(cert["route_A_qcd_fermionic_derivative_block_closed"] is True, "certificate QCD closure missing")
    require("proxy tier only" in note, "note missing limited-closure guard")

    for packet in [rows, comparison, decision, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
