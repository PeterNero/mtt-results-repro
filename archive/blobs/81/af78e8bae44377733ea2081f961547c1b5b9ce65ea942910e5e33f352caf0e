"""Build an executable H->gamma gamma one-loop proxy kernel row."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsgammagammakernelrow_or_remainingew"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAMMA = PACKET_DIR / "higgs_gamma_gamma_oneloop_kernel_row.packet.json"
EXTENDED = PACKET_DIR / "extended_executable_higgs_kernel_rows_after_gamma_gamma.packet.json"
OPEN = PACKET_DIR / "remaining_electroweak_higgs_kernel_obligations_after_gamma_gamma.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_gamma_gamma_kernel.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsGammaGammaKernelRow_or_RemainingEW_v1.md"

STATUS = "MTT_SELECTED_HIGGSGAMMAGAMMAKERNELROW_OR_REMAININGEW_BUILT_GAMMAGAMMA_KERNEL_THREE_EW_ROWS_OPEN"


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


def loop_f(tau: float) -> float:
    if tau < 1.0:
        raise ValueError("this proxy only supports tau >= 1 real-loop rows")
    return math.asin(1.0 / math.sqrt(tau)) ** 2


def spin_one_amplitude(tau: float) -> float:
    f = loop_f(tau)
    return -(2.0 + 3.0 * tau + 3.0 * tau * (2.0 - tau) * f)


def spin_half_amplitude(tau: float) -> float:
    f = loop_f(tau)
    return 2.0 * tau * (1.0 + (1.0 - tau) * f)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsggkernelrow_or_electroweakrows.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgsggkernelrow_or_electroweakrows"
        / "updated_true_equivalence_gate_after_gg_kernel.packet.json"
    )
    previous_kernels = load(
        DATA
        / "selected_higgsggkernelrow_or_electroweakrows"
        / "extended_executable_higgs_kernel_rows_after_gg.packet.json"
    )
    previous_open = load(
        DATA
        / "selected_higgsggkernelrow_or_electroweakrows"
        / "remaining_electroweak_higgs_kernel_obligations.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
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
    mw = mass_gev(masses["W"])
    mt = mass_gev(masses["t"])
    alpha_em_mz = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_em_MSbar_MZ"]["central_value"])

    tau_w = 4.0 * mw * mw / (mh * mh)
    tau_t = 4.0 * mt * mt / (mh * mh)
    a_w = spin_one_amplitude(tau_w)
    a_t = spin_half_amplitude(tau_t)
    top_charge = 2.0 / 3.0
    top_color = 3.0
    amplitude = a_w + top_color * top_charge**2 * a_t
    width = gf * alpha_em_mz**2 * mh**3 * amplitude**2 / (128.0 * math.sqrt(2.0) * math.pi**3)

    benchmark_width = next(row["width_GeV"] for row in hybrid["rows"] if row["channel"] == "H_to_gamma_gamma")
    sidecar = next(row for row in sidecars["rows"] if row["channel"] == "H_to_gamma_gamma")
    gamma_row = {
        "schema": "MTTHiggsGammaGammaOneLoopKernelRow.v1",
        "status": "H_TO_GAMMA_GAMMA_ONE_LOOP_PROXY_KERNEL_BUILT_PRECISION_OPEN",
        "channel": "H_to_gamma_gamma",
        "kernel_family": "one-loop H->gamma gamma W/top proxy kernel",
        "kernel_formula": "Gamma=G_F*alpha^2*m_H^3*|A_1(tau_W)+N_c*Q_t^2*A_1/2(tau_t)|^2/(128*sqrt(2)*pi^3)",
        "G_F_GeV_minus2": gf,
        "mH_GeV": mh,
        "mW_GeV": mw,
        "mt_GeV": mt,
        "alpha_em_MSbar_MZ": alpha_em_mz,
        "tau_W": tau_w,
        "tau_t": tau_t,
        "A_W": a_w,
        "A_top_spin_half": a_t,
        "amplitude": amplitude,
        "width_GeV": width,
        "benchmark_fill_width_GeV": benchmark_width,
        "relative_residual_to_benchmark_fill": (width - benchmark_width) / benchmark_width,
        "relative_uncertainty_sidecar": sidecar["relative_uncertainty"],
        "operator_attachment_required": "electroweak charge/operator packet with W and top charged-loop representations",
        "accepted_as_uniform_kernel_row": True,
        "accepted_as_precision_formula_row": False,
        "why_not_precision": (
            "This is a one-loop W/top proxy using alpha_em(M_Z). It omits bottom/tau loops, QCD/EW higher-order "
            "corrections, input-scheme conversion, covariance/profile treatment, and selected electroweak operator data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    executable_rows = list(previous_kernels["executable_rows"]) + [
        {
            "channel": "H_to_gamma_gamma",
            "kernel_family": gamma_row["kernel_family"],
            "kernel_formula": gamma_row["kernel_formula"],
            "kernel_status": "EXECUTABLE_ONE_LOOP_GAMMA_GAMMA_PROXY_KERNEL",
            "width_GeV": width,
            "relative_uncertainty": sidecar["relative_uncertainty"],
            "operator_attachment_required": gamma_row["operator_attachment_required"],
            "source_packet": rel(GAMMA),
            "accepted_as_uniform_kernel_row": True,
            "accepted_as_precision_formula_row": False,
            "why_not_precision": gamma_row["why_not_precision"],
        }
    ]
    remaining_rows = [row for row in previous_open["rows"] if row["channel"] != "H_to_gamma_gamma"]

    extended = {
        "schema": "MTTExtendedExecutableHiggsKernelRowsAfterGammaGamma.v1",
        "status": "SEVEN_EXECUTABLE_HIGGS_KERNEL_ROWS_BUILT_THREE_EW_ROWS_OPEN",
        "executable_rows": executable_rows,
        "summary": {
            "executable_kernel_row_count": len(executable_rows),
            "open_kernel_row_count": len(remaining_rows),
            "added_channel": "H_to_gamma_gamma",
            "all_executable_widths_positive": all(row["width_GeV"] > 0.0 for row in executable_rows),
            "uniform_formula_rows_fully_filled": False,
            "precision_formula_rows_fully_accepted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    open_packet = {
        "schema": "MTTRemainingElectroweakHiggsKernelObligationsAfterGammaGamma.v1",
        "status": "THREE_ELECTROWEAK_HIGGS_KERNEL_ROWS_REMAIN_OPEN",
        "rows": remaining_rows,
        "blocked_channels": [row["channel"] for row in remaining_rows],
        "electroweak_loop_or_offshell_open_channels": [row["channel"] for row in remaining_rows],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["executable H_to_gamma_gamma one-loop proxy kernel row"]
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterGammaGammaKernel.v1",
        "status": "GAMMAGAMMA_KERNEL_ROW_BUILT_THREE_EW_ROWS_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "fill electroweak off-shell/mixed rows WW*, ZZ*, and Z gamma; then supply ten-channel covariance/profile matrix",
        "guardrails": {
            "gamma_gamma_kernel_not_precision": True,
            "seven_kernel_rows_not_full_uniform_formula_set": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsGammaGammaKernelRowOrRemainingEW",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsggkernelrow_or_electroweakrows.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "gauge_replay": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        },
        "output_packets": {
            "higgs_gamma_gamma_oneloop_kernel_row": rel(GAMMA),
            "extended_executable_higgs_kernel_rows": rel(EXTENDED),
            "remaining_electroweak_higgs_kernel_obligations": rel(OPEN),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsGammaGammaOneLoopProxyKernelRowTheorem",
            "proved": True,
            "statement": (
                "The SM-parity Higgs kernel layer can add an executable one-loop H->gamma gamma W/top proxy row "
                "from G_F, alpha_em(M_Z), m_H, m_W, and m_t. This closes one additional electroweak loop proxy row "
                "while preserving the open precision, covariance, and selected-operator obligations."
            ),
        },
        "what_closes_now": {
            "H_to_gamma_gamma_uniform_proxy_kernel_row": True,
            "seven_executable_Higgs_kernel_rows": True,
            "remaining_kernel_obligations_reduced_to_three_EW_rows": True,
        },
        "what_remains_open": {
            "H_to_WW_star_kernel_row": True,
            "H_to_ZZ_star_kernel_row": True,
            "H_to_Z_gamma_kernel_row": True,
            "ten_channel_covariance_profile": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_kernel_layer_extended": True,
            "H_to_gamma_gamma_proxy_kernel_closed": True,
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
        "certificate": "MTT_Selected_HiggsGammaGammaKernelRow_or_RemainingEW_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "H_to_gamma_gamma_proxy_kernel_closed": True,
        "seven_executable_Higgs_kernel_rows": True,
        "uniform_formula_rows_fully_closed": False,
        "full_channel_values_closed": False,
        "cross_channel_covariance_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsRemainingEWKernelRows_or_CovarianceProfileValues_v1",
    }

    note = """# MTT Selected HiggsGammaGammaKernelRow or RemainingEW v1

Status: `MTT_SELECTED_HIGGSGAMMAGAMMAKERNELROW_OR_REMAININGEW_BUILT_GAMMAGAMMA_KERNEL_THREE_EW_ROWS_OPEN`.

This artifact adds an executable one-loop `H_to_gamma_gamma` W/top proxy kernel
to the ten-channel Higgs row basis.

The row is not a precision Higgs-width claim. It omits higher-order
corrections, smaller charged-loop terms, scheme conversion, covariance/profile
values, and selected electroweak operator attachment.
"""

    for path, payload in [
        (GAMMA, gamma_row),
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
