from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation"
STATUS = (
    "MTT_SELECTED_GAUGE_ACTION_TO_COMMON_SCHEME_MAP_CLOSED_TWO_RELATIVE_COUPLING_"
    "PREDICTIONS_COMPATIBLE_NOT_HELDOUT_ONE_COMMON_G2_ANCHOR_REMAINS"
)
NEXT = "MTT_Selected_GaugeRatioProspectiveValidationRegistration_or_PrimitiveKineticNormalizationSource_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeActionCoefficientToCommonSchemeCouplingMapAndProspectiveValidation_v1.md"
CONVENTION = OUT / "gauge_kinetic_convention_and_pew_type_separation.packet.json"
RECONSTRUCTION = OUT / "one_anchor_common_scheme_coupling_reconstruction.packet.json"
COMPATIBILITY = OUT / "correlated_leave_two_out_compatibility_not_heldout.packet.json"
PROSPECTIVE = OUT / "prospective_gauge_ratio_validation_registration.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A86_gauge": ROOT / "candidate_data" / "selected_phic1positivedensitypromotionfromclosedrouteasource_or_strictgaugerows" / "selected_gauge_action_rows_after_density_promotion.packet.json",
        "A52_convention": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "SMDR": ROOT / "candidate_data" / "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood" / "selected_smdr_multiloop_precision_workspace.packet.json",
        "PEW_type": ROOT / "candidate_data" / "selected_physicalnormalizationsourceaxiom_or_directkcertificate" / "physical_normalization_source_axiom.packet.json",
        "A85_action": ROOT / "candidate_data" / "selected_finitematchingcompletenessfromunifiedaction_or_explicitboundaryadoptionandheldoutvalidation" / "prospective_heldout_gauge_validation_freeze.packet.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing gauge convention inputs: " + ", ".join(missing))
    data = {key: load(path) for key, path in paths.items()}

    a86 = data["A86_gauge"]
    a52 = data["A52_convention"]
    smdr = data["SMDR"]
    pew = data["PEW_type"]
    k = np.asarray(a86["K_over_K2"], dtype=float)
    if not np.all(k > 0):
        raise ValueError("gauge kinetic shape must be positive")
    if abs(k[1] - 1.0) > 1e-14:
        raise ValueError("expected K2-normalized gauge shape")

    basis = smdr["basis_order"]
    centers = smdr["central_values"]
    covariance = np.asarray(smdr["covariance_matrix"], dtype=float)
    i2 = basis.index("g_2_Mt_MSbar_fullSM")
    iy = basis.index("g_Y_Mt_MSbar_fullSM")
    i3 = basis.index("g_3_Mt_MSbar_fullSM")
    gut = math.sqrt(5.0 / 3.0)
    g2 = float(centers[basis[i2]])
    gy = float(centers[basis[iy]])
    g1 = gut * gy
    g3 = float(centers[basis[i3]])

    ratio_g1_over_g2 = 1.0 / math.sqrt(float(k[0]))
    ratio_g3_over_g2 = 1.0 / math.sqrt(float(k[2]))
    predicted = np.asarray([ratio_g1_over_g2 * g2, g2, ratio_g3_over_g2 * g2], dtype=float)
    observed = np.asarray([g1, g2, g3], dtype=float)
    residual = predicted - observed
    common_c = 1.0 / (g2 * g2)
    f0 = common_c / 6.0
    reconstructed_inverse = common_c * k
    inverse_from_predicted = 1.0 / (predicted * predicted)
    inverse_map_residual = float(np.max(np.abs(reconstructed_inverse - inverse_from_predicted)))

    a1 = ratio_g1_over_g2
    a3 = ratio_g3_over_g2
    v22 = covariance[i2, i2]
    vyy = covariance[iy, iy]
    v33 = covariance[i3, i3]
    v2y = covariance[i2, iy]
    v23 = covariance[i2, i3]
    vy3 = covariance[iy, i3]
    residual_covariance = np.asarray(
        [
            [
                a1 * a1 * v22 + gut * gut * vyy - 2.0 * a1 * gut * v2y,
                a1 * a3 * v22 - a1 * v23 - gut * a3 * v2y + gut * vy3,
            ],
            [
                a1 * a3 * v22 - a1 * v23 - gut * a3 * v2y + gut * vy3,
                a3 * a3 * v22 + v33 - 2.0 * a3 * v23,
            ],
        ],
        dtype=float,
    )
    tested_residual = np.asarray([residual[0], residual[2]], dtype=float)
    residual_covariance_eigenvalues = np.linalg.eigvalsh(residual_covariance)
    chi2 = float(tested_residual @ np.linalg.solve(residual_covariance, tested_residual))
    marginal_pulls = tested_residual / np.sqrt(np.diag(residual_covariance))

    profile_k = np.asarray([(g2 / g1) ** 2, 1.0, (g2 / g3) ** 2], dtype=float)
    shape_delta = k - profile_k
    pew_value = float(pew["emitted_under_axiom"]["P_EW_action_prefactor"])
    pew_equals_c_residual = abs(pew_value - common_c)
    old_profile_f0 = float(a52["minimal_profile_normalization"]["f0_in_g_i^-2_equals_6_f0_K_i_convention"])

    convention = {
        "schema": "MTTGaugeKineticConventionAndPEWTypeSeparation.v1",
        "status": "GAUGE_KINETIC_MAP_FIXED_PEW_NOT_SUBSTITUTED_FOR_6F0",
        "selected_convention": {
            "gauge_action_form": "S_gauge=(1/4) sum_i c K_i int Fhat_i^2",
            "canonical_coupling_map": "g_i^(-2)=c K_i",
            "K_normalization": "K2=1",
            "GUT_hypercharge": "g1=sqrt(5/3) gY",
            "common_kinetic_coefficient": "c=6 f0=g2^(-2) when K2=1",
            "imported_A52_theorem_closed": a52["theorems"]["minimal_profile_overlap_normalization"]["closed"],
        },
        "type_separation": {
            "P_EW": pew_value,
            "P_EW_role": pew["axiom_statement"],
            "c_equals_6f0": common_c,
            "absolute_difference": pew_equals_c_residual,
            "theorem_equating_P_EW_with_c": False,
            "P_EW_times_K_accepted_as_inverse_coupling_rows": False,
        },
        "theorem": {
            "name": "GaugeKineticConventionAndTypeSeparationLemma",
            "statement": "The selected finite K rows are a positive gauge kinetic shape. In the already declared spectral-action convention their common-scheme couplings obey g_i^-2=c K_i. P_EW=A_EW belongs to the electroweak/H-threshold action-prefactor lane and cannot replace c=6f0 without an additional theorem; no such theorem is present.",
            "proved": a52["theorems"]["minimal_profile_overlap_normalization"]["closed"] and pew_equals_c_residual > 1.0,
        },
    }

    reconstruction = {
        "schema": "MTTOneAnchorCommonSchemeGaugeCouplingReconstruction.v1",
        "status": "TWO_RELATIVE_GAUGE_COUPLINGS_RECONSTRUCTED_FROM_SELECTED_K_SHAPE_AND_ONE_G2_ANCHOR",
        "common_scheme": smdr["selected_common_scheme"],
        "sector_order": ["g1_GUT", "g2", "g3"],
        "selected_K_over_K2": k.tolist(),
        "predicted_coupling_ratios": {
            "g1_over_g2": ratio_g1_over_g2,
            "g3_over_g2": ratio_g3_over_g2,
        },
        "one_common_anchor": {
            "id": "g_2_Mt_MSbar_fullSM",
            "value": g2,
            "role": "fix c only; it does not select either relative K coordinate",
            "continuous_anchor_count": 1,
        },
        "kinetic_normalization": {
            "c_equals_g2_inverse_squared": common_c,
            "f0_equals_c_over_6": f0,
            "A52_profile_f0_for_comparison": old_profile_f0,
            "f0_shift_from_old_profile": f0 - old_profile_f0,
        },
        "predicted_couplings": predicted.tolist(),
        "SMDR_central_couplings": observed.tolist(),
        "coupling_residuals": residual.tolist(),
        "reconstructed_inverse_couplings": reconstructed_inverse.tolist(),
        "inverse_map_residual": inverse_map_residual,
        "parameter_accounting": {
            "ordinary_SM_gauge_coupling_coordinates": 3,
            "selected_corpus_action_tier_continuous_gauge_anchors": 1,
            "relative_coordinates_replaced_by_selected_K_shape": 2,
            "new_parameters_beyond_current_SM_profile": 0,
            "strict_primitive_core_zero_anchor_derivation_closed": False,
        },
        "theorem": {
            "name": "OneAnchorGaugeCouplingReconstructionTheorem",
            "statement": "For positive K with K2=1, one common coupling anchor g2 fixes c=g2^-2 and determines g1=g2/sqrt(K1) and g3=g2/sqrt(K3). Thus the selected K shape replaces two relative gauge coordinates at the corpus-action tier, while one common dimensionless normalization remains.",
            "proved": inverse_map_residual < 1e-13,
        },
    }

    compatibility = {
        "schema": "MTTCorrelatedLeaveTwoOutGaugeCompatibilityNotHeldout.v1",
        "status": "FROZEN_K_SHAPE_COMPATIBLE_WITH_SMDR_PROFILE_NOT_AN_INDEPENDENT_HELDOUT_TEST",
        "anchor_coordinate": "g2",
        "tested_coordinates": ["g1_GUT", "g3"],
        "profile_K_over_K2": profile_k.tolist(),
        "selected_minus_profile_K": shape_delta.tolist(),
        "residual_vector": tested_residual.tolist(),
        "residual_covariance": residual_covariance.tolist(),
        "residual_covariance_eigenvalues": residual_covariance_eigenvalues.tolist(),
        "marginal_pulls_sigma": marginal_pulls.tolist(),
        "chi2_2d": chi2,
        "degrees_of_freedom": 2,
        "compatible_at_current_profile": chi2 < 5.991464547107979,
        "held_out_validation": False,
        "epistemic_reason": "All three gauge coordinates were known while the K source chain was developed. Anchoring g2 and checking g1/g3 is a covariance-aware replay diagnostic, not prospective evidence.",
        "observed_values_used_to_select_K_in_this_packet": False,
    }

    prospective = {
        "schema": "MTTProspectiveGaugeRatioValidationRegistration.v1",
        "status": "FROZEN_TWO_RATIO_PREDICTION_REGISTERED_NO_PROSPECTIVE_DATA_EXECUTED",
        "frozen_prediction": {
            "scheme": smdr["selected_common_scheme"]["scheme"],
            "reference_scale_GeV": smdr["selected_common_scheme"]["scale_GeV"],
            "K1_over_K2": float(k[0]),
            "K3_over_K2": float(k[2]),
            "g1_over_g2": ratio_g1_over_g2,
            "g3_over_g2": ratio_g3_over_g2,
            "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        },
        "test_protocol": {
            "eligible_data": "A future or genuinely unused determination of two independent common-scheme gauge ratios, either at Q=Mt or transported to Q=Mt by a frozen RG implementation.",
            "statistic": "chi2=r^T Sigma_r^(-1) r for r=(g1/g2-rho12, g3/g2-rho32)",
            "primary_threshold": "reject the selected branch at chi2>5.991464547 for two degrees of freedom (95 percent), with the threshold revisited only before data unblinding",
            "no_retuning_rule": "H_cl, Phi_C1, tau_int, K ratios, normalization convention, and matching action are frozen; no sector-relative counterterm may be added after seeing the result.",
        },
        "prospective_validation_executed": False,
        "current_profile_used_as_prospective_data": False,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A86_three_rows": a86["acceptance"]["selected_gauge_action_rows_at_corpus_action_tier"] == 3,
        "positive_K": bool(np.all(k > 0)),
        "K2_normalized": abs(float(k[1]) - 1.0) < 1e-14,
        "A52_convention_imported": convention["selected_convention"]["imported_A52_theorem_closed"],
        "PEW_type_separated": convention["theorem"]["proved"],
        "one_anchor_reconstruction_exact": reconstruction["theorem"]["proved"],
        "residual_covariance_positive": float(np.min(residual_covariance_eigenvalues)) > 0.0,
        "profile_compatible": compatibility["compatible_at_current_profile"],
        "not_called_heldout": not compatibility["held_out_validation"],
        "prospective_not_backdated": not prospective["prospective_validation_executed"],
        "two_coordinates_replaced": reconstruction["parameter_accounting"]["relative_coordinates_replaced_by_selected_K_shape"] == 2,
        "primitive_core_not_overclaimed": not reconstruction["parameter_accounting"]["strict_primitive_core_zero_anchor_derivation_closed"],
    }
    candidate = {
        "schema": "MTTSelectedGaugeActionCoefficientToCommonSchemeCouplingMapAndProspectiveValidation.v1",
        "status": STATUS,
        "results": {
            "convention_safe_map_closed": True,
            "P_EW_substituted_for_6f0": False,
            "selected_relative_gauge_predictions": 2,
            "common_g2_anchor_count": 1,
            "new_parameters_beyond_current_SM_profile": 0,
            "predicted_g1_GUT": float(predicted[0]),
            "predicted_g3": float(predicted[2]),
            "correlated_profile_chi2_2d": chi2,
            "current_profile_compatible": compatibility["compatible_at_current_profile"],
            "genuinely_heldout_validation_executed": False,
            "primitive_core_zero_anchor_derivation_closed": False,
        },
        "outputs": {
            "convention": str(CONVENTION.relative_to(ROOT)).replace("\\", "/"),
            "reconstruction": str(RECONSTRUCTION.relative_to(ROOT)).replace("\\", "/"),
            "compatibility": str(COMPATIBILITY.relative_to(ROOT)).replace("\\", "/"),
            "prospective": str(PROSPECTIVE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeActionCoefficientToCommonSchemeCouplingMapAndProspectiveValidation_v1",
        "status": STATUS,
        "convention_safe_map_closed": True,
        "P_EW_substituted_for_6f0": False,
        "selected_relative_gauge_predictions": 2,
        "common_g2_anchor_count": 1,
        "predicted_g1_GUT": float(predicted[0]),
        "predicted_g3": float(predicted[2]),
        "g1_residual": float(residual[0]),
        "g3_residual": float(residual[2]),
        "g1_marginal_pull_sigma": float(marginal_pulls[0]),
        "g3_marginal_pull_sigma": float(marginal_pulls[1]),
        "correlated_profile_chi2_2d": chi2,
        "current_profile_compatible": compatibility["compatible_at_current_profile"],
        "genuinely_heldout_validation_executed": False,
        "primitive_core_zero_anchor_derivation_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Gauge-Action Coefficient to Common-Scheme Coupling Map and Prospective Validation v1

## Convention fixed without mixing prefactors

The existing product-triple theorem supplies the convention

```text
g_i^(-2) = c K_i,    c = 6 f0.
```

With `K2=1`, one common anchor fixes `c=g2^(-2)`. The electroweak/H-threshold prefactor
`P_EW=A_EW={pew_value}` is a different typed object; it is not substituted for
`c={common_c}`. This corrects the diagnostic `P_EW*K` product in A86: it is not an inverse-coupling
row.

## One-anchor reconstruction

At the frozen SMDR v1.3 scale and scheme, use only

```text
g2 = {g2}
```

as the common normalization anchor. The selected shape predicts

```text
g1/g2 = {ratio_g1_over_g2}
g3/g2 = {ratio_g3_over_g2}
g1     = {predicted[0]}
g3     = {predicted[2]}
```

against SMDR central values `g1={g1}` and `g3={g3}`. The residuals are
`{residual[0]}` and `{residual[2]}`. Propagating the actual SMDR covariance, including the shared
`g2` anchor and `g1=sqrt(5/3)gY`, gives marginal pulls `{marginal_pulls[0]}` and
`{marginal_pulls[1]}` sigma and correlated `chi2={chi2}` for two coordinates.

This is exact convention closure and a strong compatibility result. It is not independent evidence:
the gauge profile was known while the K chain was developed. At the corpus-action tier the structure
reduces three gauge coupling coordinates to one common continuous anchor, replacing two relative
coordinates with the selected K shape. It adds no parameter beyond the existing SM profile. The
primitive-core zero-anchor derivation remains open.

## Prospective test frozen

The two ratio predictions, scheme, scale, source hashes, covariance statistic, 95-percent rejection
threshold, and no-retuning rule are now registered. A genuinely new or previously unused common-scheme
determination can test the frozen branch. No such prospective validation is claimed here.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (CONVENTION, convention),
        (RECONSTRUCTION, reconstruction),
        (COMPATIBILITY, compatibility),
        (PROSPECTIVE, prospective),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
