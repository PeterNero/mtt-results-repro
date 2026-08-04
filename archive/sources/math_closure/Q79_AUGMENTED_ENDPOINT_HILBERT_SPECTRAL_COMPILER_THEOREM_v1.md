# q79 Augmented Endpoint-Hilbert Spectral-Compiler Theorem v1

**Date:** 2026-08-02

**Status:** `AUGMENTED_ENDPOINT_TO_HILBERT_DOMAIN_ADJOINT_HODGE_AND_SPECTRAL_GALERKIN_COMPILER_CLOSED_EXACT_UNDER_SELECTED_COMPACT_ENDPOINT_HYPOTHESES_BK3_QUOTIENT_GATE_CLOSED_PHYSICAL_CONTINUUM_RESIDUAL_AND_FINITE_INTERTWINER_OPEN`

**Executable packet:** `q79_augmented_endpoint_hilbert_spectral_compiler.packet.json`

**Builder:** `build_q79_augmented_endpoint_hilbert_spectral_compiler.py`

**Independent verifier:** `verify_q79_augmented_endpoint_hilbert_spectral_compiler.py`

## 1. Result

The old target

```text
full heterotic l1 = Dbar_Q
```

is not the correct q79 target. The primary heterotic upper complex contains
the additional form lane

```text
Y_n = Omega^(0,n)(Q_phys) direct_sum Omega^(0,n+1)(X),
L_n = [[D_n, (1/2)(-1)^n A_n], [0, C_n]],
```

where `D=Dbar_Q`, `A=partial` into the cotangent lane, and `C=dbar`.
The rank-102 `Q_phys` complex is an invariant diagonal subcomplex, not the
whole upper differential. The pulled-back K3 two-form proves that the extra
lane cannot be discarded by the old `h^(2,0)=0` shortcut.

This theorem proves the next structural step: once one compact boundaryless
q79 endpoint, its Hermitian geometry, bundle metrics, normalizations and the
above differential are selected, the Hilbert spaces, operator domains,
adjoints, Hodge Hessian and finite spectral Galerkin matrices are derived.
They are not additional numerical source rows.

## 2. Endpoint-to-Hilbert compiler

Let the selected endpoint provide a compact boundaryless Hermitian threefold,
the physical visible/hidden bundles and connections, the metric density, and
the augmented differential `L`. Complete smooth sections in the geometric
`L^2` pairing:

```text
H_n = L^2(Y_n).
```

Each first-order `L_n` has its canonical closed maximal graph domain

```text
Dom(L_n)={u in L2(Y_n): L_n u is in L2 distributionally}.
```

Its Hilbert adjoint is fixed by the same pairing. If the diagonal Dolbeault
symbol complexes are elliptic, their triangular extension is elliptic. The
associated Hodge-Dirac closure has Sobolev domain `H^1`, and the degree-one
Hodge operator

```text
Delta_Y,1 = L_1^dagger L_1 + L_0 L_0^dagger
```

therefore has a canonical nonnegative self-adjoint realization with compact
resolvent. No boundary-condition row is needed on a compact manifold without
boundary. A boundary, singular endpoint or noncompact geometry would require
additional extension data and is outside this theorem.

The relative normalization of the summands must come from the selected
geometric/action source. The theorem derives the adjoint after that
normalization is supplied; it does not choose a physical action weight by
convention.

## 3. Same-source nonlinear residual

Let `Phi_Y` be the complete augmented Maurer-Cartan plus gauge/D-term residual
at a zero-defect endpoint `C_*`. If

```text
Phi_Y(C_*)=0,
D Phi_Y(C_*) = J_1 = stack(L_1, L_0^dagger),
```

then the exact squared-defect cost satisfies

```text
Hess (1/2 ||Phi_Y||^2) at C_* = J_1^dagger J_1 = Delta_Y,1.
```

Thus the nonlinear residual, selected pairing and endpoint emit the linear
repair operator together. Higher products control nonlinear vertices but do
not alter this zero-defect tangent identity.

This is a compiler theorem. The current corpus has not yet supplied the one
physical `Phi_Y` whose rows equal all selected holomorphy, anomaly, HYM and
balanced equations.

## 4. Exact weighted witness

The bound augmented-complex packet supplies

```text
L0=[['0', '1'], ['0', '1']],
L1=[['1', '-1'], ['0', '0']],
L1 L0=0.
```

With nontrivial positive metrics `G0`, `G1`, `G2`, the metric adjoints give

```text
L0^dagger=[['-4/5', '-3/5'], ['8/5', '6/5']],
L1^dagger=[['6/5', '0'], ['-8/5', '0']],
Delta_Y,1=[['14/5', '0'], ['0', '14/5']],
spec(Delta_Y,1)={'14/5': 2}.
```

The stacked residual Jacobian has exactly the same Gram operator. The naive
unweighted transpose instead gives `[['2', '0'], ['0', '2']]` and
is wrong for this selected pairing.

The witness also retains the earlier route correction:

```text
bare Q compression = 1,
full augmented Q compression = 2,
positive correction = 1.
```

Therefore the bare rank-102 Hodge operator cannot silently replace the full
upper Hodge operator.

## 5. Canonical finite calculations

Compact resolvent gives a discrete spectrum with finite multiplicities. For
every finite cutoff `Lambda`,

```text
P_Lambda = 1_[0,Lambda](Delta_Y,1)
```

has finite rank and commutes with the Hodge operator. Its matrix entries are
geometric integrals in the selected eigenbasis; they are outputs of the
endpoint, not freely supplied Galerkin coefficients. The cutoff calculation
is exact on its finite spectral subspace, while convergence or renormalized
cutoff removal remains a separate theorem.

An arbitrary finite carrier, including the accepted 27-state carrier, is not
automatically this spectral subspace. Relating it to the continuum still
requires a commuting intertwiner, or a Feshbach-Schur effective operator when
the carrier is not invariant.

## 6. Corrected source cutset

The six physical gates of the augmented route no longer represent six
independent numerical inputs:

```text
physically closed now: 1/6
conditionally derived once the endpoint is supplied: 2
independent compound source objects still required: 2
```

The already proved `b_K3` gauge-quotient/connecting-map gate is the one
physically closed gate. The map/domain and pairing/adjoint gates are
conditional consequences of one selected compact geometric endpoint; they
are not independently adjustable rows.

The remaining frontier is exactly two compound objects:

1. `S_cont`: one selected continuum geometric residual source containing the
   physical zero-defect endpoint, product/warped regime, metric and action
   normalization, and complete augmented nonlinear residual;
2. `T_fin`: one selected continuum-to-finite spectral/intertwining functor
   carrying the relevant low modes, products and lower-order payload to the
   accepted finite operators.

These are structured maps, not two scalar fit parameters.

## 7. What closes

Closed exactly under the stated endpoint hypotheses:

- the corrected augmented upper-complex target;
- endpoint-to-`L^2` Hilbert completion;
- derivation of domains and metric adjoints from one geometry;
- the augmented Hodge Hessian as a same-residual Gram operator;
- finite-rank spectral Galerkin execution from compact resolvent;
- the reduction of six apparent physical gates to two compound source maps;
- zero fitted parameters and zero observed-value inputs.

Still open physically:

- the selected visible/hidden zero-defect Hull-Strominger endpoint and common
  positive HYM chamber;
- the selected unwarped-with-error or full-warped geometric regime;
- the full augmented nonlinear residual and action normalization;
- the accepted finite intertwiner and lower-order mass/Higgs/Yukawa payload;
- numerical continuum eigenmodes and their rigorous cutoff/tail certificate.

## 8. Next executable object

```text
q79SelectedAugmentedContinuumResidualAndFiniteIntertwiner.v1
```

It should instantiate `S_cont` first, which automatically emits the Hilbert
package and spectral Galerkin matrices proved here. It should then construct
`T_fin` and test the accepted finite operators against the same continuum
source. Reintroducing independent matrix-entry rows would move backward.

## 9. Reproduction

```powershell
python ./build_q79_augmented_endpoint_hilbert_spectral_compiler.py
python ./verify_q79_augmented_endpoint_hilbert_spectral_compiler.py
```

Expected output:

```text
Q79_AUGMENTED_ENDPOINT_HILBERT_SPECTRAL_COMPILER_BUILD_PASS
Q79_AUGMENTED_ENDPOINT_HILBERT_SPECTRAL_COMPILER_VERIFY_PASS
```
