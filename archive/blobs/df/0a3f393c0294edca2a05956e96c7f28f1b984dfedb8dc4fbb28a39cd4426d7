# Selected Qa/SU3 Repaired Pipeline A B Diagnostic Comparison v1

## Purpose

This compares the two currently plausible algebraic erratum candidates for the
printed Qa/SU3 HYM connection.

Neither repair is source-certified.  This is a diagnostic comparison only.

## Repair Definitions

```text
Repair A:
  B1 = E13,
  B2 = -E31,
  B3 = E11 - E33.

Repair B:
  B1 = E13,
  B2 = -E32,
  B3 = E12.
```

Both are understood with the original scaling:

```text
B1, B2 carry sqrt(mu),
B3 carries mu.
```

## Integrability

Both repairs restore the standard algebraic integrability condition:

```text
F02_bar12 = B3 + [B1,B2] = 0.
```

So both are viable as algebraic erratum candidates.

## Hessian Diagnostics

Using the selected Iwasawa metric weights, the real `u(3)` Hessian diagnostics
show a difference.

Repair A:

```text
mu = 0.25: zero modes = 2, positive modes = 7
mu = 1:    zero modes = 2, positive modes = 7
mu = 4:    zero modes = 2, positive modes = 7
```

Repair B:

```text
mu = 0.25: zero modes = 1, positive modes = 8
mu = 1:    zero modes = 1, positive modes = 8
mu = 4:    zero modes = 1, positive modes = 8
```

Repair B therefore preserves the expected one-central-zero/eight-positive-mode
pattern from the original real block, while Repair A introduces an additional
zero mode.

## Mu Selection

For both repairs, the sampled Hessian log-det-prime is increasing with `mu`.
Thus neither repaired algebraic Hessian selects `mu` by itself.

## Diagnostic Ranking

The best diagnostic candidate is:

```text
Repair B: move B2 from -E31 to -E32.
```

Reason:

```text
it restores integrability and preserves the expected Hessian rank pattern.
```

But this does not make it source-certified.

## Not Closed

Still open:

```text
neither repair is source-certified,
Tr F wedge F = 0 and c3 = 6 have not been recomputed from a complete source-certified curvature matrix,
both repaired Hessian log-det samples remain monotone and do not select mu,
full threshold determinant and BRST quotient remain open.
```

## Verdict

```text
Repair A viable diagnostic: no, because of extra zero mode
Repair B viable diagnostic: yes
Repair B source-certified: no
mu selected: no
safe to close Qa/SU3: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Repair_B_Chern_Weil_and_Operator_Test_v1
```
