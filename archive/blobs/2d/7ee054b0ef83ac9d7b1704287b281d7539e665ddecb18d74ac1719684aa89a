---
abstract: |
  We state the exact theorem needed to turn the Lens-Nil determinant-seven
  coefficient fingerprint into a proof of the Z_7 CP row.  The theorem must
  show that the coherent projector sends the two componentwise Lens x Nil
  Bianchi equations on the invariant (2,2) basis to two integral relations on
  the residual Wilson/nil CP character lattice, preserving the primitive block
  [[2,1],[1,4]].  If this descent is proved, Smith normal form gives Z_7,
  the dyadic carry gives Z_64, and the selected CP quotient is Z_448, with the
  family Z_3 remaining an ambient kernel.  This note isolates the lemmas,
  assumptions, and failure modes for that proof.
author:
- Peter Nero
date: May 2026
title: |
  Descent Theorem Skeleton for the Lens-Nil Z_7 CP Row
---

# Purpose

We now have a strong sevenfold fingerprint:

```text
K_LN =
[2 1
 1 4],
det(K_LN)=7,
SNF(K_LN)=[7].
```

The matrix uses the reduced leading Lens x Nil coefficient fingerprint:

```text
W_1 coefficient: 2,
W_3 coefficient: 1,
leading R_+ coefficient: 4.
```

But this is still a coefficient fingerprint.  The Lens x Nil appendix writes
the curvature coefficients with `O(lambda^2 nu^2)` terms, so the missing proof
has two parts: a descent theorem and an integer-block protection lemma.

# Desired theorem

The theorem should have this form:

```text
Theorem.  In the family-trivial CP sector of the coherent Lens x Nil
background, the residual Wilson/nil character lattice is the cokernel of the
primitive matrix

K_LN = [[2,1],[1,4]].

Therefore the odd CP factor is Z_7.
```

Equivalently:

```text
Gamma_7 = coker(K_LN) ~= Z_7.
```

# Objects

Use:

```text
beta_1, beta_3
```

for the invariant `(2,2)` component basis in the Lens x Nil Bianchi system.

Use:

```text
w
```

for the residual family-trivial Wilson/circle CP character.

Use:

```text
n
```

for the residual nil survivor/termination character.

The target relation matrix is:

```text
2w + n  = 0,
w  + 4n = 0.
```

# Lemma 1: Integral Period Lattice

Needed statement:

```text
The invariant component basis beta_1,beta_3 pairs integrally with the relevant
coherent Lens x Nil cycle basis.
```

Consequence:

```text
component coefficients define integer lattice relations,
not merely real equations for radii.
```

This is where flux quantization and the left-invariant integral basis must be
used.

Status after corpus check:

```text
corpus-supported.
```

The Lens x Nil flux construction states that flux quantization holds because
the 2-forms have integral periods and that `Tr F^2` and `Tr R_+^2` lie in the
span of integral 4-forms `{beta_i}`.  For the Lens x Nil block, the relevant
forms are `beta_1,beta_3`.

Rigor caution:

```text
beta_1,beta_3 are an invariant component basis, not automatically closed
de Rham H^4 generators.
```

The closure check in:

```text
lens_nil_beta_closure_check.py
```

shows that the individual `beta_1,beta_3` forms are not closed under the
Lens x Nil structure equations.  Therefore the descent theorem must be phrased
using the integral Bianchi component lattice or differential-cohomology/gerbe
lattice selected by `Pi_coh`, unless closed representatives are explicitly
constructed.

# Lemma 2: Coherent Projector Descent

Needed statement:

```text
The coherent projector Pi_coh maps the componentwise Bianchi compatibility
conditions to residual flat-character compatibility conditions on (w,n).
```

Consequence:

```text
the same primitive coefficient block acts on the residual phase labels.
```

This is the key no-proxy step.  Without it, the determinant seven remains a
coefficient coincidence.

Status after corpus check:

```text
partly corpus-supported, partly open.
```

The corpus supports:

```text
left-invariant truncation equals coherent projection.
```

The still-open part is the stronger claim:

```text
the projected component lattice is the lattice whose unitary dual carries the
residual CP labels.
```

# Lemma 3: Family-Trivial Restriction

Needed statement:

```text
The descended Lens x Nil block acts on the family-trivial CP sublattice and
does not mix with the Z_3 family holonomy.
```

Consequence:

```text
the odd CP factor is Z_7, while family remains an orthogonal Z_3 kernel.
```

# Lemma 4: Primitive Matrix

Needed statement:

```text
The descended block is primitive:
gcd(2,1,1,4)=1.
```

Consequence:

```text
SNF([[2,1],[1,4]])=[7],
not [1,7] with a hidden common divisor or an imprimitive rescaling.
```

The dual-lattice check adds:

```text
SNF(K^T)=SNF(K)=[7].
```

Thus if the residual CP labels are Pontryagin-dual characters of the component
lattice, the same sevenfold factor appears in the character group.

# Lemma 5: Dyadic Compatibility

Needed statement:

```text
The Lens x Nil Z_7 block is independent of the six-stage shared-circle dyadic
carry block except through the selected diagonal CP character.
```

Consequence:

```text
Z_64 x Z_7 ~= Z_448
```

for the minimal selected CP quotient.

# Proof after the lemmas

Once Lemmas 1-5 hold, the proof is short.

The odd block is:

```text
K_LN =
[2 1
 1 4].
```

Its determinant is:

```text
det(K_LN)=7.
```

Since it is primitive:

```text
SNF(K_LN)=[7].
```

Therefore:

```text
Gamma_7 ~= Z_7.
```

Combining with the dyadic carry:

```text
Gamma_CP,min ~= Z_64 x Z_7 ~= Z_448.
```

If the family row is included:

```text
Gamma_amb ~= Z_64 x Z_7 x Z_3 ~= Z_1344.
```

The selected CP quotient is:

```text
Gamma_amb / Z_3-family ~= Z_448.
```

# Failure modes

The proof fails if:

```text
beta_1,beta_3 are not an integral period basis,
Pi_coh does not preserve the primitive block,
the residual character labels are not (w,n),
family Z_3 mixes into the odd CP block,
or the descended matrix is not [[2,1],[1,4]] up to unimodular equivalence.
```

It also fails if the coefficient block acts only on continuous metric/radius
variables and not on the finite residual character lattice.

# Fixed-point compatibility

The Fixed Points series supports the analytic parts of this theorem:

```text
bounded Riesz coherent projectors,
closed coherent range,
joint B_1/B_2/B_3 projector,
nil noncollapse spectral gap,
disturbance-damping stability,
selection as admissibility.
```

But it does not by itself prove the arithmetic descent.  The required adaptation
is an arithmetic fixed-sector addendum:

```text
fix the integral Bianchi/gerbe/character sector before scalar extension,
define the coherent arithmetic lattice before applying analytic projector
technology,
protect K_LN=[[2,1],[1,4]] as an exact integer block inside that fixed sector.
```

This keeps the analytic FP results intact while adding the lattice data needed
for the `Z_7` proof.

# Immediate technical tasks

The next concrete work is:

```text
1. Make the beta_1,beta_3 integral period pairing explicit.
2. Identify the dual residual character labels w,n.
3. Prove Pi_coh carries the component matrix to the character lattice.
4. Check the descended matrix up to GL(2,Z) row/column operations.
5. Prove the O(lambda^2 nu^2) curvature terms and higher-order corrections do
   not alter the fixed-sector integer block.
6. Recompute SNF and selected character order.
```

# Bottom line

The path to proof is now narrow and useful:

```text
Lens x Nil coefficients already contain the reduced determinant-seven
fingerprint det [[2,1],[1,4]]=7.
Prove coefficient-to-character descent.
Protect the integer block in the fixed arithmetic sector.
Then the Z_7 row is derived.
```

This is the correct next theorem for the MTT flavor CP program.
