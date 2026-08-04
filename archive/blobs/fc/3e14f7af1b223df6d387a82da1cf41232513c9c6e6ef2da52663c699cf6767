# Actual Shape Map Factorization Reduction v1

## Result

The QG paper gives the decisive structural factorization:

```text
B = DG(Psi*) Pi_coh = exp(-tau0 E/2) B0 exp(-tau0 A_int/2).
```

Taking adjoints on the TT quotient gives:

```text
B^*P_TT = exp(-tau0 A_int/2) B0^* exp(-tau0 E/2) P_TT.
```

Therefore the final support problem reduces from the full dressed metric shape
map to the SPT core map `B0`.

## Theorem

If the core map satisfies

```text
B0^*P_TT = U_TT C
```

for the same-angle helicity-2 carrier `U_TT` and an invertible TT matrix `C`,
then the full dressed map also satisfies

```text
B^*P_TT = U_TT C'
```

for an invertible `C'`, and hence

```text
Pi_exact64 B^*P_TT = B^*P_TT.
```

The finite verifier checks the model algebra: scalar proper-time dressing on
the selected exact plane preserves `Pi_exact64` support. Dressing cannot create
the support if `B0` lacks it, and cannot destroy it if `B0` has it.

## Remaining Minimal Gate

The last source-level statement is now:

```text
B0^*P_TT = U_TT C
```

on the selected exact GR/QG branch, with `C` invertible and the same
central-circle angle as the exact `Z64` shift.

Equivalently, the direct computation packet is:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
central shift intertwining residual = 0
```

This is the smallest remaining hard object. The retarded kernel, SPT damping,
and proper-time filters are no longer part of the mystery; they preserve the
support selected by `B0`.
