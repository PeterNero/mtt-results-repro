# MTT Selected PhiFin BN ModelActive Equivalence or SelectedMinimizerTrace v1

Status: `MTT_PHIFIN_BN_MODEL_ACTIVE_EQUIVALENCE_REJECTED_GAUGE_TRANSPORT_TRACE_REQUIRED`.

## Result

The exact untransported equivalence is rejected.

The model-active `B_N` packet is clean, but the selected diagonal End0 replay
emits

```text
D = d + du ad(T3)
```

with nonzero `du`:

```text
nonzero gradient directions = ['x1', 'x2', 'y1', 'y2']
```

Since `ad(T3)` acts nontrivially on the `T1/T2` plane, literal constant
`B_N` triplet modes cannot be the full selected covariant zero-mode triplet
before transport.

## Proof Boundary

This does not kill Route A.  It corrects it.

The previous T1/T2 covariant Green theorem already shows the selected diagonal
End0 lane is pure-gauge equivalent.  Therefore the correct `Phi_fin` trace is
not the raw model-active packet, but the gauge-transported packet:

```text
K_s^selected = exp(-u ad(T3)) K_s^model
P_s^selected = U P_s^model U^-1
```

with identity action on the protected `T3` and Higgs singlet lanes.

## What Must Be Proved Next

Emit the gauge-transported `B_N` trace and replay:

- selected transported zero-mode bases,
- selected transported projectors,
- Riesz/Green transfer,
- `dotD_alpha1` including derivative of the transport,
- validator payloads with theorem-derived source flags.

No observed constants, benchmark targets, or lifted selected flags are used.

Next artifact: `MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1`.
