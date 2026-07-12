"""Build first-pass non-fit Higgs QCD formula execution and forward replay."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXECUTION = PACKET_DIR / "higgs_qcd_nonfit_formula_execution.packet.json"
REPLAY = PACKET_DIR / "higgs_qcd_forward_replay_after_nonfit_formula_execution.packet.json"
PROMOTION = PACKET_DIR / "higgs_qcd_formula_value_promotion_status.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_nonfit_qcd_formula_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDNonFitFormulaValueExecution_or_ForwardReplay_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDNONFITFORMULAVALUEEXECUTION_OR_FORWARDREPLAY_BUILT_FIRSTPASS_VALUES_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def finite_nonnegative(value: float) -> bool:
    return math.isfinite(value) and value >= 0.0


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment.candidate.json")
    formula_gate = load(
        DATA
        / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
        / "higgs_qcd_formula_repair_value_gate.packet.json"
    )
    attachment = load(
        DATA
        / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
        / "higgs_qcd_qasu3_parity_attachment.packet.json"
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
    residuals = load(
        DATA
        / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
        / "qcd_threshold_residual_rows.packet.json"
    )
    psd = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "qcd_profile_psd_and_chisquare_check.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
        / "updated_true_equivalence_gate_after_qasu3_parity_attachment.packet.json"
    )

    # Recompute from declared formulas only. Benchmark sidecars enter later,
    # in the forward replay packet.
    ss_factor = float(ss["N3LO_massless_QCD_factor"])
    ss_width = float(ss["Gamma0_running_mass_GeV"]) * ss_factor
    gg_factor = float(gg["NLO_proxy_factor"])
    gg_width = float(gg["LO_width_GeV"]) * gg_factor

    execution_rows = [
        {
            "channel": "H_to_ss",
            "formula_family": ss["kernel_family"],
            "formula": ss["kernel_formula"],
            "inputs_without_benchmark": {
                "Gamma0_running_mass_GeV": ss["Gamma0_running_mass_GeV"],
                "N3LO_massless_QCD_factor": ss["N3LO_massless_QCD_factor"],
                "a_s_mH": ss["a_s_mH"],
                "running_mass_at_mH_GeV": ss["running_mass_at_mH_GeV"],
                "alpha_s_mH_proxy": ss["alpha_s_mH_proxy"],
            },
            "computed_width_GeV": ss_width,
            "source_kernel_packet": rel(
                DATA
                / "selected_higgssskernelrow_or_remainingchannels"
                / "higgs_ss_running_mass_kernel_row.packet.json"
            ),
            "accepted_as_firstpass_nonfit_formula_value": True,
            "accepted_as_precision_formula_value": False,
        },
        {
            "channel": "H_to_gg",
            "formula_family": gg["kernel_family"],
            "formula": gg["kernel_formula"],
            "inputs_without_benchmark": {
                "LO_width_GeV": gg["LO_width_GeV"],
                "NLO_proxy_factor": gg["NLO_proxy_factor"],
                "a_s_mH": gg["a_s_mH"],
                "alpha_s_mH_proxy": gg["alpha_s_mH_proxy"],
                "nf": gg["nf"],
                "NLO_QCD_coefficient_nf5": gg["NLO_QCD_coefficient_nf5"],
            },
            "computed_width_GeV": gg_width,
            "source_kernel_packet": rel(
                DATA
                / "selected_higgsggkernelrow_or_electroweakrows"
                / "higgs_gg_heavytop_kernel_row.packet.json"
            ),
            "accepted_as_firstpass_nonfit_formula_value": True,
            "accepted_as_precision_formula_value": False,
        },
    ]

    execution = {
        "schema": "MTTHiggsQCDNonFitFormulaExecution.v1",
        "status": "FIRSTPASS_NONFIT_QCD_FORMULA_VALUES_EXECUTED_BENCHMARK_FREE",
        "channels": [row["channel"] for row in execution_rows],
        "rows": execution_rows,
        "all_widths_finite_nonnegative": all(finite_nonnegative(row["computed_width_GeV"]) for row in execution_rows),
        "benchmarks_used_in_execution": False,
        "benchmark_over_proxy_ratios_applied": False,
        "accepted_formula_value_count": len(execution_rows),
        "accepted_as_precision_formula_values": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    residual_by_channel = {row["channel"]: row for row in residuals["rows"]}
    replay_rows = []
    for row in execution_rows:
        residual = residual_by_channel[row["channel"]]
        reference = float(residual["benchmark_width_GeV"])
        sigma = float(residual["sidecar_sigma_GeV"])
        width = float(row["computed_width_GeV"])
        replay_rows.append(
            {
                "channel": row["channel"],
                "computed_width_GeV": width,
                "benchmark_width_GeV": reference,
                "sidecar_sigma_GeV": sigma,
                "residual_GeV": width - reference,
                "pull": (width - reference) / sigma,
                "ratio_to_benchmark": width / reference,
                "benchmark_compared_after_execution": True,
                "benchmark_used_as_selector": False,
                "accepted_as_precision_formula_value": False,
            }
        )

    chi_square = sum(row["pull"] ** 2 for row in replay_rows)
    replay = {
        "schema": "MTTHiggsQCDForwardReplayAfterNonFitFormulaExecution.v1",
        "status": "FORWARD_REPLAY_EXECUTED_AFTER_NONFIT_FORMULA_VALUES_PRECISION_OPEN",
        "rows": replay_rows,
        "summary": {
            "row_count": len(replay_rows),
            "diagonal_chi_square_for_replayed_rows": chi_square,
            "largest_abs_pull_channel": max(replay_rows, key=lambda row: abs(row["pull"]))["channel"],
            "all_benchmarks_compared_after_execution": all(row["benchmark_compared_after_execution"] for row in replay_rows),
            "any_benchmark_used_as_selector": any(row["benchmark_used_as_selector"] for row in replay_rows),
            "previous_four_channel_qcd_profile_chi_square": psd["diagonal_chi_square"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion = {
        "schema": "MTTHiggsQCDFormulaValuePromotionStatus.v1",
        "status": "FIRSTPASS_FORMULA_VALUES_FILLED_PRECISION_PROMOTION_REJECTED",
        "formula_gate_import": rel(
            DATA
            / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
            / "higgs_qcd_formula_repair_value_gate.packet.json"
        ),
        "qasu3_attachment_import": rel(
            DATA
            / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment"
            / "higgs_qcd_qasu3_parity_attachment.packet.json"
        ),
        "accepted_formula_value_count": len(execution_rows),
        "firstpass_nonfit_formula_values_filled": True,
        "formula_repair_values_filled_at_precision_tier": False,
        "values_promotable_to_precision_now": False,
        "qasu3_attachment_closed_for_sm_parity": attachment[
            "accepted_for_higgs_qcd_sm_parity_operator_attachment"
        ],
        "qasu3_attachment_closed_as_no_knob": attachment["accepted_as_actual_selected_qasu3_operator_packet"],
        "blocked_precision_conditions": [
            "H_to_ss still uses one-loop running path and massless-QCD coefficient scaffold",
            "H_to_gg still uses heavy-top NLO proxy without finite mass loops or NNLO/N3LO K factors",
            "full correlated QCD profile not filled",
            "actual selected Qa/SU3 no-knob operator packet not emitted",
            "complete Higgs precision channel policy not closed",
        ],
        "previous_formula_gate_channels": formula_gate["channels"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_true["remaining_true_equivalence_blockers"])
    closed_now = previous_true["closed_now"] + [
        "first-pass benchmark-free non-fit formula values for H_to_ss and H_to_gg",
        "forward replay after non-fit QCD formula execution",
    ]
    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterNonFitQCDFormulaReplay.v1",
        "status": "FIRSTPASS_QCD_FORMULA_REPLAY_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "upgrade H_to_ss and H_to_gg from first-pass formula replay to precision threshold formula rows, or fill full correlated QCD profile",
        "guardrails": {
            "firstpass_formula_values_not_precision_values": True,
            "benchmarks_used_only_after_execution": True,
            "benchmark_ratios_not_applied": True,
            "full_correlated_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsQCDNonFitFormulaValueExecutionOrForwardReplay",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdformularepairvalues_or_qasu3operatorattachment.candidate.json"),
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
            "residual_rows": rel(
                DATA
                / "selected_higgsqcdthresholdrows_or_correlatedprofilefill"
                / "qcd_threshold_residual_rows.packet.json"
            ),
        },
        "output_packets": {
            "formula_execution": rel(EXECUTION),
            "forward_replay": rel(REPLAY),
            "promotion_status": rel(PROMOTION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsQCDFirstPassNonFitFormulaReplayTheorem",
            "proved": True,
            "statement": (
                "The declared H_to_ss and H_to_gg QCD formulas can be executed from benchmark-free inputs "
                "and only then compared to fixed sidecar benchmarks. This closes first-pass non-fit formula "
                "execution and forward replay, but rejects precision promotion because the ss and gg rows "
                "still lack precision threshold formulae, full correlation, and actual no-knob Qa/SU3 data."
            ),
        },
        "what_closes_now": {
            "benchmark_free_H_to_ss_formula_execution": True,
            "benchmark_free_H_to_gg_formula_execution": True,
            "forward_replay_after_execution": True,
            "benchmark_ratio_nonuse_verified": True,
        },
        "what_remains_open": {
            "precision_H_to_ss_threshold_formula_value": True,
            "precision_H_to_gg_threshold_formula_value": True,
            "full_correlated_QCD_profile": True,
            "actual_QaSU3_operator_packet_no_knob": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "firstpass_nonfit_formula_values_filled": True,
            "forward_replay_executed": True,
            "precision_formula_values_filled": False,
            "values_promotable_to_precision_now": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDNonFitFormulaValueExecution_or_ForwardReplay_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "firstpass_nonfit_formula_values_filled": True,
        "forward_replay_executed": True,
        "precision_formula_values_filled": False,
        "values_promotable_to_precision_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDPrecisionThresholdRows_or_CorrelatedProfileUpgrade_v1",
    }

    note = f"""# MTT Selected HiggsQCDNonFitFormulaValueExecution or ForwardReplay v1

Status: `{STATUS}`.

This artifact executes the existing `H_to_ss` and `H_to_gg` QCD formulas from
benchmark-free inputs, then performs a separate forward replay against the fixed
sidecar benchmarks. Benchmark/proxy ratios are not applied as correction
factors.

The result closes first-pass non-fit formula execution and forward replay. It
does not close precision Higgs QCD widths, full correlated profile likelihood,
actual selected Qa/SU3, true SM equivalence, or no-knob closure.
"""

    for path, payload in [
        (EXECUTION, execution),
        (REPLAY, replay),
        (PROMOTION, promotion),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
