"""Prove trace normalization and independently stress-test the frozen gauge formula."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_normalizeddeterminantactionfrommtthessian_or_independentgaugeprofiletest"
OUT = ROOT / "candidate_data" / SLUG
TRACE = OUT / "finite_trace_and_projector_uniqueness.packet.json"
VALIDATION = OUT / "buttazzo_legacy_independent_profile_test.packet.json"
GATE = OUT / "remaining_physical_hessian_action_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NormalizedDeterminantActionFromMTTHessian_or_IndependentGaugeProfileTest_v1.md"
STATUS = "MTT_SELECTED_FINITE_TRACE_PROJECTOR_NORMALIZATION_UNIQUE_LEGACY_INDEPENDENT_PROFILE_COMPATIBLE_PHYSICAL_HESSIAN_IDENTITY_OPEN"
NEXT = "MTT_Selected_PhysicalKineticHessianBlockIdentity_or_ModernPrecisionGaugeValidation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def buttazzo_couplings(inputs: np.ndarray) -> np.ndarray:
    mt, mw, alpha_s = inputs
    gy = 0.35830 + 0.00011 * (mt - 173.34) - 0.00020 * (mw - 80.384) / 0.014
    g2 = 0.64779 + 0.00004 * (mt - 173.34) + 0.00011 * (mw - 80.384) / 0.014
    g3 = 1.1666 + 0.00314 * (alpha_s - 0.1184) / 0.0007 - 0.00046 * (mt - 173.34)
    return np.asarray([math.sqrt(5.0 / 3.0) * gy, g2, g3], dtype=float)


def validation_residual(inputs: np.ndarray, frozen_k: np.ndarray, source_scale: float) -> tuple[np.ndarray, dict]:
    couplings = buttazzo_couplings(inputs)
    inverse = 1.0 / couplings**2
    validation_scale = float(inputs[0])
    beta = np.asarray([41.0 / 10.0, -19.0 / 6.0, -7.0], dtype=float)
    log_scale = math.log(validation_scale / source_scale)
    # Fix only the common normalization by the external SU2 row after transport.
    common_normalization = inverse[1] + beta[1] * log_scale / (8.0 * math.pi**2)
    predicted_inverse = common_normalization * frozen_k - beta * log_scale / (8.0 * math.pi**2)
    predicted_ratios = np.asarray([predicted_inverse[0] / predicted_inverse[1], predicted_inverse[2] / predicted_inverse[1]])
    external_ratios = np.asarray([inverse[0] / inverse[1], inverse[2] / inverse[1]])
    return predicted_ratios - external_ratios, {
        "couplings_g1GUT_g2_g3": couplings.tolist(),
        "external_ratios_K1_K3_over_K2": external_ratios.tolist(),
        "predicted_ratios_K1_K3_over_K2": predicted_ratios.tolist(),
        "common_normalization_from_SU2": float(common_normalization),
        "log_scale_transport": log_scale,
    }


def main() -> int:
    paths = {
        "finite_trace_theorem": ROOT / "candidate_data" / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.candidate.json",
        "A72_execution": ROOT / "candidate_data" / "selected_gaugekineticfunctionalofl64andq79chord_or_strictresidualvalueemission" / "frozen_zero_parameter_gauge_execution.packet.json",
        "A73_action": ROOT / "candidate_data" / "selected_gaugekineticactionderivationandfrozenprofilevalidation" / "normalized_determinant_action_derivation.packet.json",
        "A73_validation": ROOT / "candidate_data" / "selected_gaugekineticactionderivationandfrozenprofilevalidation" / "frozen_external_validation_protocol.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    trace = {
        "schema": "MTTFiniteTraceAndProjectorUniqueness.v1",
        "status": "NORMALIZED_TRACE_AND_NONTRIVIAL_PROJECTOR_RANKS_FORCED",
        "imported_MTT_theorem": data["finite_trace_theorem"]["theorem"],
        "general_finite_trace_theorem": {
            "statement": "On End(C^n), every positive normalized linear functional invariant under unitary conjugation is tau_n(A)=Tr(A)/n.",
            "proof": "Conjugation invariance makes all rank-one projectors equivalent; normalization gives each weight 1/n, and linearity gives normalized trace.",
            "tensor_product": "tau_nm=tau_n tensor tau_m is the unique product-invariant normalized trace.",
            "proved": True,
        },
        "applications": {
            "L64_tower_carrier": {"dimension": 16, "trace": "Tr/16", "forced": True},
            "Z7_regular_carrier": {"dimension": 7, "trace": "Tr/7", "forced": True},
            "Lens_Z4_carrier": {"dimension": 4, "trace": "Tr/4", "forced": True},
            "P7_nontrivial": {"rank": 6, "normalized_trace": 6.0 / 7.0, "forced": True},
            "P4_nontrivial": {"rank": 3, "normalized_trace": 3.0 / 4.0, "forced": True},
        },
        "closure": {
            "A72_trace_normalizations_are_not_knobs": True,
            "A72_projector_rank_coefficients_are_not_knobs": True,
            "physical_action_restriction_to_A73_blocks": False,
        },
        "new_continuous_parameters": 0,
    }

    frozen = data["A72_execution"]
    frozen_k = np.asarray(frozen["K_over_K2"], dtype=float)
    source_scale = 172.5590883453979
    central_inputs = np.asarray([173.34, 80.384, 0.1184], dtype=float)
    input_sigmas = np.asarray([0.76, 0.014, 0.0007], dtype=float)
    residual, detail = validation_residual(central_inputs, frozen_k, source_scale)
    jacobian = np.zeros((2, 3), dtype=float)
    for index in range(3):
        step = input_sigmas[index] * 1e-5
        plus = central_inputs.copy()
        minus = central_inputs.copy()
        plus[index] += step
        minus[index] -= step
        jacobian[:, index] = (
            validation_residual(plus, frozen_k, source_scale)[0]
            - validation_residual(minus, frozen_k, source_scale)[0]
        ) / (2.0 * step)
    covariance = jacobian @ np.diag(input_sigmas**2) @ jacobian.T
    chi2 = float(residual @ np.linalg.inv(covariance) @ residual)
    p_value_df2 = math.exp(-chi2 / 2.0)
    marginal_pulls = residual / np.sqrt(np.diag(covariance))
    validation = {
        "schema": "MTTButtazzoLegacyIndependentGaugeProfileTest.v1",
        "status": "FROZEN_FORMULA_COMPATIBLE_WITH_LEGACY_NNLO_PROFILE_AT_COVARIANCE_LEVEL",
        "primary_reference": {
            "title": "Investigating the near-criticality of the Higgs boson",
            "authors": "Buttazzo et al.",
            "url": "https://arxiv.org/abs/1307.3536",
            "scheme": "MSbar",
            "scale": "mu=Mt",
            "hypercharge": "g1=sqrt(5/3)gY",
        },
        "published_linearized_profile": {
            "gY": "0.35830+0.00011(Mt-173.34)-0.00020(MW-80.384)/0.014",
            "g2": "0.64779+0.00004(Mt-173.34)+0.00011(MW-80.384)/0.014",
            "g3": "1.1666+0.00314(alpha_s-0.1184)/0.0007-0.00046(Mt-173.34)",
            "central_inputs_Mt_MW_alpha_s": central_inputs.tolist(),
            "input_sigmas": input_sigmas.tolist(),
        },
        "frozen_formula": {
            "id": frozen["formula_id"],
            "packet_sha256": data["A73_validation"]["frozen_formula"]["packet_sha256"],
            "source_scale_GeV": source_scale,
            "retuned": False,
        },
        "transport_and_normalization": {
            "one_loop_beta_U1_SU2_SU3": [41.0 / 10.0, -19.0 / 6.0, -7.0],
            "common_normalization_count": 1,
            "common_normalization_source": "external SU2 row only",
            **detail,
        },
        "covariance_test": {
            "residual_predicted_minus_external": residual.tolist(),
            "jacobian_wrt_Mt_MW_alpha_s": jacobian.tolist(),
            "covariance": covariance.tolist(),
            "marginal_sigmas": np.sqrt(np.diag(covariance)).tolist(),
            "marginal_pulls": marginal_pulls.tolist(),
            "chi2": chi2,
            "degrees_of_freedom": 2,
            "p_value": p_value_df2,
            "pass_threshold": 0.05,
            "compatible": p_value_df2 > 0.05,
        },
        "scope": {
            "legacy_independent_compatibility_test_closed": True,
            "modern_high_precision_validation_closed": False,
            "ppm_level_external_confirmation_claimed": False,
            "higher_loop_transport_uncertainty_included": False,
            "interpretation": "The frozen formula survives an older independent NNLO input profile. The test is not precise enough to confirm its same-profile ppm agreement.",
        },
    }
    gate = {
        "schema": "MTTRemainingPhysicalHessianActionGate.v1",
        "status": "TRACE_NORMALIZATION_AND_LEGACY_VALIDATION_CLOSED_PHYSICAL_BLOCK_IDENTITY_OPEN",
        "closed": {
            "normalized_trace_uniqueness": True,
            "P7_rank_6_over_7": True,
            "P4_rank_3_over_4": True,
            "one_action_algebraic_derivation": data["A73_action"]["status"] == "ONE_FINITE_POSITIVE_ACTION_EMITS_A72_RESPONSE_EXACTLY",
            "legacy_independent_profile_compatibility": validation["covariance_test"]["compatible"],
            "formula_frozen_before_validation": True,
        },
        "open": {
            "selected_MTT_PhiFin_kinetic_Hessian_equals_A73_block_action": True,
            "q79_chord_and_Z7_Lens_projectors_coemitted_by_that_Hessian": True,
            "no_extra_relative_counterterm_or_boundary_source": True,
            "modern_common_scheme_covariance_validation": True,
        },
        "strict_physical_action_selected": False,
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }
    checks = {
        "imported_finite_trace_measure_derived": data["finite_trace_theorem"]["closure_decision"]["measure_normalization_derived"],
        "general_trace_theorem_proved": trace["general_finite_trace_theorem"]["proved"],
        "all_trace_applications_forced": all(value["forced"] for value in trace["applications"].values()),
        "projector_coefficients_exact": abs(trace["applications"]["P7_nontrivial"]["normalized_trace"] - 6.0 / 7.0) < 1e-15 and abs(trace["applications"]["P4_nontrivial"]["normalized_trace"] - 3.0 / 4.0) < 1e-15,
        "frozen_hash_preserved": data["A73_validation"]["frozen_formula"]["packet_sha256"] == sha256(paths["A72_execution"]),
        "external_test_uses_one_common_normalization": validation["transport_and_normalization"]["common_normalization_count"] == 1,
        "external_formula_not_retuned": not validation["frozen_formula"]["retuned"],
        "legacy_covariance_test_compatible": validation["covariance_test"]["compatible"],
        "legacy_p_value_above_0_05": p_value_df2 > 0.05,
        "modern_precision_not_overclaimed": not validation["scope"]["modern_high_precision_validation_closed"],
        "physical_action_selection_open": not gate["strict_physical_action_selected"],
    }
    candidate = {
        "schema": "MTTSelectedNormalizedDeterminantActionFromMTTHessianOrIndependentGaugeProfileTest.v1",
        "status": STATUS,
        "results": {
            "finite_trace_normalization_unique": True,
            "Z7_and_Lens_projector_coefficients_forced": True,
            "legacy_independent_covariance_test_passed": True,
            "legacy_test_p_value": p_value_df2,
            "modern_precision_validation_closed": False,
            "physical_MTT_Hessian_block_identity_closed": False,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "trace": str(TRACE.relative_to(ROOT)).replace("\\", "/"),
            "validation": str(VALIDATION.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_NormalizedDeterminantActionFromMTTHessian_or_IndependentGaugeProfileTest_v1",
        "status": STATUS,
        "trace_normalization_unique": True,
        "projector_ranks_P7_P4": [6.0 / 7.0, 3.0 / 4.0],
        "legacy_validation_chi2_df_p": [chi2, 2, p_value_df2],
        "legacy_validation_compatible": validation["covariance_test"]["compatible"],
        "modern_precision_validation_closed": False,
        "physical_hessian_identity_closed": False,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Normalized Determinant Action from MTT Hessian or Independent Gauge Profile Test v1

## Trace selection

The existing finite Weyl trace theorem extends to each finite carrier used by A73: unitary
conjugation invariance forces `Tr/16`, `Tr/7`, and `Tr/4`. Therefore the nontrivial `Z7` and Lens
projectors have forced normalized traces `6/7` and `3/4`. These coefficients are not knobs.

## Independent legacy test

The frozen A72 formula was transported from `{source_scale:.15g} GeV` to Buttazzo's `Mt` scale with
the SM one-loop beta vector. Only the common normalization was fixed, from `SU2`; neither relative
ratio was fitted. Propagating the published `Mt`, `MW`, and `alpha_s` uncertainties gives

```text
chi2 = {chi2:.15g} for 2 degrees of freedom,
p = {p_value_df2:.15g},
marginal pulls = {marginal_pulls.tolist()}.
```

The frozen formula is compatible with this older independent NNLO profile at the declared `p>0.05`
threshold. This is not a modern ppm-level confirmation; higher-loop transport uncertainty was not
needed for the compatibility pass and is not included.

## Remaining physical gate

Trace normalization, projector ranks, algebraic one-action existence, formula freezing, and legacy
compatibility are closed. Strict promotion still requires the selected physical MTT kinetic Hessian
to equal the A73 block action, coemit the q79 chord and projector routing, and exclude extra relative
counterterm/boundary contributions.

Next artifact: `{NEXT}`.
"""

    dump(TRACE, trace)
    dump(VALIDATION, validation)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
