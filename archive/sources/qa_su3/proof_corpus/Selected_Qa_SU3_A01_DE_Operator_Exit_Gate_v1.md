# Selected Qa/SU3 A01/D_E Operator Exit Gate v1

## Claim

The `A01/D_E` route is formalized as an executable acceptance gate.  It is
required because the gerbe period normalization is reduced to a scalar selector
that is not currently supplied by the same-branch corpus.  This artifact does
not yet supply selected matrices.

## Acceptance Interface

A valid operator exit must supply all of:

```text
selected Qa/SU3 source certificate,
typed section or finite Cech/Dolbeault cochain bases for F1..F5, G1..G5, P,
selected f and g matrices with g*f=0,
selected D_E, rho_E, Riesz, Green, heat, zeta, or torsion finite-part operator,
reproducible spectral/heat/rho_E/Riesz output,
Freed-Witten, Green-Schwarz/Bianchi, stability/local-freeness, and projector-retention checks where applicable.
```

The eleven spaces carried forward are:

```text
F1..F5, G1..G5, P.
```

## Reusable Patterns

The nonsm typed monad interface gives the right validator shape.  The q79
`rho_E` and Riesz artifacts give useful acceptance machinery.  The visible
`VAlpha` source candidates name the correct kind of same-source packet:

```text
finite Cech or Dolbeault cochain packet,
same-source D_E operator block,
same-source dotD response.
```

These are patterns and validators, not selected Qa/SU3 matrix values.

## Rejected Shortcuts

The gate rejects:

```text
identity rho_E,
simultaneously diagonal scalar phase table as physical mixing,
generic existence of f,g without matrices,
direct q79/S3 finite torsion import,
Chern/Bianchi row without same-source operator data,
observed residual or measured constants as inputs.
```

## Verdict

The operator-exit gate is built, but the operator exit is not promoted.  The
missing selected object is now:

```text
Selected_Qa_SU3_Cech_Dolbeault_Matrix_Packet_v1
```

That packet must provide the finite bases, typed maps, and same-source operator
matrices needed for a reproducible `D_E/rho_E` exit.
