---
abstract: |
  We refine the nested circle-lens-nil flavor-holonomy option by replacing
  naive real containment with complex orthogonal nesting.  The relevant
  mathematical structure is an orthogonal complex structure J, satisfying
  J^2=-1 and preserving the metric.  This is the real-linear form of
  multiplication by i and is the same structure that underlies complex Hilbert
  space, unitary Schrödinger evolution, Kähler geometry, and the complex
  structure used in the MTT quantum-field bridge.  The resulting proposal is
  that the lens level supplies a quarter-turn phase, the nil level supplies a
  sevenfold unitary rotor if such a nil monodromy is derived, and the shared
  circle may carry a dyadic refinement if the projector or Wilson/flux data
  derive it.  The key conclusion is disciplined: complex nesting is a real
  mathematical candidate and fits the Schrödinger layer better than real
  containment, but it still does not by itself prove the order-448 CP quotient.
author:
- Peter Nero
date: May 2026
title: |
  Complex Orthogonal Nesting for MTT Flavor Holonomy
---

# Purpose

The previous nested-carrier note tested the real containment picture

```text
C_1 subset L_4 subset N_7.
```

When translated into simple integer containment rows, that picture was too
rigid.  It either left free directions or collapsed the quotient to something
smaller than the effective order-448 target.

This note explores the stronger possibility:

> nesting is complex/orthogonal, not merely real inclusion.

That means each level is related to the previous level by a unitary phase
rotation, with the lens level naturally associated to the quarter-turn
operator `i`.

# Mathematical object

An orthogonal complex structure on a real carrier space `V` is a real-linear
operator

```text
J : V -> V
```

such that

```text
J^2 = -1,
g(Jx,Jy) = g(x,y).
```

It is multiplication by `i` written in real coordinates.  It rotates each
compatible real two-plane by `pi/2`.

This is the precise mathematical sense in which a level can be "turned in the
complex plane" while remaining orthogonal.

# Why this fits MTT

The MTT corpus already contains several reasons this is an admissible
direction:

1. the quantum reconstruction argues that effective Hilbert space is uniquely
   complex under admissibility and locality;
2. Schrödinger evolution is recovered as intra-basin unitary evolution;
3. the QFT bridge uses complex structures on symplectic solution spaces;
4. the string/flux slices use complex, Hermitian, Kähler, and non-Kähler
   geometry;
5. the flavor notes already require complex holonomy phases for CP violation.

Therefore complex nesting is not an alien addition.  The only question is
whether it is the specific structure selected by the flavor carrier.

# The proposed carrier picture

The real-containment shorthand

```text
C_1 subset L_4 subset N_7
```

should be replaced, for flavor CP, by a unitary nesting diagram:

```text
C --J_L--> L --R_N--> N,
```

where:

- `C` is the shared central-circle carrier;
- `J_L` is a lens quarter-turn with `J_L^2=-1`;
- `R_N` is a nil rotor, possibly sevenfold if derived;
- the pairwise flavor lines attach by unitary characters.

At the phase level this is:

```text
theta_L = theta_C + pi/2,
theta_N = theta_L + 2pi/7
```

or, in multiplicative notation,

```text
z_L = i z_C,
z_N = zeta_7 z_L.
```

Here `zeta_7 = exp(2pi i/7)`.

# Why this is better than real containment

Real containment rows such as

```text
e_l = 4 e_c,
e_n = 7 e_l
```

make the levels multiples of each other in an abelian relation matrix.  That is
not how multiplication by `i` behaves.  A quarter-turn is not "four copies" of
a circle.  It is an order-four unitary action:

```text
i^4 = 1.
```

Thus the lens contribution should enter as a finite rotor or complex structure
constraint, not as a naive scaling relation.

# Phase-lattice test

The companion script

```text
complex_nesting_phase_lattice_scan.py
```

tests the phase resolution of candidate unitary nesting lattices.

It reports:

```text
Lens quarter-turn only
  effective exponent: 4
  CKM phase error: 4.630e-01
  exact lepton -pi/2 available: True

Lens quarter-turn plus nil sevenfold rotor
  effective exponent: 28
  CKM phase error: 1.399e-02
  exact lepton -pi/2 available: True

Gaussian-style dyadic exponent 8 plus nil seven
  effective exponent: 56
  CKM phase error: 1.399e-02
  exact lepton -pi/2 available: True

Dyadic circle order 64 only
  effective exponent: 64
  CKM phase error: 2.806e-02
  exact lepton -pi/2 available: True

Dyadic circle order 64 plus nil seven
  effective exponent: 448
  CKM phase error: 6.164e-06
  exact lepton -pi/2 available: True
```

The result is exactly what the earlier finite-character work suggested, but
now with a better interpretation:

- lens `i` explains why a `-pi/2` lepton phase is natural;
- nil seven improves the source story but gives only order `28` with lens
  alone;
- an additional order-64 dyadic circle lift, combined with nil seven, gives
  the effective order-448 phase resolution.

# Caution: complex does not automatically mean Z_64

Complex structure solves one problem but not all of them.

Six binary memories do not become an order-64 cyclic phase merely because they
are arranged in complex planes.  For example, a Gaussian-integer dyadic
quotient can have 64 elements while only having exponent `8` as an abelian
phase group.  Such a quotient is still too coarse for the CKM branch.

Therefore the order-64 factor must still be a cyclic dyadic lift, nested
binary carry, projector periodicity, Wilson-line remnant, or equivalent
finite unitary character.  Complex nesting tells us how to orient the levels;
it does not by itself supply the missing dyadic resolution.

# Role of spacetime dimension

The spacetime dimension should enter the construction, but not as another
adjustable denominator in the CP quotient.

MTT already has a dimensional split:

```text
M_10 = Y_4 x X_6,
```

where `Y_4` is the effective spacetime base and `X_6` is the internal coherent
carrier.  For flavor holonomy this dimensional data plays three structural
roles.

First, `Y_4` supplies the physical Lorentzian/spin setting in which chiral
fermions, Dirac operators, and observable CKM/PMNS mixing are defined.  Thus
the flavor bundle must be compatible with a four-dimensional spin/chiral
effective theory.

Second, the internal carrier must fit inside the admissible internal geometry
selected by the circle-lens-nil hierarchy.  Dimension constrains possible
realizations, spectral gaps, and index data, but it is not by itself a finite
character quotient.

Third, the emergence of Schrödinger evolution is basin-scoped in effective
time.  The complex structure `J` used in unitary phase rotation is therefore
linked to the `3+1` effective description, but the CP denominator must still be
derived from finite unitary holonomy, not from the number `4` alone.

Thus the disciplined rule is:

> spacetime dimension constrains admissibility, chirality, spin/index data, and
> the existence of the Schrödinger/unitary layer; finite flavor CP phases come
> from the selected unitary character quotient.

This prevents a category mistake.  The `4` in spacetime dimension may explain
why a quarter-turn is structurally available in the effective quantum layer,
but it does not replace the derivation of the flavor quotient.

# Relation to Schrödinger evolution

The Schrödinger equation has the form

```text
i hbar d psi/dt = H psi.
```

Equivalently,

```text
d psi/dt = -(i/hbar) H psi.
```

The factor `i` turns Hamiltonian spectral data into norm-preserving phase
rotation.  In MTT language, this is exactly the kind of operation that belongs
inside an admissible basin: deterministic, reversible, unitary phase transport.

Complex nesting would mean that the flavor carrier uses the same kind of
orthogonal phase rotation at the internal bookkeeping level.  This is why the
idea is structurally attractive.  It aligns the flavor CP mechanism with the
already-derived Schrödinger layer rather than attaching arbitrary complex
phases afterward.

# Revised target theorem

The no-proxy flavor target should be reformulated as follows.

> Derive a finite unitary character quotient from the recursive
> circle-lens-nil carrier equipped with an orthogonal complex structure.  The
> quotient must contain a lens quarter-turn, a nil sevenfold rotor or an
> equivalent sevenfold row, and a dyadic order-64 character or equivalent
> diagonal order-448 character.  The selected pairwise flavor characters must
> satisfy the MTT phase-sum rule and reproduce the CKM/PMNS CP branches.

This is stronger and more faithful than the real-containment target.

# Correct way forward

The next derivation should not start with an integer relation matrix alone.  It
should start with a unitary carrier datum:

```text
(E_fl, g, J, nabla, rho)
```

where:

- `E_fl` is the flavor carrier bundle;
- `g` is the real metric;
- `J` is the orthogonal complex structure;
- `nabla` is a compatible unitary connection;
- `rho` is the finite character representation selected by projector,
  flux, nil monodromy, or Wilson/orbifold data.

Only after this unitary datum is specified should one pass to the finite
abelian quotient and compute the Smith normal form.

# Corpus clues for the unitary datum

A targeted corpus audit strengthens this formulation.

ProtoSpinor supplies the triadic carrier, spinorial `Z_2` loop memory,
nil survivorship basins, sector stiffness, and lens-curvature CP violation.
The central-circle paper supplies the unique shared phase/bookkeeping channel
and an explicit `Z_3` family holonomy over `S^1_cen`.  Topology-only
constraints place the phase-sum rule on pairwise Hermitian line bundles over
the four-dimensional spin base `Y_4`.  The string/flux papers supply torsional
`SU(3)`, Iwasawa, and Lens x Nil examples where flux/anomaly equations select
discrete loci.  The QM/QFT papers supply complex Hilbert rigidity,
Schrodinger/unitary propagation, and complex structures `J^2=-1` selected by
coherence phases.

The combined lesson is:

```text
Y_4 spin/chiral line-bundle data
  +
X_6 circle-lens-nil torsional/flux selection
  +
orthogonal complex structure J
  +
finite unitary character quotient
```

is the right object.  The missing `64` and `7` factors should be extracted
from this object, not inferred from dimensions or labels alone.

# Bottom line

Complex orthogonal nesting is a serious improvement over naive real nesting.
It naturally explains why the lens level wants an order-four quarter-turn and
why the construction should talk to Schrödinger/unitary evolution.

But it does not remove the proof obligation.  The remaining hard derivation is
to show that MTT selects an order-64 dyadic unitary character and a sevenfold
nil rotor, or an equivalent diagonal finite character of effective order 448.
