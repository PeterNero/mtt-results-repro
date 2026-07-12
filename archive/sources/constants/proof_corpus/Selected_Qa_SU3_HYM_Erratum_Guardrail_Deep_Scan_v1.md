# Selected Qa/SU3 HYM Erratum Guardrail Deep Scan v1

## Purpose

This note prevents premature closure of the Qa/SU3 HYM branch.

The previous erratum scan found that simple sign/transpose conventions do not
repair the printed connection.  It also identified a diagonal `B3` replacement.
That repair is valid only under the extra assumption that `B1` and `B2` remain
exactly as printed.

Here we explore whether other small algebraic repairs exist.

## Sparse Integrability Scan

Keep the printed

```text
B3 = E12.
```

Search all signed elementary matrices `B1,B2` satisfying

```text
E12 + [B1,B2] = 0.
```

The scan finds 12 sparse solutions.  The key one is:

```text
B1 = E13,
B2 = -E32,
B3 = E12.
```

This means that if the printed `B1=E13` and `B3=E12` are kept, integrability is
restored by moving the printed `B2` entry:

```text
from  -E31
to    -E32.
```

That is a one-entry move, and it may be a more plausible textual erratum than
replacing `B3` with a diagonal matrix.

## Repair Options

There are now at least two plausible algebraic repairs:

```text
Repair A:
  keep B1=E13 and B2=-E31,
  replace B3=E12 by B3=E11-E33.

Repair B:
  keep B1=E13 and B3=E12,
  replace B2=-E31 by B2=-E32.
```

No simple sparse repair keeps the printed `B2=-E31` and `B3=E12` while changing
only `B1`.

## Guardrail

The diagonal `B3` repair must not be treated as uniquely selected.  It is only
unique under the constraint:

```text
B1 and B2 are held fixed exactly as printed.
```

The one-entry `B2` move is also not source-certified.  Neither repair can be
used for final Qa/SU3 closure until it is checked against the surrounding source
claims:

```text
holomorphicity,
SU(3) trace condition,
Tr F wedge F = 0,
c3(E)=6 a wedge b wedge c,
Hessian positivity,
mu-selection behavior,
compatibility with the selected threshold operator.
```

## Safe Way Forward

The correct next step is diagnostic comparison:

```text
run repaired pipeline A and repaired pipeline B,
compare integrability, curvature invariants, Hessian blocks, and mu behavior,
do not claim either repair as source-certified without corpus evidence.
```

## Verdict

```text
diagonal B3 repair uniquely selected without qualification: no
one-entry B2 move repair exists: yes
any repair source-certified: no
safe to close Qa/SU3 from repair now: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Repaired_Pipeline_A_B_Diagnostic_Comparison_v1
```
