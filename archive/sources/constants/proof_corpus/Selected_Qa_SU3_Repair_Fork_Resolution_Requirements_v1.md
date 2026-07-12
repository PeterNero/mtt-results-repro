# Selected Qa/SU3 Repair Fork Resolution Requirements v1

## Purpose

The repaired Qa/SU3 branch has split into two imperfect candidates.

This artifact computes what must be proven next before either candidate can be
used in a final determinant or Standard Model closure claim.

## Repair A Requirement

Repair A:

```text
B1 = E13,
B2 = -E31,
B3 = E11 - E33.
```

It restores integrability and passes the metric-weighted primitive contraction
diagnostic.  But the previous Hessian diagnostic found two zero modes, not just
the central `u(1)` zero.

Therefore Repair A can close only if:

```text
the extra noncentral null direction is source-certified as a legitimate
gauge/stabilizer quotient mode.
```

Without that quotient theorem, the extra zero mode is a real operator defect.

## Repair B Requirement

Repair B:

```text
B1 = E13,
B2 = -E32,
B3 = E12.
```

It restores integrability and preserves the expected Hessian rank.  But the
metric-weighted primitive contraction is nonzero.

Therefore Repair B can close only if:

```text
the full source-certified torsion/convention correction contributes exactly the
traceless diagonal primitive-cancelling term computed in the certificate,
or an equivalent weighted distribution across the diagonal F11 blocks.
```

That correction cannot be chosen from the desired Qa/SU3 threshold value.

## Consequence

The fork is now exact:

```text
Route A: prove extra zero is quotient.
Route B: source-certify primitive-cancelling torsion/convention correction.
```

Neither route is closed yet.

## Verdict

```text
route A closed: no
route B closed: no
fork resolved: no
safe to close Qa/SU3: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Repair_A_Quotient_Mode_or_Repair_B_Torsion_Source_Test_v1
```
