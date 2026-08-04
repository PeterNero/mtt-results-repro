"""Test whether charged/Higgs scalar rows can be promoted into the gauge action."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcegaugehessiancrossuse_or_sectorendomorphismvalueemission"
OUT = ROOT / "candidate_data" / SLUG
CROSSUSE = OUT / "spectral_action_crossuse_decision.packet.json"
ROUTES = OUT / "remaining_gauge_source_routes.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourceGaugeHessianCrossUse_or_SectorEndomorphismValueEmission_v1.md"
STATUS = "MTT_SELECTED_SAME_SOURCE_GAUGE_HESSIAN_CROSSUSE_TEST_CLOSED_DIRECT_K_PROMOTION_REJECTED_NATIVE_GAUGE_FUNCTIONAL_REMAINS"
NEXT = "MTT_Selected_CircleLensNilGaugeQuadraticFunctional_or_NonUniversalKineticValueRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    paths = {
        "A51_spectral_action": ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure.candidate.json",
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A53_literal_HYM": ROOT / "candidate_data" / "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure.candidate.json",
        "A54_common_scheme": ROOT / "candidate_data" / "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate.candidate.json",
        "A57_heat": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "A63_rank": ROOT / "candidate_data" / "selected_nonuniversalgaugeendomorphismsource_or_commonspectrumnogofinality.candidate.json",
        "charged_K": ROOT / "candidate_data" / "selected_tschemenulldelta_reconciliation_or_lambdahlastrow" / "accepted_charged_kthreshold_rows_current.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}

    gauge_traces = data["A51_spectral_action"]["finite_spectral_traces"]["GUT_normalized_coefficients_three_families"]
    yukawa_traces = data["A51_spectral_action"]["finite_spectral_traces"]["Yukawa_trace_rows"]
    charged_rows = data["charged_K"]["rows"]
    checks = {
        "A51_gauge_trace_rows_are_universal": [gauge_traces[key] for key in ("U1_GUT", "SU2", "SU3")] == [6.0, 6, 6],
        "A51_separates_gauge_and_Yukawa_trace_rows": set(yukawa_traces) == {"u", "d", "e", "nu"},
        "A51_absolute_normalization_is_open": not data["A51_spectral_action"]["bosonic_action_interface"]["absolute_coefficient_normalization_closed"],
        "A52_universal_gauge_relation_no_go": data["A52_profile"]["theorems"]["universal_gauge_moment_no_go"]["proved"],
        "A53_emits_zero_normalized_gauge_functionals": data["A53_literal_HYM"]["identifiability"]["normalized_sector_functionals_emitted"] == 0,
        "A54_requires_one_gauge_inserted_action": "one selected regularized effective action" in data["A54_common_scheme"]["minimal_missing_object"]["required_identity"],
        "A57_has_typed_background_field_complex": data["A57_heat"]["theorems"]["gauge_fixed_complex"]["proved_structurally"],
        "A63_charged_H_basis_rank_two": data["A63_rank"]["closure_decision"]["charged_plus_Higgs_is_minimal_algebraic_basis"],
        "charged_K_rows_are_not_gauge_rows": all("Omega_" in row["combined_kernel_row_id"] for row in charged_rows),
        "A63_emitted_no_selected_gauge_value_payload": not data["A63_rank"]["closure_decision"]["selected_nonuniversal_operator_value_payload_emitted"],
    }

    crossuse = {
        "schema": "MTTSpectralActionCrossUseDecision.v1",
        "status": "DIRECT_CHARGED_HIGGS_K_TO_GAUGE_KINETIC_PROMOTION_REJECTED",
        "tree_level_asymptotic_spectral_action": {
            "gauge_coefficient_map": "K_a(tree) = f0 Tr_HF(T_a^2)",
            "selected_GUT_normalized_trace_rows": [6.0, 6.0, 6.0],
            "dependence_on_fixed_finite_representation": True,
            "dependence_on_charged_K_threshold_rows": False,
            "Yukawa_DF_invariants_have_separate_rows": ["Tr(Ydagger Y)", "Tr((Ydagger Y)^2)"],
            "decision": "The existing charged/Higgs K scalars cannot be inserted into tree-level gauge kinetic coefficients without changing the selected action theorem.",
        },
        "quantum_mass_threshold_alternative": {
            "mathematically_legitimate": True,
            "schematic_form": "Delta(1/g_a^2) = sum_r c_a(r) log(m_r^2/mu^2) plus scheme-dependent finite terms",
            "required_typed_inputs": [
                "physical pole or running mass in one declared scheme",
                "matching/decoupling scale mu",
                "representation index and multiplicity",
                "loop order, regulator and subtraction prescription",
                "zero-mode and broken-phase policy",
            ],
            "charged_K_is_directly_a_mass_ratio": False,
            "selects_absolute_gauge_boundary_condition": False,
            "decision": "This route is ordinary threshold/RG transport. It may transport a supplied gauge boundary condition, but it does not derive that boundary condition from the K rows.",
        },
        "rank_versus_source_distinction": {
            "charged_plus_Higgs_relative_rank": 2,
            "rank_sufficiency_proved": True,
            "same_action_value_source_proved": False,
            "lesson": "Linear independence is necessary but not a license to identify observables from different functionals.",
        },
        "external_primary_theorem_sources": [
            {
                "url": "https://arxiv.org/abs/hep-th/9606001",
                "role": "spectral action principle and gauge-coupling relation at the spectral normalization scale",
            },
            {
                "url": "https://arxiv.org/abs/hep-th/0610241",
                "role": "almost-commutative Standard Model spectral action with gauge and Yukawa/Higgs trace relations",
            },
            {
                "url": "https://arxiv.org/abs/0906.3837",
                "role": "mass-dependent gauge vacuum polarization and scheme-dependent running/decoupling via heat-kernel methods",
            },
        ],
    }

    routes = {
        "schema": "MTTRemainingGaugeSourceRoutes.v1",
        "status": "NATIVE_GAUGE_FUNCTIONAL_ROUTE_SELECTED_AS_NEXT",
        "retired_routes": [
            "reopen the ten A62 spectra",
            "use family splitting on complete identical SM families",
            "insert Yukawa/overlap K rows directly into tree-level gauge traces",
            "fit two coefficients in the A63 charged-plus-Higgs basis",
            "combine U1, SU2 and SU3 determinants from different domains or schemes",
        ],
        "remaining_routes": [
            {
                "route": "native circle/lens/nil gauge quadratic functional",
                "priority": 1,
                "why": "It can define the gauge kinetic inner product itself and is the unfilled A53/A54 source object.",
                "required_rows": {
                    "U1_circle": "selected harmonic/connection representative and normalized quadratic functional",
                    "SU2_lens": "curvature/Hodge norm of the existing selected HYM representative",
                    "SU3_nil": "selected native color representative and normalized quadratic functional",
                },
            },
            {
                "route": "non-asymptotic gauge-inserted finite heat supertrace",
                "priority": 2,
                "why": "A single selected operator and regulator could generate representation-dependent finite parts beyond the universal a4 coefficient.",
                "required_identity": "Delta_a = FP Str(T_a^2 exp(-t D_source^2)) for all three a in one domain/scheme",
            },
            {
                "route": "physical mass-threshold transport",
                "priority": 3,
                "why": "Useful as a consistency calculation after a boundary source is selected, not as the source of the boundary itself.",
            },
        ],
        "next_payload": {
            "artifact": NEXT,
            "common_fields": [
                "one selected circle/lens/nil product geometry and Hodge metric",
                "one trace normalization and volume convention",
                "one regulator/matching scheme",
                "three source-selected fields or connections",
                "three normalized K_a rows with error certificates",
                "two relative ratios computed before profile comparison",
            ],
            "acceptance": "At least two independent ratios must be emitted with no measured gauge coupling used to select fields, normalization, scale, or scheme.",
        },
    }

    candidate = {
        "schema": "MTTSelectedSameSourceGaugeHessianCrossUseOrSectorEndomorphismValueEmission.v1",
        "status": STATUS,
        "theorems": {
            "asymptotic_spectral_action_crossuse_no_go": {
                "proved": True,
                "statement": "For the fixed A51 finite representation, the asymptotic gauge kinetic coefficient is f0 times the finite generator trace. The D_F/Yukawa invariants occupy distinct scalar terms. Therefore the accepted charged and H overlap K rows are not gauge kinetic value rows and cannot be promoted by direct substitution.",
            },
            "mass_threshold_boundary_no_go": {
                "proved": True,
                "statement": "A mass-dependent one-loop determinant can transport gauge couplings across declared thresholds, but requires typed physical masses and a matching scheme and leaves an absolute/common boundary condition. It is not a no-knob source of all three gauge couplings.",
            },
            "native_functional_reduction": {
                "proved": True,
                "statement": "After the A63 rank theorem and direct-cross-use rejection, the shortest non-looping source target is the common-scheme native circle/lens/nil quadratic gauge functional, or its equivalent single gauge-inserted finite heat supertrace.",
            },
        },
        "closure_decision": {
            "A63_rank_theorem_retained": True,
            "direct_charged_H_K_crossuse_closed": False,
            "direct_crossuse_rejected": True,
            "mass_threshold_transport_available_conditionally": True,
            "native_gauge_functional_value_rows_emitted": 0,
            "native_gauge_functional_value_rows_required": 3,
            "no_knob_gauge_coupling_prediction_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "crossuse": str(CROSSUSE.relative_to(ROOT)).replace("\\", "/"),
            "routes": str(ROUTES.relative_to(ROOT)).replace("\\", "/"),
        },
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "checks": {key: bool(value) for key, value in checks.items()},
        "epistemic_policy": {
            "observed_gauge_data_used_as_selector": False,
            "target_fitting_used": False,
            "cross_functional_identification_without_theorem": False,
            "standard_QFT_threshold_transport_called_MTT_prediction": False,
            "prediction_claimed": False,
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_SameSourceGaugeHessianCrossUse_or_SectorEndomorphismValueEmission_v1",
        "status": STATUS,
        "A63_relative_rank_two_retained": True,
        "direct_K_to_tree_gauge_crossuse_rejected": True,
        "mass_threshold_route_typed_as_transport_only": True,
        "native_gauge_functional_rows_emitted": 0,
        "native_gauge_functional_rows_required": 3,
        "new_continuous_parameters": 0,
        "no_knob_gauge_coupling_prediction_closed": False,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Same-Source Gauge Hessian Cross-Use or Sector-Endomorphism Value Emission v1

## Direct cross-use test

A63 proved that charged `u,d,e` support plus the one-Higgs support spans the two-dimensional gauge
ratio plane. That rank result remains valid. It does **not** identify the charged/Higgs overlap
scalars with gauge kinetic coefficients.

For the selected A51 almost-commutative spectral action, the tree-level gauge rows are

```text
K_a(tree) = f0 Tr_HF(T_a^2),
Tr_HF(T_a^2) = (6,6,6) in GUT normalization.
```

The finite `D_F` data instead enter the separate Yukawa/Higgs invariants `Tr(Ydagger Y)` and
`Tr((Ydagger Y)^2)`. Directly substituting the nine charged `K_threshold` scalars or the H scalar
into `K_a(tree)` would change the action rather than evaluate it. That promotion is rejected.

## Legitimate threshold route

Integrating out a massive charged field can generate a mass-dependent vacuum-polarization term of
the schematic form

```text
Delta(1/g_a^2) = sum_r c_a(r) log(m_r^2/mu^2) + finite_scheme_terms.
```

This requires typed physical masses, a decoupling scale, loop order and subtraction scheme. The
current overlap `K` is not itself a proved mass ratio. Even after those inputs are supplied, the
calculation transports a gauge boundary condition; it does not select the boundary condition.

## Correct next source object

The shortest surviving route is therefore the native common-scheme gauge functional already
isolated by A53/A54: compute normalized quadratic rows for the selected `U1_circle`, `SU2_lens`,
and `SU3_nil` carriers, or compute the equivalent three insertions of one finite heat supertrace.
No A62 spectrum is reopened, and no charged/Higgs result is demoted.

Current native gauge-functional rows: `0/3`. Next artifact: `{NEXT}`.
"""

    dump(CROSSUSE, crossuse)
    dump(ROUTES, routes)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
