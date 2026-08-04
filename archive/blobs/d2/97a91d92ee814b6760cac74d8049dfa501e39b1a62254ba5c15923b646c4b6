# MTT Selected HYM Connection to Finite Operator Extraction v1

## Claim

The extraction theorem is now formalized.  The abstract HYM existence result
does not by itself emit finite operator matrices.  The first selected `D_E`
emission attempt is blocked exactly at the missing gauge-fixed HYM connection
representative and the finite basis/quadrature/error contract for that
representative.

## Contract

The legal extraction chain is:

```text
selected AH/Cech V_alpha
+ selected equal-radius Gauduchon metric
+ selected gauge-fixed HYM connection A_HYM
+ selected finite basis/quadrature B_N
=> rho_E, metric, D_E, Riesz/Green, dotD, C1/overlap data
```

Smoke matrices and lifted selected flags remain validator-schema support only.
They cannot be copied into selected values.

## Next Computation

Build the selected gauge-fixed HYM representative, either analytically in the
selected AH/good-cover coordinates or numerically by a finite Newton/Galerkin
HYM solve with an a posteriori residual and truncation certificate.  Once that
representative exists, `D_E` is the first emitted operator, followed by
Riesz/Green, `dotD`, and C1/overlap tensors.
