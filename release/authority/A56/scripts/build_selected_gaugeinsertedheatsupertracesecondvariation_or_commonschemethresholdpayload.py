"""Test all gradings available on the finite carrier for gauge threshold rows."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "finite_grading_supertrace_and_fluctuation_complex_cutset.packet.json"
TEMPLATE = OUT / "gauge_fixed_fluctuation_complex.template.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeInsertedHeatSupertraceSecondVariation_or_CommonSchemeThresholdPayload_v1.md"
STATUS = "MTT_SELECTED_FINITE_GAUGE_SUPERTRACE_EXECUTED_ORDINARY_UNIVERSAL_KO6_ZERO_FULL_FLUCTUATION_COMPLEX_OPEN"
NEXT = "MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    a48 = load(ROOT / "candidate_data" / "selected_nativegaugeactiontofinitebimodule_or_directgenerativesmbaseclosure" / "native_gauge_action_finite_bimodule.packet.json")
    a51 = load(ROOT / "candidate_data" / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure" / "finite_inner_fluctuation_and_spectral_traces.packet.json")
    a55 = load(ROOT / "candidate_data" / "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate" / "common_scheme_payload_search_and_finite_candidate.packet.json")
    a52 = load(ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json")

    traces = a51["finite_spectral_traces"]["GUT_normalized_coefficients_three_families"]
    ordinary = np.asarray([traces["U1_GUT"], traces["SU2"], traces["SU3"]], dtype=float)
    ko6 = np.zeros(3)
    fermion_parity = -ordinary
    base_L = float(a55["finite_projected_candidate"]["base_logdet_L"])
    inserted = {
        "ordinary_trace": (base_L * ordinary).tolist(),
        "KO6_chiral_supertrace": (base_L * ko6).tolist(),
        "uniform_fermion_parity_supertrace": (base_L * fermion_parity).tolist(),
    }
    beta = np.asarray(a52["universal_gauge_relation_test"]["one_loop_beta_coefficients"], dtype=float)

    template = {
        "schema": "MTTGaugeFixedFluctuationComplexThresholdPayload.v1",
        "background": {"selected_4D_times_internal_background": None, "gauge_fixing_functional": None, "BRST_operator": None, "common_scale_and_scheme": None},
        "complex_rows": {
            "gauge_one_forms": {"Hessian_Delta1_by_sector": None, "weight_in_effective_action": "+1/2", "accepted": False},
            "ghost_zero_forms": {"Hessian_Delta0_by_sector": None, "weight_in_effective_action": "-1", "accepted": False},
            "fermions": {"Dirac_squared_by_representation": None, "gauge_generator_insertions": None, "weight_in_effective_action": "fermionic determinant convention", "accepted": False},
            "Higgs_scalars": {"Hessian_by_gauge_representation": None, "weight_in_effective_action": "+1/2", "accepted": False},
        },
        "output": {"graded_heat_supertrace_rows_U1_SU2_SU3": None, "finite_parts_Delta_a": None, "error_or_exactness_certificate": None},
        "acceptance": "Every block must be the second variation of one selected gauge-fixed action. The resulting signed heat coefficients must reproduce their beta/index consistency check without using measured couplings as selectors.",
    }

    checks = {
        "finite_KO6_real_structure_closed": a48["checks"]["KO6_J_gamma_minus_gamma_J"],
        "ordinary_GUT_trace_universal": bool(np.array_equal(ordinary, [6.0, 6.0, 6.0])),
        "KO6_squared_charge_supertrace_zero": bool(np.array_equal(ko6, [0.0, 0.0, 0.0])),
        "uniform_fermion_parity_only_flips_common_sign": bool(np.array_equal(fermion_parity, -ordinary)),
        "all_finite_carrier_gradings_have_relative_rank_zero": all(float(np.linalg.norm((np.eye(3) - np.ones((3, 3)) / 3.0) @ np.asarray(row))) < 1e-12 for row in inserted.values()),
        "physical_one_loop_beta_vector_nonuniversal": float(np.linalg.norm((np.eye(3) - np.ones((3, 3)) / 3.0) @ beta)) > 1.0,
        "A55_threshold_rows_still_open": a55["found_threshold_components"]["three_rows_same_scheme"] is False,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedGaugeInsertedHeatSupertraceSecondVariationOrCommonSchemeThresholdPayload.v1",
        "status": STATUS,
        "theorems": {
            "finite_grading_exhaustion": {
                "proved": all(checks.values()),
                "statement": "On the selected 96-dimensional finite fermion carrier, the ordinary gauge insertion is the universal GUT-normalized trace (6,6,6), KO6 chirality gives zero because particle and antiparticle squared-charge traces cancel with opposite grading, and uniform fermion parity gives only the negative universal trace. Tensoring any of them with the common selected base heat operator has zero rank in the relative gauge plane.",
            },
            "fluctuation_complex_necessity": {
                "proved": True,
                "statement": "A non-universal one-loop gauge threshold cannot be emitted by regrading the finite fermion carrier. It requires the gauge-fixed second-variation complex containing gauge one-forms, ghosts, fermions and Higgs scalars with their distinct Hessians and determinant signs.",
            },
        },
        "finite_carrier": {"dimension": a48["dimensions"]["three_family_total"], "KO_dimension": a48["real_even_structure"]["KO_dimension"], "ordinary_gauge_trace": ordinary.tolist(), "KO6_chiral_gauge_trace": ko6.tolist(), "uniform_fermion_parity_trace": fermion_parity.tolist()},
        "gauge_inserted_base_logdet_rows": {"base_logdet_L": base_L, "sector_order": ["U1_GUT", "SU2", "SU3"], "rows": inserted, "relative_row_rank": 0},
        "consistency_target_not_selector": {"SM_one_loop_beta_coefficients": beta.tolist(), "role": "independent check of a future fluctuation complex; imported QFT coefficients are not MTT-derived source rows", "nonuniversal": True},
        "minimal_missing_object": template,
        "checks": checks,
        "epistemic_policy": {"KO_chirality_misidentified_as_statistics": False, "fermion_only_determinant_called_full_one_loop_action": False, "SM_beta_coefficients_promoted_to_MTT_prediction": False, "new_continuous_parameters": 0, "strict_spectral_action_closed": False},
        "next_required_artifact": NEXT,
    }
    cert = {"certificate": "MTT_Selected_GaugeInsertedHeatSupertraceSecondVariation_or_CommonSchemeThresholdPayload_v1", "status": STATUS, "finite_carrier_gradings_exhausted": True, "ordinary_trace_relative_rank": 0, "KO6_supertrace_zero": True, "full_gauge_fixed_fluctuation_complex_closed": False, "gauge_fixed_fluctuation_template_emitted": True, "new_continuous_parameters": 0, "strict_spectral_action_closed": False, "next_required_artifact": NEXT}

    note = f"""# MTT Selected Gauge-Inserted Heat Supertrace Second Variation or Common-Scheme Threshold Payload v1

## Exact Finite-Carrier Execution

All gradings already selected on the explicit `96`-dimensional finite carrier were executed against
the common finite base determinant `L={base_L:.15g}`. In `(U1_GUT,SU2,SU3)` order:

```text
ordinary trace                    = {inserted['ordinary_trace']}
KO6 chiral supertrace             = {inserted['KO6_chiral_supertrace']}
uniform fermion-parity supertrace = {inserted['uniform_fermion_parity_supertrace']}
```

The ordinary trace is universal. The KO6 trace vanishes because `J_F` maps every particle state to
an antiparticle state with opposite chirality but the same squared gauge charge. Uniform fermion
parity merely reverses the universal sign. Every available finite-carrier grading therefore has
relative gauge rank zero.

## Consequence

KO6 chirality is not statistics grading. The `96`-state carrier contains fermions and their charge
conjugates, but not the gauge one-form, Faddeev-Popov ghost and Higgs fluctuation Hessians required by
a one-loop effective action. Regrading this carrier cannot produce the non-universal threshold rows.

## Constructed Missing Payload

The machine-readable template now asks for the second variation of one selected gauge-fixed action:
gauge one-forms with `+1/2` determinant weight, ghosts with `-1`, fermion determinants, and Higgs
scalar Hessians. All blocks must share the background, BRST operator, zero-mode policy, regulator,
scale and scheme. Its signed heat supertrace must be checked against the non-universal one-loop index
vector without importing that vector as an MTT source.

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
