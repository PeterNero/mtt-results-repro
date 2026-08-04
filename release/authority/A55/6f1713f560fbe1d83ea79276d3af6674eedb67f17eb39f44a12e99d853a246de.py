"""Assemble and test the strongest common-scheme gauge kinetic payload candidate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
SLUG = "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "common_scheme_payload_search_and_finite_candidate.packet.json"
TEMPLATE = OUT / "gauge_inserted_heat_supertrace_payload.template.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonSchemeGaugeKineticPayloadSearch_or_FiniteProjectedThresholdCandidate_v1.md"
STATUS = "MTT_SELECTED_TREE_GAUGE_KINETIC_PAYLOAD_CLOSED_FINITE_THRESHOLD_COMPONENTS_FOUND_COMMON_SCHEME_SUPERTRACE_OPEN"
NEXT = "MTT_Selected_GaugeInsertedHeatSupertraceSecondVariation_or_CommonSchemeThresholdPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def best_common_anchor(initial_inv: np.ndarray, beta: np.ndarray, delta: np.ndarray, tmax: float) -> dict:
    center = np.eye(3) - np.ones((3, 3)) / 3.0
    x0 = center @ (initial_inv - delta)
    velocity = center @ (beta / (8.0 * math.pi**2))
    t = float(np.dot(velocity, x0) / np.dot(velocity, velocity))
    t = min(max(t, 0.0), tmax)
    shifted = initial_inv - beta * t / (8.0 * math.pi**2) - delta
    anchor = float(np.mean(shifted))
    return {"log_scale_ratio": t, "common_anchor": anchor, "residuals": (shifted - anchor).tolist(), "l2_residual": float(np.linalg.norm(shifted - anchor))}


def main() -> int:
    a54 = load(ROOT / "certificates" / "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure_certificate.json")
    a51 = load(ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure" / "finite_inner_fluctuation_and_spectral_traces.packet.json")
    a52 = load(ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json")
    pperp = load(QA / "candidate_data" / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json")
    quotient = load(QA / "candidate_data" / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json")
    factorized = load(QA / "candidate_data" / "selected_electroweak_u1y_factorized_threshold_operator_source_attempt.candidate.json")
    su2_gate = load(QA / "candidate_data" / "selected_electroweak_u1y_factorized_operator_or_su2_cancellation_gate.candidate.json")
    su3_bridge = load(QA / "candidate_data" / "internal_logdet_to_coupling_response_bridge.candidate.json")

    traces = a51["finite_spectral_traces"]["GUT_normalized_coefficients_three_families"]
    tree = np.asarray([traces["U1_GUT"], traces["SU2"], traces["SU3"]], dtype=float)
    gap = (2.0 * math.pi / 3.0) ** 2
    base_logdet = 4.0 * math.log(gap) + 4.0 * math.log(2.0 * gap)
    multiplicities = np.asarray([2.0, 2.0, 3.0])
    finite_candidate = multiplicities * base_logdet

    run = a52["universal_gauge_relation_test"]
    scale0 = float(run["source_scale_GeV"])
    couplings = np.asarray(run["source_couplings_g1GUT_g2_g3"], dtype=float)
    beta = np.asarray(run["one_loop_beta_coefficients"], dtype=float)
    initial_inv = 1.0 / couplings**2
    tmax = math.log(1e19 / scale0)
    response_tests = {}
    for sign in (1.0, -1.0):
        delta = sign * finite_candidate / (8.0 * math.pi**2)
        result = best_common_anchor(initial_inv, beta, delta, tmax)
        result["best_scale_GeV"] = scale0 * math.exp(result["log_scale_ratio"])
        result["delta_inverse_coupling"] = delta.tolist()
        response_tests[f"carrier_supertrace_sign_{int(sign):+d}"] = result
    for sign in (1.0, -1.0):
        delta = sign * beta * base_logdet / (8.0 * math.pi**2)
        result = best_common_anchor(initial_inv, beta, delta, tmax)
        result["best_scale_GeV"] = scale0 * math.exp(result["log_scale_ratio"])
        result["delta_inverse_coupling"] = delta.tolist()
        response_tests[f"SM_beta_supertrace_sign_{int(sign):+d}"] = result

    t12 = float((initial_inv[0] - initial_inv[1]) * 8.0 * math.pi**2 / (beta[0] - beta[1]))
    inv12 = initial_inv - beta * t12 / (8.0 * math.pi**2)
    chi_required = float((inv12[2] - inv12[1]) / base_logdet)
    canonical_chi = 1.0 / (8.0 * math.pi**2)

    template = {
        "schema": "MTTGaugeInsertedHeatSupertracePayload.v1",
        "common_operator": {
            "finite_or_smooth_operator_id": None,
            "selected_domain_and_zero_mode_projector": None,
            "regularization_and_subtraction": None,
            "matching_scale_GeV": None,
            "renormalization_scheme": None,
        },
        "sector_rows": {
            sector: {
                "generator_insertion_Ta": None,
                "quadratic_index_Tr_Ta2": None,
                "graded_heat_trace_or_second_variation": None,
                "finite_part_Delta_a": None,
                "error_certificate": None,
                "source_certificate": None,
                "accepted": False,
            }
            for sector in ["U1_GUT", "SU2", "SU3"]
        },
        "required_identity": "Delta_a = FP_{t or s} Str(T_a^2 exp(-t D_source^2)), equivalently the gauge-field second variation of one selected regularized effective action",
        "acceptance": "All three rows must use the same D_source, grading, trace, zero-mode policy, regulator, scale and scheme. Profile couplings may only be downstream tests.",
    }

    checks = {
        "A54_payload_contract_available": a54["minimal_payload_contract_emitted"],
        "tree_level_GUT_normalized_trace_payload_exact": bool(np.allclose(tree, [6.0, 6.0, 6.0], atol=0.0, rtol=0.0)),
        "selected_U1_shared_circle_projector_closed": pperp["decision"]["selected_U1_SU2_threshold_index_pair_closed"],
        "quotient_determinant_lemma_exact": quotient["decision"]["algebraic_quotient_determinant_lemma_proved"] and abs(quotient["decision"]["quotient_logdet"] - 2.0 * base_logdet) < 1e-12,
        "factorized_matrix_same_branch_but_not_source_emitted": factorized["source_identity"]["same_source_as_27mode_DE_gap_layer"] and not factorized["decision"]["selected_source_emission_closed"],
        "SU2_scoped_weak_split_cancellation_closed": su2_gate["decision"]["SU2_same_scheme_row_or_cancellation_closed_for_weaksplit"],
        "SU3_internal_logdet_bridge_closed_physical_response_open": su3_bridge["decision"]["internal_unit_response_bridge"] == "CLOSED_LOG_2008" and "OPEN" in su3_bridge["decision"]["physical_coupling_bridge"],
        "finite_carrier_candidate_not_exact_with_canonical_response": all(row["l2_residual"] > 1e-3 for row in response_tests.values()),
        "required_response_not_canonical_unit_coefficient": abs(abs(chi_required) / canonical_chi - 1.0) > 1e-3,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedCommonSchemeGaugeKineticPayloadSearchOrFiniteProjectedThresholdCandidate.v1",
        "status": STATUS,
        "theorems": {
            "tree_level_payload": {
                "proved": checks["tree_level_GUT_normalized_trace_payload_exact"],
                "statement": "The completed finite real-even SM triple emits the exact common-scheme tree-level GUT-normalized gauge trace payload (6,6,6). This is a genuine gauge kinetic source row, but it is universal and A52 proves it cannot by itself match all running couplings.",
            },
            "finite_projected_candidate": {
                "proved_conditionally": True,
                "premise": "the same selected scalar F3xF3 base operator factorizes over the physical carrier flag with post-shared-circle multiplicities (2,2,3)",
                "statement": "Under the factorization premise, the positive determinant vector is exactly L*(2,2,3), where L=4 log((2pi/3)^2)+4 log(2(2pi/3)^2). The U1 quotient row agrees with the independently proved Pperp quotient determinant.",
            },
            "canonical_response_rejection": {
                "proved": checks["finite_carrier_candidate_not_exact_with_canonical_response"],
                "statement": "Neither sign of the canonical 1/(8pi^2) carrier response, nor either sign of the SM-beta weighted response, produces exact common-anchor matching at any one-loop scale. The finite determinant spectrum alone is not the gauge kinetic payload.",
            },
            "common_scheme_obstruction": {
                "proved": True,
                "statement": "The exact U1 quotient determinant, scoped SU2 cancellation, and SU3 log(2008) payload cannot be combined because they are not three rows of one gauge-inserted effective action with one trace, regulator, domain, scale and scheme.",
            },
        },
        "accepted_tree_level_payload": {
            "sector_order": ["U1_GUT", "SU2", "SU3"],
            "trace_coefficients": tree.tolist(),
            "same_scheme": True,
            "source_derived": True,
            "new_continuous_parameters": 0,
        },
        "found_threshold_components": {
            "U1": {"Pperp_index": "2/3", "conditional_quotient_logdet": 2.0 * base_logdet, "source_emitted_as_gauge_threshold": False},
            "SU2": {"scoped_flat_FP_weak_split_cancellation": True, "absolute_same_action_finite_part": None},
            "SU3": {"internal_logdet": math.log(2008.0), "physical_response_chi_SU3": None},
            "three_rows_same_scheme": False,
        },
        "finite_projected_candidate": {
            "base_positive_spectrum": [{"eigenvalue": gap, "multiplicity": 4}, {"eigenvalue": 2.0 * gap, "multiplicity": 4}],
            "base_logdet_L": base_logdet,
            "post_shared_circle_carrier_multiplicities": multiplicities.tolist(),
            "conditional_logdet_vector": finite_candidate.tolist(),
            "source_factorization_selected": False,
            "canonical_response_tests": response_tests,
            "g1_equals_g2_scale_GeV": scale0 * math.exp(t12),
            "required_chi_for_SU3_offset_at_that_scale": chi_required,
            "canonical_chi_1_over_8pi2": canonical_chi,
            "required_over_canonical": chi_required / canonical_chi,
        },
        "minimal_missing_object": template,
        "external_primary_inspiration": [
            {"url": "https://arxiv.org/abs/1611.09442", "use": "heterotic flux thresholds are BPS-state sums depending on bundle topological data; no universal determinant multiplier may be assumed"},
            {"url": "https://arxiv.org/abs/1210.5566", "use": "torsional heterotic thresholds require model-specific regularized localized and bulk contributions"},
        ],
        "checks": checks,
        "epistemic_policy": {"profile_values_used_as_selector": False, "conditional_factorization_promoted": False, "mixed_scheme_components_combined": False, "new_continuous_parameters": 0, "strict_spectral_action_closed": False},
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_CommonSchemeGaugeKineticPayloadSearch_or_FiniteProjectedThresholdCandidate_v1",
        "status": STATUS,
        "tree_level_common_scheme_rows_closed": 3,
        "threshold_common_scheme_rows_closed": 0,
        "finite_projected_candidate_computed": True,
        "finite_projected_candidate_source_selected": False,
        "canonical_response_candidates_rejected": True,
        "gauge_inserted_heat_supertrace_template_emitted": True,
        "new_continuous_parameters": 0,
        "strict_spectral_action_closed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Common-Scheme Gauge Kinetic Payload Search or Finite Projected Threshold Candidate v1

## Payload Found

The exact tree-level gauge kinetic payload was already present but had not been separated from the
threshold search. The completed finite triple gives, in `(U1_GUT,SU2,SU3)` order,

```text
Tr_F(T_a^2) = (6,6,6).
```

These are three accepted same-scheme source rows with zero new parameters. They prove universal
tree-level normalization, not the observed non-universal low-energy couplings.

## Finite Projected Candidate

The selected 27-mode base spectrum gives one-copy

```text
L = 4 log((2*pi/3)^2) + 4 log(2*(2*pi/3)^2) = {base_logdet:.15g}.
```

If that same base operator factorizes over the physical circle/lens/nil carrier flag, quotienting the
shared circle gives multiplicities `(2,2,3)` and determinant vector

```text
({finite_candidate[0]:.15g}, {finite_candidate[1]:.15g}, {finite_candidate[2]:.15g}).
```

Its U1 entry exactly reproduces the independently proved `P_perp` quotient determinant. The premise
that one selected gauge threshold operator emits the full factorized vector is still open.

## Numerical Test

The clean candidate does not become exact under either sign of the canonical `1/(8*pi^2)` response,
nor under SM-beta supertrace weighting, at any common one-loop scale. At the unique scale
`Q={scale0 * math.exp(t12):.12g} GeV` where `g1_GUT=g2`, the required SU3 response is

```text
chi_required = {chi_required:.15g}
chi_required / (1/(8*pi^2)) = {chi_required / canonical_chi:.15g}.
```

Thus the determinant spectrum is not by itself a physical gauge kinetic payload. Its sign and weight
must come from the gauge-field second variation or graded representation supertrace.

## Exact Remaining Object

The repository has an exact U1 quotient determinant, a scoped SU2 flat-FP cancellation, and exact
SU3 internal `log(2008)`, but they use different domains or response conventions and cannot be added.
The emitted template requires the missing common operation

```text
Delta_a = FP Str(T_a^2 exp(-t D_source^2)),
```

equivalently the second variation of one selected regularized action with respect to all three gauge
fields. One operator, grading, trace, zero-mode policy, regulator, scale and scheme must generate all
three rows. Heterotic threshold literature confirms these weights are model-specific BPS/bundle data,
not a universal multiplier: https://arxiv.org/abs/1611.09442 and https://arxiv.org/abs/1210.5566.

Next artifact: `{NEXT}`.
"""

    dump(TEMPLATE, template)
    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
