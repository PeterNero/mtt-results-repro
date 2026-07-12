# Selected Qa/SU3 Final Obstruction or Projector Jacobian Resolution

## Purpose

This note records the final status of the compact-Nil Hodge/BRST branch for the
Qa/SU3 weak-split determinant.

## Fully Computed Branch

The following gates are now closed for this branch:

```text
compact Nil scalar spectrum: computed
co-closed Hodge one-form spectrum: sourced
Weitzenbock E: identified and not double-counted
p=0 ghost/measure rule: selected
p != 0 BRST physical quotient: selected
```

The selected result is:

```text
selected Qa = 4.8430192935084335
required Qa = 4.648486359430842
excess      = 0.19453293407759187
```

In weak-split form:

```text
selected lambda_12 = 2.210364204780355
target lambda_12   = 2.194153126940556
excess             = 0.01621107783979925
```

## Projector/Jacobian Resolution Test

To close this branch by a finite coherent projector/Jacobian, the missing
selected factor would have to be:

```text
log projector Jacobian = -0.19453293407759187
projector factor       = exp(-0.19453293407759187)
```

The current corpus does not select such a factor.  It provides:

```text
unit L2 harmonic normalization,
quotient-measure/Faddeev-Popov rules,
BRST cohomology rules,
canonical Nil overlap I3^(0)=c_nil.
```

None of these equals a selected finite coherent subtraction of the lowest-mode
excess.  Adding that subtraction by hand would be target fitting.

## Verdict

The compact-Nil Hodge/BRST branch is fully computed and obstructed as the final
no-knob Qa/SU3 closure.

This is not a vague failure.  It is a sharp theorem-level outcome:

```text
with the currently selected compact-Nil Hodge operator and BRST quotient,
Qa/SU3 overshoots by 0.19453293407759187.
```

Allowed next paths:

```text
1. derive a source-selected finite coherent projector/Jacobian before comparing to target,
2. replace the Qa/SU3 threshold operator with another corpus-selected operator and recompute,
3. keep compact-Nil Hodge as a near-miss diagnostic, not the final proof source.
```

Next artifact:

```text
Selected_Qa_SU3_Alternative_Operator_or_Projector_Source_Hunt_v1
```

