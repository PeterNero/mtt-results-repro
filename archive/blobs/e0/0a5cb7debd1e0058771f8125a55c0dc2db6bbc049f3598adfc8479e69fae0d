# World-in-World Z64 Metric Source Map v1

## The missing object is now explicit

Let `c2,s2` be the normalized real `k=2/k=62` Fourier pair in `R[Z64]`, and
let `e_plus,e_cross` be the normalized spatial TT tensors for a selected wave
direction. For an exact-branch source coefficient vector `psi`, define

```text
x_plus(psi)  = <c2,psi>,
x_cross(psi) = <s2,psi>,
S(psi)       = x_plus e_plus + x_cross e_cross,
Q(psi)       = exp(S(psi)),
G(psi)       = Q(psi)^T Q(psi) = exp(2 S(psi)).
```

This is an actual nonlinear world-in-world metric observable. At `psi_*=0`,

```text
DG(0)[delta psi] = 2(<c2,delta psi> e_plus
                     + <s2,delta psi> e_cross).
```

Consequently,

```text
DG(0)^* e_plus  = 2 c2,
DG(0)^* e_cross = 2 s2,
Pi_exact64 DG(0)^* P_TT = DG(0)^* P_TT.
```

The support identity is now calculated for this displayed realization. It is
not obtained by writing `B0^*P_TT := U_TT` and then setting a Boolean source
acceptance flag.

## Normalization found, not assumed

With orthonormal Frobenius and group-algebra bases,

```text
B_metric^* P_TT = U_TT (2 I2).
```

For the half-log metric, which is exactly the closure strain coordinate,

```text
B_strain^* P_TT = U_TT I2.
```

Thus the earlier `C=I2` packet is correct for logarithmic strain. The literal
metric derivative has `C=2I2`. This factor changes the propagator residue but
not its selected eigenvalue or pole location: the exact internal support still
has `lambda_*=15` in normalized branch units.

## Why the Fourier row is essentially forced

The audit solves the real intertwining equation between the `Z64` shift and
spin-2 rotation. Its solution space has dimension two: overall scale and
polarization phase. Isometry fixes the scale. Anchoring `c2` to plus and `s2`
to cross fixes the phase, which is a polarization-basis convention rather than
a measured constant. No fitted continuous physical parameter remains.

## Exact status

Closed for the constructed realization:

- a nonlinear `G(Psi)` and its derivative;
- exact TT adjoint rows and rank;
- exact `Z64` support and helicity-2 equivariance;
- the normalization matrices `2I2` and `I2`;
- the normalized internal pole support at `15`.

Still open as a theorem about MTT selection:

- prove that the exact `Z64` shared-circle generator is the same action as the
  transverse-frame orientation circle;
- prove that the selected MTT action chooses this induced metric observable;
- extend the q79 carrier map through branching and the selected HYM connection;
- derive dimensionful Newton/Planck and stress-response normalization.

So this is an explicit zero-fit realization and a genuine computation of
`DG`. It is not yet a uniqueness theorem saying every admissible MTT branch
must select this realization.
