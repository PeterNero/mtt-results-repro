---
abstract: |
  We test whether the final retarded-Schur coefficient gate for the CKM label
  q=79 can be closed from the current MTT corpus.  The result is sharply mixed
  and useful.  The positive-definite closure-strain normal form supports
  D>0, and the Schur complement then proves kappa_q>0 under the selected
  Hessian positivity hypothesis.  Retarded central-circle orientation supports
  rho_q>0 once the selected retarded kernel is fixed.  However, the upper
  adjacent-cell bound rho_q<2 kappa_q is not a consequence of positivity; it
  is the remaining amplitude theorem.  The natural missing statement is a
  Retarded Unit-Lag Lemma: in the normalized dyadic coordinate, the selected
  retarded overlap force is one Schur stiffness unit up to a strict cell
  margin.  Exact unit lag gives q_64=15 and hence q=79, and the empirical
  CKM/Jarlskog target requires epsilon=0.999560473758, only
  -4.395262419337e-4 from unit lag.
author:
- Peter Nero
date: May 2026
title: |
  Retarded-Schur Gate Audit and the Unit-Lag Lemma for CKM q=79
---

# Question

Can we now make the final gate work?

The gate is:

```text
D > 0,
kappa_q > 0,
0 < rho_q < 2 kappa_q.
```

If it holds, then:

```text
epsilon_MTT = rho_q/kappa_q in (0,2),
q_64 = 15,
q_7 = 2,
q = 79 mod 448.
```

# What the Corpus Already Supplies

The closure-strain paper supplies the structural normal form:

```text
J(s_align + delta s)
= J_0 + 1/2 delta s^T H delta s + O(||delta s||^3),
```

with `H` restricted to anchored, non-redundant directions.  It also states
that quark mixing is small because the quark sector is stiff: quark
generation changes require re-solving composite closure across lens/color
channels.

This is exactly the setting needed for a Schur-reduced coefficient theorem.

The central-circle paper supplies the shared phase channel:

```text
S^1_cen
```

as the unique common coherence bookkeeping channel controlling Yukawa phases,
relative phases, and CP-violating phases.

The topology-only papers supply the phase-sum rule.  The current `Z_64 x Z_7`
program supplies:

```text
Z_64  from recursive shared-circle dyadic carry,
Z_7   from the selected Mukai discriminant block,
q_7   = 2.
```

# Gate 1: D > 0

Let the selected local coordinates be:

```text
s   = u - 16,
eta = nuisance coordinates after removing gauge-flat directions.
```

Write the selected closure Hessian as:

```text
H =
[ a   b^T ]
[ b    D  ].
```

If the selected closure Hessian is positive definite on the anchored reduced
quark tangent space, then every principal/restricted nuisance block is positive
on the admissible nuisance subspace:

```text
D > 0.
```

This is not a numerical CKM fit.  It follows from the local alignment minimum
and the removal of gauge-flat directions.

Status:

```text
D > 0       SUPPORTED structurally,
            PROVED once the selected quotient tangent space is specified.
```

# Gate 2: kappa_q > 0

The Schur-reduced stiffness is:

```text
kappa_q = a - b^T D^{-1} b.
```

If:

```text
H > 0
```

and:

```text
D > 0,
```

then the Schur complement is positive:

```text
kappa_q > 0.
```

So the stiffness gate is essentially closed by the closure-strain normal form,
provided the selected quark CP direction belongs to the anchored positive
subspace and not a gauge-flat quotient direction.

Status:

```text
kappa_q > 0       PROVED-CONDITIONAL.
```

# Gate 3: rho_q > 0

The Schur-reduced retarded force is:

```text
rho_q = r_u - b^T D^{-1} r_eta.
```

The central-circle and retarded-orientation material support the sign:

```text
rho_q > 0.
```

But this sign is not merely a convention after the kernel is fixed.  It must
come from the selected retarded overlap derivative.  In kernel language:

```text
Y_q(s,eta)
= sum_gamma A_gamma(s,eta) exp(-S_gamma(s,eta)) chi_gamma(s,eta),
```

and:

```text
r_i = partial_i R_q(0,0).
```

The selected retarded branch must give:

```text
r_u - b^T D^{-1} r_eta > 0.
```

Status:

```text
rho_q > 0       SUPPORTED by retarded orientation,
                still requires selected-kernel sign extraction.
```

# Gate 4: rho_q < 2 kappa_q

This is the key point.

The upper bound:

```text
rho_q < 2 kappa_q
```

does not follow from:

```text
D > 0,
kappa_q > 0,
rho_q > 0.
```

The audit script constructs positive-stiffness algebra witnesses where:

```text
rho_q/kappa_q > 2
```

and the dyadic survivor becomes:

```text
q_64 = 13,
```

not `15`.

Therefore the amplitude bound is a genuine theorem obligation.

Status:

```text
rho_q < 2 kappa_q       OPEN.
```

# The Natural Missing Lemma

The missing statement should be formulated as a unit-lag theorem.

## Retarded Unit-Lag Lemma

In the selected normalized dyadic coordinate `u`, after Schur reduction over
all nuisance directions, the retarded shared-circle overlap force satisfies:

```text
0 < rho_q/kappa_q < 2.
```

The strong form is:

```text
rho_q/kappa_q = 1 + delta,
|delta| < 1.
```

The strongest and cleanest form is exact unit lag:

```text
rho_q/kappa_q = 1.
```

Exact unit lag gives:

```text
u_q = 16 - 1 = 15,
q_64 = 15.
```

Then with:

```text
q_7 = 2,
```

the CRT gives:

```text
q = 79 mod 448.
```

# Empirical Check

The CKM/Jarlskog benchmark already used in the q=79 admissibility notes gives:

```text
epsilon_target = 0.999560473758.
```

Thus:

```text
epsilon_target - 1
= -4.395262419337e-4.
```

So the data demand an almost exact unit lag.

This is important.  It means the right theorem is probably not a delicate
free numerical fit.  It is likely a normalized one-step retarded-carry
statement:

```text
retarded shared-circle carry shifts the quark CP branch one primitive dyadic
step before the lepton quarter-turn.
```

# Why Positivity Is Not Enough

The script:

```text
retarded_schur_gate_status_audit.py
```

prints:

```text
unit-lag witness epsilon:              1.000000000000 q64: 15 q: 79
too-large positive-force epsilon:      2.446854663774 q64: 13
wrong-sign witness epsilon:           -0.203904555315 q64: 17
empirical epsilon_target:              0.999560473758 q64: 15 q: 79
```

This proves:

1.  Exact unit lag is sufficient.

2.  The empirical target is almost exact unit lag.

3.  Positive Hessian and positive force alone do not prove the adjacent-cell
    bound.

# Correct Way Forward

The next proof should be the Retarded Unit-Lag Lemma.  It can be attempted in
three equivalent ways.

## Route A: Direct Kernel Derivative

Compute:

```text
r_u,
r_eta
```

from:

```text
Y_q(s,eta)
= sum_gamma A_gamma exp(-S_gamma) chi_gamma.
```

Then evaluate:

```text
rho_q = r_u - b^T D^{-1} r_eta,
kappa_q = a - b^T D^{-1} b.
```

Pass condition:

```text
0 < rho_q/kappa_q < 2.
```

This is the most direct route.

## Route B: Unit Carry Normalization

Prove that the selected retarded kernel is not arbitrary: in the normalized
dyadic coordinate, its first nonzero displacement is one carry unit.

In formula form:

```text
rho_q = kappa_q + error,
|error| < kappa_q.
```

This proves:

```text
0 < rho_q/kappa_q < 2.
```

Exact unit carry gives:

```text
rho_q = kappa_q.
```

This route matches the empirical target best.

## Route C: Norm Bound

Use the sufficient Schur inequalities:

```text
a > ||b||^2/lambda_min(D),
r_u > ||b|| ||r_eta||/lambda_min(D),
r_u + ||b|| ||r_eta||/lambda_min(D)
  < 2(a - ||b||^2/lambda_min(D)).
```

This is less elegant, but it is robust once explicit blocks are available.

# Does It Work Out?

The answer is now two-tiered:

```text
For the selected nil-projected MTT kernel: yes, conditionally proved.
For the raw pre-survivor continuous kernel: still open.
```

The finite arithmetic works.

The Schur reduction works.

The stiffness gate works conditionally from the positive closure-strain normal
form.

The empirical target lands almost exactly on unit lag.

The new successor note proves the first reading by showing that nil-survivor
projection of the positive Schur cost selects the unique nearest retarded
primitive label:

```text
q_64 = 15 = 16 - 1,
rho_q/kappa_q = 1.
```

The remaining raw-kernel gap is:

```text
compute the pre-survivor derivative
rho_q = r_u - b^T D^{-1} r_eta
from an explicit overlap realization.
```

# Gate Status

```text
finite Z_64 x Z_7 arithmetic                         PROVED
q_7=2 Mukai component                                 PROVED in current candidate
epsilon in (0,2) -> q_64=15                           PROVED
q_64=15 and q_7=2 -> q=79                             PROVED
D>0 from selected positive Hessian                    CONDITIONAL/SUPPORTED
kappa_q>0 from Schur complement                       PROVED-CONDITIONAL
rho_q>0 from retarded orientation                     SUPPORTED, kernel sign needed
rho_q<2kappa_q for raw pre-survivor kernel            OPEN
rho_q<2kappa_q for selected nil-projected kernel      PROVED-CONDITIONAL
exact unit-lag theorem for selected kernel            PROVED-CONDITIONAL
full q=79 proof using selected kernel                 PROVED-CONDITIONAL
```

# Bottom Line

The selected-kernel proof is now reduced to, and supplied by, the successor
unit-lag theorem:

```text
Retarded Unit-Lag Lemma:
epsilon_MTT = rho_q/kappa_q = 1
```

If one insists on the raw pre-survivor kernel instead, then the Schur formula
remains the exact calculation to do:

```text
epsilon_raw
= [r_u - b^T D^{-1} r_eta] / [a - b^T D^{-1} b].
```

For the selected nil-projected kernel, the CKM numerator branch closes
conditionally:

```text
q_64 = 15,
q_7 = 2,
q = 79,
l = 336,
r = 33.
```
