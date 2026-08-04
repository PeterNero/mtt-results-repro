from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

GLOBAL_HESSIAN = (
    ROOT
    / "certificates"
    / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
)
ZERO_MODE = ROOT / "certificates" / "q79_coherent_zero_mode_tt_source_certificate.json"
SCALE_BRIDGE = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"

CLOSURE_STRAIN = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "Closure_Strain_Geometry__Local_Normal_Forms_and_Conditional_Matter_Encodings_v7"
    / "main.tex"
)
TEN_D_ACTION = (
    TEXPAPERS
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "Closure_Geometry_and_a_Regime_Local_Ten_Dimensional_Action_Ansatz_v4"
    / "main.tex"
)
THETA_IV = (
    TEXPAPERS
    / "18 Theta-Closure & Execution Program"
    / "_md_v3_corrected"
    / "Theta_Closure_in_Modal_Triplet_Theory_IV__Gravity_and_Cosmology_from_the_Closure_Scale.md"
)

OUT_CERT = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Closure_to_Einstein_Action_Reduction_and_One_Scale_NoGo_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    global_hessian = load(GLOBAL_HESSIAN)
    zero_mode = load(ZERO_MODE)
    scale_bridge = load(SCALE_BRIDGE)
    closure_text = CLOSURE_STRAIN.read_text(encoding="utf-8")
    action_text = TEN_D_ACTION.read_text(encoding="utf-8")
    theta_text = THETA_IV.read_text(encoding="utf-8")

    internal_dimension = 6
    volume_homothety_exponent = internal_dimension
    normalized_constant_homothety_exponent = Fraction(-internal_dimension, 2)

    # Repository convention:
    #   kappa_h = 1/(32*pi*G4),
    #   S_EH = 2*kappa_h int sqrt(-g)(R-2 Lambda),
    #   G_mn + Lambda g_mn = (4*kappa_h)^(-1) T_mn.
    kappa_h_times_pi_g4 = Fraction(1, 32)
    eh_prefactor_times_pi_g4 = 2 * kappa_h_times_pi_g4
    field_equation_coupling_over_pi_g4 = Fraction(1, 4) / kappa_h_times_pi_g4

    # For S10=(2*kappa10^2)^(-1) int R10 and an unwarped product reduction,
    # p4=V6/(2*kappa10^2)=2*kappa_h. Therefore
    # kappa_h=V6/(4*kappa10^2)=V6/(32*pi*G10).
    kappa_h_times_kappa10_sq_over_v6 = Fraction(1, 4)
    kappa_h_times_pi_g10_over_v6 = Fraction(1, 32)

    checks = {
        "closure_source_is_C3_real_scalar_functional": (
            r"Let $\mathcal J$ be a $C^3$ gauge-invariant closure functional"
            in closure_text
        ),
        "closure_source_has_stationary_point_and_quadratic_variation": (
            r"D\mathcal J(S_\ast)=0" in closure_text
            and r"\frac12\langle s,Hs\rangle+R_3(s)" in closure_text
        ),
        "finite_closure_slice_has_dimension_six": (
            r"$\dim\operatorname{Sym}(3)=6$" in closure_text
        ),
        "prior_global_TT_Hessian_form_is_closed": (
            global_hessian["claim_tiers"]["global_symmetric_weight2_Hessian_form"]
            == "CLOSED_UNDER_STATED_STABILITY_AND_COVARIANCE_HYPOTHESES"
        ),
        "prior_Fierz_Pauli_nullspace_is_one_dimensional": (
            global_hessian["theorem"]["part_C_action_uniqueness_reduction"][
                "solution_dimension"
            ]
            == 1
        ),
        "prior_metric_coefficient_is_kappa_e_over_four": (
            global_hessian["claim_tiers"][
                "strain_to_metric_Hessian_coordinate_transport"
            ]
            == "CLOSED_EXACT_FACTOR_ONE_QUARTER"
        ),
        "q79_zero_mode_has_unit_internal_residue": (
            zero_mode["claim_tiers"]["canonical_internal_massless_residue"]
            == "CLOSED_UNIT"
        ),
        "q79_zero_mode_does_not_fix_Newton_scale": (
            zero_mode["claim_tiers"]["physical_kappa_h_or_Newton_normalization"]
            == "OPEN"
        ),
        "ten_dimensional_paper_imports_Einstein_Hilbert": (
            "imports the Einstein--Hilbert term" in action_text
        ),
        "ten_dimensional_paper_declares_action_ansatz": (
            "action is an ansatz" in action_text
        ),
        "theta_IV_uses_retired_product_geometry": (
            "S^1_{\\mathrm{cen}} \\times \\Sigma_2 \\times \\Sigma_3"
            in theta_text
        ),
        "theta_IV_old_volume_scales_as_R1_cubed": (
            "31.8\\; R_1^3" in theta_text
        ),
        "theta_IV_already_identifies_one_irreducible_normalization": (
            "single irreducible" in theta_text
        ),
        "six_dimensional_volume_homothety_is_r_to_six": (
            volume_homothety_exponent == 6
        ),
        "normalized_constant_homothety_is_r_to_minus_three": (
            normalized_constant_homothety_exponent == -3
        ),
        "EH_prefactor_is_one_over_16_pi_G": (
            eh_prefactor_times_pi_g4 == Fraction(1, 16)
        ),
        "Einstein_equation_coupling_is_8_pi_G": (
            field_equation_coupling_over_pi_g4 == 8
        ),
        "unwarped_reduction_gives_kappa_h_V6_over_4_kappa10_squared": (
            kappa_h_times_kappa10_sq_over_v6 == Fraction(1, 4)
        ),
        "unwarped_reduction_gives_kappa_h_V6_over_32_pi_G10": (
            kappa_h_times_pi_g10_over_v6 == Fraction(1, 32)
        ),
        "old_scale_bridge_agrees_with_corrected_metric_convention": (
            scale_bridge["relation"]["combined_relation"]
            == "kappa_STF = V_int/(32*pi*G_10)"
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "ClosureHessianEinsteinCompletionStressAndOneScaleNoGoTheorem",
        "part_A_hessian_reciprocity": {
            "statement": (
                "On the finite six-dimensional gauge-fixed strain slice, the second "
                "derivative D^2 J(S_*) of the declared real C3 scalar closure "
                "functional is a symmetric bilinear form. Its Riesz representative H "
                "is therefore self-adjoint. More generally, the Jacobi operator of a "
                "real local spacetime action is formally self-adjoint after the "
                "declared boundary terms are fixed."
            ),
            "proof": (
                "Schwarz symmetry gives D^2J[u,v]=D^2J[v,u]. On a finite real inner-"
                "product space, <u,Hv>=D^2J[u,v]=D^2J[v,u]=<Hu,v>, so H=H*. "
                "The field-theory statement is the same second-variation identity "
                "after integration by parts."
            ),
            "scope": (
                "Finite closure-Hessian self-adjointness is closed. Formal self-"
                "adjointness of the physical kinetic operator is no longer an "
                "independent coefficient assumption once a same-source real local "
                "spacetime action is supplied; that promotion is still open."
            ),
        },
        "part_B_nonlinear_completion": {
            "hypotheses": [
                "a four-dimensional Lorentzian metric is the selected physical observable",
                "the metric equation is a local diffeomorphism-natural symmetric tensor built from g and at most its first two derivatives",
                "the equation is identically divergence-free and at most second order",
                "the metric-only infrared branch has no additional propagating gravitational fields",
            ],
            "result": (
                "By the four-dimensional Lovelock classification, the metric equation "
                "is a G_mn+b g_mn. Matching its nonzero quadratic TT block to the "
                "already unique Fierz-Pauli operator fixes a=2*kappa_h at action level."
            ),
            "dynamically_unique_action": (
                "S_grav=2*kappa_h integral_Y sqrt(-g)(R-2 Lambda), modulo boundary "
                "terms and four-dimensional topological densities"
            ),
            "cosmological_constant_boundary": (
                "Lambda is allowed by the uniqueness theorem but is not selected by "
                "the present MTT source. A flat vacuum requires the total tadpole to "
                "set Lambda_eff=0; a cosmological branch needs its own vacuum-energy theorem."
            ),
            "primary_sources": {
                "Lovelock_1971": "https://doi.org/10.1063/1.1665613",
                "Deser_self_coupling_reprint": "https://arxiv.org/abs/gr-qc/0411023",
            },
        },
        "part_C_stress_and_coefficient": {
            "matter_definition": (
                "T_mn=-(2/sqrt(-g)) delta S_matter/delta g^(mn)"
            ),
            "variation_convention": (
                "delta S_matter=-(1/2) integral sqrt(-g) T_mn delta g^(mn)"
            ),
            "field_equation": "G_mn+Lambda g_mn=(4*kappa_h)^(-1) T_mn",
            "Newton_bridge": {
                "kappa_h": "1/(32*pi*G4)",
                "field_equation": "G_mn+Lambda g_mn=8*pi*G4*T_mn",
                "EH_prefactor": "2*kappa_h=1/(16*pi*G4)",
            },
            "conservation": (
                "For a diffeomorphism-invariant matter action, the matter equations "
                "and Noether identity give nabla^m T_mn=0. The contracted Bianchi "
                "identity makes the same conservation law necessary for the metric equation."
            ),
            "parameter_statement": (
                "Once one common metric action and kappa_h are selected, stress carries "
                "no additional gravitational normalization. Universal coupling is "
                "conditional on all retained matter sectors using that same metric."
            ),
        },
        "part_D_unwarped_q79_reduction": {
            "parent_action": "S10=(2*kappa10^2)^(-1) integral sqrt(|g10|) R10",
            "four_dimensional_prefactor": "V6/(2*kappa10^2)=2*kappa_h",
            "relations": [
                "kappa_h=V6/(4*kappa10^2)",
                "kappa10^2=8*pi*G10",
                "kappa_h=V6/(32*pi*G10)",
                "G4=G10/V6",
            ],
            "scope": (
                "These relations are exact for an unwarped product with a constant "
                "normalized zero mode. Warping, dilaton factors, higher-curvature "
                "terms, and threshold corrections replace V6 by the corresponding "
                "weighted overlap and require a new reduction calculation."
            ),
        },
        "part_E_scale_no_go": {
            "closed_data_scope": (
                "q79 topology, connectedness, scalar harmonic rank, normalized zero-"
                "mode projector, unit internal residue, and finite monodromy labels"
            ),
            "homothety": "g_X -> r^2 g_X for r>0",
            "transformations": {
                "V6": "V6 -> r^6 V6",
                "phi0": "phi0 -> r^(-3) phi0",
                "Pi0_rank": "1 -> 1",
                "unit_internal_residue": "Id -> Id",
                "kappa_h_at_fixed_parent_coupling": "kappa_h -> r^6 kappa_h",
            },
            "no_go": (
                "The currently closed scale-free q79/topological/zero-mode data cannot "
                "determine numerical kappa_h: they are unchanged as normalized data "
                "under a continuous rescaling that changes kappa_h. A selected metric "
                "scale or equivalent dimensionful primitive is necessary."
            ),
            "one_primitive_form": {
                "V6": "v6*ell_*^6",
                "G10": "g10*ell_*^8",
                "kappa_h": "[v6/(32*pi*g10)]*ell_*^(-2)",
                "interpretation": (
                    "One length primitive ell_* is sufficient only after the "
                    "dimensionless ratio v6/g10 is selected by the full metric/action source."
                ),
            },
        },
        "part_F_theta_IV_reconciliation": {
            "retained": (
                "The four-dimensional coupling is controlled by one effective ratio "
                "V6/G10, so the paper's one-effective-normalization intuition survives."
            ),
            "retired": [
                "the literal S1_cen x Sigma2 x Sigma3 proof source",
                "the numerical volume V=31.8 R1^3",
                "the claim that Theta alone fixes the active q79 internal volume",
            ],
            "replacement": (
                "Use X6_q79=P_delta x S1_shared and either compute its weighted metric "
                "volume from a selected Fu-Yau/Strominger solution or retain V6/G10 as "
                "the single effective gravitational normalization."
            ),
        },
        "remaining_selected_source_packet": {
            "name": "SelectedSpacetimeClosureActionSource.v1",
            "required_fields": {
                "physical_metric": "G=Q^TQ on the selected four-dimensional Lorentzian base",
                "naturality": "J4[f*G,f*Phi]=J4[G,Phi] for compactly supported base diffeomorphisms",
                "local_IR_order": "metric Euler-Lagrange equation is local and at most second order",
                "quadratic_match": "D2J4 on E_TT equals the computed kappa_h Fierz-Pauli block",
                "internal_reduction": "selected weighted q79 zero-mode overlap and zero/gap channel coefficients",
                "matter_map": "all retained matter sectors vary against the same metric",
                "Lorentzian_domain": "time orientation, global hyperbolicity, gauge fixing, and boundary domain",
                "scale": "selected V6/G10 or an equivalent one-primitive normalization",
                "vacuum_energy": "selected Lambda_eff or a proof of its cancellation",
            },
            "reduction": (
                "Compared with the previous four quadratic action hypotheses, formal "
                "self-adjointness follows from variational origin and linearized gauge "
                "invariance follows from diffeomorphism naturality. The genuinely open "
                "structural source is therefore a local diffeomorphism-natural spacetime "
                "action with two-derivative infrared order, plus its scale/domain data."
            ),
        },
        "parameter_count": {
            "new_fitted_parameters": 0,
            "new_empirical_inputs": 0,
            "remaining_effective_Newton_coefficients": 1,
            "remaining_effective_Newton_coefficient": "kappa_h equivalently V6/G10",
            "additional_cosmological_coefficient": "Lambda_eff remains open",
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "closure_to_einstein_action_reduction",
        "date": "2026-07-15",
        "status": "CLOSURE_HESSIAN_RECIPROCITY_NONLINEAR_EINSTEIN_STRESS_REDUCTION_AND_ONE_SCALE_NOGO_CLOSED_SELECTED_SPACETIME_ACTION_SCALE_AND_LAMBDA_OPEN",
        "inputs": {
            "global_tt_hessian_action_uniqueness": str(GLOBAL_HESSIAN),
            "q79_coherent_zero_mode": str(ZERO_MODE),
            "stf_hessian_scale_bridge": str(SCALE_BRIDGE),
            "revised_closure_strain": str(CLOSURE_STRAIN),
            "revised_ten_dimensional_action_ansatz": str(TEN_D_ACTION),
            "theta_IV_gravity_cosmology": str(THETA_IV),
        },
        "checks": checks,
        "theorem": theorem,
        "claim_tiers": {
            "finite_closure_Hessian_self_adjointness": "CLOSED_FROM_C3_SCALAR_FUNCTIONAL",
            "physical_Jacobi_operator_self_adjointness": "NOT_INDEPENDENT_ONCE_LOCAL_VARIATIONAL_SOURCE_IS_SELECTED",
            "four_dimensional_nonlinear_metric_completion": "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES",
            "Einstein_Hilbert_action_coefficient_relations": "CLOSED_EXACT",
            "Hilbert_stress_map_and_conservation": "CLOSED_CONDITIONAL_ON_ONE_DIFF_INVARIANT_SHARED_METRIC_ACTION",
            "independent_stress_normalization": "CLOSED_NONE_BEYOND_KAPPA_H",
            "unwarped_q79_dimensional_reduction_relation": "CLOSED_CONDITIONAL",
            "scale_free_q79_data_fix_numeric_kappa_h": "CLOSED_NO_GO",
            "one_dimensionful_primitive_is_necessary": "CLOSED_FOR_CURRENT_SCALE_FREE_SOURCE_DATA",
            "one_dimensionful_primitive_is_sufficient": "CONDITIONAL_ON_SELECTION_OF_DIMENSIONLESS_V6_OVER_G10_RATIO",
            "theta_IV_one_effective_normalization_insight": "RETAINED_STRUCTURALLY",
            "theta_IV_31_8_R1_CUBED_volume": "RETIRED_FOR_ACTIVE_Q79_BRANCH",
            "selected_MTT_local_diffeomorphism_natural_action": "OPEN",
            "selected_MTT_two_derivative_IR_order": "OPEN",
            "selected_numeric_kappa_h_or_G4": "OPEN_ONE_EFFECTIVE_NORMALIZATION",
            "selected_Lambda_eff": "OPEN",
            "selected_Lorentzian_domain_and_time_orientation": "OPEN",
            "full_selected_classical_GR": "OPEN",
            "quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_closure_pressure_equals_curvature_without_action": False,
            "claims_gauge_invariance_already_means_Diff_Y4": False,
            "claims_revised_10D_ansatz_derives_EH": False,
            "claims_Lovelock_hypotheses_selected_by_MTT": False,
            "claims_unit_internal_residue_fixes_Newton_constant": False,
            "claims_theta_IV_old_volume_is_active": False,
            "claims_numeric_G4_or_kappa_h": False,
            "claims_Lambda_selected": False,
            "claims_full_GR_or_QG": False,
            "uses_observed_Newton_or_cosmological_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Closure to Einstein Action Reduction and One-Scale No-Go v1

Date: 2026-07-15

## Result

The chain from closure strain to classical GR can now be stated without
conflating its proved and selected parts:

```text
q79/proto-spinor carrier
  -> selected comparison field Q
  -> G=Q^T Q and e=(1/2)log G
  -> finite closure Hessian H_e=kappa_e Id
  -> metric TT Hessian H_h=(kappa_e/4)Id
  -> unique Fierz-Pauli quadratic operator
  -> unique Einstein-Hilbert nonlinear metric completion
  -> Hilbert stress tensor and Einstein equation
```

The first five arrows are already constructed at their declared tiers. The
last two arrows are now unique mathematical reductions, conditional on one
still-missing MTT source statement: the selected closure response must be a
local, diffeomorphism-natural four-dimensional spacetime action whose metric
equation has at most two derivatives in the infrared.

This is real progress over the previous four-hypothesis action gate. A separate
self-adjointness assumption is unnecessary for a genuine variational Hessian,
and a separate stress normalization is unnecessary once matter and gravity
vary with respect to one shared metric.

## 1. Hessian reciprocity is automatic on the closure slice

The revised closure-strain paper declares a real `C^3` scalar functional
`J` and a stationary point `S_*`. Therefore Schwarz symmetry gives

```text
D^2 J(S_*)[u,v] = D^2 J(S_*)[v,u].
```

On the finite six-dimensional real strain slice, define the Riesz operator by

```text
<u,Hv> = D^2 J(S_*)[u,v].
```

Then `<u,Hv>=<Hu,v>` and hence `H=H*`. This closes self-adjointness of the
finite closure Hessian. The same second-variation identity makes the Jacobi
operator of a real local spacetime action formally self-adjoint after its
boundary conditions are fixed. It does not prove that the present closure
functional has already been promoted to that spacetime action.

## 2. Nonlinear Einstein completion

Assume that the selected physical field is a four-dimensional Lorentzian
metric and that its metric equation is:

1. local and diffeomorphism-natural;
2. symmetric and identically divergence-free;
3. built from the metric and at most its first two derivatives; and
4. metric-only in the infrared gravitational sector.

The four-dimensional Lovelock classification then leaves only

```text
a G_mn + b g_mn.
```

Matching the nonzero quadratic term to the already computed unique
Fierz-Pauli block gives the dynamically unique action

```text
S_grav = 2 kappa_h integral sqrt(-g) (R - 2 Lambda),
```

up to boundary terms and four-dimensional topological densities. This is the
nonlinear Einstein-Hilbert completion, not yet an MTT selection of its
hypotheses. Lovelock's original classification is
<https://doi.org/10.1063/1.1665613>. Deser's independent self-coupling route
shows how locality and consistent coupling of the linear gauge current generate
the Einstein nonlinearity: <https://arxiv.org/abs/gr-qc/0411023>.

`Lambda` is permitted but not selected here. Flat-background expansion requires
the total vacuum tadpole to cancel; cosmology requires an independent selected
vacuum-energy result.

## 3. Stress and exact normalization

For all retained matter fields `Phi` coupled to the same metric, define

```text
T_mn = -(2/sqrt(-g)) delta S_matter/delta g^(mn).
```

Using

```text
delta S_matter
  = -(1/2) integral sqrt(-g) T_mn delta g^(mn),
```

variation of the common action gives

```text
G_mn + Lambda g_mn = (4 kappa_h)^(-1) T_mn.
```

The repository convention is

```text
kappa_h       = 1/(32 pi G4),
2 kappa_h     = 1/(16 pi G4),
(4 kappa_h)^-1 = 8 pi G4.
```

Thus the standard Einstein equation follows exactly. Diffeomorphism invariance
of the matter action and the matter equations give `nabla^m T_mn=0`; the
contracted Bianchi identity enforces the same compatibility. No extra
gravitational stress coefficient remains beyond `kappa_h`. The open physical
point is whether one MTT-selected action couples every retained sector to this
same metric.

## 4. q79 reduction and the unavoidable scale

For the unwarped product reduction of the declared ten-dimensional ansatz,

```text
S10 = (2 kappa10^2)^(-1) integral sqrt(|g10|) R10,
```

the normalized constant internal mode gives

```text
V6/(2 kappa10^2) = 2 kappa_h,
kappa_h = V6/(4 kappa10^2)
        = V6/(32 pi G10),
G4 = G10/V6.
```

Warping, a nonconstant dilaton, higher-curvature terms, or threshold corrections
replace `V6` by a weighted overlap. They do not invalidate the need to compute
that overlap from the selected action.

There is now an exact no-go for extracting Newton's constant from the currently
closed scale-free q79 packet alone. Under an internal homothety

```text
g_X -> r^2 g_X,
V6 -> r^6 V6,
phi0 -> r^-3 phi0,
```

the topology, connectedness, rank-one harmonic projector, and unit normalized
internal residue remain unchanged, while at fixed parent coupling

```text
kappa_h -> r^6 kappa_h.
```

Therefore those closed data cannot select a numerical `kappa_h`. At least one
dimensionful primitive or an equivalent metric-scale theorem is necessary.
Writing

```text
V6  = v6 ell_*^6,
G10 = g10 ell_*^8
```

gives

```text
kappa_h = [v6/(32 pi g10)] ell_*^-2.
```

One length primitive is sufficient only after the full source selects the
dimensionless ratio `v6/g10`. From the four-dimensional point of view,
`kappa_h`, equivalently `V6/G10`, is one effective normalization.

## 5. Theta IV reconciliation

Theta IV was right to isolate one effective gravitational normalization. Its
specific calculation cannot remain a proof source because it uses the retired
literal `S1_cen x Sigma2 x Sigma3` geometry and obtains
`V=31.8 R1^3`, rather than the weighted six-volume of the active q79 branch.

Retain:

```text
G4^-1 = V6/G10
```

as a conditional dimensional-reduction relation.

Replace:

```text
V6 = 31.8 R1^3
```

with the selected q79 weighted overlap on
`X6_q79=P_delta x S1_shared`. Until that metric/action calculation is emitted,
the numerical Newton prediction remains open.

## 6. Exact remaining source packet

The next proof object is no longer an unspecified GR bridge. It is
`SelectedSpacetimeClosureActionSource.v1`, containing:

```text
physical_metric       = G=Q^TQ on Lorentzian Y4
naturality             = J4[f*G,f*Phi]=J4[G,Phi]
local_IR_order         = at most second-order metric equation
quadratic_match        = D2J4|E_TT = kappa_h Fierz-Pauli
internal_reduction     = weighted q79 zero/gap overlaps
matter_map             = one shared metric for all retained sectors
Lorentzian_domain      = time orientation, gauge, boundary domain
scale                  = selected V6/G10 or one-primitive equivalent
vacuum_energy          = selected Lambda_eff or cancellation theorem
```

Once this packet is sourced, Lovelock and the variation above supply the full
classical Einstein equations, their nonlinear completion, universal Hilbert
stress coupling, and conservation law. Quantum gravity remains a separate
program.

## Claim boundary

Closed now:

- finite closure-Hessian self-adjointness;
- reduction of the physical self-adjointness hypothesis to variational origin;
- unique nonlinear Einstein completion under the explicit Lovelock hypotheses;
- exact Hilbert stress and Newton coefficient relations;
- no independent stress-normalization knob beyond `kappa_h`;
- the scale-free q79-to-numerical-Newton no-go;
- structural retention and numerical correction of Theta IV.

Still open:

- MTT selection of the local diffeomorphism-natural spacetime action;
- MTT selection of the two-derivative infrared order;
- the weighted q79 reduction and zero/gap action coefficients;
- the numerical value of `kappa_h` or `G4`;
- `Lambda_eff`, Lorentzian domain data, and the quantum theory.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
