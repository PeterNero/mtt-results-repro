# Selected Qa/SU3 Canonical Bundle and Weitzenbock Data

## Purpose

The previous gate showed that Qa/SU3 can only continue through one of two
legal mechanisms:

```text
Path A: a selected physical projector or quotient-measure Jacobian
Path B: a selected curvature/Weitzenbock endomorphism in the gauge block
```

This note computes the canonical data available from the corpus for both paths.

## Selected Color Bundle

The SU3 color fiber is the compact Heisenberg nilmanifold
`Gamma\Nil_3` with isotropic horizontal metric:

```text
g = sigma_1^2 + sigma_2^2 + c_nil^2 sigma_3^2
```

where:

```text
sigma_1 = dx
sigma_2 = dy
sigma_3 = dz - x dy
c_nil   = 0.7766555403999195
```

The canonical massless color harmonics are the horizontal left-invariant
one-forms `dx` and `dy`.  The Route B twistor-action paper states that the
leading SU3 overlap is:

```text
I3^(0) = integral |chi_col|^2 dmu_nil = c_nil
```

Therefore the selected leading overlap is already known.  It is not the same
object as the missing determinant Jacobian.

## Path A Result

The selected overlap gives:

```text
I3^(0) = c_nil
-log(I3^(0)) = 0.25275834685845355
```

The remaining determinant gap is:

```text
required log-Jacobian = 0.7944423933963232
```

So the canonical leading overlap does not close the gap by itself.  A projector
closure would require a further selected quotient-measure theorem, for example a
determinant over additional physical quotient directions.  It cannot be inferred
from unit L2 projection alone.

## Path B Result

Use the orthonormal coframe:

```text
e1 = sigma_1
e2 = sigma_2
e3 = c_nil sigma_3
```

Then:

```text
de3 = -c_nil e1 wedge e2
```

For the 3D Heisenberg metric, the one-form Ricci/Weitzenbock endomorphism is:

```text
Ric(e1) = -(c_nil^2 / 2) e1
Ric(e2) = -(c_nil^2 / 2) e2
Ric(e3) = +(c_nil^2 / 2) e3
```

Numerically:

```text
c_nil^2 / 2 = 0.30159691421694546
c_nil^2     = 0.6031938284338909
```

For a horizontal harmonic one-form, the Hodge zero-mode condition is:

```text
Delta_Hodge omega = rough_laplacian omega + Ric(omega) = 0
```

and the script verifies:

```text
rough_laplacian horizontal contribution = +0.30159691421694546
Ric horizontal contribution             = -0.30159691421694546
Hodge total                              = 0
```

This identifies the selected Weitzenbock term, but it does not yet give the
finite determinant response of the full BRST physical gauge quotient.

## Gap Comparison

The closest geometry-derived diagnostic remains:

```text
-3 log(c_nil) = 0.7582750405753607
```

which misses the required gap by:

```text
0.036167352820962506
```

This is suggestive but not a proof.  The corpus selects `I3^(0)=c_nil`; it does
not yet select a three-direction determinant Jacobian `c_nil^-3`.

## Verdict

We have now computed the canonical SU3 Nil color bundle data and the canonical
one-form Weitzenbock endomorphism:

```text
color bundle selected: yes
projector overlap computed: yes
Weitzenbock E identified: yes
determinant closure: no
```

The remaining task is no longer to find a plausible curvature scale.  It is to
compute the finite determinant of the selected BRST physical Qa/SU3 operator
with this actual Weitzenbock term included:

```text
Selected_Qa_SU3_BRST_Physical_Determinant_With_Computed_Weitzenbock_E_v1
```

