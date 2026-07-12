---
abstract: |
  We take the minimal q79/Z3 localization packet one step closer to a Yukawa
  calculation.  The family-conserving bridge rule reduces each quark Yukawa
  sector from nine independent entries to three bridge amplitudes.  The raw
  matrices have the fixed form Y_x[i,j]=C_x[b] with b=-(i+j) mod 3, optionally
  multiplied by the selected q79 character powers.  Thus the localization
  packet forbids entry-wise Yukawa fitting and replaces it with a finite
  bridge-weight problem.  A direct check shows something sharper: pure
  bridge-reduced matrices can be full rank, but their Hermitian left forms
  commute because they are diagonalized by the same family Fourier transform.
  Therefore the bridge skeleton alone cannot generate CKM angle magnitudes.
  The remaining open task is to derive selected family breaking from
  theta/lens/nil/proto-spinor action costs, kinetic metrics, anchor
  projectors, or sector-dependent localization geometry.
author:
- Peter Nero
date: June 2026
title: |
  Bridge-Reduced Yukawa Packet from the q79/Z3 Localization Skeleton
---

# Purpose

The minimal localization packet constructed:

```text
Gamma_u[i,j] = {b_ij},
Gamma_d[i,j] = {b_ij},
b_ij = -(i+j) mod 3.
```

This note records the corresponding raw Yukawa form.

# Bridge-Reduced Matrix Form

For each sector:

```text
x in {u,d},
```

define three selected bridge weights:

```text
C_x[0], C_x[1], C_x[2].
```

Then:

```text
Y_x[i,j] = C_x[-(i+j) mod 3].
```

Explicitly:

```text
Y_x =
[[C0, C2, C1],
 [C2, C1, C0],
 [C1, C0, C2]].
```

This is not a general 3x3 matrix.  It is a three-parameter bridge-reduced
matrix in each sector.

# Selected CP Character

Each bridge weight must be of the selected-kernel form:

```text
C_x[b] =
  A_x[b] exp(-S_x[b]) tau^{w_x[b]},
tau = exp(2 pi i 79/448).
```

The real positive data:

```text
A_x[b], S_x[b]
```

must come from theta/lens/nil/proto-spinor geometry.  The phases must stay in
the q79 character algebra.

# Theorem: Entry Reduction

In the minimal selected localization packet, each quark Yukawa sector is
determined by at most three bridge weights before kinetic normalization.

Proof.  For each pair `(i,j)`, family conservation fixes a unique bridge:

```text
b_ij = -(i+j) mod 3.
```

Therefore every raw matrix entry is the selected amplitude of that bridge.
There are only three bridge classes in `Z3`, hence at most three raw weights
per sector.

# Theorem: Pure Bridge Reduction Has Trivial Left Mixing

Pure bridge reduction forces the left diagonalization basis to be common.

Proof.  Let:

```text
Y_u = Y(C_u[0],C_u[1],C_u[2]),
Y_d = Y(C_d[0],C_d[1],C_d[2]).
```

The matrices `Y_x` are reverse-circulant: each is a circulant family operator
composed with the fixed inversion/reflection on `Z3`.  Consequently:

```text
H_x = Y_x Y_x^*
```

is circulant for every bridge triple.  All circulant matrices on `Z3` are
diagonalized by the same family Fourier transform, so:

```text
[H_u,H_d]=0.
```

Thus pure bridge reduction can provide full rank and phase-rigid entries, but
it cannot by itself produce CKM angle magnitudes if the kinetic metrics are
also family-circulant.

# Corollary: Need Selected Family Breaking

Nontrivial CKM magnitudes require at least one same-source ingredient beyond
the pure bridge skeleton:

```text
sector-dependent localization centers,
non-circulant kinetic metrics,
lens/nil anisotropic widths,
anchor/cancellation projectors,
or additional selected finite channel classes.
```

Such breaking must be derived from `Sigma_MTT`; it cannot be chosen entry by
entry.

# What This Closes

```text
9 entries per quark sector -> 3 bridge weights       PROVED
entry-wise Yukawa fitting blocked                    PROVED FOR PACKET
full-rank bridge matrices possible                   CHECKED
pure bridge Hermitian forms commute                   PROVED/CHECKED
selected family breaking is necessary for CKM angles  PROVED
q79 phase algebra retained                           PROVED/IMPORTED
```

# What Remains

```text
derive C_u[0..2] from Sigma_MTT                       OPEN
derive C_d[0..2] from Sigma_MTT                       OPEN
derive kinetic metrics                                OPEN
derive selected non-circulant family breaking          OPEN
compute actual CKM magnitudes                         OPEN
extend same bridge logic to e, nu, and M_R            OPEN
```

# Bottom Line

The first flavor-kernel shape is now concrete:

```text
selected q79/Z3 localization
-> finite bridges b in Z3
-> three bridge weights per sector
-> no entry-wise Yukawa fitting
-> but no CKM magnitudes without additional selected family breaking.
```

The missing hard data have narrowed from nine arbitrary entries to selected
bridge weights plus a same-source family-breaking mechanism.
