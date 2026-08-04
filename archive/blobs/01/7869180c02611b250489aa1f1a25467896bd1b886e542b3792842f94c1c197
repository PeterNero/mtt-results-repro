---
abstract: |
  We turn the finite-label mass-action fingerprint into an explicit
  right-channel source-operator schema.  On the two light weighted
  right-singular channels, the up-sector residual is a retarded spinorial
  split J(-1/2 I + Xi_u), with Xi_u eigenvalues (-1,+1).  The down-sector
  residual is a dyadic/nil projector sum (1/64)P_dyad + (3/2 lambda_nil)P_nil.
  These operators commute with the weighted right-channel Gram matrices by
  construction, so the associated action layer preserves CKM.  The remaining
  proof obligation is no longer algebraic: MTT must identify Xi_u, P_dyad, and
  P_nil as selected projectors of the theta/lens/nil/proto-spinor source map.
author:
- Peter Nero
date: June 2026
title: |
  Finite-Label Right-Channel Source Operator Schema
---

# Purpose

The finite-label candidate found:

```text
R_u light eigenvalues = (-3/2 J, +1/2 J),
R_d light eigenvalues = (1/64, +3/2 lambda_nil),
```

relative to the Gaussian base:

```text
A_{x,a}^{base} = q_x^2 log(pi).
```

This note rewrites those labels as source operators.

# Weighted Right-Channel Space

For each quark sector:

```text
Z_x = Y_x G_A^{-1/2} = U_x S_x V_x^*.
```

The selected mass action may preserve left mixing only if it acts through
operators diagonal in the `V_x` basis.  Equivalently, the residual source
operator `R_x` must commute with:

```text
K_x = Z_x^* Z_x.
```

# Up-Sector Source Schema

Let `P_{u,1}` and `P_{u,2}` be the two light weighted right-channel spectral
projectors.  Define:

```text
I_u^light = P_{u,1}+P_{u,2},
Xi_u      = -P_{u,1}+P_{u,2}.
```

Then:

```text
R_u = J(-1/2 I_u^light + Xi_u),
J = lambda_nil/lambda_lens.
```

Hence:

```text
spec_light(R_u) = (-3/2 J, +1/2 J).
```

Interpretation:

```text
-1/2 I_u^light
```

is the common retarded half-step offset, while:

```text
Xi_u
```

is a spinorial right-channel orientation operator with eigenvalues `-1,+1`.

# Down-Sector Source Schema

Let `P_dyad` and `P_nil` be the two light weighted right-channel spectral
projectors selected by the down-sector right-channel labels.  Define:

```text
R_d = (1/64) P_dyad + (3/2 lambda_nil) P_nil.
```

Hence:

```text
spec_light(R_d) = (1/64, +3/2 lambda_nil).
```

Interpretation:

```text
1/64
```

is the dyadic survivor-width scale of the selected order-64 carrier, while:

```text
3/2 lambda_nil
```

is a three half-channel nil-survivor cost.

# Full Candidate Actions

The total candidate action operators are:

```text
A_u = 4 log(pi) I_u^light + R_u,
A_d = 1 log(pi) I_d^light + R_d.
```

Thus:

```text
spec_light(A_u) = 4 log(pi) + (-3/2 J, +1/2 J),
spec_light(A_d) = 1 log(pi) + (1/64, +3/2 lambda_nil).
```

# Algebraic Theorem

Assume `R_x` is built from spectral projectors of `K_x=Z_x^*Z_x`.  Then:

```text
[R_x,K_x]=0.
```

Therefore the action layer:

```text
Z_x' = U_x S_x exp(-A_x) V_x^*
```

preserves the left singular vectors `U_x`.  Consequently:

```text
V_CKM = U_u^* U_d
```

is unchanged.

# Proof

The projectors `P_{x,a}` are spectral projectors of `K_x`, so they commute
with `K_x`.  Any real linear combination of these projectors also commutes with
`K_x`.  Hence `R_x` and `A_x` are diagonal in the same `V_x` basis as `K_x`.
Multiplying the singular values by `exp(-A_x)` changes `S_x` but not `U_x`.
Therefore CKM is preserved.

# What Is Proved

```text
operator form producing finite labels             CONSTRUCTED
commutation with weighted right Gram matrices      PROVED
CKM preservation                                   PROVED
near-mass closure with finite labels               CHECKED
```

# What Remains Open

```text
derive Xi_u from retarded/spinorial right-channel source      OPEN
derive P_dyad from order-64 survivor-width source             OPEN
derive P_nil from nil half-channel source                     OPEN
show these projectors are selected before mass comparison     OPEN
```

# Bottom Line

The remaining wall has moved.  It is no longer:

```text
find any mass layer that preserves CKM.
```

It is now:

```text
prove that Sigma_MTT selects the projectors
Xi_u, P_dyad, P_nil
with eigenvalues (-1,+1), 1/64, and 3/2 lambda_nil.
```

