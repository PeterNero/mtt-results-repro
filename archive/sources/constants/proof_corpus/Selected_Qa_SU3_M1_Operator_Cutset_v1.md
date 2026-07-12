# Selected Qa/SU3 m=1 Operator Cut Set

## Result

After the S3 source-origin ladder, the visible Green-Schwarz curvature row is
also no longer a blocker.

Imported q79 facts:

```text
selected S3 twisted source support: closed
old S3 gerbe/Freed-Witten/block-projector blockers: retired
visible Green-Schwarz curvature row: closed
zero symbolic Bianchi residual: closed
q79 and q369 finite branch packets reach the validator layer
```

The closed Green-Schwarz row is still a curvature-level result.  It validates
the symbolic `dH`, `Tr R_+^2`, and required `Tr F_visible^2` rows, but it does
not by itself derive `Tr F_visible^2` from a selected visible bundle or sheaf.

## Remaining Cut Set

The first true gate is now:

```text
selected visible Chern-Weil/operator source
```

That source must supply:

```text
selected visible bundle or sheaf model,
Chern-Weil derivation of the visible Tr_F row,
HYM or Route-C residual with selected_source_verified true,
coherent spectral zero-mode projectors,
sector D_E action matrices,
Riesz projector and reduced Green,
same-branch dotD/alpha1 response,
antiunitary equivalence or retarded branch selection,
primitive C1 contractions.
```

So we are not looking for another symbolic Bianchi cancellation.  We are looking
for the selected operator source that makes the already-closed curvature row
physical and propagates it into the finite spectral response stack.

## Branch Status

The q79 and q369 packets form a conjugate pair.  Both reach the finite
validators, and both fail only on source-origin flags.  Therefore q=79 is not
yet uniquely selected at this level unless the next source certificate either
selects the `m=1` branch directly or proves the pair antiunitarily equivalent
until a retarded boundary condition selects one orientation.
