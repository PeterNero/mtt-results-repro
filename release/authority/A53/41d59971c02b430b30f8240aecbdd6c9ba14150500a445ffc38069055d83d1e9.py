"""Test the selected proper-time atom and zero-knob gauge-overlap candidates."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "proper_time_atom_and_overlap_source_cutset.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ProperTimeMeasureAndOverlapKineticMetricSource_or_StrictSpectralActionClosure_v1.md"
STATUS = "MTT_SELECTED_TAUINT_POINT_MEASURE_CONDITIONAL_MOMENTS_CLOSED_SCALAR_MEASURE_CANNOT_SOURCE_KGAUGE_RANK_METRIC_REJECTED"
NEXT = "MTT_Selected_GaugeOverlapMetricFromLiteralHYMConnections_or_StrictSpectralActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def running_couplings(log_ratio: float, initial: np.ndarray, beta: np.ndarray) -> np.ndarray:
    return 1.0 / np.sqrt(1.0 / initial**2 - beta * log_ratio / (8.0 * math.pi**2))


def gauge_metric(couplings: np.ndarray) -> np.ndarray:
    g1, g2, g3 = couplings
    return np.array([(g2 / g1) ** 2, 1.0, (g2 / g3) ** 2])


def golden_minimum(function, left: float, right: float, iterations: int = 160) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x1, x2 = right - ratio * (right - left), left + ratio * (right - left)
    f1, f2 = function(x1), function(x2)
    for _ in range(iterations):
        if f1 < f2:
            right, x2, f2 = x2, x1, f1
            x1 = right - ratio * (right - left)
            f1 = function(x1)
        else:
            left, x1, f1 = x1, x2, f2
            x2 = left + ratio * (right - left)
            f2 = function(x2)
    point = (left + right) / 2.0
    return point, function(point)


def main() -> int:
    a52_cert = load(ROOT / "certificates" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization_certificate.json")
    a52 = load(ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json")
    tau_cert = load(ROOT / "certificates" / "selected_neutralspectralactionslopeorseesawsource_certificate.json")

    tau = math.log(448.0) / 15.0
    tau_import = float(tau_cert["tau_int"])
    f0 = float(a52["minimal_profile_normalization"]["f0_in_g_i^-2_equals_6_f0_K_i_convention"])

    # For f(x)=f0 exp(-tau*x), f_n=f0/tau^(n/2) in the corpus convention.
    point_moments = {"f0": f0, "f2": f0 / tau, "f4": f0 / tau**2}
    hankel = np.array([[point_moments["f0"], point_moments["f2"]], [point_moments["f2"], point_moments["f4"]]])

    profile_metric = np.array(a52["minimal_profile_normalization"]["K_gauge_diagonal"], dtype=float)
    rank_metric = np.array([2.0, 1.0, 1.0 / 3.0])
    rank_metric_profile_log_residual = float(np.linalg.norm(np.log(profile_metric / rank_metric)))

    scale0 = float(a52["universal_gauge_relation_test"]["source_scale_GeV"])
    initial = np.array(a52["universal_gauge_relation_test"]["source_couplings_g1GUT_g2_g3"], dtype=float)
    beta = np.array(a52["universal_gauge_relation_test"]["one_loop_beta_coefficients"], dtype=float)
    left, right = math.log(50.0 / scale0), math.log(1e19 / scale0)
    best_log, best_rank_score = golden_minimum(
        lambda log_ratio: float(np.linalg.norm(np.log(gauge_metric(running_couplings(log_ratio, initial, beta)) / rank_metric))),
        left,
        right,
    )
    best_rank_scale = scale0 * math.exp(best_log)
    best_rank_metric = gauge_metric(running_couplings(best_log, initial, beta))

    # A scalar cutoff function commutes with the sector trace metric. It changes the
    # common multiplier only, so all ratios K_i/K_j are invariant under every f.
    trial_common_multipliers = [0.25, 1.0, 3.5]
    scalar_measure_ratio_residuals = []
    for multiplier in trial_common_multipliers:
        scaled = multiplier * rank_metric
        scalar_measure_ratio_residuals.append(float(np.linalg.norm(scaled / scaled[1] - rank_metric / rank_metric[1])))

    checks = {
        "A52_profile_normalization_and_universal_no_go_closed": a52_cert["profile_bosonic_matter_normalization_closed"] and a52_cert["universal_f0_gauge_normalization_no_go_proved"],
        "tau_int_import_matches_log448_over15": abs(tau - tau_import) < 1e-15,
        "point_measure_is_positive": f0 > 0 and tau > 0,
        "point_measure_Hankel_positive_semidefinite": min(np.linalg.eigvalsh(hankel)) > -1e-12,
        "point_measure_Hankel_rank_one": int(np.linalg.matrix_rank(hankel, tol=1e-12)) == 1,
        "scalar_measure_leaves_sector_ratios_invariant": max(scalar_measure_ratio_residuals) < 1e-15,
        "rank_metric_not_exact_at_profile_scale": rank_metric_profile_log_residual > 1e-3,
        "rank_metric_not_exact_at_any_common_scale": best_rank_score > 1e-3,
        "profile_Kgauge_still_requires_two_source_ratios": len(profile_metric) - 1 == 2,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedProperTimeMeasureAndOverlapKineticMetricSourceOrStrictSpectralActionClosure.v1",
        "status": STATUS,
        "theorems": {
            "minimal_point_measure": {
                "proved_conditionally": all(checks[key] for key in ["tau_int_import_matches_log448_over15", "point_measure_is_positive", "point_measure_Hankel_positive_semidefinite", "point_measure_Hankel_rank_one"]),
                "premise": "adopt the zero-new-scale/minimal-support rule: the selected single proper-time value tau_int is represented by the unique one-atom positive measure",
                "statement": "Under the minimal-support premise, mu(t)=f0 delta(t-tau_int) gives f(x)=f0 exp(-tau_int x) and the exact moment sequence f2=f0/tau_int, f4=f0/tau_int^2. Its Hankel moment matrix is positive semidefinite of rank one.",
            },
            "scalar_measure_overlap_independence": {
                "proved": checks["scalar_measure_leaves_sector_ratios_invariant"],
                "statement": "Every scalar cutoff/proper-time measure multiplies all finite gauge traces by one common moment. It cannot change K1/K2 or K3/K2 and therefore cannot emit or repair the non-universal A52 gauge-overlap metric.",
            },
            "native_rank_metric_rejection": {
                "proved": checks["rank_metric_not_exact_at_any_common_scale"],
                "statement": "The simplest circle/lens/nil rank metric diag(2,1,1/3) is close but not exact. Optimizing the accepted one-loop running over 50 GeV to 1e19 GeV leaves a nonzero logarithmic residual, so rank counting alone is not the selected overlap source.",
            },
        },
        "proper_time_candidate": {
            "tau_int": tau,
            "tau_formula": "log(448)/15",
            "measure": "mu(t)=f0 delta(t-tau_int)",
            "cutoff_function": "f(x)=f0 exp(-tau_int x)",
            "moments": point_moments,
            "moment_Hankel_matrix": hankel.tolist(),
            "moment_Hankel_eigenvalues": np.linalg.eigvalsh(hankel).tolist(),
            "moment_Hankel_rank": int(np.linalg.matrix_rank(hankel, tol=1e-12)),
            "selected_by_existing_MTT_source": False,
            "why_not_selected": "tau_int is selected, but the global one-atom/minimal-support measure rule is not yet an MTT theorem; the earlier neutral packet explicitly treated point support as diagnostic",
        },
        "overlap_metric_tests": {
            "profile_Kgauge": profile_metric.tolist(),
            "native_rank_candidate": rank_metric.tolist(),
            "profile_log_residual": rank_metric_profile_log_residual,
            "best_common_scale_GeV": best_rank_scale,
            "metric_at_best_common_scale": best_rank_metric.tolist(),
            "best_log_residual": best_rank_score,
            "best_relative_component_residuals": ((best_rank_metric - rank_metric) / rank_metric).tolist(),
            "rank_candidate_accepted": False,
            "independent_source_ratios_remaining": 2,
        },
        "factorization_cutset": {
            "proper_time_role": "common scalar spectral moment and moment ratios",
            "overlap_role": "sector-relative gauge kinetic metric",
            "roles_are_mathematically_independent": True,
            "one_proper_time_measure_can_close_Kgauge": False,
            "strict_remaining_object": "source-derived K1/K2 and K3/K2 from the already selected literal HYM/bundle geometry at one declared scale",
        },
        "checks": checks,
        "epistemic_policy": {
            "point_measure_promoted_to_selected_MTT_theorem": False,
            "rank_near_hit_promoted": False,
            "profile_Kgauge_relabelled_as_prediction": False,
            "new_continuous_parameters": 0,
            "strict_spectral_action_closed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ProperTimeMeasureAndOverlapKineticMetricSource_or_StrictSpectralActionClosure_v1",
        "status": STATUS,
        "tau_int_exact_source_available": True,
        "minimal_point_measure_moments_closed_conditionally": packet["theorems"]["minimal_point_measure"]["proved_conditionally"],
        "point_measure_selected_by_MTT": False,
        "scalar_measure_cannot_source_overlap_ratios": packet["theorems"]["scalar_measure_overlap_independence"]["proved"],
        "native_rank_metric_rejected_as_exact_source": packet["theorems"]["native_rank_metric_rejection"]["proved"],
        "remaining_overlap_source_ratios": 2,
        "strict_spectral_action_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Proper-Time Measure and Overlap Kinetic Metric Source or Strict Spectral Action Closure v1

## Proper Time

The selected internal value is exact:

```text
tau_int = log(448)/15 = {tau:.16g}.
```

If one adds the zero-new-scale/minimal-support premise, the unique one-atom positive measure is
`mu(t)=f0 delta(t-tau_int)`, giving `f(x)=f0 exp(-tau_int x)` and

```text
f0 = {point_moments['f0']:.16g},
f2 = {point_moments['f2']:.16g},
f4 = {point_moments['f4']:.16g}.
```

Its moment Hankel matrix is positive semidefinite and rank one. This closes a conditional canonical
measure, not a selected MTT theorem: the corpus previously labels point support as diagnostic, and no
global minimal-support law has been derived.

## Why Proper Time Cannot Fix the Gauge Metric

A scalar cutoff measure contributes one common multiplier to every finite gauge trace. Therefore it
leaves `K1/K2` and `K3/K2` invariant. Proper-time selection and gauge-overlap selection are independent
problems; no choice of scalar `f` can turn the universal A51 metric into the A52 profile metric.

## Rank-Metric Test

The obvious zero-knob circle/lens/nil candidate is

```text
K_rank = diag(2,1,1/3).
```

It is close but not exact. Its best common-scale point is

```text
Q = {best_rank_scale:.12g} GeV,
K(Q) = ({best_rank_metric[0]:.12g}, 1, {best_rank_metric[2]:.12g}),
log residual = {best_rank_score:.12g}.
```

The two exact component conditions occur at different scales. Rank counting is therefore rejected as
the strict source rather than promoted from a near-hit.

## Remaining Object

The strict problem is now smaller than A52 stated: the proper-time candidate and its positive moments
are explicit under one named premise, while a scalar measure is proved irrelevant to relative gauge
normalization. The only numerical source object still missing is the pair `K1/K2`, `K3/K2` emitted
from the already selected literal HYM/bundle connections at one declared scale. The profile values remain
available, but they are not predictions.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
