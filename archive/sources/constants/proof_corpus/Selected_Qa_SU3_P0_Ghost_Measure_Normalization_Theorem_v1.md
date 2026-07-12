# Selected Qa/SU3 P0 Ghost Measure Normalization Theorem

## Purpose

The previous determinant table identified the remaining ambiguity as the
`p=0` ghost/measure treatment.  This note closes that ambiguity.

## Selected Rule

For central momentum `p=0`, the Nil oscillator sector reduces to the horizontal
two-torus sector.  For every nonzero horizontal scalar momentum, Hodge
decomposition gives:

```text
one exact longitudinal one-form
one co-closed transverse one-form
```

The gauge-fixing corpus identifies the Faddeev-Popov determinant as the
projection Jacobian for the gauge orbit.  Ghosts are the bookkeeping variables
for that quotient-measure Jacobian.  BRST cohomology then says physical states
are quotient classes modulo null redundancy.

Therefore the selected `p=0` rule is:

```text
longitudinal exact p=0 modes are cancelled by the ghost quotient,
harmonic zero modes are excluded from the primed threshold determinant,
the transverse p=0 sector is not an additional quotient Jacobian.
```

Equivalently:

```text
selected extra p=0 logdet correction = 0
```

## Numerical Effect

The scalar compact Nil diagnostic remains:

```text
scalar total = 3.8540439660345185
```

The selected p0 ghost/measure rule adds:

```text
0
```

So after closing the `p=0` ambiguity:

```text
selected total after p0 rule = 3.8540439660345185
required unweighted Qa      = 4.648486359430842
remaining gap               = 0.7944423933963232
```

This means the missing contribution is not a hidden `p=0` ghost normalization.

## Verdict

The `p=0` ghost/measure gate is now closed, but full Qa/SU3 closure remains
open.  The remaining problem has moved to the `p != 0` physical quotient
determinant:

```text
Selected_Qa_SU3_PNonzero_Physical_Quotient_Determinant_Theorem_v1
```

