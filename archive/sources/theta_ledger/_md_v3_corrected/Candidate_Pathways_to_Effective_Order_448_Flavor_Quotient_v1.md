---
abstract: |
  We explore concrete candidate pathways for deriving the effective order-448
  flavor CP quotient in MTT.  The strongest candidate is a complex unitary
  circle-lens-nil carrier in which the lens layer supplies an orthogonal
  quarter-turn, the shared circle carries a genuine cyclic dyadic refinement
  of order 64, and the nil/string-flux sector supplies a sevenfold unitary
  rotor or equivalent row.  A new Smith-normal-form scan shows that a six-level
  dyadic carry chain gives a true Z_64, whereas six independent binary
  memories only give exponent 2.  It also shows that Gaussian-integer dyadic
  quotients can have 64 states while still failing to supply order-64 phase
  resolution unless lifted to a larger exponent-64 quotient.  We rank several
  candidate routes and identify the most promising continuation: derive the
  order-64 carry from refinement/proto-spinor/projector data and derive the
  sevenfold row from nil monodromy, Wilson/orbifold data, or torsional
  SU(3)/Lens x Nil flux quantization.
author:
- Peter Nero
date: May 2026
title: |
  Candidate Pathways to the Effective Order-448 Flavor Quotient
---

# Purpose

The current target is not to guess `Z_448`, but to derive a finite unitary
character quotient whose selected character has the same effective phase
resolution:

```text
effective order 448 = 64 x 7.
```

The corpus points toward a combined object:

```text
Y_4 spin/chiral line-bundle data
  +
X_6 circle-lens-nil torsional/flux selection
  +
orthogonal complex structure J
  +
finite unitary character quotient.
```

This note explores multiple ways that object could produce the required
quotient.

# Benchmark constraints

A successful route must satisfy:

1. exact pairwise phase-sum closure for `L_12,L_23,L_31`;
2. exact or natural lepton quarter-turn `delta_l=-pi/2`;
3. CKM phase branch near `delta_q=1.107978573420`;
4. no independent phase fitting;
5. compatibility with Majorana/two-torsion admissibility;
6. derivation from MTT carrier, topology, flux, projector, or string data.

The known finite-character benchmark is:

```text
k_q = 79 mod 448,
delta_q = 2pi * 79/448 = 1.107972409079,
phase error = 6.164e-06,
J error = 8.920e-11.
```

# Candidate 1: complex lens plus cyclic dyadic carry plus nil seven

## Mechanism

Use the complex nesting picture:

```text
C --J_L--> L --R_N--> N,
```

where:

- `J_L^2=-1` gives the lens quarter-turn;
- the shared circle carries a cyclic dyadic refinement of order `64`;
- the nil/string-flux sector supplies an order `7` unitary rotor;
- the pairwise line bundles attach as characters satisfying the phase-sum rule.

The quotient is source-presented as:

```text
Z_64 x Z_7.
```

Since `64` and `7` are coprime, its Smith normal form is:

```text
Z_448.
```

## Evidence

This route matches every numerical benchmark already tested.  It also aligns
with corpus structure:

- central circle: universal phase bookkeeping;
- lens: CP/conjugation/curvature-misalignment layer;
- nil: family survivorship and discrete termination;
- QM/QFT: complex structure `J^2=-1`;
- string/flux: discrete loci from integer flux/anomaly equations.

## Weak point

The order `64` and order `7` rows are not yet derived.  They are structurally
motivated targets.

## Status

Best current final candidate.

# Candidate 2: six-level dyadic carry from spinorial refinement

## Mechanism

ProtoSpinor gives a genuine `Z_2` loop-memory obstruction from

```text
SO(3) -> Spin(3) ~= SU(2).
```

Six independent copies would fail, but a nested refinement carry can turn
six binary levels into a cyclic order-64 quotient.

Use generators

```text
x_0,x_1,x_2,x_3,x_4,x_5
```

with relations

```text
2 x_0 = x_1,
2 x_1 = x_2,
2 x_2 = x_3,
2 x_3 = x_4,
2 x_4 = x_5,
2 x_5 = 0.
```

Then:

```text
64 x_0 = 0.
```

The Smith normal form confirms:

```text
Six-level dyadic carry chain
  torsion factors: [64]
  exponent: 64
```

Adding a nil sevenfold row gives:

```text
Dyadic carry Z_64 plus nil sevenfold source
  torsion factors: [448]
  exponent: 448
```

## Evidence

This is the first concrete route that turns the ProtoSpinor `Z_2` memory into
a real `Z_64` without committing the group-size trap.

It is also conceptually natural:

- each refinement level remembers the previous one;
- the next level is not independent but a carry/lift;
- only the final return closes.

## Weak point

The corpus has not yet explicitly stated these six carry relations.  We must
derive them from refinement stability, projector nesting, or repeated
proto-spinorial return data.

## Status

Most promising derivation of the `64` factor.

# Candidate 3: Gaussian complex dyadic quotient

## Mechanism

Since the carrier is complex, test Gaussian-integer dyadic ideals:

```text
Z[i] / (1+i)^n.
```

These are natural because `1+i` is the prime above `2` in Gaussian integers,
and multiplication by `i` is the quarter-turn.

## SNF scan

The scan gives:

```text
Z[i]/(1+i)^4
  torsion factors: [4,4]
  exponent: 4

Z[i]/(1+i)^6
  torsion factors: [8,8]
  exponent: 8

Z[i]/(1+i)^8
  torsion factors: [16,16]
  exponent: 16

Z[i]/(1+i)^10
  torsion factors: [32,32]
  exponent: 32

Z[i]/(1+i)^12
  torsion factors: [64,64]
  exponent: 64
```

The tempting `n=6` case has `64` states, but exponent only `8`.  With a nil
sevenfold row:

```text
Gaussian 64-state quotient plus nil seven
  torsion factors: [8,56]
  exponent: 56
```

So it fails the CKM phase-resolution target.

At `n=12`:

```text
Gaussian exponent-64 quotient plus nil seven
  torsion factors: [64,448]
  exponent: 448
```

This has enough phase resolution, but it is much larger than the minimal
source quotient.

## Evidence

This route is mathematically natural for complex nesting.  It explains why a
complex dyadic structure might look promising.

## Weak point

The minimal 64-state Gaussian quotient is too coarse.  The exponent-64 version
is overlarge and would require an additional selection of a diagonal character.

## Status

Interesting backup candidate; not the clean final route.

# Candidate 4: torsional SU(3) / Lens x Nil flux quotient

## Mechanism

The string/flux corpus gives a concrete selection mechanism in torsional
`SU(3)` backgrounds:

```text
d(J^2)=0,
H = i(bar partial - partial)J,
flux quantization,
dH = alpha'/4 (Tr R_+^2 - Tr F^2).
```

In the left-invariant Lens x Nil example, componentwise anomaly equations fix
discrete ratios for integer flux data `(f,h)`.

This suggests that the missing sevenfold row might arise from:

- nil monodromy;
- flux congruence;
- Wilson-line remnant;
- orbifold/discrete gauge quotient;
- instanton/worldsheet correction selecting a finite phase sector.

## Evidence

The corpus already proves that flux/anomaly equations select discrete loci in
Iwasawa and Lens x Nil examples.  This is precisely the kind of machinery
needed to turn continuous phases into finite unitary characters.

## Weak point

The worked examples currently use `L(3,1)` and do not visibly derive `Z_7`.
The sevenfold row must be extracted from a more specific flux choice or a new
Lens/Nil/Wilson/orbifold realization.

## Status

Most promising derivation of the `7` factor.

# Candidate 5: diagonal combined quotient without visible 64 and 7

## Mechanism

Instead of deriving separate factors, a flux/projector/Wilson system might
produce a single invariant factor directly:

```text
Gamma_fl = Z_448.
```

or a larger quotient containing a selected diagonal character of order `448`.

This would satisfy the finite-character benchmark without requiring the corpus
to display separate `64` and `7` rows.

## Evidence

The finite-character benchmark cares about the selected phase resolution, not
about the presentation.  Smith normal form can combine coprime source rows into
one cyclic factor.

## Weak point

This is less explanatory.  It would be correct if derived, but it gives less
structural insight into why the denominator factors as `64 x 7`.

## Status

Acceptable fallback if a concrete compactification yields the row.

## New refinement: effective character order, not necessarily ambient order

A dyadic-odd scan over

```text
N = 64 m
```

shows that `m=7` is the first companion that realizes the high-accuracy CKM
branch.  Larger multiples of seven also realize the same phase, but the
selected character order reduces back to `448`:

```text
m=7    N=448    k=79     ord_N(k)=448
m=14   N=896    k=158    ord_N(k)=448
m=21   N=1344   k=237    ord_N(k)=448
```

Thus the robust claim is not necessarily that the whole ambient topology is
exactly `Z_448`.  The robust claim is:

```text
Gamma_fl contains a canonically selected CP character chi_CP
with ord(chi_CP)=448.
```

If the quotient is minimal, then `Gamma_fl ~= Z_448 ~= Z_64 x Z_7`.  If the
carrier is recursive or larger, it must project canonically onto this same
order-448 character.

# Candidate 6: M-theory / G2 seven-carrier route

## Mechanism

The M-theory corpus uses an internal seven-manifold:

```text
X_7 = B^6 x S^1
```

or a more general `G_2`-structure space.  Flux quantization and integral
`G_4` classes fix 4D EFT data.

This could explain why `nil on 7` appears as a carrier clue: seven may refer
to the M-theory lift or `G_2` carrier rather than a direct `Z_7` quotient.

## Evidence

The corpus explicitly has `X_7`, `G_2`, integral flux classes, and
coercive/discrete moduli stabilization.

## Weak point

Dimension seven is not order seven.  This route may help explain carrier
placement, but it does not by itself supply the sevenfold finite character.

## Status

Useful interpretive route; not a final CP quotient derivation.

# Candidate 7: hypercharge or beta-function sevens

## Mechanism

The topology-only hypercharge solution includes:

```text
y_3 = -7/18.
```

The Standard Model one-loop QCD coefficient includes:

```text
b_3 = -7.
```

## Evidence

Both are real sevens in the corpus.

## Weak point

Neither is a sevenfold holonomy quotient.  The hypercharge `7` is a numerator
in a rational charge assignment; the beta-function `7` is representation/RG
data.  Treating either as `Z_7` would be numerology.

## Status

Rejected as a source of the `7` factor, but worth recording to avoid false
leads.

# Ranking

Current ranking:

```text
1. Recursive shared-circle dyadic carry + nil/Wilson seven      strongest
2. Shared-circle/nil lock with 7n=0                             strongest 7 template
3. Flux-Wilson congruence with order-seven Wilson line          strongest string/KK route
4. Six-level dyadic carry for Z_64                              strongest 64 route
5. Selected order-448 character inside larger ambient quotient  valid fallback
6. Direct minimal Z_448 from combined projector/flux rows        clean if derived
7. Gaussian dyadic complex quotient                             interesting backup
8. M-theory X_7/G2 carrier clue                                 interpretive only
9. hypercharge/beta sevens                                      rejected
```

# Recommended continuation

The next research step should split into two concrete derivations.

## Derive the dyadic carry

Try to prove that refinement/proto-spinor/projector data impose the carry
matrix:

```text
2x_0-x_1=0,
2x_1-x_2=0,
2x_2-x_3=0,
2x_3-x_4=0,
2x_4-x_5=0,
2x_5=0.
```

This would turn the existing `Z_2` loop memory into a true cyclic `Z_64`.

## Derive the sevenfold nil row

Search the torsional `SU(3)`, Lens x Nil, Wilson-line, orbifold, or M-theory
flux data for one of the finite relation templates:

```text
c - n = 0, 7n = 0,
w - f = 0, 7w = 0,
n - 7c = 0, n = 0,
448e = 0.
```

or a Smith-normal-form equivalent.  A bare monodromy relation `n-7c=0` is not
enough; it leaves a free phase unless a terminal closure or finite Wilson row
is also derived.  The derivation must come from integer flux, monodromy,
discrete gauge, Wilson, worldsheet, or projector data, not from the word
"seven" alone.

## Keep the family Z_3 separate from the CP character

The corpus already contains a central-circle `Z_3` family holonomy.  If this
factor is placed in the same ambient quotient as the CP denominator, then:

```text
Z_64 x Z_3 x Z_7 ~= Z_1344.
```

This is acceptable only if the physical CP character ignores the family factor
and has order `448`, for example as a character with `gcd(k,1344)=3`.
Therefore the CP statement should be phrased as a selected character claim,
not as a claim that the full ambient carrier has no additional family factor.

# Bottom line

The closest thing to a final candidate is now:

```text
Gamma_fl = coker(A_carry + A_nil + A_phase-sum),
chi_CP in Hom(Gamma_fl,U(1)),
ord(chi_CP)=448,
```

where `A_carry` is the six-level dyadic carry from shared-circle/proto-spinor
refinement, `A_nil` is a sevenfold nil/flux/Wilson row, and the lens layer
supplies the complex quarter-turn explaining the lepton `-pi/2` branch.

If the quotient is minimal, this reduces to:

```text
Gamma_fl ~= Z_448 ~= Z_64 x Z_7.
```

If the full topology is recursive or larger, the physical CP observable should
factor through the same finite order-448 character.  If the already-derived
family `Z_3` holonomy is included in the same ambient carrier, the ambient
quotient can be `Z_1344` while `chi_CP` still has order `448`.

This is not proven yet, but it is the most coherent and least ad hoc route
currently available.
