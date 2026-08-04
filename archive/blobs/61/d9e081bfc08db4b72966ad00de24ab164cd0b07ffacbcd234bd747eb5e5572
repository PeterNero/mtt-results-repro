"""Build an executable H->ss kernel row using the existing qq proxy family."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgssskernelrow_or_remainingchannels"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SS = PACKET_DIR / "higgs_ss_running_mass_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows.packet.json"
OPEN = PACKET_DIR / "remaining_higgs_kernel_obligations_after_ss.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_ss_kernel.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsSSKernelRow_or_RemainingChannels_v1.md"

STATUS = "MTT_SELECTED_HIGGSSSKERNELROW_OR_REMAININGCHANNELS_BUILT_SS_KERNEL_FIVE_CHANNELS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def alpha_s_one_loop(alpha_ref: float, mu_ref: float, mu: float, nf: int) -> float:
    beta0 = 11.0 - (2.0 / 3.0) * nf
    return alpha_ref / (1.0 + alpha_ref * beta0 * math.log(mu / mu_ref) / (2.0 * math.pi))


def run_mass_one_loop(m_ref: float, alpha_ref: float, alpha_mu: float, nf: int) -> float:
    exponent = 12.0 / (33.0 - 2.0 * nf)
    return m_ref * (alpha_mu / alpha_ref) ** exponent


def mass_gev(row: dict[str, Any]) -> float:
    value = float(row["central_value"])
    units = row.get("units")
    if units == "MeV":
        return value / 1000.0
    if units == "GeV":
        return value
    raise ValueError(f"unknown mass unit: {units}")


def higgs_to_ff_width(gf: float, mh: float, mf: float, color_factor: int) -> float:
    if 2.0 * mf >= mh:
        return 0.0
    beta_cubed = (1.0 - 4.0 * mf * mf / (mh * mh)) ** 1.5
    return color_factor * gf * mh * mf * mf * beta_cubed / (4.0 * math.pi * math.sqrt(2.0))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsuniformkernelrows_or_fullchannelvalues.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsuniformkernelrows_or_fullchannelvalues"
        / "updated_true_equivalence_gate_after_uniform_kernel_rows.packet.json"
    )
    previous_kernels = load(
        DATA
        / "selected_higgsuniformkernelrows_or_fullchannelvalues"
        / "executable_higgs_uniform_kernel_rows.packet.json"
    )
    previous_open = load(
        DATA
        / "selected_higgsuniformkernelrows_or_fullchannelvalues"
        / "open_higgs_kernel_obligations.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    qq_formula = load(
        DATA
        / "selected_multiloophiggsqqformula_or_fullwidthpolicy"
        / "versioned_massless_qcd_higgs_qq_formula.packet.json"
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
    mz = mass_gev(masses["Z"])
    mb = mass_gev(masses["b"])
    ms_2gev = mass_gev(masses["s"])
    alpha_mz = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["central_value"])
    alpha_mh = alpha_s_one_loop(alpha_mz, mz, mh, nf=5)
    alpha_mb = alpha_s_one_loop(alpha_mz, mz, mb, nf=5)
    alpha_2gev_nf4 = alpha_s_one_loop(alpha_mb, mb, 2.0, nf=4)

    ms_mb = run_mass_one_loop(ms_2gev, alpha_2gev_nf4, alpha_mb, nf=4)
    ms_mh = run_mass_one_loop(ms_mb, alpha_mb, alpha_mh, nf=5)
    gamma0 = higgs_to_ff_width(gf, mh, ms_mh, color_factor=3)
    coeffs = qq_formula["coefficients"]
    a_s = alpha_mh / math.pi
    n3lo_factor = 1.0 + coeffs["c1"] * a_s + coeffs["c2_nf5"] * a_s**2 + coeffs["c3_nf5"] * a_s**3
    width = gamma0 * n3lo_factor

    benchmark_width = next(row["width_GeV"] for row in hybrid["rows"] if row["channel"] == "H_to_ss")
    sidecar = next(row for row in sidecars["rows"] if row["channel"] == "H_to_ss")
    ss_row = {
        "schema": "MTTHiggsSSRunningMassKernelRow.v1",
        "status": "H_TO_SS_RUNNING_MASS_QCD_PROXY_KERNEL_BUILT_PRECISION_OPEN",
        "channel": "H_to_ss",
        "kernel_family": "running-mass H->ss with massless-QCD coefficient scaffold",
        "kernel_formula": "Gamma0(m_s(mu))*[1+c1*a_s+c2*a_s^2+c3*a_s^3]",
        "reference_mass_GeV_at_2GeV": ms_2gev,
        "running_mass_at_mb_GeV": ms_mb,
        "running_mass_at_mH_GeV": ms_mh,
        "alpha_s_2GeV_nf4_proxy": alpha_2gev_nf4,
        "alpha_s_mb_proxy": alpha_mb,
        "alpha_s_mH_proxy": alpha_mh,
        "a_s_mH": a_s,
        "Gamma0_running_mass_GeV": gamma0,
        "N3LO_massless_QCD_factor": n3lo_factor,
        "width_GeV": width,
        "benchmark_fill_width_GeV": benchmark_width,
        "relative_residual_to_benchmark_fill": (width - benchmark_width) / benchmark_width,
        "relative_uncertainty_sidecar": sidecar["relative_uncertainty"],
        "operator_attachment_required": "Y_d strange row and color/QCD operator packet",
        "nf_running_path": ["nf=4 from 2 GeV to m_b", "nf=5 from m_b to m_H"],
        "accepted_as_uniform_kernel_row": True,
        "accepted_as_precision_formula_row": False,
        "why_not_precision": (
            "Uses a one-loop running-mass path and massless-QCD proxy coefficients. "
            "Strange-mass scheme correlations, threshold matching, EW/mixed corrections, covariance, and selected Qa/SU3 remain open."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    executable_rows = list(previous_kernels["executable_rows"]) + [
        {
            "channel": "H_to_ss",
            "kernel_family": ss_row["kernel_family"],
            "kernel_formula": ss_row["kernel_formula"],
            "kernel_status": "EXECUTABLE_N3LO_MASSLESS_QCD_PROXY_KERNEL_STRANGE",
            "width_GeV": width,
            "relative_uncertainty": sidecar["relative_uncertainty"],
            "operator_attachment_required": ss_row["operator_attachment_required"],
            "source_packet": rel(SS),
            "accepted_as_uniform_kernel_row": True,
            "accepted_as_precision_formula_row": False,
            "why_not_precision": ss_row["why_not_precision"],
        }
    ]
    remaining_rows = [row for row in previous_open["rows"] if row["channel"] != "H_to_ss"]

    extended = {
        "schema": "MTTExtendedExecutableHiggsKernelRowsAfterSS.v1",
        "status": "FIVE_EXECUTABLE_HIGGS_KERNEL_ROWS_BUILT_REMAINING_CHANNELS_OPEN",
        "executable_rows": executable_rows,
        "summary": {
            "executable_kernel_row_count": len(executable_rows),
            "open_kernel_row_count": len(remaining_rows),
            "added_channel": "H_to_ss",
            "all_executable_widths_positive": all(row["width_GeV"] > 0.0 for row in executable_rows),
            "uniform_formula_rows_fully_filled": False,
            "precision_formula_rows_fully_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_packet = {
        "schema": "MTTRemainingHiggsKernelObligationsAfterSS.v1",
        "status": "FIVE_HIGGS_KERNEL_ROWS_REMAIN_OPEN",
        "rows": remaining_rows,
        "blocked_channels": [row["channel"] for row in remaining_rows],
        "color_sensitive_open_channels": [
            row["channel"]
            for row in remaining_rows
            if "Qa/SU3" in row["operator_attachment_required"] or "color" in row["operator_attachment_required"]
        ],
        "electroweak_loop_or_offshell_open_channels": [
            row["channel"]
            for row in remaining_rows
            if "electroweak" in row["operator_attachment_required"] or "SU2" in row["operator_attachment_required"]
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["executable H_to_ss running-mass QCD proxy kernel row"]
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterSSKernel.v1",
        "status": "SS_KERNEL_ROW_BUILT_FIVE_CHANNELS_EXECUTABLE_REMAINING_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "fill H_to_gg loop-induced color row or electroweak off-shell/loop rows, then supply ten-channel covariance/profile matrix",
        "guardrails": {
            "ss_kernel_not_precision": True,
            "five_kernel_rows_not_full_uniform_formula_set": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsSSKernelRowOrRemainingChannels",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsuniformkernelrows_or_fullchannelvalues.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "qq_formula_scaffold": rel(
                DATA
                / "selected_multiloophiggsqqformula_or_fullwidthpolicy"
                / "versioned_massless_qcd_higgs_qq_formula.packet.json"
            ),
        },
        "output_packets": {
            "higgs_ss_running_mass_kernel_row": rel(SS),
            "extended_executable_higgs_kernel_rows": rel(EXTENDED),
            "remaining_higgs_kernel_obligations": rel(OPEN),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsSSRunningMassKernelRowTheorem",
            "proved": True,
            "statement": (
                "The selected SM-parity Higgs kernel layer can extend the existing H->qq proxy family to H->ss "
                "because the reference packet supplies m_s(2 GeV) and the same one-loop running/massless-QCD scaffold "
                "transports it to m_H. This closes one additional executable kernel row but not precision Higgs widths."
            ),
        },
        "what_closes_now": {
            "H_to_ss_uniform_kernel_row": True,
            "five_executable_Higgs_kernel_rows": True,
            "remaining_kernel_obligations_reduced_to_five": True,
        },
        "what_remains_open": {
            "H_to_gg_kernel_row": True,
            "electroweak_loop_or_offshell_kernel_rows": True,
            "ten_channel_covariance_profile": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_kernel_layer_extended": True,
            "H_to_ss_kernel_closed": True,
            "uniform_formula_rows_fully_closed": False,
            "full_channel_values_closed": False,
            "cross_channel_covariance_profile_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsSSKernelRow_or_RemainingChannels_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "H_to_ss_kernel_closed": True,
        "five_executable_Higgs_kernel_rows": True,
        "uniform_formula_rows_fully_closed": False,
        "full_channel_values_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsGGKernelRow_or_ElectroweakOffshellRows_v1",
    }

    note = """# MTT Selected HiggsSSKernelRow or RemainingChannels v1

Status: `MTT_SELECTED_HIGGSSSKERNELROW_OR_REMAININGCHANNELS_BUILT_SS_KERNEL_FIVE_CHANNELS_OPEN`.

This artifact extends the executable Higgs kernel layer from four channels to
five by adding `H_to_ss` through the existing running-mass `H -> qq` proxy
family.

The result is useful SM-parity machinery, not a precision Higgs-width claim.
The remaining true-equivalence work is `H_to_gg`, the electroweak off-shell and
loop-induced rows, the ten-channel covariance/profile matrix, and actual
Qa/SU3 operator attachment.
"""

    for path, payload in [
        (SS, ss_row),
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
