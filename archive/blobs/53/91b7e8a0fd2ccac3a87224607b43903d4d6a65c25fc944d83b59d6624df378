# MTT Selected T1T2 Covariant Green or Rank2 Sector Transfer From Diagonal HYM v1

## Path A: Straight End0 Calculation

The coupled `T1/T2` block converges.  On `span(T1,T2)`:

```text
D_a = partial_a I_2 + (partial_a u) J
J = [[0,-1],[1,0]]
```

Since `A=du*J`, the connection is globally pure gauge:

```text
D = exp(-uJ) d exp(uJ)
```

Therefore:

```text
P_D f = exp(-uJ) mean(exp(uJ) f)
G_D f = exp(-uJ) (-Delta)^(-1) Q mean-zero(exp(uJ) f)
```

The deterministic replay gives:

```text
||(-Delta)GQ(exp(uJ)f) - Q(exp(uJ)f)||_L2 = 8.863e-16
```

Together with the protected `T3` lane, this closes the full diagonal End0
Riesz/Green packet.

The direct finite spectral replay in the ungauged frame is diagnostic only:
its residual is `2.337e-01` because finite Fourier
products with `exp(uJ)` alias outside the truncation.  The promotion is by the
global pure-gauge theorem, not by this truncated product replay.

## Path B: Superset Sector Transfer

The transfer path does not promote yet.  The abstract `End0(V_alpha)` rank-3
carrier is legal, but the current `B_N`/qutrit scaffold is explicitly rejected
as the selected End0 basis, and no selected End0-to-sector routing values are
emitted.

## Guardrail

This is still not full validator-ready SM-sector data.  The physical
same-branch `dotD_alpha1`, rank2-to-sector transfer values, and off-diagonal
Ext/HYM control theorem remain open.

## Next Artifact

`MTT_Selected_OffDiagonal_Ext_Control_or_SectorTransfer_From_Full_Diagonal_End0_Green_v1`.
