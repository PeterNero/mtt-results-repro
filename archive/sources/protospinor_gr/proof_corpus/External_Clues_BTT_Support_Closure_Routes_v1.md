# External Clues for BTT Support Closure Routes v1

## Result

External physics does not close the final support identity by itself, but it
does sharpen the target. The best remaining theorem is not a new number. It is
an equivariance theorem for the actual adjoint TT co-shape map:

```text
B^*P_TT must intertwine TT helicity rotations with the same central-circle
U(1) action whose selected finite carrier is the exact Z64 d_* branch.
```

If that is proved, the already closed Z64 uniqueness theorem forces:

```text
Pi_exact64 B^*P_TT = B^*P_TT,
support(J_TT)=|d_*> tensor span{c_2,s_2},
lambda_GR,TT=15.
```

## External Clues Imported

1. Weinberg soft-graviton logic supports universal spin-2 coupling under the
   usual S-matrix assumptions. It helps show that a physical massless spin-2
   response is not sector-local or freely adjustable.

2. Deser-style self-interaction/gauge-invariance logic supports the recovery of
   Einstein-type nonlinear coupling from consistent massless spin-2 dynamics.

3. Kaluza-Klein zero-mode logic explains why the low-energy graviton is a
   universal coherent mode rather than a massive internal excitation.

None of these standard arguments selects `Z64` or `Pi_exact64`. They are
therefore used as constraints and clues, not as proof of the finite MTT branch.

## Route Audit

### R1 Universal Spin-2 Bookkeeping Selector

This route combines massless spin-2 universality with the MTT central-circle
claim that gravity operates on the unique shared coherence channel.

It supports the physical direction strongly, but it still does not identify the
finite support projector.

### R2 Equivariant Central-Character Selector

This is the best route. It asks for a precise theorem:

```text
B^*P_TT is equivariant for the same central-circle angle that rotates TT
plus/cross with helicity weight 2.
```

Then finite sampling on the selected exact `Z64` branch leaves only the
`k=2/k=62` real character plane. This route directly targets the no-go, because
the no-go allowed nonzero TT support outside `Pi_exact64` only by leaving the
central equivariance/same-angle fact unspecified.

### R3 Zero-Mode Shadow plus Finite Helicity

This route separates two notions that can otherwise get tangled:

- external/KK zero-mode means no low-energy massive internal excitation;
- central-circle `k=2` means spin-2 helicity under the shared angular action.

So `k=2` does not contradict zero-mode gravity. But zero-mode recovery alone
still does not prove the exact finite carrier.

### R4 Closed-String Global Bookkeeping Analogy

This route is useful as intuition: closed-string massless spin-2 behavior points
to gravity as a global consistency/bookkeeping mode. But analogy cannot close
the theorem.

### R5 Direct Matrix Reconstruction

This is the brute-force route: construct the finite matrix for `B^*P_TT`, then
multiply by `Pi_exact64`. It would be decisive, but the selected entries of
`DG(Psi*)` are not yet sourced.

## Next Theorem

Write and prove:

```text
EquivariantCentralCircleTTSupportTheorem.v1
```

Statement:

```text
On the selected exact GR/QG branch, the adjoint TT co-shape map B^*P_TT is
equivariant for the central-circle U(1) action that rotates TT plus/cross with
helicity weight 2, and the selected finite carrier of that action is the exact
Z64 d_* branch.
```

This is the cleanest closure path because it adds no fitted scalar, uses no
observed Newton/Planck input, and converts the previous missing support premise
into a checkable representation-theoretic statement.
