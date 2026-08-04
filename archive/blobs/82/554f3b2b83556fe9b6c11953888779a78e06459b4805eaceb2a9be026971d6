# MTT Selected StromingerThresholdOperatorValue or MetrologyUnitSource v1

Status: `MTT_SELECTED_STROMINGERTHRESHOLDOPERATORVALUE_OR_METROLOGYUNITSOURCE_BUILT_PARTIAL_TORSIONAL_GEOMETRY_METROLOGY_PRIMITIVE_STRICT_VALUES_OPEN`.

## Result

The strict PEW source-value request has now been split into its two legal value
routes and checked against the latest cross-repo results.

### Strominger / HYM Threshold Route

New support imported from Qa/SU3:

```text
selected radii r1,r2,r3            : 4.440528182269818, 4.440528182269818, 4.440028979122532
A = r3/(r1*r2)                     : 0.22517311887007765
8*A^2                              : 0.40562346769342494
relative one-form weights          : imported
metric logdet samples monotone      : true
```

Accepted final threshold/torsion rows:

```text
Strominger threshold finite part    : 0
local-system torsion finite part    : 0
selected mu/moduli row              : 0
strict P_EW row                     : 0
direct K_threshold.Omega_H.lambda   : 0
```

So the route is stronger than before, but still not closed.  The real missing
object is now precise: `E_Qa`, source-derived OU weights, or a direct finite
heat/zeta/torsion determinant in the selected fixed-gauge domain.

### Metrology Route

The constants handoff supplies a coherent one-universal-primitive option
(`L0` or `E0`) with internal coefficients:

```text
tau_int                             : 0.40698621549433234
sqrt_tau_int                        : 0.6379547127299338
Omega0/sqrt(alpha_phys)             : 1.5675093859261626
```

This is available for a counted minimal-parameter lane, but it is not strict
no-knob closure: the same-branch absolute scale symmetry is still active.

## Next

Next artifact: `MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1`.

It must emit one of:

```text
1. torsional Weitzenbock endomorphism E_Qa
2. source-derived OU gamma_nk weights
3. direct finite heat/zeta/torsion determinant
4. strict physical rod/clock/action unit source
```
