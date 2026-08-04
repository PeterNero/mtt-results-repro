# q79 Twisted Cohesive-Superconnection and Stratified-Hodge Theorem v1

**Date:** 2026-08-02

**Status:** `GLOBAL_ALPHA_TWISTED_COHESIVE_SUPERCONNECTION_ENDOMORPHISM_DG_AND_TOTAL_SPACE_HODGE_PACKAGE_CLOSED_EXACT_UNDER_STANDARD_DESCENT_AND_HERMITIAN_CHOICE_OPEN_STRATUM_RETRACTION_RECOVERED_UNIFORM_FIBERWISE_GREEN_EXCLUDED_PHYSICAL_V3W9_HYM_ACTION_AND_TRANSFORM_OPEN`

**Executable packet:** `q79_twisted_cohesive_superconnection_and_stratified_hodge.packet.json`

**Builder:** `build_q79_twisted_cohesive_superconnection_and_stratified_hodge.py`

**Independent verifier:** `verify_q79_twisted_cohesive_superconnection_and_stratified_hodge.py`

## 1. Question

The certified q79 object

```text
S_HS in D^b(J,alpha)
```

has finite local cone representatives and exact `alpha`-twisted descent. Its
rank-three contraction on `J minus E_B` uses `r^-1` and cannot cross the
exceptional divisor. The question is whether the full upper object itself can
still carry one regular differential, Hilbert and Hodge language without first
forcing it to become an ordinary pure spectral sheaf.

The answer is yes at the twisted cohesive/perfect-complex tier.

## 2. Twisted cohesive realization

The bound source already supplies a bounded local perfect atlas with chain
maps satisfying

```text
G_ij G_jk G_ki = alpha_ijk I.
```

Twisted cohesive descent represents this object by an `alpha`-twisted graded
smooth module `E^bullet` with an integrable antiholomorphic superconnection

```text
Ebar = Ebar_0+Ebar_1+Ebar_2+...,
Ebar^2=0.
```

This construction keeps the full cone. It does not divide by `r`, does not
require constant fiberwise cohomology rank, and does not require a
trivialization of `alpha` on a spectral surface.

The claim is an existence and organization theorem. A particular physical
Hermitian metric, HYM equation and action are not selected here.

## 3. Why the deformation algebra is ordinary

Although `E` is `alpha`-twisted, its endomorphism transitions are conjugations:

```text
T_i = G_ij T_j G_ij^-1.
```

On a triple overlap the scalar gerbe factor cancels. Hence `End(E)` is an
ordinary global graded algebra and

```text
d_End(T)=[Ebar,T],
d_End^2(T)=[Ebar^2,T]=0.
```

The exact qutrit witness uses unitary transitions with

```text
G01 G12 G20 = omega I,
omega^3=1,
```

while the induced triple conjugation fixes the test endomorphism exactly:

```text
triple chain multiplier = -1/2 + sqrt(3)*I/2,
endomorphism triple defect rank = 0.
```

This is the derived-complex version of twist cancellation already seen in the
physical adjoint bundle.

## 4. Global Hodge package

Choose a smooth Hermitian metric on the twisted graded module and a Hermitian
metric/density on compact `J`. The choice exists, but is not claimed to be the
selected physical metric. It defines

```text
B_E=Ebar+Ebar^dagger,
Delta_E=B_E^2.
```

Because the principal symbol is the Dolbeault symbol, `B_E` is elliptic. On a
compact boundaryless base its closure is self-adjoint with compact resolvent.
The global Hilbert complex therefore has harmonic projection and a Green
operator on the orthogonal complement of its global kernel.

The twist does not obstruct this calculus: local scalar gerbe phases are
unitary, and the operator and inner product glue equivariantly.

This global total-space statement must not be confused with a uniformly
invertible family of fiberwise Laplacians.

## 5. Exact stratified witness

Take

```text
d_r=[diag(1,0,0), r I_3]: C^6 -> C^3.
```

The open-stratum deformation retraction uses `1/r`. The full odd differential
`Q_r`, supercharge `B_r=Q_r+Q_r^dagger` and Hodge matrix `Delta_r=B_r^2`
contain no denominator and remain finite at `r=0`.

At `r=2`:

```text
spec(Delta_r)={'5': 2, '0': 3, '4': 4},
kernel dimension=3.
```

At `r=0`:

```text
spec(Delta_r)={'1': 2, '0': 7},
kernel dimension=7.
```

Thus the full complex is regular while its cohomology rank changes. The
smallest positive fiberwise eigenvalue is `r^2`, so the fiberwise Green norm
grows like `1/r^2`. The theorem therefore proves both facts at once:

```text
full cohesive operator: regular,
uniform fiberwise rank-three Hodge contraction: impossible across r=0.
```

The global total-space Green operator includes derivatives along the base and
is not obtained by taking a pointwise limit of these fiberwise inverses.

## 6. Two lawful source routes

The visible source problem now has two mathematically distinct routes.

### Pure-bundle route

Prove the carrier-specific flat Deligne class vanishes, construct the twisted
spectral line, apply inverse BHT, and prove a physical `V3/W9` HYM endpoint.
This remains the route to an ordinary heterotic bundle interpretation.

### Derived-cohesive route

Retain `S_HS` as an `alpha`-twisted cohesive module. No equation
`alpha|C=0` is needed merely to define its global differential, endomorphism
dg algebra or Hodge calculus. Physical promotion instead requires:

- a selected superconnection action/HYM or moment-map equation;
- a transform/intertwiner from the object on `J` to the physical fields on
  `X`;
- proof that its cohomology and transferred products reproduce the accepted
  particle and interaction sectors.

The derived route bypasses one representational bottleneck; it does not prove
that the ordinary bundle endpoint is unnecessary in heterotic physics.

## 7. What closes

Closed at exact structural tier:

- existence of a global `alpha`-twisted cohesive representative of the
  certified perfect-complex descent;
- a globally ordinary endomorphism dg algebra with nilpotent commutator
  differential;
- existence of a regular total-space Hilbert/Hodge package after choosing a
  Hermitian metric;
- exact recovery of the open-stratum rank-three contraction;
- exact proof that the full complex remains regular at the exceptional
  stratum while any uniform fiberwise Green operator fails;
- a lawful derived source branch that does not assume flat-Deligne
  trivialization;
- zero fitted parameters and zero observed-value inputs.

Still open physically:

- MTT selection of the Hermitian metric, action and HYM superconnection;
- equivalence or controlled transform to the physical `V3/W9` fields on `X`;
- the ordinary pure-bundle source if that interpretation is required;
- the continuum-to-finite cohomology/product intertwiner;
- physical spectra, masses, interactions and normalization.

## 8. Next object

```text
q79SelectedPhysicalCohesiveActionAndTransformIntertwiner.v1
```

It must decide whether the derived branch is physically admitted. If it is,
the selected action supplies the metric and moment map used by the endpoint
compiler. If it is not, the pure-bundle Deligne/HYM route remains mandatory.

## 9. Reproduction

```powershell
python ./build_q79_twisted_cohesive_superconnection_and_stratified_hodge.py
python ./verify_q79_twisted_cohesive_superconnection_and_stratified_hodge.py
```

Expected output:

```text
Q79_TWISTED_COHESIVE_SUPERCONNECTION_AND_STRATIFIED_HODGE_BUILD_PASS
Q79_TWISTED_COHESIVE_SUPERCONNECTION_AND_STRATIFIED_HODGE_VERIFY_PASS
```

## 10. Primary mathematical basis

- [Block, cohesive modules](https://arxiv.org/abs/math/0509284)
- [Wei, descent of dg cohesive modules](https://arxiv.org/abs/1804.00993)
- [Bismut-Shen-Wei, coherent sheaves and superconnections](https://arxiv.org/abs/2102.08129)
- [Bressler-Gorokhovsky-Nest-Tsygan, twisted-complex Chern character](https://arxiv.org/abs/0710.0643)

These sources establish the surrounding mathematics. The q79-specific result
is the application to the hash-bound `S_HS` atlas, the exact twist-cancellation
and stratified-Hodge witnesses, and the corrected physical route split.
