# Iwasawa Sector Projection Validator

## Purpose

After `rho_E` and Hermitian metric compatibility, the next missing finite input
is the split into SM calculation slots:

```text
Q,u,d,L,e,N,H.
```

The selected zero-mode/dotD interface already records that:

```text
Q,u,d,L,e,N are three-family slots,
H is a single-Higgs carrier slot.
```

This note adds an executable validator for candidate finite-rank sector maps.
It does not construct the selected sector maps.  It defines the first accepted
projector format and checks that the supplied projectors are stable under the
same `rho_E` gluing used by the finite-element bundle.

## Supported v1 Format

A candidate file must include:

```text
rank = 3,
mesh_N >= 1,
generator_data for g1,...,g6,
sector_projection_maps for Q,u,d,L,e,N,H.
```

Each sector entry has:

```text
kind,
dimension,
projector.
```

The required sector dimensions are:

```text
Q,u,d,L,e,N: kind=family, dimension=3,
H:           kind=single_higgs_carrier, dimension=1.
```

The `projector` is a `3x3` complex matrix in the same representation convention
as the supplied finite `rho_E` data.

This v1 format is intentionally modest.  It validates finite-rank projector
data.  It does not claim that all future SM sector constructions must literally
be represented by these projectors; it only gives the current proof-repro
pipeline an executable gate for the finite-projector route.

## Projector Conditions

For each sector `s`, the validator checks:

```text
P_s^* = P_s,
P_s^2 = P_s,
rank(P_s) = declared dimension.
```

It then checks boundary-face stability:

```text
rho_E(gamma,z) P_s = P_s rho_E(gamma,z)
```

on all visited finite-mesh boundary targets.

This says the sector split is compatible with the supplied bundle gluing.  A
sector map that changes when crossing an identified face cannot be used as a
global sector slot without more data.

## Implemented Checks

The script:

```text
scripts/validate_iwasawa_sector_maps.py
```

checks:

```text
rank=3 declaration,
mesh_N positive integer,
all six generator entries present,
all seven sector entries present,
sector kind and dimension,
3x3 projector shape,
Hermitian projector,
idempotent projector,
projector rank,
rho_E invariance on boundary faces.
```

The script returns:

```text
0: complete rho_E plus sector-projector candidate passes,
1: complete candidate fails,
2: candidate is incomplete/open.
```

## Smoke Tests

The audit runs four tests.

First, the open template is refused with exit code `2`, because all sector map
entries are still null.

Second, identity `rho_E` with identity family projectors and a rank-one Higgs
projector passes.  This is only a schema smoke test:

```text
P_Q=P_u=P_d=P_L=P_e=P_N=I_3,
P_H=diag(0,0,1).
```

It is not selected SM data.

Third, a candidate declaring `Q` to have dimension `3` while supplying a
rank-one projector fails.

Fourth, a candidate with a transition matrix that does not commute with the
Higgs projector fails the `rho_E`-invariance check.

## What This Closes

This closes:

```text
finite-projector sector map validator,
family-versus-Higgs dimension gate,
rho_E-invariant sector projector gate.
```

It does not close:

```text
actual selected sector projection maps,
proof the maps come from the selected E6-to-SM branch,
actual selected rho_E,
actual selected Hermitian metric,
selected D_E action on each sector,
Gram and stiffness matrices,
Yukawa overlap matrices.
```

## Guardrail

Do not use identity family projectors as a proof of selected SM sector maps.
They are a schema smoke test only.

Do not choose sector projectors to tune CKM angles, Yukawa magnitudes, or
benchmark matrices.

Do not claim SM closure from sector-map validation.  This is a necessary input
gate before constructing sector-specific operators and overlaps.

## Verdict

The finite bundle execution stack now has executable gates for:

```text
rho_E constant algebra,
rho_E finite-mesh corner consistency,
Hermitian metric compatibility,
sector projection maps.
```

The remaining selected-data step is still the hard one: supply actual selected
`rho_E`, metric, and sector maps from typed monad/Cech/HYM data, then validate
sector-specific `D_E` actions before assembling Gram, stiffness, and Yukawa
overlap matrices.
