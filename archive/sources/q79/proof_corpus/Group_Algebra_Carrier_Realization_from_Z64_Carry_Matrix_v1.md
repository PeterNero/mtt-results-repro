---
abstract: |
  We close the abstract finite-carrier construction once the Z_64 carry rows
  are available.  The six-row dyadic carry matrix has cokernel Z_64.  The
  finite coherent carrier is therefore the group algebra
  K_64=C[coker A_64]~=C[Z_64].  Multiplication by the generator x_0 defines a
  primitive shift S with S^64=I and no smaller positive period.  The Fourier
  idempotents of S are exactly the Z_64 character projectors.  Thus the
  finite Wilson/deck carrier used in the exact Z64-to-q79 theorem is not an
  extra object: it is canonically induced by the selected carry relation
  matrix.  What remains is not carrier construction, but proving that the
  actual MTT Hessian/kernel supplies the carry matrix and preserves the
  coherent block.
author:
- Peter Nero
date: May 2026
title: |
  Group-Algebra Carrier Realization from the Z64 Carry Matrix
---

# Purpose

The finite-carrier criterion asked for:

```text
K_64 ~= C[Z_64],
S^64=I,
S^d != I for 0<d<64.
```

This note shows that once the dyadic carry rows are selected, this carrier is
canonical.

# Carry Matrix

Use the six-level carry rows:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

Let `A_64` be this integer relation matrix.  Its cokernel is:

```text
G_64 := coker A_64.
```

The row calculation already gives:

```text
G_64 ~= Z_64.
```

# Canonical Carrier

Define:

```text
K_64 := C[G_64].
```

Since `G_64 ~= Z_64`, this is:

```text
K_64 ~= C[Z_64].
```

Let `g` be the class of `x_0`.  The carry rows imply:

```text
x_i = 2^i g,
64g = 0.
```

Since the Smith form is `[64]`, `g` has exact order `64`.

Define the shift:

```text
S |h> = |h+g>,   h in G_64.
```

Then:

```text
S^64=I,
S^d != I for 0<d<64.
```

# Character Projectors

Let:

```text
omega = exp(2 pi i / 64).
```

The finite Fourier idempotents are:

```text
E_q = (1/64) sum_{r=0}^{63} omega^(-qr) S^r,
q in Z_64.
```

They satisfy:

```text
E_q E_p = delta_qp E_q,
sum_q E_q = I,
S E_q = omega^q E_q.
```

Thus the unitary character dual of `G_64` is implemented directly on the
carrier.

# Theorem: Carrier Realization from Carry Rows

If the selected MTT dyadic sector supplies the six carry rows above, then it
canonically supplies the finite carrier:

```text
K_64 = C[coker A_64] ~= C[Z_64]
```

with primitive shift `S`.  Therefore the finite Wilson/deck carrier required
by the exact dyadic branch is constructed from the carry matrix itself.

## Proof

The Smith normal form of `A_64` is `[64]`, so `coker A_64 ~= Z_64`.  The class
of `x_0` generates the quotient because all other `x_i` are powers:

```text
x_i=2^i x_0.
```

The terminal row gives `64x_0=0`, and the Smith form rules out a smaller
period.  Therefore translation by `x_0` is an exact-order-64 permutation of
the group basis of `C[G_64]`.  This is the primitive shift `S`.  The Fourier
idempotents of a finite cyclic shift are the standard character projectors.

# What This Closes

```text
finite carrier K_64 from carry rows                  CLOSED
primitive shift S from generator x_0                 CLOSED
Z_64 character projectors                            CLOSED
```

# What Remains

The remaining MTT-specific task is:

```text
prove the selected Hessian/kernel supplies the carry matrix A_64
and retains K_64 inside Pi_coh.
```

Thus carrier construction is no longer open once the carry rows are accepted.
The open task is row extraction from MTT dynamics.
