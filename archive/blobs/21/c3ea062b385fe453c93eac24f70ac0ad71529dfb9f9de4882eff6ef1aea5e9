# QFT02 Euclidean Reflection, OS Positivity, and EL Cutset

Date: 2026-07-26

## Question

After closing the auxiliary-Euclidean heat-kernel (`HK`) and formal
counterterm (`CT`) packages, can the remaining Euclidean-to-Lorentzian
package `EL` be proved from current q79 data?

## Result

The pointwise temporal reflection was already closed in the Mathematical
Language Discovery packet and is consumed here without repetition:

```text
P_n(v)=-g_L(n,v)n,
R_n=I-2P_n,
g_E=g_L+2 n_flat tensor n_flat.
```

The executable certificate verifies in both the adapted and prior boosted
q79 frames that:

- `P_n` has rank one and is idempotent;
- `R_n^2=I`;
- `R_n` preserves both `g_L` and `g_E`;
- `R_(-n)=R_n`.

This is a tangent-bundle involution, not a global spacetime reflection.

## Positive theorem

On a collar satisfying the eight-row global reflection contract, including
the positive physical transfer form `-partial_tau^2+A^2`, the
positive-frequency free physical gauge covariance obeys

```text
<Theta f,Cf>
  = sum_j (2 omega_j)^(-1)
      |int exp(-omega_j tau)f_j(tau)d tau|^2
  >= 0.
```

The domain is the gauge-invariant free BRST cohomology after harmonic and
BRST-exact rows are removed. No positivity is claimed for the full
gauge-fixed BV presentation.

The exact two-mode witness has reflected Gram rank two and probe norm

```text
1273/16384.
```

## Global obstruction

Current q79 data are smooth and do not impose reflection symmetry. The exact
collar

```text
g_E=d tau^2+(1+tau)dx1^2+dx2^2+dx3^2
```

agrees with the adapted data at `tau=0`, but under
`theta(tau,x)=(-tau,x)` its `x1` coefficient at `tau=1/4` changes from
`5/4` to `3/4`. Its slice extrinsic-curvature entry is `1/2`, whereas a
slice-fixing reflection isometry would force that entry to vanish.

Therefore the inference

```text
pointwise R_n + smooth Cauchy splitting
  => selected global reflection isometry
```

is false.

## Interacting obstruction

The prior exact flat function has zero formal Taylor jet but value `1/2` at
coupling one. Consequently the two quadratic forms

```text
q0=1,
q1=1-3f
```

have the same all-orders formal jet but fixed-coupling values `1` and `-1/2`.
Formal graphwise counterterms cannot decide interacting fixed-coupling OS
positivity without an additional completion or summation rule.

## Remaining EL exits

`EL` remains one bridge with alternative routes:

1. selected global reflection contract plus fixed-coupling completion;
2. six-row analytic Calderon-projector continuation;
3. direct smooth Lorentzian regulator and comparison with the existing
   Epstein-Glaser/QME prescription.

Renormalized equicausal Cauchy transport follows after one route is proved.
`B.QFT.02` remains open.

## Primary comparisons

- [Jaffe-Ritter reflection positivity](https://arxiv.org/abs/0705.0712)
- [Gerard-Wrochna analytic Cauchy Wick rotation](https://arxiv.org/abs/1706.08942)
- [Wrochna analytic two-time continuation](https://arxiv.org/abs/1808.03859)
- [Gerard-Wrochna linearized Yang-Mills Hadamard states](https://arxiv.org/abs/1403.7153)

## Verification

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_q79_reflection_closes_free_physical_OS_and_sharpens_EL -v
python -m py_compile mtt_qm_source/build.py scripts/verify.py tests/test_qm_source.py
python scripts/verify.py
```
