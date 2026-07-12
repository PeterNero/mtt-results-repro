# MTT Selected HWeightedFinitePartCoefficientSearch or MeshWindowNoGo v1

## Theorem

`FinitePartCoefficientInverseSearchAndMeshWindowNoGoTheorem` is emitted.

## Result

The selected HYM anisotropy family is:

```text
tau_H(k) = 4 + (x1_l2/y1_l2)/(3 - k*s_beta)
```

Using the controlled H frontier value:

```text
tau_H = 4.018017196377461
x1_l2/y1_l2 = 0.0537483972081464
s_beta = 0.004701083905943647
k_required = 3.579582815935827
```

The best bounded rational near miss is:

```text
k = 25/7 = 3.5714285714285716
tau_H(k) = 4.018016964859304
relative residual = 5.76200016622163e-08
```

Accepted finite-part coefficient source rows: `0`.

## No-Go Guard

The near miss is not promoted. It is scan-derived, and its numerator equals
`mesh + 1 = 25` and `2*theta_series_cutoff + 1 = 25`
in the current replay window. This may be real MTT window arithmetic, but it is
not yet a source theorem.

## Next Object

`MTT_Selected_FinitePartCoefficientSourceRule_or_DirectRadialOperator_v1` must emit the H-weighted finite-part coefficient, prove
mesh-independence or a continuum normalization, and export `tau_H` or `r_H` from
the same selected source.
