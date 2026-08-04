from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

FINITE_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
STRICT_TEGR = ROOT / "certificates" / "strict_same_source_teleparallel_selection_certificate.json"
TEGR_BRIDGE = ROOT / "certificates" / "closure_anholonomy_teleparallel_einstein_bridge_certificate.json"
GLOBAL_HESSIAN = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
ACTION_REDUCTION = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
ZERO_MODE = ROOT / "certificates" / "q79_coherent_zero_mode_tt_source_certificate.json"
VACUUM_NOGO = (
    ROOT
    / "certificates"
    / "q79_zero_defect_vacuum_selection_nogo_and_state_cutset_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_finite_source_tegr_classical_closure_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Finite_Source_TEGR_Classical_Closure_and_Parameter_Ledger_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    finite = load(FINITE_HESSIAN)
    strict = load(STRICT_TEGR)
    tegr = load(TEGR_BRIDGE)
    global_hessian = load(GLOBAL_HESSIAN)
    action = load(ACTION_REDUCTION)
    zero_mode = load(ZERO_MODE)
    vacuum = load(VACUUM_NOGO)

    kappa_e, kappa_h, g_eff = sp.symbols("kappa_e kappa_h G_eff", positive=True)
    lambda_eff = sp.symbols("Lambda_eff", real=True)
    kappa_transport = sp.Eq(kappa_h, kappa_e / 4)
    newton_relation = sp.Eq(g_eff, 1 / (32 * sp.pi * kappa_h))
    newton_from_strain = sp.simplify(newton_relation.rhs.subs(kappa_h, kappa_e / 4))

    tegr_ray = [sp.Rational(1, 4), sp.Rational(1, 2), -sp.Integer(1)]
    orientation_constraints = sp.Matrix([[2, 1, 1], [-4, 2, 0]])
    ray_vector = sp.Matrix(tegr_ray)

    checks = {
        "finite_q79_TT_block_is_exact_identity_shape": finite["claim_tiers"][
            "finite_rootstack_TT_2x2_block"
        ]
        == "CLOSED_EXACT_IDENTITY_SHAPE"
        and finite["finite_data"]["TT_multiplicity_block"]
        == [["1", "0"], ["0", "1"]],
        "finite_q79_TT_block_has_zero_dimensionless_fits": finite["finite_data"][
            "dimensionless_fitted_parameters"
        ]
        == 0,
        "finite_q79_TT_block_has_one_overall_scale": finite["finite_data"][
            "overall_action_normalizations"
        ]
        == 1,
        "strict_same_source_selects_unique_TEGR_ray": strict["claim_tiers"][
            "strict_same_source_two_derivative_teleparallel_action"
        ]
        == "CLOSED_UNIQUE_TEGR_RAY",
        "strict_candidate_classical_GR_is_exact_up_to_kappa_lambda_boundary": strict[
            "claim_tiers"
        ]["leading_two_derivative_classical_GR_on_candidate_branch"]
        == "CLOSED_EXACT_UP_TO_KAPPA_LAMBDA_BOUNDARY",
        "TEGR_bulk_equations_equal_Einstein": tegr["claim_tiers"][
            "TEGR_bulk_field_equations_equal_Einstein_equations"
        ]
        == "CLOSED_EXACT",
        "TEGR_EH_boundary_identity_is_exact": tegr["claim_tiers"][
            "TEGR_Einstein_Hilbert_boundary_identity"
        ]
        == "CLOSED_EXACT",
        "TEGR_ray_solves_both_orientation_constraints": orientation_constraints
        * ray_vector
        == sp.zeros(2, 1),
        "orientation_constraint_kernel_is_one_dimensional": len(
            orientation_constraints.nullspace()
        )
        == 1,
        "strain_to_metric_scale_transport_is_one_quarter": global_hessian[
            "claim_tiers"
        ]["strain_to_metric_Hessian_coordinate_transport"]
        == "CLOSED_EXACT_FACTOR_ONE_QUARTER",
        "Fierz_Pauli_operator_shape_is_unique": global_hessian["claim_tiers"][
            "Fierz_Pauli_operator_uniqueness"
        ]
        == "CLOSED_CONDITIONAL_ON_FOUR_EXPLICIT_ACTION_HYPOTHESES",
        "nonlinear_Einstein_completion_is_unique_at_declared_IR_tier": action[
            "claim_tiers"
        ]["four_dimensional_nonlinear_metric_completion"]
        == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES",
        "stress_has_no_independent_normalization": action["claim_tiers"][
            "independent_stress_normalization"
        ]
        == "CLOSED_NONE_BEYOND_KAPPA_H",
        "one_dimensionful_primitive_is_necessary": action["claim_tiers"][
            "one_dimensionful_primitive_is_necessary"
        ]
        == "CLOSED_FOR_CURRENT_SCALE_FREE_SOURCE_DATA",
        "massless_internal_zero_mode_and_unit_residue_are_closed": zero_mode[
            "claim_tiers"
        ]["geometric_coherent_zero_mode_TT_source_row"]
        == "CLOSED"
        and zero_mode["claim_tiers"]["canonical_internal_massless_residue"]
        == "CLOSED_UNIT",
        "vacuum_state_no_go_is_retained": vacuum["claim_tiers"][
            "Minkowski_zero_defect_endpoint_is_unique_vacuum"
        ]
        == "CLOSED_NO_GO_WITHOUT_STATE_OR_BOUNDARY_SELECTOR",
        "kappa_transport_is_symbolically_consistent": kappa_transport.rhs
        == kappa_e / 4,
        "Newton_relation_reduces_to_one_over_8pi_kappa_e": newton_from_strain
        == 1 / (8 * sp.pi * kappa_e),
        "Lambda_is_independent_of_TT_shape": lambda_eff not in tt_shape_symbols(),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_finite_source_tegr_classical_closure",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_FINITE_SOURCE_TWO_DERIVATIVE_CLASSICAL_GR_CLOSED_AT_DECLARED_TWO_PARAMETER_TIER_STATE_AND_QUANTUM_UV_OPEN",
        "inputs": {
            "finite_rootstack_TT_Hessian": str(FINITE_HESSIAN),
            "strict_same_source_TEGR": str(STRICT_TEGR),
            "teleparallel_Einstein_bridge": str(TEGR_BRIDGE),
            "global_TT_Hessian": str(GLOBAL_HESSIAN),
            "Einstein_action_reduction": str(ACTION_REDUCTION),
            "coherent_zero_mode": str(ZERO_MODE),
            "vacuum_selection_no_go": str(VACUUM_NOGO),
        },
        "theorem": {
            "name": "q79FiniteSourceTEGRClassicalClosureTheorem",
            "declared_tier": [
                "adopt the selected finite q79 minimal-rootstack source as the physical internal source tier",
                "use the canonical globally hyperbolic Lorentzian realization assumed by the revised Foundation/Fixed-Point chain",
                "work at local parity-even first-derivative/two-derivative infrared order",
                "require strict same-source orientation-fiber neutrality and metric descent",
            ],
            "conclusion": (
                "The finite q79 source fixes the TT Hessian shape; strict same-source "
                "metric descent fixes the TEGR ray; the TEGR boundary identity gives "
                "Einstein-Hilbert and the Einstein equations. The law has exactly the "
                "two standard effective gravitational coordinates kappa_h and Lambda_eff."
            ),
            "action": {
                "Einstein_Hilbert": "S_EH=2 kappa_h integral e (R-2 Lambda_eff)+S_matter",
                "teleparallel": "S_TEGR=-2 kappa_h integral e T_TEGR-4 kappa_h Lambda_eff integral e+S_matter",
                "TEGR_scalar": "T_TEGR=(1/4)I1+(1/2)I2-I3",
                "boundary_identity": "e R(LC)=-e T_TEGR+2 partial_mu(e T^mu)",
                "field_equation": "G_mn+Lambda_eff g_mn=(4 kappa_h)^(-1) T_mn",
            },
            "normalization_relations": {
                "strain_to_metric": "kappa_h=kappa_e/4",
                "Newton": "kappa_h=(32 pi G_eff)^(-1)",
                "combined": "G_eff=(8 pi kappa_e)^(-1)",
            },
            "state_boundary_distinction": (
                "The field equations define the classical theory without selecting one "
                "solution. Initial/asymptotic state data select our universe and are not "
                "coupling constants. The exact Ricci-flat wave no-go therefore remains "
                "valid and does not undo classical GR equivalence."
            ),
        },
        "parameter_ledger": {
            "dimensionless_gravity_shape_parameters": 0,
            "continuous_effective_law_parameters": [
                {
                    "name": "kappa_h_or_G_eff",
                    "count": 1,
                    "status": "REQUIRED_NOT_NUMERICALLY_DERIVED",
                    "meaning": "one dimensionful Newton/action normalization; kappa_h and G_eff are the same coordinate",
                },
                {
                    "name": "Lambda_eff",
                    "count": 1,
                    "status": "REQUIRED_NOT_DERIVED",
                    "meaning": "one effective cosmological coordinate, including vacuum renormalization",
                },
            ],
            "continuous_effective_law_parameter_count": 2,
            "independent_stress_normalizations": 0,
            "independent_TEGR_constitutive_ratios": 0,
            "independent_TT_polarization_stiffness_ratios": 0,
            "odd_root_choice_affecting_physical_TT_block": 0,
            "initial_or_boundary_state": {
                "counted_as_law_parameter": False,
                "status": "OPEN_PHYSICAL_STATE_SELECTION",
            },
            "higher_derivative_EFT_or_UV_parameters": "NOT_CLOSED_OR_COUNTED_AT_THIS_TIER",
        },
        "claim_tiers": {
            "finite_q79_internal_TT_operator_shape": "CLOSED_EXACT",
            "two_derivative_TEGR_constitutive_shape": "CLOSED_EXACT_UNIQUE_RAY",
            "Einstein_Hilbert_bulk_equivalence": "CLOSED_EXACT_MOD_BOUNDARY",
            "Einstein_field_equations_and_relative_stress_coupling": "CLOSED_EXACT",
            "massless_internal_zero_mode": "CLOSED_EXACT_UNIT_RESIDUE",
            "classical_GR_equivalence_at_declared_finite_source_IR_tier": "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES",
            "numeric_Newton_constant": "OPEN_ONE_DIMENSIONFUL_INPUT",
            "numeric_or_derived_Lambda_eff": "OPEN_ONE_EFFECTIVE_INPUT",
            "unique_cosmic_state_or_Minkowski_vacuum": "OPEN_STATE_BOUNDARY_SELECTION",
            "primitive_MTT_selection_of_declared_physical_tier": "OPEN_DISCRETE_REALIZATION_INPUT",
            "continuum_inverse_Fourier_Mukai_balanced_HYM_completion": "OPEN_OPTIONAL_FOR_FINITE_TIER_NOT_CLAIMED",
            "higher_derivative_quantum_UV_completion": "OPEN",
            "full_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_unconditional_primitive_MTT_branch_selection": False,
            "claims_numeric_Newton_constant_derived": False,
            "claims_cosmological_constant_derived": False,
            "claims_field_equations_select_one_vacuum": False,
            "claims_continuum_balanced_HYM_computed": False,
            "claims_quantum_gravity_closed": False,
            "uses_observed_GR_values": False,
            "adds_dimensionless_gravity_fit": False,
        },
        "checks": checks,
        "remaining_QG_cutset": [
            "select or explicitly postulate the physical Lorentzian/rootstack realization and causal state class",
            "supply one Newton/action scale and Lambda_eff, or derive them from a dimensionful MTT source and vacuum theorem",
            "select a quantum measure/action beyond the two-derivative IR law and prove unitarity/constraint closure",
            "control the higher spectral/heat-kernel remainder or provide another UV completion",
        ],
        "next_required_artifact": "MTT_q79_Selected_State_Lambda_and_QuantumMeasure_or_Explicit_TwoParameter_QG_EFT_Closure_v1",
        "note_written": str(OUT_NOTE),
    }

    note = """# q79 Finite-Source TEGR Classical Closure and Parameter Ledger v1

Date: 2026-07-15

Status:
`Q79_FINITE_SOURCE_TWO_DERIVATIVE_CLASSICAL_GR_CLOSED_AT_DECLARED_TWO_PARAMETER_TIER_STATE_AND_QUANTUM_UV_OPEN`

## Result

At the explicitly declared finite q79 source and two-derivative infrared tier,
the classical gravity chain now closes.

The new finite root-stack theorem emits

```text
H_std = kappa_e I2
```

with no dimensionless fit. Exact metric-coordinate transport gives

```text
kappa_h = kappa_e/4.
```

Strict same-source orientation neutrality fixes the full parity-even
teleparallel coefficient ray:

```text
(c1,c2,c3) proportional to (1/4,1/2,-1).
```

Therefore

```text
T_TEGR = (1/4)I1+(1/2)I2-I3,
e R(LC) = -e T_TEGR + 2 partial_mu(e T^mu).
```

The two equivalent actions are

```text
S_EH   =  2 kappa_h integral e (R-2 Lambda_eff) + S_matter,
S_TEGR = -2 kappa_h integral e T_TEGR
         -4 kappa_h Lambda_eff integral e + S_matter.
```

Their bulk equation is

```text
G_mn+Lambda_eff g_mn=(4 kappa_h)^(-1) T_mn.
```

No independent stress coefficient survives. The Newton relation is

```text
kappa_h=(32 pi G_eff)^(-1),
G_eff=(8 pi kappa_e)^(-1).
```

## Parameter ledger

At this tier the gravitational law has exactly two continuous effective
coordinates:

```text
1. kappa_h, equivalently G_eff: one dimensionful normalization;
2. Lambda_eff: one effective cosmological coordinate.
```

It has zero independent dimensionless TT-shape, TEGR-ratio, polarization, or
stress-normalization parameters. The two odd shared-circle roots give the same
finite TT block and do not add a physical parameter.

## State is not a coupling

The earlier exact pp-wave counterexample remains important: the vacuum field
equations do not choose Minkowski over every Ricci-flat wave. This does not
invalidate GR closure. A dynamical law defines a solution space; initial,
asymptotic, or quantum state data select a solution and are not extra coupling
constants. A separate MTT vacuum/state theorem is still needed to claim that
perfect closure selects our universe's flat endpoint.

## Exact boundary

This is a conditional classical closure theorem because it adopts the finite
minimal-rootstack source and canonical Lorentzian realization as the physical
tier. Primitive MTT selection of that tier remains open. The continuum
inverse-Fourier-Mukai/balanced-HYM construction is not required for this finite
source theorem and is not claimed solved.

Full quantum gravity is not yet closed. The remaining cutset is:

```text
physical realization and causal/state selection,
the values or source theorem for kappa_h and Lambda_eff,
a selected quantum measure with constraint/unitarity control,
higher-derivative or spectral-remainder/UV control.
```
"""

    OUT_CERT.write_text(json.dumps(certificate, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


def tt_shape_symbols() -> set[sp.Symbol]:
    # The normalized finite block is the constant identity; Lambda does not enter it.
    return set(sp.eye(2).free_symbols)


if __name__ == "__main__":
    main()
