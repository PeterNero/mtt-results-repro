# UST.G3C Source-Metric Commutant and Connected-Binding Theorem v1

**Date:** 2026-08-03

**Status:** `EXACT_SELECTION_CRITERION_PHYSICAL_TARGET_METRIC_OPEN`

## 1. Question

`UST.G2` shows that the physical repair Hessian depends on the metric of the
complete residual target. `UST.G3B` removes one harmless common positive scale
only after every relative target-sector weight has been selected. The open
question is therefore precise:

> Does the selected source structure determine the full target metric up to
> one positive ray, or do independent relative weights remain?

This theorem gives an exact answer. It includes cross-block terms and does not
assume that residual sectors are orthogonal. It supplies a reusable rational
certificate for finite targets and a continuum promotion rule.

It does not select the physical q79 endpoint or assert that its metric cone is
one-dimensional.

## 2. Invariant-Metric Commutant

Let `V` be a finite-dimensional real or complex vector space carrying a
selected source structure `S`. The structure may include automorphisms,
connection holonomies, differentials, products, pairings and declared
metric-binding intertwiners. Suppose `h_0` is one positive Hermitian metric
compatible with `S`.

For any second compatible positive Hermitian metric `h`, there is a unique
positive `h_0`-self-adjoint operator `A` such that

\[
h(u,v)=h_0(Au,v).
\]

If compatibility means invariance under a family of source operators, then
`A` lies in the corresponding structure commutant. Conversely, every
positive invertible self-adjoint element of that commutant defines a
compatible metric. Hence compatible target metrics are exactly the positive
cone

\[
\mathcal C_S=
\operatorname{Comm}(S)_{\mathrm{sa},+}.
\]

The relative metric is selected precisely when the projectivized cone
`C_S / R_{>0}` is one point. A directly checkable sufficient and necessary
condition whenever the compatible metrics form a linear Hermitian slice is

\[
\dim_{\mathbb R}\operatorname{Comm}(S)_{\mathrm{sa}}=1
\quad\text{and}\quad
\operatorname{Comm}(S)_{\mathrm{sa}}\text{ contains a positive element}.
\]

This is the exact form of the Schur argument needed here. Invoking irreducible
representations without identifying the complete source structure is not a
metric-selection proof.

**Proof.** Finite-dimensional Riesz representation gives the unique `A`.
Positivity and Hermitian symmetry of `h` make `A` positive and
`h_0`-self-adjoint. If `rho(g)` preserves both metrics, then

\[
h_0(A\rho(g)u,\rho(g)v)=h_0(Au,v)
=h_0(\rho(g)Au,\rho(g)v),
\]

so nondegeneracy gives `A rho(g)=rho(g) A`. The converse follows by reversing
the calculation. The same argument applies to every declared structure
operator. Since the identity is positive and belongs to the commutant, any
second independent self-adjoint commutant direction gives, for sufficiently
small real `epsilon`, a nonproportional positive element
`I + epsilon B`. Thus the projective positive cone is one point exactly when
the self-adjoint commutant is one-dimensional. \(\square\)

## 3. General Homogeneous Constraint Form

Choose a real presentation. A complex Hermitian target may be realified and
supplemented by the selected complex-structure compatibility equation. Let
`W=W^T` be the unknown real metric matrix. Every source-derived homogeneous
linear metric condition can be written as one or more equations

\[
\sum_{r=1}^{N_a} c_{a,r}L_{a,r}^{T}W R_{a,r}=0.
\tag{3.1}
\]

Examples include:

- finite symmetry invariance:
  `R^T W R - W = 0`;
- infinitesimal invariance:
  `X^T W + W X = 0`;
- self-adjointness of a source operator:
  `T^T W - W T = 0`;
- skew-adjointness:
  `T^T W + W T = 0`;
- complex-structure compatibility:
  `J^T W J - W = 0`.

Let `L_S` be the real vector space of symmetric solutions of (3.1), and let

\[
\mathcal C_S=\mathcal L_S\cap\operatorname{Sym}^{+}(V).
\]

Then exactly one of the following holds:

1. `C_S` is empty, so the proposed source constraints admit no positive
   target metric.
2. `C_S` is nonempty and `dim L_S = 1`, so the target metric is unique up to
   one positive scale ray.
3. `C_S` is nonempty and `dim L_S > 1`, so there are locally
   `dim L_S - 1` independent relative metric directions after quotienting the
   common scale.

The third statement follows because positive definiteness is open in the
space of symmetric matrices. A positive solution can be perturbed slightly in
any independent solution direction and remain positive.

**Proof.** Equation (3.1) is linear in the upper-triangular entries of `W`, so
its solutions form the vector space `L_S`. If `dim L_S=1`, any two nonzero
solutions are proportional; the existence of one positive solution selects
one orientation of that line and hence one positive ray. If `dim L_S=d>1`
and `W_*` is positive, choose `d-1` solution directions independent modulo
`W_*`. Openness of the positive cone keeps
`W_* + sum epsilon_i B_i` positive in a neighborhood of zero, producing
`d-1` independent projective directions. \(\square\)

## 4. Connected-Binding Corollary

Suppose the target decomposes into source sectors

\[
V=\bigoplus_{i=1}^{m}V_i
\]

and source symmetry first reduces each sector metric to
`h_i=a_i h_i^0`, with `a_i>0`. A selected metric-binding edge from sector `i`
to sector `j` imposes an exact positive ratio

\[
a_j=r_{ji}a_i,
\qquad r_{ji}>0.
\]

Construct the graph whose vertices are sectors and whose edges are these
certified ratio equations. If every product of edge ratios around a cycle is
one, the equations are consistent. If the graph has `c` connected components,
the compatible diagonal metric cone has `c` independent positive scale
factors. After quotienting one common scale, it therefore has `c-1` relative
scale parameters. In particular, a connected graph fixes all relative
weights.

**Proof.** Choose one root in each connected component. A spanning tree and
the edge equations determine every `a_i` in that component from its root
value. Cycle consistency makes the result path independent. Different root
values remain independent because no binding edge joins distinct components.
There are therefore `c` positive factors before, and `c-1` ratios after, the
common-scale quotient. \(\square\)

An untyped shared circle or common bundle does not by itself add a binding
edge. It closes a relative weight only when its connection, holonomy or
intertwiner supplies the required metric equation on the same source orbit.

Cross-block terms are not silently discarded. They must either be forced to
zero by the full constraint system or retained as variables in (3.1).

## 5. Exact Finite Certificate

For a rational finite target, enumerate the upper-triangular entries of `W`.
Equation (3.1) compiles to a rational matrix `M_S` with

\[
M_S\operatorname{vec}_{sym}(W)=0.
\]

Exact row reduction yields

\[
d=\dim\ker M_S.
\]

A rational positive witness is certified by exact principal minors. The
finite target metric is selected up to scale exactly when `d=1` and such a
witness exists.

The machine contract in
`state/ust_g3c_target_metric.schema.json` records:

- one source-orbit id and hash;
- the complete target scope;
- every homogeneous constraint and its same-source provenance;
- a rational positive witness;
- the claimed nullity and promotion tier;
- the absence of empirical metric entries.

The validator independently compiles the equations, row-reduces them and
checks positivity. Constraints carrying different source hashes fail the
same-source gate.

## 6. Continuum Promotion Boundary

A finite Galerkin or readout certificate selects only that finite metric unless
one additional theorem proves that its listed constraints generate the full
continuum structure commutant. A physical continuum promotion therefore
requires either:

1. a direct analytic proof that the bounded self-adjoint structure commutant
   is one-dimensional; or
2. an exact completeness theorem intertwining the continuum commutant with
   the certified finite one.

Compact-resolvent convergence, numerical stability or agreement of several
truncations is evidence, not this completeness theorem.

For a complex target represented over the reals, promotion also requires the
selected complex structure and its compatibility equation. Otherwise the
real metric cone may be larger than the Hermitian one.

## 7. Consequence for the Full Hessian

If the physical source passes the continuum criterion, write its unique
compatible target metric as

\[
W=\lambda W_* ,\qquad \lambda>0.
\]

Then no independent relative residual-sector weights remain. The physical
Hessian has the single scale orbit

\[
H_{phys,\lambda}=\lambda J^\dagger W_*J,
\]

and all dimensionless conclusions of `UST.G3B` follow. If the criterion
returns `d>1`, the source has at least `d-1` unresolved relative metric
directions. They must be derived, explicitly bound as physical constants, or
reported as parameters. They cannot be removed as units.

## 8. Reference Certificate

The bundled reference packet uses a three-dimensional signed-permutation
system. Sign invariance kills all cross terms, and permutation invariance ties
the three diagonal entries. Exact row reduction leaves

\[
W=aI_3,
\qquad a>0.
\]

This proves the compiler and criterion on a nonphysical example. It is not a
q79 source certificate and its physical-promotion flag is false.

## 9. Frontier Delta

Closed:

- exact characterization of compatible metrics as a positive source-structure
  commutant cone;
- exact criterion for uniqueness up to one positive ray;
- connected-binding count of remaining relative weights;
- inclusion of cross-block and complex-realification constraints;
- exact rational certificate compiler and positivity test;
- strict finite-to-continuum nonpromotion boundary.

Open:

- the selected physical q79 source orbit;
- its complete physical residual target and source-derived constraints;
- proof that the continuum structure commutant is one-dimensional;
- physical `K`, corrected harmonic projector and absolute scale.

This closes `UST.G3C` as a universal selection criterion. It does not promote
`UST.G3` or assert that the q79 relative metric has been selected.
