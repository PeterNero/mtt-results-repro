# BTT Exact Support Independence No-Go v1

## Result

The exact-support identity

```text
Pi_exact64 B^* P_TT = B^* P_TT
```

is independent of the currently sourced assumptions.

The current corpus and certificates close:

```text
B = DG(Psi*) Pi_coh,
Delta_TT = B A^{-1} B^* is nonzero on the physical TT quotient,
TT weight = 2,
BRST/diffeomorphism quotient compatibility,
the exact Z64 branch is coherent and available.
```

But these assumptions do not force the TT adjoint support to lie in the exact
`d_*` branch.

## Countermodel

Use a two-dimensional coherent internal toy support:

```text
e_exact = (1,0),
e_other = (0,1),
Pi_exact = diag(1,0),
A^{-1}=I.
```

Both choices

```text
B^*P_TT = e_exact
B^*P_TT = e_other
```

give the same kind of nonzero TT propagator:

```text
Delta_TT = ||B^*P_TT||^2 = 1.
```

Only the first satisfies `Pi_exact B^*P_TT = B^*P_TT`. Therefore nonzero TT
coupling plus exact-branch availability does not imply exact-branch support.

## Consequence

The final theorem cannot be proved from the current source set by algebraic
compression alone. One new ingredient is necessary:

```text
direct computation of DG(Psi*) on TT,
```

or

```text
a central-circle selection theorem proving TT adjoint support is exhausted by
the exact Z64 branch.
```

Once that ingredient is supplied, the existing uniqueness theorem immediately
returns `|d_*> tensor span{c_2,s_2}` and internal `lambda_GR,TT=15`.
