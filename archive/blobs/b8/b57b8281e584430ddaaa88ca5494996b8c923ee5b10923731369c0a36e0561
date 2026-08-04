# Selected Qa/SU3 HYM Curvature Subblock Selector Test v1

## Purpose

The previous theorem ruled out all positive `mu`-independent torsion/OU
completion terms as possible selectors.  The remaining possibility is a
genuinely `mu`-dependent curvature or OU effect.

This artifact computes the directly available algebraic Chern-curvature
subblock from the printed HYM connection matrix.

## Scope

The source gives the explicit `(0,1)` connection coefficients `B_i`, and states
that the Chern curvature is nonzero, type `(1,1)`, with

```text
Tr F_E wedge F_E = 0,
c3(E)=6 a wedge b wedge c.
```

It does not print the full curvature matrix.  Therefore this artifact computes
only the connection-commutator part:

```text
C_ij(mu) = [-B_i^*, B_j].
```

This is not the full left-invariant curvature matrix, because derivative and
structure-equation terms involving `d omega^3` and `d bar omega^3` may also
contribute.

## Computation

Using the printed matrices,

```text
B1 ~ sqrt(mu),
B2 ~ sqrt(mu),
B3 ~ mu.
```

The total algebraic commutator-curvature norm is:

```text
sum_ij ||[-B_i^*,B_j]||_F^2
  = 2 mu^2 (mu^2 + mu + 2).
```

Its derivative is:

```text
8 mu^3 + 6 mu^2 + 8 mu.
```

This is strictly positive for every `mu > 0`.

Sample values:

```text
mu = 0.01: 0.00040202
mu = 0.1:  0.0422
mu = 0.25: 0.2890625
mu = 1:    8
mu = 4:    704
mu = 16:   140288
```

## Consequence

The simplest available curvature-strength invariant does not select an
interior `mu`.

Minimizing it runs toward `mu -> 0`; maximizing it runs toward `mu -> infinity`.
So this subblock cannot be the final selector unless another selected term
competes with it.

## Remaining Live Routes

The surviving routes are:

```text
compute the full left-invariant curvature matrix including d bar_omega^3 and d omega^3 structure terms,
derive how Tr F_E wedge F_E = 0 cancels at matrix level and whether a non-norm invariant remains,
derive mu-dependent OU eigenvalue weights from the full twisted operator rather than from curvature norm,
find a source-stated discrete stability/admissibility condition that fixes mu.
```

## Verdict

```text
curvature commutator subblock computed: yes
commutator curvature norm selects mu: no
full curvature matrix computed: no
full mu selection closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Full_Left_Invariant_Curvature_Matrix_v1
```
