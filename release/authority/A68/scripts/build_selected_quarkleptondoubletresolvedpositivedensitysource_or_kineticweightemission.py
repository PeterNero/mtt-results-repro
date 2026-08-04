"""Resolve the minimal positive sector density beyond the Q/L-symmetric no-go."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission"
OUT = ROOT / "candidate_data" / SLUG
RECONSTRUCTION = OUT / "minimal_twofactor_positive_density_reconstruction.packet.json"
RATIONAL = OUT / "selected_rational_cost_nearmiss.packet.json"
CONTRACT = OUT / "next_quarkorder_sharedcircle_cost_source_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QuarkLeptonDoubletResolvedPositiveDensitySource_or_KineticWeightEmission_v1.md"
STATUS = "MTT_SELECTED_MINIMAL_QL_RESOLVED_DENSITY_RECONSTRUCTED_TWOFACTOR_COST_NEARMISS_FOUND_STRICT_SOURCE_OPEN"
NEXT = "MTT_Selected_QuarkOrderAndSharedCircleCostSpectrum_or_TwoFactorDensityValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauge_ratios(s: float, t: float) -> tuple[float, float]:
    # Sector traces are [12s,6s,6s,12,6t,6] in Q,u,d,L,e,N order.
    k1 = 21.6 * s + 10.8 + 10.8 * t
    k2 = 54.0 * s + 18.0
    k3 = 54.0 * s
    return k1 / k2, k3 / k2


def main() -> int:
    paths = {
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A66_trials": ROOT / "candidate_data" / "selected_finitekineticweightoperatorsource_or_circlelensnilzeromodegramexecution" / "predeclared_casimir_heat_weight_trials.packet.json",
        "A67_density": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "conditional_c1_positive_sector_density.packet.json",
        "A67_nogo": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "quark_lepton_doublet_symmetry_gauge_nogo.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    profile = data["A52_profile"]["minimal_profile_normalization"]["K_gauge_diagonal"]
    r1, r3 = float(profile[0]), float(profile[2])
    tau = float(data["A66_trials"]["source_times"]["tau_int"])

    # R3 is strictly increasing in s, and R1 is strictly increasing in t once s
    # is fixed, so this inversion is the unique positive two-factor solution.
    s_fit = r3 / (3.0 * (1.0 - r3))
    t_fit = (r1 * (54.0 * s_fit + 18.0) - 21.6 * s_fit - 10.8) / 10.8
    fit_ratios = gauge_ratios(s_fit, t_fit)
    q_cost_fit = -math.log(s_fit) / tau
    e_cost_fit = math.log(t_fit) / tau

    # The nearest simple half-layer/Casimir proposal suggested by the inferred
    # costs. These values are source hypotheses, not selected theorems.
    q_layer = 7.0 / 2.0
    q_casimir = 4.0 / 3.0
    e_cost = 3.0
    s_candidate = math.exp(-tau * q_layer * q_casimir)
    t_candidate = math.exp(tau * e_cost)
    candidate_ratios = gauge_ratios(s_candidate, t_candidate)
    relative_residuals = [candidate_ratios[0] / r1 - 1.0, candidate_ratios[1] / r3 - 1.0]
    log_residual = math.hypot(math.log(candidate_ratios[0] / r1), math.log(candidate_ratios[1] / r3))

    one_factor_r1_at_target_r3 = 1.2 - 0.8 * r3
    one_factor_relative_residual = one_factor_r1_at_target_r3 / r1 - 1.0
    reconstruction = {
        "schema": "MTTMinimalTwoFactorPositiveDensityReconstruction.v1",
        "status": "UNIQUE_POSITIVE_TWOFACTOR_PROFILE_RECONSTRUCTION_DIAGNOSTIC_ONLY",
        "sector_order": ["Q", "u", "d", "L", "e", "N"],
        "ansatz": {
            "sector_trace_weights": ["12s", "6s", "6s", "12", "6t", "6"],
            "meaning_s": "common attenuation of colored Q,u,d relative to the C1 incidence density",
            "meaning_t": "enhancement of the charged-lepton singlet e relative to the C1 incidence density",
            "K1": "21.6s+10.8+10.8t",
            "K2": "54s+18",
            "K3": "54s",
        },
        "one_factor_no_go": {
            "restriction": "t=1",
            "eliminated_relation": "K1/K2 = 6/5 - (4/5)(K3/K2)",
            "K1_over_K2_when_K3_matches_profile": one_factor_r1_at_target_r3,
            "profile_K1_over_K2": r1,
            "relative_residual": one_factor_relative_residual,
            "proved_not_exact": abs(one_factor_relative_residual) > 1e-10,
            "consequence": "quark/color attenuation alone cannot reproduce both independent gauge ratios",
        },
        "unique_twofactor_inverse": {
            "s": s_fit,
            "t": t_fit,
            "inferred_dimensionless_cost_minus_log_s_over_tau": q_cost_fit,
            "inferred_dimensionless_cost_log_t_over_tau": e_cost_fit,
            "reconstructed_K_over_K2": [fit_ratios[0], 1.0, fit_ratios[1]],
            "absolute_residual": max(abs(fit_ratios[0] - r1), abs(fit_ratios[1] - r3)),
            "positive": s_fit > 0.0 and t_fit > 0.0,
            "unique": True,
            "proof": "R3=3s/(3s+1) is strictly increasing for s>0; after fixing s, dR1/dt=10.8/(54s+18)>0",
        },
        "epistemic_status": {
            "profile_values_used_to_invert_s_t": True,
            "accepted_as_prediction": False,
            "accepted_as_strict_source_rows": False,
            "continuous_profile_coordinates_if_stopped_here": 2,
        },
    }
    rational = {
        "schema": "MTTSelectedRationalCostNearMiss.v1",
        "status": "SIMPLE_EXISTING_TAU_COST_CANDIDATE_NEAR_PROFILE_NOT_EXACT_NOT_SELECTED",
        "tau_int": tau,
        "tau_identity": "log(448)/15",
        "candidate_costs": {
            "colored_attenuation": "(7/2)*(4/3)=14/3",
            "charged_lepton_enhancement": "3",
            "s": s_candidate,
            "t": t_candidate,
            "s_exact_form": "448^(-14/45)",
            "t_exact_form": "448^(1/5)",
        },
        "corpus_factorization_clue": {
            "colored_cost": {
                "factorization": "nil sevenfold * two-channel Schur factor * SU3 fundamental Casimir = 7*(1/2)*(4/3)=14/3",
                "nil_sevenfold_status": "carried-forward corpus candidate; not yet a selected same-operator theorem",
                "two_channel_Schur_half_status": "proved schema in Color_Singlet_Redundancy_Source_for_Bq_v1",
                "SU3_Casimir_status": "standard selected-representation invariant C2(3)=4/3",
                "external_corpus_paths": [
                    "18 Theta-Closure & Execution Program/_md_v3_corrected/Color_Singlet_Redundancy_Source_for_Bq_v1.md",
                    "18 Theta-Closure & Execution Program/_md_v3_corrected/Sevenfold_Nil_Flux_Source_Candidate_for_MTT_Flavor_v1.md",
                ],
            },
            "charged_lepton_cost": {
                "factorization": "three charged-lepton nil basins * conjectural unit shared-circle kinetic cost = 3",
                "three_basin_status": "structural proto-spinor result",
                "unit_circle_cost_status": "open; no selected kinetic exponentiation theorem",
                "external_corpus_path": "10 ProtoSpinor/_md/Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md",
            },
            "promotion_status": "PARTIAL_SOURCE_FACTORIZATION_ONLY",
        },
        "comparison": {
            "candidate_K_over_K2": [candidate_ratios[0], 1.0, candidate_ratios[1]],
            "profile_K_over_K2_downstream_only": [r1, 1.0, r3],
            "relative_residual_U1_SU3": relative_residuals,
            "log_residual": log_residual,
            "absolute_inferred_cost_offsets": [abs(q_cost_fit - 14.0 / 3.0), abs(e_cost_fit - 3.0)],
        },
        "source_assessment": {
            "tau_int_already_selected": True,
            "SU3_fundamental_Casimir_4_over_3_standard": True,
            "seven_half_layers_selected_by_same_operator": False,
            "charged_lepton_cost_three_selected_by_same_operator": False,
            "colored_cost_has_composite_corpus_factorization": True,
            "charged_lepton_cost_has_structural_basin_count_clue": True,
            "exact_profile_match": False,
            "accepted_as_source": False,
            "new_continuous_parameters": 0,
            "reason": "The simple exponents are a strong compression clue, but their multiplicities are not emitted by a selected common MTT operator and the U1 ratio retains a 0.764 percent residual.",
        },
    }
    contract = {
        "schema": "MTTNextQuarkOrderSharedCircleCostSourceContract.v1",
        "status": "TWO_COST_SPECTRUM_SOURCE_REQUIRED",
        "required_operator": "one positive common-circle/bundle operator whose sector spectrum emits colored cost 14/3 (or the exact inferred replacement) and charged-lepton cost 3 (or the exact inferred replacement)",
        "required_proofs": [
            "derive the quark-versus-lepton attenuation from the selected bundle filtration or second-order quark breakdown",
            "derive the e-sector enhancement from the shared-circle/Lens action rather than the gauge target",
            "promote the nil sevenfold candidate and prove its composition with the B_q Schur half in the kinetic operator",
            "prove that the three charged-lepton basins each contribute one common-circle kinetic cost unit",
            "prove positivity, gauge commutation, and compatibility with the A67 C1 family blocks",
            "execute the same operator in gauge and flavor traces",
            "either remove the 0.764 percent U1 residual exactly or provide an independently controlled transport/error theorem",
        ],
        "forbidden_shortcuts": [
            "do not promote s_fit and t_fit as predictions",
            "do not identify the numerical proximity of 7/2 and 3 with source selection",
            "do not absorb the remaining U1 residual into an unnamed threshold",
        ],
        "next_required_artifact": NEXT,
    }
    checks = {
        "A67_QL_no_go_imported": data["A67_nogo"]["general_two_class_theorem"]["proved"],
        "tau_matches_log448_over_15": abs(tau - math.log(448.0) / 15.0) < 1e-15,
        "one_factor_relation_fails": reconstruction["one_factor_no_go"]["proved_not_exact"],
        "twofactor_solution_positive": s_fit > 0.0 and t_fit > 0.0,
        "twofactor_inverse_exact_numerically": reconstruction["unique_twofactor_inverse"]["absolute_residual"] < 1e-14,
        "inferred_colored_cost_near_14_over_3": abs(q_cost_fit - 14.0 / 3.0) < 1e-3,
        "inferred_e_cost_near_3": abs(e_cost_fit - 3.0) < 0.03,
        "rational_candidate_not_exact": log_residual > 1e-4,
        "rational_candidate_not_promoted": not rational["source_assessment"]["accepted_as_source"],
    }
    candidate = {
        "schema": "MTTSelectedQuarkLeptonDoubletResolvedPositiveDensitySourceOrKineticWeightEmission.v1",
        "status": STATUS,
        "results": {
            "one_factor_quark_suppression_no_go_proved": True,
            "minimal_twofactor_positive_reconstruction_unique": True,
            "simple_rational_cost_candidate_found": True,
            "strict_twofactor_source_theorem_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
            "profile_coordinates_used_for_diagnostic_reconstruction": 2,
        },
        "outputs": {
            "reconstruction": str(RECONSTRUCTION.relative_to(ROOT)).replace("\\", "/"),
            "rational_candidate": str(RATIONAL.relative_to(ROOT)).replace("\\", "/"),
            "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_QuarkLeptonDoubletResolvedPositiveDensitySource_or_KineticWeightEmission_v1",
        "status": STATUS,
        "one_factor_no_go_proved": True,
        "unique_twofactor_s_t": [s_fit, t_fit],
        "inferred_costs": [q_cost_fit, e_cost_fit],
        "rational_cost_candidate": [14.0 / 3.0, 3.0],
        "rational_candidate_K_over_K2": [candidate_ratios[0], 1.0, candidate_ratios[1]],
        "rational_candidate_relative_residual_U1_SU3": relative_residuals,
        "strict_source_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Quark/Lepton-Resolved Positive Density Source or Kinetic Weight Emission v1

## Exact reduction

Starting from the A67 positive C1 traces, the minimal Q/L-resolved ansatz is

```text
(Q,u,d,L,e,N) = (12s,6s,6s,12,6t,6).
```

It gives `K3/K2=3s/(3s+1)`. If only the colored factor is allowed (`t=1`), elimination of
`s` proves the exact relation

```text
K1/K2 = 6/5 - (4/5)(K3/K2).
```

At the accepted color ratio this predicts `{one_factor_r1_at_target_r3:.15g}`, not
`{r1:.15g}`. Quark suppression alone is therefore insufficient.

## Unique two-factor reconstruction

The two independent profile ratios invert uniquely to

```text
s = {s_fit:.17g},  -log(s)/tau_int = {q_cost_fit:.17g},
t = {t_fit:.17g},   log(t)/tau_int = {e_cost_fit:.17g}.
```

This is an exact reconstruction, not a prediction: it uses two measured profile coordinates.

## Source-native clue

The inferred costs lie strikingly close to `14/3` and `3`. With the already selected
`tau_int=log(448)/15`, those simple costs give

```text
s = 448^(-14/45), t = 448^(1/5),
K/K2 = {[candidate_ratios[0], 1.0, candidate_ratios[1]]},
relative residuals (U1,SU3) = {relative_residuals}.
```

The SU3 residual is about `0.0155%`; the U1 residual is about `0.764%`. This is useful evidence for
a two-order source, but not closure. There is now a corpus-native factorization clue:

```text
colored cost = nil sevenfold * color-completion Schur half * C2(3)
             = 7 * (1/2) * (4/3) = 14/3,
lepton cost  = three charged-lepton basins * conjectural unit circle cost = 3.
```

The Schur half and the three-basin structure are supported, but the nil sevenfold remains a
carried-forward candidate and no theorem yet maps each charged-lepton basin to a unit positive
kinetic exponent. Therefore neither cost is yet emitted by one selected MTT operator.

Next artifact: `{NEXT}`.
"""

    dump(RECONSTRUCTION, reconstruction)
    dump(RATIONAL, rational)
    dump(CONTRACT, contract)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
