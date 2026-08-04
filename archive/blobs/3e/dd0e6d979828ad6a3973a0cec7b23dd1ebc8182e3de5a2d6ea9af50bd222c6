# Selected Qa/SU3 BRST Determinant With Computed Weitzenbock E

## Purpose

The canonical Nil color bundle computation identified the one-form
Weitzenbock/Ricci endomorphism.  The next question is whether including this
term closes the Qa/SU3 determinant.

The answer is precise:

```text
the sourced co-closed one-form spectrum is already the Hodge one-form spectrum,
so the Weitzenbock term is already included there.
```

Therefore `E_Qa` must not be added a second time as a free shift.

## Data Used

The scalar compact Nil diagnostic gives:

```text
p0 scalar finite part        = 4.466165438656482
p != 0 scalar finite part    = -0.6121214726219636
scalar total                 = 3.8540439660345185
```

The sourced co-closed Hodge one-form spectrum gives:

```text
p != 0 co-closed one-form finite part = -3.2021936001917566
lowest scalar mode finite part        = 0.9889753274739147
```

The required selected Qa value after Qc/SU2 closure is:

```text
required unweighted Qa = 4.648486359430842
remaining scalar gap   = 0.7944423933963232
```

## Weitzenbock Inclusion

The computed Nil one-form Ricci block is:

```text
Ric(e1) = -0.30159691421694546
Ric(e2) = -0.30159691421694546
Ric(e3) = +0.30159691421694546
```

The p != 0 co-closed one-form formula from the sourced spectrum is a Hodge
one-form formula.  Thus it already contains the curvature endomorphism.

So the valid move is:

```text
use the sourced one-form determinant as the E-included determinant
```

and the invalid move is:

```text
add c_nil^2/2, c_nil^2, or another curvature scalar on top
```

## BRST Bookkeeping Table

The script compares the following families:

```text
scalar proxy only
scalar proxy plus previous natural p != 0 quotient candidate
p0 transverse two-torus diagnostics
p != 0 co-closed/ghost quotient diagnostics
```

The `p=0` sector is the unresolved part.  At central momentum zero, the
horizontal co-closed quotient on the two-torus has one transverse representative
per nonzero scalar mode, so its determinant finite part equals the scalar p0
finite part.  What remains source-open is the BRST measure rule: whether the
ghost determinant cancels this sector, leaves it, or leaves a half-density.

## Verdict

The Weitzenbock term has now been included without double counting.

This does not close Qa/SU3.  The remaining missing theorem is narrower:

```text
Selected_Qa_SU3_P0_Ghost_Measure_Normalization_Theorem_v1
```

It must select the `p=0` gauge/ghost measure and zero-mode treatment before the
finite determinant can be called a proof.

