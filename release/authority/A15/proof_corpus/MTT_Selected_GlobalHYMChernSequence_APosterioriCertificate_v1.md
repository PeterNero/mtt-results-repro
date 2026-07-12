# MTT Selected Global HYM Chern-Sequence A-Posteriori Certificate v1

## Advance

The selected global harmonic extension form and the positive determinant-one
metric sequence determine a unique Chern-connection sequence. The offdiagonal
connection is fixed by `eta_00^unit` and its metric adjoint; it is not an
unknown free coefficient. The diagonal component is `du*T3`.

At the selected `24^4` projected level:

```text
HYM residual L2                    = 8.208178923714022e-13
tail contraction ratio            < 0.486
zero-mean Poincare lambda_1        = 4*pi^2
maximum nonlinear density         = 6.729860855740695
linearized coercivity lower bound = 26.018695892876043
residual/coercivity indicator      = 3.1547234179255825e-14
```

This proves local uniqueness and stability of the finite projected solution.

## Remaining Guard

One mesh residual is not a continuum theorem. Literal global HYM closure still
requires a uniform mesh/theta-cutoff convergence and patchwise residual bound,
or a fully specified constructive Donaldson/balanced-metric convergence theorem
for this selected non-split Gauduchon bundle. U2 remains `1/2`, but its HYM half
is now reduced to a continuum certificate rather than unknown connection data.
