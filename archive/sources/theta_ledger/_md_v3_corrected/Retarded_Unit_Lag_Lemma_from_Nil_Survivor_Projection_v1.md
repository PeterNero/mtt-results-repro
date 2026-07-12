---
abstract: |
  We prove the retarded unit-lag lemma under the selected-kernel
  interpretation natural to MTT: the physical quark CP kernel is not the raw
  continuous pre-survivor overlap alone, but the retarded overlap after
  nil-survivor projection to primitive order-64 dyadic labels.  In the
  normalized dyadic coordinate, the lepton/lens branch is the quarter-turn
  u=16.  The quark CP branch must be primitive order 64, hence odd in Z_64,
  and retarded central-circle orientation restricts the branch to the
  predecessor side.  Positive Schur-reduced closure cost then selects the
  unique nearest retarded primitive label, namely 15.  The selected local
  quadratic basin is therefore centered at s=u-16=-1, so its expansion at
  s=0 has rho_q=kappa_q and hence rho_q/kappa_q=1.  Therefore
  0<rho_q/kappa_q<2, q_64=15, and with the Mukai component q_7=2 the CRT gives
  q=79 mod 448.  If one insists instead that rho_q/kappa_q refer to the raw
  pre-survivor continuous kernel before nil selection, then an explicit
  retarded overlap derivative is still needed.
author:
- Peter Nero
date: May 2026
title: |
  Retarded Unit-Lag Lemma from Nil-Survivor Projection
---

# Claim

The remaining lemma can be proved if the phrase "selected retarded overlap
kernel" is understood in the MTT sense:

```text
selected kernel = raw retarded overlap followed by nil-survivor projection.
```

Under that interpretation:

```text
rho_q/kappa_q = 1.
```

Hence:

```text
0 < rho_q/kappa_q < 2.
```

This closes the dyadic amplitude gate for the CKM label.

# Setup

Use the selected dyadic coordinate:

```text
u in R/64Z.
```

The lepton/lens branch is the quarter-turn:

```text
u_l = 16.
```

Let:

```text
s = u - 16.
```

The selected Schur-reduced closure cost near the quarter-turn has positive
quadratic form:

```text
C_eff(s) = C_0 + 1/2 kappa_q s^2 + O(s^3),
kappa_q > 0.
```

This positivity follows from the closure-strain normal form after removing
gauge-flat directions and Schur-reducing nuisance coordinates.

# Primitive Quark Constraint

The quark CP dyadic component must carry the full order-64 dyadic character.
In `Z_64`, the primitive labels are exactly the odd labels:

```text
1,3,5,...,63.
```

The labels adjacent to the quarter-turn are:

```text
15 < 16 < 17.
```

Thus the nearest primitive predecessor is:

```text
15.
```

The nearest primitive successor is:

```text
17.
```

# Retarded Orientation

Central-circle time ordering and projection-induced noninvertibility select
the retarded side of the quarter-turn.  Therefore the quark CP branch is
restricted to primitive labels below the lepton quarter-turn on the selected
local lift:

```text
P_- = {p in Z_64 primitive : p < 16}.
```

Concretely:

```text
P_- = {1,3,5,7,9,11,13,15}.
```

# Nil-Survivor Projection Principle

Nil termination does not leave a continuum of physical labels.  It projects to
discrete survivor basins.  In the zero-width survivor limit, the selected
retarded label is the admissible survivor minimizing the Schur-reduced closure
cost:

```text
p_* = argmin_{p in P_-} 1/2 kappa_q (p-16)^2.
```

Since:

```text
kappa_q > 0,
```

this is equivalent to minimizing:

```text
|p-16|.
```

The unique minimizer is:

```text
p_* = 15.
```

# Theorem

Assume:

1.  the selected dyadic CP factor is `Z_64`;

2.  the lepton branch is the quarter-turn `u_l=16`;

3.  quark CP labels are primitive order-64 labels;

4.  retarded central-circle orientation restricts the quark branch to the
    predecessor side;

5.  nil-survivor projection selects the lowest Schur-reduced closure cost among
    admissible retarded primitive survivors.

Then the selected dyadic quark label is:

```text
q_64 = 15.
```

Moreover the selected local basin is centered at:

```text
s_* = 15 - 16 = -1.
```

Therefore, in the selected-kernel expansion:

```text
J_sel(s)
= J_0 + 1/2 kappa_q (s+1)^2 + O((s+1)^3).
```

Expanding at the quarter-turn `s=0` gives:

```text
J_sel(s)
= J_0'
 + kappa_q s
 + 1/2 kappa_q s^2
 + O(s^3).
```

Thus:

```text
rho_q = kappa_q,
rho_q/kappa_q = 1.
```

Consequently:

```text
0 < rho_q/kappa_q < 2.
```

# Proof

The retarded primitive set below the quarter-turn is finite and nonempty.
Because `kappa_q>0`, the Schur-reduced quadratic cost is strictly increasing
with the distance from `16`.  Among primitive retarded labels:

```text
1,3,5,7,9,11,13,15,
```

the unique closest label to `16` is `15`.  Therefore nil-survivor projection
selects `15`.

The selected basin has center `s=-1`.  A positive quadratic basin centered at
`s=-1` is:

```text
1/2 kappa_q (s+1)^2.
```

Expanding around `s=0` gives linear coefficient `kappa_q` and quadratic
coefficient `kappa_q`.  Therefore:

```text
rho_q/kappa_q = 1.
```

This proves the lemma.

# CRT Consequence

The selected Mukai component is:

```text
q_7 = 2.
```

Solving:

```text
q = 15 mod 64,
q = 2  mod 7
```

gives:

```text
q = 79 mod 448.
```

The phase-sum partner to the lepton label `l=336` is:

```text
r = -(79+336) = 33 mod 448.
```

# Relation to the Empirical CKM Target

The CKM/Jarlskog benchmark previously used in the admissibility filter gives:

```text
epsilon_target = 0.999560473758.
```

Exact unit lag gives:

```text
epsilon_MTT = 1.
```

The difference is:

```text
epsilon_target - 1
= -4.395262419337e-4.
```

So the empirical target is extremely close to the exact unit-lag theorem.

The small mismatch should be interpreted as one of:

1.  experimental/benchmark convention and RG/threshold drift;

2.  a small finite-width correction to the zero-width survivor kernel;

3.  a sign that the raw pre-survivor overlap kernel has a tiny realization
    correction before nil projection.

It should not be treated as a freely adjustable fit parameter.

# Important Caveat

This proof closes the lemma for the selected nil-projected kernel.

It does not compute the raw pre-survivor continuous kernel derivative:

```text
r_u,
r_eta.
```

Therefore there are two logically distinct readings.

## Reading A: Selected MTT Kernel

If the physical CKM branch is selected only after nil-survivor filtering, then
the proof above applies and:

```text
rho_q/kappa_q = 1.
```

This is the natural MTT reading because nil termination is part of physical
survivor selection.

## Reading B: Raw Continuous Kernel

If `rho_q/kappa_q` is required to describe the raw continuous overlap before
nil-survivor projection, then the proof above does not supply the raw
derivative.  One must still compute:

```text
rho_q = r_u - b^T D^{-1} r_eta,
kappa_q = a - b^T D^{-1} b.
```

from an explicit realization.

# Verification

The script:

```text
retarded_unit_lag_projection_proof.py
```

checks:

```text
retarded primitive minimizer: 15
epsilon from projection:     1.000000000000
q448 from (15,2):            79
```

and records the only remaining condition:

```text
selected kernel equals nil-survivor projection     CONDITIONAL
raw pre-survivor kernel amplitude computed         OPEN
```

# Gate Status

```text
finite Z_64 primitive predecessor theorem             PROVED
positive Schur cost selects nearest retarded primitive PROVED
selected nil-projected rho_q/kappa_q=1                PROVED
0<rho_q/kappa_q<2 for selected kernel                 PROVED
q_64=15 and q_7=2 imply q=79                           PROVED
selected kernel includes nil-survivor projection       MTT-EXECUTION THEOREM*
raw pre-survivor derivative computed                   OPEN
```

`*` See `Selected_Kernel_Principle_for_CKM_CP_in_MTT_v1.md`: the selected
kernel follows from post-projection observability, nil-survivor execution, and
finite CP character descent.  See also
`Nil_Survivor_Execution_Theorem_for_Selected_CKM_CP_v1.md`: the abstract
nil-survivor execution theorem is proved; the concrete MTT nil operator
`N_MTT` and closure-strain Hessian remain open.

# Bottom Line

The remaining lemma is proved for the selected MTT kernel:

```text
rho_q/kappa_q = 1.
```

The proof uses no CKM numerical input.  It uses only:

```text
Z_64 dyadic carry,
primitive quark CP admissibility,
retarded central-circle orientation,
positive Schur-reduced closure cost,
nil-survivor projection by minimal closure cost.
```

Under those assumptions, the CKM numerator branch follows:

```text
q_64=15,
q_7=2,
q=79,
l=336,
r=33.
```
