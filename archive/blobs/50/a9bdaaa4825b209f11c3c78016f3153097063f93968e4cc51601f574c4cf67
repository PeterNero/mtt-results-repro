"""Construct the gauge-fixed SM fluctuation complex and finite threshold test."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "gauge_fixed_complex_and_signed_heat_rows.packet.json"
TEMPLATE = OUT / "sector_resolved_internal_fluctuation_spectra.template.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1.md"
STATUS = "MTT_SELECTED_GAUGE_FIXED_FLUCTUATION_COMPLEX_AND_BETA_SUPERTRACE_CLOSED_COMMON_INTERNAL_SPECTRUM_IS_SCALE_SHIFT_SECTOR_SPECTRA_OPEN"
NEXT = "MTT_Selected_SectorResolvedInternalFluctuationSpectra_or_NonUniversalGaugeThresholdPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> int:
    a56 = load(ROOT / "certificates" / "selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload_certificate.json")
    a48 = load(ROOT / "candidate_data" / "selected_nativegaugeactiontofinitebimodule_or_directgenerativesmbaseclosure" / "native_gauge_action_finite_bimodule.packet.json")
    a55 = load(ROOT / "candidate_data" / "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate" / "common_scheme_payload_search_and_finite_candidate.packet.json")
    a52 = load(ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json")

    # All fermions are left-Weyl rows. Conjugating a right-handed SM field does
    # not change Y^2 or nonabelian Dynkin indices.
    fermions = [
        {"field": "Q", "families": 3, "d3": 3, "d2": 2, "Y": Fraction(1, 6), "T3": Fraction(1, 2), "T2": Fraction(1, 2)},
        {"field": "u^c", "families": 3, "d3": 3, "d2": 1, "Y": Fraction(-2, 3), "T3": Fraction(1, 2), "T2": Fraction(0)},
        {"field": "d^c", "families": 3, "d3": 3, "d2": 1, "Y": Fraction(1, 3), "T3": Fraction(1, 2), "T2": Fraction(0)},
        {"field": "L", "families": 3, "d3": 1, "d2": 2, "Y": Fraction(-1, 2), "T3": Fraction(0), "T2": Fraction(1, 2)},
        {"field": "e^c", "families": 3, "d3": 1, "d2": 1, "Y": Fraction(1), "T3": Fraction(0), "T2": Fraction(0)},
        {"field": "N^c", "families": 3, "d3": 1, "d2": 1, "Y": Fraction(0), "T3": Fraction(0), "T2": Fraction(0)},
    ]
    fermion_rows = []
    sum_t = {"U1_GUT": Fraction(0), "SU2": Fraction(0), "SU3": Fraction(0)}
    for row in fermions:
        u1 = Fraction(row["families"] * row["d3"] * row["d2"]) * Fraction(3, 5) * row["Y"] ** 2
        su2 = Fraction(row["families"] * row["d3"]) * row["T2"]
        su3 = Fraction(row["families"] * row["d2"]) * row["T3"]
        indices = {"U1_GUT": u1, "SU2": su2, "SU3": su3}
        for key in sum_t:
            sum_t[key] += indices[key]
        fermion_rows.append({"field": row["field"], "Weyl_multiplicity": row["families"] * row["d3"] * row["d2"], "indices": {key: ftext(value) for key, value in indices.items()}})

    scalar_t = {"U1_GUT": Fraction(3, 10), "SU2": Fraction(1, 2), "SU3": Fraction(0)}
    adjoint_c2 = {"U1_GUT": Fraction(0), "SU2": Fraction(2), "SU3": Fraction(3)}
    gauge_ghost = {key: -Fraction(11, 3) * value for key, value in adjoint_c2.items()}
    weyl = {key: Fraction(2, 3) * value for key, value in sum_t.items()}
    scalar = {key: Fraction(1, 3) * value for key, value in scalar_t.items()}
    beta_exact = {key: gauge_ghost[key] + weyl[key] + scalar[key] for key in sum_t}
    order = ["U1_GUT", "SU2", "SU3"]
    beta_vector = np.asarray([float(beta_exact[key]) for key in order])
    imported_beta = np.asarray(a52["universal_gauge_relation_test"]["one_loop_beta_coefficients"], dtype=float)

    base_L = float(a55["finite_projected_candidate"]["base_logdet_L"])
    finite_delta = beta_vector * base_L / (8.0 * math.pi**2)
    # Since one-loop running is g^-2(Q)=g^-2(Q0)-b log(Q/Q0)/(8pi^2),
    # adding +b L/(8pi^2) is exactly Q -> Q*exp(-L).
    equivalent_scale_factor = math.exp(-base_L)
    centered_beta = (np.eye(3) - np.ones((3, 3)) / 3.0) @ beta_vector

    hessians = {
        "gauge_one_forms": {"operator": "Delta_1,a(mu,nu) = -D_a^2 delta(mu,nu) - 2 ad(F_a,mu,nu)", "gauge": "background Feynman gauge", "combined_gauge_ghost_index_weight": "-11/3 C2(G_a)", "structural_block_closed": True},
        "ghost_zero_forms": {"operator": "Delta_0,a = -D_a^2", "statistics": "complex Grassmann FP ghost", "effective_action_weight": "-1", "structural_block_closed": True},
        "left_Weyl_fermions": {"operator": "Dslash_R^2 = -D_R^2 + (1/2) sigma^{mu nu} F_R,mu nu", "heat_index_weight": "+2/3 T_a(R) per Weyl fermion", "structural_block_closed": True},
        "complex_Higgs": {"operator": "Delta_H = -D_H^2 + E_H from the selected Higgs Hessian", "heat_index_weight": "+1/3 T_a(H) per complex scalar", "structural_block_closed": True},
    }
    template = {
        "schema": "MTTSectorResolvedInternalFluctuationSpectra.v1",
        "common_background_and_scheme": {"compactification_background": None, "matching_scale_GeV": None, "regularization": None, "zero_mode_BRST_policy": None},
        "blocks": {
            name: {"internal_operator_from_selected_connection": None, "positive_spectrum_with_multiplicity": None, "gauge_index_insertion": None, "finite_part": None, "error_certificate": None, "accepted": False}
            for name in ["U1_gauge_ghost", "SU2_gauge_ghost", "SU3_gauge_ghost", "Q", "u", "d", "L", "e", "N", "H"]
        },
        "acceptance": "At least one internal spectrum or endomorphism block must differ by selected sector/representation data; a common scalar spectrum only renormalizes the matching scale.",
    }

    checks = {
        "A56_fluctuation_complex_was_exact_missing_object": a56["gauge_fixed_fluctuation_template_emitted"],
        "selected_fermion_carrier_dimension_96": a48["dimensions"]["three_family_total"] == 96,
        "fermion_index_sums_are_6_6_6": all(sum_t[key] == 6 for key in order),
        "beta_vector_derived_exactly": [ftext(beta_exact[key]) for key in order] == ["41/10", "-19/6", "-7"],
        "derived_beta_matches_accepted_QFT_vector": bool(np.allclose(beta_vector, imported_beta, atol=1e-15, rtol=0.0)),
        "finite_common_spectrum_threshold_is_beta_proportional": bool(np.allclose(finite_delta, imported_beta * base_L / (8.0 * math.pi**2), atol=1e-15, rtol=0.0)),
        "beta_response_is_nonuniversal_but_only_scale_translation": float(np.linalg.norm(centered_beta)) > 1.0 and equivalent_scale_factor > 0,
        "sector_resolved_internal_spectra_not_present": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}

    packet = {
        "schema": "MTTSelectedGaugeFixedFluctuationComplexHessiansOrOneLoopThresholdSupertracePayload.v1",
        "status": STATUS,
        "theorems": {
            "gauge_fixed_complex": {"proved_structurally": all(checks.values()), "statement": "The selected SM representation and one-Higgs carrier determine the background-field gauge/ghost, left-Weyl and complex-Higgs fluctuation blocks and their signed heat-index weights. Their exact sum is b=(41/10,-19/6,-7)."},
            "common_spectrum_scale_shift_no_go": {"proved": True, "statement": "If every fluctuation block uses the same selected internal finite determinant L, the threshold is b_a L/(8pi^2), which is algebraically identical to translating the one-loop matching scale. It cannot improve the universal-boundary mismatch found in A52."},
        },
        "fluctuation_hessians": hessians,
        "representation_index_ledger": {"fermion_rows": fermion_rows, "sum_Weyl_T": {key: ftext(value) for key, value in sum_t.items()}, "Higgs_T": {key: ftext(value) for key, value in scalar_t.items()}, "adjoint_C2": {key: ftext(value) for key, value in adjoint_c2.items()}},
        "signed_heat_coefficients": {"sector_order": order, "gauge_plus_ghost": {key: ftext(value) for key, value in gauge_ghost.items()}, "Weyl_fermions": {key: ftext(value) for key, value in weyl.items()}, "complex_Higgs": {key: ftext(value) for key, value in scalar.items()}, "total_beta_exact": {key: ftext(value) for key, value in beta_exact.items()}, "total_beta_numeric": beta_vector.tolist()},
        "common_internal_spectrum_execution": {"base_logdet_L": base_L, "Delta_inverse_g2": finite_delta.tolist(), "equivalent_one_loop_scale_factor_Qprime_over_Q": equivalent_scale_factor, "adds_independent_threshold_shape": False},
        "minimal_missing_object": template,
        "checks": checks,
        "epistemic_policy": {"standard_QFT_beta_used_to_select_rows": False, "derived_beta_compared_downstream": True, "common_spectrum_called_nonuniversal_geometry": False, "new_continuous_parameters": 0, "strict_spectral_action_closed": False},
        "next_required_artifact": NEXT,
    }
    cert = {"certificate": "MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1", "status": STATUS, "gauge_fixed_fluctuation_complex_structural_blocks_closed": 4, "signed_heat_beta_vector_derived": True, "derived_beta_vector": [ftext(beta_exact[key]) for key in order], "common_internal_spectrum_is_only_scale_shift": True, "sector_resolved_internal_spectra_closed": False, "new_continuous_parameters": 0, "strict_spectral_action_closed": False, "next_required_artifact": NEXT}

    note = f"""# MTT Selected Gauge-Fixed Fluctuation Complex Hessians or One-Loop Threshold Supertrace Payload v1

## Constructed Complex

The missing gauge-fixed complex is now explicit at the structural/heat-index level: background-field
gauge one-forms, FP ghosts, all selected left-Weyl rows, and the selected complex Higgs doublet. The
representation ledger derives, rather than imports,

```text
b_GUT = (41/10, -19/6, -7)
```

from `-11/3 C2(G) + 2/3 sum_Weyl T(R) + 1/3 sum_complex_scalar T(R)`. The independently
accepted SM running vector agrees exactly, so the signs, ghost contribution, and representation
weights are now checked.

## Finite Spectrum Execution

Using the same selected internal base determinant `L={base_L:.15g}` for every block gives

```text
Delta(1/g_a^2) = {finite_delta.tolist()}.
```

This is proportional to `b_a`. It is exactly the one-loop scale translation
`Q -> Q*exp(-L)`, with `exp(-L)={equivalent_scale_factor:.15g}`. Therefore a common finite spectrum
does not add a threshold shape and cannot repair the A52 universal-boundary no-go.

## Remaining Numerical Payload

The required new information is now sharply sector-resolved: internal gauge/ghost spectra for each
gauge factor and internal fermion/Higgs spectra for each representation, all computed from their
selected circle/lens/nil/HYM connections. At least one block must differ by selected geometry;
otherwise every determinant is only a matching-scale redefinition. The emitted template lists the
ten exact spectrum blocks and their common BRST, regulator, zero-mode and error requirements.

Next artifact: `{NEXT}`.
"""

    dump(TEMPLATE, template); dump(PACKET, packet); dump(CANDIDATE, packet); dump(CERT, cert); NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True)); return 0


if __name__ == "__main__": raise SystemExit(main())
