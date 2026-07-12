# MTT Selected GaugeTransported BN PhiFin Trace v1

Status: `MTT_SELECTED_GAUGE_TRANSPORTED_BN_PHIFIN_TRACE_PROVED_FINITE_REPLAY_OPEN`.

## Theorem

The corrected `Phi_fin` trace is proved at the selected End0/HYM function-space
level:

```text
U = exp(-u ad(T3))
K_s^sel = U K_s^model
P_s^sel = U P_s^model U^-1
```

On `span(T1,T2)`, this is the pure-gauge identity already proved in the
T1/T2 Green theorem:

```text
D = exp(-uJ) d exp(uJ)
D(U psi) = U d psi
```

The `T3` lane is protected because `ad(T3)T3=0`, and `H` is the trivial
singlet.  Therefore the model-active `B_N` zero cluster becomes the selected
diagonal End0 zero-mode trace after gauge transport.  Rank, gap, Riesz
projector, and Green operator transfer by unitary conjugation.

## What This Closes

- selected functional zero-mode bases,
- selected functional projectors,
- functional promotion of `rho_candidate` to selected `rho_s`,
- corrected Route A `Phi_fin` trace formula.

## What Remains

This is not yet finite validator replay.  Multiplication by `exp(-uJ)` is not
closed inside the raw 27-mode `B_N` truncation; the prior direct truncated
relative residual was

```text
0.23373530261576297
```

So the next gate is a transport-closed finite basis or symbolic
transport-conjugation validator replay.  `dotD_alpha1` also still needs the
derivative of the transport and the selected alpha1 driver.

No observed constants, benchmark targets, or lifted selected flags are used.

Next artifact: `MTT_Selected_TransportClosed_BN_Basis_or_ValidatorReplay_v1`.
