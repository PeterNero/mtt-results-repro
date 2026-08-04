"""Audit Higgs loop/off-shell route-A derivative rows or precision decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsloopoffshellrouteaderivativerows_or_precisiondecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LOOP_ROWS = PACKET_DIR / "route_a_loop_derivative_rows.packet.json"
COMPARISON = PACKET_DIR / "loop_rows_imported_profile_comparison.packet.json"
OPEN_ROWS = PACKET_DIR / "offshell_and_zgamma_open_kernel_contract.packet.json"
PRECISION_DECISION = PACKET_DIR / "loop_offshell_route_a_precision_decision.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_loop_offshell_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsLoopOffshellRouteADerivativeRows_or_PrecisionDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSLOOPOFFSHELLROUTEADERIVATIVEROWS_OR_PRECISIONDECISION_BUILT_GG_GAMMAGAMMA_DERIVATIVES_ZGAMMA_WW_ZZ_OPEN"
NEXT = "MTT_Selected_HiggsOffshellZGammaRouteA_or_PrecisionImportDecision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    rows = load(LOOP_ROWS)
    comparison = load(COMPARISON)
    open_rows = load(OPEN_ROWS)
    decision = load(PRECISION_DECISION)
    updated = load(UPDATED_TRUE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(rows["accepted_as_route_A_loop_derivative_block"] is True, "loop block not accepted")
    require(rows["accepted_as_full_Higgs_precision_block"] is False, "precision overaccepted")
    require(rows["rows_executed"] == 2, "wrong loop row count")
    require(rows["row_basis"] == ["H_to_gg", "H_to_gamma_gamma"], "loop row basis mismatch")
    require(len(rows["loop_covariance_GeV2"]) == 2, "covariance row count mismatch")
    require(all(len(row) == 2 for row in rows["loop_covariance_GeV2"]), "covariance col count mismatch")
    require(rows["loop_covariance_GeV2"][0][1] == rows["loop_covariance_GeV2"][1][0], "covariance asymmetry")

    for channel in rows["row_basis"]:
        row = rows["rows"][channel]
        require(row["accepted_as_route_A_formula_derivative_row"] is True, f"{channel} not accepted")
        require(row["accepted_as_full_precision_row"] is False, f"{channel} precision overaccepted")
        require(row["central_width_GeV"] > 0, f"{channel} width missing")
        require(row["propagated_sigma_GeV"] > 0, f"{channel} sigma missing")
        require(row["relative_sigma"] > 0, f"{channel} relative sigma missing")
        require(row["analytic_derivatives"]["G_F"] > 0, f"{channel} G_F derivative sign")

    require(rows["rows"]["H_to_gg"]["analytic_derivatives"]["alpha_s_effective"] > 0, "gg alpha_s derivative missing")
    require(rows["rows"]["H_to_gamma_gamma"]["analytic_derivatives"]["alpha_em"] > 0, "gamma alpha derivative missing")
    require(rows["rows"]["H_to_gamma_gamma"]["analytic_derivatives"]["amplitude_abs"] > 0, "gamma amplitude derivative missing")

    require(comparison["comparison_used_as_selector"] is False, "comparison used as selector")
    require(comparison["precision_promotion_from_comparison"] is False, "comparison promoted precision")
    require(set(comparison["comparison_rows"]) == {"H_to_gg", "H_to_gamma_gamma"}, "comparison row set mismatch")

    require(open_rows["open_row_basis"] == ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"], "open row basis mismatch")
    require(open_rows["formula_kernels_filled"] == 0, "open kernels overfilled")
    require(open_rows["central_imports_available_but_not_route_A_derivatives"] is True, "import/route distinction missing")

    require(decision["route_A_rows_closed_total_including_previous"] == 7, "route-A total count mismatch")
    require(decision["rows_remaining_for_route_A_ten_row_engine"] == ["H_to_Z_gamma", "H_to_WW_star", "H_to_ZZ_star"], "remaining rows mismatch")
    require(decision["precision_total_width_closed"] is False, "precision total overclosed")
    require(decision["precision_branching_ratios_closed"] is False, "precision BR overclosed")

    require(updated["guardrails"]["route_A_loop_rows_executed"] is True, "updated loop flag missing")
    require(updated["guardrails"]["full_route_A_ten_row_engine_closed"] is False, "full route-A overclosed")
    require(updated["guardrails"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(updated["guardrails"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["closure_decision"]["route_A_loop_derivative_block_closed_for_gg_gammagamma"] is True, "candidate loop closure missing")
    require(data["closure_decision"]["route_A_rows_closed_total_including_previous"] == 7, "candidate row count mismatch")
    require(cert["route_A_loop_derivative_block_closed_for_gg_gammagamma"] is True, "certificate loop closure missing")
    require("seven of ten" in note, "note missing limited closure count")

    for packet in [rows, comparison, open_rows, decision, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
