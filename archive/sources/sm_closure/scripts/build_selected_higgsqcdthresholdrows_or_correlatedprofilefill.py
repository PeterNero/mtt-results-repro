"""Build QCD threshold residual rows for H->ss and H->gg."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESIDUALS = PACKET_DIR / "qcd_threshold_residual_rows.packet.json"
REPAIR = PACKET_DIR / "qcd_threshold_repair_obligations.packet.json"
PROFILE = PACKET_DIR / "correlated_profile_fill_status_after_qcd_thresholds.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_threshold_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDThresholdRows_or_CorrelatedProfileFill_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDTHRESHOLDROWS_OR_CORRELATEDPROFILEFILL_BUILT_RESIDUALS_REPAIR_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def residual_row(channel: str, width: float, benchmark: float, sigma: float, formula_family: str, operator: str) -> dict[str, Any]:
    residual = width - benchmark
    ratio = benchmark / width
    return {
        "channel": channel,
        "current_proxy_width_GeV": width,
        "benchmark_width_GeV": benchmark,
        "sidecar_sigma_GeV": sigma,
        "residual_GeV": residual,
        "relative_residual_to_benchmark": residual / benchmark,
        "diagonal_pull": residual / sigma,
        "benchmark_over_proxy_ratio": ratio,
        "forbidden_fit_factor": ratio,
        "forbidden_fit_factor_may_be_applied": False,
        "required_formula_family": formula_family,
        "operator_attachment_required": operator,
        "accepted_as_threshold_corrected_value": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsgammagammacorrection_or_qcdthresholdrows.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsgammagammacorrection_or_qcdthresholdrows"
        / "updated_true_equivalence_gate_after_gamma_gamma_extension.packet.json"
    )
    ss = load(
        DATA
        / "selected_higgssskernelrow_or_remainingchannels"
        / "higgs_ss_running_mass_kernel_row.packet.json"
    )
    gg = load(
        DATA
        / "selected_higgsggkernelrow_or_electroweakrows"
        / "higgs_gg_heavytop_kernel_row.packet.json"
    )
    priority = load(
        DATA
        / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
        / "higgs_precision_promotion_priority.packet.json"
    )
    profile_blueprint = load(
        DATA
        / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
        / "higgs_correlated_profile_blueprint.packet.json"
    )

    priority_by_channel = {row["channel"]: row for row in priority["rows"]}
    rows = []
    for packet in [ss, gg]:
        channel = packet["channel"]
        benchmark = float(packet["benchmark_fill_width_GeV"])
        sigma = benchmark * float(packet["relative_uncertainty_sidecar"])
        pr = priority_by_channel[channel]
        rows.append(
            residual_row(
                channel=channel,
                width=float(packet["width_GeV"]),
                benchmark=benchmark,
                sigma=sigma,
                formula_family=pr["next_required_value"],
                operator=pr["operator_attachment_required"],
            )
        )
    rows.sort(key=lambda row: -abs(row["diagonal_pull"]))

    residuals = {
        "schema": "MTTHiggsQCDThresholdResidualRows.v1",
        "status": "QCD_THRESHOLD_RESIDUAL_ROWS_BUILT_NO_FIT_FACTOR_APPLIED",
        "rows": rows,
        "summary": {
            "row_count": len(rows),
            "channels": [row["channel"] for row in rows],
            "largest_abs_pull_channel": rows[0]["channel"],
            "largest_abs_pull": abs(rows[0]["diagonal_pull"]),
            "all_forbidden_fit_factors_blocked": all(row["forbidden_fit_factor_may_be_applied"] is False for row in rows),
            "threshold_corrected_values_filled": False,
            "precision_rows_promoted": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    repair_rows = []
    for row in rows:
        if row["channel"] == "H_to_ss":
            missing = [
                "multi-loop m_s(2 GeV)->m_H running with threshold matching and uncertainty propagation",
                "consistent MSbar mass-scheme covariance for strange mass and alpha_s",
                "EW and mixed QCD/EW corrections for H->ss",
                "selected Qa/SU3 color/Yukawa operator attachment",
            ]
        else:
            missing = [
                "finite top/bottom/charm mass loop functions and interference",
                "NNLO/N3LO QCD K factors with threshold matching",
                "alpha_s and heavy-quark mass covariance",
                "selected Qa/SU3 color trace/operator attachment",
            ]
        repair_rows.append(
            {
                "channel": row["channel"],
                "missing_repair_inputs": missing,
                "minimum_acceptance_tests": [
                    "formula value is computed before comparison to benchmark sidecar",
                    "no benchmark_over_proxy_ratio is multiplied into the row",
                    "mass-scheme and alpha_s conventions are declared",
                    "operator/source attachment status is recorded separately from measured replay",
                ],
                "repair_status": "OPEN",
            }
        )

    repair = {
        "schema": "MTTHiggsQCDThresholdRepairObligations.v1",
        "status": "QCD_THRESHOLD_REPAIR_OBLIGATIONS_ENUMERATED",
        "rows": repair_rows,
        "global_guardrail": "residual ratios are diagnostics only and may not be used as threshold correction factors",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    profile = {
        "schema": "MTTCorrelatedProfileFillStatusAfterQCDThresholds.v1",
        "status": "PROFILE_BLUEPRINT_RETAINED_VALUES_OPEN",
        "imported_blueprint": rel(
            DATA
            / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
            / "higgs_correlated_profile_blueprint.packet.json"
        ),
        "full_matrix": profile_blueprint["full_matrix"],
        "qcd_block_status": {
            "block": "QCD_color_threshold",
            "channels": ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"],
            "residual_rows_filled_for": ["H_to_ss", "H_to_gg"],
            "covariance_entries_filled": 0,
            "accepted_as_correlated_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQCDThresholdRows.v1",
        "status": "QCD_THRESHOLD_RESIDUAL_ROWS_BUILT_REPAIR_AND_PROFILE_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["QCD threshold residual rows for H_to_ss and H_to_gg"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "supply non-fit QCD threshold repair values or fill correlated QCD profile block",
        "guardrails": {
            "residual_ratios_not_applied_as_corrections": True,
            "qcd_threshold_repair_values_filled": False,
            "correlated_profile_values_filled": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsQCDThresholdRowsOrCorrelatedProfileFill",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsgammagammacorrection_or_qcdthresholdrows.candidate.json"),
            "ss_kernel": rel(
                DATA
                / "selected_higgssskernelrow_or_remainingchannels"
                / "higgs_ss_running_mass_kernel_row.packet.json"
            ),
            "gg_kernel": rel(
                DATA
                / "selected_higgsggkernelrow_or_electroweakrows"
                / "higgs_gg_heavytop_kernel_row.packet.json"
            ),
            "profile_blueprint": rel(
                DATA
                / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
                / "higgs_correlated_profile_blueprint.packet.json"
            ),
        },
        "output_packets": {
            "qcd_threshold_residual_rows": rel(RESIDUALS),
            "qcd_threshold_repair_obligations": rel(REPAIR),
            "correlated_profile_fill_status": rel(PROFILE),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsQCDThresholdResidualRowsTheorem",
            "proved": True,
            "statement": (
                "The QCD pressure rows H_to_ss and H_to_gg can be reduced to explicit residual and repair "
                "obligations. The benchmark/proxy ratios are recorded only as forbidden fit factors; true promotion "
                "requires independent threshold, scheme, covariance, and Qa/SU3 operator data."
            ),
        },
        "what_closes_now": {
            "QCD_threshold_residual_rows": True,
            "forbidden_fit_factor_guard": True,
            "QCD_repair_obligation_table": True,
            "correlated_profile_QCD_block_status": True,
        },
        "what_remains_open": {
            "non_fit_QCD_threshold_repair_values": True,
            "correlated_QCD_profile_block": True,
            "selected_Qa_SU3_operator_attachment": True,
            "accepted_precision_formula_rows": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "residual_rows_closed": True,
            "threshold_repair_values_filled": False,
            "correlated_profile_values_filled": False,
            "precision_rows_promoted": 0,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDThresholdRows_or_CorrelatedProfileFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "residual_rows_closed": True,
        "threshold_repair_values_filled": False,
        "correlated_profile_values_filled": False,
        "precision_rows_promoted": 0,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1",
    }

    note = """# MTT Selected HiggsQCDThresholdRows or CorrelatedProfileFill v1

Status: `MTT_SELECTED_HIGGSQCDTHRESHOLDROWS_OR_CORRELATEDPROFILEFILL_BUILT_RESIDUALS_REPAIR_OPEN`.

This artifact follows the QCD threshold gate selected by the gamma-gamma
extension. It computes residual rows for `H_to_ss` and `H_to_gg`, records the
benchmark/proxy ratios only as forbidden fit factors, and enumerates the
independent repair data needed for promotion.

No threshold correction value is filled here. No row is promoted to precision,
and the correlated profile remains open.
"""

    for path, payload in [
        (RESIDUALS, residuals),
        (REPAIR, repair),
        (PROFILE, profile),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
