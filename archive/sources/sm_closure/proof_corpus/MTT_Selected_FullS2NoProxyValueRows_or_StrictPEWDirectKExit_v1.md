# MTT Selected FullS2NoProxyValueRows or StrictPEWDirectKExit v1

## Theorem

`FirstSelectedDynamicValueRowAfterStep10Theorem` is emitted.

## What Closes

The old first-row rejection is replayed after Step10.  The internal source
failures are now resolved by the active Route-A source rule and the same-source
dynamic matter/overlap packet.

```text
old first-row rejection superseded = true
first selected dynamic matter/overlap value row accepted = true
accepted selected dynamic value row count = 2
VSD-01 first-response subrow closed = true
```

Accepted rows:

```text
VSD-01.phase.I_plus_Z.u.first_dynamic_row
VSD-01.phase.I_plus_Z.e.first_dynamic_row
```

Key invariants:

```text
u traceless norm^2 = 2.1828044769022577
e traceless norm^2 = 2.1828044769022577
CKM commutator norm^2 = 3.938117001379058
PMNS commutator norm^2 = 3.938117001379058
CP odd Im Tr([Hu,Hd]^3) = 1.5952446671165355
```

## Still Open

```text
VSD-01 full Yukawa magnitude rows closed = false
full S2 value rows closed = false
Yukawa/CKM/PMNS/Higgs no-proxy rows closed = false
strict P_EW source rows = 0
direct K_threshold.Omega_H.lambda rows = 0
true SM equivalence closed = false
full no-knob closure = false
```

## Next Artifact

`MTT_Selected_YukawaMagnitudeRowsFromSelectedDynamicPacket_or_ValueFunctionalGap_v1`.
