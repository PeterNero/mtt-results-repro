---
abstract: |
  We isolate the physical sign needed to turn the dyadic pre-quarter rule into
  an MTT theorem.  The corpus supports a universal orientation of the shared
  central circle, projection-induced noninvertibility, CP phases from
  central-circle overlap geometry, and nil survivor-basin selection.  These
  facts justify formulating, but do not yet prove, a retarded shared-circle
  orientation lemma: the quark CP dyadic branch is the primitive survivor
  immediately before the lepton quarter-turn in the oriented Z_64 refinement.
  The finite consequences are exact.  The retarded/pre-quarter orientation
  gives q_64=15 and hence q=79 after combining with the Mukai q_7=2 component.
  The advanced/post-quarter orientation gives a different label.  Thus the
  final non-empirical numerator proof reduces to the sign and size of one
  dyadic overlap displacement.
author:
- Peter Nero
date: May 2026
title: |
  Retarded Shared-Circle Orientation Gate for the Dyadic Pre-Quarter CKM Branch
---

# Purpose

The previous notes reduced the CKM numerator problem to:

```text
q = CRT(q_64,q_7),
q_7 = 2,
q_64 = 15.
```

The Mukai block supplies `q_7=2`.  The remaining question is whether MTT
selects:

```text
q_64 = 15 = 16-1.
```

This paper turns that into a precise physical sign gate.

# Corpus support

The corpus gives four useful ingredients.

First, the central circle is the unique shared coherence channel.  It is also
the structure through which effective time ordering is enforced.

Second, the central-circle paper ties time orientation to successive coherent
projections: coherent configurations must align their internal phase along the
central circle, and successive projections impose a monotonic ordering of this
alignment.

Third, the same central circle controls Yukawa selection, relative phase
alignment, and CP-violating phases through overlap integrals.

Fourth, the closure-strain corpus gives the relevant sector asymmetry:
neutrino sectors are soft, charged leptons are stiff but fully anchored, and
quarks are partially anchored composite sectors with maximal effective
stiffness.  It also states that CP-odd effects are stiffness-modulated.

Fifth, the proto-spinor/worldsheet bridge identifies nil with discrete
survivor-basin selection.  Locally, a survivor label is represented by a basin
potential around an admissible discrete label.

Together these facts support an oriented finite survivor rule on the selected
dyadic character.  They do not yet prove which side of the quarter-turn is
selected.

# Dyadic orientation variable

Let

```text
Z_64
```

be the selected dyadic CP factor.

The lepton/lens quarter-turn is:

```text
l_64 = 16.
```

Let `u_q` be the real-valued dyadic coordinate of the quark CP overlap before
sharp survivor projection.  The primitive survivor filter restricts the final
label to odd integers in `Z_64`.

The `q_64=15` survivor is selected exactly when:

```text
14 < u_q < 16.
```

Equivalently, if

```text
u_q = 16 - epsilon,
```

then the needed condition is:

```text
0 < epsilon < 2.
```

The sign `epsilon>0` is the retarded/pre-quarter orientation.  The bound
`epsilon<2` says the branch remains in the nearest primitive survivor cell.

# Retarded orientation lemma candidate

#### Lemma candidate

In the oriented shared-circle dyadic refinement, the quark CP overlap branch
approaches the lens/lepton quarter-turn from the retarded side and remains in
the adjacent primitive survivor cell:

```text
u_q = 16 - epsilon,      0 < epsilon < 2.
```

Then the sharp dyadic survivor is:

```text
q_64 = 15.
```

#### Proof of finite consequence

Primitive order-64 labels are odd.  The adjacent primitive labels around the
quarter-turn are:

```text
15 < 16 < 17.
```

If `14<u_q<16`, then the nearest primitive survivor is uniquely `15`.  The
phase-sum partner is then:

```text
r_64 = -(15+16)=33 mod 64.
```

This proves the finite consequence.  The unresolved part is the MTT derivation
of the sign and bound on `epsilon`.

# Alternative orientations

The check script

```text
dyadic_orientation_gate_scan.py
```

compares the finite alternatives.

```text
retarded/pre-quarter:  q_64=15, q_7=2 -> q=79
advanced/post-quarter: q_64=17, q_7=2 -> q=401
unoriented:            twofold ambiguity {15,17}
```

With the lepton and phase-sum labels included:

```text
pre-quarter triple:  (q,l,r)=(79,336,33)
post-quarter triple: (q,l,r)=(401,336,159)
```

Both satisfy abstract closure.  Only the retarded/pre-quarter orientation gives
the `q=79` branch.

# What must be proved next

The physical proof is now a derivative/sign calculation, not a search over
hundreds of labels.

One must compute the dyadic projection of the selected overlap phase:

```text
u_q = P_64 arg sum_gamma A_gamma exp(-S_gamma) chi_gamma,
```

and prove:

```text
14 < u_q < 16.
```

Equivalently, near the lens quarter-turn one must show that the first
nonvanishing displacement is retarded:

```text
u_q - 16 < 0,
```

and smaller than two dyadic units in magnitude.

# Why this is plausible but not finished

It is plausible because the corpus already says:

```text
central circle -> universal orientation,
projection -> noninvertible/retarded effective ordering,
Yukawa/CP phases -> central-circle overlap geometry,
quark sector -> stiff partially anchored closure geometry,
nil -> discrete survivor labels.
```

But plausibility is not proof.  The current manuscripts still need an actual
calculation of the overlap displacement or a theorem deriving its sign from
sector stiffness, retarded boundary conditions, or closure-strain geometry.

# Gate status

```text
central-circle orientation exists in corpus              SUPPORTED
CP phases come from central-circle overlap geometry      SUPPORTED
quark stiffness gives a plausible lag mechanism          SUPPORTED
nil/survivor filtering gives discrete labels             SUPPORTED
pre-quarter orientation gives q_64=15                    PASS
post-quarter orientation gives different label           PASS
MTT proves u_q=16-epsilon with 0<epsilon<2               OPEN
```

# Bottom line

The remaining numerator problem has become one clean sign-and-cell theorem:

```text
prove the quark CP dyadic overlap lies in the retarded cell immediately before
the lepton quarter-turn.
```

If MTT proves that, then:

```text
q_64=15,
q_7=2,
CRT(q_64,q_7)=79.
```
