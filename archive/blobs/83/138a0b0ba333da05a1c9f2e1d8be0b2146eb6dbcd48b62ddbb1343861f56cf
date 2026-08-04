"""Build the q79 circle-torsion/retarded-resolvent gauge-cost candidate."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission"
OUT = ROOT / "candidate_data" / SLUG
TORSION = OUT / "q79_shared_circle_chord_torsion.packet.json"
RESOLVENT = OUT / "retarded_resolvent_cost_operator.packet.json"
EXECUTION = OUT / "zero_continuous_parameter_gauge_execution.packet.json"
CONTRACT = OUT / "next_resolvent_routing_source_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1.md"
STATUS = "MTT_SELECTED_Q79_CIRCLE_TORSION_RETARDED_RESOLVENT_CANDIDATE_SUBPPB_PROFILE_MATCH_SOURCE_ROUTING_OPEN"
NEXT = "MTT_Selected_RetardedResolventMultiplicityAndProjectorRoutingTheorem_or_StrictGaugeValuePromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauge_ratios(colored_cost: float, e_cost: float, tau: float) -> tuple[float, float]:
    s = math.exp(-tau * colored_cost)
    t = math.exp(tau * e_cost)
    k1 = 21.6 * s + 10.8 + 10.8 * t
    k2 = 54.0 * s + 18.0
    k3 = 54.0 * s
    return k1 / k2, k3 / k2


def main() -> int:
    paths = {
        "A17_branch": ROOT / "candidate_data" / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness.candidate.json",
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A68_factorization": ROOT / "candidate_data" / "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission" / "selected_rational_cost_nearmiss.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
        "A69_residual": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "exact_residual_cost_spectrum.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    profile = data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"]
    target_r1, target_r3 = float(profile[0]), float(profile[2])
    tau = float(data["A68_factorization"]["tau_int"])

    q = 79
    modulus = 448
    holonomy_angle = 2.0 * math.pi * q / modulus
    chord_laplacian = abs(1.0 - complex(math.cos(holonomy_angle), math.sin(holonomy_angle))) ** 2
    chord_formula = 4.0 * math.sin(math.pi * q / modulus) ** 2
    torsion_cost = 0.25 * math.log(chord_laplacian)
    torsion = {
        "schema": "MTTQ79SharedCircleChordTorsion.v1",
        "status": "EXACT_Q79_HOLONOMY_CHORD_VALUE_COMPUTED_LENS_QUARTER_ROUTING_CONDITIONAL",
        "q": q,
        "modulus": modulus,
        "holonomy": "H79=exp(2pi i 79/448)",
        "positive_chord_operator": "Delta79=(1-H79)^*(1-H79)",
        "positive_chord_eigenvalue": chord_laplacian,
        "closed_formula": "4 sin^2(79 pi/448)",
        "closed_formula_value": chord_formula,
        "lens_quarter_log_cost": torsion_cost,
        "proof": "For unitary scalar H, (1-H)^*(1-H)=2-H-H^*=4 sin^2(arg(H)/2).",
        "source_status": {
            "q79_retarded_representative_selected": data["A17_branch"]["orientation_level_selection_closed"],
            "positive_chord_value_exact": True,
            "lens_quarter_routes_this_value_to_e_kinetic_lane": False,
        },
    }

    predecessor_gap = 15.0
    origin_gap = 16.0
    hidden_channel_count = 2.0
    saturated_return = 1.0 / predecessor_gap
    denominator = hidden_channel_count * predecessor_gap + origin_gap + saturated_return
    carry_rows = 6.0
    charge_channels = 7.0
    routing_ratio = (predecessor_gap + origin_gap) / (carry_rows * charge_channels)
    delta = torsion_cost / denominator
    delta_e = torsion_cost + routing_ratio * delta
    colored_cost = 14.0 / 3.0 + delta
    e_cost = 3.0 + delta_e
    resolvent = {
        "schema": "MTTRetardedResolventCostOperator.v1",
        "status": "EXPLICIT_FINITE_RESOLVENT_SKELETON_CONSTRUCTED_MULTIPLICITY_ROUTING_UNPROVED",
        "denominator_operator": {
            "spectrum": [predecessor_gap, predecessor_gap, origin_gap, saturated_return],
            "trace": denominator,
            "formula": "2*15+16+1/15",
            "interpretation": [
                "two equivalent hidden color-completion channels at the predecessor gap 15",
                "one direct retarded-origin channel at gap 16",
                "one saturated Green-return coordinate 1/15",
            ],
        },
        "projector_routing_ratio": {
            "value": routing_ratio,
            "formula": "(15+16)/(6*7)=31/42",
            "interpretation": "retarded-pair trace divided by six carry rows times seven charge channels",
        },
        "cost_emission": {
            "delta": delta,
            "delta_e": delta_e,
            "colored_cost": colored_cost,
            "charged_lepton_cost": e_cost,
            "formula_colored": "14/3 + T79/(2*15+16+1/15)",
            "formula_e": "3 + T79 + (31/42)*T79/(2*15+16+1/15)",
        },
        "mathematical_properties": {
            "denominator_positive": denominator > 0.0,
            "correction_positive": delta > 0.0,
            "zero_continuous_parameters": True,
        },
        "source_status": {
            "ingredients_individually_present": True,
            "same_action_direct_sum_multiplicity_theorem": False,
            "six_by_seven_projector_routing_theorem": False,
            "strictly_typed_as_one_selected_hessian_spectrum": False,
            "typing_warning": "15 is a selected tower eigenvalue, 16 is a retarded carrier label, and 1/15 is a saturated proper time/resolvent scale; no theorem currently makes their sum a Hessian trace.",
            "formula_discovered_after_profile_residual_known": True,
            "accepted_as_strict_source": False,
        },
    }

    r1, r3 = gauge_ratios(colored_cost, e_cost, tau)
    relative_residual = [r1 / target_r1 - 1.0, r3 / target_r3 - 1.0]
    log_residual = math.hypot(math.log(r1 / target_r1), math.log(r3 / target_r3))
    a69_profile = data["A69_operator"]["gauge_execution"]["K_over_K2"]
    a69_log_residual = math.hypot(math.log(a69_profile[0] / target_r1), math.log(a69_profile[2] / target_r3))
    execution = {
        "schema": "MTTZeroContinuousParameterGaugeExecution.v1",
        "status": "TARGET_RANKED_DISCRETE_FORMULA_SUBPPB_PROFILE_COMPATIBILITY_NOT_STRICT_PREDICTION",
        "input_formula_uses_only": ["q=79", "N=448", "Lens quarter 1/4", "retarded pair 15,16", "two hidden completion channels", "six carry rows", "seven charge channels", "saturated return 1/15"],
        "new_continuous_parameters": 0,
        "predicted_K_over_K2": [r1, 1.0, r3],
        "profile_K_over_K2_downstream_only": [target_r1, 1.0, target_r3],
        "absolute_residual_U1_SU3": [r1 - target_r1, r3 - target_r3],
        "relative_residual_U1_SU3": relative_residual,
        "relative_residual_ppm_U1_SU3": [value * 1e6 for value in relative_residual],
        "log_residual": log_residual,
        "A69_log_residual": a69_log_residual,
        "improvement_factor_over_A69": a69_log_residual / log_residual,
        "exact_central_value_equality": False,
        "profile_compatibility_claimed_without_covariance": False,
        "prediction_claimed": False,
        "reason_not_promoted": "The discrete resolvent and routing formula was assembled after the A69 residual was visible. It needs a same-action multiplicity/routing theorem and an independent covariance/scale test before prediction-profile promotion.",
    }
    inferred = data["A69_residual"]["profile_inferred_values"]
    diagnostic = {
        "delta_q_formula_minus_profile_inferred": delta - float(inferred["delta_q"]),
        "delta_e_formula_minus_profile_inferred": delta_e - float(inferred["delta_e"]),
        "routing_ratio_profile_inferred_after_T79": (float(inferred["delta_e"]) - torsion_cost) / float(inferred["delta_q"]),
        "routing_ratio_discrete": routing_ratio,
    }
    contract = {
        "schema": "MTTNextResolventRoutingSourceContract.v1",
        "status": "SAME_ACTION_RESOLVENT_MULTIPLICITY_AND_ROUTING_PROOF_REQUIRED",
        "required_proofs": [
            "derive the q79 positive chord determinant from the selected common-circle kinetic Hessian",
            "derive the Lens-quarter logarithmic normalization in that same action",
            "prove the two 15 channels, one 16 channel and saturated 1/15 return are the complete Schur/resolvent spectrum",
            "prove the 31/42 colored-to-e projector routing from six carry rows and seven charge channels",
            "freeze the formula before testing another scale or updated coupling profile",
            "supply a common-scheme covariance certificate for prediction-profile promotion",
        ],
        "forbidden_shortcuts": [
            "do not call sub-ppb central-value agreement exact equality",
            "do not hide the target-ranked discovery history",
            "do not fit an additional residual coefficient",
        ],
        "next_required_artifact": NEXT,
    }
    checks = {
        "q79_branch_selected": torsion["source_status"]["q79_retarded_representative_selected"],
        "chord_identity_exact": abs(chord_laplacian - chord_formula) < 1e-15,
        "torsion_positive": torsion_cost > 0.0,
        "resolvent_denominator_exact": abs(denominator - (2.0 * 15.0 + 16.0 + 1.0 / 15.0)) < 1e-15,
        "routing_ratio_is_31_over_42": abs(routing_ratio - 31.0 / 42.0) < 1e-15,
        "zero_continuous_parameters": execution["new_continuous_parameters"] == 0,
        "sub_ppm_both_ratios": max(abs(value) for value in execution["relative_residual_ppm_U1_SU3"]) < 1.0,
        "large_improvement_over_A69": execution["improvement_factor_over_A69"] > 1e5,
        "not_exact_equality": not execution["exact_central_value_equality"],
        "target_ranking_disclosed": resolvent["source_status"]["formula_discovered_after_profile_residual_known"],
        "strict_source_not_claimed": not resolvent["source_status"]["accepted_as_strict_source"],
    }
    candidate = {
        "schema": "MTTSelectedResidualCircleLensCostOperatorOrExactGaugeKineticValueEmission.v1",
        "status": STATUS,
        "results": {
            "q79_positive_chord_torsion_exact": True,
            "retarded_resolvent_operator_skeleton_constructed": True,
            "zero_continuous_parameter_formula_executed": True,
            "sub_ppm_profile_match": True,
            "strict_source_theorem_closed": False,
            "strict_gauge_values_accepted": 0,
            "target_ranked_candidate": True,
        },
        "diagnostic": diagnostic,
        "outputs": {
            "torsion": str(TORSION.relative_to(ROOT)).replace("\\", "/"),
            "resolvent": str(RESOLVENT.relative_to(ROOT)).replace("\\", "/"),
            "execution": str(EXECUTION.relative_to(ROOT)).replace("\\", "/"),
            "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1",
        "status": STATUS,
        "T79": torsion_cost,
        "resolvent_denominator": denominator,
        "routing_ratio": routing_ratio,
        "costs_colored_e": [colored_cost, e_cost],
        "predicted_K_over_K2": [r1, 1.0, r3],
        "relative_residual_ppm_U1_SU3": execution["relative_residual_ppm_U1_SU3"],
        "improvement_factor_over_A69": execution["improvement_factor_over_A69"],
        "new_continuous_parameters": 0,
        "target_ranked": True,
        "strict_source_closed": False,
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Residual Circle/Lens Cost Operator or Exact Gauge Kinetic Value Emission v1

## Exact q79 chord torsion

For `H79=exp(2 pi i 79/448)`, the positive shared-circle chord operator satisfies

```text
(1-H79)^*(1-H79) = 4 sin^2(79 pi/448).
```

The Lens-quarter logarithmic cost is

```text
T79 = (1/4) log(4 sin^2(79 pi/448)) = {torsion_cost:.17g}.
```

## Retarded-resolvent candidate

The two hidden color channels, retarded pair and saturated return give

```text
D = 2*15 + 16 + 1/15 = {denominator:.17g},
R = (15+16)/(6*7) = 31/42,
delta = T79/D,
c_col = 14/3 + delta,
c_e = 3 + T79 + R delta.
```

This is an explicit finite operator skeleton using no new continuous value. The same-action theorem
selecting the direct-sum multiplicities and `31/42` projector routing is still open. In particular,
`15`, `16`, and `1/15` currently have different source types (eigenvalue, carrier label, and proper
time/resolvent scale), so their sum is not yet a selected Hessian trace.

## Numerical execution

The resulting gauge row is

```text
K/K2 = {[r1, 1.0, r3]},
relative residual ppm (U1,SU3) = {execution['relative_residual_ppm_U1_SU3']}.
```

This improves the A69 log residual by a factor of `{execution['improvement_factor_over_A69']:.6g}`.
It is not exact central-value equality and is not yet promoted as a prediction. The formula was
assembled after the residual was known, so independent same-action derivation and an out-of-sample
scale/covariance test are mandatory.

Next artifact: `{NEXT}`.
"""

    dump(TORSION, torsion)
    dump(RESOLVENT, resolvent)
    dump(EXECUTION, execution)
    dump(CONTRACT, contract)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
