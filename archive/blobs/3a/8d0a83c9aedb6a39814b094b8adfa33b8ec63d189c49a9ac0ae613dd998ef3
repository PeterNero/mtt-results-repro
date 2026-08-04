---
abstract: |
  We consolidate the carried-forward candidates for deriving the MTT flavor CP
  character of effective order 448.  The current best route is not a claim
  that the full topology is exactly Z_448, but that the flavor sector selects
  a unitary CP character of order 448.  The minimal quotient is Z_64 x Z_7,
  with the Z_64 supplied by recursive shared-circle dyadic carry and the Z_7
  supplied by a nil/Wilson/flux finite row.  If the already-derived Z_3 family
  holonomy belongs to the same ambient carrier, the ambient quotient may be
  Z_1344 while the CP character still has order 448.  A targeted corpus sweep
  found no explicit order-seven Wilson line, L(7,*) lens factor, or seven-
  torsion statement, so the sevenfold row remains a proof target.
author:
- Peter Nero
date: May 2026
title: |
  Carried-Forward Candidate Program for the MTT Order-448 CP Character
---

# Executive result

The strongest current statement is:

```text
Gamma_fl contains a canonically selected unitary CP character chi_CP
with ord(chi_CP)=448.
```

The minimal quotient realizing this is:

```text
Gamma_CP,min ~= Z_64 x Z_7 ~= Z_448.
```

But the full ambient carrier may be larger or recursive:

```text
Gamma_fl -> Gamma_CP,min,
```

with the physical CKM/PMNS CP observable factoring through the selected
order-448 character.

# Current best candidate

The current best candidate is:

```text
shared central circle
  +
six-stage recursive dyadic carry
  +
nil/Wilson/flux sevenfold finite row
  +
lens complex quarter-turn
  =>
ord(chi_CP)=448.
```

In relation-matrix language:

```text
A_fl =
  A_carry
  +
  A_7
  +
  A_phase-sum,

chi_CP in Hom(coker(A_fl), U(1)),
ord(chi_CP)=448.
```

# Dyadic side: best candidate

The dyadic candidate is now precise.

Use six levels of the same shared central-circle phase:

```text
x_0,...,x_5.
```

Impose the carry matrix:

```text
2x_0 - x_1 = 0,
2x_1 - x_2 = 0,
2x_2 - x_3 = 0,
2x_3 - x_4 = 0,
2x_4 - x_5 = 0,
2x_5       = 0.
```

Smith normal form:

```text
torsion factors: [64]
exponent: 64.
```

This avoids the group-size trap:

```text
Z_2^6 has 64 elements but exponent 2.
```

The corpus support is strong but not yet a proof:

- one shared central circle;
- finite subgroup of `U(1)` for flavor holonomy;
- central-circle phases contribute to CP violation;
- CKM phases can arise from circle-bundle holonomy/Wilson-line data;
- proto-spinorial `Z_2` loop memory;
- refinement stability.

Proof still needed:

```text
derive the carry relations from projector/refinement/proto-spinor/Wilson data.
```

# Sevenfold side: best candidates

A targeted corpus sweep did **not** find an explicit:

```text
Z_7,
L(7,*),
order-seven Wilson line,
seven-torsion class,
or mod-7 congruence
```

already stated in the corpus.  Therefore seven must be derived, not quoted.

The best relation templates are:

## Shared-circle/nil lock

```text
c - n = 0,
7n = 0.
```

Smith normal form:

```text
torsion factors: [7].
```

Interpretation:

```text
the CP phase lives on the shared circle but is locked to a nil sevenfold
survivor.
```

## Flux-Wilson congruence

```text
w - f = 0,
7w = 0.
```

Smith normal form:

```text
torsion factors: [7].
```

Interpretation:

```text
integer flux selection fixes an admissible Wilson character, and the residual
Wilson line has order seven.
```

The Lens x Nil / Wilson scan makes this sharper:

```text
w - f = 0
```

alone has no torsion and leaves a free phase.  The genuinely new row is

```text
7w = 0.
```

So the proof obligation is not "find flux" but "derive an order-seven residual
Wilson character selected by flux/projector/orbifold data."

## Monodromy plus terminal nil closure

```text
n - 7c = 0,
n = 0.
```

Smith normal form:

```text
torsion factors: [7].
```

Important caution:

```text
n - 7c = 0
```

alone has no torsion and one free phase.  It is not enough.

The same scan shows that the strongest MTT-native template:

```text
c - n = 0,
7n = 0
```

also requires the second row.  The lock `c-n=0` places CP on the nil/shared
circle carrier, but only `7n=0` supplies the finite sevenfold character.

# Family Z_3 must be handled separately

The central-circle corpus already has:

```text
family holonomy: Z_3.
```

If this is part of the same ambient finite carrier:

```text
Z_64 x Z_3 x Z_7 ~= Z_1344.
```

This is not a contradiction.  The CP character can still have order `448`:

```text
N = 1344,
k = 237,
gcd(k,N)=3,
ord_N(k)=448.
```

Therefore the clean physical statement is:

```text
the selected CP character has order 448,
while the family character may live in an orthogonal Z_3 factor.
```

# Numerical benchmark retained

The effective order-448 character still gives:

```text
k_q = 79 mod 448,
delta_q = 2pi * 79/448 = 1.107972409079,
phase error = 6.164e-06,
J error = 8.920e-11,
delta_l = -pi/2 exactly via k_l = 336 mod 448.
```

Larger ambient quotients that are multiples of seven can contain the same
selected character, but the character order reduces to `448`.

# Candidate ranking

Current ranking:

```text
1. dyadic shared-circle carry + primitive determinant-seven Lens-Nil block
2. dyadic shared-circle carry + shared-circle/nil seven lock
3. dyadic shared-circle carry + finite-U(1) Wilson Z_7 selection
4. dyadic shared-circle carry + monodromy plus terminal nil closure
5. selected order-448 character inside ambient Z_1344 including family Z_3
6. direct diagonal Z_448 row from projector/flux equations
7. larger recursive carrier projecting to order-448 CP character
8. Gaussian dyadic route with diagonal selection
9. M-theory X_7/G_2 as carrier clue only
10. hypercharge numerator, QCD beta seven, bare dimension seven: rejected
```

# What would prove the candidate

The program succeeds if we derive:

```text
SNF(A_carry) contains [64],
SNF(A_7) contains [7],
chi_CP ignores or quotients out family Z_3,
phase-sum closure holds for L_12,L_23,L_31,
Majorana/two-torsion constraints remain compatible.
```

The program fails if:

```text
the dyadic side is only Z_2^6,
the seven side is only a dimension label or bare monodromy,
the family Z_3 is forced into the CP character rather than an orthogonal
sector,
or no finite character of order 448 is selected by MTT data.
```

# Immediate next work

The next concrete calculations should be:

1. Build an integer Lens x Nil/Wilson relation matrix with explicit candidate
   rows for flux, Wilson, monodromy, and nil terminal closure.
2. Compute its Smith normal form and selected character orders.
3. Build a projector-refinement model of the central-circle dyadic carry and
   test when it produces `[64]` rather than `Z_2^6`.
4. Verify that adding the family `Z_3` produces an ambient factor but does not
   change the selected CP character order.

The first two items now have a starter implementation:

```text
lens_nil_wilson_relation_scan.py
```

It confirms that all three successful sevenfold templates combine with the
dyadic carry to give torsion `[448]`, while flux-only, lock-only, congruence-
only, and monodromy-only templates fail.

The Wilson branch also has a prime-companion scan:

```text
odd_prime_companion_scan.py
```

It shows that if the missing odd row is a prime finite subgroup of `U(1)`,
then `p=7` is the first and best small prime companion to the dyadic `64`:

```text
p=7, N=448, k=79, phase_error=6.164e-06, J_error=8.920e-11.
```

So the Wilson proof target is specifically:

```text
derive residual Wilson Z_7, i.e. 7w=0.
```

The family-orthogonality scan adds a stronger consistency test:

```text
family_orthogonal_cp_character_scan.py
```

In the ambient carrier

```text
Z_64 x Z_7 x Z_3 ~= Z_1344,
```

requiring the CP character to ignore the family `Z_3` factor gives:

```text
k_q = 237 = 3*79,
ord(k_q)=448,
phase_error=6.164e-06,
J_error=8.920e-11.
```

The lepton quarter-turn and phase-sum rule also pass:

```text
k_l = 1008,  ord(k_l)=4,    delta_l=-pi/2,
k_31 = 99,   ord(k_31)=448,
(k_q+k_l+k_31) mod 1344 = 0.
```

All three labels are multiples of `3`, so the family factor remains orthogonal
to the selected CP character.

The ambient Majorana check adds a separation constraint:

```text
ambient_z1344_majorana_check.py
```

In `Z_1344`, the CP labels

```text
k_q=237, k_l=1008, k_31=99
```

are family-trivial and phase-sum closed, but none is Majorana self-conjugate.
The Majorana-admissible flat line weights are only:

```text
k_N = 0 or k_N = 672.
```

Therefore the no-proxy architecture should separate:

```text
Gamma_CP: order-448 family-trivial CP overlap character,
Gamma_N:  trivial or two-torsion neutral real-structure character.
```

This is a constraint, not a failure.  It prevents the CP phase from being
reused as a Majorana mass character.

The consolidated ambient constraint battery now checks all of these constraints
simultaneously:

```text
ambient_z1344_constraint_battery.py
```

It uses the relation matrix:

```text
six-stage dyadic carry  -> Z_64,
sevenfold finite row    -> Z_7,
family holonomy row     -> Z_3,
```

whose Smith normal form is:

```text
torsion factors: [1344],
exponent: 1344,
free rank: 0.
```

The same run passes:

```text
selected CKM character order is 448,
selected lepton branch has order 4,
lepton branch is -pi/2 mod 2pi,
pairwise phase-sum closes,
all CP labels are family-trivial,
CP labels are not Majorana self-characters,
neutral trivial and two-torsion labels are Majorana-admissible.
```

So the ambient `Z_1344` candidate is not merely numerically convenient; it is
currently compatibility-clean.

The selected CP quotient is also explicit:

```text
ambient_to_selected_cp_quotient_map.py
```

In the cyclic presentation,

```text
pi: Z_1344 -> Z_448,
pi(x)=x mod 448,
ker(pi)={0,448,896}.
```

The kernel is exactly the family `Z_3` direction.  An ambient character descends
to the selected CP quotient iff its label is divisible by `3`.  Therefore:

```text
k_q  = 237  = 3*79,
k_l  = 1008 = 3*336,
k_31 = 99   = 3*33.
```

The downstairs labels close in `Z_448`:

```text
(79+336+33) mod 448 = 0.
```

This gives the precise replacement for the old rough claim:

```text
Z_448 is the finite quotient selected by chi_CP,
not necessarily the entire ambient flavor topology.
```

The newest sevenfold refinement is:

```text
primitive_determinant_seven_block_scan.py
```

Instead of assuming a primitive row

```text
7w=0,
```

it tests the better Lens-Nil possibility:

```text
a w + b n = 0,
c w + d n = 0,
det [[a,b],[c,d]] = +/-7.
```

For example:

```text
2w+n=0,
w+4n=0
```

has determinant `7` and Smith normal form `[7]`.  Elimination derives:

```text
7w=0,
7n=0.
```

This is now the most natural proof target because the corpus already has two
independent Lens x Nil componentwise anomaly equations with integer flux data
and discrete invariant loci.  The seven can therefore arise as a determinant,
not as a literal inserted row.

Even better, the determinant-seven reduced integer fingerprint appears in the
existing Lens x Nil coefficient appendix.  The check:

```text
lens_nil_seven_fingerprint_check.py
```

uses the corpus coefficients:

```text
W_1 = 2 lambda^2 R^2,
W_3 = lambda nu R^2,
A   = 4 lambda^2 + O(lambda^2 nu^2),
B   = 4 nu^2     + O(lambda^2 nu^2).
```

The leading coefficient block:

```text
[2 1
 1 4]
```

has:

```text
det = 7,
SNF = [7].
```

So the best proof target is no longer a blind search for `Z_7`; it is:

```text
prove that the Lens x Nil coefficient block descends to the residual
Wilson/nil CP character relation block.
```

This proof target is now isolated in:

```text
Descent_Theorem_Skeleton_for_Lens_Nil_Z7_CP_Row_v1.md
```

The required lemmas are:

```text
1. beta_1,beta_3 form an integral period basis for the relevant component lattice.
2. Pi_coh descends componentwise Bianchi compatibility to residual character compatibility.
3. the descended block acts on the family-trivial CP sublattice.
4. the descended block is primitive and GL(2,Z)-equivalent to [[2,1],[1,4]].
5. the odd Z_7 block is independent of the dyadic Z_64 carry except through the selected diagonal CP character.
```

The dual-lattice feasibility check:

```text
descent_dual_lattice_check.py
```

adds a formal algebra step.  If the Lens x Nil component lattice has relation
matrix:

```text
K = [[2,1],[1,4]],
```

then both the quotient lattice and its unitary character group have:

```text
SNF(K)=SNF(K^T)=[7].
```

The corpus now supports two gates:

```text
beta_1,beta_3 live in an integral 4-form lattice,
left-invariant truncation equals coherent projection.
```

The remaining open gates are:

```text
identify residual CP labels w,n with the dual character lattice,
prove the O(lambda^2 nu^2) curvature terms and higher-order corrections do not
alter the exact fixed-sector integer block.
```

A rigor correction is now recorded in:

```text
Lens_Nil_Beta_Form_Closure_Caution_for_Z7_Descent_v1.md
```

The individual invariant forms `beta_1,beta_3` are not closed under the
Lens x Nil structure equations.  So the descent target should not be stated as
a naive `H^4` duality claim.  It should be stated as:

```text
the integral Bianchi/gerbe component lattice selected by Pi_coh has unitary
dual residual CP characters w,n.
```

The fixed-point audit:

```text
Fixed_Point_Compatibility_Audit_and_Arithmetic_Adaptation_for_Lens_Nil_Z7_v1.md
```

concludes that the Fixed Points papers hold for the analytic claims we need:

```text
Riesz projector boundedness,
joint circle-lens-nil projector,
nil spectral gap in a noncollapsing class,
disturbance-damping stability,
selection as an admissibility layer.
```

But they need an arithmetic addendum for this CP proof:

```text
fix an integral topological/differential-cohomology sector,
define an arithmetic coherent lattice before scalar extension,
protect K_LN=[[2,1],[1,4]] as an exact integer block,
identify w,n as characters of the resulting quotient.
```

This is now made theorem-shaped in:

```text
Arithmetic_Fixed_Sector_Descent_Theorem_for_Lens_Nil_Z7_CP_v1.md
```

The executable ledger is:

```text
arithmetic_fixed_sector_descent_check.py
```

The character-dual part of the descent is isolated in:

```text
Character_Dual_Descent_Lemma_for_Lens_Nil_Z7_CP_v1.md
```

with executable check:

```text
character_dual_descent_check.py
```

The key formal point is:

```text
relations on the integral Bianchi/gerbe lattice use K,
relations on unitary CP characters use K^T.
```

Since the Lens-Nil block is symmetric, `K^T=K`, and the character solutions are:

```text
(w,n) = (j/7, -2j/7) mod 1,
j=0,...,6.
```

The exactness/protection issue is isolated in:

```text
Integer_Block_Protection_Strategy_for_Lens_Nil_Z7_CP_v1.md
```

with check:

```text
integer_block_protection_check.py
```

It records the essential rigor point:

```text
small analytic corrections are not automatically harmless for exact torsion.
```

The final proof must compute the exact fixed-sector period/character matrix or
prove that the `O(lambda^2 nu^2)` terms are invisible to the character quotient.

# New obstruction: current Lens-Nil appendix is not enough

The direct attempt to close the Lens-Nil proof found a stronger obstruction.
With the structure equations and flux ansatz as written in the source appendix:

```text
beta_1 = eta^1 eta^2 eta^3 sigma^6,
beta_3 = eta^3 sigma^4 sigma^5 sigma^6,
F      = f eta^1 eta^2 + h sigma^4 sigma^5,
```

the exterior-calculus audit reports:

```text
d beta_1 = - e^12345,
d beta_3 =   e^12456,
F wedge F = 2 f h e^1245.
```

Therefore:

```text
dH = W_1 beta_1 + W_3 beta_3
```

with nonzero constant `W_1,W_3` cannot be a literal identity, since it is not
closed.  Also, the displayed abelian flux does not square to
`f^2 beta_1+h^2 beta_3`; it squares to the cross term `2fh beta_2`.

This obstruction is recorded in:

```text
Lens_Nil_Bianchi_Consistency_Obstruction_and_Correction_Path_v1.md
```

with executable audit:

```text
lens_nil_bianchi_consistency_audit.py
```

So the determinant-seven Lens-Nil route is currently blocked by a source
appendix inconsistency.  The formal `Z_7` arithmetic remains valid, but the
premise that Lens-Nil supplies `K_LN=[[2,1],[1,4]]` is not yet established.

A repaired Lens-Nil candidate now exists using closed integral Chern-character
data rather than the inconsistent `beta_1,beta_3` formula:

```text
u1=e12, u2=e13, v1=e45, v2=e46,
c1(L1)=u1+2v1+v2,
c1(L2)=u2+v1+4v2.
```

Then:

```text
ch_2(L1)+ch_2(L2)
= 2u1v1 + u1v2 + u2v1 + 4u2v2,
```

so the exact closed coefficient matrix is:

```text
K_closed = [[2,1],[1,4]],
SNF(K_closed)=[7].
```

This is recorded in:

```text
Repaired_Lens_Nil_Closed_Flux_Candidate_for_Z7_CP_v1.md
```

with check:

```text
repaired_lens_nil_closed_flux_candidate.py
```

The next gate is no longer closure.  It is:

```text
prove HYM/primitivity/admissibility or replace these line bundles by a stable
higher-rank bundle with the same closed ch_2 matrix.
```

The first HYM gate check:

```text
repaired_lens_nil_hym_gate_check.py
```

shows that, for the displayed SU(3) structure, the invariant closed primitive
`(1,1)` two-form space is only:

```text
span(e45 - e12).
```

So the simple two-line-bundle repair is not yet an admissible HYM sector.  It
proves existence of a closed integral determinant-seven Chern-character matrix,
but not a finished heterotic bundle solution.

# Stronger clue from Fu-Yau/K3

A targeted sweep of:

```text
C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings
```

found a cleaner candidate in the Fu-Yau/K3 material.

The corpus already supplies:

```text
principal T^2 bundle over K3,
fixed topological sector,
stable holomorphic bundle,
Li-Yau HYM existence on Gauduchon metrics,
MTT fixed-point selection in the Fu-Yau flux slice.
```

Inside the K3 lattice `H^2(K3,Z)`, use `U^2` with basis `(e1,f1,e2,f2)` and
define:

```text
v = (-1,  0, -1, 1),
w = ( 1, -1, -1, 1).
```

Then:

```text
v^2=-2,
w^2=-4,
v.w=-1,
Gram(v,w)=[[-2,-1],[-1,-4]].
```

Therefore:

```text
K = -Gram(v,w) = [[2,1],[1,4]],
SNF(K)=[7].
```

This is recorded in:

```text
Fu_Yau_K3_Determinant_Seven_Flux_Candidate_for_MTT_CP_v1.md
```

with check:

```text
fu_yau_k3_det7_candidate_check.py
```

This route is cleaner than the Lens-Nil coefficient route because the block is
an exact integral intersection matrix, not an approximate curvature coefficient.
The remaining gates are:

```text
realize <v,w> as primitive (1,1) in the Fu-Yau K3 base,
construct/cite a stable higher-rank or Mukai-lattice HYM bundle/charge
realization with this Chern/flux block,
show the Fu-Yau Bianchi equation admits it,
prove MTT selects it as the family-trivial CP character quotient.
```

The K3 Picard/HYM gate check now refines this.  It confirms:

```text
<v,w> is primitive in U^2,
det(-Gram(v,w))=7,
h=(0,0,1,1) is positive and orthogonal to v,w.
```

But it also shows:

```text
v^2=-2,
```

so the naive proof by two zero-slope line bundles is not safe: a polarization
orthogonal to a K3 root lies on a wall if that root is effective.  The next
route should therefore be stable higher-rank/Mukai realization, or a direct
fixed charge-lattice character quotient.

The next step has now produced a sharper replacement:

```text
Mukai_Positive_Charge_Block_for_Fu_Yau_K3_Z7_CP_v1.md
mukai_positive_det7_charge_block_check.py
```

The negative K3 `H^2` route is structurally obstructed, not merely incomplete.
For an even positive rank-two lattice:

```text
K=[[2a,b],[b,2c]],
det(K)=7,
```

reduction gives `|b|<=a<=c`, hence:

```text
7=4ac-b^2 >= 3a^2,
```

so `a=1`.  Thus any such determinant-seven block represents norm `2`; the
negative K3 block contains a `(-2)` root and runs into the Fu-Yau/K3 ample-wall
problem.

The live replacement is the full algebraic Mukai charge lattice.  On a
Picard-rank-one K3 with `H^2=2`, take:

```text
a=(5,H,0),
b=(7,3H,1).
```

Then:

```text
<a,a>=2,
<a,b>=1,
<b,b>=4,
Gram_Mukai(a,b)=[[2,1],[1,4]],
SNF=[7].
```

This preserves the `Z_7` character quotient while avoiding the root-wall
obstruction.  The remaining gates are now:

```text
stable sheaf/bundle existence and local-freeness,
Fu-Yau anomaly compatibility,
identification of CP labels with Hom(coker K_Mukai,U(1)),
MTT fixed-sector selection.
```

There is one more important caveat.  The explicit Mukai generators:

```text
a=(5,H,0),
b=(7,3H,1)
```

do not have the same HYM slope:

```text
mu_H(a)=2/5,
mu_H(b)=6/7.
```

So this is currently a determinant-seven charge-lattice block, not a direct
two-summand polystable bundle.  The same-slope route is obstructed more
generally: in Picard rank one, a same-slope pair has Gram determinant a
negative rational square, not seven.  This is checked in:

```text
mukai_same_slope_hym_obstruction_check.py
```

The full order-448 arithmetic has also been rewritten in the Mukai language:

```text
Mukai_Fixed_Sector_Descent_to_Order_448_CP_v1.md
mukai_fixed_sector_descent_check.py
```

This keeps the finite quotient:

```text
Z_64 x Z_7 ~= Z_448,
Z_64 x Z_7 x Z_3 ~= Z_1344,
Z_1344 / Z_3-family ~= Z_448.
```

but now the `Z_7` source is the positive Mukai charge block, not the blocked
Lens-Nil coefficient block.

The two current proof gates are now isolated in:

```text
Shared_Circle_Z64_Carry_Gate_Theorem_v1.md
shared_circle_z64_carry_gate_check.py

Mukai_Charge_Character_Selection_Gate_v1.md
mukai_character_selection_gate_check.py
```

The first proves formally that the six-stage carry gives `Z_64` and that
independent binary memories fail; it leaves open the MTT derivation of the
carry rows.  The second proves formally that:

```text
Hom(coker K_Mukai,U(1)) ~= Z_7
```

with generator:

```text
theta=(1/7,5/7),
```

and leaves open the MTT selection map from the Fu-Yau/K3 fixed charge sector
to this quotient.

The Mukai side is now sharpened further by:

```text
Mukai_Discriminant_Group_Selection_for_Z7_CP_v1.md
mukai_discriminant_group_check.py
```

Let `P=<a,b>` be the selected rank-two Mukai lattice.  Then:

```text
A_P=P^*/P ~= Z_7,
theta=(1/7,5/7),
K_Mukai theta=(1,3),
b(theta,theta)=2/7 mod 1.
```

This is better than saying only `coker K_Mukai`: the odd factor is the
discriminant group of the selected Mukai lattice.

The dyadic side is sharpened by:

```text
Z64_Carry_Minimality_and_Row_Obligation_v1.md
z64_carry_minimality_check.py
```

It shows:

```text
remove any carry row -> no finite Z64 conclusion,
remove terminal row  -> free rank 1,
terminal m*x5=0      -> exponent 32m.
```

So the minimal exact dyadic theorem needs all five carry rows and the terminal
closure `2x_5=0`.

The combined selected CP character is now explicit in:

```text
Selected_CP_Character_Dual_Map_v1.md
selected_cp_character_dual_check.py
```

It uses:

```text
theta_64=(1/64,1/32,1/16,1/8,1/4,1/2),
theta_7=(1/7,5/7),
theta_CP=(theta_64,theta_7).
```

Then:

```text
ord(theta_CP)=448,
CKM=79 theta_CP,
PMNS quarter-turn=336 theta_CP,
phase-sum partner=33 theta_CP,
79+336+33=0 mod 448.
```

The ambient family-trivial lifts are still:

```text
237, 1008, 99.
```

The next normalization gate is isolated in:

```text
CP_Label_Normalization_and_Overlap_Selection_Gate_v1.md
cp_label_normalization_scan.py
```

It shows that the finite topology does not by itself uniquely select `q=79`.
After imposing:

```text
l=336,
q+l+r=0 mod 448,
ord(q)=ord(r)=448,
```

there are still `192` primitive `q` labels with primitive partners.  The
CKM/Jarlskog benchmark selects:

```text
q=79,
r=33,
```

on the chosen phase branch.  Deriving `q=79` is therefore now an
overlap/selection-dynamics problem, not a finite-group problem.

# Bottom line

The correct forward path is now sharply defined:

```text
Do not search for the number 448 as a magic denominator.
Derive a finite character of order 448.
```

The most coherent derivation remains:

```text
Z_64 from recursive shared-circle dyadic carry,
Z_7 from nil/Wilson/flux finite closure,
Z_3 family holonomy kept orthogonal to chi_CP,
lens complex structure supplies the quarter-turn branch.
```
