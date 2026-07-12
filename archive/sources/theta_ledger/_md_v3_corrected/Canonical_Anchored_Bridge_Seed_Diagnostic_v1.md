---
abstract: |
  We test the leanest fully specified anchored-bridge quark seed: amplitudes
  are exp(-J_b), phases are q79 character powers, the family metric is the
  universal anchored transport/lens/nil metric, and no measured masses or CKM
  angles are used.  The seed is mathematically coherent and produces nonzero
  left mixing, but the resulting CKM-like matrix has large mixing angles rather
  than the observed small quark angles.  This is a useful diagnostic failure:
  the universal anchored profile alone is too democratic for quarks.  The
  quark sector needs an additional selected stiffness, bridge-weight hierarchy,
  or localization separation derived from Sigma_MTT.
author:
- Peter Nero
date: June 2026
title: |
  Canonical Anchored-Bridge Seed Diagnostic
---

# Purpose

The universal anchored metric theorem shows that:

```text
q79/Z3 bridge skeleton + universal anchored metric
```

can escape the pure bridge no-CKM obstruction.

This note asks the next natural question:

```text
What happens if we use the leanest fully specified no-proxy seed?
```

# Seed Definition

Use:

```text
J = (0, lambda_nil/lambda_lens, 1)
  ~= (0, 0.070028, 1).
```

Define:

```text
G_A^{-1} = diag(exp(-2J_0), exp(-2J_1), exp(-2J_2)).
```

For bridge class `b in Z3`, set:

```text
C_u[b] = exp(-J_b) tau^b,
C_d[b] = exp(-J_b) tau^{2b},
tau = exp(2 pi i 79/448).
```

Then:

```text
Y_x[i,j] = C_x[-(i+j) mod 3].
```

This seed uses no observed masses or CKM angles.

# Diagnostic Result

The audit computes:

```text
H_u = Y_u G_A^{-1} Y_u^*,
H_d = Y_d G_A^{-1} Y_d^*,
V_seed = U_u^* U_d.
```

The resulting absolute mixing matrix is approximately:

```text
|V_seed| =
[[0.6003, 0.7718, 0.2097],
 [0.6706, 0.4862, 0.5603],
 [0.4358, 0.4098, 0.8013]].
```

This is not CKM-like.  It is large-mixing/democratic compared with the quark
target:

```text
|V_CKM| ~
[[0.974, 0.225, 0.004],
 [0.225, 0.974, 0.041],
 [0.006, 0.041, 0.999]].
```

# Theorem: Universal Seed Is Not Quark-Closed

The lean universal anchored-bridge seed does not derive the observed quark CKM
magnitudes.

Proof.  The computed off-diagonal seed magnitudes are order `0.2--0.8`, while
the CKM quark off-diagonal magnitudes are hierarchical, with `V_13` and `V_23`
small.  Therefore the universal seed is not a no-proxy quark closure.

# Interpretation

This is progress, not a dead end.  We now know:

```text
pure bridge symmetry: too rigid, gives no CKM;
universal anchored seed: too democratic, gives large mixing;
observed quarks: require selected additional stiffness/hierarchy.
```

The corpus already hints at such a distinction:

```text
quarks: partially anchored composite sectors with stiff closure geometry;
leptons/neutrinos: softer or less anchored sectors.
```

Thus the next source should be:

```text
quark-specific selected stiffness or localization separation,
not arbitrary entry-wise Yukawa fitting.
```

# What This Closes

```text
first fully specified anchored-bridge seed          COMPUTED
nonzero mixing from q79/J data                      CHECKED
seed is not CKM-quark closed                        PROVED
need for extra selected quark stiffness             IDENTIFIED
```

# What Remains

```text
derive quark stiffness/localization separation       OPEN
derive bridge-weight hierarchy C_u,C_d               OPEN
test whether same seed is PMNS-like                  OPEN
compute real quark CKM only after Sigma_MTT freezes  OPEN
```

# Bottom Line

The next missing object is no longer merely "a metric."  It is:

```text
selected quark-sector stiffness or bridge hierarchy
```

derived from theta/lens/nil/proto-spinor closure.

