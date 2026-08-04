---
abstract: |
  After locking the B_q color source, predecessor orientation, and reduced
  lens-nil gap, the remaining finite branch-selection problem is the up/down
  stiffness pair.  This note defines the exact Hessian extraction target for
  mu_u and mu_d.  The constants must be sector invariants of the selected
  quark closure-strain Hessian after the common anchored metric and
  color-singlet B_q Schur completion are fixed.  Until those Hessian blocks are
  supplied, mu_u and mu_d remain diagnostic constants rather than proved MTT
  predictions.
author:
- Peter Nero
date: June 2026
title: |
  Up/Down Stiffness Hessian Extraction Target for the Quark B_q Branch
---

# Purpose

The current selected B_q branch is:

```text
sigma = -1,
Lambda_q = lambda_lens - lambda_nil,
D_q(i,j,b)^2 =
  (J_i - J_b)^2
  + (1/2)(J_j - J_{b-1})^2.
```

The remaining constants are:

```text
mu_u,
mu_d.
```

They must not be chosen from CKM data.  They must be extracted from the
selected MTT Hessian.

# Sector Kernel

For `x in {u,d}`:

```text
C_x[b] = exp(-mu_x J_b) tau^{s_x b},
s_u = 1,
s_d = 2,
tau = exp(2 pi i 79/448).
```

The Yukawa skeleton is:

```text
Y_x[i,j] =
  C_x[b_ij]
  exp[-Lambda_q D_q(i,j,b_ij)^2].
```

Once `sigma` and `Lambda_q` are fixed, `mu_x` is the only remaining sector
stiffness multiplier.

# Hessian Extraction Definition

Let `H_x^cl` be the selected quark closure-strain Hessian block for sector
`x`, restricted to the retained family/color redundancy subspace after:

```text
1. coherent projection,
2. nil/color survivor projection,
3. common anchored metric extraction,
4. B_q hidden color-channel Schur completion.
```

Let `e_J` be the normalized anchor-cost direction:

```text
e_J proportional to J - mean(J) * 1.
```

Define the scalar stiffness:

```text
mu_x = <e_J, H_x^cl e_J> / <e_J, H_anchor e_J>,
```

where `H_anchor` is the unit first-order anchored Hessian used to normalize

```text
J = (0, lambda_nil/lambda_lens, 1).
```

This definition makes `mu_x` a Hessian eigenvalue/curvature ratio, not a
Yukawa or CKM fit.

# Pass Conditions

The desired no-proxy closure needs:

```text
H_u^cl supplied from Sigma_MTT,
H_d^cl supplied from Sigma_MTT,
H_anchor supplied from Sigma_MTT,
mu_u and mu_d computed from the above ratio,
no CKM angle, quark mass, or Yukawa singular value used as input.
```

Then the branch is tested by building `Y_u,Y_d` and computing:

```text
H_u = Y_u G_A^{-1} Y_u^*,
H_d = Y_d G_A^{-1} Y_d^*,
V = U_u^* U_d.
```

# Current Diagnostic Values

The current diagnostic branch uses:

```text
mu_u = 8,
mu_d = 2.
```

With the selected-orientation and reduced-gap branch:

```text
sigma = -1,
Lambda_q = lambda_lens - lambda_nil,
```

this gives a CKM-shaped result with residual about:

```text
0.014322.
```

A sibling diagnostic with swapped stiffnesses gives a smaller CKM residual,
but it is not automatically selected because stiffness assignment must come
from `H_u^cl,H_d^cl`, not from residual minimization.

# Why This Is the Last Finite Branch

The previous notes closed or conditionally selected:

```text
q79 CP phase source,
Z3 bridge reduction,
first-order anchored metric,
need for second-order quark breakdown,
B_q color-singlet Schur coefficient,
B_q retarded predecessor orientation,
B_q reduced primitive lens-nil gap.
```

Therefore the remaining finite quark-mixing branch is:

```text
the sector Hessian stiffness extraction.
```

# Bottom Line

The next proof must compute:

```text
mu_u = <e_J,H_u^cl e_J>/<e_J,H_anchor e_J>,
mu_d = <e_J,H_d^cl e_J>/<e_J,H_anchor e_J>.
```

If this gives the diagnostic branch, or another branch that still predicts CKM
and later masses without proxy inputs, then the quark mixing part can move from
diagnostic to selected MTT computation.

