# q79 Cofinal Free-BV Spectral Cutoff and Interacting-Counterterm Cutset Theorem

Date: 2026-07-26

## 1. Result

The prior finite-shell theorem proved the Hodge Lagrangian cycle and free QME
pushforward separately on every positive finite spectral shell. This theorem
assembles those shells into a canonical cofinal family and proves explicit
free tail bounds.

It also proves that these free bounds cannot imply convergence of local
interactions. An exact four-dimensional Weyl-scaling model has covariance
operator-norm tail tending to zero while its coincident-point trace diverges.
The remaining spectral-to-continuum bridge is therefore one local,
QME-compatible counterterm sequence, not another free-shell calculation.

## 2. Cofinal spectral family

Let
\[
\Delta_{\rm BV}=QQ^\dagger+Q^\dagger Q
\]
be the positive self-adjoint compact-resolvent Hodge Laplacian of one
admissible compact auxiliary q79 BV chart. Define
\[
P_\Lambda=\mathbf 1_{[0,\Lambda]}(\Delta_{\rm BV}).
\tag{2.1}
\]

Compact resolvent implies:

1. \(P_\Lambda\) has finite rank;
2. \(P_\Lambda\) commutes with \(Q,Q^\dagger,\Delta_{\rm BV}\);
3. \(P_\Lambda\to I\) strongly as \(\Lambda\to\infty\);
4. the projectors form a nested cofinal chain.

If \(\lambda_{\rm next}(\Lambda)\) is the first eigenvalue above the cutoff,
spectral calculus gives
\[
\left\|
\Delta_{\rm BV}^{-1}(1-P_\Lambda)
\right\|
\leq
\frac1{\lambda_{\rm next}(\Lambda)}.
\tag{2.2}
\]

Since \(QQ^\dagger\leq\Delta_{\rm BV}\),
\[
\left\|
Q^\dagger\Delta_{\rm BV}^{-1}(1-P_\Lambda)
\right\|
\leq
\frac1{\sqrt{\lambda_{\rm next}(\Lambda)}}.
\tag{2.3}
\]

Thus the free Green tail and Hodge contracting-homotopy tail vanish.

## 3. Pushforward composition

For \(\Lambda_1<\Lambda_2\), the finite-dimensional shell decomposes as
\[
\operatorname{im}P_{\Lambda_2}
=
\operatorname{im}P_{\Lambda_1}
\oplus
\operatorname{im}(P_{\Lambda_2}-P_{\Lambda_1}).
\tag{3.1}
\]

The projectors commute with the BV differential and preserve the paired Hodge
decomposition. Finite-dimensional BV pushforward is associative. Integrating
the shell \((\Lambda_1,\Lambda_2]\) and then the remaining ultraviolet modes
therefore equals the corresponding single pushforward.

This closes the cofinal free-BV cutoff family on each admissible compact
auxiliary chart. It does not prove region naturality of sharp spectral
projectors.

## 4. Exact four-dimensional obstruction

Free operator-norm convergence does not control products of distributions at
coincident points.

Use the exact model
\[
\lambda_n=n^2,\qquad d_n=n^3.
\tag{4.1}
\]
The multiplicity \(d_n\sim n^3\) is the four-dimensional Weyl-law scaling
written in an integer shell model.

Above the \(N\)-th shell, the covariance norm is bounded by
\[
\frac1{(N+1)^2}\longrightarrow0.
\tag{4.2}
\]

But the local diagonal trace through the \(N\)-th shell is
\[
\sum_{n=1}^N\frac{d_n}{\lambda_n}
=\sum_{n=1}^N n
=\frac{N(N+1)}2
\longrightarrow\infty.
\tag{4.3}
\]

This is an exact counterexample to
```text
free operator-norm tail control
  implies raw local interacting cutoff convergence.
```

It is a scaling countermodel, not a claim that these are the actual q79
eigenvalues.

## 5. Existing continuum target

The interacting continuum theory is not absent. The existing q79
Epstein-Glaser theorem already supplies, on declared on-shell charts:

- renormalized local time-ordered products;
- causal factorization and microlocal spectrum;
- local Stueckelberg-Petermann renormalization freedom;
- zero local gauge-anomaly class;
- an all-orders formal QME scheme.

The spectral route must be compared with that existing continuum
prescription. It must not reopen its formal existence theorem.

## 6. Counterterm comparison contract

Let \(Z_\Lambda\) be the local comparison map applied to the spectral-cutoff
effective interaction. The remaining bridge has six rows.

1. **Locality and support.**
   \(Z_\Lambda\) is local, analytic, support preserving and compatible with
   causal factorization.
2. **Normalization.**
   \[
   Z_\Lambda(0)=0,\qquad Z_\Lambda'(0)=I.
   \]
3. **QME and Ward compatibility.**
   The renormalized cutoff effective action satisfies the coefficientwise QME
   and Ward identities.
4. **Microlocal Cauchy estimate.**
   At every perturbative order, the renormalized products are Cauchy on
   bounded sets of local functionals in the declared Hörmander/equicausal
   seminorms.
5. **Epstein-Glaser target identification.**
   The limit equals the existing continuum prescription up to one finite
   local Stueckelberg-Petermann map.
6. **Boundary gluing compatibility.**
   Counterterms on a regulated region and its complement respect the prior
   BV-BFV dual-line gluing theorem.

These rows are requirements, not asserted outputs.

## 7. Theorem

**Theorem.** On every admissible compact auxiliary q79 BV chart:

1. the compact-resolvent Hodge Laplacian generates a canonical cofinal family
   of finite-rank BV chain projectors;
2. the free Green tail is bounded by
   \(1/\lambda_{\rm next}\);
3. the Hodge homotopy tail is bounded by
   \(1/\sqrt{\lambda_{\rm next}}\);
4. nested finite-shell BV pushforwards compose;
5. these free estimates do not imply convergence of local interactions;
6. the formal spectral-to-continuum problem reduces to the six-row
   counterterm comparison contract in Section 6.

Accordingly:
```text
B.QFT.02_cofinal_free_BV_spectral_cutoff_family
  = closed_on_each_admissible_compact_auxiliary_chart;

B.QFT.02_raw_interacting_cutoff_removal
  = excluded_without_local_counterterms;

B.QFT.02_spectral_cutoff_to_EG_counterterm_bridge
  = open_six_row_contract.
```

## 8. Remaining boundary

Still open:

- construction of \(Z_\Lambda\) satisfying all six rows;
- region-natural comparison between auxiliary charts;
- coefficientwise microlocal convergence to the EG prescription;
- fixed-coupling or nonperturbative convergence;
- the interacting physical \(C^*\)-completion.

## 9. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The displayed cutoff indices are auxiliary proof coordinates.

## 10. Reproduction

```powershell
python scripts/verify.py
python -m unittest tests.test_qm_source.QmSourceTestCase.test_free_cofinal_cutoff_closes_but_local_counterterms_remain -v
```

Certificate:
```text
certificates/q79_cofinal_free_bv_cutoff_and_interacting_counterterm_cutset.certificate.json
```

