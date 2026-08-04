# UST.G1E Bundle-Cohesive Embedding and Representability Cutset v1

**Date:** 2026-08-03

**Status:** `EXACT_BUNDLE_TO_COHESIVE_EMBEDDING_REVERSE_PHYSICAL_REPRESENTABILITY_OPEN`

## 1. Result

The ordinary-bundle and derived-cohesive constructions are not two disjoint
source classes. On a complex manifold, every holomorphic bundle has a canonical
cohesive presentation concentrated in internal degree zero. Consequently, if
the selected physical q79 `V3/W9` bundle pair exists, its local deformation
source automatically admits a cohesive-superconnection presentation.

The converse is false without extra hypotheses. A general cohesive object may
have nonzero cohomological amplitude, jumping cohomology, or the wrong
topological class. To recover the ordinary physical bundle route, its declared
transform to `X_q79` must pass the representability cutset in Section 5.

Thus `UST.G1E` is closed in the bundle-to-cohesive direction and remains open
only in the reverse, physically selected direction.

## 2. Canonical Embedding

Let `E` be a holomorphic vector bundle on a complex manifold `X`. Its Dolbeault
operator defines the cohesive module

\[
\mathcal I(E)=(E^\bullet,\mathbb E),
\qquad E^0=E,
\qquad E^j=0\ (j\ne0),
\qquad \mathbb E=\bar\partial_E.
\]

Integrability is identical in the two presentations:

\[
\mathbb E^2=0
\quad\Longleftrightarrow\quad
\bar\partial_E^2=0.
\]

The cohesive endomorphism DGA is exactly the Dolbeault deformation DGA:

\[
\operatorname{End}_{\mathrm{coh}}(\mathcal I(E))
=\left(\Omega^{0,*}(\operatorname{End}E),
[\bar\partial_E,-],\wedge\circ\right).
\]

For a twisted bundle `W^tau`, the twist of its endomorphism bundle cancels:

\[
\tau(\operatorname{End}W^\tau)=\tau-\tau=0.
\]

Therefore the visible and hidden adjoint lanes used in the rank-102 physical
complex are ordinary global deformation DGAs in both presentations.

## 3. Same Nonlinear Repair Germ

For `a` in `Omega^(0,1)(End E)`, perturbing either the Dolbeault operator or the
cohesive superconnection gives the same curvature:

\[
(\bar\partial_E+a)^2
=\bar\partial_Ea+a\wedge a.
\]

Hence the Maurer-Cartan zero locus, infinitesimal gauge action, stabilizers,
Yoneda product and formal deformation functor agree. Extending the assignment
by the identity on the `T*X`, `ad(TX)`, `TX` and form/B-field lanes gives the
same full augmented heterotic complex, including its connecting map.

This is a presentation theorem. It does not create the physical bundle or its
connection.

## 4. Metric and Hodge Compatibility

Equip `E` and `X` with the same Hermitian metrics and density in both
presentations. The `L2` pairings are then literally equal, not merely
quasi-isomorphic. It follows that the adjoints, gauge slice, Hodge operator,
gauge-fixed repair Hessian and heat semigroup agree:

\[
d_{\mathrm{coh}}^\dagger=d_E^\dagger,
\qquad
\Delta_{\mathrm{coh}}=\Delta_E,
\qquad
e^{-t\Delta_{\mathrm{coh}}}=e^{-t\Delta_E}.
\]

If the complete physical residual rows are copied from the same endpoint and
target metric, their derivative `K` is also the same, so both presentations
produce the corrected full Hessian

\[
H_{\mathrm{phys}}=\Delta_{\mathcal Y,1}+K^\dagger K.
\]

No new scale or fitted parameter enters this embedding.

## 5. Reverse Physical Representability Cutset

Let `S` be a proposed cohesive source, and let `F_X(S)` denote its declared
transform to the physical q79 space. Promotion to the ordinary physical bundle
source requires all of the following:

1. **Amplitude:** `H^j(F_X(S))=0` for `j != 0` in each claimed bundle lane.
2. **Local freeness:** `H^0(F_X(S))` is locally free of ranks 3 and 9.
3. **Topology:** determinant one and the selected visible/hidden Chern and twist
   rows hold.
4. **Augmentation:** the geometric and form-sector lanes, connecting map and
   anomaly row are preserved.
5. **Metric:** the transform is isometric, or supplies controlled form and
   spectral distortion bounds.
6. **Dynamics:** nonlinear residual, gauge action, higher products and full
   physical `K` rows intertwine.
7. **Readout:** the shared differential line and finite readout commute with
   the same transform.

The first three conditions are the algebraic representability gate. The last
four are the physical same-source gate. A derived equivalence alone proves
neither group.

## 6. Current Benchmark Obstruction

The current cohesive benchmark is

\[
S_{HS}\longleftrightarrow\kappa_{hol}
\]

under the conditional BHT transform. Its locked inverse object has

\[
(c_1,c_2)(\kappa_{hol})=(-H,3u),
\]

whereas the physical visible target requires

\[
(c_1,c_2)(V_3)=(0,9u)
\]

and ultimately `c3(V3)=+/-6`. Therefore the currently instantiated
`S_HS/kappa_hol` pair fails the topology row of the reverse cutset and cannot
be identified directly with the physical visible bundle.

This excludes the present benchmark representative, not the cohesive route.
A new physical cohesive object or transform with the required rows remains a
lawful candidate.

## 7. Consequence for the One-Source Search

The candidate picture is now nested:

```text
ordinary physical bundle source
    -> canonical metricized cohesive presentation
    -> general physical cohesive-source class
```

The immediate search should no longer ask which language to choose. It should
construct one selected physical cohesive object and decide whether it lies on
the ordinary-bundle locus. Either outcome can support one source, provided the
same physical residual, metric and finite readout are certified.

## 8. Exact Boundary

Closed:

- bundle-to-cohesive embedding;
- equality of algebraic deformation data;
- equality of metric/Hodge data when the same metric is used;
- twist cancellation in adjoint lanes;
- reverse representability checklist;
- direct-promotion obstruction for the current `S_HS/kappa_hol` benchmark.

Open:

- selected physical `V3/W9` endpoint;
- a physical cohesive object with the right transformed rows;
- reverse physical representability for that selected object;
- selected metric/action and full extra-row operator `K`;
- canonical continuum-to-finite readout.

## 9. Mathematical Basis

- Jonathan Block, [Duality and equivalence of module categories in
  noncommutative geometry I](https://arxiv.org/abs/math/0509284).
- Zhaoting Wei, [Twisted complexes on a ringed space as a dg-enhancement of
  perfect complexes](https://arxiv.org/abs/1504.05055).
- Zhaoting Wei, [Descent of dg cohesive modules for open covers on complex
  manifolds](https://arxiv.org/abs/1804.00993).

These sources establish the ambient cohesive and dg-enhancement framework. The
q79-specific contribution here is the exact nesting, physical cutset and
application of the locked Chern-row mismatch.
