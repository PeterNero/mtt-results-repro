---
abstract: |
  We isolate and formalize the selected-kernel principle needed to promote the
  CKM q=79 result from an interpretive condition to an explicit MTT execution
  theorem.  The principle is not a new numerical assumption.  It follows from
  the MTT observability contract once three structural premises are accepted:
  physical quantities are recordable only after coherent projection, nil
  directions terminate in discrete survivor basins, and CP data are unitary
  characters of the selected finite quotient.  Under these premises, the
  physical CKM CP kernel cannot be the raw continuous pre-survivor overlap
  alone.  It must be the raw retarded overlap reduced along nil-survivor fibers
  to the selected finite CP label.  In the sharp-survivor limit this reduction
  is the minimum closure-cost survivor.  For the dyadic quarter-turn problem,
  primitive order-64 admissibility and retarded predecessor orientation select
  the unique nearest survivor q_64=15, so the selected basin has unit lag and
  rho_q/kappa_q=1.  Thus the q=79 theorem is conditional on standard MTT
  execution premises, not on an empirical CKM fit.  What remains open is a
  deeper dynamical derivation of nil-survivor execution itself, or alternatively
  an explicit raw pre-survivor Hessian calculation.
author:
- Peter Nero
date: May 2026
title: |
  The Selected-Kernel Principle for CKM CP in Modal Triplet Theory
---

# Purpose

The previous retarded unit-lag lemma proved:

```text
selected nil-projected kernel -> rho_q/kappa_q=1 -> q_64=15.
```

The open interpretive condition was:

```text
physical CKM kernel = selected nil-projected retarded kernel,
not merely the raw continuous pre-survivor kernel.
```

This paper turns that condition into a precise MTT execution principle.

The result is not a proof from bare QFT or bare Hilbert-space QM.  It is a
proof from the MTT observability contract:

```text
recordable physics lives after coherent projection and survivor selection.
```

Once that contract is accepted, a raw pre-survivor coordinate is not itself a
physical CP observable.  It is upstream data used to determine the selected
survivor.

# Executive Claim

Let:

```text
X_raw      = raw local modal/overlap configuration space,
Pi_coh     = coherent projection,
pi_nil     = nil-survivor projection,
pi_CP      = projection to the selected finite CP quotient,
E_CP       = pi_CP o pi_nil o Pi_coh.
```

Then the physical CKM CP observable must factor through:

```text
E_CP: X_raw -> Gamma_CP.
```

Equivalently, there is a function `O_CP` on the selected finite CP quotient
such that:

```text
O_CKM^phys = O_CP o E_CP.
```

Therefore the physical CKM CP kernel is the selected kernel:

```text
K_CKM^phys = K_sel,
```

where `K_sel` is the fiber-reduced raw retarded overlap:

```text
K_sel(g)
= Reduce_{x in E_CP^{-1}(g)}
   [K_raw^ret(x), C_cl(x)].
```

In the sharp nil-survivor limit, `Reduce` is closure-cost minimization:

```text
J_sel(g)
= min_{x in E_CP^{-1}(g)}
   [J_raw^ret(x)+C_cl(x)].
```

# The Three MTT Premises

## Premise 1: coherent-sector observability

MTT treats stable observables, amplitudes, probabilities, and records as
post-projection quantities.  The corrected theta-closure papers already use:

```text
Pi = Pi_B1 Pi_B2 Pi_B3,
```

with a bounded coherent projection and a spectral gap separating coherent from
noncoherent modes.

The physical statement is:

```text
if the coherent projection is ill-defined, stable physics is ill-defined.
```

Thus a raw modal coordinate before coherent projection is not directly
observable.

## Premise 2: nil termination gives survivor basins

The MTT flavor corpus repeatedly treats nil termination as a discrete
survivorship mechanism.  In the flavor program this is the reason nil data may
carry family/generation structure and finite residual labels.

For CKM CP, the needed form is:

```text
pi_nil: X_coh -> S_nil,
```

where `S_nil` is a finite or locally finite survivor set.  Continuous
pre-survivor coordinates may influence which survivor is selected, but they are
not themselves the final recordable CP labels.

## Premise 3: CP phases are selected finite characters

The order-448 program already localized the physical CP phase to:

```text
Gamma_CP ~= Z_64 x Z_7 ~= Z_448,
```

with an ambient family carrier:

```text
Gamma_amb ~= Z_64 x Z_7 x Z_3 ~= Z_1344,
```

and family quotient:

```text
Gamma_CP = Gamma_amb / Z_3-family.
```

The CP labels are unitary characters of the selected finite quotient.  Hence
the physical CP phase is not a real-valued raw coordinate.  It is a selected
finite character label.

# Definition: Raw Kernel

The raw retarded overlap kernel is the pre-survivor object computed from
localized overlap data before nil selection:

```text
K_raw^ret(x)
= sum_gamma A_gamma(x) exp(-S_gamma(x)) chi_gamma(x),
```

or, at the real cost level:

```text
J_raw^ret(x) = Phi(K_raw^ret(x), conjugate(K_raw^ret(x))).
```

This object is essential.  It supplies the retarded force and can distinguish
which survivor basin wins.  But by itself it is not yet a final MTT observable
unless it is invariant along execution fibers.

# Definition: Selected Kernel

Define the execution map:

```text
E_CP = pi_CP o pi_nil o Pi_coh.
```

For a selected finite CP label `g in Gamma_CP`, define the selected cost:

```text
J_sel(g)
= min_{x in E_CP^{-1}(g)}
   [J_raw^ret(x)+C_cl(x)].
```

Here `C_cl` is the closure-strain cost.  More generally the minimum may be
replaced by the stationary-phase, Schur-Feshbach, or finite-width survivor
reduction appropriate to the coherence regime.  In the sharp-survivor limit
used in the q=79 branch, the minimum is the correct local reduction.

The selected kernel is:

```text
K_sel = fiber reduction of K_raw^ret along E_CP.
```

# Theorem: Post-Projection Factorization

Assume:

1.  physical CKM CP quantities are stable recordable observables;

2.  stable recordable observables in MTT are defined on the coherent survivor
    sector;

3.  the CKM CP label is a character of the selected finite quotient
    `Gamma_CP`;

4.  two raw configurations with the same selected CP label are physically
    indistinguishable as CP-label observations.

Then the physical CKM CP observable factors through the selected finite
quotient:

```text
O_CKM^phys = O_CP o E_CP.
```

Consequently, the physical CKM CP kernel is the selected kernel, not the raw
pre-survivor kernel.

## Proof

Let `x,x' in X_raw` satisfy:

```text
E_CP(x)=E_CP(x').
```

By premise 4, `x` and `x'` are physically indistinguishable for the CKM CP
label.  Therefore:

```text
O_CKM^phys(x)=O_CKM^phys(x').
```

Thus `O_CKM^phys` is constant on the fibers of `E_CP`.  By the universal
property of quotients, any function constant on the fibers of `E_CP` factors
uniquely through the image quotient:

```text
O_CKM^phys = O_CP o E_CP.
```

This proves factorization.

Now suppose the raw kernel `K_raw^ret` varies along a fiber of `E_CP`.  Then
`K_raw^ret` cannot itself be the final physical CKM CP observable, because it
distinguishes raw configurations that are indistinguishable by the selected CP
record.  The physical kernel must be the fiber-reduced object `K_sel`.

This proves the selected-kernel principle.

# Corollary: Fiber Reduction is Not a Fit

The selected kernel is not an extra fitting knob.  It is the quotient-reduced
observable forced by MTT execution.

The raw kernel still matters through:

```text
1. survivor weights,
2. finite-width corrections,
3. retarded orientation,
4. Schur-reduced local forces,
5. possible RG or threshold drift after matching.
```

But the label observed in the sharp CP quotient is the selected survivor label.

# Application to the Dyadic CKM Branch

Use the selected dyadic coordinate:

```text
u in R/64Z,
s = u-16.
```

The lepton/lens branch is:

```text
u_l = 16.
```

The quark CP dyadic component must be primitive of order 64.  Thus admissible
dyadic labels are odd:

```text
1,3,5,...,63.
```

Retarded central-circle orientation restricts the quark branch to the
predecessor side of the quarter-turn:

```text
P_- = {1,3,5,7,9,11,13,15}.
```

The sharp selected-kernel cost is:

```text
J_sel(p)
= 1/2 kappa_q (p-16)^2,
kappa_q>0,
p in P_-.
```

The unique minimizer is:

```text
p_*=15.
```

Therefore:

```text
q_64=15.
```

The selected local basin has center:

```text
s_*=-1.
```

So:

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
rho_q/kappa_q = 1,
0 < rho_q/kappa_q < 2.
```

# CKM q=79 Consequence

The Mukai odd component supplies:

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

The lepton quarter-turn and phase-sum partner are:

```text
l=336,
r=33,
79+336+33=448.
```

# Relation to the Raw Schur Formula

The raw pre-survivor Schur calculation remains meaningful.  It computes:

```text
rho_raw = r_u - b^T D^{-1} r_eta,
kappa_raw = a - b^T D^{-1} b.
```

If one requires the raw continuous kernel itself to land in the q=79 cell, the
open condition remains:

```text
kappa_raw > 0,
0 < rho_raw < 2 kappa_raw.
```

The selected-kernel principle says something slightly different:

```text
the physical CP label is selected after nil-survivor projection.
```

Therefore:

```text
rho_sel/kappa_sel = 1
```

in the sharp selected basin, even if the raw kernel contains small realization
or finite-width corrections.

# What This Does and Does Not Prove

This paper proves:

```text
post-projection observability + nil survivorship + finite CP characters
=> physical CKM CP kernel is selected/fiber-reduced.
```

It also proves:

```text
selected/fiber-reduced dyadic kernel
=> q_64=15
=> q=79 with q_7=2.
```

It does not yet prove dynamically:

```text
why nil termination must have exactly this survivor projection,
why the Z_64 carry rows are selected,
why the Mukai Z_7 block is selected by a full compactification,
or why finite-width corrections have the observed small size.
```

Those remain downstream gates.

# Gate Status

```text
coherent-sector observability                         MTT premise, corpus-supported
nil termination as survivor projection                THEOREM-SCHEMA*
CP labels as selected finite characters               PROVED-CONDITIONAL in quotient papers
post-projection factorization theorem                 PROVED
raw kernel cannot be final observable if fiber-varying PROVED
selected sharp survivor chooses q_64=15               PROVED
CRT with q_7=2 gives q=79                              PROVED
raw pre-survivor inequality                            OPEN
concrete MTT nil operator N_MTT supplied               OPEN
```

`*` See `Nil_Survivor_Execution_Theorem_for_Selected_CKM_CP_v1.md`: nilpotent
execution plus positive closure cost and a finite CP quotient imply sharp
survivor projection.  The concrete MTT operator `N_MTT` and its closure-strain
Hessian remain to be identified.

# Revised Status of the q=79 Proof

Before this paper, the proof status was:

```text
q=79 is proved if selected kernel means nil-projected kernel.
```

After this paper, the proof status is:

```text
q=79 is an MTT execution theorem conditional on:
1. coherent-sector observability,
2. nil-survivor execution,
3. selected finite CP quotient Z_64 x Z_7,
4. retarded predecessor orientation,
5. positive Schur-reduced closure cost.
```

This is a stronger and cleaner state.  The selected-kernel step is no longer
an informal interpretation.  It is a quotient/factorization theorem from the
MTT execution contract.

# Next Proof Obligation

The next foundational target is now sharper:

```text
identify the concrete MTT nil operator N_MTT and closure-strain Hessian.
```

Equivalently:

```text
show that the actual MTT nil/coherence dynamics satisfies the hypotheses of
the nil-survivor execution theorem, with the primitive order-64 retarded branch
as the relevant quark CP admissibility set.
```

The parallel constructive target is:

```text
derive the Z_64 carry rows from recursive shared-circle topology.
```

# Bottom Line

The q=79 branch now rests on a clean execution chain:

```text
coherent projection
-> nil survivor projection
-> selected finite CP quotient
-> retarded primitive predecessor
-> q_64=15
-> q_7=2
-> q=79.
```

This does not finish the Standard Model.  It does finish the selected-kernel
hinge needed for the current CKM CP numerator theorem, modulo the named MTT
execution premises.
