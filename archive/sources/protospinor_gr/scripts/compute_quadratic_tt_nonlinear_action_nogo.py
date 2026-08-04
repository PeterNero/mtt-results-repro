from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = ROOT.parent / "mtt-results-repro" / "release" / "authority"

ACTION_REDUCTION = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
A51 = (
    AUTHORITY
    / "A51"
    / "certificates"
    / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure_certificate.json"
)
A52 = (
    AUTHORITY
    / "A52"
    / "certificates"
    / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization_certificate.json"
)
A53 = (
    AUTHORITY
    / "A53"
    / "certificates"
    / "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure_certificate.json"
)
A51_PACKET = (
    AUTHORITY
    / "A51"
    / "candidate_data"
    / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure"
    / "finite_inner_fluctuation_and_spectral_traces.packet.json"
)

OUT_CERT = ROOT / "certificates" / "quadratic_tt_nonlinear_action_nogo_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Quadratic_TT_Data_Nonlinear_Action_NoGo_and_Spectral_Exit_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    action = load(ACTION_REDUCTION)
    a51 = load(A51)
    a52 = load(A52)
    a53 = load(A53)
    a51_packet = load(A51_PACKET)

    # Around flat space, Weyl(g(epsilon)) starts at order epsilon. Therefore
    # sqrt(-g) Weyl^3 starts at order epsilon^3. The deformation has vanishing
    # value, first variation, and Hessian at the flat background, while its
    # cubic vertex is generically nonzero.
    weyl_order = 1
    volume_density_order = 0
    cubic_deformation_order = volume_density_order + 3 * weyl_order
    derivatives_invisible_to_deformation = list(range(cubic_deformation_order))
    first_visible_derivative = cubic_deformation_order

    operator_content = a51_packet["bosonic_action_interface"][
        "generated_after_standard_product_triple_heat_kernel_theorem"
    ]
    gravitational_row = next(
        row for row in operator_content if "Einstein-Hilbert" in row
    )

    checks = {
        "conditional_Einstein_reduction_is_available": (
            action["claim_tiers"]["four_dimensional_nonlinear_metric_completion"]
            == "CLOSED_UNIQUE_CONDITIONAL_ON_LOVELOCK_HYPOTHESES"
        ),
        "selected_two_derivative_IR_order_remains_open": (
            action["claim_tiers"]["selected_MTT_two_derivative_IR_order"] == "OPEN"
        ),
        "Weyl_tensor_begins_at_first_order_about_flat_space": weyl_order == 1,
        "Weyl_cubic_density_begins_at_third_order": cubic_deformation_order == 3,
        "value_first_and_second_variations_are_invisible": (
            derivatives_invisible_to_deformation == [0, 1, 2]
        ),
        "third_variation_can_distinguish_the_family": first_visible_derivative == 3,
        "A51_bosonic_operator_content_is_closed_via_standard_theorem": (
            a51["bosonic_SM_operator_content_closed_via_standard_heat_kernel_theorem"]
            is True
        ),
        "A51_contains_Einstein_and_Weyl_gravity": (
            "Einstein-Hilbert" in gravitational_row and "Weyl-curvature" in gravitational_row
        ),
        "A51_absolute_normalization_is_open": (
            a51["absolute_spectral_action_normalization_closed"] is False
        ),
        "A52_profile_product_interface_is_closed": (
            a52["profile_product_triple_interface_closed"] is True
        ),
        "A52_strict_Wick_rotation_is_open": (
            a52["strict_MTT_Wick_rotation_closed"] is False
        ),
        "A52_strict_cutoff_moments_are_open": (
            a52["strict_spectral_cutoff_moments_closed"] is False
        ),
        "A53_tau_internal_is_exact": a53["tau_int_exact_source_available"] is True,
        "A53_point_measure_is_not_selected": (
            a53["point_measure_selected_by_MTT"] is False
        ),
        "A53_strict_spectral_action_is_open": (
            a53["strict_spectral_action_closed"] is False
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "QuadraticTTDataDoNotSelectNonlinearActionTheorem",
        "background": "g(epsilon)=eta+epsilon h on a four-dimensional flat patch",
        "deformation_family": {
            "action": (
                "S_alpha=S_EH+(alpha/kappa_h) integral sqrt(-g) "
                "C_mn^rs C_rs^ab C_ab^mn"
            ),
            "alpha": "arbitrary dimensionless real coefficient",
            "uses_new_dimensionful_scale": False,
            "properties": [
                "local",
                "metric-only",
                "diffeomorphism-invariant",
                "parity-even",
                "higher-than-second-order metric equation for alpha nonzero",
            ],
        },
        "order_proof": {
            "Weyl_expansion": "C[g(epsilon)]=epsilon C1[h]+O(epsilon^2)",
            "density_expansion": (
                "sqrt(-g) C^3=epsilon^3 C1_mn^rs C1_rs^ab C1_ab^mn+O(epsilon^4)"
            ),
            "vanishing": [
                "Delta S_alpha[eta]=0",
                "D Delta S_alpha[eta]=0",
                "D2 Delta S_alpha[eta]=0",
            ],
            "generic_nonvanishing": (
                "D3 Delta S_alpha[eta] is proportional to alpha times the cubic "
                "linearized-Weyl invariant and is nonzero for generic perturbations."
            ),
        },
        "consequence": (
            "The selected metric map, global TT bundle, kappa_h, Fierz-Pauli Hessian, "
            "linearized diffeomorphism identity, and even full diffeomorphism invariance "
            "do not determine the nonlinear action. An infrared derivative-order/source "
            "theorem or equivalent suppression theorem is logically indispensable."
        ),
        "spectral_action_exit": {
            "why_it_is_relevant": (
                "A51-A53 provide a same-architecture route in which one product Dirac "
                "operator can generate SM matter and gravitational operator content."
            ),
            "currently_closed": [
                "A51 finite one-form execution and selected rank-four single-Higgs projection",
                "A51 bosonic operator content through the standard product-triple heat-kernel theorem",
                "A52 adopted-profile product-triple matter interface",
                "A53 exact tau_int=log(448)/15 and conditional one-atom moment sequence",
            ],
            "currently_open_or_conditional": [
                "MTT selection of the four-dimensional base Dirac geometry",
                "MTT Wick/Lorentzian reconstruction",
                "MTT selection of the cutoff function or proper-time measure and moments",
                "absolute Newton and vacuum-energy normalization",
                "source-derived gauge overlap metric at strict no-knob tier",
                "an infrared theorem controlling the Weyl-curvature and higher heat-kernel terms",
                "matching the spectral TT Hessian and q79 zero/gap channels to the computed kappa_h block",
            ],
            "important_difference": (
                "The standard spectral action contains Einstein-Hilbert plus Weyl "
                "gravity, not pure two-derivative GR. It is therefore a superset route. "
                "Recovering GR requires a selected low-energy truncation with an error "
                "or decoupling certificate; it cannot bypass the derivative-order gate."
            ),
            "primary_source": "https://arxiv.org/abs/hep-th/9606001",
        },
        "two_honest_exits": {
            "direct": {
                "name": "SelectedSpacetimeClosureActionSource.v1",
                "must_emit": (
                    "a real local diffeomorphism-natural metric action with at-most-"
                    "second-order infrared metric equations and the computed TT Hessian"
                ),
                "payoff": "Fierz-Pauli plus Lovelock gives Einstein-Hilbert and Hilbert stress",
            },
            "spectral_superset": {
                "name": "SelectedProductSpectralActionAndEinsteinIRLimit.v1",
                "must_emit": (
                    "base product triple, cutoff measure/moments, Lorentzian map, absolute "
                    "normalization, and a controlled Einstein infrared limit"
                ),
                "payoff": "one operator architecture can jointly host SM and gravity",
            },
            "forbidden_shortcut": (
                "infer the nonlinear action from the already closed quadratic TT data"
            ),
        },
        "parameter_count": {
            "counterfamily_new_dimensionful_parameters": 0,
            "counterfamily_free_dimensionless_coefficients": 1,
            "spectral_route_new_parameters_claimed_here": 0,
        },
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "quadratic_tt_nonlinear_action_nogo",
        "date": "2026-07-15",
        "status": "QUADRATIC_TT_TO_NONLINEAR_ACTION_SELECTION_NOGO_CLOSED_DIRECT_TWO_DERIVATIVE_AND_SPECTRAL_SUPERSET_EXITS_ISOLATED",
        "inputs": {
            "closure_to_einstein_action_reduction": str(ACTION_REDUCTION),
            "A51_finite_spectral_action": str(A51),
            "A52_product_triple_and_moments": str(A52),
            "A53_proper_time_measure": str(A53),
            "A51_operator_packet": str(A51_PACKET),
        },
        "checks": checks,
        "theorem": theorem,
        "claim_tiers": {
            "quadratic_TT_data_select_unique_nonlinear_action": "CLOSED_NO_GO",
            "explicit_same_Hessian_nonlinear_counterfamily": "CLOSED",
            "two_derivative_IR_clause_is_logically_indispensable": "CLOSED",
            "A51_spectral_bosonic_operator_content": "CLOSED_VIA_STANDARD_PRODUCT_TRIPLE_THEOREM",
            "spectral_action_is_pure_Einstein_gravity": "CLOSED_NO",
            "spectral_action_as_same_operator_SM_gravity_candidate": "CLOSED_ARCHITECTURALLY",
            "selected_MTT_product_spectral_action": "OPEN",
            "selected_Einstein_IR_limit_of_spectral_action": "OPEN",
            "direct_selected_spacetime_closure_action": "OPEN",
            "full_selected_classical_GR": "OPEN",
        },
        "guardrails": {
            "claims_quadratic_Hessian_fixes_nonlinear_vertices": False,
            "claims_diffeomorphism_invariance_alone_selects_EH": False,
            "claims_A51_selects_base_spacetime_geometry": False,
            "claims_A52_derives_Wick_rotation": False,
            "claims_A53_point_measure_is_selected": False,
            "claims_spectral_action_is_pure_two_derivative_GR": False,
            "claims_selected_MTT_action_closed": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Quadratic TT Data Nonlinear Action No-Go and Spectral Exit v1

Date: 2026-07-15

## Exact no-go

The computed `DG`, global helicity bundle, scalar TT Hessian, Fierz-Pauli
operator, and `kappa_h` relation do not select a unique nonlinear action.

On a flat background let

```text
g(epsilon)=eta+epsilon h
```

and define the diffeomorphism-invariant local family

```text
S_alpha
  = S_EH
  + (alpha/kappa_h) integral sqrt(-g)
      C_mn^rs C_rs^ab C_ab^mn,
```

where `alpha` is dimensionless. Since

```text
C[g(epsilon)] = epsilon C1[h] + O(epsilon^2),
```

the deformation starts at cubic order:

```text
sqrt(-g) C^3
  = epsilon^3 C1_mn^rs C1_rs^ab C1_ab^mn + O(epsilon^4).
```

Therefore its value, first variation, and second variation at flat space all
vanish. Every `S_alpha` has the same flat background equation and the same
Fierz-Pauli Hessian, but generic third variations and nonlinear graviton
vertices differ. The family introduces no new dimensionful scale because
`kappa_h^-1` has the required length-squared dimension.

This proves an exact independence result:

```text
quadratic TT closure + diffeomorphism invariance
  does not imply a unique nonlinear action.
```

The at-most-second-order infrared clause in the Lovelock reduction is therefore
essential. It cannot be inferred from the already computed Hessian.

## Spectral-action corpus audit

The latest SM authority packets provide a serious superset route:

- `A51` closes the finite one-form calculation, the selected rank-four
  single-Higgs projection, and the bosonic operator content via the standard
  product-triple heat-kernel theorem.
- `A52` closes the adopted-profile product-triple matter interface.
- `A53` supplies exact `tau_int=log(448)/15` and a positive one-atom moment
  sequence under a named minimal-support premise.

They do not yet select the gravitational action:

- `A51` leaves absolute spectral normalization open.
- `A52` imports rather than derives the Wick-rotated four-dimensional
  spacetime interface and leaves strict cutoff moments open.
- `A53` explicitly says the point measure is not selected by MTT and strict
  spectral-action closure remains open.

The distinction is physically important. The spectral action contains
cosmological, Einstein-Hilbert, Weyl-curvature, and nonminimal terms. The
original spectral-action paper likewise describes the result as the Standard
Model coupled to Einstein plus Weyl gravity:
<https://arxiv.org/abs/hep-th/9606001>.

Thus this route does not evade the infrared-order problem. It replaces a pure
two-derivative axiom with a stronger task: select the full product spectral
action and prove a controlled low-energy regime in which the Einstein term
dominates and the Weyl/higher terms have a quantified error.

## Two honest exits

### Direct closure-action exit

Construct `SelectedSpacetimeClosureActionSource.v1` with:

```text
G=Q^TQ,
local diffeomorphism naturality,
at-most-second-order infrared metric equation,
computed TT Hessian and q79 zero/gap reduction,
one shared metric for matter,
Lorentzian domain, kappa_h, and Lambda_eff.
```

The closed reciprocity, Fierz-Pauli, Lovelock, and Hilbert-stress reductions then
give classical Einstein gravity.

### Spectral superset exit

Construct `SelectedProductSpectralActionAndEinsteinIRLimit.v1` with:

```text
selected four-dimensional base Dirac geometry,
selected finite product triple,
selected cutoff/proper-time measure and moments,
Lorentzian/Wick reconstruction,
absolute Newton and vacuum normalization,
q79 zero/gap TT match,
controlled suppression of Weyl and higher terms.
```

This path is attractive because it can place the already closed finite-SM
operator content and gravity in one operator architecture. It is also the
harder analytic path because its Einstein limit must be proved, not declared.

## Frontier

Closed:

- explicit nonlinear counterfamily with identical quadratic TT data;
- no-go for inferring nonlinear GR from the Hessian alone;
- logical necessity of the derivative-order or suppression theorem;
- spectral action as a genuine same-operator SM/gravity architecture;
- exact classification of what A51-A53 do and do not select.

Open:

- direct MTT selection of the local two-derivative spacetime action; or
- selected product spectral action plus controlled Einstein infrared limit;
- numerical `kappa_h`, `Lambda_eff`, Lorentzian domain, and zero/gap fusion.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
