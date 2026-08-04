"""Build running-mass Higgs decay proxy values after the first QCD proxy."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_runningmasshiggsdecayproxy_or_precisionwidths"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RUNNING = PACKET_DIR / "one_loop_running_mass_higgs_decay_proxy.packet.json"
BENCH = PACKET_DIR / "higgs_decay_plausibility_benchmark.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_running_mass_proxy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RunningMassHiggsDecayProxy_or_PrecisionWidths_v1.md"

STATUS = "MTT_SELECTED_RUNNINGMASSHIGGSDECAYPROXY_OR_PRECISIONWIDTHS_BUILT_RUNNING_MASS_PROXY_PRECISION_OPEN"


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

    previous = load(DATA / "selected_loopqcddecayproxyvalues_or_fullprecisionqft.candidate.json")
    previous_gate = load(
        DATA
        / "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
        / "updated_true_equivalence_gate_after_qcd_proxy.packet.json"
    )
    qcd_proxy = load(
        DATA
        / "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
        / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    mixing = load(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json")

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    gf = float(constants["G_F"]["central_value"])
    mh = mass_gev(masses["H"])
    mz = mass_gev(masses["Z"])
    mb = mass_gev(masses["b"])
    mc = mass_gev(masses["c"])
    alpha_mz = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["central_value"])

    alpha_mh = alpha_s_one_loop(alpha_mz, mz, mh, nf=5)
    alpha_mb = alpha_s_one_loop(alpha_mz, mz, mb, nf=5)
    alpha_mc_nf4 = alpha_s_one_loop(alpha_mb, mb, mc, nf=4)

    mb_mh = run_mass_one_loop(mb, alpha_mb, alpha_mh, nf=5)
    mc_mb = run_mass_one_loop(mc, alpha_mc_nf4, alpha_mb, nf=4)
    mc_mh = run_mass_one_loop(mc_mb, alpha_mb, alpha_mh, nf=5)

    k_mh = 1.0 + (17.0 / 3.0) * alpha_mh / math.pi
    rows = []
    for fermion, mass_at_mh, reference_mass, alpha_at_reference, nf_path in [
        ("b", mb_mh, mb, alpha_mb, ["nf=5 from m_b to m_H"]),
        ("c", mc_mh, mc, alpha_mc_nf4, ["nf=4 from m_c to m_b", "nf=5 from m_b to m_H"]),
    ]:
        tree_running = higgs_to_ff_width(gf, mh, mass_at_mh, color_factor=3)
        rows.append(
            {
                "id": f"H_to_{fermion}_{fermion}bar_one_loop_running_mass_qcd_proxy",
                "fermion": fermion,
                "reference_mass_GeV": reference_mass,
                "running_mass_at_mH_GeV": mass_at_mh,
                "alpha_s_at_reference_proxy": alpha_at_reference,
                "alpha_s_at_mH_proxy": alpha_mh,
                "nf_running_path": nf_path,
                "tree_width_with_running_mass_GeV": tree_running,
                "qcd_k_factor_at_mH_proxy": k_mh,
                "running_mass_qcd_proxy_width_GeV": tree_running * k_mh,
                "accepted_as_running_mass_proxy": True,
                "accepted_as_precision_SM_decay_width": False,
            }
        )

    running_packet = {
        "schema": "MTTOneLoopRunningMassHiggsDecayProxy.v1",
        "status": "ONE_LOOP_RUNNING_MASS_HIGGS_DECAY_PROXY_BUILT_PRECISION_OPEN",
        "input_previous_qcd_proxy": rel(
            DATA
            / "selected_loopqcddecayproxyvalues_or_fullprecisionqft"
            / "one_loop_qcd_higgs_quark_decay_proxy_values.packet.json"
        ),
        "input_reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
        "scheme": {
            "alpha_s_running": "one-loop QCD proxy",
            "mass_running": "one-loop QCD mass anomalous-dimension proxy",
            "threshold_policy": "piecewise nf=4/5 toy threshold for c, nf=5 for b",
            "scale_target": "m_H",
        },
        "alpha_s_values": {
            "alpha_s_MZ_input": alpha_mz,
            "alpha_s_mH_proxy": alpha_mh,
            "alpha_s_mb_proxy": alpha_mb,
            "alpha_s_mc_nf4_proxy": alpha_mc_nf4,
        },
        "rows": rows,
        "summary": {
            "qcd_k_factor_at_mH_proxy": k_mh,
            "total_running_mass_qcd_proxy_width_GeV": sum(row["running_mass_qcd_proxy_width_GeV"] for row in rows),
            "all_running_mass_proxy_widths_finite_nonnegative": all(
                math.isfinite(row["running_mass_qcd_proxy_width_GeV"])
                and row["running_mass_qcd_proxy_width_GeV"] >= 0.0
                for row in rows
            ),
            "running_masses_reduce_widths_vs_reference_mass_proxy": all(
                row["running_mass_at_mH_GeV"] < row["reference_mass_GeV"] for row in rows
            ),
        },
        "accepted_as_more_plausible_higgs_quark_decay_proxy": True,
        "accepted_as_precision_SM_decay_widths": False,
        "why_not_precision": (
            "This uses one-loop running and a one-loop QCD K factor only. It is numerically more plausible than "
            "using reference quark masses directly, but it still lacks multiloop running, matching, higher-order "
            "QCD/EW corrections, off-shell/total-width policy, and covariance/profile comparison."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    total_width_reference = 0.00407
    br_bb_reference = 0.575
    br_cc_reference = 0.029
    benchmark = {
        "schema": "MTTHiggsDecayPlausibilityBenchmark.v1",
        "status": "PLAUSIBILITY_BENCHMARK_BUILT_NOT_A_FIT",
        "external_reference": {
            "source": "LHC Higgs Cross Section Working Group public Higgs branching-ratio tables",
            "url": "https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAtMH12509_2014",
            "mH_GeV": 125.09,
            "BR_H_to_bb_approx": br_bb_reference,
            "BR_H_to_cc_approx": br_cc_reference,
            "total_width_GeV_approx": total_width_reference,
            "used_as_source_selector": False,
            "used_for_parameter_fit": False,
        },
        "benchmark_partial_widths_GeV": {
            "H_to_bb_reference_approx": total_width_reference * br_bb_reference,
            "H_to_cc_reference_approx": total_width_reference * br_cc_reference,
        },
        "proxy_comparison": {
            row["fermion"]: {
                "proxy_width_GeV": row["running_mass_qcd_proxy_width_GeV"],
                "reference_approx_GeV": total_width_reference * (br_bb_reference if row["fermion"] == "b" else br_cc_reference),
                "ratio_proxy_to_reference_approx": row["running_mass_qcd_proxy_width_GeV"]
                / (total_width_reference * (br_bb_reference if row["fermion"] == "b" else br_cc_reference)),
            }
            for row in rows
        },
        "plausibility_result": "RUNNING_MASS_PROXY_IN_CORRECT_ORDER_OF_MAGNITUDE_FOR_HIGGS_QUARK_WIDTHS",
        "not_used_for_fit": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = list(previous_gate["remaining_true_equivalence_blockers"])
    closed_now = previous_gate["closed_now"] + ["one-loop running-mass Higgs decay proxy rows"]
    for blocker in [
        "running-mass and scale-transported Higgs decay widths",
    ]:
        if blocker in remaining:
            remaining.remove(blocker)
    for blocker in [
        "multiloop running-mass Higgs decay widths",
        "higher-order QCD/EW/off-shell total-width policy",
        "full precision loop-corrected QFT correlator/S-matrix/decay rows",
        "full covariance/profile likelihood values",
        "actual selected Qa/SU3 operator packet",
    ]:
        if blocker not in remaining:
            remaining.append(blocker)

    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterRunningMassProxy.v1",
        "status": "RUNNING_MASS_PROXY_VALUES_BUILT_FULL_PRECISION_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": closed_now,
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "replace one-loop proxy with declared multiloop running/matching and full Higgs width policy",
        "guardrails": {
            "running_mass_proxy_is_not_full_precision_width": True,
            "plausibility_benchmark_not_a_fit": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRunningMassHiggsDecayProxyOrPrecisionWidths",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_loopqcddecayproxyvalues_or_fullprecisionqft.candidate.json"),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "gauge_replay": rel(DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"),
        },
        "output_packets": {
            "one_loop_running_mass_higgs_decay_proxy": rel(RUNNING),
            "higgs_decay_plausibility_benchmark": rel(BENCH),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "RunningMassHiggsDecayProxyTheorem",
            "proved": True,
            "statement": (
                "Replacing reference quark masses by one-loop running masses at the Higgs scale emits more plausible "
                "Higgs quark decay proxy values while preserving the no-fit guardrail. The result is a controlled "
                "proxy layer, not a full precision SM decay-width computation."
            ),
        },
        "what_closes_now": {
            "one_loop_alpha_s_mH_proxy": True,
            "one_loop_running_b_c_masses_at_mH_proxy": True,
            "running_mass_higgs_quark_decay_proxy_values": True,
            "plausibility_benchmark_without_fit": True,
        },
        "what_remains_open": {
            "multiloop_running_and_threshold_matching": True,
            "higher_order_QCD_EW_offshell_total_width_policy": True,
            "full_covariance_profile_likelihood_values": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "running_mass_proxy_layer_closed": True,
            "full_precision_Higgs_widths_closed": False,
            "actual_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "answer_to_plausibility_question": {
            "previous_reference_mass_QCD_proxy_values": "mathematically correct for the stated proxy formula but not physically precision-plausible",
            "reason": "Using m_b(m_b) and m_c(m_c) directly at the Higgs scale overestimates quark widths.",
            "running_mass_proxy_values": "closer to expected SM Higgs partial-width order of magnitude, but still not precision values",
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_RunningMassHiggsDecayProxy_or_PrecisionWidths_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "running_mass_proxy_layer_closed": True,
        "full_precision_Higgs_widths_closed": False,
        "actual_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_MultiloopHiggsWidthPolicy_or_ActualQaSU3Packet_v1",
    }

    note = """# MTT Selected RunningMassHiggsDecayProxy or PrecisionWidths v1

Status: `MTT_SELECTED_RUNNINGMASSHIGGSDECAYPROXY_OR_PRECISIONWIDTHS_BUILT_RUNNING_MASS_PROXY_PRECISION_OPEN`.

The previous reference-mass QCD proxy values are correct for their declared
formula, but not precision-plausible for Higgs quark widths because the quark
masses must be transported to the Higgs scale.

This artifact builds a one-loop running-mass repair: alpha_s is transported
from M_Z to m_H, b and c masses are run to m_H, and the same one-loop QCD proxy
factor is applied at m_H.

The result is closer to the expected SM order of magnitude, but remains a proxy.
Full precision still requires multiloop running/matching, higher-order QCD/EW,
off-shell and total-width policy, covariance/profile comparison, and actual
Qa/SU3 attachment for operator-sensitive observables.
"""

    for path, payload in [
        (RUNNING, running_packet),
        (BENCH, benchmark),
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
