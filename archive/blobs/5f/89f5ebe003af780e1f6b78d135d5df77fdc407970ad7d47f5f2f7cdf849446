# Selected Qa/SU3 HYM Mu and Operator Domain Selection

## Purpose

This note asks whether the extracted Iwasawa HYM matrix parameter `mu > 0` can
be selected without fitting the Qa/SU3 residual.

## Result

`mu` is not yet selected, but the correct next operator gate is now sourced.

The Strominger-selection corpus identifies the bundle Hessian block:

```text
Delta_A acting on u(E)-valued 1-forms,
in fixed gauges,
modulo symmetry directions,
with coherent projector and OU lifting terms.
```

This is stronger than the previous state.  The branch no longer merely says
"some connection determinant."  The legal mu-selection route is the Yang-Mills
Laplacian/Hessian block on the adjoint bundle.

## Routes Checked

```text
chern classes / Bianchi:
  rejected for mu-selection.
  c1, c2, c3 and Tr F_E wedge F_E constrain topology and anomaly cancellation,
  not the nonzero determinant spectrum.

Li-Yau HYM uniqueness:
  rejected as a numeric mu rule.
  It gives uniqueness after holomorphic structure and metric are fixed, but the
  explicit source still presents a positive continuous parameter mu.

mu = 1 or unit Frobenius norm:
  forbidden unless sourced.
  The diagnostic equation 2 mu + mu^2 = 3 would give mu=1, but that is a
  convenience normalization, not a physical selection rule in the corpus.

Strominger/MTT selection Hessian:
  best legal route.
  It supplies the operator domain capable of selecting mu, but not the actual
  eigenvalues or OU weights.
```

## Why This Matters

The explicit heterotic source says bundle moduli enter continuously at this
order.  Therefore the correct move is not to choose a convenient `mu`; it is to
compute the selected Hessian/spectrum as a function of `mu` and let the
source-selected MTT/Strominger functional decide.

## Remaining Data

To close this gate we need:

```text
1. write Delta_A(mu) explicitly in the invariant Iwasawa frame,
2. fix gauge and quotient symmetry directions for u(E)-valued 1-forms,
3. compute invariant-band eigenvalues lambda_k(mu),
4. import or derive the OU weights gamma_{n,k}^{-1},
5. minimize the sourced Xi/Hessian contribution in mu,
6. only then evaluate the zeta determinant or analytic torsion response.
```

## Verdict

```text
mu selected: no
operator domain selected for next gate: yes
representation for mu-lifting: adjoint / u(E)-valued 1-forms
numeric Qa/SU3 determinant: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_HYM_Delta_A_Mu_Spectrum_Computation_v1
```
