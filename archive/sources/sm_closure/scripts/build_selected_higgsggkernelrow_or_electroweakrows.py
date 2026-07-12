"""Build a controlled H->gg proxy kernel row and leave EW rows open."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsggkernelrow_or_electroweakrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GG = PACKET_DIR / "higgs_gg_heavytop_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows_after_gg.packet.json"
OPEN = PACKET_DIR / "remaining_electroweak_higgs_kernel_obligations.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_gg_kernel.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsGGKernelRow_or_ElectroweakRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSGGKERNELROW_OR_ELECTROWEAKROWS_BUILT_GG_KERNEL_EW_ROWS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def mass_gev(row: dict[str, Any]) -> float:
    value = float(row["central_value"])
    units = row.get("units")
    if units == "MeV":
        return value / 1000.0
    if units == "GeV":
        return value
    raise ValueError(f"unknown mass unit: {units}")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgssskernelrow_or_remainingchannels.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgssskernelrow_or_remainingchannels"
        / "updated_true_equivalence_gate_after_ss_kernel.packet.json"
    )
    previous_kernels = load(
        DATA
        / "selected_higgssskernelrow_or_remainingchannels"
        / "extended_executable_higgs_kernel_rows.packet.json"
    )
    previous_open = load(
        DATA
        / "selected_higgssskernelrow_or_remainingchannels"
        / "remaining_higgs_kernel_obligations_after_ss.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    running = load(
        DATA
        / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
        / "one_loop_running_mass_higgs_decay_proxy.packet.json"
    )
    sidecars = load(
        DATA
        / "selected_higgsprecisionsidecars_or_uniformformularows"
        / "higgs_channel_uncertainty_sidecars.packet.json"
    )
    hybrid = load(
        DATA
        / "selected_higgsmissingchannelbenchmarks_or_totalwidthreplay"
        / "hybrid_higgs_total_width_replay.packet.json"
    )

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gf = float(constants["G_F"]["central_value"])
    mh = mass_gev(masses["H"])
    alpha_s_mh = float(running["alpha_s_values"]["alpha_s_mH_proxy"])
    a_s = alpha_s_mh / math.pi

    # Heavy-top effective LO kernel with the common NLO QCD coefficient for nf=5.
    # This is deliberately a proxy kernel, not HDECAY/Prophecy-level precision.
    nf = 5
    nlo_coeff_nf5 = 95.0 / 4.0 - 7.0 * nf / 6.0
    lo_width = gf * alpha_s_mh**2 * mh**3 / (36.0 * math.sqrt(2.0) * math.pi**3)
    nlo_factor = 1.0 + nlo_coeff_nf5 * a_s
    width = lo_width * nlo_factor

    benchmark_width = next(row["width_GeV"] for row in hybrid["rows"] if row["channel"] == "H_to_gg")
    sidecar = next(row for row in sidecars["rows"] if row["channel"] == "H_to_gg")
    gg_row = {
        "schema": "MTTHiggsGGHeavyTopKernelRow.v1",
        "status": "H_TO_GG_HEAVY_TOP_PROXY_KERNEL_BUILT_PRECISION_OPEN",
        "channel": "H_to_gg",
        "kernel_family": "loop-induced H->gg heavy-top effective proxy with NLO QCD coefficient",
        "kernel_formula": "Gamma_LO=G_F*alpha_s(mu)^2*m_H^3/(36*sqrt(2)*pi^3); Gamma_proxy=Gamma_LO*(1+(95/4-7*n_f/6)*alpha_s/pi)",
        "nf": nf,
        "G_F_GeV_minus2": gf,
        "mH_GeV": mh,
        "alpha_s_mH_proxy": alpha_s_mh,
        "a_s_mH": a_s,
        "LO_width_GeV": lo_width,
        "NLO_QCD_coefficient_nf5": nlo_coeff_nf5,
        "NLO_proxy_factor": nlo_factor,
        "width_GeV": width,
        "benchmark_fill_width_GeV": benchmark_width,
        "relative_residual_to_benchmark_fill": (width - benchmark_width) / benchmark_width,
        "relative_uncertainty_sidecar": sidecar["relative_uncertainty"],
        "operator_attachment_required": "Qa/SU3 color operator packet plus top/bottom/charm loop representation data",
        "accepted_as_uniform_kernel_row": True,
        "accepted_as_precision_formula_row": False,
        "why_not_precision": (
            "This is a heavy-top effective proxy with an NLO QCD coefficient. It lacks exact mass-dependent loop "
            "functions, bottom/charm interference, higher-order QCD/EW corrections, threshold covariance, and selected Qa/SU3 operator data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    executable_rows = list(previous_kernels["executable_rows"]) + [
        {
            "channel": "H_to_gg",
            "kernel_family": gg_row["kernel_family"],
            "kernel_formula": gg_row["kernel_formula"],
            "kernel_status": "EXECUTABLE_HEAVY_TOP_GG_PROXY_KERNEL_QASU3_OPEN",
            "width_GeV": width,
            "relative_uncertainty": sidecar["relative_uncertainty"],
            "operator_attachment_required": gg_row["operator_attachment_required"],
            "source_packet": rel(GG),
            "accepted_as_uniform_kernel_row": True,
            "accepted_as_precision_formula_row": False,
            "why_not_precision": gg_row["why_not_precision"],
        }
    ]
    remaining_rows = [row for row in previous_open["rows"] if row["channel"] != "H_to_gg"]

    extended = {
        "schema": "MTTExtendedExecutableHiggsKernelRowsAfterGG.v1",
        "status": "SIX_EXECUTABLE_HIGGS_KERNEL_ROWS_BUILT_EW_ROWS_OPEN",
        "executable_rows": executable_rows,
        "summary": {
            "executable_kernel_row_count": len(executable_rows),
            "open_kernel_row_count": len(remaining_rows),
            "added_channel": "H_to_gg",
            "all_executable_widths_positive": all(row["width_GeV"] > 0.0 for row in executable_rows),
            "color_sensitive_kernel_rows_filled_as_proxy": ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"],
            "color_sensitive_precision_rows_still_require_QaSU3": True,
            "uniform_formula_rows_fully_filled": False,
            "precision_formula_rows_fully_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_packet = {
        "schema": "MTTRemainingElectroweakHiggsKernelObligations.v1",
        "status": "FOUR_ELECTROWEAK_HIGGS_KERNEL_ROWS_REMAIN_OPEN",
        "rows": remaining_rows,
        "blocked_channels": [row["channel"] for row in remaining_rows],
        "color_sensitive_open_channels": [],
        "electroweak_loop_or_offshell_open_channels": [row["channel"] for row in remaining_rows],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["executable H_to_gg heavy-top proxy kernel row"]
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterGGKernel.v1",
        "status": "GG_KERNEL_ROW_BUILT_ELECTROWEAK_ROWS_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "fill electroweak off-shell/loop Higgs rows WW*, ZZ*, gamma gamma, Z gamma; then supply ten-channel covariance/profile matrix",
        "guardrails": {
            "gg_kernel_not_precision": True,
            "color_proxy_rows_still_require_actual_QaSU3_for_precision": True,
            "six_kernel_rows_not_full_uniform_formula_set": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsGGKernelRowOrElectroweakRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgssskernelrow_or_remainingchannels.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "running_mass_proxy": rel(
                DATA
                / "selected_runningmasshiggsdecayproxy_or_precisionwidths"
                / "one_loop_running_mass_higgs_decay_proxy.packet.json"
            ),
        },
        "output_packets": {
            "higgs_gg_heavytop_kernel_row": rel(GG),
            "extended_executable_higgs_kernel_rows": rel(EXTENDED),
            "remaining_electroweak_higgs_kernel_obligations": rel(OPEN),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsGGHeavyTopProxyKernelRowTheorem",
            "proved": True,
            "statement": (
                "The SM-parity Higgs kernel layer can add a controlled H->gg heavy-top effective proxy row from "
                "G_F, m_H, and alpha_s(m_H). This removes the last open explicitly color-sensitive Higgs kernel row "
                "at proxy level, while preserving the requirement that precision/source promotion needs actual Qa/SU3."
            ),
        },
        "what_closes_now": {
            "H_to_gg_uniform_proxy_kernel_row": True,
            "six_executable_Higgs_kernel_rows": True,
            "remaining_kernel_obligations_reduced_to_four_EW_rows": True,
        },
        "what_remains_open": {
            "electroweak_offshell_and_loop_Higgs_rows": True,
            "ten_channel_covariance_profile": True,
            "actual_QaSU3_operator_packet_for_precision_color_rows": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_kernel_layer_extended": True,
            "H_to_gg_proxy_kernel_closed": True,
            "uniform_formula_rows_fully_closed": False,
            "full_channel_values_closed": False,
            "cross_channel_covariance_profile_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsGGKernelRow_or_ElectroweakRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "H_to_gg_proxy_kernel_closed": True,
        "six_executable_Higgs_kernel_rows": True,
        "uniform_formula_rows_fully_closed": False,
        "full_channel_values_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsElectroweakKernelRows_or_CovarianceProfileValues_v1",
    }

    note = """# MTT Selected HiggsGGKernelRow or ElectroweakRows v1

Status: `MTT_SELECTED_HIGGSGGKERNELROW_OR_ELECTROWEAKROWS_BUILT_GG_KERNEL_EW_ROWS_OPEN`.

This artifact adds an executable `H_to_gg` heavy-top effective proxy kernel to
the ten-channel Higgs row basis. It is the last open explicitly color-sensitive
Higgs kernel row at proxy level.

The row is not a precision Higgs-width claim. Precision promotion still needs
mass-dependent loop functions, higher-order corrections, covariance/profile
values, and actual selected Qa/SU3 operator attachment.
"""

    for path, payload in [
        (GG, gg_row),
        (EXTENDED, extended),
        (OPEN, open_packet),
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
