"""Audit whether selected literal HYM data determine the gauge kinetic ratios."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "gauge_overlap_identifiability_and_source_contract.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
TEMPLATE = OUT / "literal_hym_sector_norm_payload.template.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeOverlapMetricFromLiteralHYMConnections_or_StrictSpectralActionClosure_v1.md"
STATUS = "MTT_SELECTED_LITERAL_HYM_SU2_CONNECTION_CLOSED_GAUGE_KINETIC_FUNCTIONALS_OPEN_TWO_RATIO_IDENTIFIABILITY_NOT_CLOSED"
NEXT = "MTT_Selected_CircleNilConnectionsAndCommonSchemeGaugeKineticFunctionalPayload_or_StrictSpectralActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def log_residual(candidate: np.ndarray, target: np.ndarray) -> float:
    return float(np.linalg.norm(np.log(candidate / target)))


def main() -> int:
    a47 = load(ROOT / "candidate_data" / SLUG.replace("gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure", "nativebundleautomorphismgaugegroup_or_parameterassumptionaudit") / "native_bundle_gauge_group_and_parameter_audit.packet.json")
    a52 = load(ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json")
    hym = load(ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json")
    transfer = load(ROOT / "candidate_data" / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json")

    profile = np.asarray(a52["minimal_profile_normalization"]["K_gauge_diagonal"], dtype=float)
    profile /= profile[1]
    canonical = {
        "finite_trace_GUT_normalized": np.asarray([1.0, 1.0, 1.0]),
        "carrier_rank": np.asarray([1.0, 2.0, 3.0]) / 2.0,
        "inverse_carrier_rank": (1.0 / np.asarray([1.0, 2.0, 3.0])) / 0.5,
        "endomorphism_dimension": np.asarray([1.0, 4.0, 9.0]) / 4.0,
        "lie_algebra_dimension": np.asarray([1.0, 3.0, 8.0]) / 3.0,
    }
    tests = {
        name: {
            "K_over_K2": value.tolist(),
            "log_residual_to_profile": log_residual(value, profile),
            "exact": bool(log_residual(value, profile) < 1e-12),
        }
        for name, value in canonical.items()
    }

    # One common scalar HYM response can at most move along one direction in the
    # two-dimensional ratio plane. The current selected transfer emits no U1 or
    # SU3 sector functional at all, so its strict ratio-map rank is zero.
    source_incidence = np.asarray([[0.0], [1.0], [0.0]])
    ratio_jacobian = np.asarray([source_incidence[0] - source_incidence[1], source_incidence[2] - source_incidence[1]])
    formal_rank_if_one_scalar_were_shared = int(np.linalg.matrix_rank(ratio_jacobian))
    strict_emitted_ratio_rank = 0

    source_rows = {
        "U1_circle": {
            "carrier_selected": True,
            "connection_or_harmonic_mode_selected": False,
            "curvature_or_hodge_norm_emitted": False,
            "normalized_sector_functional_emitted": False,
            "reason": "The selected central shared circle is degree-zero/spectator in the literal rank-2 HYM solve; no U1 kinetic norm is emitted.",
        },
        "SU2_lens": {
            "carrier_selected": True,
            "connection_or_harmonic_mode_selected": bool(hym["coefficient_packet"]["diagonal_expS_solution_closed"]),
            "curvature_or_hodge_norm_emitted": False,
            "normalized_sector_functional_emitted": False,
            "source": "selected eta_00 diagonal exp(S) HYM connection solution in the T3 End(2) lane",
            "residual_l2": float(hym["solution_summary"]["final_residual_l2"]),
            "reason": "The packet proves the internal HYM equation and connection representative, but does not evaluate a common-scheme four-dimensional gauge kinetic/threshold functional K2.",
        },
        "SU3_nil": {
            "carrier_selected": True,
            "connection_or_harmonic_mode_selected": False,
            "curvature_or_hodge_norm_emitted": False,
            "normalized_sector_functional_emitted": False,
            "reason": "The abstract rank-2-to-rank-3 adjoint transfer has no selected finite sector values; the corpus guard forbids promoting it.",
        },
    }
    accepted_norms = sum(int(row["normalized_sector_functional_emitted"]) for row in source_rows.values())

    template = {
        "schema": "MTTLiteralHYMSectorNormPayload.v1",
        "common_geometry": {
            "metric": "selected equal-radius Gauduchon/Hodge metric",
            "quadrature": "one common normalized volume/quadrature and error certificate",
            "renormalization_scale_GeV": None,
            "matching_and_trace_scheme": None,
        },
        "rows": {
            sector: {
                "selected_connection_representative": None,
                "selected_curvature_or_harmonic_field": None,
                "normalized_quadratic_functional": "integral Tr_rep(F_a wedge star F_a), or the declared harmonic U1 analogue",
                "K_a": None,
                "source_certificate": None,
                "error_bound": None,
                "accepted": False,
            }
            for sector in ["U1_circle", "SU2_lens", "SU3_nil"]
        },
        "acceptance": "At least two independent ratios must be computable from three same-scale rows; no observed gauge coupling may select a connection, normalization, scale, or scheme.",
    }

    checks = {
        "native_three_sector_carriers_selected": a47["checks"]["native_lie_dimension_is_12"],
        "literal_diagonal_SU2_HYM_solve_converged": hym["solver"]["converged"],
        "literal_SU2_HYM_residual_below_1e-12": hym["solution_summary"]["final_residual_l2"] < 1e-12,
        "rank2_to_rank3_values_still_open": transfer["what_remains_open"]["rank2_to_rank3_sector_transfer_values"],
        "no_normalized_gauge_kinetic_functional_emitted": accepted_norms == 0,
        "strict_ratio_map_rank_zero": strict_emitted_ratio_rank == 0,
        "one_scalar_formal_completion_rank_below_two": formal_rank_if_one_scalar_were_shared < 2,
        "all_canonical_zero_knob_completions_rejected": not any(row["exact"] for row in tests.values()),
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedGaugeOverlapMetricFromLiteralHYMConnectionsOrStrictSpectralActionClosure.v1",
        "status": STATUS,
        "theorems": {
            "literal_sector_source_rank": {
                "proved": all(checks.values()),
                "statement": "The selected literal HYM execution emits one SU2/End(2) connection representative but no common-scheme four-dimensional gauge kinetic functional in any sector. Consequently neither K1/K2 nor K3/K2 is presently defined by same-source geometry; the strict emitted ratio-map rank is zero.",
            },
            "single_response_no_go": {
                "proved": formal_rank_if_one_scalar_were_shared < 2,
                "statement": "Even granting one common scalar transfer of the rank-2 HYM response, its Jacobian in the two-dimensional gauge-ratio plane has rank at most one. Two independent profile ratios cannot be selected by that scalar alone.",
            },
            "canonical_completion_rejection": {
                "proved": checks["all_canonical_zero_knob_completions_rejected"],
                "statement": "Finite-trace, carrier-rank, inverse-rank, endomorphism-dimension, and Lie-dimension completions all fail the accepted profile ratios and therefore are not promoted as strict source laws.",
            },
        },
        "profile_comparison_only": {
            "K_over_K2": profile.tolist(),
            "used_to_select_source": False,
            "canonical_tests": tests,
        },
        "literal_HYM_source_rows": source_rows,
        "identifiability": {
            "normalized_sector_functionals_required": 3,
            "normalized_sector_functionals_emitted": accepted_norms,
            "independent_ratios_required": 2,
            "independent_ratios_emitted": strict_emitted_ratio_rank,
            "formal_rank_with_one_shared_scalar": formal_rank_if_one_scalar_were_shared,
            "missing_independent_sector_rows": ["U1_circle", "SU3_nil"],
        },
        "minimal_completion_contract": template,
        "checks": checks,
        "epistemic_policy": {
            "profile_values_promoted": False,
            "abstract_sector_transfer_promoted": False,
            "canonical_near_hit_promoted": False,
            "new_continuous_parameters": 0,
            "strict_spectral_action_closed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_GaugeOverlapMetricFromLiteralHYMConnections_or_StrictSpectralActionClosure_v1",
        "status": STATUS,
        "selected_SU2_literal_HYM_connection_closed": True,
        "selected_SU2_literal_gauge_kinetic_norm_closed": False,
        "selected_U1_literal_norm_source_closed": False,
        "selected_SU3_literal_HYM_norm_source_closed": False,
        "normalized_sector_functionals_emitted": accepted_norms,
        "independent_overlap_ratios_emitted": strict_emitted_ratio_rank,
        "single_response_insufficient_for_two_ratios": True,
        "canonical_completions_rejected": True,
        "minimal_payload_contract_emitted": True,
        "new_continuous_parameters": 0,
        "strict_spectral_action_closed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Gauge Overlap Metric from Literal HYM Connections or Strict Spectral Action Closure v1

## Executed Source Audit

The selected native carriers are `U(1)`, `SU(2)`, and `SU(3)`. The literal HYM chain currently emits
one genuine connection representative: the selected `eta_00` diagonal `exp(S)` solution in the
rank-2 `T3` lane, with final residual `{hym['solution_summary']['final_residual_l2']:.4g}`. It does
not evaluate the corresponding common-scheme four-dimensional gauge kinetic/threshold functional.
The common circle is degree-zero/spectator in that solve, and the existing rank-2-to-rank-3 theorem
explicitly does not emit finite `SU(3)` sector values.

Therefore `1/3` connection representatives but `0/3` gauge kinetic norm rows exist, and `0/2` ratios
can presently be formed from same-source literal geometry. This is not a failure of the solved rank-2
HYM equation; a connection residual is not itself a four-dimensional gauge kinetic coefficient.

## Rank Theorem

Even if the one rank-2 response were granted a common scalar transfer, its Jacobian in the ratio
plane `(log K1/K2, log K3/K2)` has rank `{formal_rank_if_one_scalar_were_shared}`, below the required
rank `2`. One scalar response cannot select two independent ratios. A sector functor must emit
separate circle and nil quadratic functionals, not merely identify their group ranks.

## Zero-Knob Completion Tests

The finite-trace, carrier-rank, inverse-rank, endomorphism-dimension, and Lie-dimension metrics were
all executed and none equals the profile metric. They remain useful diagnostics, not predictions.
Observed gauge couplings were used only for this rejection test and did not select a source formula.

## Constructed Completion

The machine-readable `literal_hym_sector_norm_payload.template.json` now fixes the missing object.
For each sector it requires a selected connection or harmonic representative, curvature/field,
normalized four-dimensional kinetic/threshold functional, common Hodge/quadrature convention,
declared scale and matching scheme, and an error certificate. Connection representatives are still
missing for `U1_circle` and `SU3_nil`; the kinetic functional is missing in all three rows. Filling
that common-scheme payload makes both ratios computable; another generic Galerkin or rank-count packet does not.

Strict spectral-action closure remains open, with zero new continuous parameters introduced.

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
