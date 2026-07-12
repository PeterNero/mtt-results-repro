# Selected Qa/SU3 Repair B Primitive Correction No-Go v1

## Purpose

Repair B is now the only live algebraic repair branch.  This artifact asks
whether the currently available corpus can source the primitive-cancelling term
that Repair B needs.

## Required Correction

For Repair B, the metric-weighted primitive obstruction is:

```text
(w1 mu + w3 mu^2) diag(1,-1,0).
```

Therefore the missing source term must contribute:

```text
-(w1 mu + w3 mu^2) diag(1,-1,0).
```

This is a precise requirement.  It is not just "some torsion" or "some OU
weight"; it must be:

```text
an SU3 color endomorphism or torsion correction,
with Cartan shape diag(-1,1,0),
with mu and mu^2 dependence tied to the same Repair B HYM family,
derived independently of the target threshold value.
```

## Current Source Tests

The currently available source terms do not supply this.

```text
R_+ gravitational curvature:
  rejected; gravitational alpha1 data, not SU3 color Cartan endomorphism.

heterotic abelian flux coefficients:
  rejected; anomaly-level coefficient data, not the Repair B primitive correction.

mu-independent torsion or OU lift:
  rejected by the existing mu-independent completion no-go.

scalar OU variance/damping weights:
  rejected; scalar weights cannot add a traceless color Cartan correction
  without a selected color endomorphism.

stored color endomorphism_E:
  rejected; current template has endomorphism_E = null.

pure sign, transpose, or wedge convention:
  rejected; conventions do not source the required
  -(w1 mu + w3 mu^2) diag(1,-1,0) term.
```

## No-Go Scope

This no-go is deliberately scoped:

```text
proved for current corpus sources: yes
proved for future new source: no
proved for changed selected branch: no
```

So Repair B is not mathematically impossible.  It is blocked by the current
source record.

## Future Escape Hatches

Repair B can still be revived if one of these is found:

```text
1. an explicit source-certified HYM curvature matrix for Repair B whose full
   Chern-Weil primitive includes the missing term,

2. a selected Strominger/Dirac/Weitzenbock endomorphism_E with exactly the
   required Cartan and mu dependence,

3. a source-certified erratum replacing the displayed HYM matrix,

4. or a decision to retire the explicit HYM-matrix route and return to compact
   Nil/local-system determinant routes.
```

## Verdict

```text
Repair B primitive correction source-certified now: no
Repair B current-source no-go: yes
Repair B mathematically impossible: no
safe to close Qa/SU3: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Explicit_Source_Certified_Connection_or_Route_Retirement_v1
```
