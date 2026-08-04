# MTT Selected Ext L2 Theta Quadrature Table v1

## Result

For the selected row

```text
eta_00 = Theta_{2,0}(z1; i) tensor Eta_{-4,0}(z2; i) dbar_z2
```

the canonical Appell-Humbert theta metric at `tau=i` gives:

```text
||Theta_{d,k}||^2 = 1/sqrt(2*d)
||eta_00||^2 = (1/sqrt(4))*(1/sqrt(8)) = 1/sqrt(32)
```

Therefore the unit `L2` representative is:

```text
eta_00^unit = 32^(1/4) * eta_00
```

## Derivation

Use the standard basis

```text
Theta_{d,k}(z)=sum_n exp(-pi*d*(n+k/d)^2 + 2*pi*i*d*(n+k/d)*z)
```

with Hermitian weight

```text
h_d(y)=exp(-2*pi*d*y^2).
```

The integral over `x in [0,1]` kills the off-diagonal Fourier terms. Completing
the square in `y` unfolds the remaining shifted lattice sum into the Gaussian
real-line integral, giving `1/sqrt(2*d)` in this metric convention.

The negative-degree factor is interpreted by Serre duality as the positive
degree-4 theta norm for the dual representative. The shared circle contributes
degree zero and factor `1`.

## What This Closes

This closes the exact `L2` theta normalization and emits a reproducible
quadrature convergence table for `eta_00`.

## Guardrail

This still does not emit transition-overlap trivialization values, a global
partition-of-unity or harmonic Dolbeault representative, the selected HYM
metric correction, Hodge/Lambda tables, or gauge projectors. The row is
normalized, but the End0 Newton/Galerkin solve is not yet ready.

## Next Artifact

`MTT_Selected_Ext_Overlap_HYM_Hodge_Projector_Table_v1`.
