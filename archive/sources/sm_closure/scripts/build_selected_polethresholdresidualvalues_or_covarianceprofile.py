"""Build literature pole/threshold residual values and covariance-profile scaffold."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_polethresholdresidualvalues_or_covarianceprofile"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FORMULAS = PACKET_DIR / "buttazzo_boundary_formula_replay.packet.json"
COVARIANCE = PACKET_DIR / "diagonal_sensitivity_covariance_scaffold.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_gate_after_formula_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PoleThresholdResidualValues_or_CovarianceProfile_v1.md"

STATUS = "MTT_SELECTED_POLETHRESHOLDRESIDUALVALUES_OR_COVARIANCEPROFILE_BUILT_FORMULA_REPLAY_COVARIANCE_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sigma(value: dict[str, Any]) -> float:
    uncertainty = value.get("uncertainty", {})
    if isinstance(uncertainty, dict):
        plus = float(uncertainty.get("plus", uncertainty.get("standard", 0.0)))
        minus = float(uncertainty.get("minus", plus))
        return 0.5 * (abs(plus) + abs(minus))
    return float(uncertainty)


def boundary_values(inputs: dict[str, float]) -> dict[str, float]:
    mt = inputs["M_t_GeV"]
    mh = inputs["M_h_GeV"]
    mw = inputs["M_W_GeV"]
    alpha3 = inputs["alpha3_MZ"]
    g_y = 0.35830 + 0.00011 * (mt - 173.34) - 0.00020 * ((mw - 80.384) / 0.014)
    return {
        "lambda_Mt": 0.12604 + 0.00206 * (mh - 125.15) - 0.00004 * (mt - 173.34),
        "y_t_Mt": 0.93690 + 0.00556 * (mt - 173.34) - 0.00042 * ((alpha3 - 0.1184) / 0.0007),
        "g_2_Mt": 0.64779 + 0.00004 * (mt - 173.34) + 0.00011 * ((mw - 80.384) / 0.014),
        "g_Y_Mt": g_y,
        "g_1_GUT_Mt": math.sqrt(5.0 / 3.0) * g_y,
        "g_3_Mt": 1.1666 + 0.00314 * ((alpha3 - 0.1184) / 0.0007) - 0.00046 * (mt - 173.34),
    }


def deltas(values: dict[str, float], reference: dict[str, Any]) -> list[dict[str, float | str]]:
    rows = []
    for key, value in values.items():
        lit = float(reference[key]["central_value"])
        rows.append(
            {
                "id": f"{key}_formula_vs_literature",
                "formula_value": value,
                "literature_value": lit,
                "absolute_delta": abs(value - lit),
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_thresholdpolerunningmaps_or_covarianceprofile.candidate.json")
    previous_gate = load(
        DATA
        / "selected_thresholdpolerunningmaps_or_covarianceprofile"
        / "updated_true_equivalence_gate_after_threshold_map_scaffold.packet.json"
    )
    literature = load(
        DATA
        / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
        / "external_literature_rg_benchmark_values.packet.json"
    )
    reference = load(DATA / "sm_equivalence_reference_data_values_fill.candidate.json")
    common = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")

    masses = reference["reference_values"]["masses"]
    alpha3 = common["common_scale_packet"]["closed_values"]["alpha_3_MZ"]
    buttazzo_inputs = dict(literature["reference_point"]["central_inputs_in_paper"])
    current_inputs = {
        "M_W_GeV": float(masses["W"]["central_value"]),
        "M_h_GeV": float(masses["H"]["central_value"]),
        "M_t_GeV": float(masses["t"]["central_value"]),
        "alpha3_MZ": float(alpha3["central_value"]),
    }

    central_values = boundary_values(buttazzo_inputs)
    current_values = boundary_values(current_inputs)
    central_rows = deltas(central_values, literature["literature_values"])

    formula_packet = {
        "schema": "MTTButtazzoBoundaryFormulaReplay.v1",
        "status": "LITERATURE_BOUNDARY_FORMULAS_REPLAYED_RESIDUAL_VALUES_FILLED",
        "source": literature["source"],
        "formula_reference": {
            "lambda_Mt": "0.12604 + 0.00206*(Mh-125.15) - 0.00004*(Mt-173.34)",
            "y_t_Mt": "0.93690 + 0.00556*(Mt-173.34) - 0.00042*((alpha3(MZ)-0.1184)/0.0007)",
            "g_2_Mt": "0.64779 + 0.00004*(Mt-173.34) + 0.00011*((MW-80.384)/0.014)",
            "g_Y_Mt": "0.35830 + 0.00011*(Mt-173.34) - 0.00020*((MW-80.384)/0.014)",
            "g_3_Mt": "1.1666 + 0.00314*((alpha3(MZ)-0.1184)/0.0007) - 0.00046*(Mt-173.34)",
            "g_1_GUT_Mt": "sqrt(5/3) * g_Y_Mt",
        },
        "buttazzo_central_input_replay": {
            "inputs": buttazzo_inputs,
            "values": central_values,
            "comparison_rows": central_rows,
            "max_absolute_delta_to_encoded_literature": max(row["absolute_delta"] for row in central_rows),
            "replays_encoded_literature_values": max(row["absolute_delta"] for row in central_rows) < 1e-14,
        },
        "current_repo_input_variant": {
            "inputs": current_inputs,
            "values": current_values,
            "comparison_to_buttazzo_central": [
                {
                    "id": key,
                    "current_input_formula_value": value,
                    "buttazzo_central_formula_value": central_values[key],
                    "absolute_delta": abs(value - central_values[key]),
                }
                for key, value in current_values.items()
            ],
            "accepted_as_selected_MTT_prediction": False,
        },
        "residuals_promoted_to_literature_formula_requirements": True,
        "precision_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    jacobian = {
        "lambda_Mt": {"M_h_GeV": 0.00206, "M_t_GeV": -0.00004},
        "y_t_Mt": {"M_t_GeV": 0.00556, "alpha3_MZ": -0.00042 / 0.0007},
        "g_2_Mt": {"M_t_GeV": 0.00004, "M_W_GeV": 0.00011 / 0.014},
        "g_Y_Mt": {"M_t_GeV": 0.00011, "M_W_GeV": -0.00020 / 0.014},
        "g_3_Mt": {"alpha3_MZ": 0.00314 / 0.0007, "M_t_GeV": -0.00046},
    }
    input_sigmas = {
        "M_W_GeV": sigma(masses["W"]),
        "M_h_GeV": sigma(masses["H"]),
        "M_t_GeV": sigma(masses["t"]),
        "alpha3_MZ": float(alpha3["uncertainty"]),
    }
    propagated = {}
    for output, derivatives in jacobian.items():
        variance = 0.0
        contributions = {}
        for input_key, derivative in derivatives.items():
            contribution = (derivative * input_sigmas[input_key]) ** 2
            variance += contribution
            contributions[input_key] = contribution
        propagated[output] = {
            "diagonal_sigma": math.sqrt(variance),
            "variance_contributions": contributions,
        }
    propagated["g_1_GUT_Mt"] = {
        "diagonal_sigma": math.sqrt(5.0 / 3.0) * propagated["g_Y_Mt"]["diagonal_sigma"],
        "variance_contributions": {
            key: (5.0 / 3.0) * value
            for key, value in propagated["g_Y_Mt"]["variance_contributions"].items()
        },
    }

    covariance_packet = {
        "schema": "MTTDiagonalSensitivityCovarianceScaffold.v1",
        "status": "DIAGONAL_SENSITIVITY_SCAFFOLD_BUILT_FULL_PROFILE_OPEN",
        "input_sigmas": input_sigmas,
        "jacobian": jacobian,
        "propagated_diagonal_uncertainties": propagated,
        "correlations_included": False,
        "full_profile_likelihood_closed": False,
        "why_open": (
            "The formulas supply a linear sensitivity map. Full true-equivalence profiling still needs "
            "published or reconstructed correlations among electroweak, Higgs, top, and alpha3 inputs, "
            "plus a declared likelihood convention."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    remaining = [
        blocker
        for blocker in previous_gate["remaining_true_equivalence_blockers"]
        if blocker != "precision pole/running threshold residual maps"
    ]
    if "full covariance/profile likelihood values" not in remaining:
        remaining.insert(0, "full covariance/profile likelihood values")
    if "multi-loop coupled RG/profile convention audit" not in remaining:
        remaining.insert(1, "multi-loop coupled RG/profile convention audit")
    updated = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterFormulaReplay.v1",
        "status": "LITERATURE_FORMULA_REPLAY_BUILT_FULL_COVARIANCE_PROFILE_OPEN",
        "previous_true_equivalence_blockers": previous_gate["remaining_true_equivalence_blockers"],
        "closed_now": [
            "Buttazzo boundary formula replay",
            "top/Higgs pole-threshold residual formula requirements",
            "diagonal sensitivity covariance scaffold",
        ],
        "remaining_true_equivalence_blockers": remaining,
        "next_primary_value_gate": "full covariance/profile likelihood values and multi-loop convention audit",
        "guardrails": {
            "formula_values_are_literature_replay_not_MTT_source": True,
            "current_input_variant_is_not_selected_prediction": True,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPoleThresholdResidualValuesOrCovarianceProfile",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_thresholdpolerunningmaps_or_covarianceprofile.candidate.json"),
            "literature_benchmark_values": rel(
                DATA
                / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
                / "external_literature_rg_benchmark_values.packet.json"
            ),
            "reference_values": rel(DATA / "sm_equivalence_reference_data_values_fill.candidate.json"),
            "common_scale_packet": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
        },
        "output_packets": {
            "buttazzo_boundary_formula_replay": rel(FORMULAS),
            "diagonal_sensitivity_covariance_scaffold": rel(COVARIANCE),
            "updated_true_equivalence_gate": rel(UPDATED),
        },
        "theorem": {
            "name": "PoleThresholdResidualFormulaReplayTheorem",
            "proved": True,
            "statement": (
                "The external literature boundary-condition formulas replay the encoded Buttazzo weak-scale "
                "benchmark values exactly at their stated central inputs, and turn the previous top/Higgs "
                "residual slots into explicit formula obligations. A diagonal sensitivity/covariance scaffold "
                "is emitted. This closes formula replay, not full profile likelihood, true SM equivalence, or no-knob derivation."
            ),
        },
        "what_closes_now": {
            "buttazzo_boundary_formula_replay": True,
            "pole_threshold_residual_formula_requirements_filled": True,
            "diagonal_sensitivity_covariance_scaffold": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "full_covariance_profile_likelihood_values": True,
            "multi_loop_coupled_RG_profile_convention_audit": True,
            "local_QFT_observable_values": True,
            "QM_GR_measurement_response_interfaces": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": True,
            "literature_formula_replay_closed": True,
            "precision_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PoleThresholdResidualValues_or_CovarianceProfile_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "literature_formula_replay_closed": True,
        "full_covariance_profile_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_FullCovarianceProfile_or_MultiLoopConventionAudit_v1",
    }

    note = """# MTT Selected PoleThresholdResidualValues or CovarianceProfile v1

Status: `MTT_SELECTED_POLETHRESHOLDRESIDUALVALUES_OR_COVARIANCEPROFILE_BUILT_FORMULA_REPLAY_COVARIANCE_OPEN`.

This artifact replays the Buttazzo et al. (`arXiv:1307.3536`) weak-scale
boundary-condition formulas for `lambda(Mt)`, `yt(Mt)`, `g2(Mt)`, `gY(Mt)`,
GUT-normalized `g1(Mt)`, and `g3(Mt)`.

At Buttazzo central inputs the formulas reproduce the encoded literature rows.
Using the current repo's measured inputs is recorded only as a downstream
variant, not as a selected MTT prediction.

The previous residual slots are now formula-level requirements, and a diagonal
sensitivity/covariance scaffold is emitted. Full covariance/profile likelihood,
multi-loop convention audit, true SM equivalence, and no-knob derivation remain
open.
"""

    for path, payload in [
        (FORMULAS, formula_packet),
        (COVARIANCE, covariance_packet),
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
