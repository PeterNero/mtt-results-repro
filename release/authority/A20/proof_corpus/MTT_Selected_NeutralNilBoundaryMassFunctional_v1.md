# MTT Selected Neutral Nil-Boundary Mass Functional v1

## Mathematical advance

For

```text
lambda_k = x + A cos(phi + 2*pi*k/3),   k=0,1,2,
```

the cosine sum vanishes, so `Tr(M_nu^dagger M_nu)=3x`. Positivity requires
`x >= -min_k A cos(...)`. Therefore minimizing the trace over the positive
domain has the unique solution

```text
x_* = -min_k A cos(phi + 2*pi*k/3),
min_k lambda_k = 0.
```

Thus neutral nil-boundary saturation would select `m_lightest=0` without a
continuous absolute-mass parameter.

Using the existing measured splittings only as downstream postchecks gives
`sum m_nu=0.0587843100473 eV` for NO and
`sum m_nu=0.101001237945 eV` for IO.

## Honest source boundary

The formula is proved, but source promotion is not. Three clauses remain:

1. bind nil-survivor minimization specifically to the neutral mass trace;
2. map selected retarded/nil phase data to NO or IO;
3. prove the selected action is Dirac-complete, or emit a separate Majorana
   operator with neutral character `k=0` or `k=672`.

The current selected action is Dirac-only; this is not yet a theorem that every
admissible extension forbids Majorana neutrinos.
