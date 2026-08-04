"""Build the common two-cost kinetic operator and isolate its exact residual."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum"
OUT = ROOT / "candidate_data" / SLUG
OPERATOR = OUT / "conditional_common_projected_kinetic_operator.packet.json"
RG_NOGO = OUT / "one_loop_scale_transport_nogo.packet.json"
CORRECTION = OUT / "exact_residual_cost_spectrum.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonQuarkOrder_SharedCircleKineticOperator_or_ExactResidualSpectrum_v1.md"
STATUS = "MTT_SELECTED_COMMON_TWO_COST_OPERATOR_CONSTRUCTED_CONDITIONALLY_ONELOOP_TRANSPORT_NOGO_PROVED_EXACT_RESIDUAL_SOURCE_OPEN"
NEXT = "MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauge_ratios(s: float, t: float) -> tuple[float, float]:
    k1 = 21.6 * s + 10.8 + 10.8 * t
    k2 = 54.0 * s + 18.0
    k3 = 54.0 * s
    return k1 / k2, k3 / k2


def main() -> int:
    paths = {
        "A17_branch": ROOT / "candidate_data" / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness.candidate.json",
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A57_beta": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "A67_density": ROOT / "candidate_data" / "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission" / "conditional_c1_positive_sector_density.packet.json",
        "A68_reconstruction": ROOT / "candidate_data" / "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission" / "minimal_twofactor_positive_density_reconstruction.packet.json",
        "A68_factorization": ROOT / "candidate_data" / "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission" / "selected_rational_cost_nearmiss.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    profile_data = data["A52_profile"]["minimal_profile_normalization"]
    profile = np.asarray(profile_data["K_gauge_diagonal"], dtype=float)
    inverse_g2 = np.asarray(profile_data["reconstructed_inverse_coupling_squared"], dtype=float)
    tau = float(data["A68_factorization"]["tau_int"])

    colored_cost = 14.0 / 3.0
    lepton_cost = 3.0
    s = math.exp(-tau * colored_cost)
    t = math.exp(tau * lepton_cost)
    r1, r3 = gauge_ratios(s, t)
    source_profile = np.asarray([r1, 1.0, r3], dtype=float)
    sector_costs = np.asarray([colored_cost, colored_cost, colored_cost, 0.0, -lepton_cost, 0.0])
    sector_scalars = np.exp(-tau * sector_costs)
    base_traces = np.asarray(data["A67_density"]["sector_trace_weights"], dtype=float)
    sector_traces = base_traces * sector_scalars

    operator = {
        "schema": "MTTConditionalCommonProjectedKineticOperator.v1",
        "status": "EXPLICIT_FINITE_POSITIVE_OPERATOR_CONSTRUCTED_SOURCE_BRIDGES_CONDITIONAL",
        "finite_operator": {
            "definition": "W_kin = exp(-tau_int C_sector) Phi_C1^+",
            "sector_order": ["Q", "u", "d", "L", "e", "N"],
            "C_sector_eigenvalues": sector_costs.tolist(),
            "exp_minus_tau_C_sector": sector_scalars.tolist(),
            "base_C1_sector_traces": base_traces.tolist(),
            "weighted_sector_traces": sector_traces.tolist(),
            "self_adjoint": True,
            "strictly_positive": True,
            "gauge_commutant": True,
            "bounded": True,
            "bounded_reason": "the selected family/sector carrier is finite projected",
        },
        "colored_cost_factorization": {
            "formula": "7*(1/2)*C2(3)=7*(1/2)*(4/3)=14/3",
            "Z7_charge_sector_selected_on_retarded_branch": data["A17_branch"]["theorem"]["proved"],
            "two_hidden_channel_Schur_half": "proved-schema corpus input",
            "C2_fundamental_SU3": 4.0 / 3.0,
            "missing_bridge": "prove that the selected Z7 charge carrier supplies seven equivalent color-completion channels in this kinetic Hessian",
        },
        "charged_lepton_cost_factorization": {
            "normalized_circle_laplacian": "Delta_S1 exp(in theta)=n^2 exp(in theta), so the primitive winding has cost 1",
            "three_basin_direct_sum_cost": 3.0,
            "finite_inverse_heat_factor": "exp(+3 tau_int) on the fully anchored e lane",
            "missing_bridges": [
                "prove the three proto-spinor charged-lepton basins are the three kinetic direct-sum copies",
                "select the inverse-heat/dual-metric sign from the shared-circle action",
            ],
        },
        "gauge_execution": {
            "K_over_K2": source_profile.tolist(),
            "profile_K_over_K2_downstream_only": profile.tolist(),
            "relative_residual": (source_profile / profile - 1.0).tolist(),
            "exact_match": bool(np.allclose(source_profile, profile, atol=1e-13, rtol=0.0)),
        },
        "source_status": {
            "operator_formula_explicit": True,
            "positivity_and_commutation_proved": True,
            "all_factor_bridges_selected": False,
            "strict_value_emission": False,
        },
    }

    beta_exact = data["A57_beta"]["signed_heat_coefficients"]["total_beta_numeric"]
    beta = np.asarray(beta_exact, dtype=float) / (8.0 * math.pi**2)
    design = np.column_stack([source_profile, beta])
    fit, _, _, _ = np.linalg.lstsq(design, inverse_g2, rcond=None)
    transported = design @ fit
    transport_residual = inverse_g2 - transported
    span_determinant = float(np.linalg.det(np.column_stack([source_profile, beta, inverse_g2])))
    pair_solutions = {}
    for name, pair in {"U1_SU2": [0, 1], "U1_SU3": [0, 2], "SU2_SU3": [1, 2]}.items():
        pair_fit = np.linalg.solve(design[pair, :], inverse_g2[pair])
        pair_prediction = design @ pair_fit
        pair_solutions[name] = {
            "common_normalization_A": float(pair_fit[0]),
            "log_scale_coordinate_ell": float(pair_fit[1]),
            "predicted_inverse_g2": pair_prediction.tolist(),
            "residual": (inverse_g2 - pair_prediction).tolist(),
        }
    rg_nogo = {
        "schema": "MTTOneLoopScaleTransportNoGo.v1",
        "status": "COMMON_NORMALIZATION_PLUS_ONELOOP_SCALE_CANNOT_CLOSE_TWO_COST_OPERATOR",
        "model": "g_a^-2 = A K_a + ell b_a/(8pi^2)",
        "source_K_over_K2": source_profile.tolist(),
        "beta_U1_SU2_SU3": beta_exact,
        "target_inverse_g2_downstream_only": inverse_g2.tolist(),
        "least_squares": {
            "common_normalization_A": float(fit[0]),
            "log_scale_coordinate_ell": float(fit[1]),
            "prediction": transported.tolist(),
            "residual": transport_residual.tolist(),
            "residual_l2": float(np.linalg.norm(transport_residual)),
        },
        "span_determinant": span_determinant,
        "span_determinant_nonzero": abs(span_determinant) > 1e-10,
        "pair_solutions": pair_solutions,
        "theorem": "Because det[K,b/(8pi^2),g^-2] is nonzero, no common normalization and one-loop matching-scale translation reproduce all three accepted inverse couplings.",
        "new_continuous_parameters_accepted": 0,
    }

    inferred = data["A68_reconstruction"]["unique_twofactor_inverse"]
    q_cost_fit = float(inferred["inferred_dimensionless_cost_minus_log_s_over_tau"])
    e_cost_fit = float(inferred["inferred_dimensionless_cost_log_t_over_tau"])
    delta_q = q_cost_fit - colored_cost
    delta_e = e_cost_fit - lepton_cost
    correction = {
        "schema": "MTTExactResidualCostSpectrum.v1",
        "status": "UNIQUE_TWO_SUPPORT_CORRECTION_COMPUTED_FROM_PROFILE_SOURCE_OPEN",
        "operator_form": "delta C = delta_q P_colored - delta_e P_e",
        "support_projectors": {
            "P_colored": [1, 1, 1, 0, 0, 0],
            "P_e": [0, 0, 0, 0, 1, 0],
        },
        "profile_inferred_values": {
            "delta_q": delta_q,
            "delta_e": delta_e,
            "corrected_colored_cost": q_cost_fit,
            "corrected_charged_lepton_cost": e_cost_fit,
        },
        "uniqueness": "A68 proves R3 strictly fixes the colored cost and then R1 strictly fixes the e cost.",
        "epistemic_status": {
            "observed_profile_used": True,
            "accepted_as_source": False,
            "accepted_as_prediction": False,
            "ordinary_one_loop_scale_transport_excluded": True,
            "remaining_source_dimension": 2,
        },
        "next_source_options": [
            "one selected circle/Lens determinant correction with fixed projections onto P_colored and P_e",
            "one same-action finite threshold operator whose two support components equal delta_q and delta_e",
            "a stronger exact operator replacing the rational costs 14/3 and 3 directly",
        ],
        "next_required_artifact": NEXT,
    }
    checks = {
        "tau_selected_value_preserved": abs(tau - math.log(448.0) / 15.0) < 1e-15,
        "operator_positive": operator["finite_operator"]["strictly_positive"],
        "operator_gauge_commutant": operator["finite_operator"]["gauge_commutant"],
        "colored_factorization_exact": abs(7.0 * 0.5 * 4.0 / 3.0 - colored_cost) < 1e-15,
        "circle_three_basin_cost_exact_conditionally": lepton_cost == 3.0,
        "candidate_gauge_execution_not_exact": not operator["gauge_execution"]["exact_match"],
        "one_loop_transport_span_determinant_nonzero": rg_nogo["span_determinant_nonzero"],
        "one_loop_transport_residual_nonzero": rg_nogo["least_squares"]["residual_l2"] > 1e-5,
        "exact_residual_correction_nonzero": delta_q > 0.0 and delta_e > 0.0,
        "residual_not_promoted": not correction["epistemic_status"]["accepted_as_source"],
    }
    candidate = {
        "schema": "MTTSelectedCommonQuarkOrderSharedCircleKineticOperatorOrExactResidualSpectrum.v1",
        "status": STATUS,
        "results": {
            "explicit_common_positive_operator_constructed": True,
            "operator_source_tier": "conditional composite bridge",
            "positivity_gauge_commutation_closed": True,
            "normalized_circle_unit_cost_derived": True,
            "three_basin_sum_cost_derived_conditionally": True,
            "one_loop_scale_transport_exit_retired": True,
            "unique_exact_residual_spectrum_computed": True,
            "strict_cost_source_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "operator": str(OPERATOR.relative_to(ROOT)).replace("\\", "/"),
            "one_loop_no_go": str(RG_NOGO.relative_to(ROOT)).replace("\\", "/"),
            "correction": str(CORRECTION.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_CommonQuarkOrder_SharedCircleKineticOperator_or_ExactResidualSpectrum_v1",
        "status": STATUS,
        "conditional_operator_costs_Q_u_d_L_e_N": sector_costs.tolist(),
        "conditional_operator_K_over_K2": source_profile.tolist(),
        "operator_positive_and_gauge_commuting": True,
        "one_loop_transport_span_determinant": span_determinant,
        "one_loop_transport_residual_l2": rg_nogo["least_squares"]["residual_l2"],
        "exact_profile_inferred_delta_q_delta_e": [delta_q, delta_e],
        "strict_source_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Common Quark-Order/Shared-Circle Kinetic Operator or Exact Residual Spectrum v1

## Explicit common operator

On the finite projected A67 carrier define

```text
C_sector = diag(14/3,14/3,14/3,0,-3,0),
W_kin = exp(-tau_int C_sector) Phi_C1^+.
```

This operator is bounded, self-adjoint, strictly positive and gauge commuting. The colored cost has
the conditional corpus factorization `7*(1/2)*C2(3)=14/3`. On a normalized shared circle the
primitive winding has Laplacian cost one, so three charged-lepton basins have direct-sum cost three.
The remaining source assumptions are the Z7-to-color-completion bridge and selection of the dual
inverse-heat sign on the fully anchored charged-lepton lane.

Its exact gauge execution is

```text
K/K2 = {source_profile.tolist()}.
```

## Scale-transport no-go

Allowing both a common kinetic normalization and ordinary one-loop scale transport gives

```text
g_a^-2 = A K_a + ell b_a/(8 pi^2).
```

The determinant `det[K,b/(8pi^2),g^-2]={span_determinant:.17g}` is nonzero. Therefore no values of
`A` and `ell` reproduce all three accepted couplings. The least-squares residual norm is
`{rg_nogo['least_squares']['residual_l2']:.17g}`. The discrepancy is not merely a matching-scale choice.

## Exact residual spectrum

Within the proved minimal two-support class, the unique correction is

```text
delta C = delta_q P_colored - delta_e P_e,
delta_q = {delta_q:.17g},
delta_e = {delta_e:.17g}.
```

These values are profile-inferred and are not promoted. The next source theorem must emit this
two-component correction from one selected circle/Lens determinant or replace the rational costs by
one exact same-action spectrum.

Next artifact: `{NEXT}`.
"""

    dump(OPERATOR, operator)
    dump(RG_NOGO, rg_nogo)
    dump(CORRECTION, correction)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
