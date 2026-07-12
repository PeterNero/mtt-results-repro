# BTT Packet Partial Fill: Weight and BRST Theorem v1

## Closed Now

Two fields in the selected `B_TT` packet are now closed.

1. The TT plus/cross plane has spin/helicity weight `2`. Under a transverse
   rotation by angle `theta`, the real polarization basis transforms by
   `R(theta)=[[cos(2 theta), sin(2 theta)],[-sin(2 theta), cos(2 theta)]]`.
   This is exactly the real weight-2 character action.

2. The `B_TT` restriction is compatible with the BRST/diffeomorphism quotient
   at the level supported by the corpus: QG works on physical TT two-point
   functions, pure-gauge directions are removed by BV gauge fixing, and the
   finite-projection paper requires weak-field gravitational filters to act on
   physical spin-2 TT data rather than diffeomorphism modes.

## Still Open

This does not yet compute the exact internal image of

```text
B_TT = DG(Psi*) Pi_coh |_{TT}
```

inside the retained exact branch `H0 tensor K64 tensor C|d_*>`, and it does not
yet prove that the TT central-circle angle is the same sampled angle used by the
exact `Z64` carrier. Therefore it still does not unconditionally prove
`lambda_GR,TT=15`.

## Remaining Minimal Gate

Compute or source the image of `DG(Psi*) Pi_coh` on the TT plus/cross quotient.
The two fields closed here mean the remaining check is narrower:

```text
B_TT nonzero,
B_TT image lies in H0 tensor K64 tensor C|d_*>,
same central-circle angle as the retained Z64 carrier.
```
