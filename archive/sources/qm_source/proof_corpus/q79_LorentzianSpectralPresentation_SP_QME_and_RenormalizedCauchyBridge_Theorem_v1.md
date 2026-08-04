# q79 Lorentzian Spectral Presentation, SP-QME, and Renormalized Cauchy Bridge Theorem v1

Date: 2026-07-26

## 1. Result

The direct Lorentzian alternative in the previous `EL` cutset can be
completed at the local formal perturbative tier.

On every declared globally hyperbolic q79 on-shell chart:

1. the free BV complex admits an auxiliary smooth Cauchy spectral
   regularization;
2. every fixed perturbative graph/order can be renormalized by local
   counterterms;
3. the resulting Lorentzian prescription and the existing
   Epstein-Glaser prescription lie in one local normalized
   Stueckelberg-Petermann orbit;
4. the finite-regulator modified Ward identity can be restored to the
   exact renormalized QME, order by order, because the q79 local anomaly
   class is zero;
5. the comparison is natural under equicausal Cauchy transport and
   descends to the formal physical algebra

```text
H^0(s_hat_V,A_int(O)).
```

This fills all six rows of the earlier cutoff-to-EG contract.

It does not prove a physical Wick rotation, equality of Euclidean Costello
and Lorentzian EG coefficients, fixed-coupling convergence, numerical RG
matching, or a nonperturbative completion.

## 2. Inputs

The internal inputs are the already certified:

- q79 gauge-fixed Green-hyperbolic BV complex;
- equicausal Peierls/star algebra and time-slice quasi-isomorphism;
- local covariant Epstein-Glaser products;
- local Stueckelberg-Petermann renormalization freedom;
- exact zero five-component q79 gauge-anomaly vector;
- all-orders compatible QME scheme;
- smooth Hadamard normal-ordering cocycle;
- cofinal free spectral cutoff and local-trace obstruction;
- boundaryless BV-BFV dual-line cancellation.

The primary external inputs are:

- [Brunetti, Duetsch, and Fredenhagen, pAQFT and the renormalization groups](https://arxiv.org/abs/0901.2038);
- [Hollands and Wald, local covariant time-ordered products](https://arxiv.org/abs/gr-qc/0111108);
- [Fredenhagen and Rejzner, renormalized BV pAQFT](https://arxiv.org/abs/1110.5232);
- [D'Angelo and Rejzner, Lorentzian gauge RG](https://arxiv.org/abs/2303.01479);
- [Hawkins, Rejzner, and Visser, equicausal pAQFT](https://arxiv.org/abs/2312.15203);
- [Brunetti, Fredenhagen, and Verch, locally covariant QFT](https://arxiv.org/abs/math-ph/0112041).

The first source relates regularized covariance flows to Epstein-Glaser
renormalization and the Stueckelberg-Petermann group. The Lorentzian
gauge-flow result is used for the finite-regulator modified
Slavnov-Taylor identity, not as a theorem that the regulator preserves the
unmodified QME.

## 3. Lorentzian Cauchy spectral presentation

Let `O` be one declared q79 chart and let `Sigma` be a Cauchy surface in a
Cauchy neighborhood of the interaction support. Let

```text
C_Sigma : Sol_sc(O) -> Data_sc(Sigma)
U_Sigma : Data_sc(Sigma) -> Sol_sc(O)
```

be the mutually inverse Cauchy restriction and Green-hyperbolic evolution
maps. Transport the free BV differential `s_0` to Cauchy data:

```text
d_Sigma = C_Sigma s_0 U_Sigma.
```

Then `d_Sigma^2=0`. Its Hodge operator records the BRST splitting, but it
cannot be used alone as a UV generator: it vanishes on physical
cohomology, which contains the transverse field modes that must also be
smoothed.

Use the selected q79 spatial metric and compatible graded bundle metric to
choose a positive self-adjoint elliptic Laplace-type operator on every
Cauchy row:

```text
A_Sigma
  = 1 + nabla_Sigma^dagger nabla_Sigma + V_Sigma,
V_Sigma = V_Sigma^dagger,
A_Sigma >= c > 0.
```

It is block diagonal in ghost number and respects the field/cotangent
reality structure. On a local compact realization it has compact
resolvent. On a noncompact realization only the properly supported local
heat calculus is used. In either case, for `epsilon>0`,

```text
R_epsilon
  = exp[-epsilon (log 2) A_Sigma]
```

is smoothing and self-adjoint on all Cauchy rows, including physical
cohomology. Exact commutation with `d_Sigma` is not required. A finite
regulator may break BRST; that breaking is controlled by the modified
Slavnov-Taylor identity and removed after local renormalization in Section
5.

The dyadic normalization is an auxiliary coordinate chosen to make the
finite certificate rational. Replacing `log 2` by any positive constant
changes only the regulator parametrization.

Let `C_F,Sigma` denote the Cauchy-data form of a chosen compatible
Lorentzian Feynman/Hadamard contraction. Define

```text
Delta_F,epsilon
  = U_Sigma R_epsilon C_F,Sigma
      R_epsilon^dagger U_Sigma^dagger.
```

For positive `epsilon` this has a smooth kernel on the active local domain.
As `epsilon` decreases to zero it converges to the original contraction
away from partial and total diagonals. For two positive regulator values,
the covariance difference is smooth, so the prior normal-ordering
isomorphism applies:

```text
beta_(epsilon2,epsilon1)
  = exp[hbar Gamma_(Delta_F,epsilon2-Delta_F,epsilon1)].
```

The additive covariance identity gives the exact cocycle

```text
beta_(3,2) beta_(2,1) = beta_(3,1).
```

### Important finite-cutoff boundary

`Delta_F,epsilon` is a smooth presentation regulator. It is generally
nonlocal at finite `epsilon`; its regularized time ordering need not obey
strict causal factorization or the unmodified QME. These properties are
statements about the renormalized local limit, not the raw cutoff.

No Lorentzian hyperbolic kinetic operator is being treated as a positive
elliptic heat generator. Positivity belongs to the auxiliary elliptic
Cauchy operator.

## 4. Local counterterm comparison

Let `Smat_epsilon` denote the regularized formal S-matrix constructed with
`Delta_F,epsilon`. For regular functionals it is well defined without
extending singular products. On local functionals, its graph kernels
converge off the diagonals.

At every finite graph and perturbative bidegree, extend the off-diagonal
kernel by the local Epstein-Glaser scaling-degree procedure. Equivalently,
subtract the finite Taylor jet supported on each relevant diagonal. The
forest recursion makes these subtractions compatible on nested partial
diagonals. Hence there is a normalized local counterterm map

```text
Z_epsilon(0)=0,
Z_epsilon'(0)=id
```

such that

```text
Smat_L
  = lim_(epsilon -> 0)
      Smat_epsilon composed with Z_epsilon
```

exists coefficientwise in the relevant distributional/equicausal
seminorms.

The limit `Smat_L` satisfies locality, covariance, field independence, causal
factorization, unitarity, and the Action Ward identity. The already
constructed `Smat_EG` satisfies the same axioms. The main theorem of
renormalization therefore gives one unique normalized local
Stueckelberg-Petermann map with

```text
Smat_L = Smat_EG composed with Z_(L->EG).
```

This proves scheme comparison, not coefficient equality. Choosing a
different admissible Cauchy Hodge realization or smoothing profile changes
`S_L` by another element of the same formal presentation groupoid.

## 5. QME restoration

At finite regulator, write the modified Ward identity schematically as

```text
MWI_epsilon = A_epsilon.
```

At perturbative order `n`, after lower orders have been restored, the
Quantum Action Principle and anomalous-MWI consistency make the remaining
breaking:

```text
A_n local,
gh(A_n)=1,
s A_n = 0 modulo d.
```

The controlling q79 anomaly certificate computes the complete nontrivial
four-dimensional gauge-anomaly class as

```text
[A_n] =
(0,0,0,0,0)
in H_local^(1,4)(s|d).
```

Therefore

```text
A_n = s B_n + d C_n
```

for a finite local ghost-zero primitive `B_n`. Replacing the order-`n`
counterterm by

```text
Z_epsilon,n -> Z_epsilon,n - B_n
```

removes the breaking without altering lower orders. Induction gives a
BRST-compatible Stueckelberg-Petermann comparison and the exact
renormalized QME at every finite order.

The executable witness includes a nonzero closed vector `A=sB` and verifies
exactly that adding `-B` makes the residual zero. The witness illustrates
the homological step; the actual absence of a nontrivial obstruction is the
separately certified q79 anomaly computation.

## 6. The six-row bridge

| Row | Closure |
|---|---|
| locality and support | Off-diagonal heat-smoothed contractions plus local diagonal EG extensions give support-preserving counterterms |
| normalization | `Z_epsilon(0)=0` and `Z_epsilon'(0)=id`; the exact finite jet verifies identity, inverse, and cocycle |
| QME and Ward compatibility | The finite modified identity is restored by local BRST primitives because the q79 anomaly class vanishes |
| microlocal Cauchy bound | At each fixed graph/order, proper smoothing plus local subtraction gives convergence in the declared Hormander/equicausal seminorms |
| EG target identification | The main renormalization theorem gives the unique local SP comparison with the existing EG prescription |
| boundary gluing | The active physical domain is boundaryless and the prior dual-line theorem cancels the auxiliary BV-BFV boundary factor |

Thus the old contract is `6/6` closed at the local formal tier.

## 7. Renormalized Cauchy transport

Let `O_-` and `O_+` be causally complete neighborhoods of two Cauchy
surfaces in the same declared q79 chart. Let

```text
alpha_C : A_ec(O_-) -> A_ec(O_+)
```

be the equicausal time-slice isomorphism.

Local covariant renormalization makes `Z` a natural transformation. Support
preservation ensures that its value on a local functional depends only on
the germ of the background and interaction near that support. Consequently
the square

```text
Z_O+ composed with alpha_C
  = alpha_C composed with Z_O-
```

commutes on the local/multilocal interacting domain.

After QME restoration, both arrows intertwine the nilpotent quantum BRST
differential. They therefore descend to

```text
H^0(s_hat_V,A_int(O_-))
  -> H^0(s_hat_V,A_int(O_+)).
```

This is the required renormalized equicausal Cauchy transport. It does not
extend the time-ordering operator to every equicausal functional; its
renormalized domain remains the local/multilocal subalgebra.

## 8. Exact executable witness

The certificate uses the six-dimensional complex

```text
d e_2 = e_3,
d e_4 = 2 e_5,
d e_i = 0 otherwise.
```

Its BRST Hodge spectrum is exactly

```text
(0,0,1,1,4,4).
```

The strictly positive finite regulator generator is `A=1+Delta_Hodge`, with
spectrum

```text
(1,1,2,2,5,5).
```

At dyadic step one,

```text
exp[-(log 2)A]
  = diag(1/2,1/2,1/4,1/4,1/32,1/32),
```

and step-two smoothing is its exact square. A rational `3/5-4/5` rotation
on the two harmonic modes, together with sign transport on one
contractible pair, is an orthogonal Cauchy chain map. It commutes with the
chosen finite smoother and preserves every displayed covariance. This
commuting finite model is a consistency witness, not a requirement imposed
on a general finite regulator.

The certificate also verifies:

- the covariance-shift cocycle;
- exact smoothing of all modes without deleting the physical subspace;
- a nilpotent finite counterterm-jet generator and exact SP group law;
- one nonzero BRST-exact breaking and exact counterterm cancellation.

These matrices test the algebraic identities. They are not numerical q79
beta functions or Standard-Model counterterm coefficients.

## 9. Status

Closed here:

- one direct smooth Lorentzian Cauchy spectral presentation;
- the six-row cutoff-to-EG bridge at every finite perturbative bidegree;
- local BRST-compatible SP comparison with the existing EG prescription;
- coefficientwise formal regulator removal;
- renormalized equicausal Cauchy transport on physical `H^0`;
- formal independence of auxiliary smoothing choices within the
  presentation groupoid.

Still open:

- explicit Euclidean Costello-to-Lorentzian EG coefficient comparison, if
  cross-signature equivalence is still desired;
- numerical beta functions, thresholds, matching, and uncertainties;
- a uniform fixed-nonzero-coupling regulator limit;
- an interacting gauge-BRST C-star completion;
- a selected global interacting state;
- nonperturbative completion and observable comparison.

No physical parameter, selector, fit, or observed value is introduced.
