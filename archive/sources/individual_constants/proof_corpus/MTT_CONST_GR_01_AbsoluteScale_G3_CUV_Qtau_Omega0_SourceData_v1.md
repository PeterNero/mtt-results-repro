# MTT CONST GR 01 Absolute Scale G3 CUV Q_tau Omega0 Source Data v1

Status: `MTT_CONST_GR_01_G3_CUV_QTAU_OMEGA0_SOURCE_DATA_BUILT`

Label: `CONST-GR-01 / ABSOLUTE-SCALE-GN / G3-CUV-QTAU-OMEGA0-SOURCE-DATA`

## Result

```text
internal C_UV/Q_tau ratio usable as shared scale data   True
selected q64=15 character premise explicit             True
literal GR-TT noise-channel identity                   False
active physical unit gate                              Omega0 or E0/L0
Newton/Planck prediction                               False
```

G3 splits the G2 blocker.  The selected character-channel import gives:

```text
q64                 = 15
d_Q                 = 1
C_UV_internal       = 0.405623467693425
rho_UV              = 0.164530397543639
s_star              = 1.464646774701829
```

That is enough for shared internal scale propagation under the explicit
character-channel premise.  It is not a physical unit.

## Active Physical Gate

```text
Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))
omega_gap_phys = Omega0 / s_star
Lambda_gap_phys = sqrt(15) * Omega0 / s_star
```

So the active absolute-scale blocker is `Omega0`, or equivalently the same
`E0/L0` metrological primitive already isolated by alpha and weak mixing.

## Parked Strict Upgrade

The strict provenance upgrade is:

```text
GR_TT_Stochastic_Channel_Equals_Selected_CP_Character_Theorem_v1
```

This would strengthen the GR-specific source story, but it is not the same as
selecting the physical length/action unit.

## Next

`CONST-GR-01 / ABSOLUTE-SCALE-GN / G4-OMEGA0-PHYSICAL-UNIT-OR-ONE-METROLOGY-PRIMITIVE`
