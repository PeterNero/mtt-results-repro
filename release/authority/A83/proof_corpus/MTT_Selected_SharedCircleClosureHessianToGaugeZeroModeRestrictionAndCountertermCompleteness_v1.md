# MTT Selected Shared-Circle Closure Hessian to Gauge-Zero-Mode Restriction and Counterterm Completeness v1

## Exact covariant restriction

A82 supplies the positive finite closure Hessian `H_cl`. With the already selected proper time and
C1 density, functional calculus gives

```text
W_kin = exp(-tau_int H_cl) Phi_C1^+.
```

The resulting `18x18` family/sector density is positive definite; its least eigenvalue is
`0.0436756347304`. Since `Phi_C1^+` acts on the family factor and the selected gauge
representation is `I3_family tensor rho_16`, it commutes with the gauge action. The finite quadratic
covariantization

```text
S_gauge^(2)[F] = (1/2) sum_ab Tr_HF(W_kin T_a T_b) <F^a,F^b>
```

has Hessian exactly equal to A65's `K_ab`. It reproduces A80's three kinetic rows with residual
`0.000e+00` and its ratios with residual
`0.000e+00`. The mathematical restriction is closed.

## Why physical identity does not follow automatically

ProtoSpinor explicitly defines its closure cost as bookkeeping geometry, **not a Lagrangian**. The
spectral-shadow paper obtains a heat action only after assuming that the coherent fixed-point action has
a proper-time representation. A67 is also explicit that its C1 density is closed at an accepted
source-axiom tier rather than at strict unpatched no-knob tier. Finally, A75 proves that setting a finite
determinant to zero at the origin does not eliminate two allowed relative linear matching terms.

Therefore `H_cl -> W_kin -> S_gauge` is a fully executed canonical map, but current MTT premises do not
yet say that it is the physical map. This is a logical obstruction, not a missing calculation.

## Minimal sufficient premise

The exact remaining premise is:

> ClosureShadowGaugeActionAxiom. On a selected finite coherent sector with positive closure Hessian H_cl, selected C1 density Phi_C1^+, and selected proper time tau_int, the quadratic physical gauge shadow at the finite matching point is S_gauge^(2)=(1/2) Tr_HF(exp(-tau_int H_cl) Phi_C1^+ F^2). No additional sector-relative gauge-quadratic functional is present at that matching point; one common overall normalization is the already counted P_EW primitive.

It has two logically necessary clauses: the heat-shadow map and finite matching completeness. It adds
zero continuous or discrete numerical parameters and no new physical primitive beyond the already
counted `P_EW`.

Under this one structural premise, all three gauge rows emit, both relative A75 counterterm coordinates
are fixed to zero at the selected matching point, and the A82 partition-invariant spectator class is
complete. Unconditionally, strict gauge values remain zero because the premise is written and tested but
not derived or adopted here. The existing ratio candidate also remains a posteriori rather than an
independent prediction; it needs a held-out test after the action is frozen.

Next artifact: `MTT_Selected_ClosureShadowGaugeActionAxiomDerivation_or_ExplicitAdoptionAndHeldOutValidation_v1`.
