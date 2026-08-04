# UST.G2P/G5A Physical Residual and Finite-Transfer Ingestion v1

**Date:** 2026-08-03

**Status:** `EXACT_HASH_BOUND_UPSTREAM_INGESTION_PHYSICAL_ENDPOINT_OPEN`

## 1. Provenance and Scope

This theorem ingests the independently verified closure-dynamics commit
`33c25ea2922ef26ab2c71d6165247bee8b08463f`. It reconciles that result with
`UST.G2`, `UST.G3A`, `UST.G3B` and `UST.G3C`; it does not rederive the upstream
Hull-Strominger variation formulas.

The locked upstream artifacts are:

1. the physical V3/W9 residual and finite-intertwiner decision theorem;
2. its complete-residual decision packet;
3. its same-source continuum-to-finite cutset packet.

Their SHA-256 and Git-blob identities are recorded in
`state/upstream-lock.json`. Both the dedicated upstream verifier and the full
closure-dynamics canonical verifier pass at the locked commit.

## 2. G2P: Complete Physical Residual

For a future zero-defect physical endpoint `s_*`, the upstream theorem fixes
the complete residual as

\[
\Phi_{phys}=
(\Phi_0,\mu_{TX},\mu_V,\mu_W,B,A,N),
\]

where

\[
\begin{aligned}
\mu_{TX}&=R_\Theta\wedge\omega^2,\\
\mu_V&=F_V\wedge\omega^2,\\
\mu_W&=F_W\wedge\omega^2,\\
B&=d(\|\Omega\|_\omega\omega^2),\\
A&=dH-\frac{\alpha'}4
  (\operatorname{tr}R_\Theta^2-
   \operatorname{tr}F_V^2-
   \operatorname{tr}F_W^2),\\
N&=i\Omega\wedge\overline\Omega-c_3\omega^3.
\end{aligned}
\]

The six extra derivative rows are now explicit:

\[
K=(K_{TX},K_V,K_W,K_{bal},K_{anom},K_{norm}).
\]

In particular, differentiating the curvature-square anomaly term produces the
coefficient `alpha_prime/2`, not `alpha_prime/4`.

With the declared minimal orthogonal repair target,

\[
W_{rep}=\operatorname{diag}
(I_{E_0},I_{\mu TX},I_{\mu V},I_{\mu W},I_{bal},I_{anom},I_{norm}),
\]

the exact symbolic Hessian is

\[
H_{phys}=\Delta_{\mathcal Y,1}+K^\dagger K,
\qquad
\ker H_{phys}=\ker\Delta_{\mathcal Y,1}\cap\ker K.
\]

No absorption or scalar-rescaling identity is available. The endpoint fields
and therefore the numerical coefficients of `K` remain open.

This closes `UST.G2P` at exact symbolic differential-operator tier. It is
strictly stronger than knowing only that some unspecified `K` must be added,
but strictly weaker than a physical operator execution.

## 3. Repair Metric Versus Physical Action Metric

The upstream direct-sum metric is a legitimate structural binding:

- all seven residual lanes use their endpoint-induced `L2` pairings;
- cross blocks are set to zero;
- all relative coefficients are fixed to one before empirical comparison;
- zero continuous or discrete fit parameters and zero observed values enter.

It therefore defines one exact repair model without adding adjustable scalar
rows. It does not establish either of the stronger statements:

1. that the complete q79 source-structure commutant forces this metric up to a
   common ray; or
2. that this positive repair norm is the Lorentzian, BV or ten-dimensional
   physical action metric.

Under `UST.G3C`, its present classification is
`BOUND_STRUCTURAL_REPAIR_METRIC`. It is not
`DERIVED_UNIQUE_SOURCE_METRIC`. Under `UST.G3B`, one common positive scale may
still remain. A future action or commutant theorem may promote the binding;
until then, no physical metric-selection claim is made.

## 4. Corrected Rank-102 Allowable Structure

The five complex lane ranks are

```text
Tstar_X:             3
ad_TX:               8
ad_E_visible:        8
ad_E_hidden_twisted: 80
TX:                  3
total:               102
```

The base augmented-Hodge and non-anomaly support has 19 allowed ordered lane
blocks and 7,716 one-mode positions. The real anomaly row has simultaneous
support on all five lanes. Its Gram term therefore permits six additional
ordered cross-gauge blocks:

```text
ad_TX <-> ad_E_visible
ad_TX <-> ad_E_hidden_twisted
ad_E_visible <-> ad_E_hidden_twisted
```

The complete allowable mask is consequently the full `5 x 5` mask:

```text
allowed ordered blocks: 25
allowed one-mode positions: 102^2 = 10,404
newly reconsidered positions: 2,688
```

This is a support theorem, not a nonvanishing theorem. Particular physical
entries may vanish after the endpoint is selected. What is no longer valid is
to force those 2,688 positions to zero before computing the anomaly Gram row.

The corrected compression is

\[
p_QH_{phys}i_Q=
\Delta_Q+\frac14A_0A_0^\dagger+p_QK^\dagger Ki_Q.
\]

This correction concerns the continuum/rank-102 Hessian. It does not by
itself replace or invalidate the separately typed finite `27 x 27` carrier.
Any claimed derivation of a finite physical Hessian from the old 19-block mask
must, however, be rerun through the corrected transfer.

## 5. G5A: Same-Source Full-Hessian Transfer

Let `T_fin` map the retained continuum system sector to the finite carrier and
let `S_R` map residual targets. Forward intertwining

\[
S_RK_c=K_fT_{fin}
\]

does not alone imply transfer of `K^dagger K`. Exact transfer requires:

1. `T_fin^dagger T_fin=I` on the retained system sector;
2. `S_R^dagger S_R=I` on the retained residual target;
3. forward `K` intertwining;
4. a reducing image for `K_f^dagger K_f`, or a separately certified adjoint
   square relation.

Under these conditions,

\[
T_{fin}K_c^\dagger K_c=K_f^\dagger K_fT_{fin},
\]

so the full Hessian and corrected harmonic projector commute with the readout.

For an approximate map, define

\[
\begin{aligned}
\epsilon_0&=\|H_{0,f}T-TH_{0,c}\|,\\
\epsilon_K&=\|K_fT-S_RK_c\|,\\
\epsilon_\perp&=
\|(I-TT^\dagger)K_f^\dagger S_R\|.
\end{aligned}
\]

Then

\[
\epsilon_H\le
\epsilon_0+(\|K_f\|+\|K_c\|)\epsilon_K
+\epsilon_\perp\|K_c\|.
\]

The upstream rational counterexample has `epsilon_K=0` but
`epsilon_perp=1/2`, proving that the leakage term cannot be omitted for a
nonreducing isometric image. A spectral gap then controls projector error.

This closes `UST.G5A` as the exact universal full-Hessian/projector transfer
criterion. The selected physical q79 `T_fin` remains open.

## 6. Candidate Decision

The new upstream audit agrees with `UST.G3A`:

- the reference/cohesive benchmark fails the physical Chern row;
- the smooth projective V3/W9 pair has the desired cohomological topology but
  lacks a selected holomorphic common-chamber HYM realization;
- the four primitive rows of the minimal physical source remain unfilled.

No currently bound candidate passes all seven representability rows. The
promotable-candidate count remains zero.

## 7. Frontier Delta

Closed:

- the six physical residual rows and their symbolic Frechet derivative `K`;
- the minimal orthogonal repair metric as a zero-fit structural binding;
- the corrected 25-block, 10,404-position rank-102 allowable mask;
- exact full-Hessian and harmonic-projector transfer conditions;
- the necessary adjoint-leakage term and approximate error contract.

Open:

- the characteristic-zero eta9/Deligne visible source;
- a twisted-holomorphic locally free hidden W9 in the same positive chamber;
- physical HYM connections and numerical `K` coefficients;
- source-forced uniqueness of the repair metric or its physical-action map;
- the physical harmonic projector, low spectrum and rank-102 entries;
- the selected physical `T_fin`, products, tails and clock normalization.

`UST.G2P` and `UST.G5A` are closed at their declared universal/symbolic tiers.
`UST.G3`, `UST.G4`, physical `UST.G5` and `B.HS.01` remain open.
