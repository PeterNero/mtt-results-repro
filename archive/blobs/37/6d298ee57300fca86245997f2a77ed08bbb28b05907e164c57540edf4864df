# Selected Qa/SU3 Repair Chern-Weil Operator Diagnostic v1

## Purpose

This tests the two repaired Qa/SU3 HYM connection candidates against the next
diagnostic gate.

Neither repair is source-certified.  This artifact is deliberately a guardrail:
it asks which repair survives the algebraic Chern-Weil and HYM primitive tests
before any final determinant calculation is attempted.

## Repairs Tested

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

Both use the original scaling:

```text
B1, B2 carry sqrt(mu),
B3 carries mu.
```

## Diagnostic Operator

For each repair, compute:

```text
F02_bar12 = B3 + [B1,B2],
F11_ij = [-B_i^*, B_j],
Lambda_J F = sum_i w_i F11_ii,
```

where the weights `w_i` are the selected Iwasawa one-form metric weights.

The script also computes algebraic coefficients for:

```text
Tr F,
Tr F wedge F,
Tr F wedge F wedge F.
```

These are not yet final published Chern-character normalizations; they are
matrix-valued invariant-form diagnostics.

## Result

The repairs split:

```text
Repair A restores integrability and passes the metric-weighted primitive
contraction diagnostic on the sampled positive mu values.

Repair B restores integrability and preserves the expected Hessian rank from
the previous gate, but fails the naive metric-weighted primitive contraction.
```

This is important because the previous artifact found:

```text
Repair A: extra Hessian zero mode,
Repair B: one central zero and eight positive modes.
```

So there is no single repaired branch that currently has all desired
properties.

## Consequence

The Qa/SU3 HYM branch is not closed.

The correct interpretation is:

```text
Repair A is geometrically better for the primitive/HYM diagnostic, but
operator-rank worse.

Repair B is operator-rank better, but primitive/HYM worse unless a sourced
torsional or convention correction changes the primitive contraction.
```

## Verdict

```text
source-certified repair found: no
Repair A closed: no
Repair B closed: no
mu selected: no
safe to close Qa/SU3: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Source_Certified_Connection_or_Full_Torsion_Primitive_Correction_v1
```
