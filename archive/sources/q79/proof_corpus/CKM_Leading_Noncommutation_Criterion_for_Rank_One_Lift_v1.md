---
abstract: |
  We close the leading CKM noncommutation test for Yukawa matrices near the
  rank-one Iwasawa seed.  If Y_u=E33+epsilon M_u and Y_d=E33+epsilon M_d,
  then [Y_uY_u^\dagger,Y_dY_d^\dagger] has leading term epsilon
  [E33,A_d-A_u], where A_s=E33 M_s^\dagger+M_s E33.  This leading term is
  nonzero exactly when the up/down heavy-link vectors
  (M_s,13,M_s,23) differ.  Thus after the C1 alpha_1 response matrices are
  computed, the first CKM orientation target is Delta v=(M_d13-M_u13,
  M_d23-M_u23).  CKM angle magnitudes and the Jarlskog invariant remain open.
author:
- Peter Nero
date: May 2026
title: |
  CKM Leading Noncommutation Criterion for the Rank-One Lift
---

# Purpose

The rank-lift criterion identifies the first determinant target:

```text
C33(M_s) = M_s,11 M_s,22 - M_s,12 M_s,21.
```

For quarks, full rank is not enough.  CKM mixing requires that the up and down
Hermitian forms fail to commute:

```text
H_u = Y_u Y_u^dagger,
H_d = Y_d Y_d^dagger,
[H_u,H_d] != 0.
```

This note closes the leading noncommutation test near the shared rank-one seed.

# Setup

Let:

```text
Y_u(epsilon) = E33 + epsilon M_u + O(epsilon^2),
Y_d(epsilon) = E33 + epsilon M_d + O(epsilon^2),
```

where `E33=diag(0,0,1)`.  Define:

```text
H_s = Y_s Y_s^dagger,
A_s = E33 M_s^dagger + M_s E33.
```

Then:

```text
H_s = E33 + epsilon A_s + O(epsilon^2).
```

Write the heavy-link vector:

```text
v_s = (M_s,13, M_s,23).
```

# Leading Commutator

Expanding gives:

```text
[H_u,H_d]
  = epsilon [E33, A_d - A_u] + O(epsilon^2).
```

Only the heavy-link difference enters this leading term.  Let:

```text
Delta v = v_d - v_u = (Delta v1, Delta v2).
```

Then:

```text
[E33, A_d - A_u] =
[[0, 0, -Delta v1],
 [0, 0, -Delta v2],
 [conj(Delta v1), conj(Delta v2), 0]].
```

Therefore the leading noncommutation condition is:

```text
Delta v != (0,0).
```

# Theorem

#### Leading CKM Noncommutation Criterion

For:

```text
Y_u = E33 + epsilon M_u + O(epsilon^2),
Y_d = E33 + epsilon M_d + O(epsilon^2),
```

the commutator `[Y_uY_u^dagger,Y_dY_d^dagger]` is nonzero at order `epsilon`
if and only if:

```text
(M_d,13-M_u,13, M_d,23-M_u,23) != (0,0).
```

Consequently, once the selected C1 alpha_1 response matrices are computed, the
first CKM orientation scalar/vector target is the heavy-link mismatch:

```text
Delta v = (M_d13-M_u13, M_d23-M_u23).
```

#### Proof

The first variation of the Hermitian form is:

```text
A_s = E33 M_s^dagger + M_s E33.
```

Since `[E33,E33]=0`, the order-`epsilon` part of the commutator is:

```text
[E33,A_d] + [A_u,E33]
  = [E33,A_d-A_u].
```

The matrix `A_d-A_u` has nonzero off-diagonal entries connecting the third
family to the first two exactly through `Delta v`.  Direct multiplication by
`E33` gives the displayed matrix.  It vanishes exactly when both components of
`Delta v` vanish.

# Relation to CP

The q79 branch supplies a CP-active finite character:

```text
q = 79 mod 448.
```

However, this theorem does not by itself prove CKM CP violation or angle
magnitudes.  The full Jarlskog gate still requires selected matrices with
nondegenerate spectra and:

```text
Im det([H_u,H_d]) != 0
```

equivalently, up to convention:

```text
Tr([H_u,H_d]^3) != 0.
```

Thus the logic is:

```text
rank:        C33(M_u), C33(M_d) nonzero,
orientation: Delta v nonzero at leading order,
CP:          q79-active channel plus nonzero selected Jarlskog invariant,
magnitudes:  selected singular values and RG matching.
```

# Degenerate Case

If:

```text
Delta v = (0,0),
```

then the leading order commutator vanishes.  This does not prove that CKM
mixing is impossible.  It means the next test must use the `O(epsilon^2)`
terms:

```text
[E33, M_d M_d^dagger - M_u M_u^dagger] + [A_u,A_d].
```

That fallback calculation remains open until the selected response matrices
are known.

# What This Closes

```text
leading CKM noncommutation expansion,
heavy-link mismatch target,
separation between rank and CKM orientation,
guardrail against claiming Jarlskog or CKM magnitudes too early.
```

# What Remains Open

```text
actual M_u entries,
actual M_d entries,
Delta v from selected overlaps,
O(epsilon^2) fallback if Delta v=0,
selected Jarlskog invariant,
CKM angle magnitudes,
canonical kinetic metrics,
RG and threshold matching.
```

# Next Calculation

In parallel with the light-family rank minor:

```text
C33_s = M_s,11 M_s,22 - M_s,12 M_s,21,
```

compute the two heavy-link differences:

```text
M_d13 - M_u13,
M_d23 - M_u23.
```

If at least one is nonzero, the up/down Hermitian forms are already
noncommuting at leading order.

Follow-up CP status: the Jarlskog closure criterion is now closed as a
matrix-level target.  Once canonical selected `Y_u,Y_d` exist, define:

```text
H_u = Y_u Y_u^dagger,
H_d = Y_d Y_d^dagger,
Delta_CP = Im det([H_u,H_d]).
```

With nondegenerate spectra, `Delta_CP != 0` is the full CKM CP gate.
