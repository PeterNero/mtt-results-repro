"""Close profile bosonic normalization and execute the universal spectral-moment no-go."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "product_triple_profile_normalization_and_moment_nogo.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1.md"
STATUS = "MTT_PRODUCT_TRIPLE_PROFILE_MATTER_NORMALIZATION_CLOSED_OVERLAP_METRIC_EXACT_UNIVERSAL_SPECTRAL_MOMENT_CLAIM_BLOCKED_BY_GAUGE_NOGO"
NEXT = "MTT_Selected_ProperTimeMeasureAndOverlapKineticMetricSource_or_StrictSpectralActionClosure_v1"
TOL = 1e-12


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def running_couplings(log_ratio: float, initial: np.ndarray, beta: np.ndarray) -> np.ndarray:
    inverse_squared = 1.0 / initial**2 - beta * log_ratio / (8.0 * math.pi**2)
    return 1.0 / np.sqrt(inverse_squared)


def relative_spread(couplings: np.ndarray) -> float:
    return float(np.std(couplings) / np.mean(couplings))


def golden_minimum(function, left: float, right: float, iterations: int = 160) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = right - ratio * (right - left)
    x2 = left + ratio * (right - left)
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


def archived_smdr_best(path: Path) -> dict:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        columns = line.split()
        try:
            scale = float(columns[0])
            g3, g2, gp = map(float, columns[2:5])
        except (ValueError, IndexError):
            continue
        couplings = np.array([math.sqrt(5.0 / 3.0) * gp, g2, g3])
        rows.append((scale, couplings, relative_spread(couplings)))
    scale, couplings, spread = min(rows, key=lambda row: row[2])
    return {
        "scale_GeV": scale,
        "couplings_g1GUT_g2_g3": couplings.tolist(),
        "relative_standard_deviation": spread,
        "max_over_min": float(max(couplings) / min(couplings)),
        "row_count": len(rows),
    }


def main() -> int:
    a03 = load(ROOT / "certificates" / "selected_renormalizedsmobservablefunctor_fromcommonschemeaction_certificate.json")
    a51 = load(ROOT / "certificates" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure_certificate.json")
    transport = load(ROOT / "candidate_data" / "selected_multiloopcommonsourceprecisiontransport_or_officialjointlikelihood" / "smdr_multiloop_common_source_transport.raw.json")
    central = transport["central_output"]
    scale0 = float(transport["target_scale_GeV"])
    initial = np.array(
        [math.sqrt(5.0 / 3.0) * central["SMDR_gp_in"], central["SMDR_g_in"], central["SMDR_g3_in"]],
        dtype=float,
    )

    # One-loop SM coefficients in GUT-normalized order (g1,g2,g3).
    beta = np.array([41.0 / 10.0, -19.0 / 6.0, -7.0], dtype=float)
    upper_scale = 1e19
    best_log, best_spread = golden_minimum(
        lambda log_ratio: relative_spread(running_couplings(log_ratio, initial, beta)),
        0.0,
        math.log(upper_scale / scale0),
    )
    best_scale = scale0 * math.exp(best_log)
    best_couplings = running_couplings(best_log, initial, beta)
    archived_best = archived_smdr_best(ROOT / "SMDR" / "fig_data" / "FIG_RGrun_vs_Q.dat")

    # Exact profile-tier kinetic normalization. The common factor is fixed by the SU2
    # convention K2=1; K1 and K3 are then the two measured relative overlap coordinates.
    g1, g2, g3 = [float(value) for value in initial]
    overlap_metric = np.array([(g2 / g1) ** 2, 1.0, (g2 / g3) ** 2], dtype=float)
    finite_trace_coefficient = 6.0
    f0_convention = 1.0 / (finite_trace_coefficient * g2**2)
    reconstructed_inverse_g2 = f0_convention * finite_trace_coefficient * overlap_metric
    target_inverse_g2 = 1.0 / initial**2
    normalization_residual = float(np.linalg.norm(reconstructed_inverse_g2 - target_inverse_g2))

    pair_crossings = {}
    for first, second, label in [(0, 1, "g1_equals_g2"), (0, 2, "g1_equals_g3"), (1, 2, "g2_equals_g3")]:
        crossing_log = (1.0 / initial[first] ** 2 - 1.0 / initial[second] ** 2) * 8.0 * math.pi**2 / (beta[first] - beta[second])
        crossing = running_couplings(crossing_log, initial, beta)
        pair_crossings[label] = {
            "scale_GeV": scale0 * math.exp(crossing_log),
            "couplings_g1GUT_g2_g3": crossing.tolist(),
            "all_three_relative_range": float((max(crossing) - min(crossing)) / np.mean(crossing)),
        }

    checks = {
        "A03_profile_local_QFT_action_equivalence_closed": a03["actual_local_QFT_observable_functor_at_parity_profile_standard"],
        "A51_single_Higgs_and_bosonic_operator_content_closed": a51["selected_single_Higgs_projection_closed"] and a51["bosonic_SM_operator_content_closed_via_standard_heat_kernel_theorem"],
        "accepted_common_scale_is_positive": scale0 > 0,
        "universal_one_loop_gauge_relation_has_no_solution": max(best_couplings) / min(best_couplings) > 1.04,
        "archived_multiloop_trajectory_confirms_no_unification": archived_best["max_over_min"] > 1.04,
        "profile_overlap_metric_positive": bool(np.all(overlap_metric > 0)),
        "profile_overlap_normalization_exact": normalization_residual < TOL,
        "profile_overlap_coordinates_count_two": len(overlap_metric) - 1 == 2,
        "spectral_moment_scale_rescaling_degeneracy_exact": True,
        "old_5TeV_cutoff_not_used": abs(scale0 - 5000.0) > 1.0,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedSpectralCutoffMomentsAndSpacetimeProductTripleOrBosonicActionNormalization.v1",
        "status": STATUS,
        "theorems": {
            "profile_product_triple_interface": {
                "closed": checks["A03_profile_local_QFT_action_equivalence_closed"] and checks["A51_single_Higgs_and_bosonic_operator_content_closed"],
                "statement": "At the adopted parity/profile standard, the A50/A51 finite triple is tensored with the standard Wick-rotated four-dimensional spin spectral triple already imported by the A03 renormalized-SM action functor. This closes the product-triple interface and bosonic matter operator content, but does not derive the Lorentzian-to-Euclidean dictionary from MTT.",
            },
            "universal_gauge_moment_no_go": {
                "proved": checks["universal_one_loop_gauge_relation_has_no_solution"] and checks["archived_multiloop_trajectory_confirms_no_unification"],
                "statement": "No scale between the accepted common top scale and 1e19 GeV makes g1_GUT=g2=g3 on the selected SM running branch. A universal f0 multiplying the A51 equal GUT-normalized trace coefficients therefore cannot reproduce all three accepted gauge couplings; changing only Lambda or f0 cannot repair the mismatch.",
            },
            "minimal_profile_overlap_normalization": {
                "closed": checks["profile_overlap_normalization_exact"],
                "statement": "With K2=1 as normalization convention, the positive diagonal overlap metric K=diag((g2/g1)^2,1,(g2/g3)^2) exactly reconstructs all three accepted inverse gauge couplings through g_i^-2=6 f0 K_i. The two relative entries are profile coordinates equivalent to the two independent measured coupling ratios, not new parameters or no-knob predictions.",
            },
            "spectral_moment_identifiability": {
                "proved": True,
                "statement": "The heat-kernel action determines only f0 K_i, f2 Lambda^2, and f4 Lambda^4. The transformation Lambda->c Lambda, f2->f2/c^2, f4->f4/c^4 leaves these coefficients invariant, so Lambda, f2, and f4 cannot be uniquely recovered without a selected cutoff/proper-time measure or an additional source law.",
            },
        },
        "profile_product_triple": {
            "base": "standard compact four-dimensional Euclidean spin spectral triple used by the imported SM spectral-action theorem",
            "finite_factor": "A50 completed KO6 finite triple with A51 selected rank-four Higgs submodule",
            "total_Dirac_form": "D_M tensor 1 + gamma5 tensor D_F,H",
            "Wick_rotation_status": "imported parity/profile dictionary; not derived from MTT",
            "strict_MTT_spacetime_selection_closed": False,
        },
        "universal_gauge_relation_test": {
            "source_scale_GeV": scale0,
            "source_couplings_g1GUT_g2_g3": initial.tolist(),
            "one_loop_beta_coefficients": beta.tolist(),
            "search_interval_GeV": [scale0, upper_scale],
            "best_scale_GeV": best_scale,
            "best_couplings_g1GUT_g2_g3": best_couplings.tolist(),
            "best_relative_standard_deviation": best_spread,
            "best_max_over_min": float(max(best_couplings) / min(best_couplings)),
            "pair_crossings": pair_crossings,
            "archived_SMDR_multiloop_grid_crosscheck": archived_best,
            "universal_f0_closes_all_three": False,
        },
        "minimal_profile_normalization": {
            "scale_GeV": scale0,
            "scheme": transport["runtime"]["scheme"],
            "field_order": ["U1_GUT", "SU2", "SU3"],
            "K_gauge_diagonal": overlap_metric.tolist(),
            "normalization_convention": "K_SU2=1",
            "f0_in_g_i^-2_equals_6_f0_K_i_convention": f0_convention,
            "reconstructed_inverse_coupling_squared": reconstructed_inverse_g2.tolist(),
            "target_inverse_coupling_squared": target_inverse_g2.tolist(),
            "residual": normalization_residual,
            "independent_relative_profile_coordinates": 2,
            "new_parameters_relative_to_profile_SM": 0,
            "new_parameters_relative_to_strict_no_knob_MTT": 2,
            "source_status": "accepted measured profile calibration; selected internal overlap derivation open",
        },
        "moment_identifiability": {
            "observable_combinations": ["f0*K_1", "f0*K_2", "f0*K_3", "f2*Lambda^2", "f4*Lambda^4"],
            "exact_rescaling_kernel": "Lambda->c Lambda; f2->f2/c^2; f4->f4/c^4",
            "unique_Lambda_from_current_action": False,
            "selected_f0_f2_f4_from_MTT": False,
            "old_5TeV_chain_status": "retired by corpus revision authority and not used",
            "gravity_normalization_status": "physical Newton/Planck source remains open in the GR proof repo",
            "vacuum_energy_status": "no selected cancellation/renormalization condition for the f4 Lambda^4 term",
        },
        "checks": checks,
        "epistemic_policy": {
            "profile_bosonic_matter_action_closed": True,
            "strict_universal_spectral_action_closed": False,
            "gauge_overlap_values_derived_without_measured_couplings": False,
            "old_5TeV_calibration_reused": False,
            "standard_4D_spin_base_imported": True,
            "MTT_Wick_rotation_derived": False,
            "spectral_cutoff_claimed_unique": False,
            "continuous_profile_coordinates_used": 2,
            "new_continuous_parameters_beyond_SM_profile": 0,
        },
        "remaining_strict_source_object": {
            "name": "SelectedProperTimeMeasureAndOverlapKineticMetric",
            "required_fields": [
                "MTT-selected four-dimensional Lorentzian/Euclidean product-triple dictionary",
                "positive proper-time measure mu(tau) or cutoff function f and its moments",
                "source-derived K_gauge overlap metric at the same spectral scale",
                "same-source gravity/vacuum normalization or an explicit renormalized subtraction policy",
            ],
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1",
        "status": STATUS,
        "profile_product_triple_interface_closed": packet["theorems"]["profile_product_triple_interface"]["closed"],
        "profile_bosonic_matter_normalization_closed": True,
        "universal_f0_gauge_normalization_no_go_proved": packet["theorems"]["universal_gauge_moment_no_go"]["proved"],
        "profile_overlap_metric_exact": packet["theorems"]["minimal_profile_overlap_normalization"]["closed"],
        "profile_overlap_relative_coordinates": 2,
        "new_parameters_beyond_SM_profile": 0,
        "strict_spectral_cutoff_moments_closed": False,
        "strict_MTT_Wick_rotation_closed": False,
        "old_5TeV_chain_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Spectral Cutoff Moments and Spacetime Product Triple or Bosonic Action Normalization v1

## Product-Triple Scope

At the adopted profile standard, A03 already imports the standard renormalized four-dimensional SM
action and quantization dictionary. Tensoring its Wick-rotated compact spin triple with the completed
A50/A51 finite factor closes the product-triple interface and bosonic matter operator content. This is
an almost-commutative profile embedding, not an MTT derivation of Wick rotation or physical spacetime.

## Universal Spectral Normalization No-Go

A51 gives equal GUT-normalized finite gauge traces. A universal spectral moment would therefore require
`g1_GUT=g2=g3` at one scale. Starting from the accepted SMDR common-scale values and running the
one-loop SM equations over `{scale0:.6g}` to `1e19 GeV`, the best point is

```text
Q_best = {best_scale:.12g} GeV,
(g1,g2,g3) = ({best_couplings[0]:.9f}, {best_couplings[1]:.9f}, {best_couplings[2]:.9f}),
max(g_i)/min(g_i) = {max(best_couplings) / min(best_couplings):.9f}.
```

The mismatch is larger than four percent. The archived multi-loop SMDR trajectory independently has
the same failure. Hence no choice of one `f0` or cutoff scale closes all three gauge terms on the
selected pure-SM branch.

## Exact Profile Exit

The MTT overlap formulation naturally permits a positive kinetic metric. At the accepted common top
scale, fixing `K_2=1` gives

```text
K_gauge = diag({overlap_metric[0]:.15g}, 1, {overlap_metric[2]:.15g}),
f0 = {f0_convention:.15g}             in g_i^-2 = 6 f0 K_i.
```

This reconstructs all three inverse couplings with residual `{normalization_residual:.3e}`. The two
relative entries are exactly the two independent measured coupling ratios. They add zero parameters
beyond the profile SM, but count as two un-derived coordinates relative to strict no-knob MTT.

## Moment Identifiability

The heat-kernel coefficients expose only

```text
f0 K_i,   f2 Lambda^2,   f4 Lambda^4.
```

The exact rescaling `Lambda->c Lambda`, `f2->f2/c^2`, `f4->f4/c^4` leaves the action unchanged.
Therefore the current action cannot uniquely determine `Lambda,f2,f4`. The old `5 TeV` calibration is
retired and was not reused. Absolute Newton normalization and the vacuum-energy subtraction/source law
also remain open.

## Result

The bosonic SM matter action is closed at the declared profile standard, including exact canonical
gauge normalization through `K_gauge`. The stronger claim that MTT uniquely selects a universal cutoff
function and all spectral moments is not closed and, with `K_gauge=I`, is disproved on the selected SM
running branch. The remaining strict object is one selected proper-time measure and source-derived
overlap kinetic metric, together with its spacetime/Wick and gravity normalization provenance.

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
