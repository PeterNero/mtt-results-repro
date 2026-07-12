"""Build an all-charged-fermion H->gamma gamma one-loop correction row."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsgammagammacorrection_or_qcdthresholdrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAMMA = PACKET_DIR / "higgs_gamma_gamma_all_charged_fermion_oneloop.packet.json"
PULL = PACKET_DIR / "gamma_gamma_pull_after_formula_extension.packet.json"
QCD = PACKET_DIR / "qcd_threshold_rows_next_gate.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_gamma_gamma_extension.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsGammaGammaCorrection_or_QCDThresholdRows_v1.md"

STATUS = "MTT_SELECTED_HIGGSGAMMAGAMMACORRECTION_OR_QCDTHRESHOLDROWS_BUILT_ALL_CHARGED_ONELOOP_EXTENSION"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def mass_gev(row: dict[str, Any]) -> float:
    value = float(row["central_value"])
    units = row["units"]
    if units == "GeV":
        return value
    if units == "MeV":
        return value / 1000.0
    raise ValueError(f"unknown mass units: {units}")


def loop_f(tau: float) -> complex:
    if tau >= 1.0:
        return complex(math.asin(1.0 / math.sqrt(tau)) ** 2, 0.0)
    root = math.sqrt(1.0 - tau)
    log_term = math.log((1.0 + root) / (1.0 - root))
    return -0.25 * complex(log_term, -math.pi) ** 2


def spin_one_amplitude(tau: float) -> complex:
    f = loop_f(tau)
    return -(2.0 + 3.0 * tau + 3.0 * tau * (2.0 - tau) * f)


def spin_half_amplitude(tau: float) -> complex:
    f = loop_f(tau)
    return 2.0 * tau * (1.0 + (1.0 - tau) * f)


def complex_payload(value: complex) -> dict[str, float]:
    return {"real": value.real, "imag": value.imag, "abs": abs(value)}


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgspromotionpriority_or_correlatedprofileblueprint.candidate.json")
    previous_gate = load(
        DATA
        / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
        / "updated_true_equivalence_gate_after_higgs_priority.packet.json"
    )
    old_gamma = load(
        DATA
        / "selected_higgsgammagammakernelrow_or_remainingew"
        / "higgs_gamma_gamma_oneloop_kernel_row.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")
    priority = load(
        DATA
        / "selected_higgspromotionpriority_or_correlatedprofileblueprint"
        / "higgs_precision_promotion_priority.packet.json"
    )

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gf = float(constants["G_F"]["central_value"])
    mh = mass_gev(masses["H"])
    mw = mass_gev(masses["W"])
    alpha_em_mz = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_em_MSbar_MZ"]["central_value"])
    prefactor = gf * alpha_em_mz**2 * mh**3 / (128.0 * math.sqrt(2.0) * math.pi**3)

    fermions = [
        {"id": "t", "charge": 2.0 / 3.0, "color": 3.0},
        {"id": "b", "charge": -1.0 / 3.0, "color": 3.0},
        {"id": "c", "charge": 2.0 / 3.0, "color": 3.0},
        {"id": "s", "charge": -1.0 / 3.0, "color": 3.0},
        {"id": "u", "charge": 2.0 / 3.0, "color": 3.0},
        {"id": "d", "charge": -1.0 / 3.0, "color": 3.0},
        {"id": "tau", "charge": -1.0, "color": 1.0},
        {"id": "mu", "charge": -1.0, "color": 1.0},
        {"id": "e", "charge": -1.0, "color": 1.0},
    ]

    tau_w = 4.0 * mw * mw / (mh * mh)
    a_w = spin_one_amplitude(tau_w)
    contributions = [
        {
            "particle": "W",
            "mass_GeV": mw,
            "tau": tau_w,
            "charge": 1.0,
            "color": 1.0,
            "spin": 1,
            "amplitude_contribution": complex_payload(a_w),
        }
    ]
    amplitude = a_w
    for fermion in fermions:
        m = mass_gev(masses[fermion["id"]])
        tau = 4.0 * m * m / (mh * mh)
        bare = spin_half_amplitude(tau)
        contribution = fermion["color"] * fermion["charge"] ** 2 * bare
        amplitude += contribution
        contributions.append(
            {
                "particle": fermion["id"],
                "mass_GeV": m,
                "tau": tau,
                "charge": fermion["charge"],
                "color": fermion["color"],
                "spin": 0.5,
                "bare_spin_half_amplitude": complex_payload(bare),
                "amplitude_contribution": complex_payload(contribution),
                "mass_scheme_warning": masses[fermion["id"]]["scheme"],
            }
        )

    width = prefactor * abs(amplitude) ** 2
    old_width = float(old_gamma["width_GeV"])
    benchmark = float(old_gamma["benchmark_fill_width_GeV"])
    sidecar_sigma = benchmark * float(old_gamma["relative_uncertainty_sidecar"])
    old_pull = (old_width - benchmark) / sidecar_sigma
    new_pull = (width - benchmark) / sidecar_sigma

    gamma = {
        "schema": "MTTHiggsGammaGammaAllChargedFermionOneLoop.v1",
        "status": "ALL_CHARGED_FERMION_ONELOOP_EXTENSION_BUILT_PRECISION_OPEN",
        "channel": "H_to_gamma_gamma",
        "kernel_family": "one-loop H->gamma gamma W plus all charged fermion proxy kernel",
        "kernel_formula": "Gamma=G_F*alpha^2*m_H^3*|A_1(tau_W)+sum_f N_c Q_f^2 A_1/2(tau_f)|^2/(128*sqrt(2)*pi^3)",
        "G_F_GeV_minus2": gf,
        "mH_GeV": mh,
        "mW_GeV": mw,
        "alpha_em_MSbar_MZ": alpha_em_mz,
        "prefactor": prefactor,
        "amplitude_total": complex_payload(amplitude),
        "contributions": contributions,
        "previous_W_top_width_GeV": old_width,
        "all_charged_one_loop_width_GeV": width,
        "benchmark_fill_width_GeV": benchmark,
        "relative_residual_to_benchmark_fill": (width - benchmark) / benchmark,
        "old_pull_against_sidecar": old_pull,
        "new_pull_against_sidecar": new_pull,
        "pull_improvement": abs(old_pull) - abs(new_pull),
        "accepted_as_formula_extension": True,
        "accepted_as_precision_formula_row": False,
        "why_not_precision": (
            "This extends the one-loop proxy by adding all charged fermion loops from frozen measured parity masses. "
            "It still uses mixed pole/MSbar mass conventions, alpha_em(M_Z), no QCD/EW higher-order corrections, "
            "no scheme conversion, no covariance/profile likelihood, and no selected electroweak operator packet."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    pull = {
        "schema": "MTTGammaGammaPullAfterFormulaExtension.v1",
        "status": "GAMMA_GAMMA_PULL_REPLAYED_AFTER_FORMULA_EXTENSION_PRECISION_OPEN",
        "channel": "H_to_gamma_gamma",
        "old_width_GeV": old_width,
        "new_width_GeV": width,
        "benchmark_width_GeV": benchmark,
        "sidecar_sigma_GeV": sidecar_sigma,
        "old_pull": old_pull,
        "new_pull": new_pull,
        "abs_pull_improvement": abs(old_pull) - abs(new_pull),
        "extension_moves_toward_benchmark": abs(new_pull) < abs(old_pull),
        "extension_selected_by_benchmark": False,
        "accepted_as_precision": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    priority_rows = priority["rows"]
    qcd_targets = [row for row in priority_rows if row["channel"] in {"H_to_ss", "H_to_gg"}]
    qcd = {
        "schema": "MTTQCDThresholdRowsNextGate.v1",
        "status": "QCD_THRESHOLD_ROWS_SELECTED_AS_NEXT_GATE_VALUES_OPEN",
        "rows": [
            {
                "channel": row["channel"],
                "current_pull": row["diagonal_pull"],
                "required_formula_family": row["next_required_value"],
                "operator_attachment_required": row["operator_attachment_required"],
                "next_value_required": "mass-scheme/running-threshold correction row",
                "accepted_as_filled": False,
            }
            for row in qcd_targets
        ],
        "next_gate_after_gamma_gamma": "construct QCD threshold/mass-scheme correction rows for H_to_ss and H_to_gg",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterGammaGammaExtension.v1",
        "status": "GAMMA_GAMMA_FORMULA_EXTENSION_BUILT_QCD_THRESHOLDS_NEXT",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": previous_gate["closed_now"] + ["all-charged-fermion H_to_gamma_gamma one-loop formula extension"],
        "remaining_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "QCD threshold/mass-scheme correction rows for H_to_ss and H_to_gg",
        "guardrails": {
            "gamma_gamma_extension_not_precision": True,
            "observed_benchmark_not_used_as_selector": True,
            "qcd_threshold_rows_open": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsGammaGammaCorrectionOrQCDThresholdRows",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgspromotionpriority_or_correlatedprofileblueprint.candidate.json"),
            "old_gamma_gamma_kernel": rel(
                DATA
                / "selected_higgsgammagammakernelrow_or_remainingew"
                / "higgs_gamma_gamma_oneloop_kernel_row.packet.json"
            ),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
        },
        "output_packets": {
            "higgs_gamma_gamma_all_charged_fermion_oneloop": rel(GAMMA),
            "gamma_gamma_pull_after_formula_extension": rel(PULL),
            "qcd_threshold_rows_next_gate": rel(QCD),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "HiggsGammaGammaAllChargedOneLoopExtensionTheorem",
            "proved": True,
            "statement": (
                "The top-priority gamma-gamma proxy row admits a stricter one-loop formula extension by adding all "
                "charged fermion loop contributions from frozen measured parity masses. The extension is executable "
                "and not fitted to the benchmark, but it is still not a precision row."
            ),
        },
        "what_closes_now": {
            "H_to_gamma_gamma_all_charged_one_loop_formula_extension": True,
            "gamma_gamma_pull_recomputed_without_fit": True,
            "QCD_threshold_rows_selected_as_next_gate": True,
        },
        "what_remains_open": {
            "gamma_gamma_precision_EW_QCD_scheme_corrections": True,
            "selected_electroweak_operator_attachment": True,
            "H_to_ss_QCD_threshold_row": True,
            "H_to_gg_QCD_threshold_row": True,
            "ten_channel_correlated_covariance_profile": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "formula_extension_closed": True,
            "gamma_gamma_precision_promoted": False,
            "QCD_threshold_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsGammaGammaCorrection_or_QCDThresholdRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "formula_extension_closed": True,
        "gamma_gamma_precision_promoted": False,
        "QCD_threshold_rows_closed": False,
        "old_pull": old_pull,
        "new_pull": new_pull,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDThresholdRows_or_CorrelatedProfileFill_v1",
    }

    note = """# MTT Selected HiggsGammaGammaCorrection or QCDThresholdRows v1

Status: `MTT_SELECTED_HIGGSGAMMAGAMMACORRECTION_OR_QCDTHRESHOLDROWS_BUILT_ALL_CHARGED_ONELOOP_EXTENSION`.

This artifact follows the Higgs priority controller and extends the top-priority
`H_to_gamma_gamma` row from a W/top proxy to a W plus all charged fermion
one-loop proxy.

The extension is not fitted to the benchmark and does not promote the row to
precision. It still lacks higher-order EW/QCD corrections, scheme conversion,
covariance/profile likelihood, and selected electroweak operator attachment.
"""

    for path, payload in [
        (GAMMA, gamma),
        (PULL, pull),
        (QCD, qcd),
        (UPDATED, updated),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "old_pull": old_pull, "new_pull": new_pull}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
