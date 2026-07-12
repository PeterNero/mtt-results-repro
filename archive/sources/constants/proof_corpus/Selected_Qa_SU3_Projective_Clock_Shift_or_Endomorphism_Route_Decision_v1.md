# Selected Qa/SU3 Projective Clock-Shift or Endomorphism Route Decision v1

## Purpose

The previous theorem closes the ordinary rank-one local-system bridge
negatively:

```text
q64=15 cannot be a rank-one U(1) compact-Nil central character,
q64=15 cannot be a scalar SU3 center element.
```

This note decides what remains.

## Projective Clock-Shift Route

The projective route is mathematically real.

Let

```text
omega = exp(2*pi*i/64).
```

On `C^64`, the finite clock and shift matrices can satisfy

```text
C S C^-1 S^-1 = omega I.
```

Replacing `C` by `C^15` realizes

```text
C^15 S C^-15 S^-1 = omega^15 I
                  = exp(2*pi*i*15/64) I.
```

So the order-64 phase survives as a nonabelian/projective finite Heisenberg
carrier.

But this is not yet Qa/SU3 closure.

The carrier is naturally a `64`-dimensional projective/U-type module.  Existing
visible-sector projective sources in the q79 corpus support qutrit/F3^2
twisted Chan-Paton and D7 structures.  Those are mostly order-3 visible-sector
statements, not a source-certified order-64 Qa/SU3 threshold operator.

Therefore:

```text
projective clock-shift route: open auxiliary branch
projective clock-shift route as current proof source: no
```

It would become a proof route only if a source theorem identifies this
projective carrier with the same Qa/SU3 BRST/HYM threshold complex and computes
the resulting determinant or torsion finite part.

## Endomorphism Route

The endomorphism route remains the physically aligned route:

```text
find selected endomorphism_E / zero-order Weitzenbock block / equivalent
selected threshold operator for Qa/SU3,
then compute its heat coefficient, spectrum, or torsion finite part.
```

This route is not closed either.  The explicit printed HYM matrix source has
been retired, and the rank-one local-system torsion branch is now blocked.  But
the endomorphism route targets the actual color-threshold operator, so it is the
primary next route.

## Decision

```text
primary next route:
  source-certified endomorphism_E / full Qa/SU3 threshold operator

conditional auxiliary route:
  projective clock-shift / twisted finite Heisenberg carrier

secondary backup:
  global section or fundamental-domain measure, only if proven distinct from
  the selected FP/BRST quotient normalization
```

## Guardrails

Do not use:

```text
qutrit/F3^2 projective Chan-Paton results as q64/U64 Qa/SU3 closure,
U64 clock-shift determinant as SU3 threshold determinant without an
operator-domain theorem,
projective carrier existence as analytic torsion finite part,
Qa/SU3 residual to choose the clock-shift dimension or normalization,
retired explicit HYM matrix entries as selected endomorphism_E data.
```

## Verdict

```text
Qa/SU3 closed: no
full SM closure achieved: no
target fitting used: no
projective q64 route killed: no
projective q64 route selected as proof source: no
endomorphism/operator source hunt is primary: yes
```

## Next Artifact

```text
Selected_Qa_SU3_Endomorphism_Source_Hunt_After_Torsion_No_Go_v1
```
