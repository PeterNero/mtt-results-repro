# q79 Gauge-Fixed Laplace Operator and Interior Heat-Kernel Theorem

Date: 2026-07-26

## 1. Result

The heat-kernel work package `HK` is closed on the currently declared
boundaryless, compact-support, formal q79 QFT domain.

The proof required one correction. The previously certified operator
\[
\Delta_{\rm adj}=d_{\rm BV}d_{\rm BV}^\dagger+
d_{\rm BV}^\dagger d_{\rm BV}
\]
is positive and compact-resolvent, but the Maxwell detour differential has
arrow orders \((1,2,1)\). Consequently \(\Delta_{\rm adj}\) has a fourth-order
transverse symbol on part of the complex. Compact resolvent does not make it
Laplace type.

The correct heat operator is assembled from the already certified
background-Feynman-gauge Hessian blocks:
\[
L_{\rm gf}
=L_A\oplus L_{\rm gh}\oplus L_H
\oplus D^-D^+\oplus D^+D^-,
\tag{1.1}
\]
with the corresponding cotangent partners. Its principal symbol is
\[
\sigma_2(L_{\rm gf})(x,\xi)
=|\xi|_{g_E}^2\,\mathrm{id}
\tag{1.2}
\]
on every propagated block. It is therefore a generalized Laplace-type
operator. Smooth curvature, background, mass, Higgs and Yukawa terms are
lower order.

This proves the local heat expansion and uniform interior remainders. It
does not turn the auxiliary coframe flip into a physical Wick rotation and
does not yet identify the Euclidean heat prescription with Lorentzian
Epstein-Glaser products.

## 2. Exact Maxwell-detour correction

At a nonzero Euclidean covector \(k\), write
\[
M(k)=|k|^2I-kk^*.
\tag{2.1}
\]
The minimal gauge BV symbol is the exact complex
\[
\mathbb C\xrightarrow{k}\mathbb C^4
\xrightarrow{M(k)}\mathbb C^4
\xrightarrow{k^*}\mathbb C.
\tag{2.2}
\]

### 2.1 Why the adjoint Hodge sum fails

For \(k=(1,0,0,0)\), the transverse part of
\(\Delta_{\rm adj}\) has symbol value \(1\). After replacing \(k\) by \(2k\),
the Maxwell symbol scales by four, so its adjoint square scales by sixteen:
\[
1\longmapsto16.
\tag{2.3}
\]
A second-order Laplace symbol would scale by four. Equation (2.3) is an
exact no-go for using the naive adjoint Hodge sum as the required heat
operator.

The compact-resolvent and cofinal spectral-cutoff theorems remain valid;
only the stronger Laplace-type interpretation is excluded.

### 2.2 Costello-style symbol witness

Let
\[
\Pi_T(k)=I-\frac{kk^*}{|k|^2}
=\frac{M(k)}{|k|^2}.
\tag{2.4}
\]
Define the reverse symbol on (2.2) by
\[
k^*,\qquad \Pi_T(k),\qquad k.
\tag{2.5}
\]
It is square zero because
\[
k^*\Pi_T=0,\qquad \Pi_Tk=0,
\tag{2.6}
\]
and its graded commutator with (2.2) is
\[
[Q,Q^{\rm GF}]_{\rm symbol}=|k|^2I_{10}.
\tag{2.7}
\]
The certificate verifies (2.2), (2.6) and (2.7) exactly over the rationals
at five nonzero covectors.

The projector in (2.4) is pseudodifferential, so this symbol witness is not
misreported as a local differential gauge-fixing operator. The local
differential heat operator used below is the gauge-fixed Hessian (1.1),
whose symbol was independently certified by the Lorentzian
Feynman-'t Hooft calculation and becomes (1.2) under the auxiliary positive
coframe metric.

## 3. Higgs and Weyl blocks

For the Higgs Koszul-Tate pair, the principal equation operator is
\[
P_H(k)=|k|^2I_4.
\]
Using the identity as the reverse map gives
\[
[Q_H,Q_H^{\rm GF}]=|k|^2I_8.
\tag{3.1}
\]

For the realified Weyl symbol,
\[
\sigma_W(k)^T\sigma_W(k)
=\sigma_W(k)\sigma_W(k)^T
=|k|^2I_4.
\tag{3.2}
\]
Taking the transpose Weyl symbol as the reverse map gives
\[
[Q_W,Q_W^{\rm GF}]=|k|^2I_8.
\tag{3.3}
\]

Ghost and gauge blocks have the same metric scalar principal symbol after
background Feynman gauge. Finite q79 multiplicities do not change
ellipticity or the heat calculus.

## 4. Closed extension

Let
\[
K=\operatorname{supp}V\Subset X
\]
be the compact interaction support inside the rounded auxiliary chart, and
let
\[
\delta=\operatorname{dist}_{g_E}(K,\partial X)>0.
\tag{4.1}
\]

The chart is ball-like and the local gauge bundle is trivial. Extend the
smooth metric, bundle, connection and lower-order operator coefficients from
a neighborhood of \(K\) to a compact closed double \(\widehat X\). On
\(\widehat X\), the generalized Laplace operator \(L_{\rm gf}\) has a smooth
heat kernel with the standard near-diagonal expansion
\[
K_t(x,y)
\sim
(4\pi t)^{-2}e^{-\sigma(x,y)/(2t)}
\sum_{j\geq0}t^j a_j(x,y).
\tag{4.2}
\]
The expansion and all differentiated remainders are uniform on compact
subsets of \(K\times K\).

The coefficients \(a_j\) depend only on finite jets of the operator near the
diagonal. Therefore two closed extensions agreeing near \(K\) have the same
local coefficients there.

## 5. The auxiliary boundary is UV-flat

The exact half-line Dirichlet image formula is
\[
K_D(t;x,y)-K_{\mathbb R}(t;x,y)
=-(4\pi t)^{-1/2}
\exp\!\left[-\frac{(x+y)^2}{4t}\right].
\tag{5.1}
\]
For \(x,y\geq\delta\),
\[
|K_D-K_{\mathbb R}|
\leq
(4\pi t)^{-1/2}e^{-\delta^2/t}.
\tag{5.2}
\]

For every integer \(N\geq0\), the exponential series gives the exact
inequality
\[
e^{-\delta^2/t}
\leq
N!\left(\frac{t}{\delta^2}\right)^N.
\tag{5.3}
\]
Thus the boundary correction is \(O(t^\infty)\). Any finite derivative
prefactor is absorbed by choosing a larger \(N\).

The general not-feeling-the-boundary theorem supplies the corresponding
interior estimate for admissible nonnegative self-adjoint boundary
realizations. Parametrix locality gives the same conclusion for the smooth
generalized-Laplace bundle operator after a harmless constant shift; such a
shift does not change the principal symbol or the existence of the local
expansion.

Consequently the ultraviolet divergent coefficients generated by vertices
in \(K\) are independent of the auxiliary boundary realization. Local
counterterms remain supported in \(K\), so their boundary trace vanishes.
This removes `GLUE` as an independent *local UV counterterm* calculation on
the current domain. It does not prove finite-scale boundary independence or
cover a genuine physical boundary.

## 6. Honest APS classification

If the original bounded APS realization is retained globally, its heat
trace is not asserted to have only the ordinary local half-power expansion.
The spectral projector is pseudodifferential. General spectral-boundary heat
theory gives a polyhomogeneous expansion with power and power-log terms, and
some global boundary coefficients can be nonlocal.

This does not affect Section 5: after smearing inside \(K\), the boundary
contribution is \(O(t^\infty)\), so none of those global APS terms enters the
interior ultraviolet counterterm coefficients.

## 7. Corrected bridge

The former bridge classification said that Epstein-Glaser identification
would follow from `HK`, `CT`, `GLUE` and the
Stueckelberg-Petermann theorem. That statement omitted a type boundary.

The heat construction here is auxiliary Euclidean. The existing
Epstein-Glaser prescription is Lorentzian and causal. The
Stueckelberg-Petermann theorem compares admissible renormalization
prescriptions inside the same perturbative causal framework; it is not by
itself a Wick-rotation theorem.

The remaining bridge therefore has two independent packages:

1. **CT:** execute the graphwise local heat-counterterm recursion, solve the
   BRST primitive equations, and prove the equicausal Cauchy estimates;
2. **EL:** prove an Euclidean-to-Lorentzian local comparison, or construct
   the same smooth regulator directly in Lorentzian pAQFT and compare it
   there with Epstein-Glaser.

Local UV `GLUE` follows from support preservation after `CT`. A genuine
physical boundary or finite heat scale remains outside this closure.

## 8. Theorem

**Theorem.** On the declared trivial/smooth on-shell q79 chart and for local
interactions with compact support:

1. the naive adjoint Hodge sum is not Laplace type on the Maxwell-detour
   rows;
2. the corrected gauge-fixed gauge, ghost, Higgs and squared-Weyl operator
   has principal symbol \(|\xi|_{g_E}^2I\);
3. it admits a local generalized-Laplace heat-kernel expansion with uniform
   differentiated remainders;
4. auxiliary-boundary dependence is \(O(t^\infty)\) on the interaction
   support;
5. the unsmeared APS trace is correctly typed as power/power-log and not
   purely local.

Hence

```text
B.QFT.02_HK_selected_mixed_BV_heat_kernel_hypotheses
  = closed_on_declared_boundaryless_compact_support_
    auxiliary_Euclidean_regulator_tier;

B.QFT.02_local_UV_auxiliary_boundary_dependence
  = closed_as_O_t_infinity_on_compact_interior_support;

B.QFT.02_spectral_or_heat_to_EG_counterterm_bridge
  = open_two_independent_work_packages_CT_and_EL.
```

## 9. External theorem boundary

- I. G. Avramidi, generalized-Laplace heat-kernel coefficient calculus:
  <https://arxiv.org/abs/hep-th/9503132>.
- G. Grubb, spectral boundary conditions and power/power-log expansions:
  <https://arxiv.org/abs/math/0302286>.
- L. Li and A. Strohmaier, boundary-insensitive short-time heat estimates:
  <https://arxiv.org/abs/1604.00784>.
- B. I. Albert, heat-kernel renormalization on a class of manifolds with
  boundary: <https://arxiv.org/abs/1609.02220>.

These establish the analytic heat-calculus routes. They do not select the
auxiliary Euclidean regulator physically and do not supply the missing
Euclidean-to-Lorentzian equivalence.

## 10. Parameter ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

## 11. Reproduction

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_gaugefixed_laplace_operator_closes_local_HK -v
python scripts/verify.py
```

Certificate:

```text
certificates/q79_costello_gaugefixing_laplace_and_interior_heat_kernel.certificate.json
```
