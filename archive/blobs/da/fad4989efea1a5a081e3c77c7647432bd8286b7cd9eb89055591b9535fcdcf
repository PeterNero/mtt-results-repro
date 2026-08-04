# UST.G2 Full-Residual Hodge Decomposition Theorem v1

**Date:** 2026-08-03

**Status:** `EXACT_UNIVERSAL_RESIDUAL_DECOMPOSITION_AND_KERNEL_THEOREM_PHYSICAL_K_OPERATOR_OPEN`

## 1. Problem Corrected

The exact augmented Maurer-Cartan-plus-gauge residual has tangent Gram operator

\[
J^\dagger J=\Delta_{\mathcal Y,1}.
\]

The complete physical Hull-Strominger residual also contains HYM moment maps,
balanced, anomaly and possibly further gauge rows. Those rows cannot be assumed
to leave the Hessian unchanged. This theorem gives the complete universal
formula and the exact equality test.

It is a Hilbert-space theorem. It does not identify the physical extra-row
operator on q79.

## 2. Orthogonal Residual Theorem

Let \(\mathcal H\), \(\mathcal E_0\) and \(\mathcal E_R\) be Hilbert spaces.
Let

\[
\Phi_0:\mathcal U\subset\mathcal H\to\mathcal E_0,
\qquad
R:\mathcal U\to\mathcal E_R
\]

be twice differentiable near \(s_*\), with

\[
\Phi_0(s_*)=0,\qquad R(s_*)=0.
\]

Set

\[
J=D\Phi_0(s_*),\qquad K=DR(s_*),
\]

and use the orthogonal target sum

\[
\Phi=(\Phi_0,R):\mathcal U\to\mathcal E_0\oplus\mathcal E_R.
\]

Then

\[
\boxed{
\operatorname{Hess}_{s_*}\frac12\|\Phi\|^2
=J^\dagger J+K^\dagger K.
}
\]

The proof is direct differentiation. Terms involving second derivatives of
\(\Phi_0\) and \(R\) are multiplied by their zero residuals and vanish.

For the augmented MTT base residual

\[
\Phi_0(a)=\left(\operatorname{MC}(a),L_0^\dagger a\right),
\]

one has

\[
J=\begin{pmatrix}L_1\\L_0^\dagger\end{pmatrix},
\qquad
J^\dagger J=\Delta_{\mathcal Y,1},
\]

so the physical result is

\[
\boxed{
H_{\mathrm{phys}}
=\Delta_{\mathcal Y,1}+K^\dagger K.
}
\]

For closed unbounded operators the same identity is read first as an equality
of nonnegative closed quadratic forms on the common form domain, followed by
the associated self-adjoint realization.

## 3. General Target-Metric Formula

If the residual target carries a nonorthogonal positive metric

\[
W=\begin{pmatrix}W_0&C\\C^\dagger&W_R\end{pmatrix},
\]

then

\[
H_W
=J^\dagger W_0J
+J^\dagger CK
+K^\dagger C^\dagger J
+K^\dagger W_RK.
\]

Thus even the phrase "the same residual norm" requires a selected target
pairing. The orthogonal formula is recovered for \(C=0\) and identity diagonal
weights.

## 4. Kernel and Spectral Consequences

In the orthogonal positive case,

\[
\langle v,H_{\mathrm{phys}}v\rangle
=\|Jv\|^2+\|Kv\|^2.
\]

Therefore

\[
\boxed{
\ker H_{\mathrm{phys}}
=\ker\Delta_{\mathcal Y,1}\cap\ker K.
}
\]

The extra physical rows can remove harmonic directions but cannot create new
ones. Also

\[
H_{\mathrm{phys}}\succeq\Delta_{\mathcal Y,1}.
\]

For compact-resolvent realizations the min-max principle implies eigenvalue
monotonicity, counted with multiplicity:

\[
\lambda_j(H_{\mathrm{phys}})
\geq\lambda_j(\Delta_{\mathcal Y,1}).
\]

This makes the extra physical rows relevant to particle/zero-mode counting;
they cannot be omitted merely because the Maurer-Cartan tangent is known.

## 5. Exact Hodge-Equality Tests

With the base target normalized as above,

\[
H_{\mathrm{phys}}=\kappa\Delta_{\mathcal Y,1}
\]

holds exactly if and only if

\[
K^\dagger K=(\kappa-1)\Delta_{\mathcal Y,1}.
\]

Consequences:

1. For \(\kappa=1\), equality requires \(K=0\) on the declared domain.
2. If \(K=SJ\) and
   \(S^\dagger S=(\kappa-1)I\) on the closure of \(\operatorname{im}J\),
   then the extra rows rescale the same Hodge operator.
3. A selected nonorthogonal target metric may absorb cross terms, but must
   satisfy the general block identity explicitly.
4. Otherwise the correct repair Hessian is the larger operator
   \(\Delta_{\mathcal Y,1}+K^\dagger K\), not the bare Hodge operator.

These alternatives are the exact test for a future moment-map, redundancy or
Kaehler-type identity.

## 6. Rank-102 Compression

Combining this theorem with the augmented-complex compression gives

\[
p_QH_{\mathrm{phys}}i_Q
=\Delta_{Q,1}
+\frac14A_0A_0^\dagger
+p_QK^\dagger Ki_Q.
\]

There are therefore two distinct positive corrections:

1. the mandatory form-sector correction from the triangular complex;
2. the physical-row correction from HYM/balanced/anomaly rows not already
   represented in the Maurer-Cartan target.

Either correction may vanish on a particular reduced domain only by theorem.

## 7. Physical Decision Packet

To instantiate the theorem, the selected q79 endpoint must emit:

1. the complete physical row map \(R\);
2. its derivative \(K\) on the same domain as \(J\);
3. the full target metric, including any cross block \(C\);
4. one of the equality certificates in Section 5, or the retained correction;
5. the resulting harmonic projector and low spectrum;
6. the rank-102 compression and finite intertwiner using the corrected operator.

No new empirical parameter is required by the theorem. The selected geometry
and action must provide the target metric and any overall scale.

## 8. Frontier Delta

`UST.G2` closes at universal theorem tier:

```text
base MC-plus-gauge Hessian: Delta_Y
full physical Hessian:      Delta_Y + K^dagger K
full kernel:                ker(Delta_Y) intersect ker(K)
exact rescaling test:       K^dagger K = (kappa-1) Delta_Y
symbolic physical K rows:   CLOSED SUBSEQUENTLY BY UST.G2P
endpoint K coefficients and action metric: OPEN
```

This corrects the earlier overly strong expectation that every physical row
must reproduce the bare Hodge operator exactly.

## 9. Subsequent Physical Specialization

The later hash-bound result `UST.G2P` fixes the six symbolic physical rows and
their Frechet derivative formulas, and binds a minimal orthogonal `L2` repair
target with zero fitted parameters. Thus "physical K open" above now means
that the selected endpoint and numerical coefficients of `K` remain open. The
source-forced or physical-action status of the target metric also remains
open. The universal formula and proof in this theorem are unchanged.
