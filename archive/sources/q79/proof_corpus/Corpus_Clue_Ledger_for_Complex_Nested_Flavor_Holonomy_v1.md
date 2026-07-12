---
abstract: |
  We audit the MTT corpus for clues relevant to the complex nested flavor
  holonomy program.  The scan focuses on ProtoSpinor, the central-circle
  paper, topology-only constraints, string/flux compactification papers, and
  quantum-mechanics/QFT reconstructions.  The result is a disciplined source
  ledger: ProtoSpinor supports a triadic circle-lens-nil carrier, nil
  survivorship basins, sector stiffness, and lens-curvature CP violation; the
  central-circle paper supports one universal circle, Z_3 family holonomy, and
  Yukawa phase/profile restriction; topology-only constraints place the
  phase-sum rule on pairwise line bundles over Y_4; string/flux work supports
  torsional SU(3), Iwasawa/Lens x Nil discrete loci, flux quantization, and
  pure phase cubic Yukawas; QM/QFT work supports complex Hilbert structure,
  Schrödinger/unitary evolution, and selected complex structures J^2=-1.  None
  of these directly derives Z_64 or Z_7, but together they sharply constrain
  the correct route: derive a finite unitary character quotient from a complex
  circle-lens-nil carrier compatible with Y_4 spin/chirality and X_6
  string/flux selection.
author:
- Peter Nero
date: May 2026
title: |
  Corpus Clue Ledger for Complex Nested Flavor Holonomy
---

# Purpose

This note records what the existing MTT corpus contributes to the current
flavor-holonomy question:

```text
Can the effective order-448 CP quotient arise from complex/orthogonal nesting
of circle, lens, and nil carriers?
```

The scan covered four clue zones:

1. ProtoSpinor and closure-strain papers;
2. the central-circle and topology-only papers;
3. string/flux compactification papers and dimension statements;
4. quantum mechanics and QFT reconstruction papers.

The goal is not to force a conclusion.  The goal is to isolate which pieces
are already corpus-supported and which remain proof obligations.

# Executive result

The corpus supports the following refined target:

```text
Y_4 spin/chiral line-bundle data
  +
X_6 circle-lens-nil carrier selection
  +
orthogonal complex structure J
  +
finite unitary character quotient
  =>
phase-sum-compatible CKM/PMNS CP holonomy.
```

It does not yet support:

```text
Z_64 or Z_7 as already-derived flavor quotient factors.
```

Those factors remain targets for extraction from projector periodicity, flux
quantization, Wilson/orbifold remnants, nil monodromy, or a concrete
string/flux realization.

# ProtoSpinor clues

## 3D proto-internal world and spin double cover

The world-in-world paper says the proto-localization scaffold is a local
encoding layer, not the full realization space.  Its key contribution is a
three-dimensional internal world at each proto-point and a forced spinorial
double cover:

```text
SO(3) -> Spin(3) ~= SU(2).
```

It also distinguishes the proto-scaffold from the full ten-dimensional
realization:

```text
X -> admissible projection -> P -> Y^4.
```

Implication for flavor:

- the spinorial `Z_2` memory is real and structural;
- it supports dyadic memory, but not by itself `Z_64`;
- it constrains chiral/fermionic encodings downstream.

The crucial caution is that ProtoSpinor's `3D` is a local proto-scaffold
dimension, not a license to overwrite the separate `M_10=Y_4 x X_6` realization.

## Nil termination and discrete survivorship

ProtoSpinor repeatedly connects nil termination with quantization and discrete
survivorship.  Closure-strain then states that exactly three generations are
nil survivorship basins.

Implication for flavor:

- nil is a genuine family/generation carrier;
- nil should appear in the flavor quotient, not merely in mass magnitudes;
- the known nil evidence points most strongly to `3` families, not yet to a
  sevenfold quotient.

Thus a `Z_7` nil rotor remains possible, but it must be derived from a more
specific nil monodromy, flux, or compactification row.

## Sector stiffness and mixing hierarchy

Closure-strain derives the qualitative hierarchy:

```text
PMNS >> CKM
```

from sector stiffness:

```text
D_q(g,h) >> D_l(g,h) >> D_nu(g,h).
```

Implication for flavor:

- numerical CKM/PMNS angles should not be treated as independent fits;
- the lepton/neutrino sectors are expected to be softer than the quark sector;
- this supports why one common holonomy quotient can project differently into
  CKM and PMNS.

## CP violation from lens-curvature misalignment

Closure-strain gives a structural CP criterion on the lens sector:

```text
R^T H_l R = H_l     CP invariant,
R^T H_l R != H_l   CP violating.
```

Here `R` is lens conjugation and `H_l` is the lens Hessian block at alignment.

Implication for flavor:

- CP violation belongs naturally to the lens redundancy/curvature layer;
- the lens quarter-turn `i` is plausible as the unitary refinement of this
  lens-sector CP geometry;
- CP phase magnitudes are explicitly execution-level and not yet computed in
  ProtoSpinor.

# Central-circle clues

The central-circle paper is one of the strongest constraints on the program.
It states that:

```text
B_1 = S^1_cen,
B_2 = S^1_cen x F_2,
B_3 = S^1_cen x F_3.
```

The circle is the unique shared internal structure, and every coherent
configuration must satisfy its constraint.

It also says the circle supports:

- nontrivial holonomy;
- conserved phase modulo `2pi`;
- winding number;
- a rigid discrete harmonic spectrum.

Implication for flavor:

- the shared circle is the natural carrier for universal phase bookkeeping;
- multiple independent circles are disfavored;
- any dyadic order-64 lift should probably be a refinement of this one shared
  circle, not six unrelated binary factors.

# Family holonomy and Yukawa restriction

The central-circle paper states that fermion families arise from a `Z_3`
holonomy of a flavor line bundle over `S^1_cen`, giving exactly three coherent
family sectors.  It also says the same circle holonomy controls allowed
left/right fermion profiles and relative phases, thereby constraining Yukawa
overlaps.

Implication for flavor:

- family holonomy is already a central-circle phenomenon;
- Yukawa existence and size are circle-restricted;
- current explicit family holonomy is `Z_3`, not `Z_64`.

This is a very useful anchor: the missing CP quotient should be compatible with
the `Z_3` family structure but should not be confused with it.

# Topology-only clues on Y_4

The topology-only paper places the rigorous line-bundle constraints on the
four-dimensional spin base `Y_4`.

The triplet data are Hermitian line bundles with flux balance:

```text
alpha_1 + alpha_2 + alpha_3 = 0.
```

Pairwise twist bundles are:

```text
L_ij = det B_i tensor det B_j.
```

The canonical trivialization is:

```text
L_12 tensor L_23 tensor L_31 ~= C.
```

This produces the phase-sum rule:

```text
arg det U_12 + arg det U_23 + arg det U_31 in 2pi Z.
```

Implication for flavor:

- the phase-sum rule is not optional and is already rigorous;
- pairwise flavor phases live naturally as unitary holonomies of line bundles;
- `Y_4` supplies spin/chirality/index constraints, not an arbitrary denominator.

# Dimension clue from Y_4

On a four-manifold, the Dirac index uses degree-four characteristic classes:

```text
Index(D tensor L) = integral_Y4 (1/2 c1(L)^2 - 1/24 p1(TY_4)).
```

For `Y_4=K3`, the corpus records a route to three families when
`c1(L_ij)^2=2`.

Implication for flavor:

- spacetime dimension enters family counting and chirality rigorously;
- this supports including `Y_4` in the proof architecture;
- it does not make spacetime dimension a CP phase denominator.

# Majorana clue

The topology-only Majorana criterion is:

```text
L^2 ~= C  iff  2 c1(L)=0.
```

Implication for flavor:

- Majorana admissibility is a two-torsion condition;
- any finite CP quotient must respect the separate two-torsion/self-character
  criterion;
- the CP weights used for CKM need not themselves be Majorana weights.

# String/flux and dimension clues

## Torsional SU(3) and complex threefolds

The string/flux papers use a torsional `SU(3)` slice, complex balanced Iwasawa,
and Lens x Nil examples.  They include:

```text
d(J^2)=0,
H = i(bar partial - partial)J,
flux quantization,
dH = alpha'/4 (Tr R_+^2 - Tr F^2).
```

Implication for flavor:

- complex structure and torsion are already part of the selected string/flux
  corner;
- nil/solv manifolds provide finite invariant bases;
- flux quantization gives a plausible source of integer quotient rows.

## Discrete loci

The heterotic selection paper states that the fixed-point/contraction criterion
selects discrete loci on:

```text
Iwasawa,
Lens x Nil.
```

In Lens x Nil, componentwise anomaly equations fix `R_1/R` for integer flux
data `(f,h)`.

Implication for flavor:

- discrete selection from flux/anomaly equations is corpus-supported;
- this is one of the best places to search for a derived `7` row;
- however, the existing worked Lens x Nil example uses `L(3,1)` and does not
  visibly derive `Z_7`.

## Iwasawa cubic Yukawa pure phase

The Iwasawa example records a normalized cubic Yukawa:

```text
lambda_123 = integral_X Omega wedge Tr(Psi_1 wedge Psi_2 wedge Psi_3),
```

which is a pure phase removable by chiral rephasing at tree level.

Implication for flavor:

- cubic/trilinear Yukawa structure is compatible with complex phase language;
- tree-level pure phases may be unphysical until flux/instantons/mixings are
  included;
- CP phase magnitudes likely require corrections beyond the normalized
  baseline.

# Quantum mechanics and QFT clues

## Complex Hilbert rigidity

The QM corpus contains a Soler/admissibility rigidity theorem: effective
quantum theory is uniquely complex under admissible projection, locality, and
basin-measure reconstruction.

It excludes:

- quaternionic Hilbert space by local tomography/predictive stability;
- real Hilbert space because it lacks phase-rich coherence transport.

Implication for flavor:

- using complex unitary phase rotations is not optional at the effective QM
  layer;
- complex orthogonal nesting fits the MTT reconstruction better than real
  containment;
- `i` should be treated as structural, not decorative.

## Schrödinger layer

The QM reconstruction obtains self-adjoint `H_obs` and unitary propagators
from closed quadratic forms.  The Schrödinger equation appears as the
basin-scoped unitary layer:

```text
i hbar d psi/dt = H psi.
```

Implication for flavor:

- complex phase rotation is tied to admissible intra-basin dynamics;
- flavor CP holonomy should be compatible with unitary time evolution;
- this supports the unitary carrier datum `(E_fl,g,J,nabla,rho)`.

## QFT complex structures

The QFT bridge explicitly uses a complex structure

```text
J^2 = -1
```

on symplectic solution spaces, with positivity

```text
mu(x,y) = sigma(x,Jy).
```

MTT projection selects a Hadamard quasifree state, hence a `J` or covariance
data, using modal coherence phases.

Implication for flavor:

- the exact mathematical object needed for complex nesting already appears in
  the corpus;
- orthogonal complex structure is a legitimate downstream encoding of
  coherence phases;
- finite flavor characters should be viewed as unitary character data on top
  of this complex structure.

# What the clues suggest

The strongest synthesis is:

```text
central circle = universal phase/bookkeeping carrier
lens = CP/conjugation/curvature-misalignment carrier
nil = family survivorship and possible discrete termination carrier
Y_4 = spin/chiral/index and phase-sum line-bundle base
X_6 = string/flux/torsional selection arena
QM/QFT = complex/unitary phase-rotation layer
```

This makes the correct forward program:

```text
derive finite unitary character quotient from a complex circle-lens-nil carrier
compatible with Y_4 line-bundle topology and X_6 torsional/flux selection.
```

# Candidate source routes for the missing factors

## Order 4

Best current source:

- lens quarter-turn as orthogonal complex structure;
- CP/lens conjugation interacting with alignment curvature;
- `Y_4` chiral/spin setting supports complex unitary dynamics but does not by
  itself give the quotient.

Status: plausible and structurally supported.

## Order 7

Possible sources:

- nil monodromy or nil termination beyond the known three family basins;
- Lens x Nil flux/anomaly equations with integer data;
- Wilson/orbifold remnant in a string/flux corner;
- worldsheet instanton or flux-induced finite phase sector.

Status: not yet derived.  The corpus gives nil discreteness and flux selection,
but not an explicit `Z_7` flavor row.

## Order 64

Possible sources:

- cyclic dyadic refinement of the shared central circle;
- nested binary carry built from repeated spinorial/refinement memories;
- projector periodicity of order 64;
- Wilson-line or orbifold remnant;
- flux/projector Diophantine row with invariant factor 64.

Status: not yet derived.  ProtoSpinor supplies genuine `Z_2` memory, but
independent binary memories remain exponent 2 unless organized into a cyclic
dyadic lift.

# Correct next calculation

The next concrete calculation should be a coupled `Y_4/X_6` finite-character
extraction:

1. choose the topology-only pairwise bundles `L_12,L_23,L_31` on `Y_4`;
2. impose the phase-sum trivialization;
3. choose a compatible torsional `SU(3)` or Lens x Nil internal realization;
4. include flux quantization and Wilson/orbifold/projector rows;
5. encode lens CP as a complex/orthogonal quarter-turn;
6. compute the finite unitary character quotient and its Smith normal form;
7. test the selected characters against CKM and PMNS phase branches.

# Bottom line

The corpus does not let us simply assert:

```text
Z_448 is already in MTT.
```

But it does give a much better route than a guessed denominator:

```text
Z_448, or an equivalent effective order-448 character, should be sought as the
finite unitary quotient selected jointly by Y_4 line-bundle topology,
central-circle phase bookkeeping, lens complex CP geometry, nil survivorship,
and X_6 string/flux quantization.
```

That is the correct way forward.
