# BTT Adjoint Shape Map Typing Theorem v1

## Correction

The source-defined metric shape map is

```text
B = DG(Psi*) Pi_coh.
```

This maps coherent/internal configurations to metric fluctuations. Therefore the
previous image gate

```text
B_TT : span{TT_plus,TT_cross} -> H0 tensor K64 tensor C|d_*>
```

is not the correctly typed object unless `B_TT` is explicitly interpreted as a
pullback. The correct operator is the adjoint/co-shape support map:

```text
J_TT := Pi_exact64 B^* P_TT.
```

## Closed Now

The TT coupling is nonzero at the adjoint-support level. The QG source defines
the physical graviton propagator as

```text
Delta_prop = B A^{-1} B^*
```

and the TT quadratic kernel as its inverse. On the physical TT quotient, this
requires nontrivial `B^* P_TT` support. Together with the previous packet, the
spin-2 weight and BRST/diffeomorphism compatibility are closed.

The exact `Z64` branch is also available and coherent:

```text
P_CP,64 <= Pi_coh,
[L,Pi_coh]=0,
d_*=(2,2,2,2,2),
C(d_*)=15.
```

## Still Open

The final support identity is not sourced:

```text
Pi_exact64 B^* P_TT = B^* P_TT,
```

nor is the same sampled central-circle angle between `J_TT` and the exact `Z64`
shift sourced. If those two fields close, the already proved uniqueness theorem
forces

```text
support(J_TT)=|d_*> tensor span{c_2,s_2}
lambda_GR,TT=15
```

in normalized internal exact-branch units.
