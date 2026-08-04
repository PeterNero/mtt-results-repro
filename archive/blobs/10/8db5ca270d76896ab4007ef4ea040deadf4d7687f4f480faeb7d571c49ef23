# B.QFT.02 First-Order Costello BV Counterterm Assessment

Date: 2026-07-26

## Decision

`CT` is closed on the compact-support auxiliary-Euclidean formal tier.
The remaining independent bridge package is `EL`.

## New result

The ordinary second-order Maxwell detour cannot provide Costello's local
first-order gauge-fixing operator. The correct q79 presentation uses the
first-order Yang-Mills BV complex

```text
Omega0
  -> Omega1 + Omega2_selfdual
  -> Omega2_selfdual + Omega3
  -> Omega4
```

with dimensions `1 -> 7 -> 7 -> 1` per gauge generator.

An exact weighted-adjoint calculation verifies:

```text
Q^2 = 0
(QGF)^2 = 0
[Q,QGF] = |xi|^2 I16
ranks = 1, 6, 1
```

These identities are checked at five nonzero rational covectors. The
degree-reversing wedge/trace BV pairing has rank 16, and both `Q` and
`QGF` are exactly pairing-skew. The construction repeats over the
`8+3+1=12` local gauge generators.

The self-dual auxiliary field is algebraically eliminated. The reduced
action is ordinary Yang-Mills plus a topological constant on the fixed
bundle sector. No physical degree of freedom or coupling is added.

## Counterterm result

For one fixed Costello asymptotic splitting, the graphwise recursion

```text
C_(i,k) =
  Sing Gamma_(i,k)(P(epsilon,T), I - earlier counterterms)
```

constructs a unique local, heat-scale-independent counterterm at every
finite perturbative bidegree. The exact q79 anomaly vector is zero in all
five local channels, so every QME obstruction is BRST exact modulo a
total derivative and is removed by a finite local primitive.

This is a formal all-orders existence and source theorem. It is not a
numerical beta-function or threshold calculation.

## Frontier delta

Before:

```text
HK closed
CT open
EL open
```

After:

```text
HK closed
first-order local BV presentation closed
CT closed at formal Euclidean tier
EL open
```

Renormalized equicausal Cauchy transport is part of `EL`, because the
Euclidean heat theory itself has no causal Cauchy structure.

## Verification

```powershell
python -m unittest tests.test_qm_source.QmSourceTestCase.test_firstorder_costello_BV_closes_formal_CT -v
python scripts/verify.py
```
