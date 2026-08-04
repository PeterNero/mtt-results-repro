# MTT Selected HYM Uniform Spectral Convergence and Patching Certificate v1

## New theorem

The patching part is closed. The selected global extension form and positive
determinant-one metric determine the Chern connection functorially. On every
overlap,

```text
H_j = g_ij^dagger H_i g_ij
A_j = g_ij^-1 A_i g_ij + g_ij^-1 d g_ij
F_j = g_ij^-1 F_i g_ij
```

so the HYM residual patches by conjugation. There are no missing patchwise
connection coefficients.

## Nested Fourier execution

The selected nonlinear equation was solved independently at cutoffs
`12, 16, 20, 24, 28` and compared on the same phase-correct 32-grid. Successive
`L2` differences are:

```text
12->16: 7.2636485706104679e-08
16->20: 4.4151285566138080e-10
20->24: 2.8683042541053651e-12
24->28: 1.9678182946716621e-14
```

For the cutoff-24 solution, phase-correct dealiased evaluation on meshes
`28, 32, 36` gives a stable residual. At mesh 36:

```text
residual L2              = 1.1283045736204390e-10
coercivity lower bound   = 2.5876979532844523e+01
residual/coercivity      = 4.3602638097245126e-12
```

## Exact remaining boundary

This does not infer a continuum theorem from finitely many meshes. The only
remaining HYM object is an outward-rounded bound on the unresolved continuous
Fourier residual and nonlinear derivative tail, suitable for a
Newton-Kantorovich or radii-polynomial inequality. Once that scalar bound is
smaller than the certified coercive radius, continuum existence and local
uniqueness follow. The next artifact is
`MTT_Selected_HYMValidatedFourierResidualTailBound_v1`.
