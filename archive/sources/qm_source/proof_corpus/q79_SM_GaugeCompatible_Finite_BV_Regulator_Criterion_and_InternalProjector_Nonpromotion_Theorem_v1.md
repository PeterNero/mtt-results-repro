# q79 SM Gauge-Compatible Finite BV Regulator Criterion and Internal-Projector Nonpromotion Theorem v1

## Verdict

The next q79 Standard-Model quantum-field-theory object can now be stated
without ambiguity.

MTT does not need to select an unrelated finite projector at every cutoff.
It needs to select one external, gauge-fixed BV Hilbert-complex package

```text
(Sigma or U, Dom(d_BV), d_BV, dagger, Delta_BV, omega_BV)
```

for which

```text
d_BV^2 = 0,
Delta_BV = d_BV d_BV^dagger + d_BV^dagger d_BV
```

is positive self-adjoint with compact resolvent. Its spectral functional
calculus then emits the entire finite family

```text
C_Lambda = 1_[0,Lambda](Delta_BV)
```

automatically.

This closes the regulator criterion. It does not supply the selected
external operator or the interacting continuum limit.

The selected `27`-dimensional projected HYM package, the `96x96` finite
Standard-Model Dirac operator, the A57 finite fluctuation packet and the MLD
finite QME seed cannot substitute for this missing object. They act on
internal or finite algebraic factors and do not cut continuum spacetime
modes. That nonpromotion statement is now a theorem, not a warning.

The executable certificate passes all `63/63` declared checks.

## Audited Inputs

The result consumes the following already established tiers.

1. The q79 gauge-fixed Lorentzian SM BV complex supplies the continuum field
   bundles and normally hyperbolic or Dirac principal symbols on each declared
   on-shell chart.
2. The local formal QME, anomaly cancellation, positive formal physical state
   space and free physical C*-reference net remain intact.
3. The selected projected HYM source has
   `A_N=C^3_class tensor M_3(C)` and `dim(H_N)=27`, with exact operations only
   inside that finite source algebra.
4. The finite SM geometry has an actual `96x96` finite Dirac operator at
   profile tier.
5. A52 explicitly does not derive physical spacetime or Wick rotation and
   does not select strict spectral moments.
6. The MLD shifted-cotangent construction gives an exact finite
   nonzero-differential QME seed, while explicitly denying that its finite DGA
   is a physical spacetime discretization.

No one of these boundaries is reopened or silently strengthened.

## Full Differential Requirement

The required `d_BV` is not merely the gauge BRST differential.

It must be the full linearized gauge-fixed BV differential, including:

```text
Koszul-Tate / equations-of-motion part
    + gauge BRST part
    + antifield cotangent lift.
```

This distinction matters. A ghost-only BRST complex reduces gauge
redundancy, but its physical high-frequency modes remain cohomology. Such a
complex cannot contract the ultraviolet physical sector. The kinetic
Koszul-Tate block is what makes nonzero gauge-fixed fluctuation modes
available for BV pushforward.

## Hodge-Spectral Regulator Theorem

Let `(E,d)` be a graded Hilbert complex. Assume:

1. `d` is closed, densely defined and `d^2=0`;
2. `Delta=d d^dagger+d^dagger d` is positive self-adjoint;
3. `(Delta+1)^-1` is compact;
4. the chosen domain and boundary conditions are preserved by `d`,
   `d^dagger`, the faithful gauge action and the BV pairing;
5. the cutoff retains cotangent-paired modes together.

For `Lambda>=0`, define

```text
C_Lambda = 1_[0,Lambda](Delta).
```

Then:

```text
C_Lambda^2 = C_Lambda = C_Lambda^dagger,
rank(C_Lambda) < infinity,
[C_Lambda,d] = [C_Lambda,d^dagger] = 0,
C_Lambda C_Mu = C_min(Lambda,Mu),
s-lim_(Lambda->infinity) C_Lambda = I.
```

Let

```text
G_Lambda = Delta^-1 (I-C_Lambda)
h_Lambda = d^dagger G_Lambda.
```

The inverse is only taken on the positive omitted spectrum. Then

```text
d h_Lambda + h_Lambda d = I-C_Lambda.
```

Consequently the ultraviolet complement is contractible, all harmonic
cohomology is retained, and the inclusion of the retained spectral complex
is a quasi-isomorphism at the linear BV level.

### Proof

Compact resolvent gives a discrete spectrum with finite multiplicities and no
finite accumulation point. Therefore every bounded spectral interval has
finite-dimensional range. The spectral theorem gives self-adjoint
idempotence, nesting and strong convergence.

Nilpotency implies

```text
d Delta = d d^dagger d = Delta d,
d^dagger Delta = Delta d^dagger.
```

Functional calculus therefore makes every `C_Lambda` a chain map. On the
omitted positive spectrum,

```text
(d d^dagger+d^dagger d) Delta^-1 (I-C_Lambda)
  = I-C_Lambda,
```

which is exactly the displayed homotopy identity.

This theorem is a sufficient automatic construction. It does not claim that
every possible regulator must be spectral.

## Exact q79 Quartet Witness

For one selected gauge generator and one spatial mode, use the ordered basis

```text
(epsilon_1, epsilon_2, x, y, c, cbar)
```

with

```text
Q x = c,
Q cbar = y.
```

With the standard coefficient inner product,

```text
Delta_Q = Q Q^T + Q^T Q
        = diag(0,0,1,1,1,1).
```

Hence

```text
C_0 = 1_{0}(Delta_Q)
    = diag(1,1,0,0,0,0)
    = P_phys.
```

The reduced Green operator is `G=diag(0,0,1,1,1,1)` and
`h=Q^T G`. Exact rational matrix multiplication gives

```text
Qh+hQ = I-P_phys,
h^2 = hP_phys = P_phys h = 0.
```

Thus the physical projector already used in the local formal-state theorem
is precisely the zero-mode Hodge projector of the gauge quartet. This is a
nontrivial compatibility check. Repeating `P_phys` over every spacetime mode
does not make it a finite ultraviolet cutoff.

The certificate also executes the shifted-cotangent lift

```text
Q_BV = diag(Q,-Q^T)
```

against the canonical coefficient symplectic matrix. It verifies exact
nilpotency, preservation of the pairing and compatibility of the lifted
projector.

## Exact Nested-Family Witness

An independent eight-dimensional Hilbert complex contains two harmonic rows
and three contractible pairs with differential amplitudes `1`, `2` and `3`.
Its Hodge spectrum is

```text
(0,0,1,1,4,4,9,9).
```

The cutoffs at `0`, `1`, `4` and `9` have ranks

```text
2, 4, 6, 8.
```

Every projector is self-adjoint, idempotent and a chain map. Their products
give the smaller cutoff. For the cutoff at `1`,

```text
G_high = diag(0,0,0,0,1/4,1/4,1/9,1/9)
```

and the executable verifies

```text
d d^T G_high + d^T G_high d = I-C_1.
```

This finite model checks every algebraic identity used in the general
spectral theorem.

## Internal-Projector Nonpromotion Theorem

Let `E_ext` be an infinite-dimensional continuum field space, let `H_int` be
finite dimensional, and let `P_int` be any nonzero finite-rank operator on
`H_int`. Then

```text
ran(I_ext tensor P_int)
  = E_ext tensor ran(P_int).
```

Therefore

```text
rank(I_ext tensor P_int) = infinity.
```

The operator leaves every external high-frequency mode untouched. Any
composition made only from internal maps still has the form
`I_ext tensor T_int` and has the same defect.

### Consequences

```text
P_N on A_N or H_N:       not an external regulator;
D_F and f(D_F):          not an external regulator;
A57 internal spectra:    not an external regulator;
finite MLD DGA/QME seed: not an external regulator;
per-mode P_phys:         gauge reduction, not a mode cutoff.
```

A valid combined operation must contain a separately typed external factor,
for example

```text
C_Lambda^ext tensor P_int.
```

The certificate verifies the rank law
`rank(I_n tensor P)=n rank(P)` for `n=1,...,8` and exhibits a high external
mode that is fixed by the internal-only projector but killed by a genuine
external cutoff.

## BV Pushforward Layer

A finite projector is not yet a quantum measure. The ultraviolet fields must
be integrated rather than merely deleted.

The certificate executes an exact rational quadratic split

```text
H = [ A  B  ]
    [ B^T C ]
```

with positive invertible `C`. Completing the square gives

```text
H_eff = A-B C^-1 B^T
      = [[5/2,1/2],
         [1/2,7/6]].
```

It verifies

```text
det(H) = det(C) det(H_eff)
       = 6 * 8/3
       = 16
```

and exact block diagonalization.

This is the finite Hessian mechanism behind Wilsonian elimination. It is not
the physical q79 path integral. A QME-preserving BV pushforward additionally
requires:

1. a BV-compatible infrared/ultraviolet splitting;
2. a selected ultraviolet Lagrangian integration cycle;
3. determinant-line orientation and anomaly control;
4. an ultraviolet action satisfying the QME;
5. convergence or renormalized control across scales.

Finite-dimensional BV pushforward and Wilsonian QME preservation are
established mechanisms in the external literature. They do not select the
missing q79 data.

## Exact Remaining Object

The single source packet now required is

```text
q79ExternalGaugeFixedBVSpectralPackage = (
    Sigma_or_U,
    domain_and_boundary_conditions,
    d_BV,
    dagger,
    Delta_BV,
    C_Lambda,
    G_Lambda,
    ultraviolet_Hessian,
    integration_cycle,
    determinant_orientation
).
```

It must discharge seven clauses:

1. select a compact Cauchy-data domain or justify a compact Euclidean
   continuation;
2. select BRST-compatible elliptic boundary conditions, or use a compact
   boundaryless domain;
3. prove positivity, self-adjointness and compact resolvent;
4. prove gauge and BV-pairing equivariance;
5. select the ultraviolet inverse, integration cycle and determinant
   orientation;
6. prove QME-preserving transport across cutoffs;
7. prove regulator removal or a controlled fixed-coupling C*-limit.

The prior Lorentzian hyperbolic operators are the closest continuum input.
They do not automatically select a positive elliptic spatial or Euclidean
operator, its boundary domain, or naturality under region embeddings.

## Frontier

Closed now:

```text
finite BV regulator criterion:                         exact;
automatic family from one admissible BV Laplacian:    conditional theorem;
q79 quartet Hodge compatibility:                      exact;
internal projector as spacetime regulator:            excluded;
finite Gaussian elimination mechanism:                exact;
finite algebraic QME seed:                             already closed.
```

Still open:

```text
selected external Delta_BV/domain package;
physical QME-preserving regulator pushforward;
uniform regulator-removal estimates;
interacting fixed-coupling gauge-BRST C*-net;
selected interacting state and observable comparison.
```

No physical parameter, fit or observed value is added. `Lambda` is an
RG/regulator coordinate, not a new measured constant.

## External Context

The Hilbert-complex framework is due to
[Bruning and Lesch](https://doi.org/10.1016/0022-1236(92)90147-B).
Finite BV pushforward as a strong deformation retract and quasi-isomorphism
is developed by
[Cattaneo and Mnev](https://arxiv.org/abs/2605.30558).
QME-compatible Wilsonian flow is treated by
[Igarashi, Itoh and So](https://arxiv.org/abs/hep-th/0101101).
Heat-kernel BV renormalization with boundary illustrates why the boundary
domain is real mathematical data, not notation:
[Albert](https://arxiv.org/abs/1609.02220).

These works justify the mechanism. None proves that the q79 geometry selects
the required external operator or its fixed-coupling C*-limit.

## Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_sm_gauge_compatible_finite_bv_regulator_criterion.certificate.json
```
