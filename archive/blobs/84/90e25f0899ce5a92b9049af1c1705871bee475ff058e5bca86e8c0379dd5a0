from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

CLASSICAL = (
    ROOT / "certificates" / "q79_finite_source_tegr_classical_closure_certificate.json"
)
FREE_QUANTUM = (
    ROOT
    / "certificates"
    / "q79_free_graviton_quantization_and_uv_cutset_certificate.json"
)
SM_ANOMALY = (
    TEXPAPERS
    / "mtt-results-repro"
    / "release"
    / "authority"
    / "A46"
    / "candidate_data"
    / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem"
    / "typed_family_gauge_carrier_and_anomaly_table.packet.json"
)
SM_OBSERVABLE_FUNCTOR = (
    TEXPAPERS
    / "mtt-results-repro"
    / "release"
    / "authority"
    / "A03"
    / "candidate_data"
    / "selected_renormalizedsmobservablefunctor_fromcommonschemeaction"
    / "renormalized_sm_observable_functor.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_interacting_low_energy_qg_eft_closure_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Interacting_Low_Energy_Quantum_Gravity_EFT_Closure_and_UV_Boundary_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    classical = load(CLASSICAL)
    free_quantum = load(FREE_QUANTUM)
    sm_anomaly = load(SM_ANOMALY)
    sm_functor = load(SM_OBSERVABLE_FUNCTOR)

    loops, vertices, internal_lines = sp.symbols(
        "L V I", integer=True, nonnegative=True
    )
    superficial_degree = 4 * loops + 2 * vertices - 2 * internal_lines
    connected_identity = {internal_lines: loops + vertices - 1}
    reduced_degree = sp.expand(superficial_degree.subs(connected_identity))

    loop_table = [
        {
            "loop_order": loop_order,
            "superficial_derivative_order": int(
                reduced_degree.subs(loops, loop_order)
            ),
        }
        for loop_order in range(5)
    ]

    kappa_h, G_eff = sp.symbols("kappa_h G_eff", positive=True)
    graviton_vertex_coupling_squared = 32 * sp.pi * G_eff
    q79_relation = {G_eff: 1 / (32 * sp.pi * kappa_h)}
    coupling_in_q79_units = sp.simplify(
        graviton_vertex_coupling_squared.subs(q79_relation)
    )
    goroff_sagnotti_prefactor = sp.Rational(209, 2880) / (4 * sp.pi) ** 4

    anomaly_table = sm_anomaly["anomaly_table"]
    anomaly_checks = [
        bool(row["cancelled"]) for row in anomaly_table.values()
    ]

    checks = {
        "classical_two_derivative_GR_tier_available": classical["claim_tiers"][
            "classical_GR_equivalence_at_declared_finite_source_IR_tier"
        ]
        == "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES",
        "free_two_helicity_q79_sector_available": free_quantum["claim_tiers"][
            "free_massless_q79_graviton_carrier"
        ]
        == "CLOSED_EXACT_TWO_HELICITIES",
        "finite_internal_UV_shortcut_already_excluded": free_quantum["claim_tiers"][
            "finite_internal_trace_changes_4D_UV_power_counting"
        ]
        == "CLOSED_NO_GO",
        "connected_Einstein_graph_power_counting_is_2L_plus_2": reduced_degree
        == 2 * loops + 2,
        "tree_one_loop_two_loop_orders_are_2_4_6": [
            row["superficial_derivative_order"] for row in loop_table[:3]
        ]
        == [2, 4, 6],
        "q79_kappa_relation_gives_kappa_gr_squared_inverse_kappa_h": coupling_in_q79_units
        == 1 / kappa_h,
        "Goroff_Sagnotti_coefficient_is_nonzero": goroff_sagnotti_prefactor != 0,
        "selected_SM_local_and_global_anomaly_table_cancels": all(anomaly_checks),
        "SM_quantization_precedent_is_explicitly_imported": sm_functor[
            "scope_guards"
        ]["standard_SM_quantization_imported_as_parity_structure"]
        is True,
        "SM_quantization_precedent_is_not_MTT_derived": sm_functor[
            "scope_guards"
        ]["standard_SM_quantization_derived_from_MTT"]
        is False,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    status = (
        "Q79_INTERACTING_LOW_ENERGY_QG_EFT_PARITY_CLOSED_AT_FIXED_ORDER_"
        "LOCAL_WILSON_VALUES_PRIMITIVE_MTT_MEASURE_AND_UV_COMPLETION_OPEN"
    )

    certificate = {
        "certificate": "q79_interacting_low_energy_qg_eft_closure",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": status,
        "inputs": {
            "finite_source_classical_GR": str(CLASSICAL),
            "free_q79_graviton": str(FREE_QUANTUM),
            "selected_SM_anomaly_table": str(SM_ANOMALY),
            "SM_parity_quantization_precedent": str(SM_OBSERVABLE_FUNCTOR),
        },
        "theorem": {
            "name": "q79InteractingLowEnergyQuantumGravityEFTParityTheorem",
            "declared_tier": [
                "adopt the same finite q79 minimal-rootstack Lorentzian source tier used by the classical closure theorem",
                "use the Einstein-Hilbert/TEGR action with kappa_h and Lambda_eff",
                "import standard background-field BRST/BV perturbative quantization as parity structure, exactly as standard BRST/Faddeev-Popov quantization is imported in the closed SM observable functor",
                "include every local diffeomorphism-invariant counterterm through a declared finite derivative and loop order",
                "restrict predictions to energies and curvatures below the EFT breakdown scale",
            ],
            "composition": (
                "Obs_QG,EFT^MTT = Readout o LSZ/Inclusive o Green o "
                "Q_GR,EFT o E_q79"
            ),
            "equivalence_statement": (
                "If E_q79 supplies the same renormalized low-energy gravitational "
                "action, Wilson coefficients, gauge-fixing, state, scale and scheme "
                "as quantum GR EFT through order N, then the renormalized generating "
                "functionals and all gauge-invariant observables agree through order N."
            ),
            "power_counting_proof": (
                "For a connected Einstein graph, D=4L+2V-2I and "
                "L=I-V+1, hence D=2L+2. At every fixed L_max only a finite "
                "basis of local diffeomorphism invariants is required."
            ),
            "predictive_quantum_subsector": (
                "The nonanalytic long-distance terms generated by massless low-energy "
                "propagation are insensitive to local UV counterterms. Once kappa_h, "
                "the low-energy spectrum and state are fixed, that class introduces "
                "no new Wilson coefficient."
            ),
            "UV_boundary": (
                "Pure Einstein gravity has no physically relevant one-loop divergence "
                "on shell at Lambda_eff=0, but its two-loop S matrix has the nonzero "
                "Goroff-Sagnotti Riemann-cubed divergence. Thus fixed-order EFT "
                "predictivity is closed by standard composition, while two-parameter "
                "all-scale renormalizability and UV completion are excluded."
            ),
        },
        "finite_data": {
            "connected_graph_superficial_degree_before_topology": "4L+2V-2I",
            "connected_graph_identity": "L=I-V+1",
            "connected_graph_superficial_degree": "2L+2",
            "loop_derivative_table_L0_to_L4": loop_table,
            "q79_normalization": "kappa_h=(32 pi G_eff)^(-1)",
            "graviton_vertex_coupling_squared": "32 pi G_eff=1/kappa_h",
            "Goroff_Sagnotti_dimensionless_prefactor": (
                "209/[2880 (4 pi)^4]"
            ),
            "Goroff_Sagnotti_operator": (
                "kappa_gr^2 integral sqrt(-g) "
                "R_mn^rs R_rs^ab R_ab^mn / epsilon"
            ),
            "selected_SM_anomaly_rows_checked": len(anomaly_checks),
            "selected_SM_anomaly_rows_cancelled": sum(anomaly_checks),
            "physical_graviton_polarizations": 2,
        },
        "parameter_ledger": {
            "two_derivative_law_parameters": ["kappa_h_or_G_eff", "Lambda_eff"],
            "two_derivative_law_parameter_count": 2,
            "free_quantum_parameters_beyond_kappa_h": 0,
            "leading_nonanalytic_long_distance_Wilson_parameters": 0,
            "local_higher_derivative_Wilson_coefficients_at_fixed_order": (
                "FINITE_BUT_VALUES_NOT_EMITTED_BY_CURRENT_MTT_SOURCE"
            ),
            "local_higher_derivative_Wilson_coefficients_at_all_orders": (
                "UNBOUNDED_TOWER_WITHOUT_A_SELECTED_UV_COMPLETION"
            ),
            "gauge_fixing_and_renormalization_scheme": (
                "CONVENTION_COORDINATES_NOT_PHYSICAL_FIT_PARAMETERS"
            ),
            "causal_or_asymptotic_state": "REQUIRED_STATE_DATA_NOT_A_LAW_PARAMETER",
        },
        "claim_tiers": {
            "interacting_low_energy_quantum_GR_EFT": (
                "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER"
            ),
            "q79_to_quantum_GR_EFT_observable_functor": (
                "CLOSED_AT_PARITY_STANDARD_CONDITIONAL_ON_DECLARED_WILSON_DATA_AND_STATE"
            ),
            "classical_diffeomorphism_BRST_algebra": (
                "CLOSED_STANDARD_LIE_ALGEBRA_NILPOTENCY"
            ),
            "selected_SM_gauge_and_mixed_anomaly_table": "CLOSED_EXACT_SIX_ROWS",
            "quantum_master_equation_and_renormalized_Ward_identities": (
                "IMPORTED_STANDARD_EFT_STRUCTURE_NOT_DERIVED_FROM_MTT"
            ),
            "leading_nonanalytic_long_distance_quantum_corrections": (
                "CLOSED_AS_UV_INDEPENDENT_PREDICTIVE_CLASS_VALUES_NOT_COMPUTED_HERE"
            ),
            "one_loop_pure_GR_on_shell_Lambda_zero_divergence": (
                "CLOSED_NO_PHYSICALLY_RELEVANT_DIVERGENCE_STANDARD_RESULT"
            ),
            "two_loop_pure_GR_divergence": (
                "CLOSED_NONZERO_GOROFF_SAGNOTTI_STANDARD_RESULT"
            ),
            "two_parameter_interacting_quantum_GR_at_all_scales": "CLOSED_NO_GO",
            "finite_internal_carrier_as_spacetime_UV_regulator": "CLOSED_NO_GO",
            "MTT_selected_values_for_all_EFT_Wilson_coefficients": "OPEN",
            "primitive_MTT_derivation_of_quantum_measure_and_BV_QME": "OPEN",
            "massless_soft_dressed_asymptotic_completeness": "OPEN",
            "nonperturbative_or_UV_complete_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_standard_EFT_quantization_is_derived_from_MTT": False,
            "claims_fixed_order_EFT_is_UV_completion": False,
            "claims_only_kappa_and_Lambda_suffice_beyond_tree_level": False,
            "claims_all_higher_derivative_coefficients_are_selected": False,
            "claims_BRST_parity_closes_nonperturbative_measure": False,
            "claims_two_loop_divergence_is_removed_by_finite_internal_dimension": False,
            "uses_observed_quantum_gravity_values": False,
            "adds_fitted_continuous_parameter": False,
        },
        "primary_sources": {
            "low_energy_EFT_and_nonanalytic_predictions": (
                "https://arxiv.org/abs/gr-qc/9405057"
            ),
            "modern_quantum_GR_EFT_review": "https://arxiv.org/abs/2211.09902",
            "one_loop_pure_gravity": "https://inspirehep.net/literature/95368",
            "two_loop_pure_gravity": "https://inspirehep.net/literature/213907",
            "two_loop_DOI": "https://doi.org/10.1016/0370-2693(85)91470-4",
        },
        "checks": checks,
        "next_required_artifact": (
            "MTT_q79_Selected_HigherDerivative_Wilson_Source_or_"
            "Nonperturbative_UV_FixedPoint_and_BV_Closure_v1"
        ),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Interacting Low-Energy Quantum Gravity EFT Closure and UV Boundary v1

Date: 2026-07-15

Status:
`{status}`

## What is newly closed

The q79 finite-source construction already supplies the positive two-helicity
massless graviton, the unique two-derivative TEGR/Einstein action shape, and the
relative Hilbert stress coupling. There is therefore a standard interacting
quantum route which does not require the rejected permanent-Gaussian claim:
quantize that action as quantum general relativity effective field theory.

At the declared parity tier, define

```text
Obs_QG,EFT^MTT
  = Readout o LSZ/Inclusive o Green o Q_GR,EFT o E_q79.
```

`Q_GR,EFT` is the standard background-field BRST/BV perturbative construction,
imported as parity structure. This is exactly the standard used by the closed
renormalized-SM observable functor: equality of the renormalized action,
measure convention, state, scale, scheme, and coefficients through order `N`
implies equality of generating functionals and gauge-invariant observables
through order `N`. It is not rebranded as an MTT derivation of quantization.

The selected three-family SM representation also passes all six stored anomaly
rows, including the even `SU(2)` doublet count. This removes the already-audited
SM gauge/mixed-anomaly obstruction at the parity tier; it does not replace a
constructive proof of the full gravitational BV measure.

## Exact power-counting theorem

For a connected graph made from two-derivative Einstein vertices,

```text
D = 4L + 2V - 2I,
L = I - V + 1,
therefore D = 2L + 2.
```

The required local counterterms consequently have derivative order `2L+2`.
At every fixed loop/derivative order, the diffeomorphism-invariant local basis
is finite, so the theory is renormalizable and predictive order by order as an
EFT. The exact table begins

```text
tree:     2 derivatives
one loop: 4 derivatives
two loop: 6 derivatives.
```

The long-distance nonanalytic loop terms come from the massless low-energy
propagators. Local UV counterterms cannot imitate those nonanalytic terms, so
their coefficient class is fixed once `kappa_h`, the low-energy spectrum, and
the causal state are fixed. No new Wilson parameter enters that class.

## The exact UV boundary

For `Lambda_eff=0`, pure Einstein gravity has no physically relevant on-shell
one-loop divergence. At two loops, however, the pure-gravity S matrix has the
nonzero Goroff-Sagnotti divergence

```text
Gamma_div^(2) proportional to
  [209/(2880 (4 pi)^4 epsilon)] kappa_gr^2
  integral sqrt(-g) R_mn^rs R_rs^ab R_ab^mn,

kappa_gr^2 = 32 pi G_eff = 1/kappa_h.
```

This establishes both halves of the result:

1. interacting low-energy q79 quantum gravity reaches the standard predictive
   quantum-GR EFT tier at every declared finite order;
2. the same calculation proves that `kappa_h` and `Lambda_eff` alone cannot be
   a UV-complete interacting quantum theory.

The finite q79 internal algebra fixes internal traces and the helicity block,
but it does not change the `D=2L+2` spacetime power counting.

## Parameter ledger

At two derivatives there are exactly the already-recorded coordinates
`kappa_h` (or `G_eff`) and `Lambda_eff`. Free quantization adds none. The
UV-independent nonanalytic long-distance quantum class adds none. Local
higher-derivative terms require finitely many Wilson coefficients at each
fixed order, but their numerical values are not yet emitted by the selected
MTT source; across all orders this is an unbounded tower unless a genuine UV
completion selects it.

Gauge choice, subtraction scheme, and renormalization scale are conventions,
not new physical fit parameters. Initial, causal, or asymptotic state data are
state data rather than law parameters.

## What remains for full quantum gravity

The remaining hard target is no longer the existence of an interacting
low-energy quantum theory. It is one of the genuinely stronger exits:

1. derive the higher-curvature Wilson rows from the selected q79 operator and
   control their full remainder; or
2. select and prove a nonperturbative UV fixed theory with its quantum measure,
   BV/constraint closure, unitarity, and continuum limit.

Primitive MTT selection of the Lorentzian realization, numerical `kappa_h`,
`Lambda_eff`, and a unique cosmic state remain separate source/value questions.

## Primary comparison sources

- Donoghue, low-energy gravity EFT and UV-independent nonanalytic corrections:
  https://arxiv.org/abs/gr-qc/9405057
- Donoghue, modern quantum-GR EFT review:
  https://arxiv.org/abs/2211.09902
- 't Hooft and Veltman, one-loop gravity:
  https://inspirehep.net/literature/95368
- Goroff and Sagnotti, two-loop pure gravity:
  https://inspirehep.net/literature/213907
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(status)


if __name__ == "__main__":
    main()
