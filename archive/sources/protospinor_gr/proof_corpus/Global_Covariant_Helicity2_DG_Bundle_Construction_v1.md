# Global Covariant Helicity-2 DG Bundle Construction v1

Date: 2026-07-15

## Associated-bundle construction

Let `P_perp->S2` be the oriented transverse-frame `SO(2)` principal bundle and
let `V2=R2` carry the weight-two action

```text
R_2(theta)=rotation(2 theta).
```

At `theta=2pi/64`, this is exactly the real `k=2/k=62` Fourier representation
already used by the finite `Z64` source. Therefore

```text
E_TT=P_perp x_{SO(2)} V2
```

is the correct global home of those local two-component rows. It has Chern
number `-4`; the topology is retained rather than incorrectly trivialized.

## Global TT projector

For a unit direction `n`, set `P_n=I-nn^T` and

```text
T_n(S)=P_n S P_n-(1/2)tr(P_n S P_n)P_n.
```

The executable checks show that `T_n` has rank two in every tested fiber, is
transverse and trace-free, and satisfies

```text
T_{Rn}(R S R^T)=R T_n(S) R^T.
```

It is therefore a global `SO(3)`-equivariant bundle map. At the north-pole
frame it recovers the existing `e_plus,e_cross` basis exactly.

## Globalized DG and exact support

The local Fourier plane and physical TT fiber are the same weight-two
representation. Passing to associated bundles turns the local intertwiner into
a global bundle isomorphism. The literal metric derivative is fiberwise twice
this isomorphism; half-log strain is once it.

Tensor with the selected internal `|d_*>` factor. The exact finite projector
acts on that factor and identity on `E_TT`, so

```text
Pi_exact64 DG_global^*P_TT=DG_global^*P_TT
```

holds fiberwise and the normalized internal pole remains `lambda=15`.

This construction is parameter-free. It closes the global geometric
covariantization of the explicit `DG`, but not selection by the Lorentzian MTT
action, stress-energy coupling, or massless graviton dynamics.

Current status:

```text
GLOBAL_COVARIANT_HELICITY2_DG_BUNDLE_CONSTRUCTED_EXACT_SUPPORT_CLOSED_SELECTED_ACTION_STRESS_LORENTZIAN_OPEN
```
