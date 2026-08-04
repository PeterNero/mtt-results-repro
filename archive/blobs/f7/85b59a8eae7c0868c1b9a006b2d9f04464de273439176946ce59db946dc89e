---
abstract: |
  We evaluate the current state of the MTT order-448 CP program after the
  Lens-Nil obstruction, the Fu-Yau/K3 turn, and the positive Mukai charge
  replacement and fixed-sector selection reduction.  The finite abelian arithmetic is now strong: the selected
  quotient is Z_64 x Z_7 ~= Z_448 and the ambient family carrier is
  Z_64 x Z_7 x Z_3 ~= Z_1344, with the family Z_3 in the kernel of the
  selected CP character.  What remains open is geometric selection.  The
  Lens-Nil coefficient route is blocked, the negative K3 H^2 route is
  root-obstructed, and the live odd-factor route is a positive determinant-
  seven block in the algebraic Mukai charge lattice.  However, that Mukai
  block should currently be treated as a charge-lattice block, not as two
  same-slope HYM bundle summands.  The fixed-sector MTT selection part is
  now closed once a Bianchi-compatible Mukai sector is supplied.  The forward
  program splits into a fast conditional theorem, a primary global Mukai/Fu-Yau route, a hard full
  heterotic bundle route, a dyadic shared-circle carry proof, and an M-theory
  flux-lattice backup.
author:
- Peter Nero
date: May 2026
title: |
  State of Proof and Ways Forward for the MTT Order-448 CP Program
---

# Executive state

The program has moved from numerology to a precise conditional theorem.

The strongest honest statement is:

```text
If MTT selects:
1. a dyadic shared-circle carry block with invariant factor 64,
2. a Bianchi-compatible Fu-Yau/Mukai sector supplies a positive Mukai charge block with invariant factor 7,
3. a family Z3 factor orthogonal to the CP character,
4. the CP labels as unitary characters of the selected quotient,

then the selected CP character has order 448.
```

The finite arithmetic behind this is solid:

```text
Z_64 x Z_7 ~= Z_448,
Z_64 x Z_7 x Z_3 ~= Z_1344,
Z_1344 / Z_3-family ~= Z_448.
```

The open problem is no longer "why 448 fits."  It is:

```text
why the global geometry supplies exactly these finite character data.
```

# What is now proved

## Finite quotient arithmetic

The Smith-normal-form checks prove:

```text
six-stage dyadic carry        -> [64],
Mukai determinant-seven block -> [7],
selected product             -> [448],
ambient plus family Z3        -> [1344].
```

The family quotient is explicit:

```text
pi: Z_1344 -> Z_448,
ker(pi)={0,448,896}.
```

The selected CP labels are family-trivial lifts:

```text
k_q  = 237  = 3*79,
k_l  = 1008 = 3*336,
k_31 = 99   = 3*33.
```

They close:

```text
79 + 336 + 33 = 448 = 0 mod 448.
```

So the finite character architecture is internally coherent.

## Lens-Nil is not usable as written

The original Lens-Nil coefficient proof is blocked.

The audit found:

```text
d beta_1 != 0,
d beta_3 != 0,
F=f eta12+h sigma45 gives F^2=2fh beta_2,
not f^2 beta_1+h^2 beta_3.
```

Therefore the original Lens-Nil appendix cannot prove the odd `Z_7` row.
It remains a clue, not a proof source.

## Negative K3 H2 route is root-obstructed

The first Fu-Yau/K3 replacement put:

```text
K=-Gram(v,w)=[[2,1],[1,4]]
```

inside `H^2(K3,Z)`.  This proved the arithmetic, but the block contains a
`(-2)` root.  More strongly, any even rank-two determinant-seven K3 `H^2`
block has a norm-two vector after reduction.  Thus a direct pair of
anti-self-dual K3 two-form curvatures runs into the ample-wall/root-wall issue.

So this route is structurally unsuitable as the final HYM proof.

## Positive Mukai charge block is the live odd source

The current best `Z_7` source is the algebraic Mukai lattice.

On a Picard-rank-one K3 with:

```text
H^2=2,
```

take:

```text
a=(5,H,0),
b=(7,3H,1).
```

The Mukai pairing gives:

```text
<a,a>=2,
<a,b>=1,
<b,b>=4,
Gram_Mukai(a,b)=[[2,1],[1,4]],
SNF=[7].
```

This is the cleanest currently known odd-factor source.

# The new caveat: charge lattice is not yet a bundle

The Mukai block is strong, but it must not be overclaimed.

The two vectors:

```text
a=(5,H,0),
b=(7,3H,1)
```

have different slopes:

```text
mu_H(a)=2/5,
mu_H(b)=6/7.
```

So they do not directly form two summands of one polystable HYM gauge bundle.

In fact, the obstruction is structural.  For Picard rank one and `H^2=2`, if
two Mukai vectors:

```text
x=(r,nH,s),
y=(R,NH,S)
```

have the same slope `n/r=N/R`, then:

```text
det Gram(x,y)=-(rB-RA)^2
```

for rational `A,B`.  So a same-slope determinant-seven Gram block is impossible.

Therefore the Mukai result should be read as:

```text
PASS: determinant-seven charge-lattice block;
OPEN: realization as a single supersymmetric heterotic gauge bundle.
```

# Route ranking

## Route 1: conditional theorem now

This is the fastest rigorous paper result.

State the theorem with explicit assumptions:

```text
A64: recursive shared-circle sector gives invariant factor 64.
A7: a Bianchi-compatible Fu-Yau/K3 sector supplies K_Mukai with SNF [7].
Afix: fixed-sector MTT selection carries that supplied block to the selected
      Strominger fixed point.
Achar: CP labels are Hom(coker K_Mukai,U(1)) on the odd sector.
Afam: family Z3 lies in the kernel of chi_CP.
```

Then the conclusion:

```text
ord(chi_CP)=448.
```

This route is honest and publishable as a conditional structural theorem.  It
does not yet finish the foundational derivation.

## Route 2: Mukai charge-lattice selection

This is the strongest live route to the odd factor.

The goal is not to force `a` and `b` to be HYM summands.  Instead:

```text
the fixed Fu-Yau/K3 differential K-theory or Mukai charge lattice contains a
selected finite quotient with relation matrix K_Mukai.
```

Then CP phases are unitary characters:

```text
Hom(coker K_Mukai,U(1)).
```

This route avoids the same-slope obstruction.  The fixed-sector selection map
is now proved by the Strominger selection theorem once the sector is supplied:

```text
fixed topological sector -> integral charge lattice -> finite character quotient.
```

The remaining work is global topological-sector construction/choice.

## Route 3: full heterotic Fu-Yau bundle construction

This is the strongest physics route and the hardest.

It would require:

```text
1. a stable or polystable locally free bundle V on the Fu-Yau geometry;
2. slope/HYM compatibility;
3. Bianchi/anomaly equation with the chosen gerbe class;
4. a determinant-seven residual character quotient extracted from V.
```

The current Mukai pair `a,b` does not itself give such a bundle.  A successful
version will probably need one of:

```text
single stable bundle whose topological charge lattice has a determinant-seven
quotient;
extension/monad construction with hidden determinant-seven Chern-character
subblock;
virtual K-theory/differential-character interpretation accepted by the physics.
```

This route would be the most convincing final proof, but it is not the shortest
next step.

## Route 4: dyadic shared-circle carry

This route is independent and necessary.

Even a perfect `Z_7` proof does not prove order `448` unless the dyadic factor
is really order `64`, not merely six independent `Z_2` memories.

The required theorem is:

```text
2x_i=x_{i+1},
2x_5=0
```

for six refinement levels of the same shared central circle.

This must come from:

```text
projector refinement,
proto-spinor loop memory,
central-circle holonomy,
Wilson/orbifold remnant,
or an explicit integral relation matrix in the compactification.
```

This is the other main hard gate.

## Route 5: M-theory flux-lattice backup

This is a backup if heterotic HYM becomes too restrictive.

The M-theory corpus already supports:

```text
shifted G4 quantization,
fixed integral degree-four lattice,
large gauge transformations,
flux-sector selection.
```

The search target would be:

```text
a determinant-seven subquotient in the G4/tadpole/charge lattice.
```

This route avoids some bundle-slope issues, but it is farther from the current
flavor construction and still needs the CP-character identification.

## Route 6: repaired Lens-Nil

This is now low priority.

The repaired closed Lens-Nil Chern-character block proves that a closed
integral `[[2,1],[1,4]]` source can be written, but the displayed invariant
HYM gate fails.  It may still be useful as:

```text
a local model,
a heuristic source of the determinant-seven fingerprint,
or a later stable-bundle construction target.
```

It should not be the primary route.

# Recommended next sequence

## Step 1: write the conditional theorem cleanly

Produce a theorem paper:

```text
Order_448_CP_Conditional_Selection_Theorem_v1.md
```

This locks in what is actually proved by the finite arithmetic.

## Step 2: decide the interpretation of the Mukai block

There are two options:

```text
charge-lattice interpretation:
  CP labels are differential/K-theory characters of coker K_Mukai.

bundle-summand interpretation:
  CP labels come from a single polystable HYM bundle.
```

The first is currently viable.  The second is blocked for the present pair and
needs a new construction.

## Step 3: prove or replace the dyadic carry

The dyadic side is as important as the sevenfold side.

Search target:

```text
derive the carry matrix from shared-circle recursion,
not from six independent binary labels.
```

This gate is now isolated in:

```text
Shared_Circle_Z64_Carry_Gate_Theorem_v1.md
shared_circle_z64_carry_gate_check.py
```

The formal result is:

```text
six-stage carry with terminal closure -> SNF [64],
six independent binary memories       -> exponent 2,
carry without terminal closure        -> free rank 1.
```

The open part is precisely the derivation of the carry rows from MTT projector,
refinement, proto-spinor, Wilson-line, or shared-circle holonomy data.

## Step 4: supply the Fu-Yau topological sector

The fixed-sector map is now:

```text
Bianchi-compatible Fu-Yau/K3 topological sector
  -> integral Mukai charge lattice with P
  -> MTT fixed-sector selection
  -> Hom(A_P,U(1)).
```

The remaining missing input is the global sector itself: construct or select a
Fu-Yau/Strominger sector whose Bianchi and Chern/Mukai data contain `P`.

The formal character-dual side is now isolated in:

```text
Mukai_Charge_Character_Selection_Gate_v1.md
mukai_character_selection_gate_check.py
```

It proves:

```text
K_Mukai=[[2,1],[1,4]],
SNF(K_Mukai)=[7],
Hom(coker K_Mukai,U(1)) ~= Z_7,
theta=(1/7,5/7) generates the character group.
```

The sharper canonical formulation is:

```text
Mukai_Discriminant_Group_Selection_for_Z7_CP_v1.md
mukai_discriminant_group_check.py
```

If `P` is the rank-two Mukai lattice spanned by the selected vectors, then:

```text
A_P=P^*/P ~= Z_7,
theta=(1/7,5/7),
b(theta,theta)=2/7 mod 1.
```

Thus the best `Z_7` statement is:

```text
the odd CP factor is the unitary dual of the discriminant group of the
selected Mukai block.
```

The fixed-sector selection reduction is now recorded in:

```text
Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md
fu_yau_mukai_fixed_sector_selection_audit.py
```

It proves that once a Bianchi-compatible sector contains `P`, MTT selection
carries the `Z_7` quotient to the unique selected fixed point.  The open part
is global topological-sector realization/choice.

The dyadic minimality obligation is also now isolated in:

```text
Z64_Carry_Minimality_and_Row_Obligation_v1.md
z64_carry_minimality_check.py
```

It shows that the exact minimal `Z_64` proof needs:

```text
all five carry rows,
terminal closure 2x_5=0.
```

A larger recursive carrier is allowed only if the selected physical CP
character is proved to descend to order `64`.

The combined selected character itself is now recorded in:

```text
Selected_CP_Character_Dual_Map_v1.md
selected_cp_character_dual_check.py
```

It gives:

```text
theta_CP =
(1/64,1/32,1/16,1/8,1/4,1/2,1/7,5/7),
ord(theta_CP)=448.
```

The CKM/PMNS/closure labels are:

```text
79 theta_CP,
336 theta_CP,
33 theta_CP,
```

and they sum to zero in the character group.

The label-normalization gate is now separated in:

```text
CP_Label_Normalization_and_Overlap_Selection_Gate_v1.md
cp_label_normalization_scan.py
```

This check shows:

```text
finite topology fixes the denominator 448,
lepton quarter-turn fixes l=336,
phase-sum closure fixes r once q is chosen,
but finite topology alone does not uniquely fix q=79.
```

There remain `192` primitive `q` labels with primitive phase-sum partners.  The
CKM/Jarlskog benchmark selects `q=79` on the chosen phase branch.  The next
numerical theorem must derive `q=79` from overlap geometry or a selection
functional.

## Step 5: keep the M-theory backup alive

If the HYM/bundle route becomes too rigid, search the M-theory `G4` lattice for
the same determinant-seven quotient.  This should be a parallel backup, not the
main path yet.

# Final evaluation

We have achieved:

```text
a rigorous finite arithmetic target,
a clean separation of selected CP quotient from ambient family topology,
a proof that the old Lens-Nil source fails,
a proof that negative K3 H2 determinant-seven curvature pairs are root-obstructed,
a stronger Mukai charge-lattice odd source,
and a precise list of remaining proof gates.
```

We have not yet achieved:

```text
the full MTT extraction of the dyadic K_64 block from the actual Hessian/kernel,
the global Fu-Yau/Strominger sector containing K_Mukai,
or a complete supersymmetric Fu-Yau bundle/anomaly construction.
```

The best way forward is therefore two-track:

```text
Track A: finish the conditional theorem and character-lattice formalism.
Track B: prove the two hard global gates: actual Z_64 Hessian/kernel
         extraction and Z_7 Fu-Yau/Mukai topological-sector realization.
```

That is the current honest path toward a real proof.
