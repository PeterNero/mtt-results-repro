# Closure Anholonomy Teleparallel Einstein Bridge v1

Date: 2026-07-15

## Result

The direct classical-gravity route is now more concrete. The scalar closure
potential `J(S)` cannot generate the massless graviton kinetic term: if its
coframe dependence is algebraic, its Hessian has an order-zero principal
symbol, while the already certified Fierz-Pauli block has principal symbol
`kappa_h p^2 P_TT`. If the strain is an independent scalar, its sigma-model
kinetic term contributes matter stress but still does not become a pure metric
kinetic term around a constant aligned background.

The correct mathematical version of "gravity is non-closure pressure" is
instead coframe anholonomy:

```text
theta^0 = N dt,
theta^a = E^a_i (dx^i + N^i dt),
T^a = d theta^a + omega^a_b wedge theta^b.
```

Here `T^a` is literal non-closure of the coframe. The local comparison field
`Q_WW=RU` already supplies a candidate spatial triad and
`G3=Q_WW^T Q_WW`; it does not yet supply the full Lorentzian coframe, lapse,
shift, time orientation, or inertial connection.

## Exact Einstein bridge

For a flat metric-compatible teleparallel connection, define

```text
I1 = T^{abc} T_{abc},
I2 = T^{abc} T_{bac},
I3 = T^a T_a,
T_TEGR = (1/4) I1 + (1/2) I2 - I3.
```

The three quadratic invariants are independent; the exact witness matrix used
by the verifier has determinant `-4`. The geometric identity is

```text
e R(LC) = -e T_TEGR + 2 partial_mu(e T^mu).
```

Consequently, in the repository convention,

```text
S_EH = 2 kappa_h integral e (R - 2 Lambda)
```

is equal, up to the displayed boundary term, to

```text
S_TEGR = -2 kappa_h integral e T_TEGR
         -4 kappa_h Lambda integral e.
```

Their bulk variations therefore give exactly the same equation,

```text
G_mn + Lambda g_mn
  = (4 kappa_h)^(-1) T_mn
  = 8 pi G4 T_mn.
```

This is not merely a weak-field analogy. Once the coframe, inertial connection,
boundary conditions, and common matter coupling are supplied, it is an exact
nonlinear reformulation of classical GR. The standard identity and field
equivalence are reviewed in <https://arxiv.org/abs/1303.3897>; a constitutive
teleparallel formulation is developed in <https://arxiv.org/abs/1611.05759>.

There is no remaining topological existence problem once the corrected action
paper's declared spacetime inputs are admitted. Smooth global hyperbolicity
gives `Y4` diffeomorphic to `R x Sigma3`; every orientable smooth
three-manifold is parallelizable. Hence `TY4` is trivial and a global
Lorentzian coframe exists. Defining the frame to be parallel constructs a flat
metric-compatible Weitzenbock connection whose torsion is its anholonomy.
Lapse and shift are varied ADM multiplier/gauge fields, not additional fitted
constants. This closes conditional existence under the imported v4 input; it
does not identify the selected MTT `Q_WW` with that coframe. See
<https://arxiv.org/abs/gr-qc/0306108> and
<https://arxiv.org/abs/2207.12149>.

The TEGR vector is also not an independent choice once the action is required
to descend to MTT's metric observable. The exact quotient

```text
Q_WW -> R(x) Q_WW,
G3=Q_WW^T Q_WW -> G3
```

makes local frame orientation invisible. If the coframe action has no
independent frame/connection modes and descends, modulo a boundary, to a local
metric action with at-most-second-order equations, Lovelock forces the metric
bulk action to be Einstein-Hilbert plus `Lambda`. The independent torsion basis
and the identity above then force `(1/4,1/2,-1)`, while the existing TT Hessian
fixes its overall coefficient to `-2 kappa_h`. Thus the remaining TEGR source
problem is not a new three-parameter fit.

There is now also a direct exact selector for the no-extra-frame-mode clause.
For the general parity-even quadratic action

```text
T_c=c1 I1+c2 I2+c3 I3,
```

take a pure local Lorentz perturbation `A_ab=-A_ba` around Minkowski space.
It changes the coframe while leaving the metric unchanged at first order. At
the witness momentum `p=(1,0,0,0)`, the three boost-like modes have bulk symbol

```text
2 c1+c2+c3,
```

and the three rotation-like modes have bulk symbol

```text
-4 c1+2 c2.
```

Closure-neutrality of all fixed-metric frame representatives sets both to
zero. The exact rank-two constraint matrix has null ray

```text
(c1,c2,c3)=lambda(1/4,1/2,-1).
```

The TEGR pure-frame residual is exactly zero, and the boundary identity proves
nonlinear sufficiency. Thus the only remaining constitutive question is whether
MTT identifies fixed-metric teleparallel representatives as one
closure-neutrality fiber. Once that structural statement is supplied, TEGR is
forced directly.

The local coframe lift itself is explicit. Select an oriented Cauchy embedding
`i:B->Y4` and type the outer bundle as `TP=TB`. On the admissible invertible
branch, `Q_WW:TB->TI` then identifies `TI` automatically with the oriented
internal spatial frame bundle; `TI` is not another independent choice. In
local frames,

```text
theta^0=N dt,
theta^a=Q_WW^a_i(dx^i+N^i dt)
```

gives

```text
g_00=-N^2+h_ij N^i N^j,
g_0i=h_ij N^j,
g_ij=h_ij=(Q_WW^T Q_WW)_ij,
det(e)=N det(Q_WW),
det(g)=-N^2 det(Q_WW)^2.
```

The symbolic matrix and determinant residuals are exactly zero. Lapse and
shift remain varied constraint fields rather than fit coordinates.

Even the transition cocycle is already the correct one. The revised
world-in-world paper defines `Q_WW` globally in `Hom(TP,TI)` and gives

```text
Q_j=g_I,ij Q_i g_P,ij^(-1).
```

After selecting the Cauchy support and `TP=TB`, this is exactly the
tetrad/solder-form transformation law. On the admissible `GL+(3)` domain,
`Q_WW` is a bundle isomorphism, `TI` is identified automatically, and
`h=Q_WW^* delta` is global. Thus cocycle globalization and the inner-bundle
typing are closed conditional on one outer-support identification. The strict
remaining source clause is only MTT selection of the Cauchy embedding and
`TP=TB`; rank and dimension matching do not prove it.

## Exact symbolic check

For a diagonal Bianchi-I coframe with directional Hubble variables `H1,H2,H3`,
the script obtains

```text
I1 = -2(H1^2+H2^2+H3^2),
I2 = -(H1^2+H2^2+H3^2),
I3 = -(H1+H2+H3)^2,
T_TEGR = 2(H1 H2+H1 H3+H2 H3).
```

It then verifies symbolically, with residual exactly zero,

```text
R_LC + T_TEGR - B = 0,
B = 2/e partial_t[e(H1+H2+H3)].
```

## What this closes

- `J(S)` alone is excluded as the source of the graviton kinetic term.
- The old implication `grad S != 0 => curvature => Einstein` is excluded.
- Coframe torsion gives an exact, typed non-closure tensor.
- The unique TEGR coefficient vector in the independent quadratic basis is
  selected exactly by pure-frame closure-neutrality; exact Einstein equivalence
  proves nonlinear sufficiency.
- The resulting action gives all nonlinear classical Einstein equations and
  the same Hilbert stress coupling, up to boundary data.
- No new fitted number is introduced. The same one gravitational scale
  `kappa_h` and the separate vacuum coordinate `Lambda_eff` remain.

## What remains selected rather than merely constructed

The direct action exit is no longer an unspecified action search. Its remaining
source theorem has three explicit clauses:

1. Select an oriented Cauchy embedding `i:B->Y4` and the outer tangent typing
   `TP=TB`. Invertible `Q_WW` then identifies `TI` automatically. The local ADM
   map, transition cocycle, global coframe existence, and flat-connection
   construction are already closed once this one support identification and
   the declared v4 spacetime hypotheses are admitted.
2. Prove that fixed-metric teleparallel representatives form one MTT
   closure-neutrality fiber. The exact pure-frame symbol then forces the TEGR
   vector `(1/4,1/2,-1)` and the boundary identity supplies full nonlinear
   metric descent; there is no independent constitutive choice.
3. Derive from that same action the zero-mode/gapped-channel weights, the one
   effective `kappa_h` normalization, and `Lambda_eff`.

The fixed-point heat kernel remains useful for projection, damping, and quantum
corrections. It does not by functional calculus alone select the coframe or the
TEGR constitutive law. The spectral-action route therefore remains a separate
candidate for ultraviolet completion, while this teleparallel route supplies
the cleanest direct classical bridge.
