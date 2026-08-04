# q79 SM Local Auxiliary Elliptic BV Regulator Existence and Boundary-Selection Cutset Theorem v1

Date: 2026-07-24

## Verdict

The missing external operator is no longer blocked by analytic existence.

On one bounded `H^1=0` q79 chart, the selected coframe and the already
certified Standard-Model BV bundles admit a concrete auxiliary Euclidean
full-linear-BV Hilbert complex with:

```text
d_BV,X^2 = 0,
Delta_BV,X = d_BV,X d_BV,X^dagger
             + d_BV,X^dagger d_BV,X,
(Delta_BV,X+1)^-1 compact.
```

The boundary package is:

```text
gauge/ghost: relative and BRST-compatible Yang-Mills data;
Higgs:       Dirichlet data with the adjoint cotangent domain;
Weyl:        generalized APS data paired with the complementary adjoint data;
antifields:  the boundary-Green adjoints of the field domains.
```

Therefore

```text
C_Lambda = 1_[0,Lambda](Delta_BV,X)
```

is an actual finite-rank external spectral family commuting with the full
linear differential. This is the first accepted external operator row in the
q79 regulator search.

The word `auxiliary` is essential. The construction does not prove that MTT
selects the rounded region, the positive coframe metric, or the APS
convention. It also does not prove that physical observables are independent
of those choices. The ultraviolet BV integration cycle, determinant
orientation, interacting QME pushforward, regulator removal, and
fixed-coupling C*-limit remain open.

The executable certificate passes all `52/52` declared checks.

## 1. Inputs and type guards

Let

```text
O = D(U)
```

be one of the prior local q79 regions, where `U` is a bounded open subset of a
Cauchy surface with smooth boundary, compact closure, and

```text
H^1(U;R)=0.
```

The gauge bundle is trivial on this chart. The prior hyperbolic theorem
includes the on-shell symmetric-phase background

```text
(Abar,Hbar,psibar)=(0,0,0).
```

Choose a rounded smooth compact subdomain

```text
X compactly contained in O,
X diffeomorphic to a closed four-ball.
```

The selected q79 coframe `e=(e^0,e^1,e^2,e^3)` defines the positive metric

```text
g_E = sum_(a=0)^3 e^a tensor e^a
```

on `X`.

This formula is an analytic regulator construction. It is not a physical
Wick rotation, a second spacetime, or an MTT prediction that Lorentzian time
is Euclidean. The compact region and its boundary are also not physical
walls.

## 2. Full linear BV deformation complex

At the declared trivial on-shell background, the minimal gauge block is the
Maxwell detour complex, repeated for the twelve faithful gauge generators:

```text
0 -> Omega^0(adP)
  --d--> Omega^1(adP)
  --delta_E d--> Omega^1(adP)^*
  --delta_E--> Omega^0(adP)^*
  -> 0.
```

It is a complex because

```text
d^2=0,
(delta_E d)d=0,
delta_E(delta_E d)=0.
```

The middle map is the Koszul-Tate/equations-of-motion row. Thus this is not
the ghost-only BRST complex excluded by the preceding regulator criterion.

The Higgs and Weyl rows are the two-term Koszul-Tate complexes

```text
Gamma(E_H) --P_H--> Gamma(E_H)^*,

Gamma(S^+ tensor E_chiral)
  --D^+-->
Gamma(S^- tensor E_chiral),
```

together with their cotangent-adjoint rows. The algebraic
antighost/Nakanishi pair and its cotangent lift are added as a contractible
direct summand.

The finite direct sum has the already certified q79 multiplicities:

```text
12 gauge generators,
4 real Higgs components,
96 complex left-Weyl components.
```

Finite multiplicity does not affect ellipticity or compactness.

## 3. Exact principal-symbol theorem

For a nonzero Euclidean covector `k`, the gauge symbol sequence is

```text
C --k--> C^4
  --M(k)--> C^4
  --k^*--> C,

M(k)=|k|^2 I-k k^*.
```

The identities

```text
M(k)k=0,
k^*M(k)=0,
rank(k)=1,
rank(M(k))=3,
rank(k^*)=1
```

show exactness at every term. Gauge fixing adds `k k^*`, so

```text
M(k)+k k^* = |k|^2 I.
```

The Higgs principal symbol is `|k|^2 I_4`. The realified two-component Weyl
symbol obeys

```text
sigma_W(k)^T sigma_W(k)
  = sigma_W(k) sigma_W(k)^T
  = |k|^2 I_4.
```

It is therefore invertible for every nonzero `k`.

Consequently the direct-sum full linear BV symbol complex is elliptic. The
certificate executes the matrices exactly over the rationals for

```text
(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,2,3,4).
```

These samples verify the implementation. The displayed algebraic formulas,
not sampling, prove the all-covector statement.

## 4. Boundary domain

### 4.1 Gauge, ghost, and Higgs rows

Use the standard relative/tangential-Dirichlet gauge-field trace, the
compatible normal gauge-fixing condition, and Dirichlet ghost data. These
are the Yang-Mills boundary conditions whose gauge invariance and strong
ellipticity are established in the registered boundary-value literature.

Operator-theoretically, let `d_rel^p` be the closed relative/minimal
realization of `d` on `p`-forms and let

```text
delta_abs^(p+1)=(d_rel^p)^dagger.
```

The middle Maxwell map is the natural closed composition

```text
M_rel=delta_abs^2 d_rel^1.
```

Its domain is the set of relative one-forms for which `d_rel^1 a` lies in
the adjoint domain. The next codifferential uses its maximal adjoint
realization. These definitions make the boundary domain part of the
operator, preserve the two zero compositions, and avoid treating a boundary
condition as informal notation.

The Higgs field has Dirichlet trace. At the zero Higgs background its
linear BRST variation vanishes. Dirichlet ghost data restrict infinitesimal
gauge transformations to the based gauge group at the regulator boundary.

The resulting de Rham Hilbert complex is closed and compact. The condition
`H^1(U;R)=0` removes the local harmonic one-form obstruction used in the
prior physical-state construction. Compact resolvent would still hold with
finite-dimensional harmonic rows; spectral regulation retains rather than
deletes them.

### 4.2 Chiral Weyl rows

A chiral operator

```text
D^+: S^+ tensor E -> S^- tensor E
```

is not an operator from one Hilbert space to itself and is not called
self-adjoint here.

Let `A_boundary` be an adapted self-adjoint tangential operator for `D^+`.
Use the generalized APS domain

```text
B_APS = H^(1/2)_(-infinity,0)(A_boundary)
```

for `D^+`. The Hilbert adjoint `D^-` receives the complementary nonnegative
boundary domain prescribed by the boundary Green form.

Generalized APS and adjoint boundary conditions are elliptic and regular.
On compact `X`, their graph domains embed compactly in `L^2`. Hence

```text
(D^+_APS)^dagger D^+_APS
```

and

```text
D^+_APS (D^+_APS)^dagger
```

are positive self-adjoint operators with compact resolvent.

The APS projector depends on the full boundary operator. It is gauge
covariant under conjugation, but it is generally not natural under arbitrary
inclusions of regions. That failure is retained as an open clause.

### 4.3 BV pairing

Every field domain is paired with its boundary-Green adjoint antifield
domain. Thus integrations by parts have no unrecorded boundary remainder.
This is the boundary typing required by the BV-BFV framework.

The finite certificate uses

```text
A_boundary = diag(-3,-1,0,2)
```

and verifies that the negative APS projector and complementary nonnegative
adjoint projector are self-adjoint, idempotent, orthogonal, exhaustive, and
covariant under unitary conjugation. The zero mode is assigned once, to the
adjoint domain.

## 5. Compact-resolvent Hodge theorem

Let `d_BV,X` be the closed direct-sum differential with the domains above.
Then

```text
Delta_BV,X
  = d_BV,X d_BV,X^dagger
    + d_BV,X^dagger d_BV,X
```

is positive and self-adjoint.

The mixed de Rham realization has compact graph embedding. The APS Weyl
realization and its adjoint have elliptic regularity, so their graph domains
also lie in positive Sobolev order and embed compactly by Rellich. Dirichlet
Laplace-type Higgs rows have the same property. A finite direct sum preserves
compactness.

Therefore

```text
(Delta_BV,X+1)^-1
```

is compact.

The Hodge-spectral theorem proved in the preceding packet now applies
without another hypothesis. For every `Lambda>=0`,

```text
C_Lambda = 1_[0,Lambda](Delta_BV,X)
```

is finite-rank, self-adjoint, nested, and a chain map. It preserves the BV
cotangent pairing when paired spectral rows are retained together. Its
positive omitted spectrum has the exact Hodge contracting homotopy

```text
h_Lambda
  = d_BV,X^dagger Delta_BV,X^-1 (1-C_Lambda).
```

## 6. What this closes

Closed:

```text
existence of one typed external full-linear-BV operator/domain: yes;
elliptic full-BV principal symbol:                          exact;
BRST-compatible bosonic boundary package:                 established;
paired elliptic Weyl/adjoint boundary package:             established;
positive self-adjoint BV Hodge Laplacian:                  established;
compact resolvent:                                         established;
finite external spectral regulator family:                automatic.
```

Still open:

```text
physical or MTT-selected Wick rotation:                    open;
MTT selection of X and the APS convention:                 open;
regulator-choice independence replacing such selection:   open;
region-inclusion naturality at finite cutoff:              open;
UV Lagrangian cycle and determinant orientation:           open;
interacting QME-preserving BV pushforward:                 open;
uniform regulator removal:                                 open;
fixed-coupling gauge-BRST C*-limit and state:              open.
```

Thus `B.QFT.02` remains open, but its truth value has changed. The external
operator no longer has to be discovered from scratch. The next theorem must
either select this analytic package from MTT or prove that all admissible
packages yield canonically equivalent QME pushforwards and the same physical
limit.

## 7. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The rounded region, positive analytic metric, boundary convention, and
spectral coordinate are auxiliary regulator data. They remain harmless only
if physical selection or regulator-choice independence is proved before
promotion.

## 8. External theorem boundary

The analytic steps use:

- [Pauly and Schomburg](https://arxiv.org/abs/2106.03448) for closed compact
  de Rham Hilbert complexes with mixed boundary conditions;
- [Bar and Ballmann](https://arxiv.org/abs/1101.1196) for generalized APS
  conditions, adjoint domains, elliptic regularity, and Fredholm
  realizations of first-order elliptic operators;
- [Avramidi and Esposito](https://arxiv.org/abs/hep-th/9710048) for
  gauge-invariant strongly elliptic Euclidean Yang-Mills boundary problems;
- [Moss and Silva](https://arxiv.org/abs/gr-qc/9610023) for systematic
  BRST-invariant gauge boundary conditions;
- [Cattaneo, Mnev, and Reshetikhin](https://arxiv.org/abs/1201.0290) for the
  BV-BFV boundary-data requirement.

These theorems establish admissibility and existence. They do not derive an
MTT physical boundary, a q79 integration cycle, or the interacting
continuum limit.

## 9. Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Generated certificate:

```text
certificates/q79_sm_local_auxiliary_elliptic_bv_regulator.certificate.json
```
