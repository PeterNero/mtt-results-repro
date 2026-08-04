# QFT02 Cauchy-Normal Euclidean-Metric Reduction

Date: 2026-07-24

## Decision

The local regulator's positive metric and its Cauchy-normal/Euclideanization
choice are one source obligation, not two.

The exact deterministic map is

```text
(g_L,n) -> g_E=g_L+2 n_flat tensor n_flat.
```

Once the future unit Cauchy normal `n` is fixed, `g_E` is positive, unique and
equal to the existing adapted-coframe sum-of-squares metric. It introduces no
extra coefficient or anisotropy parameter.

## What Is Closed

```text
positivity of g_E;
uniqueness of g_E under the adapted sign-flip contract;
equality with sum_a ea tensor ea;
residual spatial SO(3) invariance;
diffeomorphism naturality;
reduction of two open rows to one source object.
```

The residual spatial-frame and diffeomorphism regulator-orbit theorems remain
valid without modification.

## Exact No-Go

The rational boost

```text
B_01=[[5/3,4/3],
      [4/3,5/3]]
```

preserves the Lorentzian metric and has determinant one. It changes the
adapted normal and produces

```text
g_E'=[[41/9,40/9],
      [40/9,41/9]]
```

in the boosted `0-1` block.

Both positive metrics have determinant one, but for `k=(1,0,0,0)` the scalar
elliptic principal symbol changes exactly:

```text
1 -> 41/9.
```

Since the scalar sector has no internal conjugation that can repair a changed
scalar coefficient, a boost changing the normal is not regulator-neutral at
the finite auxiliary spectral tier.

## Correct Interpretation

This is not physical Lorentz violation. The physical Lorentzian metric is
unchanged. The positive elliptic regulator metric depends on a chosen
time-normal field, as Euclideanizations generally do.

The fixed-normal presentation group contains:

```text
residual spatial Spin(3);
diffeomorphisms transporting g_L and n together;
based faithful internal gauge;
compactly supported BV gauge fixing.
```

A Lorentz boost that changes `n` moves between Euclideanization classes and
must be handled by a separate independence theorem or a q79 source-selection
rule.

## Corrected Frontier

Remove these two independent-looking rows:

```text
positive metric;
Cauchy normal / Euclideanization.
```

Replace them by:

```text
future-unit-Cauchy-normal/Euclideanization class
modulo diffeomorphism and residual SO(3).
```

The best next theorem is now sharply typed:

```text
either select n from the q79 causal data,
or prove normalized regulator independence along admissible
relative-collar deformations n_t.
```

Such a path must control the induced bulk Hodge spectrum, APS data,
determinant line and interacting cutoff limit. The present result does not
claim that closure.

## Parameter Ledger

```text
new physical continuous parameters: 0
new physical discrete selectors:    0
new fits:                           0
new observed values:                0
```

The remaining normal field is geometric source data, not a numerical fit.

## Reproduction

```powershell
python .\scripts\verify.py
python -m unittest discover -s tests -v
```

Machine-readable certificate:

```text
certificates/q79_cauchy_normal_euclidean_metric_rigidity.certificate.json
```
