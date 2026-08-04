---
abstract: |
  We identify the CKM-preserving structure required of the selected mass layer.
  A generic family-basis prefactor changes the left Hermitian forms and spoils
  CKM.  A positive action layer must instead act in the right singular
  eigenchannels of the canonically weighted matrix Y G_A^{-1/2}.  In that
  weighted basis it changes singular values while preserving the left singular
  vectors that define CKM.  Therefore it can supply the missing quark mass
  hierarchy without changing the already-selected CKM branch.  This is a
  theorem target, not a final source derivation: MTT must still derive the
  weighted right-eigenchannel action costs from Sigma_MTT rather than choose
  them from observed masses.
author:
- Peter Nero
date: June 2026
title: |
  Right-Eigenchannel Mass-Layer Theorem Target for CKM-Preserving Yukawa Closure
---

# Purpose

The selected finite B_q branch gives CKM-shaped left mixing but singular values
that are too shallow.

A family-basis prefactor can improve singular values, but it changes the left
Hermitian forms and spoils CKM.

This note identifies the correct algebraic shape of the missing mass layer.

# Theorem: Weighted Right-Eigenchannel Actions Preserve Left Mixing

Let the selected left Hermitian form be computed with the anchored inverse
metric:

```text
H = Y G_A^{-1} Y^*.
```

Define the canonically weighted matrix:

```text
Z = Y G_A^{-1/2}.
```

Then:

```text
H = Z Z^*.
```

Let:

```text
Z = U S V^*
```

be the singular-value decomposition of the weighted matrix.

Let the mass layer act by:

```text
Z' = U S P V^*
```

where

```text
P = diag(exp(-A_1), exp(-A_2), 1)
```

is positive diagonal in the selected weighted right singular eigenchannel
basis.  Equivalently,

Then:

```text
Y' = Z' G_A^{1/2}.
```

Then:

```text
Y'G_A^{-1}Y'^* = Z'Z'^* = U S P^2 S U^*.
```

Therefore the left eigenvectors are still `U`; only the singular values change.
Consequently, applying such a layer separately to `Y_u` and `Y_d` preserves:

```text
V_CKM = U_u^* U_d.
```

# Proof

Since `P` is diagonal in the same basis as `S`, the product `S P^2 S` is
diagonal.  Hence the spectral projectors of `Y'G_A^{-1}Y'^*` are the same
columns of `U` as for `YG_A^{-1}Y^*`, unless a degeneracy is introduced.  For
strict singular value ordering, no degeneracy is introduced and the left mixing
is unchanged.

# Required Right-Eigenchannel Actions

From the selected B_q branch, the required extra actions are:

```text
A_u ~= (4.480058, 4.615899, 0),
A_d ~= (1.158678, 1.526516, 0).
```

If these are supplied in the weighted right eigenchannel basis, the benchmark
normalized quark singular values of the weighted matrices are recovered while
the selected CKM matrix is preserved.

# MTT Source Requirement

This does not prove the masses.  It states the form the selected source must
take:

```text
Sigma_MTT must produce right-singlet/eigenchannel action costs
that commute with the selected weighted right-channel metric of each B_q
Yukawa sector.
```

Candidate sources:

```text
1. right-singlet line-bundle action costs;
2. holomorphic/instanton prefactors attached to right-channel zero modes;
3. Higgs-overlap prefactors diagonal in the right-channel basis;
4. nil-survivor finite-width corrections after left-sector projection.
```

# What This Closes

```text
CKM-preserving weighted mass-layer algebra         PROVED
family-basis prefactor no-go explained             PROVED
weighted right-eigenchannel action target defined  DEFINED
```

# What Remains

```text
derive A_u,A_d from Sigma_MTT without mass inputs          OPEN
connect weighted right eigenchannels to zero modes          OPEN
relate weighted singular values to final physical masses    OPEN
run RG/threshold normalization                             OPEN
```

# Bottom Line

The mass layer must not be an arbitrary family-basis diagonal.  It must be a
selected weighted right-eigenchannel action layer:

```text
Z_x = Y_x G_A^{-1/2} = U_x S_x V_x^*
-> Z_x' = U_x S_x P_x V_x^*
-> Y_x' = Z_x' G_A^{1/2}.
```

That is the clean path toward mass closure without undoing the CKM branch.
