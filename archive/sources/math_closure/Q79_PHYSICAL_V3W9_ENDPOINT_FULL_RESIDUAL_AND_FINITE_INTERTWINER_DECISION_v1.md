# q79 Physical V3/W9 Endpoint, Full Residual and Finite-Intertwiner Decision v1

**Date:** 2026-08-03

**Endpoint packet:** `q79_physical_v3w9_endpoint_full_residual.packet.json`

**Finite-readout packet:** `q79_same_source_continuum_to_finite_intertwiner_cutset.packet.json`

## 1. Exact source decision

This result ingests `UST.G1E` and `UST.G2` from the requested unified-source
commit `0a7c44f43eab9a02132c836364f7fc5f2158af10`. It does not repeat the ordinary-bundle-to-cohesive
embedding.

No currently bound source is a selected physical V3/W9 endpoint. The existing
`S_HS/kappa_hol` benchmark fails the physical Chern row exactly. The separately
typed smooth V3/W9 pair has the required local ranks and cohomological candidate
rows, but it has not been promoted to a holomorphic pair in one common
Gauduchon/HYM chamber. The four-row `S_phys` object is an input contract whose
four primitive rows remain unfilled.

This is a no-promotion theorem for the current source set, not a no-go against a
future physical ordinary or cohesive endpoint.

## 2. Complete residual

For a zero-defect physical endpoint `s_star`, retain the augmented base row

```text
Phi_0(s)=(MC_Y(s),L0^dagger(s-s_star)),
J=D Phi_0(s_star)=stack(L1,L0^dagger),
J^dagger J=Delta_Y,1.
```

The complete repair residual also contains

```text
mu_TX = R_Theta wedge omega^2,
mu_V  = F_V wedge omega^2,
mu_W  = F_W wedge omega^2,
B     = d(||Omega||_omega omega^2),
A     = dH-alpha_prime/4*(tr R_Theta^2-tr F_V^2-tr F_W^2),
N     = i Omega wedge bar(Omega)-c_3 omega^3.
```

The packet emits the Frechet derivative of every row. In particular, the
anomaly derivative contains the factor `alpha_prime/2` multiplying the three
curvature-variation pairings. With the selected minimal orthogonal direct sum
of endpoint-induced `L2` target metrics,

```text
H_phys=Delta_Y,1+K^dagger K.
```

No current identity proves `K=0` or
`K^dagger K=(kappa-1)Delta_Y,1`, so neither bare-Hodge absorption nor scalar
rescaling is promoted. The repair metric is not yet identified with a
Lorentzian or ten-dimensional action.

## 3. Corrected rank-102 structure

The previous augmented-Hodge mask has 19 allowed ordered lane blocks and 7716
one-mode positions. The HYM, balanced and normalization rows alone reproduce
that mask. The full real anomaly/Bianchi row has simultaneous support on

```text
Tstar_X, ad_TX, ad_V3, ad_W9, TX.
```

Its Gram term therefore permits the six previously forbidden ordered
cross-gauge blocks. The corrected full-Hessian allowable mask has 25 ordered
blocks and all 10404 positions. This is an allowable structural mask, not a
claim that every physical coefficient is nonzero.

The physical compression is

```text
p_Q H_phys i_Q
  = Delta_Q+(1/4)A0 A0^dagger+p_Q K^dagger K i_Q.
```

An exact finite witness shows the correction reducing a two-dimensional base
harmonic space to a one-dimensional intersection kernel with spectral gap one.

## 4. Same-source finite readout

The second packet proves that an isometric system map `T_fin` and residual map
`S_R` satisfying

```text
S_R K_c=K_f T_fin
```

transport `K^dagger K`, the full Hessian and the corrected harmonic projector.
For approximate maps,

```text
epsilon_H
 <= epsilon_0+(||K_f||+||K_c||)epsilon_K
    +epsilon_perp||K_c||.
```

A spectral gap then controls the projector defect. For a non-surjective
isometry an additional adjoint-leakage term is retained; it vanishes when the
selected finite image is reducing. The packet includes a
nontrivial exact rational witness. The physical q79 `T_fin` remains open because
the physical endpoint and `K` coefficients remain open; the static `F_3`
endpoint is not relabeled as the dynamic physical map.

## 5. Frontier delta

Closed here:

- hash-bound ingestion of UST.G1E/G2;
- seven-row adjudication of every current candidate class;
- complete physical residual and derivative-`K` operator formula;
- minimal orthogonal repair target and mandatory full-Hessian formula;
- correction of the rank-102 allowable mask from 19 to 25 ordered blocks;
- exact/approximate same-source full-Hessian and projector transfer theorem.

Still open:

- characteristic-zero eta9/Deligne visible source;
- twisted-holomorphic locally free hidden W9;
- one common positive Gauduchon/HYM chamber and physical connections;
- numerical `K`, harmonic projector, low spectrum and rank-102 entries;
- physical `T_fin`, product/tail bounds and clock normalization;
- cyclic/BV or Lorentzian action identification.

## 6. Primary mathematical interfaces

- de la Ossa and Svanes, *Holomorphic Bundles and the Moduli Space of N=1
  Supersymmetric Heterotic Compactifications*,
  https://arxiv.org/abs/1402.1725.
- Garcia-Fernandez, Rubio and Tipler, *Infinitesimal Moduli for the Strominger
  System and Killing Spinors in Generalized Geometry*,
  https://arxiv.org/abs/1503.07562.
- Perego, *Kobayashi-Hitchin Correspondence for Twisted Vector Bundles*,
  https://arxiv.org/abs/1910.01867.

These sources support the ambient deformation, elliptic and twisted-HYM
interfaces. The q79 candidate adjudication and corrected finite mask are the
MTT-specific results.

## 7. Reproduction

Set `MTT_UST_ROOT`, `MTT_LEGACY_CLOSURE_ROOT` or `MTT_QG_ROOT` only when the
sibling repositories are stored elsewhere, then run:

```powershell
python ./build_q79_physical_v3w9_endpoint_full_residual_and_finite_intertwiner_decision.py
python ./verify_q79_physical_v3w9_endpoint_full_residual_and_finite_intertwiner_decision.py
```
