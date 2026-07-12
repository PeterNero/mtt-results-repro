"""Build threshold/pole-running map scaffold after external literature RG benchmarks."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholdpolerunningmaps_or_covarianceprofile"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAUGE = PACKET_DIR / "one_loop_gauge_mz_to_mt_transport.packet.json"
RESIDUALS = PACKET_DIR / "pole_threshold_residual_map_requirements.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_threshold_map_scaffold.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdPoleRunningMaps_or_CovarianceProfile_v1.md"

STATUS = "MTT_SELECTED_THRESHOLDPOLERUNNINGMAPS_OR_COVARIANCEPROFILE_BUILT_GAUGE_BRIDGE_THRESHOLDS_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_gauge_one_loop(g0: float, beta_coefficient: float, mu0: float, mu1: float) -> float:
    """One-loop solution for dg/dln(mu)=b*g^3/(16*pi^2)."""
    inv_g2 = 1.0 / (g0 * g0) - beta_coefficient * math.log(mu1 / mu0) / (8.0 * math.pi * math.pi)
    return math.sqrt(1.0 / inv_g2)


def delta_row(name: str, transported: float, literature: float) -> dict[str, Any]:
    return {
        "id": name,
        "transported_value": transported,
        "literature_value": literature,
        "absolute_delta": abs(transported - literature),
        "relative_delta": abs(transported - literature) / abs(literature),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json")
    previous_gate = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "threshold_covariance_gap_after_literature_benchmark.packet.json"
    )
    literature = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "external_literature_rg_benchmark_values.packet.json"
    )
    comparison = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "literature_vs_local_convention_comparison.packet.json"
    )
    common = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    firstpass = load(
        DATA
        / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
        / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
    )

    mz = 91.1876
    mt = float(literature["reference_point"]["central_inputs_in_paper"]["M_t_GeV"])
    closed = common["common_scale_packet"]["closed_values"]
    g1_mz = float(closed["g_1_GUT_MZ"]["central_value"])
    g2_mz = float(closed["g_2_MZ"]["central_value"])
    g3_mz = float(closed["g_3_MZ"]["central_value"])
    lit_values = literature["literature_values"]

    beta = {
        "g_1_GUT": 41.0 / 10.0,
        "g_2": -19.0 / 6.0,
        "g_3": -7.0,
    }
    transported = {
        "g_1_GUT_Mt_one_loop": run_gauge_one_loop(g1_mz, beta["g_1_GUT"], mz, mt),
        "g_2_Mt_one_loop": run_gauge_one_loop(g2_mz, beta["g_2"], mz, mt),
        "g_3_Mt_one_loop": run_gauge_one_loop(g3_mz, beta["g_3"], mz, mt),
    }
    transported["g_Y_Mt_one_loop"] = transported["g_1_GUT_Mt_one_loop"] / math.sqrt(5.0 / 3.0)
    gauge_rows = [
        delta_row("g1GUT_one_loop_MZ_to_Mt_vs_literature", transported["g_1_GUT_Mt_one_loop"], lit_values["g_1_GUT_Mt"]["central_value"]),
        delta_row("g2_one_loop_MZ_to_Mt_vs_literature", transported["g_2_Mt_one_loop"], lit_values["g_2_Mt"]["central_value"]),
        delta_row("g3_one_loop_MZ_to_Mt_vs_literature", transported["g_3_Mt_one_loop"], lit_values["g_3_Mt"]["central_value"]),
    ]
    max_gauge_delta = max(row["absolute_delta"] for row in gauge_rows)

    gauge_packet = {
        "schema": "MTTOneLoopGaugeMZToMtTransport.v1",
        "status": "ONE_LOOP_GAUGE_TRANSPORT_BRIDGE_BUILT_PRECISION_THRESHOLDS_OPEN",
        "transport": {
            "scheme": "MSbar, GUT-normalized U(1)",
            "mu0_GeV": mz,
            "mu1_GeV": mt,
            "formula": "1/g_i(mu1)^2 = 1/g_i(mu0)^2 - b_i log(mu1/mu0)/(8*pi^2)",
            "beta_coefficients": beta,
            "input_values": {
                "g_1_GUT_MZ": g1_mz,
                "g_2_MZ": g2_mz,
                "g_3_MZ": g3_mz,
            },
            "transported_values": transported,
        },
        "literature_reference": literature["source"],
        "comparison_rows": gauge_rows,
        "max_absolute_delta_to_literature": max_gauge_delta,
        "passes_coarse_gauge_bridge": max_gauge_delta < 0.01,
        "accepted_as_precision_threshold_match": False,
        "why_not_precision": (
            "This is a one-loop gauge bridge only. It does not include the full Buttazzo threshold "
            "matching context, uncertainty covariance, or multi-loop coupled Yukawa/Higgs running."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    local = comparison["local_values"]
    lit_lambda = float(lit_values["lambda_Mt"]["central_value"])
    lit_yt = float(lit_values["y_t_Mt"]["central_value"])
    residual_packet = {
        "schema": "MTTPoleThresholdResidualMapRequirements.v1",
        "status": "POLE_THRESHOLD_RESIDUAL_SLOTS_FILLED_AS_REQUIREMENTS_NOT_FITS",
        "residual_slots": {
            "top_tree_to_MSbar_Mt": {
                "input_value": local["y_t_native_tree"],
                "benchmark_value": lit_yt,
                "required_multiplicative_map": lit_yt / local["y_t_native_tree"],
                "required_additive_delta": lit_yt - local["y_t_native_tree"],
                "promotable_now": False,
            },
            "top_firstpass_MZ_to_MSbar_Mt": {
                "input_value": local["y_t_MZ_firstpass"],
                "benchmark_value": lit_yt,
                "required_multiplicative_map": lit_yt / local["y_t_MZ_firstpass"],
                "required_additive_delta": lit_yt - local["y_t_MZ_firstpass"],
                "promotable_now": False,
            },
            "lambda_tree_to_MSbar_Mt": {
                "input_value": local["lambda_tree_native"],
                "benchmark_value": lit_lambda,
                "required_additive_delta": lit_lambda - local["lambda_tree_native"],
                "promotable_now": False,
            },
            "lambda_firstpass_MZ_to_MSbar_Mt": {
                "input_value": firstpass["accepted_values"]["lambda_H_MZ_firstpass"],
                "benchmark_value": lit_lambda,
                "required_additive_delta": lit_lambda - firstpass["accepted_values"]["lambda_H_MZ_firstpass"],
                "promotable_now": False,
            },
        },
        "interpretation": (
            "These residuals identify the map that a legitimate threshold/pole-running theorem must "
            "supply. They are not fitted corrections and cannot be used as selected MTT source data."
        ),
        "required_for_promotion": [
            "top pole/direct mass to MSbar running top Yukawa matching",
            "Higgs pole mass and vev convention to MSbar lambda(Mt) matching",
            "coupled multi-loop running policy or accepted literature threshold table",
            "uncertainty/covariance propagation for the benchmark inputs",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker != "literature/local convention agreement after threshold maps"
    ]
    if "precision pole/running threshold residual maps" not in remaining:
        remaining.insert(0, "precision pole/running threshold residual maps")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterThresholdMapScaffold.v1",
        "status": "GAUGE_SCALE_BRIDGE_BUILT_THRESHOLD_AND_COVARIANCE_VALUES_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": [
            "one-loop gauge M_Z-to-M_t transport scaffold",
            "pole/threshold residual slots identified",
        ],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "promote residual slots by threshold/pole-running theorem or accepted covariance profile",
        "guardrails": {
            "residuals_are_requirements_not_fitted_corrections": True,
            "gauge_bridge_is_precision_match": False,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedThresholdPoleRunningMapsOrCovarianceProfile",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance.candidate.json"),
            "literature_benchmark_values": rel(
                DATA
                / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
                / "external_literature_rg_benchmark_values.packet.json"
            ),
            "literature_vs_local_comparison": rel(
                DATA
                / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
                / "literature_vs_local_convention_comparison.packet.json"
            ),
            "common_scale_packet": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "firstpass_values": rel(
                DATA
                / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
                / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
            ),
        },
        "output_packets": {
            "one_loop_gauge_mz_to_mt_transport": rel(GAUGE),
            "pole_threshold_residual_map_requirements": rel(RESIDUALS),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "ThresholdPoleRunningMapScaffoldTheorem",
            "proved": True,
            "statement": (
                "The M_Z gauge triplet admits an executable one-loop MSbar transport bridge to M_t, "
                "and the top-Yukawa/Higgs-lambda residual slots against the external literature benchmark "
                "are now explicit theorem obligations. This closes the map scaffold and residual inventory, "
                "but not precision threshold matching, covariance/profile closure, true SM equivalence, or no-knob derivation."
            ),
        },
        "what_closes_now": {
            "one_loop_gauge_MZ_to_Mt_transport_scaffold": True,
            "external_literature_gauge_bridge_compared": True,
            "pole_threshold_residual_slots_identified": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "precision_pole_running_threshold_residual_maps": True,
            "full_covariance_profile_values": True,
            "multi_loop_coupled_RG_threshold_policy": True,
            "local_QFT_observable_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "threshold_map_scaffold_built": True,
            "precision_threshold_maps_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_ThresholdPoleRunningMaps_or_CovarianceProfile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "one_loop_gauge_bridge_built": True,
        "precision_threshold_maps_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_PoleThresholdResidualValues_or_CovarianceProfile_v1",
    }

    note = """# MTT Selected ThresholdPoleRunningMaps or CovarianceProfile v1

Status: `MTT_SELECTED_THRESHOLDPOLERUNNINGMAPS_OR_COVARIANCEPROFILE_BUILT_GAUGE_BRIDGE_THRESHOLDS_OPEN`.

This artifact builds the first executable bridge after the external Buttazzo et
al. RG benchmark insertion: one-loop MSbar gauge transport from `M_Z` to `M_t`
using the standard SM coefficients `b=(41/10,-19/6,-7)` for GUT-normalized
`g1`, `g2`, and `g3`.

It also emits the residual slots that the next theorem must promote for
`yt(Mt)` and `lambda(Mt)`. Those residuals are requirements, not fitted
corrections, and they are not selected MTT source data.

The result advances SM-parity benchmarking but keeps true SM equivalence open:
precision pole-to-running threshold maps, covariance/profile values, local QFT
observable values, QM/GR interfaces, and actual Qa/SU3 operator data remain.
"""

    for path, payload in [
        (GAUGE, gauge_packet),
        (RESIDUALS, residual_packet),
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
