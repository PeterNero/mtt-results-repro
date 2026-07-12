# Core B0 Factorization Final Gate v1

## Decision

The final exact-support theorem is not honestly closed yet.

We have reduced it to the smallest remaining object:

```text
B0^*P_TT = U_TT C
```

where `B0` is the metric shape-map core from the QG SPT factorization,
`U_TT` is the same-angle helicity-2 carrier into the exact `Z64 d_*` branch, and
`C` must be invertible on the TT plus/cross quotient.

## What Does Not Close It

The QG paper also introduces a spectral-filter object with a similar name:

```text
B := f(L),
B0 := integral e^{-sL} ...
```

and proves that this filter-core is positive and commutes with `L`. That is
useful for damping and filter independence, but it is not the same object as
the metric shape-map core in

```text
B = DG(Psi*)Pi_coh = exp(-tau0 E/2) B0 exp(-tau0 A_int/2).
```

Therefore we must not use the spectral-filter `B0` as a proof of the metric
co-shape support.

The central-circle paper also gives the right physical channel: gravity operates
on the shared circle/coherence channel. But it does not compute the matrix
`B0^*P_TT`, so it cannot close the final support identity by itself.

## Final Packet

To finish the theorem, fill:

```text
SelectedCoreB0TTFactorizationPacket.v1
```

with these checks:

```text
rank(U_TT^* B0^*P_TT)=2
(I-Pi_exact64)B0^*P_TT=0
S_64 B0^*P_TT = B0^*P_TT R_TT(2 theta)
```

If those pass, then all remaining implications are already verified:

```text
B0^*P_TT=U_TT C
B^*P_TT=U_TT C'
Pi_exact64 B^*P_TT=B^*P_TT
support(J_TT)=|d_*> tensor span{c2,s2}
lambda_GR,TT=15
```

## Status

This is a good kind of open problem: the theorem is no longer vague. It is a
specific finite core-map packet. The next genuine progress must supply the
metric shape-map core entries or a source theorem proving the same three packet
checks.
