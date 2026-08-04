# q79 Physical-Family Source Dependency, Analytic Completion, and Finite-Projection Nonpromotion Theorem v1

**Date:** 2026-07-26
**Repository:** `mtt-qm-source-proof`
**Blockers:** `B.QFT.02`, `B.HS.01`, `B.GEO.01`, `B.ACTION.01`
**Certificate:** `certificates/q79_physical_family_source_dependency_analytic_completion_cutset.certificate.json`

## Status

This theorem closes the **analytic construction** of the physical chiral
operator family as an implication. It also proves that the current finite q79
projected source data cannot select the missing smooth physical source.

The actual selected physical family remains open because its three upstream
source objects remain open:

```text
B.HS.01      selected visible/hidden HYM endpoints
B.GEO.01     physical HYM-to-symbol Hessian naturality
B.ACTION.01  selected upper action and physical BV Hessian
```

No full-domain or continuum row is promoted.

## Current Source Boundary

The pinned q79 sources state four compatible facts:

1. the finite root-stack Reynolds Hessian is exact, rank four and has one
   overall action scale, but does not construct the nonzero-Chern continuum
   HYM bundle or Hessian;
2. the 27-mode projected HYM algebra is exact as a finite algebra, not as an
   unprojected continuum integral;
3. the universal shared line and finite Hessian intertwiner are exact on the
   flat root-stack symbol, while literal equality with the nonzero-Chern HYM
   connection is excluded by Chern-Weil theory; and
4. the anomaly-line packet fixes the determinant-line obstruction and
   zero-mode-density formula but explicitly still requires the selected
   smooth AHS/BV connection and Hessian family.

Thus the missing object is a smooth physical **lift and intertwiner**, not
another finite matrix operation.

## Theorem A: Finite Projection Does Not Select a Smooth Lift

Let \(\mathcal A\) be an infinite-dimensional affine Coulomb slice of smooth
connections on the physical q79 bundle, and let

\[
P_N:\mathcal A-A_0\longrightarrow V_N
\]

be a finite-rank linear bandlimit or projected-source map. Then
\(\ker P_N\) is infinite dimensional.

Choose a nonzero \(a\in\ker P_N\) in the Coulomb slice with
\(d_{A_0}a\ne0\). Such a choice is possible because finitely many projected
conditions cannot exhaust the infinite-dimensional coexact connection
directions. For

\[
A_t=A_0+t a,
\]

all finite source rows that factor through \(P_N A_t\) are identical.
Nevertheless,

\[
D_{A_t}=D_{A_0}+t\,c(a)
\]

for the twisted Dirac operator, where \(c(a)\) is Clifford multiplication.
For a nonzero connection variation it is not the zero operator. Consequently
the Dirac family changes, and its Hessian

\[
H_{A_t}=D_{A_t}^{*}D_{A_t}
\]

is not fixed by the finite rows.

Therefore finite projected data cannot select a unique smooth physical
connection, Dirac family or Hessian family. A future HYM/Bianchi/action
theorem may select one, but those equations are additional same-source
information and are exactly what the upstream blockers request.

### Exact Rational Witness

The certificate uses the \(8\times8\) Sylvester-Walsh matrix. The projector
onto its first four characters has rank four. The fifth character is a
nonzero exact kernel direction.

Two connection rows,

\[
A_0=0,\qquad A_1=\frac13 h_5,
\]

therefore have the same finite projection, namely zero. Their finite
derivative rows differ. The exact operator model

\[
D(A)=I+\operatorname{diag}(A)
\]

then gives distinct invertible Dirac matrices and distinct positive
Hessians, despite identical projected source data. Every calculation is
rational.

This is a nonselection witness, not a physical HYM solution.

## Theorem B: Selected Source Implies the Analytic Family

Assume the following physical source package is supplied:

1. selected smooth visible and hidden locally free bundles in one positive
   Gauduchon/HYM chamber;
2. their smooth HYM connections and a physical gauge slice;
3. a unitary parallel spectral-symbol intertwiner implementing
   `B.GEO.01`; and
4. the selected upper action and gauge-fixed physical BV Hessian implementing
   `B.ACTION.01`.

After a common Sobolev-domain trivialization, the selected Clifford
connection gives a smooth family of twisted chiral elliptic operators

\[
D_b^+:H^1(E_b^+)\longrightarrow L^2(E_b^-).
\]

The selected quadratic action and gauge fixing give a self-adjoint
compact-resolvent Hessian family \(H_b\).

On a regular chart \(U\) carrying one contour \(\Gamma\) separated from the
spectrum, holomorphic functional calculus defines

\[
P_b=\frac{1}{2\pi i}\oint_\Gamma (z-H_b)^{-1}\,dz.
\]

The projector is smooth, finite rank and constant rank on \(U\). Its
canonical Kato connection is

\[
\nabla^K=P\,d,\qquad
\dot U=[\dot P,P]U.
\]

The smooth elliptic family also has the analytic determinant line

\[
\operatorname{Det}(D)
=\det\ker(D)^*\otimes\det\operatorname{coker}(D),
\]

with Quillen metric and Bismut-Freed unitary connection. The established
Dai-Freed interface supplies the corresponding holonomy law. These objects
feed directly into the already closed anomaly and orbitwise-measure
theorems.

No additional physical scalar or discrete selector is introduced by these
analytic functors. A declared contour is local regulator/chart data. It is
not a new measured constant, and it cannot be continued through a spectral
crossing without the separate crossing/gluing theorem.

### Exact Kato Witness

For

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
P_0=\operatorname{diag}(1,0),
\]

the Cayley path has velocity \(K=2J\) at zero. The certificate verifies
exactly that

\[
\dot P_0=[K,P_0],
\qquad
[\dot P_0,P_0]=K.
\]

At parameter \(1/2\), the Cayley transform is the rational rotation

\[
U=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]

The transported rank-one projector is the spectral projector of

\[
H=P+4(I-P),
\]

whose exact gap is three.

## Dependency Corollary

The row

```text
selected_physical_chiral_projector_and_Hessian_family
```

is not an independent unresolved QFT construction. Its analytic completion
is closed, while its actual source is dependency-reduced to:

```text
B.HS.01 + B.GEO.01 + B.ACTION.01.
```

The full-domain measure contract remains `0/4`. Within that contract, only
three rows remain independent of this upstream source chain:

1. the local measure current on full quotient moduli;
2. crossing-strata and disconnected-sector gluing; and
3. cutoff-uniform locality and fixed-coupling norm control.

The continuum table remains `1/9`.

## Claim Boundary

Closed:

- finite projected q79 data do not select a unique smooth operator family;
- a selected smooth physical source canonically emits the Dirac and Hessian
  family;
- regular gapped charts canonically carry Riesz bundles and Kato connection;
- the supplied elliptic family canonically carries its analytic determinant
  line; and
- the selected-family row is dependency-reduced to the three upstream
  blockers.

Open:

- the actual visible/hidden HYM endpoints;
- the physical nonzero-Chern HYM-to-symbol Hessian intertwiner;
- the selected upper action and physical BV Hessian;
- a global geometry-selected regulator family;
- local quotient-moduli measure current;
- crossing and disconnected-sector gluing;
- uniform cutoff estimates; and
- the full interacting q79 continuum theory.

## Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:     0
new fits:                            0
new observed values:                 0
```

The rational witness scale `1/3` is auxiliary proof data and has physical
parameter count zero.

## Primary Mathematical Interfaces

- T. Kato, *Perturbation Theory for Linear Operators*: isolated Riesz
  projections and Kato transport.
- J.-M. Bismut and D. S. Freed, *The Analysis of Elliptic Families I-II*:
  determinant bundles, Quillen metric, connection, curvature and Dirac-family
  holonomy.
- X. Dai and D. S. Freed, *Eta-Invariants and Determinant Lines*:
  determinant-line variation, gluing and global-anomaly holonomy.

## Version Delta

Version 1 replaces the generic first full-domain extension row by a typed
dependency theorem. It proves both analytic sufficiency after source
selection and exact nonselection from the present finite rows. It makes no
physical-family or continuum promotion.
