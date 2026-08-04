# q79 Cohesive Maurer-Cartan Repair and Derived-Transform Intertwiner Theorem v1

**Date:** 2026-08-02

**Status:** `CANONICAL_COHESIVE_MAURER_CARTAN_REPAIR_RESIDUAL_AND_HODGE_TANGENT_CLOSED_EXACT_ON_SHS_CONDITIONAL_BHT_DERIVED_DEFORMATION_AND_YONEDA_TRANSPORT_CLOSED_ISOMETRIC_HODGE_INTERTWINER_CHARACTERIZED_AND_WITNESSED_PHYSICAL_V3W9_HYM_METRIC_AND_FINITE_INTERTWINER_OPEN`

**Executable packet:** `q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.packet.json`

**Builder:** `build_q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.py`

**Independent verifier:** `verify_q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.py`

## 1. What is new

This theorem composes two results that were previously separate:

1. the universal heterotic `L_infinity`/Maurer-Cartan theorem already proves
   that a gauge-fixed squared residual has Hodge Hessian at an uncurved fixed
   point;
2. the q79 Hartshorne-Serre transform already supplies an actual global
   `alpha`-twisted cohesive object `S_HS` whose endomorphisms form an ordinary
   global dg algebra.

The composition removes an old ambiguity. On this object the nonlinear
closure residual is not an arbitrary polynomial ansatz. It is the canonical
curvature of a perturbed superconnection:

```text
d=[Ebar,-],
F(a)=d a+a^2=(Ebar+a)^2,
F(a)=0  <=>  Ebar+a remains integrable.
```

This is a structural benchmark on `S_HS`. It is not yet the selected physical
`V3/W9` Hull-Strominger endpoint.

## 2. Repair operator from the same source

Choose a Hermitian pairing and use the gauge row `d_0^dagger a`. Define

```text
Phi(a)=(d_1 a+a^2, d_0^dagger a),
E(a)=1/2 ||Phi(a)||^2.
```

At the integrable background `a=0`,

```text
D Phi(0)=(d_1,d_0^dagger),
Hess E(0)=d_1^dagger d_1+d_0 d_0^dagger=Delta_1.
```

Consequently the negative-gradient repair flow has tangent equation

```text
partial_s a=-Delta_1 a
```

and tangent semigroup `exp(-s Delta_1)`. The heat operator is therefore the
linear shadow of nonlinear integrability repair on this cohesive object.

The algebraic residual is canonical once the cohesive object is fixed. The
Hermitian metric, adjoint, absolute action scale and physical moment-map rows
remain additional source data; `d^dagger a=0` is a gauge fixing and is not
silently identified with the physical HYM equation.

## 3. What the BHT transform preserves

The hash-bound q79 corpus conditionally supplies a nonequivariant twisted BHT
Fourier-Mukai equivalence carrying

```text
kappa_hol in D^b(X)  <->  S_HS in D^b(J,alpha).
```

After choosing dg enhancements, this equivalence transports the derived
endomorphism algebra up to dg/A-infinity quasi-isomorphism. Hence it preserves:

- `Ext` groups;
- Yoneda products on cohomology;
- the formal Maurer-Cartan deformation problem up to equivalence;
- obstruction classes encoded by that formal deformation problem.

This closes the benchmark `J`-to-`X` derived deformation bridge for the
Hartshorne-Serre object, conditional on the already declared BHT hypotheses.

It does **not** follow that an arbitrary Fourier-Mukai equivalence preserves a
chosen Hermitian norm, adjoint, Hodge Laplacian or numerical spectrum.
Derived equivalence is not automatically a unitary equivalence.

## 4. Exact sufficient-condition witness

For the existing nonlinear DGLA witness, take

```text
d0=(1,0)^T,
d1=(0,1),
MC(y)=y2+y2^2,
G(y)=y1.
```

Its cost Hessian is the identity. Transport all degree spaces by the exact
orthogonal matrix

```text
U1=[['sqrt(2)/2', 'sqrt(2)/2'], ['sqrt(2)/2', '-sqrt(2)/2']].
```

The verifier proves exactly:

```text
d1' d0'=0,
Phi'(z)=U_out Phi(U1^T z),
J'=U_out J U1^T,
H'=U1 H U1^T=[['1', '0'], ['0', '1']],
Delta1'=H',
E'(z)=E(U1^T z).
```

Thus a chain/product map that is also isometric really does intertwine the
nonlinear residual, pairing, adjoint, Hodge Hessian and repair semigroup. This
is a sufficient-condition theorem, not evidence that the physical BHT kernel
already satisfies those metric identities.

## 5. Exact boundary

Closed now:

- the canonical Maurer-Cartan curvature residual on `End(S_HS)`;
- the derivation of its tangent Hodge repair operator from the same cohesive
  source after a Hermitian choice;
- the conditional BHT transport of formal deformation theory and Yoneda
  products between `S_HS` and `kappa_hol`;
- an exact finite proof of the stronger isometric-intertwiner implication;
- zero fitted parameters and zero observed-value inputs.

Still open:

- primitive MTT selection of the physical `V3/W9` object rather than the
  benchmark `kappa_hol/S_HS` object;
- the selected Hermitian/HYM metric and physical moment-map/action rows;
- full projective `E[3]` equivariance;
- an isometric analytic BHT/Fourier-Mukai intertwiner, or a quantified
  non-isometric comparison theorem;
- the accepted continuum-to-finite cohomology/product map and its numerical
  error certificate.

The strict physical upper-object count therefore remains `3/13`. What changes
is the shape of the unknown: an arbitrary nonlinear residual is no longer
needed on the derived benchmark. The unresolved part is physical source
selection plus metric and finite intertwiners.

## 6. Next object

```text
q79SelectedPhysicalV3W9CohesiveEndpointAndIsometricFiniteIntertwiner.v1
```

It must either construct the physical pure-bundle endpoint or prove that a
derived-cohesive endpoint has the correct Chern, HYM and particle data. It must
then supply a selected metric comparison and finite cohomology/product
intertwiner. A categorical equivalence alone is not enough for numerical
spectral equality.

## 7. Reproduction

```powershell
python ./build_q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.py
python ./verify_q79_cohesive_maurer_cartan_repair_and_derived_transform_intertwiner.py
```

Expected output:

```text
Q79_COHESIVE_MAURER_CARTAN_REPAIR_AND_DERIVED_TRANSFORM_INTERTWINER_BUILD_PASS
Q79_COHESIVE_MAURER_CARTAN_REPAIR_AND_DERIVED_TRANSFORM_INTERTWINER_VERIFY_PASS
```

## 8. Primary mathematical basis

- [Dotsenko-Shadrin-Vallette, Maurer-Cartan methods in deformation theory](https://arxiv.org/abs/2212.11323)
- [Wei, twisted complexes as a dg enhancement](https://arxiv.org/abs/1504.05055)
- [Lunts-Orlov, uniqueness of enhancements](https://arxiv.org/abs/0908.4187)
- [Brinzanescu-Halanay-Trautmann, Fourier-Mukai transforms on non-Kahler elliptic bundles](https://arxiv.org/abs/1008.3365)

These establish the surrounding deformation, enhancement and transform
machinery. The q79-specific contribution is the hash-bound composition on
`S_HS`, the exact source-tier ledger and the executable isometric-intertwiner
witness.
