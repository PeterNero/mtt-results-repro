# Selected q79/Z64 to QWW Source Factorization v1

Date: 2026-07-15

## Exact source map

The branch-continuation theorem makes `J` a global rank-six isometric
isomorphism on the unique minimal full-monodromy q79 root stack. Therefore the
exact `Z64` TT plane has a unique q79 preimage. In the local q79 coordinates
`(a1,a2,a3;b1,b2,b3)`, define

```text
f_plus  = (1/sqrt(2),-1/sqrt(2),0;0,0,0),
f_cross = (0,0,0;0,0,1),
Phi_q79(psi)=<c2,psi>f_plus+<s2,psi>f_cross.
```

The exact lane projectors give

```text
f_plus  in A0, the rank-two diagonal-shape lane,
f_cross in A,  the rank-three off-diagonal-shear lane.
```

The rank-one scalar lane is absent on the physical TT quotient. This is not a
missing coordinate: trace is removed by the TT constraint.

## Complete factorization

The maps now compose without a prefilled matrix:

```text
exact Z64 k=2 plane
  -> Phi_q79
q79 A0+A source plane on the full-monodromy root stack
  -> J
S(psi)=<c2,psi>e_plus+<s2,psi>e_cross
  -> exp
Q_WW(psi)=exp(S(psi))
  -> pullback metric
G(psi)=Q_WW(psi)^T Q_WW(psi)=exp(2S(psi)).
```

Consequently

```text
DG(0)=2 J Phi_q79,
rank(Phi_q79)=2,
Pi_exact64 Phi_q79^*=Phi_q79^*,
Pi_exact64 DG(0)^*P_TT=DG(0)^*P_TT.
```

## Uniqueness

Each step has now been reduced to a universal or representation-theoretic
choice:

1. helicity two forces the real `k=2/k=62` plane in `R[Z64]`;
2. isometry fixes its scale and polarization phase is basis gauge;
3. the natural q79 `J` is unique and invertible on the minimal root stack;
4. logarithmic strain fixes the positive polar representative `Q_WW=exp(S)`;
5. the inner Euclidean metric fixes the pullback `G=Q_WW^T Q_WW`.

Thus the selected-branch source realization is unique up to polarization,
frame, and diffeomorphism gauge. It introduces zero fitted physical parameters.
The global construction uses associated weight-two bundles and does not equate
the flat internal shared line with the nontrivial global helicity line.

## Boundary

This closes the old q79/`Z64`-to-`Q_WW` map problem on the selected massless
helicity-two minimal-rootstack branch. Primitive MTT must still select that
root-stack Lorentzian physical branch. The flat finite-monodromy carrier also
has not yet been identified with the independently selected
inverse-Fourier-Mukai/HYM Hessian and overlap kernels. The rank-two physical TT
source is not claimed to emit all six off-shell strain coordinates.

Current status:

```text
SELECTED_Q79_Z64_QWW_TT_SOURCE_FACTORIZATION_CLOSED_UNIQUE_UP_TO_POLARIZATION_AND_FRAME_GAUGE_PRIMITIVE_ROOTSTACK_LORENTZIAN_BRANCH_AND_INVERSE_FOURIER_MUKAI_OPERATOR_IDENTITY_OPEN
```
